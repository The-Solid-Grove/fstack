#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

# Syntax-check every shell script the repo relies on. Convention and wiring
# checks (shebang, strict mode, audit/test pairing, runner coverage) live in
# suite_hygiene_audit.py.
for script in "$ROOT"/tests/*.sh "$ROOT/setup" "$ROOT/scripts/ensure-fgrove-cli"; do
  bash -n "$script" || {
    echo "FAIL: bash -n rejected $script" >&2
    exit 1
  }
done

(cd "$ROOT/tests" && python3 suite_hygiene_audit_test.py)
python3 "$ROOT/tests/suite_hygiene_audit.py" "$ROOT"

echo "PASS: suite hygiene checks"
