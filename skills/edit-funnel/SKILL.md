---
name: edit-funnel
description: Use when editing FunnelsGrove hosted funnels through local CLI sync, including loading a project or funnel with fgrove, making scoped local updates, syncing changes back, publishing preview, and verifying the preview URL before finishing.
---

# Edit Funnel

## Overview

Use this skill to turn a hosted FunnelsGrove funnel edit request into a verified
preview deployment. Work from the local synced funnel tree, keep edits scoped,
and finish only after `fgrove publish --env preview` returns a URL that has been
checked.

## Required Inputs

Collect these before editing, asking one question at a time only when local
context cannot answer them:

1. Target workspace, project, and funnel id or slug.
2. Requested edit and success criteria.
3. Whether the original funnel may be edited directly or a clone is safer.
4. Target local directory, if the funnel is already synced.
5. API URL when the default `FUNNELSGROVE_API_URL` is not the target.

## CLI Reference

Prefer the installed `funnelsgrove-cli` skill when available. In this workspace,
the source reference is:

`/Users/andrew/work/funnelsgrove/app-deals/codex-skills/funnelsgrove-cli/SKILL.md`

Use this command shape as the minimum workflow:

```bash
<fstack-checkout>/scripts/ensure-fgrove-cli
fgrove whoami
fgrove use --project <project-id-or-slug> --funnel <funnel-id-or-slug>
fgrove status
fgrove sync down --funnel <id-or-slug> --dir <local-dir>
fgrove docs --dir <local-dir>
fgrove sync up --message '<summary>'
fgrove publish --env preview --message '<summary>'
```

Add `--api-url <api-url>` or `--workspace <workspace-id>` when the target is not
covered by defaults.

Run the fstack `scripts/ensure-fgrove-cli` helper before every hosted funnel
edit. It checks the installed `fgrove` version against npm and installs
`@funnelsgrove/cli@latest` when the CLI is missing or outdated. If the helper is
not available, do the equivalent check manually before continuing. Always run
`fgrove docs --dir <local-dir>` after that check so a newly installed CLI can
refresh the funnel-specific editing docs.

## Workflow

### 1. Establish the Target

Identify the workspace, project, and funnel before loading or editing. If the
request affects a production funnel, changes pricing or checkout, or is
experimental, prefer a clone unless the user explicitly wants the original
edited.

```bash
fgrove projects list
fgrove funnels list
fgrove funnels clone --funnel <source-id-or-slug> --name <new-name>
```

### 2. Load the Local Project

Check/update the CLI version first, then check auth and context. Sync down only
when there is no current synced directory or when the local tree is stale. Keep
`.funnelsgrove-sync.json` in place because it carries the draft sync state.

```bash
<fstack-checkout>/scripts/ensure-fgrove-cli
fgrove whoami
fgrove use --project <project-id-or-slug> --funnel <funnel-id-or-slug>
fgrove status
fgrove sync down --funnel <id-or-slug> --dir <local-dir>
fgrove docs --dir <local-dir>
```

### 3. Inspect Before Editing

Read the local docs produced by `fgrove docs`, especially the generated
`AGENTS.md` or `agent.md`, then inspect the funnel tree with fast file search.
Treat those generated agent docs as the source of truth for funnel-specific
build and edit rules. Find the exact pages, steps, content files, styles,
assets, and tests that control the requested behavior.

```bash
rg --files <local-dir>
```

### 4. Make Scoped Updates

Edit only the local funnel tree. Keep code simple and DRY. Avoid unrelated
refactors, metadata churn, generated output, and secret files. Treat `.env` and
`.env.*` as local runtime material, not uploadable source.

### 5. Run Local Checks

Run the checks that exist in the synced tree. Prefer the narrowest relevant
check first, then a build or full smoke pass when available.

```bash
npm test
npm run lint
npm run build
```

If no package scripts exist, still verify the edited files structurally and open
the local preview if the tree provides a dev command.

### 6. Sync and Publish Preview

Use a clear message that names the edit. Do not publish production from this
skill unless the user explicitly asks for production and provides the target
domain.

```bash
fgrove sync up --message '<summary>'
fgrove publish --env preview --message '<summary>'
```

Save the returned preview URL, published version id, and sequence when present.

### 7. Verify Preview

Open or otherwise verify the preview URL before claiming completion. At minimum,
check the first step, the edited step, and any paywall, checkout, or conversion
step affected by the request. Also check browser console/runtime errors when a
browser tool is available.

## Completion Gate

Finish only after all of these are true:

1. Target workspace/project/funnel and local directory are recorded.
2. Requested edits are synced with `fgrove sync up`.
3. Preview is published with `fgrove publish --env preview`.
4. Returned preview URL is verified.
5. Checks run are listed, including any unavailable checks.
6. Any blockers have a named root cause and concrete next step.

## Safety Rules

- Never sync secrets, `.env*`, `node_modules`, `.next`, `out`, or local build output.
- Do not overwrite non-target funnel files to make a broad visual pass easier.
- Do not edit production-critical checkout/pricing flows directly when cloning is safer.
- Do not call work complete based only on local tests; preview verification is required.
