#!/usr/bin/env python3
"""Audit source-tag provenance in the cross-funnel copy bank.

The copy bank (`copy/00-COPY-BANK-by-screen-type.md`) reorganizes verbatim
copy from the per-funnel research notes by screen type. Its contract is that
every harvested line carries a `[tag]` naming the source funnel, so a reader
can jump from any line back to the full teardown, copy dump, or live
walkthrough it came from. That provenance silently rots in two ways:

1. A line gets added without a tag — the copy loses its source.
2. A tag stops resolving — the note file it pointed at was renamed or
   removed, or the tag was a typo from the start.

This audit enforces both mechanically. A tag resolves when its normalized
form (lowercase, alphanumerics only) matches a corpus note's filename stem by
exact or prefix relation in either direction — so `[iqbrain]` finds
`live/iq-brain.md`, `[betterme]` finds `betterme-chair-yoga.md`, and
`[headway-live]` finds `live/headway.md`. Index/synthesis files (`00-*`) and
READMEs are not source notes and never satisfy a tag. Tags shorter than three
characters must match a stem exactly.

Exit code 0 when every list line is tagged and every tag resolves, 1 with one
line per violation otherwise.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

CORPUS_DIR = "skills/writing-funnel-copy/references/funnels-research"
COPY_BANK = "copy/00-COPY-BANK-by-screen-type.md"

TAG_SUFFIX_RE = re.compile(r"\[([a-z0-9-]+(?:\s*,\s*[a-z0-9-]+)*)\]$")
LIST_ITEM_RE = re.compile(r"^\s*-\s+\S")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
MIN_PREFIX_TAG_LENGTH = 3


@dataclass(frozen=True)
class Diagnostic:
    code: str
    line: int
    message: str

    def render(self, path: str) -> str:
        return f"{path}:{self.line}: {self.code}: {self.message}"


def normalize(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower())


def corpus_stems(corpus_root: Path) -> set[str]:
    """Normalized stems of every source note under the research corpus."""
    return {
        normalize(path.stem)
        for path in corpus_root.rglob("*.md")
        if path.name.lower() != "readme.md" and not path.name.startswith("00-")
    }


def tag_resolves(tag: str, stems: set[str]) -> bool:
    normalized = normalize(tag)
    if not normalized:
        return False
    if len(normalized) < MIN_PREFIX_TAG_LENGTH:
        return normalized in stems
    return any(
        stem == normalized
        or stem.startswith(normalized)
        or normalized.startswith(stem)
        for stem in stems
    )


def audit_text(text: str, stems: set[str]) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    in_fence = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence or not LIST_ITEM_RE.match(line):
            continue
        match = TAG_SUFFIX_RE.search(line.rstrip())
        if match is None:
            diagnostics.append(
                Diagnostic(
                    "copy-bank-untagged-line",
                    line_number,
                    "list line does not end with a `[source-funnel]` tag",
                )
            )
            continue
        for tag in (part.strip() for part in match.group(1).split(",")):
            if not tag_resolves(tag, stems):
                diagnostics.append(
                    Diagnostic(
                        "copy-bank-unresolved-tag",
                        line_number,
                        f"tag `[{tag}]` does not match any funnel note in the corpus",
                    )
                )
    return diagnostics


def audit(root: Path) -> list[str]:
    corpus_root = root / CORPUS_DIR
    copy_bank = corpus_root / COPY_BANK
    if not copy_bank.is_file():
        return [f"{CORPUS_DIR}/{COPY_BANK}: copy bank not found (renamed? update this audit)"]
    stems = corpus_stems(corpus_root)
    if not stems:
        return [f"{CORPUS_DIR}: no funnel note files found"]
    relative = f"{CORPUS_DIR}/{COPY_BANK}"
    text = copy_bank.read_text(encoding="utf-8")
    return [diagnostic.render(relative) for diagnostic in audit_text(text, stems)]


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    errors = audit(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"FAIL: {len(errors)} copy-bank provenance violation(s)", file=sys.stderr)
        return 1
    print("PASS: every copy-bank line is tagged and every tag resolves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
