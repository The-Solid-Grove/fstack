#!/usr/bin/env python3

from pathlib import Path
import unittest

from contract_guidance_audit import (
    CONTRACT_GATE,
    audit_behavioral_transcript,
    audit_contract_gate,
    audit_directive_negation,
    audit_managed_docs,
    audit_mandatory_validation,
    audit_repo,
    audit_research_taxonomy,
)


ROOT = Path(__file__).parents[1]
FIXTURES = ROOT / "tests/fixtures/contract-guidance"


def codes(diagnostics):
    return {diagnostic.code for diagnostic in diagnostics}


class ContractGuidanceAuditTest(unittest.TestCase):
    def test_behavioral_red_green_transcript_is_verbatim_and_complete(self):
        path = FIXTURES / "behavioral-pressure-transcript.md"
        self.assertEqual(audit_behavioral_transcript(path.read_text(), str(path)), [])

    def test_exact_contract_gate_rejects_softened_mutation(self):
        self.assertEqual(audit_contract_gate(CONTRACT_GATE, "skill.md"), [])
        softened = CONTRACT_GATE.replace("**MUST** read", "**SHOULD** read")
        self.assertIn(
            "exact-contract-gate-required",
            codes(audit_contract_gate(softened, "skill.md")),
        )

    def test_negated_validation_is_rejected(self):
        text = CONTRACT_GATE + "\n\n" + (FIXTURES / "negated-validation.md").read_text()
        self.assertEqual(audit_contract_gate(text, "negated-validation.md"), [])
        self.assertIn(
            "required-directive-negated",
            codes(audit_directive_negation(text, "negated-validation.md")),
        )

    def test_negated_managed_docs_are_rejected(self):
        text = CONTRACT_GATE + "\n\n" + (
            FIXTURES / "negated-managed-docs.md"
        ).read_text()
        self.assertEqual(audit_contract_gate(text, "negated-managed-docs.md"), [])
        self.assertIn(
            "required-directive-negated",
            codes(audit_directive_negation(text, "negated-managed-docs.md")),
        )

    def test_backticked_kind_assignment_is_rejected(self):
        text = (FIXTURES / "backticked-kind-assignment.md").read_text()
        self.assertIn(
            "research-canonical-kind-rule",
            codes(audit_research_taxonomy(text, "backticked-kind-assignment.md")),
        )

    def test_optional_validation_mutation_is_rejected(self):
        text = (FIXTURES / "optional-validation.md").read_text()
        self.assertIn(
            "validation-cannot-be-optional",
            codes(audit_mandatory_validation(text, "optional-validation.md")),
        )
        self.assertIn(
            "validation-must-be-mandatory",
            codes(audit_mandatory_validation(text, "optional-validation.md")),
        )

    def test_altered_punctuation_does_not_hide_stale_labels(self):
        text = (FIXTURES / "altered-punctuation-stale-labels.md").read_text()
        diagnostics = audit_research_taxonomy(text, "altered-labels.md")
        messages = {diagnostic.message for diagnostic in diagnostics}
        self.assertIn(
            "research duplicates canonical taxonomy token paywall_offer", messages
        )
        self.assertIn(
            "research duplicates canonical taxonomy token multi_select_choice",
            messages,
        )

    def test_skip_managed_docs_pressure_is_rejected(self):
        text = (FIXTURES / "skip-managed-docs.md").read_text()
        self.assertIn(
            "managed-docs-required",
            codes(audit_managed_docs(text, "skip-managed-docs.md")),
        )

    def test_copy_teardown_metadata_pressure_is_rejected(self):
        text = (FIXTURES / "copy-teardown-metadata.md").read_text()
        diagnostics = audit_research_taxonomy(text, "copy-teardown-metadata.md")
        self.assertIn("research-canonical-taxonomy", codes(diagnostics))
        self.assertIn(
            "research contains copied checkout classification",
            {diagnostic.message for diagnostic in diagnostics},
        )

    def test_current_skills_pass_all_pressure_guardrails(self):
        self.assertEqual(audit_repo(ROOT), [])


if __name__ == "__main__":
    unittest.main()
