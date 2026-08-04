#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

(cd "$ROOT/tests" && python3 viewport_canon_audit_test.py)
python3 "$ROOT/tests/viewport_canon_audit.py" "$ROOT"
