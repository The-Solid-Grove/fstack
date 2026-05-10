# fstack Bootstrap Design

## Goal

Create the first usable version of `fstack`: a small skill pack for AI agents that edit FunnelsGrove web funnels through the local `fgrove` workflow.

## Scope

This bootstrap includes user-facing installation docs, a simple installer for Codex and Claude Code, and one skill named `edit-funnel`. It does not add a full package manager, generated skill variants, auto-update hooks, or additional funnel QA/design skills.

## Approach

Use one git checkout as the source of truth. The `setup` script links skills from this checkout into the selected host skill directory:

- Codex: `~/.codex/skills`
- Claude Code: `~/.claude/skills`
- Auto: install to every detected host, defaulting to Codex and Claude paths when detection is inconclusive

Updates stay simple: pull the repository and rerun setup.

## Files

- `README.md`: explain purpose, requirements, installation, updating, uninstalling, and `edit-funnel` usage.
- `setup`: idempotent Bash installer that creates host skill directories and symlinks `skills/*`.
- `skills/edit-funnel/SKILL.md`: workflow for loading a funnel with `fgrove`, editing local files, syncing up, publishing preview, and verifying before completion.
- `skills/edit-funnel/agents/openai.yaml`: Codex UI metadata.
- `tests/smoke.sh`: fast validation for installer syntax, required files, skill frontmatter, docs coverage, and dry-run installs.

## edit-funnel Workflow

The skill should follow the staged shape of the referenced brainstorming skill without copying its product-design gates:

1. Establish target workspace/project/funnel and whether edits should happen on a clone.
2. Check `fgrove` auth and context.
3. Sync or load the local funnel tree.
4. Refresh local funnel docs with `fgrove docs`.
5. Inspect structure before editing.
6. Make scoped edits in the local funnel tree.
7. Run available checks.
8. Sync up with a clear message.
9. Publish preview.
10. Verify the returned preview URL before claiming completion.

## Safety Rules

- Keep code simple and DRY.
- Do not publish production unless the user explicitly asks.
- Do not edit the original production funnel for risky changes when cloning is safer.
- Do not claim publish success until the CLI returns a preview URL and the URL has been opened or otherwise verified.
- Treat `.env` and other local secrets as runtime-only material.

## Testing

Use shell-based smoke tests for this bootstrap. The tests should verify the installer does not require network access, can run against temporary home directories, and creates symlinks for both Codex and Claude Code.
