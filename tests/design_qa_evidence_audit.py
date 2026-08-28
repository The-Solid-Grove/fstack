#!/usr/bin/env python3
"""Evidence-tag audit for the step-level design QA checklist.

00-STEP-DESIGN-QA.md promises that every rule is tagged with its evidence
level ([V]/[P]/[S]/[F]/[✗]) "so we don't enforce folklore as law". This audit
holds the file to that promise:

- every checklist item (`- [ ]`) must carry at least one evidence tag,
- every numbered myth in the myths section must carry at least one tag,
- every step-type row in the overlays table must carry at least one tag,
- every tag used in the file must be one the legend table defines.

Stdlib only, mirrors the other tests/*_audit.py suites.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


TARGET = (
    "skills/writing-funnel-copy/references/funnels-research/00-STEP-DESIGN-QA.md"
)
KNOWN_TAG_LETTERS = ("V", "P", "S", "F", "✗")
# A tag is [<letter>] or [<letter><separator>...], e.g. [P], [F-derived],
# [S/P], [✗ V], [P — Noom teardown]. The separator requirement keeps prose
# like "[red/green/orange]" and checkbox "[ ]" markers from matching.
TAG_RE = re.compile(r"\[(V|P|S|F|✗)(?:\]|[ /—–-][^\]]*\])")
CHECKLIST_ITEM_RE = re.compile(r"^- \[[ x]\] ")
NUMBERED_ITEM_RE = re.compile(r"^\d+\.\s")
HEADING_RE = re.compile(r"^#{2,3}\s")


@dataclass(frozen=True)
class Diagnostic:
    code: str
    path: str
    message: str


def _blocks(lines: list[str], start_re: re.Pattern[str]) -> list[tuple[int, str]]:
    """Collect (line_number, joined_text) blocks that begin with start_re.

    A block runs until the next block start, a heading, a table row, or a
    blank line — continuation lines are indented, so this joins wrapped
    checklist/numbered items into one searchable string.
    """
    blocks: list[tuple[int, str]] = []
    current_start: int | None = None
    current: list[str] = []
    for number, line in enumerate(lines, start=1):
        if start_re.match(line):
            if current_start is not None:
                blocks.append((current_start, " ".join(current)))
            current_start = number
            current = [line.strip()]
        elif current_start is not None:
            if line.startswith((" ", "\t")) and line.strip():
                current.append(line.strip())
            else:
                blocks.append((current_start, " ".join(current)))
                current_start = None
                current = []
    if current_start is not None:
        blocks.append((current_start, " ".join(current)))
    return blocks


def _sections(text: str) -> dict[str, list[str]]:
    """Split the document into {heading_line: body_lines} sections."""
    sections: dict[str, list[str]] = {}
    heading = ""
    for line in text.splitlines():
        if HEADING_RE.match(line):
            heading = line.strip()
            sections[heading] = []
        else:
            sections.setdefault(heading, []).append(line)
    return sections


def _find_section(sections: dict[str, list[str]], marker: str) -> list[str] | None:
    for heading, body in sections.items():
        if marker.lower() in heading.lower():
            return body
    return None


def audit_checklist_items(text: str, path: str) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for number, block in _blocks(text.splitlines(), CHECKLIST_ITEM_RE):
        if not TAG_RE.search(block):
            excerpt = block[:72]
            diagnostics.append(
                Diagnostic(
                    "rule-missing-evidence-tag",
                    path,
                    f"line {number}: checklist rule has no evidence tag: {excerpt}",
                )
            )
    return diagnostics


def audit_myths(text: str, path: str) -> list[Diagnostic]:
    body = _find_section(_sections(text), "Myths")
    if body is None:
        return [
            Diagnostic(
                "myths-section-required",
                path,
                "file must keep a Myths section listing refuted rules",
            )
        ]
    diagnostics: list[Diagnostic] = []
    for number, block in _blocks(body, NUMBERED_ITEM_RE):
        if not TAG_RE.search(block):
            excerpt = block[:72]
            diagnostics.append(
                Diagnostic(
                    "myth-missing-evidence-tag",
                    path,
                    f"myth item has no evidence tag: {excerpt}",
                )
            )
    return diagnostics


def audit_overlay_table(text: str, path: str) -> list[Diagnostic]:
    body = _find_section(_sections(text), "Step-type overlays")
    if body is None:
        return [
            Diagnostic(
                "overlays-section-required",
                path,
                "file must keep a Step-type overlays section",
            )
        ]
    diagnostics: list[Diagnostic] = []
    for line in body:
        stripped = line.strip()
        if not stripped.startswith("| **"):
            continue
        if not TAG_RE.search(stripped):
            step_type = stripped.split("|")[1].strip().strip("*")
            diagnostics.append(
                Diagnostic(
                    "overlay-row-missing-evidence-tag",
                    path,
                    f"overlay row has no evidence tag: {step_type}",
                )
            )
    return diagnostics


def audit_legend(text: str, path: str) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    used = {match.group(1) for match in TAG_RE.finditer(text)}
    defined: set[str] = set()
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip().split("|") if cell.strip()]
        # A legend row defines a tag when the tag is the entire first cell.
        if cells and line.lstrip().startswith("|"):
            for letter in KNOWN_TAG_LETTERS:
                if cells[0] == f"`[{letter}]`":
                    defined.add(letter)
    for letter in sorted(used):
        if letter not in KNOWN_TAG_LETTERS:
            diagnostics.append(
                Diagnostic(
                    "unknown-evidence-tag",
                    path,
                    f"tag [{letter}] is used but is not a known evidence level",
                )
            )
        elif letter not in defined:
            diagnostics.append(
                Diagnostic(
                    "legend-missing-tag",
                    path,
                    f"tag [{letter}] is used but the legend never defines it",
                )
            )
    return diagnostics


def audit_text(text: str, path: str) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    diagnostics.extend(audit_checklist_items(text, path))
    diagnostics.extend(audit_myths(text, path))
    diagnostics.extend(audit_overlay_table(text, path))
    diagnostics.extend(audit_legend(text, path))
    return diagnostics


def audit_repo(root: Path) -> list[Diagnostic]:
    target = root / TARGET
    if not target.is_file():
        return [Diagnostic("target-missing", TARGET, "audited file not found")]
    return audit_text(target.read_text(encoding="utf-8"), TARGET)


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
