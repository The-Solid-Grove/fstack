#!/usr/bin/env python3
"""Audit that QA viewport/breakpoint sizes stay on the canonical set.

The funnel QA breakpoints are defined once, in `docs/funnel-qa-checklist.md`:
small `375x667`, medium `393x852`, large `402x874`, desktop-small `1280x800`.
The same four sizes are repeated inline by the create/edit/preview skill
recipes. Historically these repeats have drifted (stale device sizes, partial
enumerations), which silently makes different docs prescribe different QA
passes. This audit pins every `<W>x<H>` token in skills/ and docs/ markdown to
the canonical set:

1. Any `\\d{3,4}x\\d{3,4}` token must be one of the four canonical viewports.
   A token that is genuinely not a viewport (for example image dimensions)
   must be added to NON_VIEWPORT_ALLOWLIST here, which is the explicit record
   that it was reviewed.
2. A file that uses two or more distinct canonical viewports is enumerating
   the QA set and must list all four, so no doc prescribes a partial pass.
3. `docs/funnel-qa-checklist.md` must itself define all four canonical
   viewports, since it is the file the others are expected to match.

The funnels-research corpus is excluded: its teardowns record devices as
observed on live third-party funnels, not fstack's QA canon.

Exit code 0 when clean, 1 with one diagnostic per line otherwise.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

CANONICAL_VIEWPORTS = ("375x667", "393x852", "402x874", "1280x800")
CANON_FILE = "docs/funnel-qa-checklist.md"
EXCLUDED_DIRS = ("skills/writing-funnel-copy/references/funnels-research",)
# Reviewed non-viewport WxH tokens (e.g. image dimensions). Keep sorted.
NON_VIEWPORT_ALLOWLIST: frozenset[str] = frozenset()

VIEWPORT_TOKEN = re.compile(r"(?<![0-9A-Za-z])(\d{3,4}x\d{3,4})(?![0-9A-Za-z])")


@dataclass(frozen=True)
class Diagnostic:
    code: str
    path: str
    line: int
    message: str

    def render(self) -> str:
        return f"{self.path}:{self.line}: {self.code}: {self.message}"


def extract_tokens(text: str) -> list[tuple[int, str]]:
    tokens = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for match in VIEWPORT_TOKEN.finditer(line):
            tokens.append((lineno, match.group(1)))
    return tokens


def audit_file(text: str, path: str) -> list[Diagnostic]:
    diagnostics = []
    tokens = extract_tokens(text)
    canonical_hint = ", ".join(CANONICAL_VIEWPORTS)

    for lineno, token in tokens:
        if token in CANONICAL_VIEWPORTS or token in NON_VIEWPORT_ALLOWLIST:
            continue
        diagnostics.append(
            Diagnostic(
                code="viewport-noncanonical",
                path=path,
                line=lineno,
                message=(
                    f"`{token}` is not a canonical QA viewport"
                    f" ({canonical_hint}); fix the size, or if this is not a"
                    " viewport add it to NON_VIEWPORT_ALLOWLIST in"
                    " tests/viewport_canon_audit.py"
                ),
            )
        )

    used = {token for _, token in tokens if token in CANONICAL_VIEWPORTS}
    if len(used) >= 2 and len(used) < len(CANONICAL_VIEWPORTS):
        missing = ", ".join(v for v in CANONICAL_VIEWPORTS if v not in used)
        first_line = min(
            lineno for lineno, token in tokens if token in CANONICAL_VIEWPORTS
        )
        diagnostics.append(
            Diagnostic(
                code="viewport-set-incomplete",
                path=path,
                line=first_line,
                message=(
                    "file enumerates the QA breakpoint set but is missing"
                    f" {missing}; list all four canonical viewports"
                ),
            )
        )
    return diagnostics


def _is_excluded(relative: str) -> bool:
    return any(
        relative == excluded or relative.startswith(excluded + "/")
        for excluded in EXCLUDED_DIRS
    )


def audit_repo(root: Path) -> list[Diagnostic]:
    diagnostics = []
    for pattern in ("skills/**/*.md", "docs/**/*.md"):
        for path in sorted(root.glob(pattern)):
            relative = path.relative_to(root).as_posix()
            if _is_excluded(relative):
                continue
            diagnostics.extend(
                audit_file(path.read_text(encoding="utf-8"), relative)
            )

    canon_path = root / CANON_FILE
    canon_text = (
        canon_path.read_text(encoding="utf-8") if canon_path.is_file() else ""
    )
    missing = [v for v in CANONICAL_VIEWPORTS if v not in canon_text]
    if missing:
        diagnostics.append(
            Diagnostic(
                code="viewport-canon-anchor-missing",
                path=CANON_FILE,
                line=1,
                message=(
                    "canonical breakpoint definition must include"
                    f" {', '.join(missing)}"
                ),
            )
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
        print(diagnostic.render(), file=sys.stderr)
    return 1 if diagnostics else 0


if __name__ == "__main__":
    raise SystemExit(main())
