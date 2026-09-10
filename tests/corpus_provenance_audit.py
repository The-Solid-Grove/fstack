#!/usr/bin/env python3
"""Dependency-free provenance audit for the funnels-research corpus.

Evidence files must say where their observations come from and, for live
walkthroughs, when they were captured:

- Top-level teardowns need a `> Source:` line near the top.
- copy/*-copy.md swipe files need a `> Source:` line near the top.
- live/*.md walkthroughs need a dated `> Walked:` line, or an explicit
  unknown capture date with a dated repository record. Import is not capture.
- No markdown file under skills/ or docs/ may contain a machine-specific
  absolute filesystem path (/Users/..., /home/..., C:\\Users\\...).
"""

from __future__ import annotations

import datetime
import re
import sys
from dataclasses import dataclass
from pathlib import Path


CORPUS = "skills/writing-funnel-copy/references/funnels-research"

TEARDOWN_SOURCE_WINDOW = 25
COPY_SOURCE_WINDOW = 5
LIVE_WALKED_WINDOW = 6

SOURCE_PATTERN = re.compile(r"^> Source:\s*\S")
WALKED_PATTERN = re.compile(r"^> Walked: (?:unknown; recorded in repository: )?(\d{4})-(\d{2})-(\d{2})\b")
ABSOLUTE_PATH_PATTERN = re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\Users)")


@dataclass(frozen=True)
class Diagnostic:
    code: str
    path: str
    message: str


def _diagnostic(code: str, path: str, message: str) -> Diagnostic:
    return Diagnostic(code=code, path=path, message=message)


def _has_source_line(text: str, window: int) -> bool:
    return any(
        SOURCE_PATTERN.match(line) for line in text.splitlines()[:window]
    )


def audit_teardown_source(text: str, path: str) -> list[Diagnostic]:
    if _has_source_line(text, TEARDOWN_SOURCE_WINDOW):
        return []
    return [
        _diagnostic(
            "teardown-source-required",
            path,
            "teardown must declare a `> Source:` line in its first "
            f"{TEARDOWN_SOURCE_WINDOW} lines",
        )
    ]


def audit_copy_source(text: str, path: str) -> list[Diagnostic]:
    if _has_source_line(text, COPY_SOURCE_WINDOW):
        return []
    return [
        _diagnostic(
            "copy-source-required",
            path,
            "copy swipe file must declare a `> Source:` line in its first "
            f"{COPY_SOURCE_WINDOW} lines",
        )
    ]


def audit_live_walk_date(text: str, path: str) -> list[Diagnostic]:
    for line in text.splitlines()[:LIVE_WALKED_WINDOW]:
        match = WALKED_PATTERN.match(line)
        if not match:
            continue
        year, month, day = (int(part) for part in match.groups())
        try:
            datetime.date(year, month, day)
        except ValueError:
            return [
                _diagnostic(
                    "live-walk-date-invalid",
                    path,
                    f"walk date {match.group(1)}-{match.group(2)}-"
                    f"{match.group(3)} is not a valid calendar date",
                )
            ]
        if not 2020 <= year <= 2100:
            return [
                _diagnostic(
                    "live-walk-date-invalid",
                    path,
                    f"walk date year {year} is outside the plausible range",
                )
            ]
        return []
    return [
        _diagnostic(
            "live-walk-date-required",
            path,
            "live walkthrough must declare a capture date or explicit unknown "
            "capture date with repository record date in its "
            f"first {LIVE_WALKED_WINDOW} lines",
        )
    ]


def audit_absolute_paths(text: str, path: str) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for number, line in enumerate(text.splitlines(), start=1):
        if ABSOLUTE_PATH_PATTERN.search(line):
            diagnostics.append(
                _diagnostic(
                    "absolute-path-forbidden",
                    path,
                    f"line {number} contains a machine-specific absolute "
                    "filesystem path",
                )
            )
    return diagnostics


def _relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def audit_repo(root: Path) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    corpus = root / CORPUS

    for path in sorted(corpus.glob("*.md")):
        if path.name.startswith("00-") or path.name == "README.md":
            continue
        diagnostics.extend(
            audit_teardown_source(path.read_text(), _relative(root, path))
        )

    for path in sorted(corpus.glob("copy/*-copy.md")):
        diagnostics.extend(
            audit_copy_source(path.read_text(), _relative(root, path))
        )

    for path in sorted(corpus.glob("live/*.md")):
        if path.name == "README.md":
            continue
        diagnostics.extend(
            audit_live_walk_date(path.read_text(), _relative(root, path))
        )

    for base in ("skills", "docs"):
        for path in sorted((root / base).rglob("*.md")):
            diagnostics.extend(
                audit_absolute_paths(path.read_text(), _relative(root, path))
            )

    return diagnostics


def main() -> int:
    root = (
        Path(sys.argv[1]).resolve()
        if len(sys.argv) > 1
        else Path(__file__).parents[1]
    )
    diagnostics = audit_repo(root)
    for diagnostic in diagnostics:
        print(
            f"{diagnostic.code}: {diagnostic.path}: {diagnostic.message}",
            file=sys.stderr,
        )
    return 1 if diagnostics else 0


if __name__ == "__main__":
    raise SystemExit(main())
