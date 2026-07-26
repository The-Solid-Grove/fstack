#!/usr/bin/env python3
"""Unit tests for skill_frontmatter_audit.py."""

import tempfile
import unittest
from pathlib import Path

from skill_frontmatter_audit import audit


VALID_DESCRIPTION = (
    "Use when editing hosted funnels through local CLI sync, including scoped"
    " local edits, local preview, QA, and publish."
)


def write_skill(root: Path, dir_name: str, name: str, description: str) -> None:
    skill_md = root / "skills" / dir_name / "SKILL.md"
    skill_md.parent.mkdir(parents=True, exist_ok=True)
    skill_md.write_text(
        f"---\nname: {name}\ndescription: {description}\n---\n\n# Body\n",
        encoding="utf-8",
    )


class SkillFrontmatterAuditTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_conforming_skill_passes(self):
        write_skill(self.root, "edit-funnel", "edit-funnel", VALID_DESCRIPTION)
        self.assertEqual(audit(self.root), [])

    def test_missing_skill_md_fails(self):
        (self.root / "skills/empty-skill").mkdir(parents=True)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("missing SKILL.md", errors[0])

    def test_missing_frontmatter_block_fails(self):
        skill_md = self.root / "skills/edit-funnel/SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text("# No frontmatter\n", encoding="utf-8")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("no closed --- frontmatter block", errors[0])

    def test_unclosed_frontmatter_block_fails(self):
        skill_md = self.root / "skills/edit-funnel/SKILL.md"
        skill_md.parent.mkdir(parents=True)
        skill_md.write_text(
            f"---\nname: edit-funnel\ndescription: {VALID_DESCRIPTION}\n",
            encoding="utf-8",
        )
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("no closed --- frontmatter block", errors[0])

    def test_name_directory_mismatch_fails(self):
        write_skill(self.root, "edit-funnel", "edit-funnels", VALID_DESCRIPTION)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("does not match directory", errors[0])

    def test_non_kebab_case_name_fails(self):
        write_skill(self.root, "Edit_Funnel", "Edit_Funnel", VALID_DESCRIPTION)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("not kebab-case", errors[0])

    def test_description_must_start_with_use_when(self):
        write_skill(
            self.root, "edit-funnel", "edit-funnel",
            "Edits hosted funnels through local CLI sync with preview and QA.",
        )
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("does not start with 'Use when'", errors[0])

    def test_stub_description_fails(self):
        write_skill(self.root, "edit-funnel", "edit-funnel", "Use when editing.")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("stub", errors[0])

    def test_overlong_description_fails(self):
        write_skill(
            self.root, "edit-funnel", "edit-funnel",
            "Use when " + "editing funnels " * 80,
        )
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("too long", errors[0])

    def test_host_agent_name_in_description_fails(self):
        write_skill(
            self.root, "preview-funnel", "preview-funnel",
            "Use when Codex needs to turn finished funnel copy into a"
            " temporary clickable local mockup for copy review.",
        )
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("host agent `Codex`", errors[0])
        self.assertIn("host-agnostic", errors[0])

    def test_host_agent_match_is_word_bounded(self):
        # "concludes" contains no standalone host name and must not trip the
        # host-agnostic check.
        write_skill(
            self.root, "edit-funnel", "edit-funnel",
            "Use when a review concludes that funnel copy needs a temporary"
            " local mockup before implementation.",
        )
        self.assertEqual(audit(self.root), [])

    def test_multiple_skills_all_audited(self):
        write_skill(self.root, "edit-funnel", "edit-funnel", VALID_DESCRIPTION)
        write_skill(self.root, "create-funnel", "wrong-name", VALID_DESCRIPTION)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("create-funnel", errors[0])

    def test_empty_skills_dir_fails_loudly(self):
        (self.root / "skills").mkdir(parents=True)
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("no skill directories found", errors[0])


if __name__ == "__main__":
    unittest.main()
