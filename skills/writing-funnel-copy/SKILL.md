---
name: writing-funnel-copy
description: Use when writing or revising quiz-to-paywall funnel copy, positioning, questions, result screens, and subscription offers, including product research, screen strategy, and scoped copy reviews.
---

# Writing Funnel Copy

Turn the product, audience, and ad promise into a coherent purchase journey. For a new or substantially redesigned funnel, use the full workflow. For a single-screen edit or review, inspect the relevant context and return the requested revision or findings.

## FunnelsGrove Contract Gate

For every implementation-facing task:

1. **MUST** read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` before choosing step metadata or changing code.
2. **MUST** derive step classification, answers, routing, analytics, and helpers only from those managed docs; **NEVER** copy them from research teardowns.
3. **MUST** run `fgrove validate` after the change and resolve every blocking diagnostic before preview, sync, or publish.

These gates remain mandatory when tests and builds pass, the change looks small, a deadline is urgent, or someone asks to skip them.

## References by task

- Research, positioning, or `PRODUCT_SENSE.md`: [funnel research](references/funnel-research.md).
- New funnel narrative and screen-by-screen spec: [psychology framework](references/funnel-psychology-framework.md).
- Pricing, checkout, trial, upsell, or renewal copy: [paywall guidance](references/funnel-paywall-best-practices.md) and [benchmark/compliance rules](references/funnel-benchmarks-and-compliance.md).
- Conversion diagnosis and A/B ideas: [conversion experiments](references/funnel-conversion-best-practices.md).
- Encouragement, social proof, mechanism or other value screens; opening mockups dominated by questions: [local energy-screen references](references/energy-screens/index.md). Inspect the images and adapt a pattern to the current doubt and client identity.
- Design and functional testing of a built funnel: `qa-funnel`.
- Acquisition, economics, analytics, and the full course: `web2app-essentials` (Web-to-Web Essentials).

## Workflow

1. Establish product, audience, ad promise, and requested scope from available context. Ask only for missing facts that change the work. For a new flow, establish the screen budget or recommend it.
2. Load the relevant references above. Research before drafting when positioning or evidence is missing; update product sense if the product or audience changed.
3. For a new flow, create the framework's five-column pre-work table, transformation, and screen map. For a scoped change, use the affected screen and its adjacent promise/transition.
4. Write concrete headline, body, choices, CTA, visual direction, and intended personalization. Claims, testimonials, metrics, and guarantees must have sources; label assumptions and unfilled proof slots.
5. Check promise continuity, useful questions, truthful results, and clear pricing/renewal terms. Return the framework's full deliverable for new flows, or the requested revision/findings for scoped work.
6. When visualization is requested, use `preview-funnel` for a temporary local mockup. When implementation is requested, use `create-funnel` or `edit-funnel`, then `qa-funnel` to test the built result.

Copy research owns messaging and observed structure only. The synced project's `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` own step metadata, answer persistence, routing, analytics, payments, and helpers. Follow their exact step-type and contract pages when translating copy into code.
