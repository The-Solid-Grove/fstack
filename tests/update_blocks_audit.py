#!/usr/bin/env python3
"""Audit sourcing discipline in web2app-essentials "Post-course update" blocks.

The web2app-essentials corpus is a distillation of a fixed 2024 course; new
knowledge is only ever added as blockquoted "Post-course update" blocks inside
existing modules. The repo's standing rule for those blocks is: only specific,
verifiable findings — every block must say when it was verified and must cite
at least one source link. This audit enforces that mechanically:

1. The block's first line is a header of the form
   `> **Post-course update (verified <Month> <Year>): <headline>**`.
2. The block body contains at least one `[text](https://...)` source link.

Scope is every markdown module under `skills/web2app-essentials/references/`.
Exit code 0 when every block conforms, 1 with one line per violation.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


REFERENCES_DIR = "skills/web2app-essentials/references"
UPDATE_MARKER = "Post-course update"
HEADER_RE = re.compile(
    r"^> \*\*Post-course update \(verified "
    r"(January|February|March|April|May|June|July|August|September|October|November|December)"
    r" \d{4}\): .+\*\*$"
)
SOURCE_LINK_RE = re.compile(r"\[[^\]]+\]\(https://[^)\s]+\)")


@dataclass(frozen=True)
class Diagnostic:
    code: str
    path: str
    line: int
    message: str

    def render(self) -> str:
        return f"{self.path}:{self.line}: {self.code}: {self.message}"


@dataclass(frozen=True)
class Block:
    """A run of consecutive `>` blockquote lines."""

    start_line: int  # 1-indexed line of the first blockquote line
    lines: tuple[str, ...]

    @property
    def text(self) -> str:
        return "\n".join(self.lines)


def find_blockquote_blocks(text: str) -> list[Block]:
    blocks: list[Block] = []
    current: list[str] = []
    start = 0
    for number, line in enumerate(text.splitlines(), start=1):
        if line.startswith(">"):
            if not current:
                start = number
            current.append(line)
        elif current:
            blocks.append(Block(start_line=start, lines=tuple(current)))
            current = []
    if current:
        blocks.append(Block(start_line=start, lines=tuple(current)))
    return blocks


def audit_block(block: Block, path: str) -> list[Diagnostic]:
    if UPDATE_MARKER not in block.text:
        return []
    diagnostics: list[Diagnostic] = []
    if not HEADER_RE.match(block.lines[0]):
        diagnostics.append(
            Diagnostic(
                code="update-block-verified-stamp",
                path=path,
                line=block.start_line,
                message=(
                    "update block must start with "
                    "`> **Post-course update (verified <Month> <Year>): <headline>**`"
                ),
            )
        )
    if not SOURCE_LINK_RE.search(block.text):
        diagnostics.append(
            Diagnostic(
                code="update-block-source-link",
                path=path,
                line=block.start_line,
                message="update block must cite at least one https source link",
            )
        )
    return diagnostics


def audit_file(text: str, path: str) -> list[Diagnostic]:
    return [
        diagnostic
        for block in find_blockquote_blocks(text)
        for diagnostic in audit_block(block, path)
    ]


def audit_repo(root: Path) -> list[Diagnostic]:
    references = root / REFERENCES_DIR
    diagnostics: list[Diagnostic] = []
    for path in sorted(references.glob("**/*.md")):
        relative = str(path.relative_to(root))
        diagnostics.extend(audit_file(path.read_text(encoding="utf-8"), relative))
    return diagnostics


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    diagnostics = audit_repo(root)
    for diagnostic in diagnostics:
        print(diagnostic.render(), file=sys.stderr)
    return 1 if diagnostics else 0


if __name__ == "__main__":
    sys.exit(main())
