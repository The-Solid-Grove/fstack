---
id: funnel-research-stage
title: Funnel Research Stage
summary: Product sense, competitor research, messaging strategy, and pre-plan funnel positioning.
intents:
  - research
  - plan
keywords:
  - product-sense
  - competitor
  - positioning
  - messaging
  - objections
  - onboarding strategy
  - PRODUCT_SENSE.md
---

# Funnel Research Stage

Use this reference alongside the copied source prompt at
`references/funnel-research.md` before plan generation or funnel code edits
when the task is to research a product, sharpen positioning, build
`PRODUCT_SENSE.md`, compare competitors, or prepare the strategy behind a
quiz-to-paywall funnel.

## Goal

Extend the copied `funnel-research.md` prompt with fstack-specific research
quality requirements, especially found copy and actionable recommendations.

## Process

1. Consolidate product context from the latest user intent and current
   `PRODUCT_SENSE.md`, if it exists.
2. Run competitor research across iOS, Android, and web.
3. Apply the funnel psychology framework to synthesize onboarding psychology
   and step strategy.
4. Write or update `PRODUCT_SENSE.md`.

## Required PRODUCT_SENSE.md Sections

Include dedicated sections for:

- Product context summary and target audience.
- Competitor set: 5-10 competitors across iOS, Android, and web, with source
  URLs.
- Competitor breakdown: offer angle, pricing/trial, funnel/paywall pattern,
  and copy/tone.
- Copy found: useful competitor headlines, hooks, onboarding prompts,
  paywall claims, CTAs, FAQ lines, proof blocks, and offer framing, each tied
  to its source and funnel location.
- Messaging map: ad promise vs. onboarding copy vs. paywall framing.
- Objection map and mitigation patterns.
- Differentiation strategy and positioning recommendations.
- Useful recommendations: prioritized funnel, copy, offer, proof, paywall,
  and A/B test recommendations with the research evidence behind each one.
- Onboarding strategy synthesis:
  - value stack
  - entry mental state
  - transformation narrative
  - barrier handling strategy
  - paywall timing rationale
- Mascot profile seed, when provided: name/reference/style constraints.

## Behavior Rules

- If the user changes product, audience, value proposition, or positioning,
  update `PRODUCT_SENSE.md` in the same run.
- Do not write funnel implementation files under `src/` during this stage.
- Do not write `PLAN.md` during this stage unless explicitly asked; planning is
  a separate stage.
- Do not invent competitor data, pricing, proof, ratings, claims, or source
  URLs. Use sources, label assumptions, or leave a research slot open.

## Research Quality Bar

Useful research should give the next planning or copy pass concrete strategic
inputs, not a generic market summary. Prioritize:

- What each competitor promises at entry.
- How competitors sequence onboarding questions, proof, result previews, and
  paywall timing.
- Which found copy patterns are worth adapting, and why.
- Which objections the market already handles well, and which remain exposed.
- Where the product can credibly differentiate without overclaiming.
- Which claims require proof, legal review, or softer assumption language.

## Copy Found Notes

Capture copy as research evidence, not as final copy to paste. For each useful
copy item, include:

- Source URL or app/store/page name.
- Funnel location: ad, app store, landing page, quiz screen, interstitial,
  loader, paywall, checkout, FAQ, or cancellation/downsell.
- Short excerpt or tight paraphrase.
- Role: hook, objection handling, proof, mechanism explanation, urgency,
  guarantee, price framing, identity, or CTA.
- Why it matters and how it should influence this product's funnel.

Keep excerpts short. Do not copy long competitor passages into the final funnel;
adapt the underlying pattern to the product's real proof, offer, and voice.
