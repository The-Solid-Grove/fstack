#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

assert_file() {
  [ -f "$1" ] || fail "missing file: $1"
}

assert_executable() {
  [ -x "$1" ] || fail "missing executable bit: $1"
}

assert_contains() {
  local file="$1"
  local pattern="$2"
  grep -Eq "$pattern" "$file" || fail "$file does not contain pattern: $pattern"
}

assert_not_contains() {
  local file="$1"
  local pattern="$2"
  ! grep -Eq "$pattern" "$file" || fail "$file contains unwanted pattern: $pattern"
}

assert_no_template_markers() {
  local path="$1"
  if grep -RInE 'TODO|TBD|\[TODO|Replace with|placeholder' "$path" >/tmp/fstack-smoke-placeholders.$$ 2>/dev/null; then
    cat /tmp/fstack-smoke-placeholders.$$ >&2
    rm -f /tmp/fstack-smoke-placeholders.$$
    fail "template markers remain under $path"
  fi
  rm -f /tmp/fstack-smoke-placeholders.$$
}

validate_skill_dir() {
  local skill="$1"
  assert_no_template_markers "$skill"

  local validator="/Users/andrew/.codex/skills/.system/skill-creator/scripts/quick_validate.py"
  if [ -f "$validator" ] && command -v python3 >/dev/null 2>&1 && python3 -c 'import yaml' >/dev/null 2>&1; then
    python3 "$validator" "$skill"
  fi
}

check_readme() {
  assert_file "$ROOT/README.md"
  assert_file "$ROOT/VERSION"
  assert_contains "$ROOT/README.md" '^# fstack'
  assert_contains "$ROOT/VERSION" '^0\.2\.0$'
  assert_contains "$ROOT/README.md" 'Current version'
  assert_contains "$ROOT/README.md" 'Codex'
  assert_contains "$ROOT/README.md" 'Claude Code'
  assert_contains "$ROOT/README.md" 'Install'
  assert_contains "$ROOT/README.md" 'Update'
  assert_contains "$ROOT/README.md" 'Uninstall'
  assert_contains "$ROOT/README.md" 'edit-funnel'
  assert_contains "$ROOT/README.md" 'writing-funnel-copy'
}

check_setup() {
  assert_file "$ROOT/setup"
  assert_executable "$ROOT/setup"
  bash -n "$ROOT/setup"
}

check_skill() {
  local skill="$ROOT/skills/edit-funnel"
  assert_file "$skill/SKILL.md"
  assert_file "$skill/agents/openai.yaml"
  assert_contains "$skill/SKILL.md" '^name: edit-funnel$'
  assert_contains "$skill/SKILL.md" '^description:'
  assert_contains "$skill/SKILL.md" 'fgrove'
  assert_contains "$skill/SKILL.md" 'publish --env preview'
  assert_contains "$skill/agents/openai.yaml" 'display_name:'
  assert_contains "$skill/agents/openai.yaml" 'default_prompt:'
  validate_skill_dir "$skill"
}

check_copy_skill() {
  local skill="$ROOT/skills/writing-funnel-copy"
  assert_file "$skill/SKILL.md"
  assert_file "$skill/agents/openai.yaml"
  assert_file "$skill/references/funnel-psychology-framework.md"
  assert_file "$skill/references/funnel-paywall-best-practices.md"
  assert_file "$skill/references/funnel-conversion-best-practices.md"
  assert_contains "$skill/SKILL.md" '^name: writing-funnel-copy$'
  assert_contains "$skill/SKILL.md" '^description:'
  assert_contains "$skill/SKILL.md" 'references/funnel-psychology-framework.md'
  assert_contains "$skill/SKILL.md" 'references/funnel-paywall-best-practices.md'
  assert_contains "$skill/SKILL.md" 'references/funnel-conversion-best-practices.md'
  assert_contains "$skill/SKILL.md" 'Product name and what it does'
  assert_contains "$skill/SKILL.md" 'Five-column pre-work table'
  assert_contains "$skill/SKILL.md" 'Screen-by-screen spec'
  assert_contains "$skill/references/funnel-psychology-framework.md" '^id: funnel-psychology-framework$'
  assert_contains "$skill/references/funnel-psychology-framework.md" '^# Funnel Psychology Engine$'
  assert_contains "$skill/references/funnel-paywall-best-practices.md" '^id: funnel-paywall-best-practices$'
  assert_contains "$skill/references/funnel-paywall-best-practices.md" '^# Paywall Structure'
  assert_contains "$skill/references/funnel-conversion-best-practices.md" '^id: funnel-conversion-best-practices$'
  assert_contains "$skill/references/funnel-conversion-best-practices.md" '^# Web Funnel Conversion Best Practices$'
  assert_not_contains "$skill/references/funnel-conversion-best-practices.md" 'web2wave|Source:|Q4 2025|📊|⚠️'
  assert_contains "$skill/agents/openai.yaml" 'display_name:'
  assert_contains "$skill/agents/openai.yaml" 'default_prompt:'
  validate_skill_dir "$skill"
}

check_install_for_host() {
  local host="$1"
  local skill_parent="$2"
  local tmp_home
  tmp_home="$(mktemp -d)"

  HOME="$tmp_home" "$ROOT/setup" --host "$host" --repo-root "$ROOT" --quiet

  for skill_name in edit-funnel writing-funnel-copy; do
    local link="$tmp_home/$skill_parent/$skill_name"
    [ -L "$link" ] || fail "expected symlink at $link"
    [ "$(cd "$link" && pwd -P)" = "$ROOT/skills/$skill_name" ] || fail "wrong symlink target for $host"
  done

  rm -rf "$tmp_home"
}

check_installs() {
  check_install_for_host codex ".codex/skills"
  check_install_for_host claude ".claude/skills"
}

check_auto_install_fallback() {
  local tmp_home
  tmp_home="$(mktemp -d)"

  PATH="/usr/bin:/bin" HOME="$tmp_home" "$ROOT/setup" --host auto --repo-root "$ROOT" --quiet

  [ -L "$tmp_home/.codex/skills/edit-funnel" ] || fail "auto fallback did not install Codex skill"
  [ -L "$tmp_home/.claude/skills/edit-funnel" ] || fail "auto fallback did not install Claude skill"
  [ -L "$tmp_home/.codex/skills/writing-funnel-copy" ] || fail "auto fallback did not install Codex copy skill"
  [ -L "$tmp_home/.claude/skills/writing-funnel-copy" ] || fail "auto fallback did not install Claude copy skill"
  [ "$(cd "$tmp_home/.codex/skills/edit-funnel" && pwd -P)" = "$ROOT/skills/edit-funnel" ] || fail "wrong auto Codex symlink target"
  [ "$(cd "$tmp_home/.claude/skills/edit-funnel" && pwd -P)" = "$ROOT/skills/edit-funnel" ] || fail "wrong auto Claude symlink target"
  [ "$(cd "$tmp_home/.codex/skills/writing-funnel-copy" && pwd -P)" = "$ROOT/skills/writing-funnel-copy" ] || fail "wrong auto Codex copy symlink target"
  [ "$(cd "$tmp_home/.claude/skills/writing-funnel-copy" && pwd -P)" = "$ROOT/skills/writing-funnel-copy" ] || fail "wrong auto Claude copy symlink target"

  rm -rf "$tmp_home"
}

check_readme
check_setup
check_skill
check_copy_skill
check_installs
check_auto_install_fallback

echo "PASS: fstack smoke checks"
