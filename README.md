# fstack

A small skill pack for building and editing web funnels with AI agents.

- `edit-funnel` — local editing loop for FunnelsGrove hosted funnels (sync, preview, QA, publish).
- `writing-funnel-copy` — quiz-to-paywall copy and conversion strategy.

Current version: `0.4.0`

## Requirements

- Git, Bash
- Codex and/or Claude Code
- FunnelsGrove CLI for hosted funnel work:

  ```bash
  npm install -g @funnelsgrove/cli
  fgrove login
  ```

## Install

```bash
git clone git@github.com:The-Solid-Grove/fstack.git ~/.fstack
cd ~/.fstack
./setup --host auto
```

Single host: `./setup --host codex` or `./setup --host claude`.

| Host | Skill directory |
| --- | --- |
| Codex | `~/.codex/skills/<skill-name>` |
| Claude Code | `~/.claude/skills/<skill-name>` |

The installer creates idempotent symlinks back to this checkout. By default it
also checks the installed `fgrove` CLI against the latest `@funnelsgrove/cli`
on npm and updates it when newer. Skip that check with `--skip-fgrove-cli`.

## Update

```bash
cd ~/.fstack
git pull --ff-only
./setup --host auto
```

## Use `edit-funnel`

Ask the agent to use the skill against a target funnel:

```text
Use $edit-funnel to edit <workspace>/<project>/<funnel>. Change <copy/screen>,
run local preview, ask whether to publish, publish preview if approved, run QA,
and publish production only after approved preview QA.
```

The skill syncs the funnel locally, reads its `AGENTS.md`/`agent.md`, makes
edits, runs checks, opens local preview, and loops until ready. Update local
project packages with the package manager already used by the synced tree.
Use `npm outdated`, `pnpm outdated`, yarn, or bun as appropriate, and never
introduce a second lockfile. Ask whether to publish before any deploy, run preview QA on the
returned preview URL, and only run production QA after an explicit production
publish.

Full QA covers email submit, a test payment (or approved payment-path
equivalent), reopening checkout to verify the larger discount path, and
`/manage-subscription` cancellation when a test subscription is available.
Production publish is opt-in — pass the target domain explicitly.

## Use `writing-funnel-copy`

```text
Use $writing-funnel-copy for a <product> funnel. Ask for the required product
context first, then return the strategy and screen-by-screen copy.
```

The skill asks for product, audience, entry promise, and screen count, then
returns pre-work, transformation arc, screen specs, paywall architecture, and
A/B ideas. Reference material lives under
`skills/writing-funnel-copy/references/`.

## Team setup

Use a shared global checkout. Add this to your project `AGENTS.md` or
`CLAUDE.md`:

```markdown
Use fstack for FunnelsGrove funnel work. Use `edit-funnel` for hosted edits
and `writing-funnel-copy` for quiz-to-paywall strategy. Always run local
preview, ask before publishing, run preview QA before any production publish,
and run production QA after production publish.
```

Each teammate runs:

```bash
git clone git@github.com:The-Solid-Grove/fstack.git ~/.fstack
cd ~/.fstack && ./setup --host auto
```

## Uninstall

```bash
rm -f ~/.codex/skills/edit-funnel ~/.claude/skills/edit-funnel
rm -f ~/.codex/skills/writing-funnel-copy ~/.claude/skills/writing-funnel-copy
rm -rf ~/.fstack
```

## Develop

```bash
bash tests/smoke.sh
```

Smoke checks validate the README, installer syntax, skill frontmatter, and
temporary Codex/Claude Code installs.
