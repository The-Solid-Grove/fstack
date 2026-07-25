#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

(cd "$ROOT/tests" && python3 reference_links_audit_test.py)
python3 "$ROOT/tests/reference_links_audit.py" "$ROOT"
