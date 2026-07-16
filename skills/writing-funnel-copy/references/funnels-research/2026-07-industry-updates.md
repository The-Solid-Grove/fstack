# Industry Updates — July 2026 Web Research

Web-research snapshot of funnel-industry publications, collected 2026-07-16.
Unlike the live walkthroughs and code teardowns in this folder, these are
**reported** numbers and patterns, not verified first-hand — treat as leads to
validate, not as evidence-grade findings.

## Benchmarks (Funnelfox, 311-funnel analysis + 2026 pattern review)

- Typical web2app funnel: **~3% conversion from session start to purchase**,
  with **~13% of sessions reaching the paywall**. Most conversion loss happens
  inside onboarding, not on the paywall.
- Experiment-type LTV uplift ranking: **localization first (~62.3%)**, then
  pricing/plan structure, then copy, visual design last.
- Post-purchase web-to-app download conversion: **90–95%**.
- Email retargeting: **5–10% revenue uplift** (up to ~20% for market leaders).
- Market context: 63% YoY growth in funnels launched (2024 vs 2023), Meta
  reports ~50% YoY growth in web-to-app spend, TikTok share rising (some apps
  now outspend Meta there).

## Pattern shifts vs. our existing findings

Mostly confirms `00-LIVE-FINDINGS.md`; deltas worth noting:

- **Intro discount replaced the free trial as default.** 50–70% off the first
  billing period rolling into full price, on a three-option paywall. Free web
  trials add friction and hand off poorly to in-app trials; paid-only web
  funnels with layered discounts are the recommended default.
- **Onboarding got longer, not shorter: 20–60 screens.** Length is framed as a
  commitment mechanism. Fatigue is managed by rotating question formats and
  inserting micro-rewards (education cards, social proof, affirmations,
  "building your plan" screens) between question blocks — not by cutting steps.
- **Choose-your-trial-price** (Nebula: €1/€5/€9/€13.67) doubles as a
  willingness-to-pay filter, with the €1 tier reused as the exit-intent
  fallback offer.
- **Post-purchase upsell stacking** is normal at the top end — Noom runs 6
  upsells + 2 upgrade options across ~25 post-purchase screens.
- **Trust blocks cluster at the paywall** (guarantee, badges, billing terms,
  FAQ inline) rather than being spread through the funnel.

## Competitor capability: RevenueCat web-funnel experiments

RevenueCat shipped (2026-04) an **Experiment step type** in its web funnel
editor: visitors are assigned to up to **4 variants**, each routing down a
different funnel path, with per-variant conversion tracked in the funnel
editor and an experiments list. Relevant as a baseline for FunnelsGrove's
experiment UX.

## Sources

- [How top apps do web2app in 2026: funnel patterns](https://blog.funnelfox.com/web2app-funnel-patterns-2026/)
- [Web funnels trends: 311 analyzed funnels](https://blog.funnelfox.com/web-funnels-insights-and-trends/)
- [Strategic guide to A/B testing web-to-app funnels](https://blog.funnelfox.com/ab-testing-web-to-app-funnels-guide/)
- [RevenueCat changelog: A/B tests within web funnels](https://www.revenuecat.com/changelog/release/run-ab-tests-within-web-funnels-2026-04-01)
