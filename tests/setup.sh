#!/usr/bin/env bash
set -euo pipefail

# Black-box tests for ./setup.
#
# smoke.sh already covers the happy-path installs against the real repo
# (codex, claude, and the auto fallback when neither host CLI is on PATH).
# This suite covers everything else: argument parsing and validation errors,
# --skills-dir overrides, idempotent re-runs, stale-symlink repair, the
# non-symlink refusal guard, fgrove-helper wiring (default, --quiet,
# --skip-fgrove-cli, helper failure, missing helper), and partial host
# auto-detection. Each case runs the real script against a fake --repo-root
# built under mktemp, so no case touches the network, npm, or the real
# ~/.codex / ~/.claude skill directories.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SETUP="$ROOT/setup"
BASH_BIN="$(command -v bash)"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

[ -x "$SETUP" ] || fail "missing executable script: $SETUP"

# Fake repo the cases install from: two real skills, one dir that must be
# skipped (no SKILL.md), and an ensure-fgrove-cli stub that records every
# invocation to $HELPER_LOG and exits ${HELPER_EXIT:-0}.
FAKE_REPO="$TMP/fake-repo"
mkdir -p "$FAKE_REPO/skills/alpha" "$FAKE_REPO/skills/beta" \
  "$FAKE_REPO/skills/not-a-skill" "$FAKE_REPO/scripts"
echo "# alpha" > "$FAKE_REPO/skills/alpha/SKILL.md"
echo "# beta" > "$FAKE_REPO/skills/beta/SKILL.md"
echo "no SKILL.md here" > "$FAKE_REPO/skills/not-a-skill/README.md"
cat > "$FAKE_REPO/scripts/ensure-fgrove-cli" <<'STUB'
#!/bin/sh
echo "helper $*" >> "$HELPER_LOG"
exit "${HELPER_EXIT:-0}"
STUB
chmod +x "$FAKE_REPO/scripts/ensure-fgrove-cli"

ALPHA_TARGET="$(cd "$FAKE_REPO/skills/alpha" && pwd -P)"
BETA_TARGET="$(cd "$FAKE_REPO/skills/beta" && pwd -P)"

CASE_N=0

# new_home: fresh fake $HOME per case (sets globals HOME_DIR and HELPER_LOG).
new_home() {
  CASE_N=$((CASE_N + 1))
  HOME_DIR="$TMP/home-$CASE_N"
  HELPER_LOG="$HOME_DIR/helper.log"
  mkdir -p "$HOME_DIR"
}

# run_setup [ENV=VALUE ...] -- [setup args ...]
# Runs setup with HOME=$HOME_DIR and fills OUT, ERR, STATUS.
run_setup() {
  local envs=()
  while [ "$#" -gt 0 ] && [ "$1" != "--" ]; do
    envs+=("$1")
    shift
  done
  [ "${1:-}" = "--" ] && shift

  set +e
  OUT="$(env \
    HOME="$HOME_DIR" \
    HELPER_LOG="$HELPER_LOG" \
    ${envs[@]+"${envs[@]}"} \
    "$BASH_BIN" "$SETUP" "$@" 2>"$HOME_DIR/stderr")"
  STATUS=$?
  set -e
  ERR="$(cat "$HOME_DIR/stderr")"
}

assert_status() {
  [ "$STATUS" -eq "$1" ] || fail "$CURRENT_CASE: expected exit $1, got $STATUS (stdout: $OUT; stderr: $ERR)"
}

assert_out_contains() {
  case "$OUT" in
    *"$1"*) ;;
    *) fail "$CURRENT_CASE: stdout missing '$1' (stdout: $OUT)" ;;
  esac
}

assert_err_contains() {
  case "$ERR" in
    *"$1"*) ;;
    *) fail "$CURRENT_CASE: stderr missing '$1' (stderr: $ERR)" ;;
  esac
}

# assert_linked <link path> <expected resolved target>
assert_linked() {
  local link="$1" expected="$2"
  [ -L "$link" ] || fail "$CURRENT_CASE: expected symlink at $link"
  [ "$(cd "$link" && pwd -P)" = "$expected" ] \
    || fail "$CURRENT_CASE: $link resolves to $(cd "$link" && pwd -P), expected $expected"
}

assert_absent() {
  [ ! -e "$1" ] && [ ! -L "$1" ] || fail "$CURRENT_CASE: expected nothing at $1"
}

ok() {
  echo "ok: $CURRENT_CASE"
}

# --- argument parsing and validation --------------------------------------

CURRENT_CASE="--help exits 0 with usage"
new_home
run_setup -- --help
assert_status 0
assert_out_contains "Usage:"
ok

CURRENT_CASE="unknown options exit 1 with usage"
new_home
run_setup -- --bogus
assert_status 1
assert_err_contains "Unknown option: --bogus"
assert_err_contains "Usage:"
ok

CURRENT_CASE="--host without a value exits 1"
new_home
run_setup -- --host
assert_status 1
assert_err_contains "Missing value for --host"
ok

CURRENT_CASE="invalid --host value exits 1"
new_home
run_setup -- --host emacs
assert_status 1
assert_err_contains "Unknown --host value: emacs"
ok

CURRENT_CASE="--skills-dir with --host auto exits 1"
new_home
run_setup -- --host auto --skills-dir "$HOME_DIR/anywhere" --repo-root "$FAKE_REPO" --skip-fgrove-cli
assert_status 1
assert_err_contains "--skills-dir requires --host codex or --host claude"
assert_absent "$HOME_DIR/anywhere"
ok

# --- linking behavior ------------------------------------------------------

CURRENT_CASE="codex install links every skill dir with a SKILL.md"
new_home
run_setup -- --host codex --repo-root "$FAKE_REPO" --skip-fgrove-cli
assert_status 0
assert_linked "$HOME_DIR/.codex/skills/alpha" "$ALPHA_TARGET"
assert_linked "$HOME_DIR/.codex/skills/beta" "$BETA_TARGET"
assert_absent "$HOME_DIR/.codex/skills/not-a-skill"
assert_absent "$HOME_DIR/.claude/skills"
assert_out_contains "linked codex: $HOME_DIR/.codex/skills/alpha"
assert_out_contains "fstack ready."
ok

CURRENT_CASE="claude install links into ~/.claude/skills"
new_home
run_setup -- --host claude --repo-root "$FAKE_REPO" --skip-fgrove-cli
assert_status 0
assert_linked "$HOME_DIR/.claude/skills/alpha" "$ALPHA_TARGET"
assert_linked "$HOME_DIR/.claude/skills/beta" "$BETA_TARGET"
assert_absent "$HOME_DIR/.codex/skills"
ok

CURRENT_CASE="--skills-dir overrides the host default (equals-form flags)"
new_home
run_setup -- --host=codex --skills-dir="$HOME_DIR/custom" --repo-root="$FAKE_REPO" --skip-fgrove-cli
assert_status 0
assert_linked "$HOME_DIR/custom/alpha" "$ALPHA_TARGET"
assert_linked "$HOME_DIR/custom/beta" "$BETA_TARGET"
assert_absent "$HOME_DIR/.codex/skills"
ok

CURRENT_CASE="re-running is idempotent"
new_home
run_setup -- --host codex --repo-root "$FAKE_REPO" --skip-fgrove-cli
assert_status 0
run_setup -- --host codex --repo-root "$FAKE_REPO" --skip-fgrove-cli
assert_status 0
assert_linked "$HOME_DIR/.codex/skills/alpha" "$ALPHA_TARGET"
assert_linked "$HOME_DIR/.codex/skills/beta" "$BETA_TARGET"
ok

CURRENT_CASE="a stale symlink is repointed at the skill"
new_home
mkdir -p "$HOME_DIR/.codex/skills" "$HOME_DIR/elsewhere"
ln -s "$HOME_DIR/elsewhere" "$HOME_DIR/.codex/skills/alpha"
run_setup -- --host codex --repo-root "$FAKE_REPO" --skip-fgrove-cli
assert_status 0
assert_linked "$HOME_DIR/.codex/skills/alpha" "$ALPHA_TARGET"
ok

CURRENT_CASE="refuses to replace a non-symlink skill"
new_home
mkdir -p "$HOME_DIR/.codex/skills/alpha"
echo "precious local edits" > "$HOME_DIR/.codex/skills/alpha/SKILL.md"
run_setup -- --host codex --repo-root "$FAKE_REPO" --skip-fgrove-cli
assert_status 1
assert_err_contains "Refusing to replace non-symlink skill: $HOME_DIR/.codex/skills/alpha"
[ -f "$HOME_DIR/.codex/skills/alpha/SKILL.md" ] \
  || fail "$CURRENT_CASE: the non-symlink skill dir was modified"
grep -q "precious local edits" "$HOME_DIR/.codex/skills/alpha/SKILL.md" \
  || fail "$CURRENT_CASE: the non-symlink skill content was modified"
ok

CURRENT_CASE="repo root without a skills directory exits 1"
new_home
mkdir -p "$HOME_DIR/empty-repo"
run_setup -- --host codex --repo-root "$HOME_DIR/empty-repo" --skip-fgrove-cli
assert_status 1
assert_err_contains "Missing skills directory:"
ok

CURRENT_CASE="empty skills directory exits 1"
new_home
mkdir -p "$HOME_DIR/bare-repo/skills"
run_setup -- --host codex --repo-root "$HOME_DIR/bare-repo" --skip-fgrove-cli
assert_status 1
assert_err_contains "No skills found under"
ok

CURRENT_CASE="skills directory with no SKILL.md dirs exits 1"
new_home
mkdir -p "$HOME_DIR/husk-repo/skills/docs-only"
echo "not a skill" > "$HOME_DIR/husk-repo/skills/docs-only/README.md"
run_setup -- --host codex --repo-root "$HOME_DIR/husk-repo" --skip-fgrove-cli
assert_status 1
assert_err_contains "No skills found under"
assert_absent "$HOME_DIR/.codex/skills/docs-only"
ok

# --- fgrove helper wiring ----------------------------------------------------

CURRENT_CASE="default run invokes the fgrove helper once with no flags"
new_home
run_setup -- --host codex --repo-root "$FAKE_REPO"
assert_status 0
[ -f "$HELPER_LOG" ] || fail "$CURRENT_CASE: helper was never invoked"
[ "$(grep -c '^helper' "$HELPER_LOG")" -eq 1 ] \
  || fail "$CURRENT_CASE: expected exactly one helper invocation (log: $(cat "$HELPER_LOG"))"
grep -q '^helper --quiet' "$HELPER_LOG" \
  && fail "$CURRENT_CASE: helper unexpectedly invoked with --quiet"
ok

CURRENT_CASE="--quiet passes --quiet to the helper and silences stdout"
new_home
run_setup -- --host codex --repo-root "$FAKE_REPO" --quiet
assert_status 0
grep -q '^helper --quiet' "$HELPER_LOG" \
  || fail "$CURRENT_CASE: helper not invoked with --quiet (log: $(cat "$HELPER_LOG"))"
[ -z "$OUT" ] || fail "$CURRENT_CASE: expected empty stdout, got: $OUT"
assert_linked "$HOME_DIR/.codex/skills/alpha" "$ALPHA_TARGET"
ok

CURRENT_CASE="--skip-fgrove-cli does not invoke the helper"
new_home
run_setup -- --host codex --repo-root "$FAKE_REPO" --skip-fgrove-cli
assert_status 0
[ ! -f "$HELPER_LOG" ] || fail "$CURRENT_CASE: helper invoked despite --skip-fgrove-cli (log: $(cat "$HELPER_LOG"))"
ok

CURRENT_CASE="helper failure aborts before any linking"
new_home
run_setup HELPER_EXIT=1 -- --host codex --repo-root "$FAKE_REPO"
assert_status 1
assert_absent "$HOME_DIR/.codex/skills/alpha"
ok

CURRENT_CASE="missing helper exits 1 unless skipped"
new_home
mkdir -p "$HOME_DIR/helperless-repo/skills/alpha"
echo "# alpha" > "$HOME_DIR/helperless-repo/skills/alpha/SKILL.md"
run_setup -- --host codex --repo-root "$HOME_DIR/helperless-repo"
assert_status 1
assert_err_contains "Missing fgrove CLI helper:"
run_setup -- --host codex --repo-root "$HOME_DIR/helperless-repo" --skip-fgrove-cli
assert_status 0
assert_linked "$HOME_DIR/.codex/skills/alpha" "$(cd "$HOME_DIR/helperless-repo/skills/alpha" && pwd -P)"
ok

# --- host auto-detection -----------------------------------------------------
# smoke.sh covers the neither-CLI-found fallback (installs both); these cover
# the partial-detection paths it skips.

CURRENT_CASE="auto installs only codex when only codex is on PATH"
new_home
mkdir -p "$HOME_DIR/hostbin"
printf '#!/bin/sh\nexit 0\n' > "$HOME_DIR/hostbin/codex"
chmod +x "$HOME_DIR/hostbin/codex"
run_setup PATH="$HOME_DIR/hostbin:/usr/bin:/bin" -- --host auto --repo-root "$FAKE_REPO" --skip-fgrove-cli
assert_status 0
assert_linked "$HOME_DIR/.codex/skills/alpha" "$ALPHA_TARGET"
assert_absent "$HOME_DIR/.claude/skills"
ok

CURRENT_CASE="auto installs only claude when only claude is on PATH"
new_home
mkdir -p "$HOME_DIR/hostbin"
printf '#!/bin/sh\nexit 0\n' > "$HOME_DIR/hostbin/claude"
chmod +x "$HOME_DIR/hostbin/claude"
run_setup PATH="$HOME_DIR/hostbin:/usr/bin:/bin" -- --host auto --repo-root "$FAKE_REPO" --skip-fgrove-cli
assert_status 0
assert_linked "$HOME_DIR/.claude/skills/alpha" "$ALPHA_TARGET"
assert_absent "$HOME_DIR/.codex/skills"
ok

echo "setup checks passed"
