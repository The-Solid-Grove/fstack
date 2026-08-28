#!/usr/bin/env python3
"""Unit tests for design_qa_evidence_audit.py."""

from __future__ import annotations

import unittest

from design_qa_evidence_audit import (
    TAG_RE,
    audit_checklist_items,
    audit_legend,
    audit_myths,
    audit_overlay_table,
    audit_text,
)


LEGEND = """
| Tag | Meaning |
| --- | --- |
| `[V]` | Verified |
| `[P]` | Practitioner pattern |
| `[S]` | Standard |
| `[F]` | Framework rule |
| `[✗]` | Refuted |
"""

MYTHS = """
## 8. Myths — do NOT enforce these

1. **Red buttons convert best.** Confounded classics. `[✗ V]`
2. **Shorter funnels convert better.** Verified opposite. `[V]`
"""

OVERLAYS = """
## 7. Step-type overlays

| Step type | Extra checks |
| --- | --- |
| **Question (ask)** | Easy questions first `[V]` |
| **Loader** | Rotating status copy `[F]` |
"""


def _codes(diagnostics):
    return [diagnostic.code for diagnostic in diagnostics]


class TagPatternTest(unittest.TestCase):
    def test_matches_plain_and_annotated_tags(self):
        for sample in (
            "`[V]`",
            "`[P — Noom teardown]`",
            "`[F-derived]`",
            "`[S/P]`",
            "`[✗ V]`",
            "`[✗/P]`",
            "`[P — verified ordering [V]]`",
        ):
            self.assertIsNotNone(TAG_RE.search(sample), sample)

    def test_ignores_checkboxes_prose_brackets_and_unknown_letters(self):
        for sample in ("- [ ] rule", "- [x] rule", "[red/green] buttons", "[Value]"):
            self.assertIsNone(TAG_RE.search(sample), sample)


class ChecklistTest(unittest.TestCase):
    def test_tagged_items_pass(self):
        text = "- [ ] **One value.** Exactly one idea. `[F]`\n"
        self.assertEqual(audit_checklist_items(text, "f"), [])

    def test_untagged_item_fails(self):
        text = "- [ ] **One value.** Exactly one idea.\n"
        self.assertEqual(_codes(audit_checklist_items(text, "f")), [
            "rule-missing-evidence-tag",
        ])

    def test_tag_on_continuation_line_passes(self):
        text = (
            "- [ ] **Expectation match.** Delivers what the previous step\n"
            "      implied. `[F]`\n"
        )
        self.assertEqual(audit_checklist_items(text, "f"), [])

    def test_untagged_wrapped_item_reports_first_line(self):
        text = (
            "intro\n"
            "- [ ] **Tagged.** Fine. `[P]`\n"
            "- [ ] **Untagged.** Wrapped across\n"
            "      two lines with no tag.\n"
            "\n"
        )
        diagnostics = audit_checklist_items(text, "f")
        self.assertEqual(_codes(diagnostics), ["rule-missing-evidence-tag"])
        self.assertIn("line 3", diagnostics[0].message)


class MythsTest(unittest.TestCase):
    def test_tagged_myths_pass(self):
        self.assertEqual(audit_myths(LEGEND + MYTHS, "f"), [])

    def test_untagged_myth_fails(self):
        text = MYTHS + "3. **Faces always work.** They don't.\n"
        self.assertEqual(_codes(audit_myths(text, "f")), [
            "myth-missing-evidence-tag",
        ])

    def test_missing_section_fails(self):
        self.assertEqual(_codes(audit_myths("# doc\n", "f")), [
            "myths-section-required",
        ])


class OverlayTableTest(unittest.TestCase):
    def test_tagged_rows_pass(self):
        self.assertEqual(audit_overlay_table(OVERLAYS, "f"), [])

    def test_untagged_row_fails(self):
        text = OVERLAYS + "| **Paywall** | Hero above the fold |\n"
        diagnostics = audit_overlay_table(text, "f")
        self.assertEqual(_codes(diagnostics), ["overlay-row-missing-evidence-tag"])
        self.assertIn("Paywall", diagnostics[0].message)

    def test_missing_section_fails(self):
        self.assertEqual(_codes(audit_overlay_table("# doc\n", "f")), [
            "overlays-section-required",
        ])


class LegendTest(unittest.TestCase):
    def test_defined_tags_pass(self):
        self.assertEqual(audit_legend(LEGEND + "- [ ] rule `[V]`\n", "f"), [])

    def test_undefined_tag_fails(self):
        text = "| `[V]` | Verified |\n- [ ] rule `[P]`\n"
        self.assertEqual(_codes(audit_legend(text, "f")), ["legend-missing-tag"])


class FullDocumentTest(unittest.TestCase):
    def test_clean_document_passes(self):
        text = (
            LEGEND
            + "\n## 1. Checks\n\n- [ ] **One value.** `[F]`\n"
            + OVERLAYS
            + MYTHS
        )
        self.assertEqual(audit_text(text, "f"), [])

    def test_each_violation_type_reported_once(self):
        text = (
            LEGEND
            + "\n## 1. Checks\n\n- [ ] **Untagged rule.**\n"
            + OVERLAYS
            + "| **Paywall** | No tag here |\n"
            + MYTHS
            + "3. **Untagged myth.** Oops.\n"
        )
        self.assertEqual(sorted(_codes(audit_text(text, "f"))), [
            "myth-missing-evidence-tag",
            "overlay-row-missing-evidence-tag",
            "rule-missing-evidence-tag",
        ])


if __name__ == "__main__":
    unittest.main()
