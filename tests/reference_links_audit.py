#!/usr/bin/env python3
"""Audit that documentation cross-references resolve to real files.

Scheduled corpus reorganizations keep moving reference files; a stale path in
a SKILL.md or an index README fails silently at runtime (the skill tells the
agent to stop when a reference is missing). This audit catches those breaks
in CI instead. Three classes of links are checked:

1. Backticked `references/...` paths inside every `skills/*/SKILL.md` must
   exist relative to that skill's directory. A path ending in `/` must be a
   directory; anything else must be a file.
2. Relative markdown links in every markdown file under `skills/` and
   `docs/`, plus the root `README.md`, must resolve relative to the file's
   own directory (external URLs are ignored, as are links inside fenced
   code blocks).
3. Anchor fragments must resolve: a `#fragment` on a relative link to a
   markdown file (or a same-file `#fragment` link) must match a heading in
   the target, using GitHub-style slugs with `-N` suffixes for duplicate
   headings.

Exit code 0 when every link resolves, 1 with one line per broken link
otherwise.
"""

import re
import sys
from pathlib import Path

BACKTICK_REF = re.compile(r"`(references/[^`\s]*)`")
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"#{1,6}\s+(.*)")
CODE_FENCE = re.compile(r"\s*(```|~~~)")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:")


def audit_skill_md(skill_md: Path) -> list[str]:
    errors = []
    base = skill_md.parent
    for ref in BACKTICK_REF.findall(skill_md.read_text(encoding="utf-8")):
        target = base / ref
        if ref.endswith("/"):
            if not target.is_dir():
                errors.append(f"{skill_md}: missing directory `{ref}`")
        elif not target.is_file():
            errors.append(f"{skill_md}: missing file `{ref}`")
    return errors


def strip_code_fences(text: str) -> str:
    kept = []
    in_fence = False
    for line in text.splitlines():
        if CODE_FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            kept.append(line)
    return "\n".join(kept)


def slugify(heading: str) -> str:
    text = re.sub(r"[`*_]", "", heading.strip().lower())
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def heading_slugs(markdown: str) -> set[str]:
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    for line in strip_code_fences(markdown).splitlines():
        match = HEADING.match(line)
        if not match:
            continue
        slug = slugify(match.group(1))
        seen = counts.get(slug, 0)
        counts[slug] = seen + 1
        slugs.add(slug if seen == 0 else f"{slug}-{seen}")
    return slugs


def audit_markdown(md_file: Path) -> list[str]:
    errors = []
    base = md_file.parent
    text = md_file.read_text(encoding="utf-8")
    for link in MARKDOWN_LINK.findall(strip_code_fences(text)):
        if link.startswith(EXTERNAL_PREFIXES):
            continue
        target_path, _, fragment = link.partition("#")
        target = base / target_path if target_path else md_file
        if target_path and not (target.is_file() or target.is_dir()):
            errors.append(f"{md_file}: broken relative link `{link}`")
            continue
        if fragment and target.is_file() and target.suffix == ".md":
            slugs = heading_slugs(target.read_text(encoding="utf-8"))
            if slugify(fragment) not in slugs:
                errors.append(f"{md_file}: broken anchor `{link}`")
    return errors


def markdown_files(root: Path) -> list[Path]:
    files = set(root.glob("skills/**/*.md")) | set(root.glob("docs/**/*.md"))
    readme = root / "README.md"
    if readme.is_file():
        files.add(readme)
    return sorted(files)


def audit(root: Path) -> list[str]:
    errors = []
    for skill_md in sorted(root.glob("skills/*/SKILL.md")):
        errors.extend(audit_skill_md(skill_md))
    for md_file in markdown_files(root):
        errors.extend(audit_markdown(md_file))
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    errors = audit(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"FAIL: {len(errors)} broken reference link(s)", file=sys.stderr)
        return 1
    print("PASS: all skill reference links resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
