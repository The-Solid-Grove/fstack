#!/usr/bin/env bash
set -euo pipefail

# Offline test for scripts/reference-strip using a saved journey fixture.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
out="$(python3 "$ROOT/scripts/reference-strip" --file "$ROOT/tests/fixtures/reference-strip/journey.json")"
grep -qx 'Strip: Q E Q Q Q E L P @ \$' <<<"$out"
grep -q 'energy share 33% · longest question run 3 · first energy screen 2' <<<"$out"
grep -q '  10 \$ paywall: Start your plan' <<<"$out"
if python3 "$ROOT/scripts/reference-strip" >/dev/null 2>&1; then
  echo "FAIL: missing arguments should exit non-zero" >&2
  exit 1
fi
echo "PASS: reference strip"
