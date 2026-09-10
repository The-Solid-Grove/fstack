#!/usr/bin/env python3
"""Unit tests for reference_links_audit.py."""

import tempfile
import unittest
from pathlib import Path

from reference_links_audit import audit, heading_slugs


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
        write(self.root / "skills/demo/references/guide.md",
              "# Guide\n\n## Anchor\n\nguide")
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

    def test_broken_link_in_non_readme_reference_fails(self):
        write(self.root / "skills/demo/references/notes.md",
              "See [companion](missing-companion.md).")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("missing-companion.md", errors[0])

    def test_broken_link_in_docs_fails(self):
        write(self.root / "docs/checklist.md", "See [plan](plans/gone.md).")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("plans/gone.md", errors[0])

    def test_broken_link_in_root_readme_fails(self):
        write(self.root / "README.md", "See [docs](docs/missing.md).")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("docs/missing.md", errors[0])

    def test_broken_anchor_fails(self):
        write(self.root / "skills/demo/references/guide.md", "# Guide\n\nbody")
        write(self.root / "skills/demo/references/notes.md",
              "See [section](guide.md#no-such-section).")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("broken anchor", errors[0])
        self.assertIn("no-such-section", errors[0])

    def test_same_file_anchor_is_validated(self):
        write(self.root / "docs/guide.md",
              "# Guide\n\n## Real Section\n\nJump to [real](#real-section) "
              "and [fake](#fake-section).")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("fake-section", errors[0])

    def test_links_inside_code_fences_are_ignored(self):
        write(self.root / "docs/guide.md",
              "# Guide\n\n```md\nSee [example](not-a-real-file.md).\n```\n")
        self.assertEqual(audit(self.root), [])

    def test_anchor_to_non_markdown_target_is_not_checked(self):
        write(self.root / "docs/guide.md", "See [style](style.css#L10).")
        write(self.root / "docs/style.css", "body {}")
        self.assertEqual(audit(self.root), [])

    def test_heading_slugs_formatting_and_duplicates(self):
        slugs = heading_slugs(
            "# Paywall & Checkout\n"
            "## Step 1: QA\n"
            "## Repeat\n"
            "## Repeat\n"
            "```txt\n# Not A Heading\n```\n"
        )
        self.assertIn("paywall--checkout", slugs)
        self.assertIn("step-1-qa", slugs)
        self.assertIn("repeat", slugs)
        self.assertIn("repeat-1", slugs)
        self.assertNotIn("not-a-heading", slugs)

    def test_non_skill_paths_are_not_checked(self):
        # `AGENTS.md`, `docs/funnelsgrove/...` etc. refer to the synced funnel
        # project, not this repo — only `references/...` paths are audited.
        write(self.root / "skills/demo/SKILL.md",
              "Read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` first.")
        self.assertEqual(audit(self.root), [])


if __name__ == "__main__":
    unittest.main()
