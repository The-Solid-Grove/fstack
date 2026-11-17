#!/usr/bin/env bash
set -euo pipefail

# The Claude directory accepts only Markdown, text, JSON, YAML and images from
# publishers that are not Verified. plugin/ must hold only those files, and
# plugin/skills/ must match what scripts/build-claude-plugin builds from skills/.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
status=0

if ! python3 "$ROOT/scripts/build-claude-plugin" --check; then
  status=1
fi

while IFS= read -r -d '' file; do
  name="${file#"$ROOT"/}"
  case "$name" in
    plugin/LICENSE) continue ;;
  esac
  case "$(printf %s "$file" | tr "[:upper:]" "[:lower:]")" in
    *.md|*.txt|*.json|*.yaml|*.yml|*.png|*.jpg|*.jpeg|*.gif|*.webp|*.ico) ;;
    *) echo "FAIL: $name is not a file type the Claude directory accepts" >&2; status=1; continue ;;
  esac
  if [ "$(head -c 2 "$file")" = '#!' ]; then
    echo "FAIL: $name starts with #!" >&2
    status=1
  fi
done < <(find "$ROOT/plugin" \( -type f -o -type l \) -print0)

if find "$ROOT/plugin" -type l | grep -q .; then
  echo "FAIL: plugin/ must not contain symbolic links" >&2
  status=1
fi

python3 - "$ROOT" <<'PY' || status=1
import json, sys
from pathlib import Path
root = Path(sys.argv[1])
manifest = json.loads((root / "plugin/.claude-plugin/plugin.json").read_text())
marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text())
assert manifest["name"] == "funnelsgrove", manifest["name"]
assert manifest["license"] == "MIT"
assert (root / "plugin" / manifest["icon"]).is_file(), manifest["icon"]
assert [p["source"] for p in marketplace["plugins"]] == ["./plugin"], marketplace["plugins"]
assert len((root / "plugin/README.md").read_text().split()) >= 40
PY

[ "$status" -eq 0 ] && echo 'ok: plugin/ is a current, Markdown-only Claude plugin build'
exit "$status"
