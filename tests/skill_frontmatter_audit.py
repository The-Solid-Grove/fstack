#!/usr/bin/env python3
"""Audit SKILL.md frontmatter discipline across every skill in the pack.

Skill routing in both host agents is driven entirely by the `name` and
`description` frontmatter of each `skills/*/SKILL.md`. A malformed or
misleading description silently breaks routing: the skill still installs, but
the agent stops picking it when it should (or picks it when it should not).
This audit enforces the pack's frontmatter contract mechanically:

1. The file starts with a `---` frontmatter block containing `name:` and
   `description:` as single-line values.
2. `name` equals the skill's directory name and is kebab-case.
3. `description` starts with "Use when" (the routing convention every skill
   in this pack follows), and is neither a stub (< 40 chars) nor over the
   1024-char limit hosts truncate at.
4. `description` names no specific host agent (Codex, Claude, Cursor,
   Copilot, Gemini). fstack installs the same skill into multiple hosts, so
   the routing text must stay host-agnostic; host-specific phrasing belongs
   in per-host config such as `agents/openai.yaml`.

Exit code 0 when every skill conforms, 1 with one line per violation.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKILLS_DIR = "skills"
KEBAB_CASE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HOST_AGENT_NAMES = re.compile(r"\b(Codex|Claude|Cursor|Copilot|Gemini)\b", re.IGNORECASE)
DESCRIPTION_MIN = 40
DESCRIPTION_MAX = 1024


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Single-line `key: value` pairs from a leading --- block, else None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        match = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return None


def audit_skill(skill_dir: Path) -> list[str]:
    rel = f"{SKILLS_DIR}/{skill_dir.name}/SKILL.md"
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"{rel}: missing SKILL.md"]

    fields = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    if fields is None:
        return [f"{rel}: no closed --- frontmatter block at top of file"]

    errors = []
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        errors.append(f"{rel}: frontmatter has no single-line `name:` value")
    else:
        if name != skill_dir.name:
            errors.append(
                f"{rel}: name `{name}` does not match directory `{skill_dir.name}`"
            )
        if not KEBAB_CASE.match(name):
            errors.append(f"{rel}: name `{name}` is not kebab-case")

    if not description:
        errors.append(f"{rel}: frontmatter has no single-line `description:` value")
    else:
        if not description.startswith("Use when"):
            errors.append(f"{rel}: description does not start with 'Use when'")
        if len(description) < DESCRIPTION_MIN:
            errors.append(
                f"{rel}: description is a stub ({len(description)} chars,"
                f" minimum {DESCRIPTION_MIN})"
            )
        if len(description) > DESCRIPTION_MAX:
            errors.append(
                f"{rel}: description too long ({len(description)} chars,"
                f" maximum {DESCRIPTION_MAX})"
            )
        host_match = HOST_AGENT_NAMES.search(description)
        if host_match:
            errors.append(
                f"{rel}: description names host agent `{host_match.group(0)}`;"
                " routing text must be host-agnostic"
            )
    return errors


def audit(root: Path) -> list[str]:
    skills_root = root / SKILLS_DIR
    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skill_dirs:
        return [f"{SKILLS_DIR}: no skill directories found"]
    return [error for skill_dir in skill_dirs for error in audit_skill(skill_dir)]


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    errors = audit(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"FAIL: {len(errors)} skill frontmatter violation(s)", file=sys.stderr)
        return 1
    print("PASS: every SKILL.md frontmatter conforms to the routing contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
