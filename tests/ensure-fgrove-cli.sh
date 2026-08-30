#!/usr/bin/env bash
set -euo pipefail

# Black-box tests for scripts/ensure-fgrove-cli.
#
# Each case runs the real script inside a sandbox PATH that contains only the
# core tools it needs plus optional `fgrove`/`npm` shims, so every branch of
# the install/update decision logic is exercised without touching the network
# or the machine's real npm/fgrove state. Shim behavior is driven by files:
#   $FGROVE_VERSION_FILE  what `fgrove --version` prints (missing shim = CLI absent)
#   $NPM_VIEW_FILE        what `npm view <pkg> version` prints (empty = registry error)
#   $NPM_LOG              records every `npm install` invocation
#   $NPM_INSTALLS_VERSION version the npm shim "installs" into FGROVE_VERSION_FILE

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$ROOT/scripts/ensure-fgrove-cli"
BASH_BIN="$(command -v bash)"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

[ -x "$SCRIPT" ] || fail "missing executable script: $SCRIPT"

CASE_N=0

# make_sandbox <with_fgrove:0|1> <with_npm:0|1>
# Sets $SB to a fresh sandbox dir. Its bin/ holds symlinks to the coreutils
# the script uses, plus /bin/sh shims for fgrove and npm when requested.
# (Sets a global rather than echoing so CASE_N increments in this shell.)
make_sandbox() {
  local with_fgrove="$1" with_npm="$2"
  CASE_N=$((CASE_N + 1))
  SB="$TMP/case-$CASE_N"
  local sb="$SB"
  mkdir -p "$sb/bin"

  local tool
  for tool in grep head tr cat; do
    ln -s "$(command -v "$tool")" "$sb/bin/$tool"
  done

  if [ "$with_fgrove" -eq 1 ]; then
    cat >"$sb/bin/fgrove" <<'SHIM'
#!/bin/sh
if [ "$1" = "--version" ] && [ -n "${FGROVE_VERSION_FILE:-}" ] && [ -f "$FGROVE_VERSION_FILE" ]; then
  cat "$FGROVE_VERSION_FILE"
  exit 0
fi
exit 1
SHIM
    chmod +x "$sb/bin/fgrove"
    : >"$sb/fgrove-version"
  fi

  if [ "$with_npm" -eq 1 ]; then
    cat >"$sb/bin/npm" <<'SHIM'
#!/bin/sh
case "$1" in
  view)
    if [ -n "${NPM_VIEW_FILE:-}" ] && [ -s "$NPM_VIEW_FILE" ]; then
      cat "$NPM_VIEW_FILE"
      exit 0
    fi
    exit 1
    ;;
  install)
    shift
    echo "install $*" >>"$NPM_LOG"
    if [ -n "${NPM_INSTALLS_VERSION:-}" ] && [ -n "${FGROVE_VERSION_FILE:-}" ]; then
      printf '%s\n' "$NPM_INSTALLS_VERSION" >"$FGROVE_VERSION_FILE"
    fi
    exit 0
    ;;
esac
exit 1
SHIM
    chmod +x "$sb/bin/npm"
    : >"$sb/npm-view"
    : >"$sb/npm.log"
  fi
}

# run_script <sandbox> [extra env VAR=VALUE ...] -- [script args ...]
# Fills OUT, ERR, STATUS.
run_script() {
  local sb="$1"
  shift
  local envs=()
  while [ "$#" -gt 0 ] && [ "$1" != "--" ]; do
    envs+=("$1")
    shift
  done
  [ "${1:-}" = "--" ] && shift

  set +e
  OUT="$(env -i \
    PATH="$sb/bin" \
    HOME="$sb" \
    FGROVE_VERSION_FILE="$sb/fgrove-version" \
    NPM_VIEW_FILE="$sb/npm-view" \
    NPM_LOG="$sb/npm.log" \
    ${envs[@]+"${envs[@]}"} \
    "$BASH_BIN" "$SCRIPT" "$@" 2>"$sb/stderr")"
  STATUS=$?
  set -e
  ERR="$(cat "$sb/stderr")"
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

assert_installed() {
  local sb="$1" expected="$2"
  [ -s "$sb/npm.log" ] || fail "$CURRENT_CASE: expected an npm install, none recorded"
  grep -q "install -g $expected" "$sb/npm.log" \
    || fail "$CURRENT_CASE: npm.log missing 'install -g $expected' (log: $(cat "$sb/npm.log"))"
}

assert_no_install() {
  local sb="$1"
  [ ! -s "$sb/npm.log" ] || fail "$CURRENT_CASE: unexpected npm install (log: $(cat "$sb/npm.log"))"
}

ok() {
  echo "ok: $CURRENT_CASE"
}

# --- cases ---------------------------------------------------------------

CURRENT_CASE="installs when CLI is missing"
make_sandbox 1 1; sb="$SB"
: >"$sb/fgrove-version" # empty --version output = effectively not installed
echo "1.2.3" >"$sb/npm-view"
run_script "$sb" NPM_INSTALLS_VERSION=1.2.3 --
assert_status 0
assert_out_contains "Installing fgrove CLI 1.2.3"
assert_out_contains "fgrove CLI ready: 1.2.3"
assert_installed "$sb" "@funnelsgrove/cli@latest"
ok

CURRENT_CASE="no install when versions match"
make_sandbox 1 1; sb="$SB"
echo "1.2.3" >"$sb/fgrove-version"
echo "1.2.3" >"$sb/npm-view"
run_script "$sb" --
assert_status 0
assert_out_contains "fgrove CLI is current: 1.2.3"
assert_no_install "$sb"
ok

CURRENT_CASE="updates when npm has a newer version"
make_sandbox 1 1; sb="$SB"
echo "1.2.3" >"$sb/fgrove-version"
echo "1.2.4" >"$sb/npm-view"
run_script "$sb" NPM_INSTALLS_VERSION=1.2.4 --
assert_status 0
assert_out_contains "Updating fgrove CLI from 1.2.3 to 1.2.4"
assert_out_contains "fgrove CLI ready: 1.2.4"
assert_installed "$sb" "@funnelsgrove/cli@latest"
ok

CURRENT_CASE="keeps an installed version newer than npm"
make_sandbox 1 1; sb="$SB"
echo "1.3.0" >"$sb/fgrove-version"
echo "1.2.9" >"$sb/npm-view"
run_script "$sb" --
assert_status 0
assert_out_contains "fgrove CLI is current: 1.3.0"
assert_no_install "$sb"
ok

CURRENT_CASE="upgrades a prerelease to the stable release of the same core"
make_sandbox 1 1; sb="$SB"
echo "1.2.3-beta.1" >"$sb/fgrove-version"
echo "1.2.3" >"$sb/npm-view"
run_script "$sb" NPM_INSTALLS_VERSION=1.2.3 --
assert_status 0
assert_out_contains "Updating fgrove CLI from 1.2.3-beta.1 to 1.2.3"
assert_installed "$sb" "@funnelsgrove/cli@latest"
ok

CURRENT_CASE="does not replace a stable install with a same-core prerelease"
make_sandbox 1 1; sb="$SB"
echo "1.2.3" >"$sb/fgrove-version"
echo "1.2.3-rc.1" >"$sb/npm-view"
run_script "$sb" --
assert_status 0
assert_no_install "$sb"
ok

CURRENT_CASE="updates a two-part installed version when a patch release lands"
make_sandbox 1 1; sb="$SB"
echo "1.2" >"$sb/fgrove-version"
echo "1.2.1" >"$sb/npm-view"
run_script "$sb" NPM_INSTALLS_VERSION=1.2.1 --
assert_status 0
assert_out_contains "Updating fgrove CLI from 1.2 to 1.2.1"
assert_installed "$sb" "@funnelsgrove/cli@latest"
ok

CURRENT_CASE="parses the version out of noisy --version output"
make_sandbox 1 1; sb="$SB"
echo "fgrove/2.1.0 darwin-arm64 node-v20.1.0" >"$sb/fgrove-version"
echo "2.1.0" >"$sb/npm-view"
run_script "$sb" --
assert_status 0
assert_out_contains "fgrove CLI is current: 2.1.0"
assert_no_install "$sb"
ok

CURRENT_CASE="exits 0 with a warning when npm is missing but the CLI is installed"
make_sandbox 1 0; sb="$SB"
echo "1.2.3" >"$sb/fgrove-version"
run_script "$sb" --
assert_status 0
assert_err_contains "npm is not available"
ok

CURRENT_CASE="exits 1 when npm and the CLI are both missing"
make_sandbox 0 0; sb="$SB"
run_script "$sb" --
assert_status 1
assert_err_contains "not installed and npm is not available"
ok

CURRENT_CASE="keeps the installed CLI when the registry read fails"
make_sandbox 1 1; sb="$SB"
echo "1.2.3" >"$sb/fgrove-version"
: >"$sb/npm-view" # empty = npm view fails
run_script "$sb" --
assert_status 0
assert_err_contains "keeping installed fgrove CLI 1.2.3"
assert_no_install "$sb"
ok

CURRENT_CASE="exits 1 when the CLI is missing and the registry read fails"
make_sandbox 0 1; sb="$SB"
: >"$sb/npm-view"
run_script "$sb" --
assert_status 1
assert_err_contains "could not be read from npm"
ok

CURRENT_CASE="--quiet silences info output on the current path"
make_sandbox 1 1; sb="$SB"
echo "1.2.3" >"$sb/fgrove-version"
echo "1.2.3" >"$sb/npm-view"
run_script "$sb" -- --quiet
assert_status 0
[ -z "$OUT" ] || fail "$CURRENT_CASE: expected empty stdout, got: $OUT"
ok

CURRENT_CASE="FGROVE_PACKAGE and FGROVE_BIN overrides are honored"
make_sandbox 1 1; sb="$SB"
mv "$sb/bin/fgrove" "$sb/bin/customgrove"
echo "0.9.0" >"$sb/fgrove-version"
echo "1.0.0" >"$sb/npm-view"
run_script "$sb" FGROVE_BIN=customgrove FGROVE_PACKAGE=@acme/cli NPM_INSTALLS_VERSION=1.0.0 --
assert_status 0
assert_installed "$sb" "@acme/cli@latest"
ok

CURRENT_CASE="unknown options exit 1 with usage"
make_sandbox 1 1; sb="$SB"
run_script "$sb" -- --bogus
assert_status 1
assert_err_contains "Unknown option: --bogus"
assert_err_contains "Usage:"
ok

CURRENT_CASE="--help exits 0 with usage"
make_sandbox 0 0; sb="$SB"
run_script "$sb" -- --help
assert_status 0
assert_out_contains "Usage:"
ok

echo "ensure-fgrove-cli checks passed"
