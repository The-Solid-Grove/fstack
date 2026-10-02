---
name: writing-funnel-copy
description: Use when writing or revising quiz-to-paywall funnel copy, positioning, questions, result screens, and subscription offers, including product research, screen strategy, and scoped copy reviews.
---

# Writing Funnel Copy

Turn the product, audience, and ad promise into a coherent purchase journey. For a new or substantially redesigned funnel, work in this order:

**Understand the product → Pre-work → user approval → Emotional Arc → user approval → screen copy.**

The two approvals are separate handoffs. A request to write a funnel starts this workflow; it does not approve strategy or an arc the user has not seen.

## FunnelsGrove Contract Gate

For every implementation-facing task:

1. **MUST** read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` before choosing step metadata or changing code.
2. **MUST** derive step classification, answers, routing, analytics, and helpers only from those managed docs; **NEVER** copy them from research teardowns.
3. **MUST** run `fgrove validate` after the change and resolve every blocking diagnostic before preview, sync, or publish.

These gates remain mandatory when tests and builds pass, the change looks small, a deadline is urgent, or someone asks to skip them.

## References by task

- New or redesigned funnel: **read the complete [Funnel Psychology Framework](references/funnel-psychology-framework.md) before preparing Pre-work.** It contains the detailed strategy, emotional progression, worked examples, and screen-writing criteria.
- Product understanding, positioning, or `PRODUCT_SENSE.md`: read [funnel research](references/funnel-research.md) during step 1 when evidence is missing.
- Pricing, checkout, trial, upsell, or renewal copy: [paywall guidance](references/funnel-paywall-best-practices.md) and [benchmark/compliance rules](references/funnel-benchmarks-and-compliance.md).
- Conversion diagnosis and A/B ideas: [conversion experiments](references/funnel-conversion-best-practices.md).
- Design and functional testing of a built funnel: `qa-funnel`.
- Acquisition, economics, analytics, and the full course: `web2app-essentials` (Web-to-Web Essentials).

## Workflow for a new or redesigned funnel

Keep each stage as a clearly titled artifact in the conversation or the project's existing planning document, such as `PLAN.md`. Follow existing file conventions when saving; separate files are optional. Record which version of Pre-work and Emotional Arc the user approved so later work can use them without repeating the interview.

### 1. Understand the product

Read the available product brief, `PRODUCT_SENSE.md`, existing funnel, entry creative, offer, and proof. Establish what the product actually does, who it serves, their entry situation, the advertised promise, the real mechanism, pricing/access, limitations, and requested scope. Ask only for missing facts that change the strategy; label hypotheses and proof gaps.

**Done when:** a concise product brief separates facts from assumptions and identifies the audience, entry promise, offer, and available evidence. Research or update product sense where needed. This brief is context for Pre-work; it is not the proposed screen sequence.

### 2. Prepare Pre-work and obtain approval

Follow [Pre-work](references/funnel-psychology-framework.md#pre-work): develop the five-column table, choose the primary problem and failure of current alternatives, connect the product mechanism to a credible benefit, and define the transformation and entry promise. Include objections, evidence gaps, and the recommended strategic focus.

Present **Pre-work** as a reviewable artifact and ask the user to approve it or request changes. **Stop here until the user explicitly approves this Pre-work. Do not draft the Emotional Arc, screen sequence, headlines, or CTAs while approval is pending.** Revise and present the artifact again when changes are requested.

**Done when:** the framework's Pre-work checks pass and the user approves the presented strategy.

### 3. Build Emotional Arc and obtain approval

From the approved Pre-work, follow [Emotional Arc](references/funnel-psychology-framework.md#emotional-arc). Recommend a screen budget if none was supplied. Map each proposed screen's narrative job, incoming feeling/belief, intended emotional shift, useful value/evidence, effort asked, objection, and transition. Cover meaningful branches and the offer/access handoff.

Present **Emotional Arc** with a short explanation of the overall progression and effort/value balance. Use structural screen labels; finished headlines, question wording, body copy, and CTAs belong to step 4. Ask the user to approve the arc or request changes. **Stop here until the user explicitly approves this Emotional Arc.**

**Done when:** the framework's arc checks pass and the user approves the proposed journey.

### 4. Write the screen copy

Use the approved arc's screen IDs and follow the framework's [screen-copy specification](references/funnel-psychology-framework.md#screen-copy). Write the headline, body, choices, CTA, visible proof, visual direction, actual personalization, and intended transition for each screen. Read the paywall and benchmark/compliance references before drafting offer terms. Clearly mark unresolved proof slots and product facts for confirmation.

**Done when:** each screen fulfills its approved role, all required copy fields are present, claims have sources or explicit unresolved slots, and the [review checks](references/funnel-psychology-framework.md#review-checks) pass. Return the full screen copy with links to its approved Pre-work and Emotional Arc, plus any remaining gaps and useful experiments.

### 5. Hand off within the requested scope

When visualization is requested, use `preview-funnel` for a temporary local mockup. When implementation is requested, use `create-funnel` or `edit-funnel`, then `qa-funnel` to test the built result. Strategy or copy approval is not permission to publish.

## Continuing, revising, or reviewing existing work

- Reuse explicitly approved Pre-work and Emotional Arc when they still match the product, audience, promise, offer, and current requested scope. State what approval you are relying on; an existing file or silence alone is not approval.
- For a local wording correction that preserves the existing strategy, offer, sequence, and emotional progression, inspect the affected screen and adjacent transitions, read the relevant framework rules, and return the scoped revision. Historical approval records are not required for this narrow correction; avoid rebuilding unrelated screens.
- A change to the strategic focus, audience, promise, mechanism, or offer reopens Pre-work approval and then arc approval for the affected scope. A change to the sequence or emotional progression reopens arc approval before rewriting the affected screens.
- For a new or redesigned flow with missing approvals, prepare the missing stage for the requested scope and obtain approval in order. Keep an unchanged approved stage intact.
- A review-only request can return findings and recommendations directly. Apply the workflow above when moving from findings into rewritten copy.

Copy research owns messaging and observed structure only. The synced project's `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` own step metadata, answer persistence, routing, analytics, payments, and helpers. Follow their exact step-type and contract pages when translating copy into code.
