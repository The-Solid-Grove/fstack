# fstack

fstack is a small skill pack for building and editing web funnels with AI agents.
It includes `edit-funnel` for the FunnelsGrove local editing loop and
`writing-funnel-copy` for quiz-to-paywall funnel copy based on conversion
psychology.

Current version: `0.4.0`

## Requirements

- Git
- Bash
- Codex and/or Claude Code
- FunnelsGrove CLI access for hosted funnel work:

```bash
npm install -g @funnelsgrove/cli
fgrove login
```

If you already use the FunnelsGrove CLI skill from
`/Users/andrew/work/funnelsgrove/app-deals/codex-skills/funnelsgrove-cli`,
keep using it for detailed CLI command help. `edit-funnel` references that
workflow instead of duplicating every command.

## Install

Clone fstack once, then link the skills into your agent.

```bash
git clone git@github.com:The-Solid-Grove/fstack.git ~/.fstack
cd ~/.fstack
./setup --host auto
```

Install for one host:

```bash
./setup --host codex
./setup --host claude
```

Host install locations:

| Host | Skill directory |
| --- | --- |
| Codex | `~/.codex/skills/<skill-name>` |
| Claude Code | `~/.claude/skills/<skill-name>` |

The installer creates symlinks back to this checkout. It is idempotent, so rerun
it any time. By default it also checks the installed `fgrove` CLI against the
latest `@funnelsgrove/cli` version on npm and updates the global CLI when a
newer version is available.

For offline installs or CI smoke checks that should not touch global npm
packages, skip that check:

```bash
./setup --host auto --skip-fgrove-cli
```

## Update

Updates follow the same simple shape as gstack: pull the checkout and rerun
setup.

```bash
cd ~/.fstack
git pull --ff-only
./setup --host auto
```

If you installed from a different path, run those commands from that checkout.

## Use `edit-funnel`

In Codex or Claude Code, ask the agent to use the skill:

```text
Use $edit-funnel to edit the ClaimBee onboarding funnel. Change the hero copy,
run local preview, ask whether to publish, publish preview if approved, run QA,
and publish production only after approved preview QA.
```

The skill expects a target workspace/project/funnel or enough context to find
one. It will:

1. Confirm the target and whether a clone is safer.
2. Check/update the `fgrove` CLI version.
3. Check `fgrove` auth and current context.
4. Sync the funnel into a local directory or use the existing synced tree.
5. Refresh local editing docs with `fgrove docs`.
6. Read the generated `AGENTS.md` or `agent.md` docs before editing.
7. Update local project packages when requested or needed for checks.
8. Make the requested edits.
9. Run available checks.
10. Open the local preview by default.
11. Adjust locally and repeat the local preview loop until the change is ready.
12. Ask whether to publish.
13. If approved, run `fgrove sync up`.
14. Run `fgrove publish --env preview`.
15. Run preview QA on the returned preview URL.
16. If production publish is explicitly approved, publish production and run
    production QA on the production URL.

Update local project packages with the package manager already used by the
synced funnel tree. Use `npm outdated`, `npm update`, and `npm install` for
`package-lock.json`; `pnpm outdated`, `pnpm update`, and `pnpm install` for
`pnpm-lock.yaml`; `yarn outdated`, `yarn upgrade`, and `yarn install` for
`yarn.lock`; or the Bun equivalents for `bun.lockb`. Do not introduce a second
lockfile. After package updates, run the funnel's checks before local preview.

Full QA covers adding or submitting email, making a test payment or approved
payment-path equivalent, closing and reopening checkout to verify the larger
discount path, and checking `/manage-subscription` through the cancellation
flow when a test subscription is available.

Production publish is intentionally not part of the default flow. Ask for it
explicitly and provide the target domain when you want production. The skill
should not publish production until preview QA has passed or you explicitly
accept the risk of skipped QA.

## Use `writing-funnel-copy`

Use this skill when you want a complete quiz-to-paywall funnel concept before
editing screens:

```text
Use $writing-funnel-copy for a sleep app funnel. Ask me for the required product
context first, then return the formatted strategy and screen-by-screen copy.
```

The skill asks for product, audience, entry promise, and screen count before
writing. It then returns the five-column pre-work, transformation, emotional
arc, fuel check, screen specs, paywall architecture, and A/B test ideas.
The full psychology framework is bundled as a nearby reference at
`skills/writing-funnel-copy/references/funnel-psychology-framework.md`, and the
paywall-specific guidance is bundled at
`skills/writing-funnel-copy/references/funnel-paywall-best-practices.md`.
Conversion experiment guidance is bundled at
`skills/writing-funnel-copy/references/funnel-conversion-best-practices.md`.
The skill instructs agents to read the relevant references before drafting.

## Team Setup

For now, use a shared global checkout instead of vendoring skills into each
project. Add this to a project `AGENTS.md` or `CLAUDE.md` when teammates should
use fstack:

```markdown
Use fstack for FunnelsGrove funnel work. Start with `edit-funnel` for hosted
funnel edits and `writing-funnel-copy` for quiz-to-paywall strategy. Do not
finish hosted edits until a local preview has been checked. Ask whether to
publish before hosted deploys; if publishing, run preview QA before any
production publish and run production QA after production publish.
```

Then each teammate runs:

```bash
git clone git@github.com:The-Solid-Grove/fstack.git ~/.fstack
cd ~/.fstack && ./setup --host auto
```

## Uninstall

Remove the symlinks:

```bash
rm -f ~/.codex/skills/edit-funnel
rm -f ~/.claude/skills/edit-funnel
rm -f ~/.codex/skills/writing-funnel-copy
rm -f ~/.claude/skills/writing-funnel-copy
```

Remove the checkout only if nothing else depends on it:

```bash
rm -rf ~/.fstack
```

## Develop

Run the smoke checks:

```bash
bash tests/smoke.sh
```

The checks validate README coverage, installer syntax, skill frontmatter, and
temporary Codex/Claude Code installs.
