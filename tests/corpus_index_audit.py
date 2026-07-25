#!/usr/bin/env python3
"""Audit that every web2app-essentials module is indexed and routable.

The web2app-essentials skill only ever loads module files through two entry
points: the routing table in `SKILL.md` and the index in
`references/README.md`. A module file that exists on disk but is missing from
either is invisible at runtime — the skill never reads it, so the knowledge
silently drops out of answers. Scheduled corpus updates keep adding module
files, which makes this the most likely drift.

The link-resolution audit (`reference_links_audit.py`) catches the opposite
failure (a listed path that no longer exists); this audit catches orphans.

Exit code 0 when every module file is indexed in both places, 1 with one line
per gap otherwise.
"""

import sys
from pathlib import Path

SKILL_DIR = "skills/web2app-essentials"


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
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    errors = audit(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"FAIL: {len(errors)} unindexed corpus module(s)", file=sys.stderr)
        return 1
    print("PASS: every web2app-essentials module is indexed and routable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
