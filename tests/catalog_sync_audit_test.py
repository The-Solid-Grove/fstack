#!/usr/bin/env python3
"""Unit tests for catalog_sync_audit.py."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import catalog_sync_audit

CONFORMING = """# Catalog

### 1. First Pattern

Body.

### 2. Second Pattern

Body.

## Summary Table

| # | Pattern | Impact |
| --- | --- | --- |
| 1 | First pattern | +5% |
| 2 | Second pattern | +7% |
"""


class CatalogSyncAuditTest(unittest.TestCase):
    def run_audit(self, content: str) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            references = root / catalog_sync_audit.REFERENCES_DIR
            references.mkdir(parents=True)
            (references / "catalog.md").write_text(content, encoding="utf-8")
            return catalog_sync_audit.audit_repo(root)

    def test_conforming_catalog_passes(self):
        self.assertEqual(self.run_audit(CONFORMING), [])

    def test_missing_table_row_fails(self):
        content = CONFORMING.replace("| 2 | Second pattern | +7% |\n", "")
        errors = self.run_audit(content)
        self.assertEqual(len(errors), 1)
        self.assertIn("catalog-table-missing-row", errors[0])
        self.assertIn("pattern 2", errors[0])

    def test_orphan_table_row_fails(self):
        content = CONFORMING + "| 3 | Ghost pattern | +9% |\n"
        errors = self.run_audit(content)
        self.assertEqual(len(errors), 1)
        self.assertIn("catalog-table-orphan-row", errors[0])

    def test_non_contiguous_headings_fail(self):
        content = CONFORMING.replace("### 2. Second Pattern", "### 3. Second Pattern")
        errors = self.run_audit(content)
        self.assertTrue(
            any("catalog-heading-sequence" in error for error in errors)
        )

    def test_file_without_numeric_table_is_skipped(self):
        content = "### 1. Lone Pattern\n\nBody, no summary table.\n"
        self.assertEqual(self.run_audit(content), [])

    def test_file_without_numbered_headings_is_skipped(self):
        content = "# Doc\n\n| 1 | Row | +1% |\n"
        self.assertEqual(self.run_audit(content), [])

    def test_funnels_research_corpus_is_excluded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            references = root / catalog_sync_audit.REFERENCES_DIR
            corpus = references / "funnels-research"
            corpus.mkdir(parents=True)
            broken = CONFORMING.replace("| 2 | Second pattern | +7% |\n", "")
            (corpus / "teardown.md").write_text(broken, encoding="utf-8")
            self.assertEqual(catalog_sync_audit.audit_repo(root), [])

    def test_current_corpus_conforms(self):
        repo_root = Path(__file__).resolve().parent.parent
        self.assertEqual(catalog_sync_audit.audit_repo(repo_root), [])


if __name__ == "__main__":
    unittest.main()
