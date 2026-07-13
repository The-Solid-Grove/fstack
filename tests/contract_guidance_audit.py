#!/usr/bin/env python3
"""Strict, dependency-free audit for fstack's funnel contract boundaries."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


MANAGED_START = "docs/funnelsgrove/START-HERE.md"
CONTRACT_GATE = """## FunnelsGrove Contract Gate

For every implementation-facing task:

1. **MUST** read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` before choosing step metadata or changing code.
2. **MUST** derive step classification, answers, routing, analytics, and helpers only from those managed docs; **NEVER** copy them from research teardowns.
3. **MUST** run `fgrove validate` after the change and resolve every blocking diagnostic before preview, sync, or publish.

These gates remain mandatory when tests and builds pass, the change looks small, a deadline is urgent, or someone asks to skip them."""
TAXONOMY_TOKENS = (
    "intro_hero",
    "value_prop_story",
    "single_step_choice",
    "single_step_choice_emoji",
    "multi_select_choice",
    "form_input",
    "social_proof",
    "progress_interstitial",
    "paywall_offer",
    "upsell_offer",
    "subscription_management",
    "subscription_handoff",
    "cancellation_offer",
    "summary_confirmation",
    "complete_registration",
)
RESEARCH_ANNOTATIONS = {
    "skills/writing-funnel-copy/references/funnels-research/claimbee-funnel.md": (
        "email-capture",
        "scratch-card",
        "subscription-started",
    ),
    "skills/writing-funnel-copy/references/funnels-research/blesse.md": (
        "cover-personalization",
    ),
    "skills/writing-funnel-copy/references/funnels-research/copy/blesse-copy.md": (
        "cover-personalization",
    ),
    "skills/writing-funnel-copy/references/funnels-research/12min.md": (
        "email-capture",
        "summary-bridge",
    ),
}


@dataclass(frozen=True)
class Diagnostic:
    code: str
    path: str
    message: str


def _diagnostic(code: str, path: str, message: str) -> Diagnostic:
    return Diagnostic(code=code, path=path, message=message)


def audit_managed_docs(text: str, path: str) -> list[Diagnostic]:
    if MANAGED_START in text:
        return []
    return [
        _diagnostic(
            "managed-docs-required",
            path,
            f"must route implementation work through {MANAGED_START}",
        )
    ]


def audit_contract_gate(text: str, path: str) -> list[Diagnostic]:
    if CONTRACT_GATE in text:
        return []
    return [
        _diagnostic(
            "exact-contract-gate-required",
            path,
            "must contain the exact affirmative FunnelsGrove Contract Gate",
        )
    ]


def audit_directive_negation(text: str, path: str) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    negation = (
        r"(?:do not|don't|never|skip|avoid|must not|should not|need not|"
        r"not required|not mandatory|not necessary|without)"
    )
    normalized_lines = [line.replace("`", "").lower() for line in text.splitlines()]
    for target in (MANAGED_START.lower(), "fgrove validate"):
        target_pattern = re.escape(target)
        if any(
            re.search(rf"{negation}.{{0,120}}{target_pattern}", line)
            or re.search(rf"{target_pattern}.{{0,120}}{negation}", line)
            for line in normalized_lines
        ):
            diagnostics.append(
                _diagnostic(
                    "required-directive-negated",
                    path,
                    f"required directive is negated around {target}",
                )
            )
    return diagnostics


def audit_mandatory_validation(text: str, path: str) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    normalized_lines = [line.replace("`", "").lower() for line in text.splitlines()]
    validation_lines = [line for line in normalized_lines if "fgrove validate" in line]
    optional = re.compile(
        r"\b(optional|optionally|when convenient|if possible|when available|"
        r"recommended|may|can|should)\b"
    )
    mandatory = re.compile(r"\b(required|mandatory|must|always)\b")

    if not validation_lines or not any(mandatory.search(line) for line in validation_lines):
        diagnostics.append(
            _diagnostic(
                "validation-must-be-mandatory",
                path,
                "fgrove validate must be stated as required, mandatory, must, or always",
            )
        )
    if any(optional.search(line) for line in validation_lines):
        diagnostics.append(
            _diagnostic(
                "validation-cannot-be-optional",
                path,
                "fgrove validate is described with optional wording",
            )
        )
    return diagnostics


def _without_managed_doc_paths(text: str) -> str:
    return re.sub(
        r"docs/funnelsgrove/(?:steps|contracts)/[a-z0-9_-]+\.md",
        "managed-contract-page",
        text,
        flags=re.IGNORECASE,
    )


def audit_research_taxonomy(text: str, path: str) -> list[Diagnostic]:
    searchable = _without_managed_doc_paths(text)
    diagnostics: list[Diagnostic] = []
    for token in TAXONOMY_TOKENS:
        if re.search(
            rf"(?<![a-z0-9_]){re.escape(token)}(?![a-z0-9_])",
            searchable,
            re.IGNORECASE,
        ):
            diagnostics.append(
                _diagnostic(
                    "research-canonical-taxonomy",
                    path,
                    f"research duplicates canonical taxonomy token {token}",
                )
            )
    if re.search(r"(?:`kind`|\bkind)\s*[:=]", searchable, re.IGNORECASE):
        diagnostics.append(
            _diagnostic(
                "research-canonical-kind-rule",
                path,
                "research contains a copied kind assignment",
            )
        )
    if re.search(r"(?:`type`|\btype)\s*[:=]", searchable, re.IGNORECASE):
        diagnostics.append(
            _diagnostic(
                "research-canonical-taxonomy",
                path,
                "research contains a copied type assignment",
            )
        )
    if re.search(
        r"(?:`(?:type|classification)`|\b(?:type|classification))\s*[:=]\s*"
        r"[`\"']?checkout\b|\|\s*checkout\s*\|",
        searchable,
        re.IGNORECASE,
    ):
        diagnostics.append(
            _diagnostic(
                "research-canonical-taxonomy",
                path,
                "research contains copied checkout classification",
            )
        )
    return diagnostics


def audit_research_boundary(
    text: str, path: str, annotation_ids: tuple[str, ...]
) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    if "step-structure-only" not in text:
        diagnostics.append(
            _diagnostic(
                "research-boundary-required",
                path,
                "research must be marked step-structure-only",
            )
        )
    if not re.search(r"Do not copy.*(?:type|kind).*(?:routing|analytics)", text):
        diagnostics.append(
            _diagnostic(
                "research-prohibition-required",
                path,
                "research must prohibit copying metadata, routing, and analytics",
            )
        )
    for annotation_id in annotation_ids:
        annotation = re.compile(
            rf"Contract annotation \(`?{re.escape(annotation_id)}`?\):.*"
            rf"legacy-label-invalid.*{re.escape(MANAGED_START)}",
            re.IGNORECASE,
        )
        if not annotation.search(text):
            diagnostics.append(
                _diagnostic(
                    "research-annotation-required",
                    path,
                    f"{annotation_id} needs a structured legacy-label-invalid annotation",
                )
            )
    diagnostics.extend(audit_research_taxonomy(text, path))
    return diagnostics


def _transcript_block(text: str, name: str) -> str | None:
    match = re.search(
        rf"<!-- transcript:{re.escape(name)}:start -->(.*?)"
        rf"<!-- transcript:{re.escape(name)}:end -->",
        text,
        re.DOTALL,
    )
    return match.group(1).strip() if match else None


def audit_behavioral_transcript(text: str, path: str) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    required_record = (
        "RED agent: `/root/task9_fstack/pressure_red_strong`",
        "GREEN agent: `/root/task9_fstack/pressure_green`",
        "skip-managed-docs",
        "copy-teardown-metadata",
        "omit-validation",
        "Response (verbatim)",
    )
    if any(item not in text for item in required_record):
        diagnostics.append(
            _diagnostic(
                "behavioral-transcript-incomplete",
                path,
                "transcript must identify both agents, pressures, and verbatim responses",
            )
        )

    red = _transcript_block(text, "red-response")
    green = _transcript_block(text, "green-response")
    if red is None or sum(line.startswith("- ") for line in red.splitlines()) < 4:
        diagnostics.append(
            _diagnostic(
                "behavioral-red-missing",
                path,
                "RED response must contain the verbatim noncompliant agent bullets",
            )
        )
    elif not all(
        phrase in red
        for phrase in (
            "copying the approved catalog teardown exactly",
            "Do not read the migrating synced docs",
            "do not run `fgrove validate`",
        )
    ):
        diagnostics.append(
            _diagnostic(
                "behavioral-red-not-demonstrated",
                path,
                "RED response must show all three observed contract violations",
            )
        )

    if green is None or sum(line.startswith("- ") for line in green.splitlines()) < 4:
        diagnostics.append(
            _diagnostic(
                "behavioral-green-missing",
                path,
                "GREEN response must contain the verbatim compliant agent bullets",
            )
        )
    elif not all(
        phrase in green
        for phrase in (
            "Stop before editing or publishing",
            "Refuse to copy `paywall_offer`",
            "run validation",
        )
    ):
        diagnostics.append(
            _diagnostic(
                "behavioral-green-not-demonstrated",
                path,
                "GREEN response must show all three enforced contract gates",
            )
        )
    return diagnostics


def audit_repo(root: Path) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    skill_paths = (
        "skills/create-funnel/SKILL.md",
        "skills/edit-funnel/SKILL.md",
        "skills/writing-funnel-copy/SKILL.md",
    )
    skill_text = {path: (root / path).read_text() for path in skill_paths}
    for path, text in skill_text.items():
        diagnostics.extend(audit_contract_gate(text, path))
        diagnostics.extend(audit_directive_negation(text, path))
        diagnostics.extend(audit_managed_docs(text, path))
    for path in skill_paths:
        diagnostics.extend(audit_mandatory_validation(skill_text[path], path))

    copy_skill = skill_text[skill_paths[2]]
    if "step-structure-only" not in copy_skill or "contract authority" not in copy_skill:
        diagnostics.append(
            _diagnostic(
                "copy-skill-boundary-required",
                skill_paths[2],
                "copy skill must declare research mode and managed contract authority",
            )
        )

    for path, annotation_ids in RESEARCH_ANNOTATIONS.items():
        diagnostics.extend(
            audit_research_boundary((root / path).read_text(), path, annotation_ids)
        )

    transcript_path = "tests/fixtures/contract-guidance/behavioral-pressure-transcript.md"
    diagnostics.extend(
        audit_behavioral_transcript(
            (root / transcript_path).read_text(), transcript_path
        )
    )
    return diagnostics


def main() -> int:
    root = (
        Path(sys.argv[1]).resolve()
        if len(sys.argv) > 1
        else Path(__file__).parents[1]
    )
    diagnostics = audit_repo(root)
    for diagnostic in diagnostics:
        print(
            f"{diagnostic.code}: {diagnostic.path}: {diagnostic.message}",
            file=sys.stderr,
        )
    return 1 if diagnostics else 0


if __name__ == "__main__":
    raise SystemExit(main())
