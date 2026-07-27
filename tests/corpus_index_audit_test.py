#!/usr/bin/env python3
"""Unit tests for corpus_index_audit.py."""

import tempfile
import unittest
from pathlib import Path

from corpus_index_audit import audit


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class CorpusIndexAuditTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.skill = self.root / "skills/web2app-essentials"
        self.research = self.root / "skills/writing-funnel-copy/references/funnels-research"
        self.addCleanup(self._tmp.cleanup)
        # Minimal valid research corpus so web2app-focused tests stay green.
        write(self.research / "teardown.md", "content")
        write(self.research / "README.md", "- [teardown](teardown.md)")

    def test_indexed_and_routed_module_passes(self):
        write(self.skill / "references/1-intro/1.1-basics.md", "content")
        write(self.skill / "references/README.md",
              "- [1.1 Basics](1-intro/1.1-basics.md) — what funnels are")
        write(self.skill / "SKILL.md",
              "| Basics | `references/1-intro/1.1-basics.md` |")
        self.assertEqual(audit(self.root), [])

    def test_module_missing_from_readme_fails(self):
        write(self.skill / "references/1-intro/1.1-basics.md", "content")
        write(self.skill / "references/README.md", "no links here")
        write(self.skill / "SKILL.md",
              "| Basics | `references/1-intro/1.1-basics.md` |")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("README.md does not index", errors[0])
        self.assertIn("1-intro/1.1-basics.md", errors[0])

    def test_module_missing_from_routing_table_fails(self):
        write(self.skill / "references/1-intro/1.1-basics.md", "content")
        write(self.skill / "references/README.md",
              "- [1.1 Basics](1-intro/1.1-basics.md)")
        write(self.skill / "SKILL.md", "no routing table entries")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("routing table does not route", errors[0])

    def test_readme_itself_is_not_a_module(self):
        # references/README.md sits at the top level, not inside a module
        # folder, so it must not be required to index itself.
        write(self.skill / "references/1-intro/1.1-basics.md", "content")
        write(self.skill / "references/README.md",
              "- [1.1 Basics](1-intro/1.1-basics.md)")
        write(self.skill / "SKILL.md",
              "| Basics | `references/1-intro/1.1-basics.md` |")
        self.assertEqual(audit(self.root), [])

    def test_empty_corpus_fails_loudly(self):
        write(self.skill / "references/README.md", "empty")
        write(self.skill / "SKILL.md", "empty")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("no module files found", errors[0])

    def _write_valid_web2app_skill(self):
        write(self.skill / "references/1-intro/1.1-basics.md", "content")
        write(self.skill / "references/README.md",
              "- [1.1 Basics](1-intro/1.1-basics.md)")
        write(self.skill / "SKILL.md",
              "| Basics | `references/1-intro/1.1-basics.md` |")

    def test_research_file_missing_from_own_dir_readme_fails(self):
        self._write_valid_web2app_skill()
        write(self.research / "copy/swipe.md", "content")
        write(self.research / "copy/README.md", "no links here")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("does not index `swipe.md`", errors[0])
        self.assertIn("funnels-research/copy", errors[0])

    def test_research_dir_without_readme_fails(self):
        self._write_valid_web2app_skill()
        write(self.research / "live/walkthrough.md", "content")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("no README.md index", errors[0])
        self.assertIn("funnels-research/live", errors[0])

    def test_research_subdir_readme_indexes_only_its_own_files(self):
        # A file indexed in the parent README but not its own dir's README
        # still fails: routing descends README by README.
        self._write_valid_web2app_skill()
        write(self.research / "live/walkthrough.md", "content")
        write(self.research / "live/README.md",
              "- [walkthrough](walkthrough.md)")
        self.assertEqual(audit(self.root), [])

    def test_missing_research_corpus_fails_loudly(self):
        self._write_valid_web2app_skill()
        import shutil
        shutil.rmtree(self.research)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("research corpus directory not found", errors[0])


if __name__ == "__main__":
    unittest.main()
