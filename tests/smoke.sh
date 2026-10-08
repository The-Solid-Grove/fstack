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
    'funnel-rhythm-template.md', 'energy-screens.md', 'paywall-blueprints.md',
}
copy_skill = (r / 'skills/writing-funnel-copy/SKILL.md').read_text()
for ref in ('funnel-rhythm-template.md', 'energy-screens.md', 'paywall-blueprints.md'):
    assert f'references/{ref}' in copy_skill, ref
rhythm = (r / 'skills/writing-funnel-copy/references/funnel-rhythm-template.md').read_text()
assert '## Cadence rules' in rhythm and 'fgrove references steps' in rhythm
import re
viewport = re.compile(r'(?<![\w.])\d{3,4}x\d{3}(?![\w])')
checklist = (r / 'skills/qa-funnel/references/checklist.md').read_text()
table = set(viewport.findall(checklist[checklist.index('## Visual Pass'):]))
assert {'375x667', '375x548', '1280x800'} <= table, table
for p in [*r.glob('skills/**/*.md'), *r.glob('skills/**/*.yaml'), *r.glob('docs/*.md')]:
    stray = set(viewport.findall(p.read_text())) - table
    assert not stray, (p, stray)
for skill in ('qa-funnel/SKILL.md', 'edit-funnel/SKILL.md', 'preview-funnel/SKILL.md'):
    assert 'checklist.md#visual-pass' in (r / 'skills' / skill).read_text(), skill
assert not (r / 'skills/writing-funnel-copy/references/funnels-research').exists()
assert 'Reach second step | 30–60%' in (r / 'skills/writing-funnel-copy/references/funnel-best-practices.md').read_text()
for p in r.glob('skills/**/*.md'):
    assert 'Reach mid-onboarding' not in p.read_text(), p
PYEOF
echo "PASS: skills install and route correctly"
