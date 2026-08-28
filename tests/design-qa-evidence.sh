#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python3 "$ROOT/tests/design_qa_evidence_audit_test.py"
python3 "$ROOT/tests/design_qa_evidence_audit.py" "$ROOT"

echo "PASS: step-design QA evidence-tag checks"
