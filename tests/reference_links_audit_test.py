#!/usr/bin/env python3
"""Unit tests for reference_links_audit.py."""

import tempfile
import unittest
from pathlib import Path

from reference_links_audit import audit


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ReferenceLinksAuditTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_resolving_links_pass(self):
        write(self.root / "skills/demo/SKILL.md",
              "Read `references/guide.md` and browse `references/corpus/`.")
        write(self.root / "skills/demo/references/guide.md", "guide")
        write(self.root / "skills/demo/references/corpus/README.md",
              "See [guide](../guide.md) and [site](https://example.com) "
              "and [section](../guide.md#anchor).")
        self.assertEqual(audit(self.root), [])

    def test_missing_backticked_file_fails(self):
        write(self.root / "skills/demo/SKILL.md", "Read `references/gone.md`.")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("references/gone.md", errors[0])

    def test_file_where_directory_expected_fails(self):
        write(self.root / "skills/demo/SKILL.md", "Browse `references/corpus/`.")
        write(self.root / "skills/demo/references/corpus", "not a directory")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("missing directory", errors[0])

    def test_broken_readme_relative_link_fails(self):
        write(self.root / "skills/demo/references/README.md",
              "See [moved file](old-name.md).")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("old-name.md", errors[0])

    def test_non_skill_paths_are_not_checked(self):
        # `AGENTS.md`, `docs/funnelsgrove/...` etc. refer to the synced funnel
        # project, not this repo — only `references/...` paths are audited.
        write(self.root / "skills/demo/SKILL.md",
              "Read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` first.")
        self.assertEqual(audit(self.root), [])


if __name__ == "__main__":
    unittest.main()
