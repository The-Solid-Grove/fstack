---
name: web2app-essentials
description: Use when answering questions about web2app or quiz-to-paywall web funnel benchmarks, conversion rates, unit economics, paid acquisition, creatives, onboarding design, paywalls, pricing, payments, funnel analytics, growth process, or subscription compliance, or when learning how web2app funnels work end to end.
---

# Web2App Essentials

## Overview

A knowledge base for web2app and quiz-to-paywall web funnels, distilled from a
practitioner course (2024). Use it to answer concrete questions (benchmarks,
uplift figures, pricing patterns, compliance rules) and to teach the full
web2app model end to end. The corpus lives beside this file under
`references/`, one folder per module, indexed by `references/README.md`.

This skill is educational reference only. It never drives implementation: for
funnel code or copy changes use `edit-funnel`, `create-funnel`, or
`writing-funnel-copy`, which route through the project's managed contract
docs.

## Answering questions

1. Identify the topic and load only the matching module file(s) from the
   routing table below. Read `references/README.md` first only when the topic
   is unclear.
2. Answer with the concrete numbers, tables, and checklists from the
   reference — quote benchmarks as ranges, exactly as written.
3. Always carry the corpus caveats: benchmarks vary widely between products;
   judge changes by CAC and ROAS (CR × LTV), not proxy metrics; uplift figures
   are course-observed, not guarantees.
4. If the corpus does not cover the question, say so rather than
   extrapolating; the references note where source material was lost
   (slide-image tables, garbled transcripts).

## Routing table

| Question is about | Read |
|---|---|
| What web2app is, funnel models, why web vs app store, unit economics, drop-off benchmarks, optimization order | `references/1-intro-to-web-funnels/1.1-introduction-to-web-funnels.md` |
| Funnel anatomy, build vs buy, platform capability checklist | `references/1-intro-to-web-funnels/1.2-funnel-structure-and-tools.md` |
| Examples of top live funnels and their patterns | `references/1-intro-to-web-funnels/1.3-top-funnel-examples.md` |
| CAC/LTV math, Meta/TikTok/Google buying, targeting, scaling playbooks | `references/2-paid-acquisition/2.1-media-buying.md` |
| Creative production process, creative metrics, idea sourcing, spy tools | `references/2-paid-acquisition/2.2-performance-creatives.md` |
| Onboarding/quiz structure, storytelling, loaders, email capture, paywall composition, post-purchase app handoff | `references/3-onboarding-and-experiments/3.1-onboarding.md` |
| Post-launch debugging, where to look for growth, funnel A/B testing rules | `references/3-onboarding-and-experiments/3.2-onboarding-experiments.md` |
| Pricing, plans, intro offers, trials, upsells, paywall experiments | `references/4-payments-and-monetization/4.1-monetization-and-paywalls.md` |
| PSP vs MoR, checkout design, declines/retries, disputes, payment mechanics | `references/4-payments-and-monetization/4.2-payments-in-web-funnels.md` |
| Event taxonomy, dashboards, UTM/attribution, marketing analytics | `references/5-web-funnel-analytics/5.1-web-funnel-analytics.md` |
| Revenue/financial model structure for a funnel | `references/5-web-funnel-analytics/5.2-revenue-model-template.md` |
| Growth team, planning rituals, experiment pipeline, ICE/RICE, A/B statistics | `references/6-growth-team-and-process/6.1-growth-process.md` |
| Hypothesis docs and experiment-tracking templates | `references/6-growth-team-and-process/6.2-hypothesis-and-process-templates.md` |
| Chargebacks, monitoring programs, taxes, transactional emails, data consent | `references/7-risks-and-compliance/7.1-compliance-and-risks.md` |
| Paywall disclosure rules, FTC/ROSCA/California subscription law | `references/7-risks-and-compliance/7.2-legal-compliance-summary.md` |

## Learning path

When asked to teach web2app in general (onboarding a teammate, "explain how
this works", study plan), walk the modules in course order 1 → 7: what a
funnel is and its economics, how traffic is bought, how the onboarding sells,
how the paywall and payments monetize, how it is measured, how a team iterates
on it, and what keeps it legal. Summarize each module from its reference files
and go deeper where the learner asks.

## Quick benchmark card

Keep answers anchored to these headline numbers (details and caveats in the
module files):

- Drop-off: 100% land → 35–60% mid-onboarding → 10–20% paywall → 8–15%
  checkout → 0.5–5% purchase.
- Paywall-to-purchase: 10–15%. Post-purchase app install: 80–90%.
- Intro offers: 50–70% off first cycle. Upsell take rate: 20–30%.
- Apple Pay: 60–80% of payments. Email sequences: up to 30% of revenue.
