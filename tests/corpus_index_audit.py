#!/usr/bin/env python3
"""Audit that every corpus file is indexed and routable.

Two corpora are checked, both against the same failure class: a file that
exists on disk but is missing from its index is invisible at runtime — the
skill never reads it, so the knowledge silently drops out of answers.
Scheduled corpus updates keep adding files, which makes this the most likely
drift.

1. **web2app-essentials modules.** The skill only ever loads module files
   through two entry points: the routing table in `SKILL.md` and the index in
   `references/README.md`. Every `references/*/*.md` must appear in both.
2. **writing-funnel-copy research corpus.** The skill routes agents through
   `references/funnels-research/README.md` and tells them to "load only the
   relevant files" — so every markdown file in that tree must be linked from
   the `README.md` of its own directory, and every directory holding markdown
   files must have a `README.md` index. (This audit found a fully orphaned
   cross-funnel copy bank when it was introduced.)

The link-resolution audit (`reference_links_audit.py`) catches the opposite
failure (a listed path that no longer exists); this audit catches orphans.

Exit code 0 when every file is indexed, 1 with one line per gap otherwise.
"""

import sys
from pathlib import Path

SKILL_DIR = "skills/web2app-essentials"
RESEARCH_CORPUS_DIR = "skills/writing-funnel-copy/references/funnels-research"


def find_modules(skill_root: Path) -> list[str]:
    """Module files, as paths relative to `references/` (e.g. `1-x/1.1-y.md`)."""
    references = skill_root / "references"
    return sorted(
        str(path.relative_to(references))
        for path in references.glob("*/*.md")
    )


def audit_readme_index(readme_text: str, modules: list[str]) -> list[str]:
    return [
        f"references/README.md does not index `{module}`"
        for module in modules
        if f"({module})" not in readme_text
    ]


def audit_routing_table(skill_text: str, modules: list[str]) -> list[str]:
    return [
        f"SKILL.md routing table does not route to `references/{module}`"
        for module in modules
        if f"`references/{module}`" not in skill_text
    ]


def audit_research_corpus(root: Path) -> list[str]:
    """Every .md in the research corpus must be linked from its own dir's README."""
    corpus = root / RESEARCH_CORPUS_DIR
    if not corpus.is_dir():
        return [f"{RESEARCH_CORPUS_DIR}: research corpus directory not found"]
    errors = []
    for directory in sorted(
        {path.parent for path in corpus.rglob("*.md")}
    ):
        rel_dir = directory.relative_to(root)
        readme = directory / "README.md"
        if not readme.is_file():
            errors.append(f"{rel_dir}: directory has markdown files but no README.md index")
            continue
        readme_text = readme.read_text(encoding="utf-8")
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            if f"({path.name})" not in readme_text:
                errors.append(f"{rel_dir}/README.md does not index `{path.name}`")
    return errors


def audit(root: Path) -> list[str]:
    skill_root = root / SKILL_DIR
    modules = find_modules(skill_root)
    if not modules:
        return [f"{SKILL_DIR}: no module files found under references/"]
    readme_text = (skill_root / "references/README.md").read_text(encoding="utf-8")
    skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
    errors = [
        f"{SKILL_DIR}/{error}"
        for error in audit_readme_index(readme_text, modules)
        + audit_routing_table(skill_text, modules)
    ]
    errors.extend(audit_research_corpus(root))
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    errors = audit(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"FAIL: {len(errors)} unindexed corpus file(s)", file=sys.stderr)
        return 1
    print("PASS: every corpus file is indexed and routable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
