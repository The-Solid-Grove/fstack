#!/usr/bin/env python3

import tempfile
import unittest
from pathlib import Path

from corpus_provenance_audit import (
    CORPUS,
    audit_absolute_paths,
    audit_copy_source,
    audit_live_walk_date,
    audit_repo,
    audit_teardown_source,
)


ROOT = Path(__file__).parents[1]

TEARDOWN_WITH_SOURCE = """\
# Example Funnel — Research Notes

> Source: funnels/rag-catalog/example — src/steps/step-01.tsx … step-09.tsx.

## 1. Overview
"""

TEARDOWN_WITHOUT_SOURCE = """\
# Example Funnel — Research Notes

## 1. Overview

Body prose without any provenance.
"""

COPY_WITH_SOURCE = """\
# Example — Copy Swipe (verbatim from source)
> Source: rag-catalog/example. Extracted from step source files.

## Step 1
"""

LIVE_WITH_WALKED = """\
# Example (Vertical) — Live Funnel Walkthrough

> Walked: 2026-06-15 (capture date from repo history).

## Overview
"""

LIVE_WITHOUT_WALKED = """\
# Example (Vertical) — Live Funnel Walkthrough

## Overview
"""

LIVE_WALKED_TOO_DEEP = """\
# Example (Vertical) — Live Funnel Walkthrough

## Overview
Line
Line
Line
> Walked: 2026-06-15
"""

LIVE_WALKED_BAD_DATE = """\
# Example (Vertical) — Live Funnel Walkthrough

> Walked: 2026-02-30

## Overview
"""

LIVE_WALKED_BAD_YEAR = """\
# Example (Vertical) — Live Funnel Walkthrough

> Walked: 3026-06-15

## Overview
"""


def codes(diagnostics):
    return {diagnostic.code for diagnostic in diagnostics}


class TeardownSourceTest(unittest.TestCase):
    def test_source_line_passes(self):
        self.assertEqual(
            audit_teardown_source(TEARDOWN_WITH_SOURCE, "example.md"), []
        )

    def test_missing_source_is_rejected(self):
        self.assertEqual(
            codes(audit_teardown_source(TEARDOWN_WITHOUT_SOURCE, "example.md")),
            {"teardown-source-required"},
        )

    def test_source_beyond_window_is_rejected(self):
        text = "\n" * 30 + "> Source: somewhere\n"
        self.assertEqual(
            codes(audit_teardown_source(text, "example.md")),
            {"teardown-source-required"},
        )


class CopySourceTest(unittest.TestCase):
    def test_source_line_passes(self):
        self.assertEqual(audit_copy_source(COPY_WITH_SOURCE, "x-copy.md"), [])

    def test_missing_source_is_rejected(self):
        self.assertEqual(
            codes(audit_copy_source(TEARDOWN_WITHOUT_SOURCE, "x-copy.md")),
            {"copy-source-required"},
        )


class LiveWalkDateTest(unittest.TestCase):
    def test_walked_line_passes(self):
        self.assertEqual(audit_live_walk_date(LIVE_WITH_WALKED, "live.md"), [])

    def test_missing_walked_line_is_rejected(self):
        self.assertEqual(
            codes(audit_live_walk_date(LIVE_WITHOUT_WALKED, "live.md")),
            {"live-walk-date-required"},
        )

    def test_walked_line_beyond_window_is_rejected(self):
        self.assertEqual(
            codes(audit_live_walk_date(LIVE_WALKED_TOO_DEEP, "live.md")),
            {"live-walk-date-required"},
        )

    def test_invalid_calendar_date_is_rejected(self):
        self.assertEqual(
            codes(audit_live_walk_date(LIVE_WALKED_BAD_DATE, "live.md")),
            {"live-walk-date-invalid"},
        )

    def test_implausible_year_is_rejected(self):
        self.assertEqual(
            codes(audit_live_walk_date(LIVE_WALKED_BAD_YEAR, "live.md")),
            {"live-walk-date-invalid"},
        )


class AbsolutePathTest(unittest.TestCase):
    def test_clean_text_passes(self):
        self.assertEqual(
            audit_absolute_paths(TEARDOWN_WITH_SOURCE, "example.md"), []
        )

    def test_macos_home_path_is_rejected(self):
        text = "> Source: `/Users/someone/work/repo/funnels/example`\n"
        self.assertEqual(
            codes(audit_absolute_paths(text, "example.md")),
            {"absolute-path-forbidden"},
        )

    def test_linux_home_path_is_rejected(self):
        text = "See /home/someone/checkout/file.md for details.\n"
        self.assertEqual(
            codes(audit_absolute_paths(text, "example.md")),
            {"absolute-path-forbidden"},
        )

    def test_windows_profile_path_is_rejected(self):
        text = "Copied from C:\\Users\\someone\\repo.\n"
        self.assertEqual(
            codes(audit_absolute_paths(text, "example.md")),
            {"absolute-path-forbidden"},
        )

    def test_each_offending_line_is_reported(self):
        text = "/Users/a/one\nclean line\n/home/b/two\n"
        self.assertEqual(len(audit_absolute_paths(text, "example.md")), 2)


class AuditRepoTest(unittest.TestCase):
    def _make_tree(self, tmp: str) -> Path:
        root = Path(tmp)
        corpus = root / CORPUS
        (corpus / "copy").mkdir(parents=True)
        (corpus / "live").mkdir()
        (root / "docs").mkdir()
        (corpus / "README.md").write_text("# Index\n")
        (corpus / "00-NOTES.md").write_text("# Notes, exempt\n")
        (corpus / "example.md").write_text(TEARDOWN_WITH_SOURCE)
        (corpus / "copy" / "example-copy.md").write_text(COPY_WITH_SOURCE)
        (corpus / "copy" / "README.md").write_text("# Index\n")
        (corpus / "live" / "example.md").write_text(LIVE_WITH_WALKED)
        (corpus / "live" / "README.md").write_text("# Index\n")
        (corpus / "live" / "nebula.md").write_text(LIVE_WITHOUT_WALKED)
        return root

    def test_conforming_tree_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(audit_repo(self._make_tree(tmp)), [])

    def test_violations_are_collected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._make_tree(tmp)
            corpus = root / CORPUS
            (corpus / "bad-teardown.md").write_text(TEARDOWN_WITHOUT_SOURCE)
            (corpus / "live" / "bad.md").write_text(LIVE_WITHOUT_WALKED)
            (root / "docs" / "note.md").write_text("/Users/a/leak\n")
            self.assertEqual(
                codes(audit_repo(root)),
                {
                    "teardown-source-required",
                    "live-walk-date-required",
                    "absolute-path-forbidden",
                },
            )

    def test_fstack_repo_is_clean(self):
        self.assertEqual(audit_repo(ROOT), [])


if __name__ == "__main__":
    unittest.main()
