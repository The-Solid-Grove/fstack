---
name: writing-funnel-copy
description: Use when writing or revising quiz-to-paywall funnel copy, positioning, question and energy-screen rhythm, plan reveals, email capture, and subscription paywalls, including product and reference-funnel research, Pre-work, Emotional Arc, screen copy, and scoped copy reviews.
---

# Writing Funnel Copy

Before the first fstack skill in a conversation, run the [update check](../../docs/getting-started.md#agent-update-check): it applies a safe update automatically; reread this file if it reports `updated`, and offer any update it could not apply without blocking the task.

Turn the product, audience and ad promise into a quiz-to-paywall journey that keeps the visitor's energy high: easy questions broken up every 2–3 screens by **energy screens** that reassure, prove and excite, a personal **plan** reveal, **email**, and a **paywall** cloned from a proven reference structure. Every screen is a psychological instrument with one job, and value is shown so the visitor concludes it themselves (the Hitchcock principle).

For a new or substantially redesigned funnel, work in this order:

**Product → Reference scan → Pre-work → approval → Emotional Arc → approval → Screen copy → Self-test → Hand-off.**

The two approvals are separate handoffs. A request to write a funnel starts this workflow; it does not approve strategy or an arc the user has not seen.

## FunnelsGrove Contract Gate

For every implementation-facing task:

1. **MUST** read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` before choosing step metadata or changing code.
2. **MUST** derive step classification, answers, routing, analytics, and helpers only from those managed docs; **NEVER** copy them from research teardowns.
3. **MUST** run `fgrove validate` after the change and resolve every blocking diagnostic before preview, sync, or publish.

These gates remain mandatory when tests and builds pass, the change looks small, a deadline is urgent, or someone asks to skip them.

## References by task

| Task | Read |
| --- | --- |
| New or redesigned funnel | The complete [Funnel Psychology Framework](references/funnel-psychology-framework.md) before Pre-work; the [Funnel Rhythm Template](references/funnel-rhythm-template.md) before the Emotional Arc. |
| Energy screens | The [Energy Screen Catalog](references/energy-screens.md) when assigning archetypes in the arc and again when writing each energy screen. |
| Paywall | The [Paywall Blueprints](references/paywall-blueprints.md) when choosing the paywall in the arc and when writing its copy. |
| Research, drafting or review | The relevant sections of [Funnel Best Practices](references/funnel-best-practices.md); cite stable `FBP-###` IDs in findings and experiment proposals. |

Use `qa-funnel` for design and functional testing of a built funnel; use `web2app-essentials` for acquisition, economics, analytics and the full Web-to-Web course.

## Reference funnels

`fgrove references` reads the public Funnel Screens library (recorded journeys with screen text, appearance and full-height images) without login. Run the Fstack checkout's `scripts/ensure-fgrove-cli` if `fgrove` is missing. Commands are listed in the [rhythm template](references/funnel-rhythm-template.md#reading-a-reference-rhythm-with-the-cli).

References supply rhythm, screen jobs, composition and paywall structure. Their claims, ratings, prices and testimonials describe the recorded product only, and their screen classification is not FunnelsGrove step metadata. If the CLI is unavailable, use the IDs and descriptions recorded in the references and state that images were not inspected.

## Workflow for a new or redesigned funnel

Keep each stage as a clearly titled artifact in the conversation or the project's planning document (for example `PLAN.md` or `COPY.md`). Record which version of Pre-work and Emotional Arc the user approved so later work can reuse them without repeating the interview.

### 1. Understand the product

Read the product brief, `PRODUCT_SENSE.md`, existing funnel, entry creative, offer and proof. Establish what the product does, its mechanism, who it serves, the advertised promise, pricing/access and limitations. Research before asking; ask only for missing facts that change the strategy, in one compact round. Include the high-value proof assets energy screens need: store rating, number of users, awards, expert backing, method name, catalogue size, real testimonials.

**Done when:** a concise brief separates facts from assumptions and lists audience, entry promise, offer and available proof.

### 2. Scan reference funnels

Pick 1–2 recorded funnels from the same or an adjacent category (`fgrove references categories`, `fgrove references list --category …`). Print each one's rhythm strip with the Fstack checkout's `scripts/reference-strip <funnel-id>` (`Q E Q Q E … L P @ $`, with energy share and longest question run), read the screens, and note which energy archetypes appear where, the closing order and the paywall structure. Open the images of screens you expect to borrow from. Add a candidate paywall reference (`fgrove references list --step-type paywall`) whose price model fits the offer.

**Done when:** a short reference scan (strips, notable energy screens with funnel ID and position, candidate paywall) is ready to inform the arc.

### 3. Prepare Pre-work and obtain approval

Follow [Pre-work](references/funnel-psychology-framework.md#pre-work): foundation, five-column table (problems, why current solutions fail, barriers, values, higher-level values), primary anchor, transformation and entry promise, **energy inventory** (which proof assets exist and which are open), and **2–3 planned Hitchcock moments** (input → what we reveal → what the visitor concludes).

Present **Pre-work** as a reviewable artifact and ask the user to approve it or request changes. **Stop here until the user explicitly approves this Pre-work. Do not draft the Emotional Arc, screen sequence, headlines or CTAs while approval is pending.**

**Done when:** the Pre-work checks pass and the user approves the presented strategy.

### 4. Build the Emotional Arc on the rhythm template and obtain approval

From the approved Pre-work, lay the journey on the [rhythm template](references/funnel-rhythm-template.md) and return the [Emotional Arc](references/funnel-psychology-framework.md#emotional-arc):

- one **feeling journey** line;
- the **rhythm strip**, checked against the [cadence rules](references/funnel-rhythm-template.md#cadence-rules): screen 1 asks, first energy screen by screen 3, at most 3 questions in a row early (4 later), energy share 30–45%, varied archetypes, closing `M → L → P → @ → $`;
- the **screen map**: screen and archetype, job and Pre-work link, before → after, what earns it, fuel mark, reference (funnel ID and position), answer use → next;
- a short **fuel and effort check**, the closing order, the chosen [paywall blueprint](references/paywall-blueprints.md) with its reference screen, material branches and open decisions.

Assign every energy screen an archetype from the [catalog](references/energy-screens.md) that fits its trigger, and every question a named use. Recommend a screen budget if none was supplied. Labels stay structural; finished headlines, question wording and CTAs belong to step 5.

Present the **Emotional Arc** and ask the user to approve it or request changes. **Stop here until the user explicitly approves this Emotional Arc.**

**Done when:** the cadence rules pass (or each deviation has a written reason), and the user approves the journey.

### 5. Write the screen copy

Use the approved arc's IDs and the framework's [screen-copy specification](references/funnel-psychology-framework.md#screen-copy): headline, body, choices, CTA, evidence/visual, personalisation, fuel and transition for every screen.

- **Questions:** one clear thing, 2–6 distinct options, icons/images where the reference uses them; the answer's use stays visible in the next screens.
- **Energy screens:** follow the archetype's copy and visual formula in the [catalog](references/energy-screens.md); open by reflecting the preceding answer; make the dominant visual carry the proof (number, chart, product, their own answers).
- **Mirror, loading, plan reveal, email:** follow the [closing sequence](references/funnel-rhythm-template.md#closing-sequence) formulas; the plan uses the visitor's real answers with an illustrative label.
- **Paywall:** follow the [clone procedure](references/paywall-blueprints.md#clone-procedure): take the reference paywall's section list exactly, write copy for every section, and keep billing, renewal, trial and cancellation terms readable before the CTA. Read [offer practices](references/funnel-best-practices.md#offers-checkout-and-access) before drafting terms.
- **Hitchcock pass:** replace every bare claim ("best", "amazing", "proven") with the evidence or the visitor's own data. Mark missing proof as `[PROOF: …]` and unconfirmed offer facts as `[OFFER: …]`; never invent numbers, ratings or testimonials.

### 6. Self-test before presenting

Required before showing copy to the user:

1. **Per-screen rubric:** run the [review checks](references/funnel-psychology-framework.md#review-checks) (value, fuel, scan, attention, Hitchcock, answer link, commitment, trust, truth) and fix every failure.
2. **Journey checks:** re-read the final rhythm strip against the cadence rules, the promise chain from ad to paywall, the Hitchcock moments and paywall section parity with its reference.
3. **Rendered check:** render the copy with [preview-funnel](../preview-funnel/SKILL.md) and inspect every screen at the small first-view size from the [visual pass](../qa-funnel/references/checklist.md#visual-pass) (`375x548`): headline within three lines, single-choice options and the CTA visible without scrolling, energy screens showing their evidence block or labelled visual, paywall sections in reference order. Fix copy that does not fit and re-check.

**Done when:** every screen passes or has a named open slot, and the result is returned with the full screen copy, the final rhythm strip, a compact self-test table (screen → failures fixed → remaining open slots), the preview URL when it is running, links to the approved Pre-work and Emotional Arc, and useful experiments.

### 7. Hand off within the requested scope

For a copy-review clickthrough, use [preview-funnel](../preview-funnel/SKILL.md). For full visual design, use [design-funnel](../design-funnel/SKILL.md) with the existing `Design.md`, the approved Pre-work and Emotional Arc (including each screen's reference and the paywall reference) and the complete copy. When implementation is requested, use `create-funnel` or `edit-funnel`, then `qa-funnel`. Strategy or copy approval is not permission to publish.

## Continuing, revising, or reviewing existing work

- Reuse explicitly approved Pre-work and Emotional Arc when they still match the product, audience, promise, offer and requested scope. State which approval you rely on; an existing file or silence alone is not approval.
- For a local wording correction that preserves the strategy, offer, sequence and emotional progression, inspect the affected screen and its neighbours, apply the relevant practices and the per-screen rubric, and return the scoped revision.
- A change to the strategic focus, audience, promise, mechanism or offer reopens Pre-work approval and then arc approval for the affected scope. A change to the sequence, cadence or emotional progression reopens arc approval before rewriting the affected screens.
- For a rhythm review of an existing funnel, write its current strip, compare it with the cadence rules and the reference scan, and propose concrete insertions (which energy archetype after which question) or merges.
- A review-only request can return findings and recommendations directly. Apply the workflow above when moving from findings into rewritten copy.

Copy research owns messaging and observed structure only. The synced project's `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` own step metadata, answer persistence, routing, analytics, payments and helpers; these managed docs decide how each screen is implemented. Follow their exact step-type and contract pages when translating copy into code.
