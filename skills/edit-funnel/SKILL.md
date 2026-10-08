---
name: edit-funnel
description: Use when editing an existing FunnelsGrove funnel in its remembered local folder, previewing changes, or delivering an authorized preview or production release.
---

# Edit Funnel

Before the first fstack skill in a conversation, run the [update check](../../docs/getting-started.md#agent-update-check): it applies a safe update automatically; reread this file if it reports `updated`, and offer any update it could not apply without blocking the task.

Reuse one working folder for each hosted funnel. Make the requested change there,
verify it locally, and deliver only to the environments the user authorized.
An edit normally keeps the same hosted funnel and local folder. A separate hosted
clone is a product decision for a separately requested copy, not a routine setup step.

## FunnelsGrove Contract Gate

For every implementation-facing task:

1. **MUST** read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` before choosing step metadata or changing code.
2. **MUST** derive step classification, answers, routing, analytics, and helpers only from those managed docs; **NEVER** copy them from research teardowns.
3. **MUST** run `fgrove validate` after the change and resolve every blocking diagnostic before preview, sync, or publish.

These gates remain mandatory when tests and builds pass, the change looks small, a deadline is urgent, or someone asks to skip them.

## 1. Resolve and reuse the working folder

Run the fstack checkout's `scripts/ensure-fgrove-cli` before hosted funnel work.
It checks and updates the installed CLI; if unavailable, use the installed CLI's
current update guidance. Resolve the requested API, workspace, project and funnel
from supplied context. Confirm the connected account with
`fgrove --api-url <api-url> whoami`.
Ask only for missing information that prevents selecting the right target.

**First follow [Local workspace](references/local-workspace.md)** to find,
verify, reuse and remember the funnel's canonical folder. Download only when no
usable folder exists. Preserve local changes and the sync manifest when refreshing;
temporary recovery files do not become another permanent checkout.

Run commands from that verified folder or pass its explicit `--dir`. Its
`.funnelsgrove-sync.json` supplies the local target; `fgrove use` is only a global
fallback for commands outside a synced folder. Use current `fgrove --help` and
subcommand help for flags rather than guessing from an older example.

Completion: an unambiguous target, one verified working folder, its remembered
location or a reported registration blocker, and local/remote changes accounted for.

## 2. Read the current implementation contracts

Refresh managed documentation with `fgrove docs --dir <local-dir>`, then read
the local `AGENTS.md` and `docs/funnelsgrove/START-HERE.md`. Follow the task route
to the exact step-type and contract pages before editing behavior. Also read
existing `AGENTS.project.md` and `Design.md` for product-specific constraints.

The managed bundle owns metadata, answers, routing, analytics, payments and
validation. For experiment work, read its `recipes/add-experiment.md`; use that
current workflow instead of maintaining experiment definitions from old source
examples. Research, screenshots and this skill supply context, not contracts.

Locate the files controlling the requested change and state the observable
success criteria. Install dependencies with the existing package manager and
lockfile when needed. Update packages only when requested or needed to unblock
the work; keep those changes scoped and report them.

Completion: the relevant contracts and product constraints are understood,
and the files and checks needed for the requested edit are identified.

## 3. Edit and verify locally

Work in the canonical folder. Preserve unrelated edits, generated/runtime
configuration and ignored secrets. Keep `.env*`, dependencies and build output
out of delivered source. Use meaningful product routes for new screens; follow
the existing project's ordering conventions for internal IDs and filenames.

For image or image-routing changes, read the managed asset/preload contract and
the [image QA checks](../qa-funnel/references/checklist.md#image-performance).
Keep raster artwork on the publish optimization path, register dimensions and
step `assetIds`, and preserve first-viewport priority plus low-priority loading
of likely next-step images. Verify the shell actually consumes that metadata.
For image-heavy funnels, keep a contract test covering valid asset references
and manifest-driven next-step preloading. Remote artwork must not bypass the
build-time compression and AVIF/WebP pipeline.

**MUST** run `fgrove validate --dir <local-dir>` after the change and resolve
blocking diagnostics. Run the tree's relevant tests, lint and build commands;
use its scripts and managed QA guidance to choose the checks.

Start the local preview using the project's instructions. Exercise the changed
screens through their real incoming and outgoing flow, inspect runtime errors,
and fix failures before delivery. Verify every created or edited screen at
`375x667`, `393x852`, `402x874`, and `1280x800`; also apply the managed local QA
requirements, including available viewport height and interaction states.
Check actual long copy, answers and validation errors for clipping, overlap,
hidden controls and horizontal overflow.

Use `qa-funnel` for [design checks](../qa-funnel/references/design.md) and scoped
flow QA. Checkout, pricing, payments, subscriptions, identity/email capture,
routing, analytics and broad visual/flow changes require its
[full checklist](../qa-funnel/references/checklist.md). Use approved test
identities and payment paths; name unavailable checks instead of treating them
as passed. Revalidate and retest after fixes.

Completion: contract validation and applicable local checks pass; the changed
flow and all four baseline layouts have evidence. If local preview cannot run,
report its specific blocker and the checks that remain unverified.

## 4. Deliver within the authorized scope

For local-only work, keep the result in the remembered folder and finish with
the verification report. A local edit does not authorize `git push`,
`fgrove github pull`, `fgrove sync up`, or a hosted publish.

For hosted delivery, follow [Publishing](references/publishing.md). Reuse
authorization already given for the target and environment. Ask only for the
missing authorization, after the local result is concrete and reviewable.
Choose one source path, verify the candidate on preview, and publish production
only when explicitly authorized for its target domain.

Completion: the requested delivery stage is reached and verified, or the
remaining authorization or technical blocker is named. A returned deployment
URL alone does not establish successful QA.

## 5. Hand off

Report the target and canonical folder so the next edit resumes there. Include
the change, checks and viewports exercised, and any blocked or skipped checks.
For hosted delivery, include URLs, version evidence, preview coverage and
post-publish results. Report image optimization/preload evidence when applicable.
Distinguish a verified local edit, synced draft, preview release and production
release; claim only the stage actually completed.
