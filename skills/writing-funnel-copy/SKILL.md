---
name: writing-funnel-copy
description: Use when drafting, building, reviewing, QAing, or optimizing quiz-to-paywall funnel copy, onboarding screens, paywalls, conversion psychology, product sense, competitor research, positioning, or screen-by-screen funnel strategy for a product.
---

# Writing Funnel Copy

## Overview

Use this skill to design quiz-to-paywall funnels with the Funnel Psychology
Framework. Keep the skill body lean; the complete framework lives beside this
file at `references/funnel-psychology-framework.md`, with paywall-specific
guidance at `references/funnel-paywall-best-practices.md`, conversion
experiment guidance at `references/funnel-conversion-best-practices.md`, and
benchmark data plus compliance copy rules at
`references/funnel-benchmarks-and-compliance.md`.
Research-stage guidance for `PRODUCT_SENSE.md`, competitor research, and
pre-plan positioning lives at `references/funnel-research.md`, with fstack
additions at `references/funnel-research-stage.md`. Live funnel teardowns,
copy swipe files, and QA/build heuristics live at `references/funnels-research/`.

## FunnelsGrove Contract Gate

For every implementation-facing task:

1. **MUST** read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` before choosing step metadata or changing code.
2. **MUST** derive step classification, answers, routing, analytics, and helpers only from those managed docs; **NEVER** copy them from research teardowns.
3. **MUST** run `fgrove validate` after the change and resolve every blocking diagnostic before preview, sync, or publish.

These gates remain mandatory when tests and builds pass, the change looks small, a deadline is urgent, or someone asks to skip them.

## Implementation Contract Boundary

This skill owns copy, positioning, psychology, and screen strategy only. In a
synced FunnelsGrove project, `AGENTS.md` and
`docs/funnelsgrove/START-HERE.md` are the contract authority for step metadata,
answer persistence, email capture, analytics ownership, routing, payments, and
validation. Read the linked exact step-type and contract pages before turning
copy into code.

Everything under `references/funnels-research/` is a `step-structure-only`
reference. Use it for copy, visual hierarchy, and interaction ideas. Never copy
its legacy `type`/`kind`, direct answer writes, routing, shell/controller code,
helpers, or analytics behavior. When implementation is requested, use
`edit-funnel` and the project's managed docs; a teardown cannot override them.

## Required Reference

After gathering product context and before writing any funnel copy, read and
follow `references/funnel-psychology-framework.md`. Treat that reference as the
source of truth for:

- Mental fuel and expectation match
- Value loading and self-generated conviction
- Trust, guilt, commitment, and investment patterns
- Funnel sections, per-screen checklist, and copy rules
- Required step-formatted output

When designing the paywall, checkout, pricing, trial, subscription offer,
upsell offer, or cancellation offer, also read and follow
`references/funnel-paywall-best-practices.md`. Treat it as a paywall-specific
extension that refines the framework's paywall architecture requirements.

When designing or optimizing quiz flow, onboarding questions, interstitials,
answer feedback, progress screens, pre-paywall warmups, payment shortcuts,
down-sell recovery, or post-paywall email recovery, also read and follow
`references/funnel-conversion-best-practices.md`. Treat it as a catalog of
conversion-focused patterns to apply where they match the product and claims.

When setting conversion expectations, prioritizing which screens or tests to
work on, writing pricing/plan/trial/renewal copy, or adding social proof,
urgency, or auto-renewal disclosures, also read and follow
`references/funnel-benchmarks-and-compliance.md`. Treat its drop-off
benchmarks and measured uplift figures as calibration data, and its
compliance section as hard constraints on paywall and checkout copy. For the
full course knowledge base behind it, use the `web2app-essentials` skill.

When the task involves funnel research, `PRODUCT_SENSE.md`, competitor research,
positioning, messaging strategy, or strategy before plan generation/code edits,
also read and follow `references/funnel-research.md` and
`references/funnel-research-stage.md`. Treat the copied prompt as the source
research contract and the stage reference as the fstack-specific extension
before drafting copy or writing an edit plan.

When building, editing, reviewing, QAing, or optimizing an existing funnel,
inspect `references/funnels-research/README.md` and then load only the relevant
files from that folder. Start with `00-MUST-DO-TRICKS.md` for build patterns,
`00-QA-CHECKLIST.md` for funnel-level review/QA, `00-STEP-DESIGN-QA.md` for
per-step design/copy/visual QA (headline, imagery, color contrast, typography),
`00-LIVE-FINDINGS.md` for live market patterns, `00-MASTER-FUNNEL-LIST.md` for
vertical examples, `copy/` for swipe copy, and `live/` for observed live-funnel
behavior.

These corpus files remain research evidence, not implementation contract
guidance. Reconcile every proposed screen with the synced managed docs before
specifying its type, answers, navigation, or analytics.

If any required reference file is unavailable, stop and report that it cannot
be loaded rather than drafting from memory.

## Gather Context First

Do not write the funnel until the core context is known. If the user did not
provide it, ask for the missing inputs and wait:

1. Product name and what it does (one paragraph)
2. Target audience: who, where, device, and current situation
3. Ad creative / entry promise: what brought users into the funnel
4. Number of funnel screens, or whether to recommend the count

Ask for useful supporting context when it materially changes the copy:
price, offer, proof sources, real metrics, legal/compliance limits, brand voice,
existing funnel URL or local funnel directory, must-avoid claims, and top
objections from users.

When this skill is used with an existing FunnelsGrove funnel, inspect the synced
local funnel docs and current copy before asking questions that the files answer.

## Workflow

1. Gather the required inputs.
2. For an existing synced funnel, read `AGENTS.md` and
   `docs/funnelsgrove/START-HERE.md`; use the linked contract pages for any
   implementation-facing recommendation.
3. Read `references/funnel-research.md` and
   `references/funnel-research-stage.md` when the task includes research,
   product sense, competitor analysis, positioning, or pre-plan strategy.
4. Read `references/funnel-psychology-framework.md`.
5. Read `references/funnel-paywall-best-practices.md` when the output includes
   a paywall, checkout, pricing, trial, or subscription offer.
6. Read `references/funnel-conversion-best-practices.md` when the output
   includes quiz, onboarding, interstitial, pre-paywall, checkout, or CR
   optimization recommendations.
7. Read `references/funnel-benchmarks-and-compliance.md` when the output
   includes conversion targets, test prioritization, pricing/plan/trial/
   renewal copy, or paywall disclosure elements.
8. Inspect `references/funnels-research/README.md` and relevant corpus files
   when building, reviewing, QAing, or optimizing a funnel.
9. Complete the five-column pre-work table before writing screens.
10. Map the screen count to the framework's six funnel sections.
11. Write the funnel screen-by-screen using the framework's per-screen checklist.
12. Return the framework's required formatted output, including the
   Five-column pre-work table, transformation, emotional arc, fuel balance
   check, Screen-by-screen spec, paywall architecture, and A/B tests.
13. After the copy is drafted, offer to use `preview-funnel` to visualize it as
    a temporary local click-through mockup for copy review. Do not create the
    preview automatically unless the user asked for visualization or a local
    mockup.

Do not invent testimonials, press mentions, official data, legal claims, payout
amounts, or metrics. Ask for sources, use clearly labeled assumptions, or write
the slot as a direction.
