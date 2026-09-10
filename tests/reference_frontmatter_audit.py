#!/usr/bin/env python3
"""Audit the YAML frontmatter on writing-funnel-copy reference files.

The top-level references in `skills/writing-funnel-copy/references/` carry
routing frontmatter (`id`, `title`, `summary`, `intents`) that mirrors the
routing prose in SKILL.md. The convention has already drifted once: one file
shipped with `description`/`version` and no title or intents, so an agent
scanning frontmatter to pick references saw an inconsistent contract. This
audit locks the convention for the files that opted into it.

Scope is deliberately narrow: only direct children of the writing-funnel-copy
references directory. The `funnels-research/` corpus below it and the
web2app-essentials modules use different conventions with their own audits.

Checks per file:

1. A closed `---` frontmatter block at the top of the file.
2. `id:` present and equal to the filename stem.
3. `title:` and `summary:` present and non-empty.
4. `intents:` present with at least one entry, every entry from the known
   vocabulary (catches typos like `implment`).

Extra fields (`version`, `keywords`, `always_load`, ...) are allowed.
Exit code 0 when every file conforms, 1 with one line per violation.
"""

import re
import sys
from pathlib import Path

REFERENCES_DIR = "skills/writing-funnel-copy/references"
ALLOWED_INTENTS = {"research", "plan", "implement", "edit", "qa", "publish"}
SCALAR_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
LIST_ITEM_RE = re.compile(r"^\s+-\s+(.+?)\s*$")


def parse_frontmatter(text: str) -> dict | None:
    """Return {key: scalar-or-list} for the leading frontmatter, else None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields: dict = {}
    current_list_key = None
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        item = LIST_ITEM_RE.match(line)
        if item and current_list_key is not None:
            fields[current_list_key].append(item.group(1))
            continue
        scalar = SCALAR_RE.match(line)
        if scalar:
            key, value = scalar.group(1), scalar.group(2).strip()
            if value:
                fields[key] = value
                current_list_key = None
            else:
                fields[key] = []
                current_list_key = key
    return None  # never closed


def audit_file(path: Path, rel: str) -> list[str]:
    fields = parse_frontmatter(path.read_text(encoding="utf-8"))
    if fields is None:
        return [f"{rel}: missing or unclosed `---` frontmatter block"]
    errors = []
    stem = path.stem
    if fields.get("id") != stem:
        errors.append(
            f"{rel}: frontmatter `id` must be `{stem}`, got `{fields.get('id')}`"
        )
    for key in ("title", "summary"):
        value = fields.get(key)
        if not value or not isinstance(value, str):
            errors.append(f"{rel}: frontmatter `{key}` is missing or empty")
    intents = fields.get("intents")
    if not isinstance(intents, list) or not intents:
        errors.append(f"{rel}: frontmatter `intents` must list at least one intent")
    else:
        for intent in intents:
            if intent not in ALLOWED_INTENTS:
                errors.append(
                    f"{rel}: unknown intent `{intent}` "
                    f"(allowed: {', '.join(sorted(ALLOWED_INTENTS))})"
                )
    return errors


def audit(root: Path) -> list[str]:
    references = root / REFERENCES_DIR
    files = sorted(references.glob("*.md"))
    if not files:
        return [f"{REFERENCES_DIR}: no reference files found"]
    errors = []
    for path in files:
        errors.extend(audit_file(path, f"{REFERENCES_DIR}/{path.name}"))
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    errors = audit(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"FAIL: {len(errors)} frontmatter violation(s)", file=sys.stderr)
        return 1
    print("PASS: every writing-funnel-copy reference has conforming frontmatter")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
