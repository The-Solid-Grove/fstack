#!/usr/bin/env bash
set -euo pipefail

# Every skill must work when the skills CLI (`npx skills add`) copies only
# `skills/<name>/` into an agent's skill folder, next to the other fstack skills.
# Nothing under skills/ may therefore point above the skills/ directory or
# require a git checkout of the pack.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
status=0

# 1. No path climbs out of skills/: `../../` is allowed only inside references/
#    (reaching a sibling skill), and never from a SKILL.md or anywhere deeper.
while IFS= read -r hit; do
  file="${hit%%:*}"
  case "$file" in
    "$ROOT"/skills/*/references/*) continue ;;
  esac
  echo "FAIL: $hit" >&2
  status=1
done < <(grep -rn '\.\./\.\./' "$ROOT/skills" || true)
if grep -rn '\.\./\.\./\.\./' "$ROOT/skills"; then
  echo "FAIL: a path climbs above skills/" >&2
  status=1
fi

# 2. No instruction depends on the pack checkout.
if grep -rniE 'fstack checkout|<fstack-checkout>|fstack_checkout/scripts' "$ROOT/skills" --include='*.md' --include='*.yaml' --include='*.mjs' --include='*.py' ; then
  echo "FAIL: skills must not depend on an fstack checkout" >&2
  status=1
fi

# 3. Scripts a skill names live inside that skill.
for skill in "$ROOT"/skills/*/; do
  while IFS= read -r script; do
    [ -f "$skill/$script" ] || { echo "FAIL: $skill names missing $script" >&2; status=1; }
  done < <(grep -ohE '`?scripts/[A-Za-z0-9_.-]+' "$skill/SKILL.md" "$skill"/references/*.md 2>/dev/null | tr -d '`' | sort -u)
done

[ "$status" -eq 0 ] && echo "PASS: skills are portable to skills-CLI installs"
exit "$status"
