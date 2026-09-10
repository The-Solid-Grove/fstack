---
id: funnel-research
title: Funnel Research Prompt
summary: Structured research stage that enriches PRODUCT_SENSE.md before plan generation.
version: 2.1.0
intents:
  - research
  - plan
---
Goal: enrich `PRODUCT_SENSE.md` with research and strategy before plan generation or funnel code edits.

Process:
1. Consolidate product context from latest user intent and current `PRODUCT_SENSE.md`.
2. Run competitor research across iOS/Android/Web.
3. Apply the onboarding framework prompt to synthesize onboarding psychology and step strategy.
4. Write/update `PRODUCT_SENSE.md`.

`PRODUCT_SENSE.md` must include dedicated sections for:
- Product context summary and target audience.
- Competitor set (5-10 across iOS/Android/Web) with source URLs.
- Competitor breakdown (offer angle, pricing/trial, funnel/paywall pattern, copy/tone).
- Messaging map (ad promise vs onboarding copy vs paywall framing).
- Objection map and mitigation patterns.
- Differentiation strategy and positioning recommendations.
- Onboarding strategy synthesis from framework outputs:
  - value stack
  - entry mental state
  - transformation narrative
  - barrier handling strategy
  - paywall timing rationale
- Mascot profile seed (name/reference/style constraints) when provided.

Behavior rules:
- If user changes product/audience/value proposition/positioning, update `PRODUCT_SENSE.md` in the same run.
- Do not write funnel implementation files under `src/` in this stage.
- Do not write `PLAN.md` in this stage unless explicitly asked; planning is a separate stage.
