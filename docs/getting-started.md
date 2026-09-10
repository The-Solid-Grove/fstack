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

For research and copy, you need Git, Bash, and your agent. For clickable previews, the bundled workflow also uses Python 3 and browser access.

<details>
<summary><strong>Building or editing with FunnelsGrove</strong></summary>

Hosted work also needs Node.js 18+, npm, and access to FunnelsGrove:

```bash
npm install -g @funnelsgrove/cli
fgrove login
```

Run `./setup --host auto` without `--skip-fgrove-cli` to check and update the global CLI against npm as part of setup.

`create-funnel` needs access to a FunnelsGrove monorepo checkout containing `apps/funnel-template`. The published CLI does not include that template. The skill helps locate the checkout before scaffolding.

</details>

## Update

```bash
cd ~/.fstack
git pull --ff-only
./setup --host auto --skip-fgrove-cli
```

Because the skills are linked, pulling updates changes the installed files. Commit your own adaptations before updating. Omit `--skip-fgrove-cli` when you also want setup to check and update the CLI.

## Team setup

Each teammate installs the pack. Add a short pointer to your project's `AGENTS.md` or `CLAUDE.md`:

```markdown
Use fstack for Web-to-Web funnel work: web2app-essentials for research,
writing-funnel-copy for strategy and screen copy, preview-funnel for
clickable copy review, create-funnel for new FunnelsGrove projects,
edit-funnel for hosted changes, and qa-funnel for design and flow testing. Read the matching SKILL.md and
follow the project's managed FunnelsGrove docs for implementation.
```

## Uninstall

Remove the installed symlinks first. This preserves directories if you replaced a link with your own copy:

```bash
for host in ~/.codex/skills ~/.claude/skills; do
  for skill in create-funnel edit-funnel preview-funnel writing-funnel-copy web2app-essentials qa-funnel; do
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

Current version: `0.6.0`

## Course references

Web-to-Web Essentials keeps the existing `web2app-essentials` invocation for installed users. Its `references/` directory is a verbatim export of the published course lessons and worksheets, plus a Markdown transcription of the published one-pagers, not a separately edited curriculum. Root-relative course links and images resolve against `https://funnelsgrove.com`; relative Markdown links retain the course tree.

Improve the canonical course first, regenerate and test its served content, publish it, then export the committed revision:

```bash
python3 scripts/sync-course --source <funnelsgrove-checkout> --ref <published-commit>
python3 scripts/sync-course --check --source <funnelsgrove-checkout> --ref <published-commit>
```

The export replaces the entire References directory and records the source commit, the canonical one-pager data hash, and SHA-256 of each exported file in `course.json`. `--check` without a source checkout detects local drift offline; it does not certify that production serves that revision. Verify the live course before merging an export. Make future lesson edits in the course source and re-export.
