#!/usr/bin/env bash
set -euo pipefail

# Exercise the public checker against real local Git remotes and checkouts.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
CHECK="$ROOT/scripts/check-fstack-update"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null
export GIT_AUTHOR_NAME=Test GIT_AUTHOR_EMAIL=test@example.invalid
export GIT_COMMITTER_NAME=Test GIT_COMMITTER_EMAIL=test@example.invalid

fail() { echo "FAIL: $*" >&2; exit 1; }
contains() { [[ "$OUT" == *"$1"* ]] || fail "missing '$1': $OUT"; }

git init -q --bare --initial-branch=main "$TMP/remote.git"
git init -q --initial-branch=main "$TMP/source"
printf '0.6.0\n' > "$TMP/source/VERSION"
git -C "$TMP/source" add VERSION
git -C "$TMP/source" commit -qm initial
git -C "$TMP/source" remote add origin "$TMP/remote.git"
git -C "$TMP/source" push -q origin main
git clone -q "$TMP/remote.git" "$TMP/installed pack"
REPO="$TMP/installed pack"

OUT="$(bash "$CHECK" --repo-root "$REPO")"
contains 'fstack: current'
contains '0.6.0'
echo 'ok: current checkout'

before="$(git -C "$REPO" rev-parse HEAD)"
printf 'new skill content\n' > "$TMP/source/content.md"
git -C "$TMP/source" add content.md
git -C "$TMP/source" commit -qm 'update without a VERSION bump'
git -C "$TMP/source" push -q origin main
OUT="$(bash "$CHECK" --repo-root "$REPO")"
contains 'fstack: update available'
contains 'Ask the user'
[ "$(git -C "$REPO" rev-parse HEAD)" = "$before" ] || fail 'checker moved HEAD'
[ ! -e "$REPO/content.md" ] || fail 'checker applied the update'
echo 'ok: newer commit with the same VERSION is offered, not applied'

git clone -q "$TMP/remote.git" "$TMP/ahead"
printf 'local adaptation\n' > "$TMP/ahead/local.md"
git -C "$TMP/ahead" add local.md
git -C "$TMP/ahead" commit -qm 'local commit'
OUT="$(bash "$CHECK" --repo-root "$TMP/ahead")"
contains 'fstack: current'
[[ "$OUT" != *'update available'* ]] || fail 'offered to downgrade a local-ahead checkout'
echo 'ok: local-ahead checkout already includes remote updates'

git -C "$REPO" checkout -qb custom-copy
printf 'custom copy\n' > "$REPO/custom.md"
git -C "$REPO" add custom.md
git -C "$REPO" commit -qm 'custom branch work'
printf 'staged edit\n' >> "$REPO/custom.md"
git -C "$REPO" add custom.md
printf 'unstaged edit\n' >> "$REPO/custom.md"
printf 'untracked work\n' > "$REPO/draft.md"
before="$(git -C "$REPO" rev-parse HEAD)"
before_status="$(git -C "$REPO" status --porcelain)"
before_index="$(git -C "$REPO" diff --cached)"
before_worktree="$(git -C "$REPO" diff)"
OUT="$(bash "$CHECK" --repo-root "$REPO")"
contains 'fstack: update available'
contains 'diverged'
contains 'custom-copy'
contains 'local changes'
[ "$(git -C "$REPO" rev-parse HEAD)" = "$before" ] || fail 'moved custom HEAD'
[ "$(git -C "$REPO" status --porcelain)" = "$before_status" ] || fail 'changed working tree status'
[ "$(git -C "$REPO" diff --cached)" = "$before_index" ] || fail 'changed staged work'
[ "$(git -C "$REPO" diff)" = "$before_worktree" ] || fail 'changed unstaged work'
[ "$(cat "$REPO/draft.md")" = 'untracked work' ] || fail 'changed untracked work'
echo 'ok: diverged dirty branch is reported and preserved'

OUT="$(bash "$CHECK" --repo-root "$REPO" --quiet 2>&1)"
[ -z "$OUT" ] || fail "quiet checker printed: $OUT"
git -C "$REPO" checkout -q --detach
OUT="$(bash "$CHECK" --repo-root "$REPO")"
contains 'detached HEAD'
echo 'ok: quiet output and detached checkout guidance'

mv "$TMP/remote.git" "$TMP/offline.git"
OUT="$(bash "$CHECK" --repo-root "$REPO" 2>&1)" || fail "offline check blocked work: $OUT"
contains 'fstack: update check unavailable'
[[ "$OUT" != *'fstack: current'* ]] || fail 'offline check claimed freshness'
OUT="$(bash "$CHECK" --repo-root "$REPO" --quiet 2>&1)"
[ -z "$OUT" ] || fail "offline quiet checker printed: $OUT"
echo 'ok: offline check is nonblocking without claiming freshness'

mv "$TMP/offline.git" "$TMP/remote.git"
mkdir -p "$REPO/scripts" "$REPO/skills/example"
cp "$CHECK" "$REPO/scripts/check-fstack-update"
printf '# Example skill\n' > "$REPO/skills/example/SKILL.md"
OUT="$(bash "$ROOT/setup" --host codex --repo-root "$REPO" \
  --skills-dir "$TMP/installed skills" --skip-fgrove-cli)"
contains 'fstack: update available'
[ -L "$TMP/installed skills/example" ] || fail 'setup did not install skills'
echo 'ok: setup checks the pack even when the fgrove CLI check is skipped'

OUT="$(bash "$ROOT/setup" --host codex --repo-root "$REPO" \
  --skills-dir "$TMP/installed skills" --skip-fgrove-cli --skip-update-check)"
[[ "$OUT" != *'fstack: update'* ]] || fail 'setup checked despite explicit skip'
contains 'fstack ready.'
echo 'ok: setup can skip the pack check explicitly'

OUT="$(bash "$ROOT/setup" --host codex --repo-root "$REPO" \
  --skills-dir "$TMP/installed skills" --skip-fgrove-cli --quiet 2>&1)"
[ -z "$OUT" ] || fail "quiet setup printed: $OUT"
mv "$TMP/remote.git" "$TMP/offline.git"
OUT="$(bash "$ROOT/setup" --host codex --repo-root "$REPO" \
  --skills-dir "$TMP/offline skills" --skip-fgrove-cli 2>&1)"
contains 'fstack: update check unavailable'
contains 'fstack ready.'
[ -L "$TMP/offline skills/example" ] || fail 'offline check blocked setup'
echo 'ok: setup stays quiet when requested and installs while offline'

git -C "$REPO" remote remove origin
OUT="$(bash "$CHECK" --repo-root "$REPO")"
contains 'fstack: update check unavailable'
echo 'ok: checkout without origin remains usable'

OUT="$(bash "$CHECK" --help)"
contains 'Usage:'
if bash "$CHECK" --unknown >/dev/null 2>&1; then fail 'accepted unknown option'; fi
if bash "$CHECK" --repo-root >/dev/null 2>&1; then fail 'accepted missing repo path'; fi
echo 'ok: public usage errors are reported'

python3 "$ROOT/tests/check_fstack_update_timeout.py" "$CHECK" "$REPO"
