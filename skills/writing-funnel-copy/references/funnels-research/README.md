# Funnel Research

Step-by-step teardowns of 10 real high-performing quiz-to-paywall funnels from the
`funnelsgrove/funnels/rag-catalog/` set, analyzed through the fstack conversion framework
(`fstack/skills/writing-funnel-copy/references/`). Goal: extract what makes funnels convert
so we can validate and build the highest-performing funnels possible.

## Start here (synthesis)

- **[00-MUST-DO-TRICKS.md](00-MUST-DO-TRICKS.md)** — the playbook: 49 must-do tricks +
  the impact-pattern table + cross-funnel meta-lessons + live-funnel addendum. Read this
  to build a funnel.
- **[00-QA-CHECKLIST.md](00-QA-CHECKLIST.md)** — pass/fail validation list. Part A =
  conversion completeness; Part B = real bugs from the code teardowns; Part C = live-funnel
  addendum (pricing/rollover/downsell/payment/gating). Run before preview publish and again
  on the preview URL before production.
- **[00-STEP-DESIGN-QA.md](00-STEP-DESIGN-QA.md)** — per-step design/content QA: step
  anatomy, fuel/copy checks, imagery/faces, CTA color-contrast rules, typography sizing,
  step-type overlays, and refuted CRO myths. Every rule evidence-tagged ([V] verified /
  [P] practitioner / [S] standard / [F] framework / [✗] refuted). Run on every screen;
  complements the funnel-level checklist above.
- **[00-LIVE-FINDINGS.md](00-LIVE-FINDINGS.md)** — what ~24 real funnels from `funnels.xlsx`
  actually do: real prices, evergreen timers, first-term→rollover, exit downsells,
  withhold-the-result paywalls, payment reality, gating, and per-vertical levers.
- **[00-MASTER-FUNNEL-LIST.md](00-MASTER-FUNNEL-LIST.md)** — the full index of 313 funnels
  from `funnels.xlsx` (Webfunnels.club curated set), grouped by 26 verticals.

## External research

- **[campaignswell-scaling-web-funnels.md](campaignswell-scaling-web-funnels.md)** —
  Campaignswell guide "Inside web funnels that scaled up to $1.8M spend/mo": 7 scaling
  principles, 6 money-losing mistakes, pre-scale health checklist, and 5 case studies
  (Dialogue AI, Talaboos, GlamAI, N1x, NVAPPS). Covers the layer around our teardowns —
  creatives↔funnel narrative continuity, LTV-based scaling, web-payment ops, per-channel
  funnel adaptation.
- **[web2app-2026-trends.md](web2app-2026-trends.md)** — July 2026 external snapshot:
  Funnelfox 2026 benchmarks (~3% session→purchase, ~13% reach paywall, ~6% paywall CVR,
  localization as top LTV lever), RevenueCat's 2026 web-to-app guide (paid trials over
  free, single annual plan on web, promise↔app alignment, payment-failure reality), and
  Stripe wallet-button rules that feed the edit-funnel Wallet Checkout Lock.

## Copy swipe files

- **[copy/](copy/)** — verbatim step-by-step on-screen copy per funnel (swipe file for
  writing new copy / A/B variants). 10 code-extracted (exact) + 1 consolidated live-observed.

## Two research layers

1. **Code teardowns** (`*.md` in this folder) — 10 funnels from `funnelsgrove/funnels/
   rag-catalog/` read at the source level (every step, route, experiment, paywall file).
2. **Live walkthroughs** (`live/*.md`) — ~24 funnels from `funnels.xlsx` driven in a real
   browser through to the paywall (real pricing/offers, ~20 verticals).

## Per-funnel teardowns

Each has: overview · step-by-step walkthrough · branching/experiments · paywall
architecture · upsell/downsell/cancellation · high-performance techniques · copy tricks ·
weaknesses.

| Funnel | Vertical | Quality | Standout lever |
| --- | --- | --- | --- |
| [headway-funnel](headway-funnel.md) | Self-growth / book summaries | 0.95 | Expectation-match bookending; disciplined ask/give fuel cadence |
| [astroline](astroline.md) | Astrology | — | Self-generated value (birth chart + palm scan); accuracy-gauge progress |
| [betterme-chair-yoga](betterme-chair-yoga.md) | Fitness (older audience) | — | Poke→soothe on pain; date+event-anchored body projection |
| [promova](promova.md) | Language learning | — | Objection-pre-handling screens; loader-as-social-proof |
| [12min](12min.md) | Micro-learning / book summaries | — | Time-as-hero anchoring; annual-default per-month pricing |
| [keiki](keiki.md) | Kids' early learning (parent buyer) | — | Buyer/user emotional split; mascot ally; guilt poke→soothe→empower |
| [claimbee-funnel](claimbee-funnel.md) | Money/claims finder | — | **Best real branching**; Hitchcock payouts; abandon-discount ladder |
| [blesse](blesse.md) | Faith / personalized prayer book | — | Endowment (name+recolor own book); vertical authority proof |
| [addmile](addmile.md) | Well-being / habits | — | Cold-open age gate; self-authored problem ownership |
| [monivate](monivate.md) | Personal finance / investing | — | Twin Hitchcock anchors; rigged knowledge-deficit bars |

## Top cross-funnel takeaways

1. **The spine is universal:** hook → ask/give quiz → problem mechanism → dated
   future-state → commitment/email → paywall (value recap + anchored price + proof +
   earned urgency + guarantee) → wallet-pay checkout → downsell → upsell → handoff →
   cancellation-with-save.
2. **Self-generated value (Hitchcock) is the strongest lever** — let users supply inputs
   and conclude the value themselves; show ranges, never promises.
3. **Personalization is usually theatrical** (linear routing, hard-coded results). That
   converts only while reflected copy stays generically true — it becomes a *bug* the
   moment hard-coded text contradicts the user's input. Real branching (ClaimBee) is the
   competitive edge.
4. **Paywalls are over-invested; post-paywall is under-invested.** Checkout-close
   downsell and cancellation save-offers were the most common gaps = cheapest wins.
5. **The biggest defect classes:** contradictory hard-coded personalization, cosmetic
   (dead) timers, decorative non-functional wallet pay, dummy emails pre-filled in prod,
   dishonest progress denominators, and orphaned template scaffold steps still shipping.
