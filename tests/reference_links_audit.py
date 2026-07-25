#!/usr/bin/env python3
"""Audit that documentation cross-references resolve to real files.

Scheduled corpus reorganizations keep moving reference files; a stale path in
a SKILL.md or an index README fails silently at runtime (the skill tells the
agent to stop when a reference is missing). This audit catches those breaks
in CI instead. Two classes of links are checked:

1. Backticked `references/...` paths inside every `skills/*/SKILL.md` must
   exist relative to that skill's directory. A path ending in `/` must be a
   directory; anything else must be a file.
2. Relative markdown links in every `skills/**/README.md` index must resolve
   relative to the README's own directory (external URLs and anchors are
   ignored).

Exit code 0 when every link resolves, 1 with one line per broken link
otherwise.
"""

import re
import sys
from pathlib import Path

BACKTICK_REF = re.compile(r"`(references/[^`\s]*)`")
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "#")


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


def audit_readme(readme: Path) -> list[str]:
    errors = []
    base = readme.parent
    for link in MARKDOWN_LINK.findall(readme.read_text(encoding="utf-8")):
        if link.startswith(EXTERNAL_PREFIXES):
            continue
        target_path = link.split("#", 1)[0]
        if not target_path:
            continue
        target = base / target_path
        if not (target.is_file() or target.is_dir()):
            errors.append(f"{readme}: broken relative link `{link}`")
    return errors


def audit(root: Path) -> list[str]:
    errors = []
    for skill_md in sorted(root.glob("skills/*/SKILL.md")):
        errors.extend(audit_skill_md(skill_md))
    for readme in sorted(root.glob("skills/**/README.md")):
        errors.extend(audit_readme(readme))
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
