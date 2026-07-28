#!/usr/bin/env python3

from pathlib import Path
import tempfile
import unittest

from agents_yaml_audit import audit_repo, audit_yaml


ROOT = Path(__file__).parents[1]

CONFORMING = """\
interface:
  display_name: "Edit Funnel"
  short_description: "Edit, local-preview, and QA FunnelsGrove funnels"
  default_prompt: "Use $edit-funnel to load a funnel and make the edits."
"""

MISSING_KEY = """\
interface:
  display_name: "Edit Funnel"
  default_prompt: "Use $edit-funnel to load a funnel and make the edits."
"""

EMPTY_VALUE = """\
interface:
  display_name: ""
  short_description: "Edit, local-preview, and QA FunnelsGrove funnels"
  default_prompt: "Use $edit-funnel to load a funnel and make the edits."
"""

WRONG_SKILL_REF = """\
interface:
  display_name: "Edit Funnel"
  short_description: "Edit, local-preview, and QA FunnelsGrove funnels"
  default_prompt: "Use $create-funnel to load a funnel and make the edits."
"""

LONG_DESCRIPTION = """\
interface:
  display_name: "Edit Funnel"
  short_description: "{}"
  default_prompt: "Use $edit-funnel to load a funnel and make the edits."
""".format("x" * 81)


def codes(diagnostics):
    return {diagnostic.code for diagnostic in diagnostics}


class AgentsYamlAuditTest(unittest.TestCase):
    def test_conforming_yaml_passes(self):
        self.assertEqual(audit_yaml(CONFORMING, "openai.yaml", "edit-funnel"), [])

    def test_missing_key_is_rejected(self):
        self.assertIn(
            "openai-yaml-missing-key",
            codes(audit_yaml(MISSING_KEY, "openai.yaml", "edit-funnel")),
        )

    def test_empty_value_is_rejected(self):
        self.assertIn(
            "openai-yaml-missing-key",
            codes(audit_yaml(EMPTY_VALUE, "openai.yaml", "edit-funnel")),
        )

    def test_prompt_must_reference_own_skill(self):
        self.assertIn(
            "openai-yaml-prompt-skill-ref",
            codes(audit_yaml(WRONG_SKILL_REF, "openai.yaml", "edit-funnel")),
        )

    def test_long_short_description_is_rejected(self):
        self.assertIn(
            "openai-yaml-short-description-length",
            codes(audit_yaml(LONG_DESCRIPTION, "openai.yaml", "edit-funnel")),
        )

    def test_missing_yaml_for_skill_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / "skills" / "my-skill"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: my-skill\n---\n")
            self.assertEqual(codes(audit_repo(root)), {"openai-yaml-missing"})

    def test_orphan_yaml_without_skill_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            agents = root / "skills" / "gone-skill" / "agents"
            agents.mkdir(parents=True)
            (agents / "openai.yaml").write_text(CONFORMING)
            self.assertEqual(codes(audit_repo(root)), {"openai-yaml-orphan"})

    def test_current_repo_conforms(self):
        self.assertEqual([d.render() for d in audit_repo(ROOT)], [])


if __name__ == "__main__":
    unittest.main()
