---
name: qa-funnel
description: "Use when reviewing funnel screen images or rendered designs, or testing built funnels independently or after an edit or publish: content, responsive layout, branches, checkout, registration, subscription management, and production verification."
---

# QA Funnel

Before the first fstack skill in a conversation, follow the [update check](../../docs/getting-started.md#agent-update-check); offer available updates without blocking the task.

Inspect the requested screen artifact or local, preview, or production URL and produce an evidence-backed report. A QA request authorizes inspection and ordinary test interactions; publishing, changing source, real charges, and changing real customer subscriptions require their own authorization. Reuse permission already given for the target.

## 1. Establish scope

Resolve the artifact/URL, screen or funnel identity, revision/version and expected behavior from the conversation and project. For design review, read the exact copy, inspected reference, `Design.md` and prior findings. For runtime checks, also resolve the environment and any required test account. Ask only for missing inputs that prevent the requested checks.

- **Image design QA:** inspect each generated or supplied screen image using the image scope in [design checks](references/design.md); report image-direction results separately from pending runtime checks.
- **Rendered design QA:** inspect every requested screen and relevant state with the same design checks, including responsive and interaction evidence.
- **Scoped edit QA:** inspect the changed screens, their incoming/outgoing routes, and affected conversion paths; broaden when shared layout or behavior changes.
- **Full or post-publish QA:** use [the full checklist](references/checklist.md), including design, every step, branch, active experiment, paywall, registration, and subscription management.

For a synced FunnelsGrove project, read its `AGENTS.md` and `docs/funnelsgrove/START-HERE.md`, then the managed QA and relevant step-contract pages. They own expected behavior. Research and screenshots cannot supply routing, answer, analytics, or payment contracts. Run `fgrove validate --dir <local-dir>` when source is available; browser checks still apply when only a hosted URL is available.

## 2. Inspect and collect evidence

For each new or revised design screen, use the [per-screen calibration loop](references/design.md#per-screen-calibration-loop) to compare its matched reference and review text/composition together. With existing edit authorization, correct, reopen and recheck, then reconcile output documents; inspection-only QA returns findings to the owning design/edit workflow. For image scope, open each actual artifact and compare its copy, reference composition and shared style using the design reference. For rendered scope, walk the actual flow, not just direct links to isolated screens. Record which branches and variants you reached and how. Verify design at `375x667`, `393x852`, `402x874`, and `1280x800`; include keyboard, zoom/reflow, and supported-device checks from the design reference.

Use test identities and test-mode payments or the already approved payment-path equivalent. When unavailable, inspect the remaining reachable paths and name the untested transaction or subscription check as a blocker. An emulator can establish layout; it cannot establish real device wallet support.

For release candidates and post-publish QA, record matching preview and production versions and their evidence. Missing preview evidence blocks release readiness, but does not prevent inspecting the current production URL. Route any authorized publish or fix through `edit-funnel`, then retest the changed version. A QA-only request does not authorize publishing a missing preview.

## 3. Report and retest

Report separately:

- **Design:** image-direction and rendered-design status, readability, hierarchy, truthful copy, responsive fit, accessibility and image performance, with per-screen revision evidence.
- **Function:** steps, branches, experiments, answers, analytics, checkout, access and cancellation.
- **Release:** URLs and versions, matching preview evidence, post-publish production results.

For each failure include severity, artifact/URL, screen/variant/revision, viewport or image scope, reproduction, expected versus actual behavior, and screenshot or other evidence. Separate bugs from testable conversion suggestions. Mark checks **pass**, **fail**, **blocked**, or **not applicable**, with reasons; blocked is never pass.

Finish the audit when every in-scope check has a status. Return findings to the design/edit workflow for authorized corrections; reopen each corrected artifact or screen before passing that revision. Shared style/component changes require rechecking affected screens. Claim release readiness only when required checks pass on the candidate and required post-publish checks pass on production, or explicitly report the user's accepted exceptions. Retest fixes and adjacent paths before changing a failed result to pass.
