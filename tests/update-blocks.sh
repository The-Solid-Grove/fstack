#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python3 "$ROOT/tests/update_blocks_audit_test.py"
python3 "$ROOT/tests/update_blocks_audit.py" "$ROOT"

echo "PASS: post-course update block checks"
