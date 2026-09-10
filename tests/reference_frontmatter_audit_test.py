#!/usr/bin/env python3
"""Unit tests for reference_frontmatter_audit.py."""

import tempfile
import unittest
from pathlib import Path

from reference_frontmatter_audit import REFERENCES_DIR, audit

CONFORMING = """\
---
id: funnel-example
title: Funnel Example
summary: An example reference.
intents:
  - research
  - plan
---

# Funnel Example
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ReferenceFrontmatterAuditTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.references = self.root / REFERENCES_DIR
        self.addCleanup(self._tmp.cleanup)

    def test_conforming_file_passes(self):
        write(self.references / "funnel-example.md", CONFORMING)
        self.assertEqual(audit(self.root), [])

    def test_extra_fields_are_allowed(self):
        text = CONFORMING.replace(
            "intents:", "version: 2.1.0\nalways_load: true\nkeywords:\n  - quiz\nintents:"
        )
        write(self.references / "funnel-example.md", text)
        self.assertEqual(audit(self.root), [])

    def test_missing_frontmatter_fails(self):
        write(self.references / "funnel-example.md", "# No frontmatter\n")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("missing or unclosed", errors[0])

    def test_unclosed_frontmatter_fails(self):
        write(self.references / "funnel-example.md", "---\nid: funnel-example\n")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("missing or unclosed", errors[0])

    def test_id_must_match_filename_stem(self):
        write(self.references / "funnel-other.md", CONFORMING)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("`id` must be `funnel-other`", errors[0])

    def test_missing_title_and_summary_fail(self):
        text = CONFORMING.replace("title: Funnel Example\n", "").replace(
            "summary: An example reference.\n", ""
        )
        write(self.references / "funnel-example.md", text)
        errors = audit(self.root)
        self.assertEqual(len(errors), 2)
        self.assertIn("`title` is missing or empty", errors[0])
        self.assertIn("`summary` is missing or empty", errors[1])

    def test_missing_intents_fails(self):
        text = CONFORMING.replace("intents:\n  - research\n  - plan\n", "")
        write(self.references / "funnel-example.md", text)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("`intents` must list at least one intent", errors[0])

    def test_empty_intents_list_fails(self):
        text = CONFORMING.replace("  - research\n  - plan\n", "")
        write(self.references / "funnel-example.md", text)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("`intents` must list at least one intent", errors[0])

    def test_unknown_intent_fails(self):
        text = CONFORMING.replace("- plan", "- implment")
        write(self.references / "funnel-example.md", text)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("unknown intent `implment`", errors[0])

    def test_empty_references_dir_fails_loudly(self):
        self.references.mkdir(parents=True)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("no reference files found", errors[0])

    def test_corpus_subdirectories_are_out_of_scope(self):
        write(self.references / "funnel-example.md", CONFORMING)
        write(self.references / "funnels-research/teardown.md", "# No frontmatter\n")
        self.assertEqual(audit(self.root), [])


if __name__ == "__main__":
    unittest.main()
