#!/usr/bin/env python3

import tempfile
import unittest
from pathlib import Path

from viewport_canon_audit import audit_file, audit_repo

ROOT = Path(__file__).parents[1]

ALL_FOUR = """\
Check content fit at small `375x667`, medium `393x852`, large `402x874`,
and desktop-small `1280x800` before considering the step ready.
"""

ROGUE_TOKEN = """\
Verify the layout at `390x844` before publishing.
"""

PARTIAL_SET = """\
Run the visual pass at small `375x667` and medium `393x852`.
"""

SINGLE_MENTION = """\
The overflow bug reproduces only at `375x667`.
"""

NOT_DIMENSIONS = """\
Payment volume grew 8x; the hash was 1a2b3c4d and the id abc123x456def.
"""


def codes(diagnostics):
    return [d.code for d in diagnostics]


class AuditFileTest(unittest.TestCase):
    def test_all_four_canonical_passes(self):
        self.assertEqual(audit_file(ALL_FOUR, "doc.md"), [])

    def test_noncanonical_token_flagged(self):
        diagnostics = audit_file(ROGUE_TOKEN, "doc.md")
        self.assertEqual(codes(diagnostics), ["viewport-noncanonical"])
        self.assertEqual(diagnostics[0].line, 1)
        self.assertIn("390x844", diagnostics[0].message)

    def test_partial_enumeration_flagged(self):
        diagnostics = audit_file(PARTIAL_SET, "doc.md")
        self.assertEqual(codes(diagnostics), ["viewport-set-incomplete"])
        self.assertIn("402x874", diagnostics[0].message)
        self.assertIn("1280x800", diagnostics[0].message)

    def test_single_mention_allowed(self):
        self.assertEqual(audit_file(SINGLE_MENTION, "doc.md"), [])

    def test_non_dimension_text_ignored(self):
        self.assertEqual(audit_file(NOT_DIMENSIONS, "doc.md"), [])

    def test_rogue_and_partial_both_reported(self):
        text = PARTIAL_SET + ROGUE_TOKEN
        self.assertEqual(
            sorted(codes(audit_file(text, "doc.md"))),
            ["viewport-noncanonical", "viewport-set-incomplete"],
        )


class AuditRepoTest(unittest.TestCase):
    def _repo(self, tmp, checklist=ALL_FOUR):
        root = Path(tmp)
        (root / "docs").mkdir()
        (root / "docs" / "funnel-qa-checklist.md").write_text(checklist)
        (root / "skills" / "demo").mkdir(parents=True)
        return root

    def test_clean_repo_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(tmp)
            (root / "skills" / "demo" / "SKILL.md").write_text(ALL_FOUR)
            self.assertEqual(audit_repo(root), [])

    def test_funnels_research_excluded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(tmp)
            research = (
                root
                / "skills"
                / "writing-funnel-copy"
                / "references"
                / "funnels-research"
                / "live"
            )
            research.mkdir(parents=True)
            (research / "walk.md").write_text(
                "Observed on an iPhone 13 mini viewport `375x812`.\n"
            )
            self.assertEqual(audit_repo(root), [])

    def test_missing_anchor_definition_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(tmp, checklist="No breakpoints here.\n")
            diagnostics = audit_repo(root)
            self.assertEqual(codes(diagnostics), ["viewport-canon-anchor-missing"])
            self.assertEqual(
                diagnostics[0].path, "docs/funnel-qa-checklist.md"
            )

    def test_skill_drift_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(tmp)
            (root / "skills" / "demo" / "SKILL.md").write_text(ROGUE_TOKEN)
            self.assertEqual(codes(audit_repo(root)), ["viewport-noncanonical"])

    def test_current_repo_conforms(self):
        self.assertEqual([d.render() for d in audit_repo(ROOT)], [])


if __name__ == "__main__":
    unittest.main()
