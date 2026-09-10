#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

(cd "$ROOT/tests" && python3 skill_frontmatter_audit_test.py)
python3 "$ROOT/tests/skill_frontmatter_audit.py" "$ROOT"

echo "PASS: skill frontmatter checks"
