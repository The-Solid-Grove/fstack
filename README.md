# fstack

fstack is a small skill pack for building and editing web funnels with AI agents.
The first skill, `edit-funnel`, guides Codex or Claude Code through the
FunnelsGrove local editing loop: load a hosted funnel with `fgrove`, make scoped
local updates, sync them back, publish a preview, and verify the preview before
finishing.

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
| Codex | `~/.codex/skills/edit-funnel` |
| Claude Code | `~/.claude/skills/edit-funnel` |

The installer creates symlinks back to this checkout. It is idempotent, so rerun
it any time.

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
sync it back, publish preview, and verify the preview URL.
```

The skill expects a target workspace/project/funnel or enough context to find
one. It will:

1. Confirm the target and whether a clone is safer.
2. Check `fgrove` auth and current context.
3. Sync the funnel into a local directory or use the existing synced tree.
4. Refresh local editing docs with `fgrove docs`.
5. Make the requested edits.
6. Run available checks.
7. Run `fgrove sync up`.
8. Run `fgrove publish --env preview`.
9. Verify the returned preview URL before claiming the work is done.

Production publish is intentionally not part of the default flow. Ask for it
explicitly and provide the target domain when you want production.

## Team Setup

For now, use a shared global checkout instead of vendoring skills into each
project. Add this to a project `AGENTS.md` or `CLAUDE.md` when teammates should
use fstack:

```markdown
Use fstack for FunnelsGrove funnel work. Start with `edit-funnel` for hosted
funnel edits, and do not finish until a preview URL has been published and
verified.
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
