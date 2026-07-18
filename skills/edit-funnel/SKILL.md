---
name: edit-funnel
description: Use when editing FunnelsGrove hosted funnels through local CLI sync, including scoped local edits, local preview, QA, preview publish, or production publish.
---

# Edit Funnel

## Overview

Use this skill to turn a hosted FunnelsGrove funnel edit request into a locally
previewed change, then a verified preview or production deployment when the user
explicitly wants to publish. Work from the local synced funnel tree, keep edits
scoped, and default to a local preview loop before any hosted publish.

## FunnelsGrove Contract Gate

For every implementation-facing task:

1. **MUST** read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` before choosing step metadata or changing code.
2. **MUST** derive step classification, answers, routing, analytics, and helpers only from those managed docs; **NEVER** copy them from research teardowns.
3. **MUST** run `fgrove validate` after the change and resolve every blocking diagnostic before preview, sync, or publish.

These gates remain mandatory when tests and builds pass, the change looks small, a deadline is urgent, or someone asks to skip them.

## Required Inputs

Collect these before editing, asking one question at a time only when local
context cannot answer them:

1. Target workspace, project, and funnel id or slug.
2. Requested edit and success criteria.
3. Whether the original funnel may be edited directly or a clone is safer.
4. Target local directory, if the funnel is already synced.
5. API URL when the default `FUNNELSGROVE_API_URL` is not the target.
6. QA credentials or test payment details when checkout or subscription QA is
   required.

## CLI Reference

Prefer the installed `funnelsgrove-cli` skill when available for full command
help. Use the command shape below as the minimum hosted CLI workflow. Local
preview and contract commands come from the managed funnel docs and should run before
syncing any hosted draft.

```bash
<fstack-checkout>/scripts/ensure-fgrove-cli
fgrove whoami
fgrove use --project <project-id-or-slug> --funnel <funnel-id-or-slug>
fgrove status
git -C <local-dir> status --short
fgrove github status --dir <local-dir>
fgrove sync down --funnel <id-or-slug> --dir <local-dir>
fgrove docs --dir <local-dir>
# read AGENTS.md and docs/funnelsgrove/START-HERE.md
# run fgrove validate and local preview as directed before hosted sync
# if GitHub is connected: git push, then fgrove github pull
# if GitHub is not connected:
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

### 2. Load, Refresh, and Merge the Local Project

Check/update the CLI version first, then check auth and context. Sync down only
when there is no current synced directory or after the local tree is clean or
checkpointed. Keep `.funnelsgrove-sync.json` in place because it carries the
draft sync state.

```bash
<fstack-checkout>/scripts/ensure-fgrove-cli
fgrove whoami
fgrove use --project <project-id-or-slug> --funnel <funnel-id-or-slug>
fgrove status
git -C <local-dir> status --short
fgrove github status --dir <local-dir>
fgrove sync down --funnel <id-or-slug> --dir <local-dir>
fgrove docs --dir <local-dir>
```

If the local tree has changes, create a checkpoint before refreshing remote
state. Prefer a normal WIP commit on a local branch when the directory is a git
checkout; otherwise copy the changed files or sync the latest draft into a temp
directory. Do not run `fgrove sync down` over a dirty synced directory unless
the user explicitly wants to discard local changes and you pass `--force`.

When GitHub is connected and remote is ahead, run `fgrove github pull --dir
<local-dir>` to pull GitHub into the hosted draft, then poll `fgrove github
status --dir <local-dir>` until the pull job is completed or skipped. After
that, sync the latest draft into a clean directory and merge the local
checkpoint with normal git or file diff tools before editing further.

For GitHub-connected funnels, GitHub is the write path for source changes. After
local checks pass, commit and push with normal git, then run `fgrove github pull
--dir <local-dir>` and poll `fgrove github status --dir <local-dir>` until the
pull job completes or skips. Do not run `fgrove sync up` for the same local
diff.

When GitHub is not connected, use the hosted draft as remote truth: run `fgrove
sync down --funnel <id-or-slug> --dir <temp-dir>` or use an already selected
`fgrove use` context to download the current draft into a temporary clean
directory. Compare it with the local checkpoint, merge intentionally, then
continue from the merged local tree. If `fgrove sync up` reports that the remote
draft changed since the local directory was synced, repeat this temp-directory
merge flow before retrying.

### 3. Inspect Before Editing

Read the local docs produced by `fgrove docs`, especially the generated
`AGENTS.md`, then open `docs/funnelsgrove/START-HERE.md` and follow its task
route. Treat this managed bundle as the contract source of truth for step
metadata, choices, email capture, lifecycle and semantic analytics, routing,
payments, and validation. Read the exact step-type page plus any linked
contract page before editing behavior. An older `agent.md`, this fstack skill,
or a research teardown may help with workflow or visual structure, but cannot
override or supply implementation contracts. Find the exact pages, steps,
content files, styles, assets, and tests that control the requested behavior.

```bash
rg --files <local-dir>
```

### 4. Update Local Project Packages

When the user asks to update packages, or when stale dependencies block local
checks or preview, update the synced funnel project with the package manager
already used by the tree. Detect it from lockfiles and generated docs:

| Lockfile | Package manager | Inspect | Update | Install |
| --- | --- | --- | --- | --- |
| `package-lock.json` | npm | `npm outdated` | `npm update` | `npm install` |
| `pnpm-lock.yaml` | pnpm | `pnpm outdated` | `pnpm update` | `pnpm install` |
| `yarn.lock` | yarn | `yarn outdated` | `yarn upgrade` | `yarn install` |
| `bun.lockb` | bun | `bun outdated` | `bun update` | `bun install` |

Use one package manager per project. Do not create a new lockfile with a
different tool. If no lockfile exists, follow `packageManager` in `package.json`
or ask before choosing. After updating, run the install command for that manager
so the lockfile and installed dependencies match, then run the local checks.

Keep package updates separate from unrelated funnel edits when possible. Report
the package manager, update command, install command, changed lockfile, and any
security or peer-dependency warnings.

### 5. Make Scoped Updates

Edit only the local funnel tree. Keep code simple and DRY. Avoid unrelated
refactors, metadata churn, generated output, and secret files. Treat `.env` and
`.env.*` as local runtime material, not uploadable source.

After creating or editing any funnel step, run a content-fit audit for that step
in the local preview. Verify all four default breakpoints: small `375x667`,
medium `393x852`, large `402x874`, and desktop-small `1280x800`. Fix clipped,
overflowing, overlapping, or hidden content before moving on to another step.

When creating a step, keep the public route meaningful. `path` should describe
the screen's purpose, such as `/motivation`, `/fitness-goal`, `/email-capture`,
or `/paywall`; do not create user-facing paths like `/step-1` or `/step-07`.
Sequential ids and `step-NN-*` filenames are acceptable when the existing funnel
uses them for ordering, but URLs should be readable product routes.

### Experiment Source of Truth

For new or edited experiments, prefer the FunnelsGrove UI/API as the source of
truth. It owns the database row, PostHog flag, and generated
`src/config/experiments.generated.ts`; `src/config/experiments.ts` should usually
stay as the generated compatibility wrapper. If a user asks for a code-authored
experiment or the UI/API path is unavailable, keep the object source-readable:
explicit `sourceStepId` or `stepId`, explicit variant route step ids, labels,
traffic percentages, and normal manifest steps/edges for every variant.

When porting an experiment from another funnel or staging variant steps before
the experiment is live, follow `references/experiment-migration.md`: keep
inactive variants unbranched (manifest step, no `branches` entry, unreachable
from the default flow), never copy experiment ids across funnels, replace
hardcoded `goToStep` targets with `goNext()` plus manifest edges, and never
hand-edit the generated managed docs bundle.

### Image Performance Lock

For any new or edited image, image-heavy step, or route that changes which
images appear next, preserve the ClaimBee/Blessly pattern:

- Keep raster assets in paths the FunnelsGrove publish artifact pipeline can
  optimize. Do not replace local public/content-managed images with remote
  image URLs that bypass build-time compression and AVIF/WebP variant creation.
- Keep build-time image reduction enabled. When publishing, check
  `publishBuild.stageTimings.imageVariants`, CLI stage output, or deployment
  metadata so image optimization is confirmed or named as unavailable.
- Declare image metadata in `funnelManifest.assets` with stable `src`, `width`,
  and `height`, then attach each step's images with `assetIds`. Update
  `assetIds` whenever step artwork or routing changes.
- Use the normal framework priority/preload path for first-viewport images.
  In the flow shell, warm only likely next-step image assets at low priority
  after the active step loads; do not preload the whole funnel up front.
- For image-heavy funnels, add or keep a contract test that every declared
  `assetId` exists and that the shell uses manifest-driven next-step preloads
  instead of a component-local hardcoded preload map.

### 6. Run Local Checks

Run the checks that exist in the synced tree. Prefer the narrowest relevant
check first, then a build or full smoke pass when available.

```bash
fgrove validate --dir <local-dir>
npm test
npm run lint
npm run build
```

`fgrove validate` is required after creating or changing a step, its metadata,
answers, routing, analytics, or payment behavior. Resolve every blocking
diagnostic before preview or sync; do not treat a passing framework build as a
replacement for contract validation.

If no package scripts exist, still verify the edited files structurally and open
the local preview if the tree provides a dev command.

### 7. Preview Locally and Adjust

Start or open the local preview by default before any hosted publish. Use the
generated funnel docs first, then package scripts such as `npm run dev` when the
docs point there. Inspect the changed flow in the browser, check console/runtime
errors when a browser tool is available, adjust the local files, rerun checks,
and preview locally again until the local result matches the request.

For created or edited steps, the local preview inspection must include the
content-fit audit at small `375x667`, medium `393x852`, large `402x874`, and
desktop-small `1280x800` before considering the step ready.

For major edits, ask the user whether to run the full QA checklist before
publishing. Major edits include checkout, pricing, payment, subscription,
cancellation, identity/email capture, routing, analytics, or broad visual/flow
changes.

### 8. Ask Before Publishing

Ask the user whether to publish after local preview verification. Do not sync up
or publish only because local checks passed. If the user declines publishing,
stop after reporting the local checks and local preview status.

### 9. Sync, Publish Preview, and Run QA

Use a clear message that names the edit. Do not publish production from this
skill unless the user explicitly asks for production and provides the target
domain.

For GitHub-connected funnels, push source changes through GitHub and pull them
into the hosted draft:

```bash
git push
fgrove github pull --dir <local-dir>
fgrove github status --dir <local-dir>
fgrove publish --env preview --message '<summary>'
```

Poll `fgrove github status` until the pull job has completed or skipped before
publishing. Do not also run `fgrove sync up` for the same source change.

For funnels without GitHub, sync local source directly to the hosted draft:

```bash
fgrove sync up --message '<summary>'
fgrove publish --env preview --message '<summary>'
```

Save the returned preview URL, published version id, and sequence when present.

Run QA on the preview URL before any production publish. At minimum, check the
first step, the edited step, and any paywall, checkout, or conversion step
affected by the request. For major edits and production candidates, run the full
QA checklist.

### 10. Verify Preview Coverage for Production

Before production publish or post-publish production QA, verify whether the
current production candidate or current production version already has a matching
preview build. Use the current `fgrove` CLI, deployment history, version id,
sequence, generated funnel docs, or API status available for the target.

Record the production URL or target domain, preview URL, version ids, sequences,
and how the match was verified. If there is no matching preview build, publish
to preview first and run the full QA checklist on the preview URL before
continuing. Missing preview QA is a blocker unless the user explicitly accepts
the risk.

### 11. Publish Production and Run Production QA

Publish production only when the user explicitly approves production after the
preview URL has passed QA. Use the production publish command required by the
generated docs or current `fgrove` CLI, for example:

```bash
fgrove publish --env production --message '<summary>'
```

Save the returned production URL, published version id, and sequence when
present. Run the same required QA on the production URL after publish. Do not
claim production completion when production QA fails or cannot run unless the
user explicitly accepts the risk.

## QA Checklist

Use the narrowest QA that covers the edit for small copy/style changes. Use the
full checklist in `docs/funnel-qa-checklist.md` for major edits,
preview-to-production candidates, missing preview-build coverage, and every
production URL after publish.

Full QA verifies every step, every branch, every active A/B experiment, submit email
or identity capture, Apple Pay and Google Pay button appearance on checkout,
paywall and checkout experience, test payment or approved payment-path
equivalent, closing and reopening checkout for the larger discount path, the
complete registration page, registration and legal/support/account links, and
the `/manage-subscription` cancellation flow when a test subscription is
available.

If a flow cannot run because test credentials, payment mode, an existing
subscription, route support, or third-party services are unavailable, report the
skipped flow as a named blocker or explicit unavailable item. Production QA
blockers block the completion claim unless the user explicitly accepts the risk.

## Completion Gate

Finish only after all of these are true:

1. Target workspace/project/funnel and local directory are recorded.
2. Requested edits pass available local checks.
3. Local preview is opened or an unavailable local preview has a named reason.
4. Every created or edited step has a reported content-fit audit at small
   `375x667`, medium `393x852`, large `402x874`, and desktop-small `1280x800`.
5. Image edits preserve build-time image optimization and manifest-driven
   next-step preloading, or any unavailable optimization/preload check is named.
6. The user is asked whether to publish after local preview.
7. If publishing, requested edits are synced through the correct source path:
   GitHub-connected funnels use normal `git push` plus `fgrove github pull`;
   funnels without GitHub use `fgrove sync up`.
8. If publishing, preview is published with `fgrove publish --env preview`.
9. If preview is published, preview QA is run and reported.
10. If production is explicitly requested or post-publish QA is requested,
   preview-build coverage for the current production candidate or version is
   verified and reported.
11. If there is no matching preview build, preview is published and full QA is
   run on the preview URL before continuing.
12. If production is explicitly requested, production is published only after
   preview QA and production QA is run on the production URL.
13. Checks and QA flows run are listed, including unavailable checks or skipped
   flows.
14. Any blockers have a named root cause and concrete next step.

## Safety Rules

- Never sync secrets, `.env*`, `node_modules`, `.next`, `out`, or local build output.
- Do not overwrite non-target funnel files to make a broad visual pass easier.
- Do not bypass the publish pipeline's image optimization with unoptimized
  remote image URLs for funnel-critical artwork.
- Do not edit production-critical checkout/pricing flows directly when cloning is safer.
- Do not publish before the user approves publishing after local preview.
- Do not call work complete based only on local tests; local preview and the
  relevant hosted QA gate are required.
