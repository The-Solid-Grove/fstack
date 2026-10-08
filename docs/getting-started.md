# Setup and maintenance

[Back to the skills](../README.md).

## Install

Clone the pack and link the skills to your agent:

```bash
git clone https://github.com/The-Solid-Grove/fstack.git ~/.fstack
cd ~/.fstack
./setup --host auto --skip-fgrove-cli
```

Choose a single agent with `--host codex` or `--host claude`. Auto detects installed agent commands and falls back to both when neither is found.

The installer creates symlinks in `~/.codex/skills/` and/or `~/.claude/skills/`. Keep the checkout: those links point to its files. Re-running setup refreshes the links.

For research and copy, you need Git, Bash, and your agent. For clickable previews, the bundled workflow also uses Python 3 and browser access. Reference funnels (rhythm, energy screens and paywall structures) come from the public Funnel Screens library through [`fgrove references`](../skills/design-funnel/references/cli-references.md), which needs the `fgrove` CLI but no login; `scripts/ensure-fgrove-cli` installs it.

`design-funnel` uses existing `Design.md` and approved copy artifacts, an
image-generation tool for representative mockups, and image/browser inspection
for QA. If reference access is unavailable, continue with supplied references,
the recorded reference IDs, product assets and `Design.md`, recording missing
reference coverage. A hosted implementation also requires access to its
FunnelsGrove project.

<details>
<summary><strong>Building or editing with FunnelsGrove</strong></summary>

Hosted work also needs Node.js 18+, npm, and access to FunnelsGrove:

```bash
npm install -g @funnelsgrove/cli
fgrove login
```

Run `./setup --host auto` without `--skip-fgrove-cli` to check and update the global CLI against npm as part of setup.

`create-funnel` requires a connected `fgrove` account, an existing project, and a CLI release with `fgrove templates` and `fgrove funnels create`. It creates from one of three hosted templates through the API, downloads the new funnel source, and establishes `Design.md`; no template checkout is needed.

Creation and editing [remember one working folder per funnel](../skills/edit-funnel/references/local-workspace.md). Later edits resume there, including across conversations. The local registry stores API/workspace/funnel identity and the folder path; it contains no credentials or funnel source.

</details>

## Update

Agents update fstack once per conversation, before the first fstack skill runs: when the checkout is a clean `main` branch behind `origin/main`, the check fast-forwards it and refreshes skill links (see [Agent update check](#agent-update-check)). It compares commits, so it picks up improvements even when `VERSION` has not changed. Custom branches, detached checkouts, local edits and diverged history are never changed; the agent offers the update instead. Setup only checks. A failed network check leaves the current skills usable.

Check or update manually with:

```bash
./scripts/check-fstack-update          # report only
./scripts/check-fstack-update --apply  # fast-forward a clean main and refresh links
```

For an offline installation, use `./setup --skip-update-check --skip-fgrove-cli`. The two flags control the pack and CLI checks independently.

### Agent update check

Before the first fstack skill in a conversation, resolve the loaded skill directory to its physical location. Installed skills are symlinks; derive the checkout from their target, not from `~/.codex` or `~/.claude`.

```bash
fstack_skill_dir="$(cd "<directory-containing-the-loaded-SKILL.md>" && pwd -P)"
fstack_checkout="$(cd "$fstack_skill_dir/../.." && pwd -P)"
"$fstack_checkout/scripts/check-fstack-update" --apply
```

- **`fstack: updated (…)`** — a clean `main` checkout was fast-forwarded to the latest release and skill links were refreshed in the hosts that already use this checkout (new skills linked, removed ones unlinked). Tell the user the old and new versions in one line, then reread the active `SKILL.md` and the references it needs before continuing.
- **`fstack: current`** or **`update check unavailable`** — continue with the installed skills.
- **`fstack: update available (…)`** — the checkout is on a custom branch, detached, has local changes or has diverged, so nothing was changed. Show the installed and latest revisions and offer to update once per conversation; continue the task with the current skills while awaiting the answer. When the user accepts, keep local edits, custom branches and divergent history intact: explain the specific state and agree how to retain that work before moving the checkout to `main` and running `git -C "$fstack_checkout" pull --ff-only origin main`.

After any update that adds or removes skills in a custom skills directory, rerun `"$fstack_checkout/setup"` with the user's original host/skills-directory options (`--skip-fgrove-cli --skip-update-check`). Set `FSTACK_SKILL_DIRS` (colon-separated) to refresh custom directories during `--apply`. Without `--apply`, the check only fetches metadata and never changes the checkout.

## Team setup

Each teammate installs the pack. Add a short pointer to your project's `AGENTS.md` or `CLAUDE.md`:

```markdown
Use fstack for Web-to-Web funnel work: web2app-essentials for research,
writing-funnel-copy for strategy and screen copy, preview-funnel for
clickable copy review, design-funnel for visual patterns and shared style,
create-funnel for new FunnelsGrove projects,
edit-funnel for hosted changes, and qa-funnel for design and flow testing. Read the matching SKILL.md and
follow the project's managed FunnelsGrove docs for implementation.
```

## Uninstall

Remove the installed symlinks first. This preserves directories if you replaced a link with your own copy:

```bash
for host in ~/.codex/skills ~/.claude/skills; do
  for skill in create-funnel edit-funnel preview-funnel design-funnel writing-funnel-copy web2app-essentials qa-funnel; do
    link="$host/$skill"
    if [ -L "$link" ] && [ "$(readlink "$link")" = "$HOME/.fstack/skills/$skill" ]; then
      rm "$link"
    fi
  done
done
```

If you used a different checkout path, substitute it in the target check. You can then remove the checkout once you have saved any changes you want to keep.

## Develop

Each skill has a `skills/<name>/SKILL.md` entry point. Supporting research, examples, and styles live beside it in `references/`; Codex interface metadata lives in `agents/openai.yaml`.

Keep entry points focused on when to act, what to read, and what completion means. Put detailed material in linked references so it is loaded when the task needs it.

Run the smoke checks or every available suite:

```bash
bash tests/smoke.sh

# All suites, including course export and reference checks
for suite in tests/*.sh; do
  bash "$suite" || exit "$?"
done
```

The pack version is recorded in [`VERSION`](../VERSION).

## Course references

Web-to-Web Essentials keeps the existing `web2app-essentials` invocation for installed users. Its `references/` directory is a verbatim export of the published course lessons and worksheets, plus a Markdown transcription of the published one-pagers, not a separately edited curriculum. Root-relative course links and images resolve against `https://funnelsgrove.com`; relative Markdown links retain the course tree.

Improve the canonical course first, regenerate and test its served content, publish it, then export the committed revision:

```bash
python3 scripts/sync-course --source <funnelsgrove-checkout> --ref <published-commit>
python3 scripts/sync-course --check --source <funnelsgrove-checkout> --ref <published-commit>
```

The export replaces the entire References directory and records the source commit, the canonical one-pager data hash, and SHA-256 of each exported file in `course.json`. `--check` without a source checkout detects local drift offline; it does not certify that production serves that revision. Verify the live course before merging an export. Make future lesson edits in the course source and re-export.
