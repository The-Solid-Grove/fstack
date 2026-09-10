#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python3 "$ROOT/tests/agents_yaml_audit_test.py"
python3 "$ROOT/tests/agents_yaml_audit.py" "$ROOT"

echo "PASS: agents/openai.yaml interface checks"
