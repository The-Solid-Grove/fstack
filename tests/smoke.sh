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
  if grep -RInE --exclude-dir=funnels-research 'TODO|TBD|\[TODO|Replace with|placeholder' "$path" >/tmp/fstack-smoke-placeholders.$$ 2>/dev/null; then
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
  assert_file "$ROOT/docs/funnel-qa-checklist.md"
  assert_contains "$ROOT/README.md" '^# fstack'
  assert_contains "$ROOT/VERSION" '^0\.5\.4$'
  assert_contains "$ROOT/README.md" 'Current version'
  assert_contains "$ROOT/README.md" 'Codex'
  assert_contains "$ROOT/README.md" 'Claude Code'
  assert_contains "$ROOT/README.md" 'Install'
  assert_contains "$ROOT/README.md" 'Update'
  assert_contains "$ROOT/README.md" 'Uninstall'
  assert_contains "$ROOT/README.md" 'create-funnel'
  assert_contains "$ROOT/README.md" 'edit-funnel'
  assert_contains "$ROOT/README.md" 'writing-funnel-copy'
  assert_contains "$ROOT/README.md" 'preview-funnel'
  assert_contains "$ROOT/README.md" 'local preview'
  assert_contains "$ROOT/README.md" 'Ask whether to publish'
  assert_contains "$ROOT/README.md" 'content-fit audit'
  assert_contains "$ROOT/README.md" 'small.*375.?x.?667'
  assert_contains "$ROOT/README.md" 'medium.*393.?x.?852'
  assert_contains "$ROOT/README.md" 'large.*402.?x.?874'
  assert_contains "$ROOT/README.md" 'desktop-small.*1280.?x.?800'
  assert_contains "$ROOT/README.md" 'preview QA'
  assert_contains "$ROOT/README.md" 'production QA'
  assert_contains "$ROOT/README.md" 'Image performance'
  assert_contains "$ROOT/README.md" 'AVIF/WebP'
  assert_contains "$ROOT/README.md" 'manifest-driven next-step image preloading'
  assert_contains "$ROOT/README.md" 'meaningful route slugs'
  assert_contains "$ROOT/README.md" '/step-1'
  assert_contains "$ROOT/README.md" 'docs/funnel-qa-checklist\.md'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'preview build'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'every step'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'every branch'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'A/B experiment'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'Apple Pay'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'Google Pay'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'Stripe dashboard'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'Visual Pass'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" '375x667'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" '393x852'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" '402x874'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" '1280x800'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'Image Performance'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'imageVariants'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'AVIF/WebP'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'assetIds'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'second-stage discount'
  assert_contains "$ROOT/docs/funnel-qa-checklist.md" 'complete registration'
}

check_setup() {
  assert_file "$ROOT/setup"
  assert_executable "$ROOT/setup"
  bash -n "$ROOT/setup"
  assert_file "$ROOT/scripts/ensure-fgrove-cli"
  assert_executable "$ROOT/scripts/ensure-fgrove-cli"
  bash -n "$ROOT/scripts/ensure-fgrove-cli"
}

check_skill() {
  local skill="$ROOT/skills/edit-funnel"
  assert_file "$skill/SKILL.md"
  assert_file "$skill/agents/openai.yaml"
  assert_contains "$skill/SKILL.md" '^name: edit-funnel$'
  assert_contains "$skill/SKILL.md" '^description:'
  assert_contains "$skill/SKILL.md" 'fgrove'
  assert_contains "$skill/SKILL.md" 'ensure-fgrove-cli'
  assert_contains "$skill/SKILL.md" 'AGENTS.md'
  assert_contains "$skill/SKILL.md" 'agent.md'
  assert_contains "$skill/SKILL.md" 'publish --env preview'
  assert_contains "$skill/SKILL.md" 'local preview'
  assert_contains "$skill/SKILL.md" 'content-fit audit'
  assert_contains "$skill/SKILL.md" 'small.*375.?x.?667'
  assert_contains "$skill/SKILL.md" 'medium.*393.?x.?852'
  assert_contains "$skill/SKILL.md" 'large.*402.?x.?874'
  assert_contains "$skill/SKILL.md" 'desktop-small.*1280.?x.?800'
  assert_contains "$skill/SKILL.md" 'Ask the user whether to publish'
  assert_contains "$skill/SKILL.md" 'production URL'
  assert_contains "$skill/SKILL.md" 'preview-build coverage'
  assert_contains "$skill/SKILL.md" 'docs/funnel-qa-checklist\.md'
  assert_contains "$skill/SKILL.md" 'every step'
  assert_contains "$skill/SKILL.md" 'every branch'
  assert_contains "$skill/SKILL.md" 'A/B experiment'
  assert_contains "$skill/SKILL.md" 'submit email|add.*email'
  assert_contains "$skill/SKILL.md" 'test payment|payment path'
  assert_contains "$skill/SKILL.md" 'Apple Pay'
  assert_contains "$skill/SKILL.md" 'Google Pay'
  assert_contains "$skill/SKILL.md" 'complete registration'
  assert_contains "$skill/SKILL.md" 'larger discount'
  assert_contains "$skill/SKILL.md" '/manage-subscription'
  assert_contains "$skill/SKILL.md" 'cancellation flow'
  assert_contains "$skill/SKILL.md" 'Update Local Project Packages'
  assert_contains "$skill/SKILL.md" 'package manager'
  assert_contains "$skill/SKILL.md" 'package-lock\.json'
  assert_contains "$skill/SKILL.md" 'pnpm-lock\.yaml'
  assert_contains "$skill/SKILL.md" 'yarn\.lock'
  assert_contains "$skill/SKILL.md" 'bun\.lockb'
  assert_contains "$skill/SKILL.md" 'npm outdated'
  assert_contains "$skill/SKILL.md" 'pnpm outdated'
  assert_contains "$skill/SKILL.md" 'npm update'
  assert_contains "$skill/SKILL.md" 'Image Performance Lock'
  assert_contains "$skill/SKILL.md" 'AVIF/WebP'
  assert_contains "$skill/SKILL.md" 'funnelManifest\.assets'
  assert_contains "$skill/SKILL.md" 'assetIds'
  assert_contains "$skill/SKILL.md" 'next-step preloads'
  assert_contains "$skill/SKILL.md" 'public route'
  assert_contains "$skill/SKILL.md" '/step-1'
  assert_contains "$skill/agents/openai.yaml" 'display_name:'
  assert_contains "$skill/agents/openai.yaml" 'default_prompt:'
  validate_skill_dir "$skill"
}

check_fgrove_cli_helper() {
  local tmp_dir fake_bin install_log latest_file installed_file
  tmp_dir="$(mktemp -d)"
  fake_bin="$tmp_dir/bin"
  install_log="$tmp_dir/install.log"
  latest_file="$tmp_dir/latest"
  installed_file="$tmp_dir/installed"
  mkdir -p "$fake_bin"

  cat > "$fake_bin/fgrove" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
if [ "${1:-}" = "--version" ]; then
  echo "fgrove $(cat "$FGROVE_INSTALLED_FILE")"
  exit 0
fi
echo "unexpected fgrove call: $*" >&2
exit 1
EOF
  chmod +x "$fake_bin/fgrove"

  cat > "$fake_bin/npm" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
if [ "${1:-}" = "view" ] && [ "${2:-}" = "@funnelsgrove/cli" ] && [ "${3:-}" = "version" ]; then
  cat "$FGROVE_LATEST_FILE"
  exit 0
fi
if [ "${1:-}" = "install" ]; then
  printf '%s\n' "$*" >> "$FGROVE_INSTALL_LOG"
  exit 0
fi
echo "unexpected npm call: $*" >&2
exit 1
EOF
  chmod +x "$fake_bin/npm"

  echo "1.2.3" > "$latest_file"
  echo "1.2.3" > "$installed_file"
  PATH="$fake_bin:$PATH" \
    FGROVE_LATEST_FILE="$latest_file" \
    FGROVE_INSTALLED_FILE="$installed_file" \
    FGROVE_INSTALL_LOG="$install_log" \
    "$ROOT/scripts/ensure-fgrove-cli" --quiet
  [ ! -f "$install_log" ] || fail "helper installed fgrove when versions matched"

  echo "1.2.4" > "$installed_file"
  PATH="$fake_bin:$PATH" \
    FGROVE_LATEST_FILE="$latest_file" \
    FGROVE_INSTALLED_FILE="$installed_file" \
    FGROVE_INSTALL_LOG="$install_log" \
    "$ROOT/scripts/ensure-fgrove-cli" --quiet
  [ ! -f "$install_log" ] || fail "helper downgraded a newer local fgrove CLI"

  echo "1.2.2" > "$installed_file"
  PATH="$fake_bin:$PATH" \
    FGROVE_LATEST_FILE="$latest_file" \
    FGROVE_INSTALLED_FILE="$installed_file" \
    FGROVE_INSTALL_LOG="$install_log" \
    "$ROOT/scripts/ensure-fgrove-cli" --quiet
  grep -Eq '^install -g @funnelsgrove/cli@latest$' "$install_log" || fail "helper did not install latest fgrove CLI"

  rm -rf "$tmp_dir"
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
  assert_contains "$skill/SKILL.md" 'preview-funnel'
  assert_contains "$skill/SKILL.md" 'visualize|visualizing'
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

check_preview_skill() {
  local skill="$ROOT/skills/preview-funnel"
  assert_file "$skill/SKILL.md"
  assert_file "$skill/agents/openai.yaml"
  assert_contains "$skill/SKILL.md" '^name: preview-funnel$'
  assert_contains "$skill/SKILL.md" '^description:'
  assert_contains "$skill/SKILL.md" 'funnel copy'
  assert_contains "$skill/SKILL.md" 'mockup'
  assert_contains "$skill/SKILL.md" 'sticky'
  assert_contains "$skill/SKILL.md" 'python3 -m http.server'
  assert_contains "$skill/SKILL.md" '375x667'
  assert_contains "$skill/SKILL.md" '393x852'
  assert_contains "$skill/SKILL.md" '402x874'
  assert_contains "$skill/SKILL.md" '1280x800'
  assert_contains "$skill/SKILL.md" 'throwaway|temporary'
  assert_contains "$skill/agents/openai.yaml" 'display_name:'
  assert_contains "$skill/agents/openai.yaml" 'default_prompt:'
  validate_skill_dir "$skill"
}

check_create_skill() {
  local skill="$ROOT/skills/create-funnel"
  assert_file "$skill/SKILL.md"
  assert_file "$skill/agents/openai.yaml"
  assert_contains "$skill/SKILL.md" '^name: create-funnel$'
  assert_contains "$skill/SKILL.md" '^description:'
  assert_contains "$skill/SKILL.md" 'apps/funnel-template'
  assert_contains "$skill/SKILL.md" 'fgrove create'
  assert_contains "$skill/SKILL.md" '[Rr]eskin'
  assert_contains "$skill/SKILL.md" 'funnel.manifest.ts'
  assert_contains "$skill/SKILL.md" 'discount-on-close'
  assert_contains "$skill/SKILL.md" '375x667'
  assert_contains "$skill/SKILL.md" '393x852'
  assert_contains "$skill/SKILL.md" '402x874'
  assert_contains "$skill/SKILL.md" '1280x800'
  assert_contains "$skill/SKILL.md" 'qa-checklist'
  assert_contains "$skill/SKILL.md" 'Stripe dashboard'
  assert_contains "$skill/SKILL.md" 'sync up'
  assert_contains "$skill/SKILL.md" 'publish --env preview'
  assert_contains "$skill/SKILL.md" 'AVIF/WebP'
  assert_contains "$skill/SKILL.md" 'funnelManifest\.assets'
  assert_contains "$skill/SKILL.md" 'assetIds'
  assert_contains "$skill/SKILL.md" 'meaningful route slug'
  assert_contains "$skill/SKILL.md" '/step-1'
  assert_contains "$skill/agents/openai.yaml" 'display_name:'
  assert_contains "$skill/agents/openai.yaml" 'default_prompt:'
  validate_skill_dir "$skill"
}

check_install_for_host() {
  local host="$1"
  local skill_parent="$2"
  local tmp_home
  tmp_home="$(mktemp -d)"

  HOME="$tmp_home" "$ROOT/setup" --host "$host" --repo-root "$ROOT" --skip-fgrove-cli --quiet

  for skill_name in create-funnel edit-funnel preview-funnel writing-funnel-copy; do
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

  PATH="/usr/bin:/bin" HOME="$tmp_home" "$ROOT/setup" --host auto --repo-root "$ROOT" --skip-fgrove-cli --quiet

  [ -L "$tmp_home/.codex/skills/edit-funnel" ] || fail "auto fallback did not install Codex skill"
  [ -L "$tmp_home/.claude/skills/edit-funnel" ] || fail "auto fallback did not install Claude skill"
  [ -L "$tmp_home/.codex/skills/writing-funnel-copy" ] || fail "auto fallback did not install Codex copy skill"
  [ -L "$tmp_home/.claude/skills/writing-funnel-copy" ] || fail "auto fallback did not install Claude copy skill"
  [ -L "$tmp_home/.codex/skills/preview-funnel" ] || fail "auto fallback did not install Codex preview skill"
  [ -L "$tmp_home/.claude/skills/preview-funnel" ] || fail "auto fallback did not install Claude preview skill"
  [ "$(cd "$tmp_home/.codex/skills/edit-funnel" && pwd -P)" = "$ROOT/skills/edit-funnel" ] || fail "wrong auto Codex symlink target"
  [ "$(cd "$tmp_home/.claude/skills/edit-funnel" && pwd -P)" = "$ROOT/skills/edit-funnel" ] || fail "wrong auto Claude symlink target"
  [ "$(cd "$tmp_home/.codex/skills/writing-funnel-copy" && pwd -P)" = "$ROOT/skills/writing-funnel-copy" ] || fail "wrong auto Codex copy symlink target"
  [ "$(cd "$tmp_home/.claude/skills/writing-funnel-copy" && pwd -P)" = "$ROOT/skills/writing-funnel-copy" ] || fail "wrong auto Claude copy symlink target"
  [ "$(cd "$tmp_home/.codex/skills/preview-funnel" && pwd -P)" = "$ROOT/skills/preview-funnel" ] || fail "wrong auto Codex preview symlink target"
  [ "$(cd "$tmp_home/.claude/skills/preview-funnel" && pwd -P)" = "$ROOT/skills/preview-funnel" ] || fail "wrong auto Claude preview symlink target"

  rm -rf "$tmp_home"
}

check_readme
check_setup
check_fgrove_cli_helper
check_skill
check_copy_skill
check_preview_skill
check_create_skill
check_installs
check_auto_install_fallback
bash "$ROOT/tests/contract-guidance.sh"

echo "PASS: fstack smoke checks"
