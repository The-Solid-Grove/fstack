#!/usr/bin/env python3
"""Audit path-like `.md` references inside the funnels-research corpus.

The corpus files cross-reference each other with backticked paths and bare
prose paths (`00-QA-CHECKLIST.md`, `live/*.md`) rather than markdown links, so
the markdown-link audit never sees them. A renamed or misspelled directory
silently strands the reference — exactly what happened when two files pointed
at `funnel-research/live/*.md` while the directory is `funnels-research/live/`.

Rules:
- Tokens audited: backticked `.md` paths, and bare `.md` paths that contain a
  `/` (bare no-slash filenames in prose are too ambiguous to audit).
- Glob patterns are allowed and must match at least one file.
- A token passes when it resolves relative to the containing file's directory,
  the corpus root, or the references root.
- Teardowns legitimately reference files that live in the torn-down funnel
  project, not in fstack; those are excluded via EXTERNAL_BASENAMES (exact
  no-slash names) and EXTERNAL_PREFIXES (first path segment).
- Fenced code blocks are ignored.

Exit code 0 when every audited reference resolves, 1 with one line per
violation otherwise.
"""

import glob
import os
import re
import sys
from pathlib import Path

CORPUS_DIR = "skills/writing-funnel-copy/references/funnels-research"
REFERENCES_DIR = "skills/writing-funnel-copy/references"

# Files that belong to the funnel project under teardown, not to fstack.
EXTERNAL_BASENAMES = {
    "AGENTS.md",
    "CLAUDE.md",
    "FLOW_CONFIG_AND_ROUTING.md",
    "PLAN.md",
    "PRODUCT_SENSE.md",
}

# First path segments that point into a funnel project's own tree.
EXTERNAL_PREFIXES = {"docs", "src", "output", "public"}

BACKTICKED_TOKEN = re.compile(r"`((?:\.\./)*[A-Za-z0-9_.*-]+(?:/[A-Za-z0-9_.*-]+)*\.md)`")
BARE_TOKEN = re.compile(
    r"(?<![`\w/.-])((?:\.\./)*[A-Za-z0-9_.*-]+(?:/[A-Za-z0-9_.*-]+)+\.md)(?![`\w])"
)
FENCE = re.compile(r"^(```|~~~)")


def extract_tokens(text: str) -> list[tuple[int, str]]:
    """(line_number, token) pairs for audited references, skipping fences."""
    tokens: list[tuple[int, str]] = []
    in_fence = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        if FENCE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        seen_spans: list[tuple[int, int]] = []
        for match in BACKTICKED_TOKEN.finditer(line):
            seen_spans.append(match.span())
            tokens.append((line_number, match.group(1)))
        for match in BARE_TOKEN.finditer(line):
            if any(start <= match.start() < end for start, end in seen_spans):
                continue
            tokens.append((line_number, match.group(1)))
    return tokens


def is_external(token: str) -> bool:
    if "/" not in token:
        return token in EXTERNAL_BASENAMES
    return token.split("/", 1)[0] in EXTERNAL_PREFIXES


def resolves(token: str, bases: list[Path]) -> bool:
    for base in bases:
        candidate = os.path.normpath(str(base / token))
        if glob.glob(candidate):
            return True
    return False


def audit(root: Path) -> list[str]:
    corpus = root / CORPUS_DIR
    references = root / REFERENCES_DIR
    if not corpus.is_dir():
        return [f"{CORPUS_DIR}: corpus directory not found"]
    errors: list[str] = []
    for path in sorted(corpus.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        bases = [path.parent, corpus, references]
        for line_number, token in extract_tokens(text):
            if is_external(token):
                continue
            if not resolves(token, bases):
                relative = path.relative_to(root)
                errors.append(
                    f"{relative}:{line_number}: unresolved corpus reference "
                    f"`{token}` (not found relative to the file, the corpus "
                    "root, or the references root)"
                )
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = audit(root)
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
