#!/usr/bin/env python3
"""Audit that numbered pattern catalogs stay in sync with their summary tables.

Catalog-style references (currently funnel-conversion-best-practices.md) pair
numbered `### N. <Pattern>` sections with a summary table whose first column
repeats those numbers. Scheduled runs append new patterns; when a section is
added without its table row (or a row without its section), the table silently
misrepresents the catalog. This audit fails on that drift.

Scope is every top-level markdown file directly under
`skills/writing-funnel-copy/references/` (the `funnels-research/` corpus is
excluded). A file participates only when it contains at least one numbered
pattern heading AND at least one numeric summary-table row; files without both
features are skipped.

Checks per participating file:

1. Pattern heading numbers must be contiguous starting at 1.
2. The set of numbers in numbered table rows must equal the set of heading
   numbers.

Exit code 0 when every catalog is in sync, 1 with one line per violation
otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REFERENCES_DIR = "skills/writing-funnel-copy/references"
PATTERN_HEADING = re.compile(r"^### (\d+)\. ")
TABLE_ROW = re.compile(r"^\| (\d+) \|")


def audit_file(path: Path, rel: str) -> list[str]:
    heading_numbers: list[int] = []
    heading_lines: dict[int, int] = {}
    table_numbers: list[int] = []
    for lineno, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        heading = PATTERN_HEADING.match(line)
        if heading:
            number = int(heading.group(1))
            heading_numbers.append(number)
            heading_lines.setdefault(number, lineno)
            continue
        row = TABLE_ROW.match(line)
        if row:
            table_numbers.append(int(row.group(1)))

    if not heading_numbers or not table_numbers:
        return []

    errors: list[str] = []

    expected = list(range(1, len(heading_numbers) + 1))
    if sorted(heading_numbers) != expected:
        errors.append(
            f"{rel}: catalog-heading-sequence: pattern headings must be "
            f"contiguous 1..{len(heading_numbers)}, got {sorted(heading_numbers)}"
        )

    missing_rows = sorted(set(heading_numbers) - set(table_numbers))
    for number in missing_rows:
        errors.append(
            f"{rel}:{heading_lines[number]}: catalog-table-missing-row: "
            f"pattern {number} has no matching summary-table row"
        )
    orphan_rows = sorted(set(table_numbers) - set(heading_numbers))
    for number in orphan_rows:
        errors.append(
            f"{rel}: catalog-table-orphan-row: summary-table row {number} "
            f"has no matching `### {number}. ` pattern heading"
        )
    return errors


def audit_repo(root: Path) -> list[str]:
    references = root / REFERENCES_DIR
    errors: list[str] = []
    for path in sorted(references.glob("*.md")):
        errors.extend(audit_file(path, str(path.relative_to(root))))
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = audit_repo(root)
    for error in errors:
        print(error)
    if errors:
        return 1
    print("PASS: pattern catalogs and summary tables are in sync")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
