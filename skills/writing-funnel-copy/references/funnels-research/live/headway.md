# Headway (Self-improvement) — Live Funnel Walkthrough

> Walked: 2026-06-15 (capture date from repo history).

> NOTE: Funnel was only partially walkable. The quiz route (`/self-growth/quiz`)
> consistently returned a hard error screen ("This quiz is tougher than we
> thought / We've run into a little problem here. Please try again.") on every
> attempt across multiple age branches and a re-navigation. This is a backend or
> geo/region block from the current environment, not a clickable interstitial.
> I captured the entry screen and the first social-proof interstitial; the quiz
> body and paywall were NOT reachable. Per the skip-after-retry rule, I stopped
> after the documented retries.

## Overview
- **URL:** https://onboarding.makeheadway.com (operator: GTHW App Limited, Limassol, Cyprus)
- **Entry promise:** "Become the most interesting person in the room" — books/big-ideas summary app positioned as social/self-growth status, not "reading."
- **Personalizes on:** Age first (18-24 / 25-34 / 35-44 / 45+); presumably goals/interests deeper in (not reached).
- **Step count:** Advertised "3-MINUTE QUIZ." Full step count not observable due to block.
- **Paywall reached?** No — blocked at quiz step.

## Flow Walkthrough
1. **Entry / Age gate** — single-question screen.
   - Headline: "Become the most interesting person in the room"
   - Sub-label: "3-MINUTE QUIZ" (time-cost expectation set up front — caps perceived effort).
   - Options: 4 illustrated cards — "Age: 18-24", "Age: 25-34", "Age: 35-44", "Age: 45+". Each card is a distinct illustrated persona (student w/ grad cap, young man w/ coffee, woman w/ glasses + chat bubbles, older man in beanie).
   - Lever: Investment escalation — first interaction is effortless (one tap), near-100% answerable. Personas let the user self-identify ("that's me"), priming relevance.
   - Branch notes: Age routes the persona/content; all branches funnel to `/self-growth/social-proof` next.
2. **Social-proof interstitial** (give-screen, zero effort) — appears immediately AFTER the first answer, before any more questions.
   - Hero stat: "40+ million people" / "already use the Headway app"
   - Testimonial card: quote "Headway is a bite-sized learning app for those who strive to grow" — attributed to *Daily Mail*.
   - "MENTIONED IN" press-logo wall: Yahoo News, Forbes, MakeUseOf, TechCrunch, Entrepreneur, Hackernoon.
   - CTA: "Continue"
   - Lever: Trust Gate resolved early (threat + hierarchy) via user-count social proof + press credibility, placed in screen 2 exactly where the framework says trust must resolve (screens 1-3). Refuels before asking more questions.
3. **Quiz body** — NOT REACHED (error).

## Paywall Architecture
NOT REACHED — quiz route blocked. Cannot document pricing/tiers/anchors/trial/timer/Apple Pay/downsell from live walkthrough.

## Standout Techniques
- **Status reframe in the headline:** Sells the *social outcome* ("most interesting person in the room"), not the mechanism (book summaries). Maps benefit to a higher-level value (status/being interesting) rather than the feature (reading).
- **Time-boxed promise up front:** "3-MINUTE QUIZ" label caps the perceived ability cost before the user commits any fuel.
- **Trust injected at screen 2, not the paywall:** Social proof (40M users) + press logos sit immediately after the very first micro-commitment, front-loading the Trust Gate while fuel is still full.
- **Persona-card age gate:** Illustrated archetypes make the easiest-possible first question also do identity priming.

## Notable Copy & Microcopy
- "Become the most interesting person in the room"
- "3-MINUTE QUIZ"
- "40+ million people already use the Headway app"
- "Headway is a bite-sized learning app for those who strive to grow" — Daily Mail
- "MENTIONED IN"

## Weaknesses / Risks
- **Funnel reliability:** The quiz step hard-errored on every attempt from this environment. If this reproduces for real users in some regions, it kills conversion at step 3 — the single worst place to lose a user who just gave a micro-commitment and saw social proof.
- The error screen copy ("This quiz is tougher than we thought") is friendly but offers no real recovery path other than a "Try again" that loops back into the same failure.
