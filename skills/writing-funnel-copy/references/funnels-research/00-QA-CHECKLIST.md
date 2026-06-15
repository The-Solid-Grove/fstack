# New-Funnel QA Validation Checklist

Run this against every new funnel **before preview publish** and again **on the preview
URL before production**. It has two parts:

- **Part A — Conversion completeness:** does the funnel contain the elements that make
  funnels convert? (Derived from the fstack framework + the 10-funnel teardown.)
- **Part B — Defect catch-list:** the concrete bugs that actually shipped in the
  high-performing reference funnels. Every item here is a real failure observed in this
  research set — check each one explicitly.

Mark each ✅ pass / ⚠️ weak / ❌ fail. A funnel is launch-ready only when Part A has no ❌
and Part B has no ❌.

---

## PART A — Conversion Completeness

### A1. Opening (screens 1–3)
- [ ] Screen 1 matches the ad/store promise within 3 seconds (expectation match).
- [ ] First interaction is a one-tap question with ~100% agreement, not a welcome screen.
- [ ] First question has ≤5 options, short scannable labels.
- [ ] Trust gate resolved by screen 3 (visual quality, relevant personalization, early proof).
- [ ] Quiz length set expectation ("3-minute quiz") and/or progress bar deferred past screen 1.

### A2. Quiz body
- [ ] No 3 ask-screens in a row without a give-screen (validation/insight/proof) between.
- [ ] Per-answer feedback acknowledges the choice and ties it to the plan.
- [ ] At least one self-generated-value (Hitchcock) moment: user supplies input → funnel
      reflects "their" result as a range, not a claim.
- [ ] Loader screens are used for priming (rotating status copy, proof, or a micro-question),
      not blank waits.
- [ ] Problem is activated and its mechanism shown before the solution is sold.
- [ ] Social proof appears early (around Q3), before skepticism peaks.
- [ ] Investment ladder escalates (tap → answers → personal info → email).
- [ ] A commitment / pledge beat or "app does it for me vs. myself" fork is present.

### A3. Future-state projection
- [ ] A dated, personalized projection chart appears before the paywall.
- [ ] It is anchored to the user's stated goal/event/date.
- [ ] Regulated verticals (health/finance/beauty/legal) use ranges + disclaimers, no guarantees.

### A4. Email / data capture
- [ ] Email framed as functionally necessary (delivery of plan/results), placed late.
- [ ] Consequence stated ("we'll send results here").

### A5. Paywall
- [ ] Personalized result-summary hero + CTA above the fold.
- [ ] Value recap as benefit-framed feature grid (outcomes, not features).
- [ ] 2–3 pricing tiers with best-value/"Most Popular" pre-selected as anchor.
- [ ] Crossed-out original price + savings badge.
- [ ] Per-day price reframe present.
- [ ] Price block + CTA repeated at least twice.
- [ ] Proof stack: ratings, user count, before/after, one named success story, vertical authority.
- [ ] Honest urgency: sticky discount + countdown; discount feels earned (gamified reveal
      or carried-in pre-applied code).
- [ ] Money-back guarantee badge near the CTA (if true).
- [ ] FAQ answering the top 3–5 barriers (trial, cancel, "will it work," scam, refund).

### A6. Checkout
- [ ] Apple Pay / Google Pay present and **above** the card fields.
- [ ] Checkout opens as an in-page modal (payment intent pre-created), not a full navigation.
- [ ] Checkout-close downsell: a deeper limited offer on dismiss, user kept on paywall.

### A7. Post-purchase & retention
- [ ] "Subscription started" confirmation screen.
- [ ] Post-purchase upsell positioned as the natural fit for the user's result.
- [ ] Web→app handoff (deep link + QR) if applicable.
- [ ] Cancellation flow offers a save (pause/discount/downgrade) before hard cancel.

### A8. Copy & attention (spot-check 5 screens)
- [ ] Headlines ≤6 words, scannable in 1 second.
- [ ] Body ≤2–3 sentences; stats/icons instead of text walls.
- [ ] The largest visual element carries the value message; value-carrier is animated.
- [ ] Every screen passes the 3-second test (a glance absorbs the value point).
- [ ] Ranges not exact promises; expert tone, no "buy now" energy.

---

## PART B — Defect Catch-List (real bugs from the reference funnels)

### B1. Personalization integrity ⚠️ most common failure
- [ ] **No hard-coded name/profile that contradicts user input.** Blesse shipped a paywall
      cover "for MARI" ignoring the entered name; Addmile hard-codes "Maria/Maria Tsar";
      Keiki shows "Girl/3-4" regardless of answers; BetterMe hard-codes name/event/weight.
      → If you can't branch for real, keep reflected copy generic enough to always be true.
- [ ] Captured answers that the UI claims drive results actually do (or the result copy is
      safely generic). Verify the "your plan/result" screen reflects at least one real input.
- [ ] Event/goal pills on the projection/paywall reflect the user's actual selection.
- [ ] Number/locale formatting is correct (Monivate's "$50.000" read as $50.00 not $50,000;
      verify currency matches geo — BetterMe shipped Georgian lari with no geo logic).

### B2. Urgency & discount integrity
- [ ] **Countdown timer is live and actually counts down** (Headway, Promova, 12min, Addmile,
      Monivate all shipped static/cosmetic timers stuck at a fixed time).
- [ ] Promo code shown as "applied" actually applies through Stripe/checkout.
- [ ] Discount/offer is real and consistent from reveal → paywall → checkout.

### B3. Payment & checkout
- [ ] Apple/Google Pay is a **real functional button**, not a decorative logo (Headway's was
      a static image; several funnels lacked wallet pay entirely).
- [ ] Checkout completes a real test payment on the preview URL.
- [ ] Reopening checkout shows the larger/downsell discount path correctly.
- [ ] Pricing tier IDs are unique and map to distinct plans (Keiki had duplicate plan IDs for
      the 3- and 6-month tiers).
- [ ] Plan selector actually changes the selected plan (12min forced `annual` regardless of tap).

### B4. Routing & dead code
- [ ] No orphaned/legacy steps from a template still shipping or route-accessible (Headway
      shipped leftover ClaimBee `step-32/34/35` scaffold; ClaimBee shipped two unreachable
      legacy iPhone steps still in the manifest; Keiki had unwired upsell/cancellation files).
- [ ] The live paywall is the one actually wired into the sequence (verify the active route,
      not a leftover scaffold file).
- [ ] If experiments/branching are configured, they are actually wired (not empty
      `funnelExperiments` / `choiceTargetsByStepId` while the UI implies branching).
- [ ] All entry-point deep links (e.g. `?ep=paywall`, `offer`) resolve to a valid step.

### B5. Progress bar honesty
- [ ] Progress denominator is not wildly dishonest vs. real screen count (Keiki showed x/24
      over 15 screens; Blesse showed a 17-step bar over ~5 quiz screens; Addmile "of 22" over
      19). Mild inflation is a known tactic — gross mismatch erodes trust and looks broken.
- [ ] Progress never visibly jumps backward or exceeds 100%.

### B6. Forms & data
- [ ] **No dummy/dev data pre-filled in production inputs** (Monivate and Promova shipped
      `tsarmari@solidgrove.ai` / `tsarmari@solidgrove.ai` pre-filled in the email field).
- [ ] Email input has validation; rejects malformed addresses.
- [ ] Marketing-consent checkbox is not silently pre-checked if that violates policy
      (Promova shipped a pre-checked opt-in).

### B7. Content & polish
- [ ] No placeholder/typo copy ("8-WEEK PLA" in Addmile; stub FAQ answers in 12min/Promova).
- [ ] FAQ rows actually expand/answer (several funnels shipped non-functional FAQ accordions).
- [ ] No duplicate steps (Addmile had duplicate steps 12/13).
- [ ] Compliance language present where required (no guaranteed health/finance/legal outcomes).

### B8. Full functional QA (on preview URL, per fstack edit-funnel)
- [ ] Email submit works end to end.
- [ ] Test payment (or approved equivalent) completes.
- [ ] Reopen checkout → verify the larger-discount/downsell path.
- [ ] `/manage-subscription` cancellation works (and offers a save).

---

## Scoring

| Verdict | Criteria |
| --- | --- |
| **Ship** | Part A: no ❌, ≤2 ⚠️. Part B: zero ❌. |
| **Fix first** | Any ❌ in either part, or a B1/B2/B3 ⚠️ (personalization/urgency/payment bugs hurt trust and revenue most). |
| **Rework** | Missing a whole Part A section (e.g., no future-state projection, no downsell, no cancellation save). |

The single highest-ROI gaps to check first, because the reference set missed them most:
**(1)** hard-coded personalization that contradicts input, **(2)** dead/cosmetic timers,
**(3)** missing checkout-close downsell, **(4)** missing cancellation save offer,
**(5)** no functional wallet pay.

---

## PART C — Live-funnel addendum (from walking ~24 real funnels; see `00-LIVE-FINDINGS.md`)

### C1. Pricing & rollover transparency (compliance-critical)
- [ ] **Rollover price is disclosed clearly, not just in fine print.** Every live sub
      funnel charges a low first term that auto-renews much higher (e.g. €15.19 →
      €38.95/mo; $1.98 → $28.80/mo). The discounted intro and the recurring rate must
      both be visible before payment. This is the top legal exposure — verify it.
- [ ] Per-day headline number matches the actual tier math (price ÷ days).
- [ ] Crossed-out anchor is a real reference price, not invented.
- [ ] "Most Popular"/"Best value" pre-selection points to the intended margin tier.

### C2. Downsell & urgency (now known to be standard)
- [ ] **A checkout-close downsell exists and fires** (deeper discount or scratch-card).
      This is industry-standard live — its absence is a real revenue gap, not an edge case.
- [ ] If using an evergreen/reset timer (industry norm), confirm it's deliberate and not
      claiming a hard deadline you don't honor.

### C3. Payment options
- [ ] At minimum **one-tap PayPal** is present (the de-facto floor in the wild).
- [ ] Apple/Google Pay present where the audience/device supports it (upside, +CR).
- [ ] For ecommerce/physical-product funnels: shipping-address step works, subscribe-vs-
      one-time is clear, and any "secret gift"/bonus actually appears in the order.

### C4. Gating & platform fit
- [ ] Biometric/photo gates (palm/selfie) have a fallback or are truly necessary — they're
      a major drop-off point and block some users entirely.
- [ ] No account+password wall *before* the paywall unless intentional (it kills
      web-funnel conversion; observed blocking Imprint, Heartify, Geozilla).
- [ ] **Web-vs-app paywall is a deliberate choice** for the vertical (policy-sensitive or
      retention-heavy verticals may belong in-app; most self-improvement belongs on web).
- [ ] Funnel actually loads from a clean URL and an ad-style UTM/click-id URL (some init
      only fires with ad params; observed funnels hung on bare URLs).

### C5. "Withhold-the-result" funnels (if applicable)
- [ ] If you lock a computed result behind payment (IQ score, location, match), there is a
      believable teaser/range AND an anti-gaming guardrail protecting result credibility.
