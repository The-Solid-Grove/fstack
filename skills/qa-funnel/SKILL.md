---
name: qa-funnel
description: Use when testing a funnel independently or after an edit or publish: design, content, responsive layout, branches, checkout, registration, subscription management, and production verification.
---

# QA Funnel

Inspect the requested local, preview, or production URL and produce an evidence-backed report. A QA request authorizes inspection and ordinary test interactions; publishing, changing source, real charges, and changing real customer subscriptions require their own authorization. Reuse permission already given for the target.

## 1. Establish scope

Resolve the URL, environment, funnel identity, version, expected flow, and available test account from the conversation and project. Ask only for missing inputs that prevent the requested checks.

- **Design QA:** inspect every requested screen with [design checks](references/design.md).
- **Scoped edit QA:** inspect the changed screens, their incoming/outgoing routes, and affected conversion paths; broaden when shared layout or behavior changes.
- **Full or post-publish QA:** use [the full checklist](references/checklist.md), including design, every step, branch, active experiment, paywall, registration, and subscription management.

For a synced FunnelsGrove project, read its `AGENTS.md` and `docs/funnelsgrove/START-HERE.md`, then the managed QA and relevant step-contract pages. They own expected behavior. Research and screenshots cannot supply routing, answer, analytics, or payment contracts. Run `fgrove validate --dir <local-dir>` when source is available; browser checks still apply when only a hosted URL is available.

## 2. Inspect and collect evidence

Walk the actual flow, not just direct links to isolated screens. Record which branches and variants you reached and how. Verify design at `375x667`, `393x852`, `402x874`, and `1280x800`; include keyboard, zoom/reflow, and supported-device checks from the design reference.

Use test identities and test-mode payments or the already approved payment-path equivalent. When unavailable, inspect the remaining reachable paths and name the untested transaction or subscription check as a blocker. An emulator can establish layout; it cannot establish real device wallet support.

For release candidates and post-publish QA, record matching preview and production versions and their evidence. Missing preview evidence blocks release readiness, but does not prevent inspecting the current production URL. Route any authorized publish or fix through `edit-funnel`, then retest the changed version. A QA-only request does not authorize publishing a missing preview.

## 3. Report and retest

Report separately:

- **Design:** readability, hierarchy, truthful copy, responsive fit, accessibility and image performance.
- **Function:** steps, branches, experiments, answers, analytics, checkout, access and cancellation.
- **Release:** URLs and versions, matching preview evidence, post-publish production results.

For each failure include severity, URL/step/variant, viewport, reproduction, expected versus actual behavior, and screenshot or other evidence. Separate bugs from testable conversion suggestions. Mark checks **pass**, **fail**, **blocked**, or **not applicable**, with reasons; blocked is never pass.

Finish the audit when every in-scope check has a status. Claim release readiness only when required checks pass on the candidate and required post-publish checks pass on production, or explicitly report the user's accepted exceptions. Retest fixes and adjacent paths before changing a failed result to pass.
