# IQ Brain (IQ Test) — Live Funnel Walkthrough

> Walked: 2026-06-15 (capture date from repo history).

## Overview
- **URL:** https://iqbrainpro.com → `/start/iq` → `/test/iq` → `/email/<sessionId>` → `/checkout/<sessionId>`.
- **Entry promise:** "Discover Your Accurate IQ score in 3 minutes — Test your cognitive abilities and more! Compare your results with friends and family..." Homepage shows live counters ("32,149 IQ Tests Conducted This Month", "106 Average IQ Score") and a sample certificate ("Total Score: 150").
- **Personalizes on:** essentially nothing demographic — it's a pure performance test. The whole funnel personalizes on your (withheld) test score and the implied percentile. No age/goal questions; the "answers" themselves are the personalization input.
- **Step count:** Test = **20 questions** (Raven's-matrices-style visual pattern puzzles, "growing difficulty"), then a ~5-second calculating loader, an email gate, then the paywall. ~23 screens.
- **Paywall reached?** YES — the locked-IQ-score paywall captured in full, with exact pricing.

## Flow Walkthrough (ordered)
1. **Landing** — "Discover Your Accurate IQ score in 3 minutes". Floating avatars + a sample question bubble + live test/score counters. CTA "START NOW". (No cookie banner.) Page also pre-loads the sales narrative: official certificate via email, "Trusted by 130,000+", category tiles (Career, Finance, Mental Health, IQ & EQ, ADHD, Personality Disorders...), and "AVERAGE IQ BY COUNTRY" table.
2. **Test intro** (`/start/iq`) — "Get ready to start the IQ test! / Take our scientifically-backed IQ test and unlock insights about yourself." Three cards: **20 questions (with growing difficulty) / Select the answer (choose the right one) / Take your time (in a quiet environment).** Trust row: "Science-backed · Private & Secure · 100M+ Users". CTA "Start Certified Test". Footer: "Our test is based on the latest psychological studies, and gives very similar results compared to standardized IQ tests."
3. **Test, Q1-20** (`/test/iq`) — each screen: a visual matrix with a "?" cell + 6 numbered answer tiles, a **count-UP timer** (00:01→), and a progress bar. Selecting an answer auto-advances. Pattern types seen: diagonal lines, tapered bars, dot grids, nested shapes (triangle/circle/square/hexagon matrices), wave fields, geometry-with-markers. On Q20, selecting an answer reveals a confirm: **"Get my results — Do you want to confirm your answers? You will not be able to edit them after validation."**
4. **Anti-gaming guardrail** *(notable)* — On a first run where I answered every question with the same option, the result was **rejected**: "Result of IQ Test — Your IQ is not within the current range of our test. You can try again carefully, and we will make a more accurate assessment." → forced retry. Only after giving *varied* answers did the funnel proceed to a score/paywall. (The funnel refuses to monetize obviously-random input.)
5. **Calculating loader** — "Calculating your IQ score... — Hang tight while our AI brain analyses your answers against the 5 key measures of intelligence..." with sequentially-checking items: **Memory → Speed → Reaction → Concentration → Logic.** Progress bar to 100% (~5s). (Effort-justification + manufactured rigor.)
6. **Email gate** (`/email/...`) — "Where should we send your **report**?" over a "Full IQ Brain Report" document mockup. Email field + required consent: "I agree to receive result information about my IQ test. Your data will be processed in accordance with our Privacy policy." (Entered funnel.research@example.com — no password/account.) → routes straight to `/checkout`.
7. **PAYWALL / locked score** (`/checkout/...`).

## Paywall Architecture
**The core mechanic (vertical-defining):** the score is computed but *withheld*. The user is shown a teasing RANGE and a percentile, with the exact number replaced by a "?", and must pay to reveal it.

- **Hero:** `"Your IQ score in 100-120 and report is Ready!"` — gives a 20-point RANGE, never the number.
- **Locked-score block:** large circular gauge with a **"?"** where the score should be; left label "Your IQ Results"; right label **"Higher than 80% of people"**; a "CERTIFIED IQ TEST" ribbon badge.
- **Blurred results table:** Cognitive Skill rows — Visual Perception / Abstract Reasoning / Pattern Recognition / Spatial Orientation / Analytical Thinking — each with **"???"** values and greyed ranking labels (Intelligent / Above Average / Average / Below Average / Low). All redacted until purchase. CTA "Get Your Full Report".
- **Exact pricing (rendered USD variant):**
  | Line | Today | Anchor |
  |---|---|---|
  | **Total today** | **$1.98** (−90%) | — |
  | IQ Score + Report | $1.98 | ~~$19.80~~ |
  | 7-days Trial to Premium Toolkit | $0 | ~~$7.2~~ |
  | **Afterwards** | **$28.80 / month** (recurring) | — |
  - *(A second localized variant surfaced in the page DOM with EUR-style figures: total €19.8 (−51%), report €39.8→€19.8, toolkit €9.7→€0, "afterwards €38.8/month" — see Weaknesses re: price inconsistency.)*
- **Anchors:** struck-through "regular" prices on every line; the trial-to-toolkit shown as a free add-on ($7.2 → $0).
- **Per-day reframe:** not used; instead a tiny "today" price ($1.98) hides the real $28.80/mo recurring cost.
- **Trial terms (explicit, small grey text):** "You are enrolling in a monthly subscription to iqbrainpro.com service. You agree to be billed [$28.80/$38.8] per month until you cancel. Payments will be charged from the card you specified above. To cancel, write to support@iqbrainpro.com or in your profile settings." → the $1.98 is a trip-wire that rolls into a full-price monthly sub.
- **Social proof:** animated odometer "Over **1,394,131** certificates ordered"; "Full statistical analysis... against the **3,000,000** who've already taken the test... how you stack up against professional peers and celebrities"; a live "Latest results" feed (USA IQ 121 / Belgium 106 / Estonia 91 / UK 82 / Canada 83 / Argentina 125, each "X minutes ago"); greyed press logos (Yahoo, The Globe and Mail, Barchart, Benzinga).
- **Guarantee:** "GUARANTEED SAFE CHECKOUT" badge row (AES-256bit, McAfee Secure, Norton, "Powered by Stripe"). No explicit money-back guarantee text (unlike Coursiv).
- **Urgency / timer:** **LIVE** sticky banner "We Guarantee Discount Until 10:00" counting down (observed 10:00 → 09:23). Frames the discount as a held reservation.
- **Apple/Google Pay:** **NOT present.** Checkout is card-based via Stripe — payment icons are PayPal, Visa, Mastercard, Amex, Discover (plus security seals). No Apple Pay / Google Pay buttons.
- **"What will you get?" value grid (below offer):** Your exact IQ score (bell-curve graphic with "?") · Full performance analysis (vs 3M, peers & celebrities) · Printable IQ certificate (sample: "CERTIFICATE — James — Your score 134") · Tailored brain-training program (mobile app mockup: Concentration/Memory/Reasoning games — "Science, that feels like games").
- **CTA:** "Order now" (offer block) + "Get Your Full Report" (results block) + sticky implied. Requires "I agree to the T&Cs and Privacy policy" checkbox.
- **Checkout-close downsell:** not tested (would require entering card flow / exit-intent; no payment performed).

## Standout Techniques (vertical-unique to IQ tests)
- **Withheld-score reveal as the entire purchase trigger.** Unlike fitness ("here's your plan") or income ("here's your roadmap"), the IQ funnel makes you *do real cognitive work* (20 timed puzzles), computes a result, then **hides the one number you came for behind the paywall** — replaced by a "?" and a tantalizing range ("100-120") + percentile ("higher than 80%"). The sunk-cost from the test + curiosity gap is the conversion engine. This is the purest Hitchcock/curiosity-gap monetization of the three verticals.
- **Anti-random guardrail** that rejects garbage answers ("not within the current range") — both protects the "scientific" framing and forces re-engagement (more sunk cost).
- **Credential/status framing.** "CERTIFIED IQ TEST", printable certificate, "use our OFFICIAL certificate on your resume", comparison to "celebrities" — sells social status, not self-improvement.
- **Test-as-product disguised as test-as-service.** The 5-metric loader (Memory/Speed/Reaction/Concentration/Logic) and "AI brain analyses" manufacture scientific authority for what is a pattern quiz.
- **Trip-wire pricing** ($1.98 today) far more aggressive than Coursiv's intro pricing — the headline price is ~6% of the real monthly cost.

## Notable Copy & Microcopy
- "Discover Your Accurate IQ score in 3 minutes"
- "Your IQ score in 100-120 and report is Ready!" (range, never the number)
- "Higher than 80% of people"
- "Hang tight while our AI brain analyses your answers against the 5 key measures of intelligence..."
- "Your IQ is not within the current range of our test. You can try again carefully..." (anti-gaming)
- "Evidence-based personalized training to boost IQ up to 37% in 4 weeks"
- "how you stack up against professional peers and celebrities"
- "Science, that feels like games"

## Weaknesses / Risks
- **Hard trip-wire subscription.** $1.98 (or €19.8) "today" silently converting to **$28.80–$38.8/month** is the single biggest chargeback/complaint risk; disclosure is in small grey text only.
- **Price inconsistency across page regions** — the rendered offer showed USD $1.98 today / $28.80/mo, while the page DOM/footer simultaneously contained EUR-flavored figures (€19.8 today, €38.8/mo) and a "$28.80/month" footer. Mixed/contradictory pricing within one page erodes trust and may be a localization bug.
- **Scientific-validity overclaim.** "scientifically-backed", "100M+ Users", "boost IQ up to 37% in 4 weeks", celebrity comparison — claims that invite skepticism and potential regulatory scrutiny; IQ is not meaningfully trainable +37%.
- **Manufactured-proof signals.** Live "Latest results" feed, odometer "1,394,131 certificates", and faded press logos read as synthetic; the per-session resetting timer is clearly fake urgency.
- **No money-back guarantee** stated, unlike best practice for a paid-result product — increases perceived risk at the exact moment of payment.
- **Score withheld entirely** (not even a fuzzy number) can feel like a bait-and-switch after the user invested 3+ minutes — high rage-quit risk for users who object on principle.
- **No Apple/Google Pay** raises checkout friction on mobile vs. competitors.
