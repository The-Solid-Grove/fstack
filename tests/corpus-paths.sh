#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

(cd "$ROOT/tests" && python3 corpus_path_refs_audit_test.py)
python3 "$ROOT/tests/corpus_path_refs_audit.py" "$ROOT"
