#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
bash -n "$ROOT/setup" "$ROOT/scripts/ensure-fgrove-cli" "$ROOT/scripts/check-fstack-update"
for host in codex claude; do
  HOME="$TMP/$host" "$ROOT/setup" --host "$host" --skip-fgrove-cli --skip-update-check --quiet
  for skill in create-funnel edit-funnel preview-funnel design-funnel writing-funnel-copy web2app-essentials qa-funnel; do
    link="$TMP/$host/.$host/skills/$skill"
    test -L "$link"
    test "$(cd "$link" && pwd -P)" = "$ROOT/skills/$skill"
    test -f "$link/SKILL.md"
    test -f "$link/agents/openai.yaml"
  done
done
python3 - "$ROOT" <<'PYEOF'
from pathlib import Path
import sys
r = Path(sys.argv[1])
for skill in ('create-funnel', 'edit-funnel'):
    assert 'qa-funnel' in (r / 'skills' / skill / 'SKILL.md').read_text()
for skill in r.glob('skills/*/SKILL.md'):
    assert str(skill.relative_to(r)) in (r / 'README.md').read_text(), skill
assert {p.name for p in (r / 'skills/writing-funnel-copy/references').rglob('*.md')} == {
    'funnel-best-practices.md', 'funnel-psychology-framework.md',
}
assert not (r / 'skills/writing-funnel-copy/references/funnels-research').exists()
assert 'Reach second step | 30–60%' in (r / 'skills/writing-funnel-copy/references/funnel-best-practices.md').read_text()
for p in r.glob('skills/**/*.md'):
    assert 'Reach mid-onboarding' not in p.read_text(), p
PYEOF
echo "PASS: skills install and route correctly"
