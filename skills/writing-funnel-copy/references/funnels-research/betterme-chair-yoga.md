# BetterMe Chair Yoga Funnel — Research Notes

## 1. Overview

**Product:** BetterMe Chair Yoga — short, low-impact, chair-based workouts plus a "personalized wellness plan" for **women in their 40s** who want to slim down at home without a gym. (`PRODUCT_SENSE.md`, `rag.meta.json` domain tags: `chair-yoga`, `wellness`, `weight-loss`, `women-over-40`, `subscription`; quality score 0.95.)

**Entry promise:** A personalized Chair Yoga plan startable at home with minimal equipment (just a chair), realistic daily time (10–15 min), and visible progress toward a goal date.

**Shape:** 24 quiz/value steps → long-form paywall → post-checkout app handoff. Linear, mobile-portrait (390px). Sourced from a BetterMe Figma (node ids preserved in `bettermeSteps`), so this is a faithful clone of a real high-performing production funnel.

**Architecture note for QA:** Every step `step-01.tsx … step-24.tsx` plus `step-32-paywall.tsx` is a **one-line re-export** from a single brand file `src/steps/betterme.tsx` (1,901 lines). All real copy/logic lives there. `step-33-subscription-started.tsx` is the only standalone step. Step numbering is non-contiguous (jumps 24 → 32 → 33) but the runtime sequence (`funnel.sequence.ts`) maps cleanly: `step-1…step-24, paywall, subscription-started` (26 routable steps).

**Transformation arc:** Before — "I'm 40+, my back/knees hurt, I have no time, I doubt exercise can help me lose weight." After — "I have a gentle plan tuned to my body that hits my goal weight by my event date, and it's risk-free."

---

## 2. Step-by-Step Walkthrough

Answers are stored via `setAnswer(key, …)`; keys noted per step. Progress bar (5 segments) values come from `STEP_PROGRESS`. Headers alternate between `LogoHeader` (info/reveal screens) and `ProgressHeader` (question screens) — a deliberate ask/give visual rhythm.

### step-1 — Landing / intro_hero (`LandingStep`, node 62:4436)
- **Headline:** "Over 2 million women" / "in **their 40s** already tried a BetterMe"
- **Type:** Intro hero, no question. CTA: `CONTINUE`.
- **Value loaded:** Social proof + instant audience match ("women in their 40s") = expectation match with the ad on screen 1.
- **Lever:** Trust gate (ally + hierarchy) via scale claim; zero-effort first screen (investment escalation — "just look").
- **Branching:** → step-2.

### step-2 — Chair Yoga familiarity / single_step_choice (`ChairYogaQuestionStep`, 62:4485)
- **Headline:** "Have you tried Chair Yoga before?"
- **Options:** Yes / No → `bettermeChairYogaTried`. Tapping any option auto-advances (`goNext` on click).
- **Lever:** Effortless first micro-commitment (near-100% answerable). Side-art layout with a chair-yoga pose image.
- **Branching:** No per-answer divergence — both → step-3. (Answer captured but not routed on.)

### step-3 — Gentle reassurance / value_prop_story (`ChairYogaIntroStep`, 62:4560)
- **Headline:** "You'll do fantastic!"
- **Copy:** "gentle and effective fitness option for all levels"; "You only need **a chair to get in shape at home!**"
- **Lever:** GIVE screen (refill after the ask). Kills the "I'm not fit enough / no equipment" barrier. Coach thumbs-up hero image.

### step-4 — Primary goal / single_step_choice (`MainGoalStep`, 62:4611)
- **Headline:** "What's your main goal?"
- **Options:** Lose weight / Maintain weight and get fit → `bettermeMainGoal`. Auto-advance.
- **Lever:** Confirmation question; commitment toward a weight outcome. Only 2 options (low decision fatigue).

### step-5 — Weight-loss proof / value_prop_story (`SolutionInfoStep`, 62:4687)
- **Headline:** "We've got just the solution!"
- **Copy:** "For women in their 40s, Chair Yoga is an excellent option to **slim down with minimal effort.**" / "10-15 mins a day to see first changes."
- **Lever:** GIVE; anchors effort low (10–15 min) and re-states age targeting. Answers "can chair yoga actually help me lose weight?"

### step-6 — Body type / single_step_choice (`BodyTypeStep`, 62:4852)
- **Headline:** "How would you describe your build?"
- **Options (illustrated cards):** Slim / Mid-sized / Full-figured / Extended size → `bettermeBodyType`. Auto-advance.
- **Lever:** Body-type personalization via images (low cognitive cost, self-identification). Visual, not text.

### step-7 — Fitness progress message / value_prop_story (`DriveProgressStep`, 62:4961)
- **Headline:** "Drive your fitness progress with Chair Yoga"
- **Copy:** "Chair Yoga adapts to you and your goal." / "**Burn calories, shape your journey.** It's your rhythm, your rules, your transformation."
- **Lever:** GIVE; autonomy/empowerment framing tied to the just-given body type.

### step-8 — Best-shape recency / single_step_choice (`BestShapeStep`, 62:5012)
- **Headline:** "How long ago were you in the best shape of your life?"
- **Options:** Less than a year ago / 1 to 2 years ago / More than 3 years ago / Never → `bettermeBestShapeRecency`. Auto-advance.
- **Lever:** Light nostalgia/loss — surfaces the gap between past-best-self and now (poke). No soothe on this screen (relies on later reassurance).

### step-9 — Sensitive areas / multi_select_choice (`SensitiveAreasStep`, 62:5104)
- **Headline:** "Do you struggle with any of the following?" / caption "Choose all that apply"
- **Options (image cards, checkboxes):** Sensitive back / Sensitive knees / None of the above → `bettermeSensitiveAreas` (array). CTA `NEXT STEP`, **disabled until ≥1 selected**.
- **Logic:** "None" is mutually exclusive — selecting it clears others; selecting any other clears "None" (`SensitiveAreasStep` reducer).
- **Lever:** Surfaces the #1 objection (joint pain) so the next screen can resolve it. Multi-select = higher investment.

### step-10 — Joint reassurance / value_prop_story (`KneesInfoStep`, 62:5205)
- **Headline:** "We got you!"
- **Copy:** "lots of **gentle exercises that strengthen your knees.**" / "longer walks, less tension, and more day-to-day confidence!"
- **Lever:** GIVE — direct soothe of the pain just admitted in step-9 (poke → soothe pairing). Higher-level value (confidence, mobility).

### step-11 — Sleep habits / single_step_choice (`SleepStep`, 62:5256)
- **Headline:** "How much sleep do you usually get?"
- **Options:** Less than 5 hours / 5-6 hours / 7-8 hours / More than 8 hours → `bettermeSleepHours`. Auto-advance. Header title shifts to **"Almost There"**.
- **Lever:** Holistic-wellness signal (implies the plan considers more than workouts → personalization depth).

### step-12 — Diet preference / single_step_choice (`DietStep`, 62:5447, scrollable)
- **Headline:** "What type of diet do you prefer?"
- **Options:** grouped into **With Meat** (Traditional, Keto, Paleo), **Without Meat** (Vegetarian, Vegan, Keto Vegan), **With Fish** (Mediterranean, Pescatarian), **Without Allergens** (Lactose Free, Gluten Free), each with image + descriptive detail → `bettermeDietPreference`. Auto-advance. Header title "Nutrition".
- **Lever:** Implies a nutrition plan is bundled (value expansion beyond yoga). 10 options but grouped to stay scannable.

### step-13 — Height capture / form_input (`HeightStep`, 62:5640)
- **Headline:** "How tall are you?"
- **Input:** ft/cm toggle, value hard-coded **167 cm** (mock). Stores `bettermeHeightUnit`, `bettermeHeightCm=167`, `bettermeHeightConsent=true`.
- **Consent gate:** Checkbox "I consent to BetterMe processing my health onboarding data…" + Privacy Policy link. CTA `NEXT STEP` **disabled until consent checked**; inline alert "Consent required to continue" when unchecked.
- **Lever:** Data capture framed as required-for-service (GDPR/health-compliance). Investment escalation (personal metrics).
- **Entry point:** `step-13` is the **`metrics` entry point** (`funnel.routing.ts`, sourceHints `metrics`, `almost-there`) — deep-link straight into the metric-capture phase.

### step-14 — Current weight / form_input (`CurrentWeightStep`, 62:5737)
- **Headline:** "How much do you weigh?"
- **Input:** lbs/kg toggle, value **54 kg** (mock). Stores `bettermeCurrentWeightKg=54`.
- **Feedback card (success/green):** "Your BMI is 19.36, which is normal" / "Healthy starting BMI to tone up and get your dream body."
- **Lever:** Immediate adaptive feedback after an ask; validates the user ("you're already healthy"). BMI personalization.

### step-15 — Goal weight warning / form_input (`GoalWeightWarningStep`, 62:5828)
- **Headline:** "What is your goal weight?" — value **50 kg**, danger card: "**That goal may be too low for your body**" / "Increase your goal slightly to unlock a healthier, more realistic plan."
- **Logic:** CTA permanently disabled; **auto-advances after 1,200 ms** (`setTimeout`), setting `bettermeGoalWeightKg=52`. (`isPreviewLocked()` blocks the auto-advance in preview.)
- **Lever:** Health-compliance + Hitchcock — funnel "corrects" an unhealthy goal to a safe 52 kg, making the recommendation feel expert and protective rather than salesy.

### step-16 — Goal weight confirmed / summary_confirmation (`GoalWeightSuccessStep`, 62:5918)
- **Headline:** "What is your goal weight?" — value **52 kg**, neutral card: "**Get moving: lose 4% of your weight**" / "a realistic target to build momentum without extreme restrictions."
- **Logic:** CTA enabled, re-sets `bettermeGoalWeightKg=52`.
- **Lever:** Resolves the warning (poke→soothe on body image). Quantified, modest target ("4%") = believable, low-fear.

### step-17 — Age capture / form_input (`AgeStep`, 62:6010)
- **Headline:** "How old are you?" — value **43 years** (mock). Stores `bettermeAgeYears=43`.
- **Feedback card:** "We ask your age to personalize your plan" / "Your routines and pacing are tuned to your body and stage of life."
- **Lever:** Age framed as personalization input, not gatekeeping. Confirms 40s targeting numerically.

### step-18 — Wellness profile / summary_confirmation (`WellnessProfileStep`, 62:6094, scrollable)
- **Headline:** "Here's your wellness profile"
- **Content:** BMI scale widget with "You – 19.36" marker in the **NORMAL** band (gradient bar: underweight/normal/overweight/obese); success card "Healthy BMI: Good starting BMI to tone up…"; trait grid: **Body type: Mesomorph** (info tooltip), **Lifestyle: Active**, **Fitness level: Intermediate**, **Metabolism: Moderate, challenging to stay trim** + a wellness avatar image.
- **Lever:** Self-generated value peak — a "diagnostic result" assembled from their inputs makes the product feel like it deeply analyzed them. Big perceived-value deposit before the late section.

### step-19 — Upcoming event / single_step_choice (`EventStep`, 62:6256, scrollable)
- **Headline:** "Do you have an important event coming up?" / sub: "Having something to look forward to can be a great motivator for **reaching your goal**"
- **Options (image cards):** Vacation / Wedding / Holiday / Sporting event / Reunion / Birthday / Other / No events any time soon → `bettermeEventType`. Auto-advance.
- **Lever:** Manufactures a personal deadline (date-based motivation) that the prediction chart and pricing will hang on. Note: downstream copy hard-codes "Wedding" regardless of selection (see §3).

### step-20 — Event date / form_input (`EventDateStep`, 62:6392)
- **Headline:** "When is your event?" / "We will **keep this important event** in mind for your journey"
- **Input:** Date field showing **6/26/2026** (mock). Stores `bettermeEventDate='2026-06-26'`. CTA `CONTINUE` + secondary **"SKIP THIS STEP"** (`goNext` without setting date).
- **Trust microcopy:** lock icon + "Your data will be processed in accordance with our Privacy Policy."
- **Lever:** Commitment to a concrete date → fuels the projection. Skip option preserves fuel for users without an event.

### step-21 — Prediction chart / progress_interstitial (`PredictionStep`, 62:6682)
- **Headline:** "The last plan you'll ever need to get in shape"
- **Projection:** "We predict you'll be **52 kg by March 26***" with event pill "Just in time for the **Wedding**"; line chart from 54→52 kg, axis Feb 26 → Mar 26, "Goal 52 kg" label.
- **Disclaimer (health-compliance):** "*Based on the data of users who log their progress in the app. Consult your physician first. The chart is a non-customized illustration and results may vary."
- **Lever:** Future-state projection tied to their goal weight + event = the conversion-best-practice "+15%" pattern. Range/illustration framing keeps it compliant.

### step-22 — Social proof loader / progress_interstitial (`SocialProofLoaderStep`, 62:6774)
- **Content:** Animated progress ring (0→33% over ~1.8 s), then auto-advances after **2,400 ms**. "**150 million people** have chosen BetterMe"; 5-star testimonial — "I have never felt better — Rosanna M." ("When I turned 70 I realized I was losing balance and strength… within two years I have never felt better.")
- **Lever:** Loader as priming real estate; massive social-proof number + an age-relevant (70-y-o) testimonial right before the offer. Self-paced wait builds anticipation.

### step-23 — Plan ready / summary_confirmation (`PlanReadyStep`, 62:6864)
- **Headline:** "MARI, your 4-week Chair Yoga Plan is ready!" (name "MARI" hard-coded)
- **Content:** "Your Weight" before/after curve, "Now" → "After 4 weeks", axis Week 1–4. Disclaimer "This chart is for illustrative purposes only."
- **Lever:** Personalized (named) plan reveal — peak ownership. Final visualization before discount/price.

### step-24 — Scratch discount / value_prop_story (`ScratchDiscountStep`, 62:6958)
- **Headline:** "Scratch to reveal your special discount!" / "We want you to start your journey with a nice surprise"
- **Interaction:** Scratch card; on tap it reveals **"30% discount on your Chair Yoga Plan"**, then auto-advances to paywall after **900 ms**.
- **Lever:** Gamified earned-discount reveal (best-practice "+8%"). Active reveal makes the price feel won, carried into the paywall.

### paywall — paywall_offer (`PaywallStep`, 62:7110) — see §4.

### subscription-started — subscription_handoff (`StepSubscriptionStarted`, `step-33`)
- **Headline:** kicker "BetterMe unlocked" / "Your Chair Yoga plan is ready."
- **Content:** App Store + Google Play buttons, QR code (generated via `api.qrserver.com` from `NEXT_PUBLIC_FUNNEL_QR_TARGET`), "Open BetterMe now" deep link.
- **Logic:** Detects platform from UA (`resolvePlatform`); on iOS/Android auto-fires the deep link after 500 ms (once per session via `sessionStorage` guard). Reads `payment_intent` + `redirect_status` from query and fires `apiService.trackFunnelEvent` (`payment_checkout_succeeded` / `payment_checkout_returned`), deduped per payment intent.
- **Lever:** Post-purchase web→app handoff; resolves "how do I actually use this."

---

## 3. Branching, Experiments & Entry Points

**Routing is fully linear.** `funnel.routing.ts` `stepRouteRulesById` is a straight chain step-1→…→step-24→paywall→subscription-started. `choiceTargetsByStepId` is **empty `{}`** and `funnelExperiments` is **empty `[]`**. `resolveConfiguredNextStep` ignores context entirely (`void context`). So:

- **No per-answer divergence anywhere.** All single/multi-select answers are *captured* (for personalization/analytics) but never alter the path. Every `onClick` calls `goNext()`.
- **No A/B experiment variants are wired** (the variant infra exists in `FunnelExperimentConfig` types but is unused).

**Entry points (`funnelEntryPoints`):**
1. `default` → `step-1` (sourceHints: web, default, betterme, chair-yoga) — main flow.
2. `metrics` → `step-13` (sourceHints: metrics, almost-there) — skips the qualifying quiz and drops users into height/weight/age capture. Useful for warm/retargeted traffic.
3. `paywall` → `paywall` (sourceHints: paywall, checkout) — direct-to-offer deep link.

**In-funnel conditional logic (UI-level, not routing):**
- step-9: "None of the above" is mutually exclusive with the two sensitivity options.
- step-13: CTA disabled until consent checkbox is checked (hard gate).
- step-15: CTA permanently disabled; **timed auto-advance** (1.2 s) is the only exit — a forced "your goal is too low → corrected to 52 kg" beat.
- step-22 & step-24 & step-15 all respect `isPreviewLocked()` (`?previewStepLock=1`) to freeze auto-advance for QA/preview.

**Hard-coded personalization (QA risk):** Despite capturing real answers, downstream screens use fixed mock values — name "MARI"/"mari_feb26", weight 54→52 kg, BMI 19.36, age 43, event "Wedding", date 6/26/2026, "March 26" projection. The event pill says "Wedding" even if the user picked Vacation. This is a demo/clone artifact, not true dynamic personalization.

---

## 4. Paywall Architecture (`PaywallStep`, node 62:7110)

A single long scrolling page (not a multi-screen paywall), with a **sticky top bar** persisting through scroll.

**Sticky bar (always visible):** Live countdown timer starting at **09:50** (`useCountdown(593)`, loops on hit-zero) + `GET MY PLAN` button → `goNext()` to subscription-started.

**Section 1 — Before/After hero (above fold):**
- Tabs "Now" / "Your Goal"; two avatar figures with an arrow between; stats per side: "Body fat: Normal", "Chair yoga level: Advanced", 3-bar level meter. (Note: both sides currently show identical "Normal/Advanced" — a clone bug; should differ.)
- Future-state visualization as the hero (best-practice "+10-15%").

**Section 2 — Offer:**
- Title "Your Chair Yoga Plan is ready!"
- **Earned-discount block:** green banner "Your promo code is applied!", user tag "✓ **mari_feb26**", and a **second countdown** mirroring the sticky timer. Ties the step-24 scratch reveal to the price.
- **Plan list (`PAYWALL_PLANS`, currency ₾ Georgian lari):**
  | Plan | Old | Now | Per-day old → now | Badge |
  |---|---|---|---|---|
  | 1-Week Trial (chip "4-Week Plan") | ₾28.56 | **₾19.99** | ₾4.08 → ₾2.86 | — |
  | 4-Week Plan | ₾85.70 | **₾59.99** | ₾3.06 → ₾2.14 | **Most Popular** (default-selected) |
  | 12-Week Plan | ₾142.85 | **₾99.99** | ₾1.70 → ₾1.19 | — |
  - Each shows struck-through old price → new price and **per-day** anchor. Middle plan pre-selected (`useState('4-week')`).
- **CTA:** `GET MY PLAN` → goNext.
- **Recurring-billing disclosure (compliance):** "Without cancellation… BetterMe will automatically charge **₾85.70 every 4 weeks** until I cancel. Cancel online via the profile…"

**Section 3 — Social proof (repeat):** "150 million people have chosen BetterMe" + the same Rosanna M. 5-star testimonial from step-22.

**Section 4 — Risk reversal + legal:**
- **30-day money-back guarantee** card (icon): "We're even ready to return your money if you can demonstrate that you followed the plan but didn't see any results." + money-back policy link (conditional refund, not unconditional).
- Company address (BetterMe International Limited, Paphos, Cyprus) + Privacy | Terms links.

**Against the paywall best-practice checklist:** Hits hero/future-state, pricing with per-day + crossed-out anchors, social proof numbers, before/after, recurring disclosure, money-back guarantee, urgency timer, repeated CTA. **Missing vs. ideal:** no Apple Pay/Google Pay wallet button under prices, no FAQ block, single testimonial reused (no second/varied before-after set), features-as-benefits grid is absent.

---

## 5. Upsell / Downsell / Cancellation Flow

- **No upsell, no downsell, no checkout-close recovery modal, and no cancellation/win-back step exist in this funnel.** Paywall → `subscription-started` is the terminal transition.
- The recurring-billing disclaimer points users to cancel "via the profile on the website or app" — handled by `src/app/manage-subscription/page.tsx` (a generic subscription-management page), **outside the funnel sequence**, not an in-funnel save/cancellation offer.
- The conversion-best-practices checkout pop-up down-sell ("+15% ARPU") and a cancellation-offer step are **opportunities not implemented**.

---

## 6. High-Performance Techniques Observed

1. **Screen-1 expectation match + scale proof:** "Over 2 million women in their 40s" mirrors the ad's audience and resolves trust on the first glance, zero effort.
2. **Strict ask/give rhythm:** every 1–2 question screens is followed by a reassurance/value screen (step-2→3, 4→5, 6→7, 8→9→10), enforced visually by alternating `ProgressHeader` (ask) vs `LogoHeader` (give).
3. **Poke→soothe pairing on the core objection:** step-9 makes the user admit back/knee pain; step-10 ("We got you!") immediately resolves it.
4. **Adaptive, validating feedback after metric inputs:** BMI "19.36, normal," age "tuned to your stage of life" — makes the product feel observant.
5. **Health-authority "correction" beat:** step-15 rejects an unsafe goal weight and auto-corrects to 52 kg — positions the brand as a protective expert, not a seller, and is compliance-friendly.
6. **Self-generated diagnostic value:** step-18 "wellness profile" (BMI band + Mesomorph/Active/Intermediate traits) reframes captured answers as an expert analysis.
7. **Date-anchored future-state projection:** step-21 ties goal weight to the user's event ("52 kg by March 26, just in time for the Wedding") with compliant range/illustration disclaimers — the highest-leverage conversion pattern.
8. **Loader as priming:** step-22 spends dead loading time on 150M social proof + an age-matched (70-y-o) testimonial right before price.
9. **Gamified earned discount:** step-24 scratch card → 30% off, carried into the paywall as a named, pre-applied promo ("mari_feb26") with a live timer — discount feels won, not handed out.
10. **Per-day price anchoring + crossed-out prices + dual urgency timers** on the paywall; middle ("Most Popular") plan pre-selected to steer choice.
11. **Risk reversal close:** 30-day money-back guarantee placed in the final section, plus recurring-billing transparency to reduce chargeback/cancellation friction.

---

## 7. Notable Copy & Microcopy Tricks

- **Audience echo as proof:** "For women in their 40s, Chair Yoga is an excellent option…" repeats the targeting demographic verbatim across steps 1, 5, 21.
- **Effort-minimizing numbers:** "10-15 mins a day," "lose 4% of your weight," "first changes" — small, believable, low-fear quantities (ranges, not promises).
- **Empowerment verbs:** "your rhythm, your rules, your transformation" (step-7) shifts agency to the user.
- **Reassurance headlines as rewards:** "You'll do fantastic!", "We got you!", "We've got just the solution!" — each give-screen opens with praise/relief.
- **Progress label escalation:** header title moves "My Profile" → "Almost There" → "Nutrition" to signal nearing the end and sustain momentum.
- **Compliance language done well:** "results may vary," "non-customized illustration," "Consult your physician first," "for illustrative purposes only," conditional money-back ("if you can demonstrate that you followed the plan").
- **Consent framed as service-enablement:** step-13 health-data consent is positioned as required "to provide services and enhance my user experience," gated as a hard CTA blocker.
- **Earned-discount identity tag:** "mari_feb26" promo code personalizes the deal and implies it's reserved for this user.
- **Skip valve:** step-20 "SKIP THIS STEP" prevents friction for users without an event date.

---

## 8. Weaknesses / Risks / Things to Avoid

1. **Personalization is fake (clone artifact).** Captured answers (`bettermeBodyType`, `bettermeEventType`, weights, age) never feed the visuals. Name "MARI", event "Wedding", weight 54→52, BMI 19.36, age 43, and the projection date are hard-coded. In production this would feel broken/inconsistent — e.g., picking "Vacation" still shows "Wedding," and "MARI" is wrong for every real user. **QA: verify dynamic binding before shipping.**
2. **Paywall before/after stats are identical on both sides** ("Body fat: Normal / Chair yoga level: Advanced" for both "Now" and "Your Goal"), undermining the transformation message. Likely a copy bug.
3. **No A/B experiment infrastructure wired** — `funnelExperiments` empty; the typed variant system is dead until populated. No front-screen or projection variants to test the highest-leverage patterns.
4. **No payment-friction reduction at the offer:** no Apple Pay / Google Pay under the price tiers (best-practice +10-15% left on the table), no in-page checkout modal, no checkout-close down-sell.
5. **No FAQ / objection block on the paywall** — top objections (does it work for me, how does billing work, refunds) are not addressed at the point of decision.
6. **No cancellation / win-back / downsell flow** in-funnel; relies on a generic manage-subscription page.
7. **Forced auto-advance on step-15** (disabled CTA + 1.2 s timer) can feel like a glitch on slow devices or to users who wanted to set a different goal; the "correction" is unskippable.
8. **Looping countdown timers** (sticky 09:50 + promo block) reset on hit-zero rather than expiring — common but a mild honesty/credibility risk if scrutinized; ensure it matches a real, enforced offer.
9. **Currency is Georgian lari (₾)** with no locale/geo logic — pricing will be wrong for the stated US/EN-style audience unless localized at runtime.
10. **Single reused testimonial** (Rosanna M., shown on step-22 and the paywall) — repetition weakens the "varied proof" effect best practice recommends; also a 70-year-old testimonial for a 40s-targeted funnel is slightly off-audience.

---

*Sources: `src/steps/betterme.tsx` (all step components + paywall), `src/config/funnel.sequence.ts`, `src/config/funnel.routing.ts`, `src/config/funnel.steps.ts`, `src/steps/step-33-subscription-started.tsx`, `rag.meta.json`, `PRODUCT_SENSE.md`, `output/playwright/paywall-mobile.png`.*
