# Promova Funnel — Research Notes

> Source: `funnels/rag-catalog/promova/`. All step UI lives in a single brand file `src/steps/promova.tsx`; the `step-NN.tsx` files are thin re-exports. Routing config: `src/config/funnel.routing.ts`, `funnel.sequence.ts`, `funnel.steps.ts`. Quality score in `rag.meta.json`: 0.94.

## 1. Overview

- **Vertical:** Language learning (English speaking). AI-tutor + personalized study plan, mobile-web → app subscription.
- **Entry promise (Screen 1):** *"Speak English like a native!"* — matches the ad's fluency hook within the first 3 seconds.
- **Shape:** 17 quiz/value screens → email capture → long-form paywall → subscription handoff (deep-link to app). 19 runtime steps total.
- **Viewport:** 390×844 (portrait phone only). Designed mobile-native.
- **Transformation arc:** anxious/insecure learner ("I worry about mistakes", "tests stress me out") → confident, seen, on a credible 3-month progress path (Beginner → Pre-Intermediate).
- **Progress framing trick:** The header counter reads **`current/28`** (`STEP_TOTAL = 28`) while the real sequence is only ~18 screens, and the per-screen `current` values are non-contiguous (2, 8, 15, 17, 20, 25, 27…). This **understates how far along you are** so the bar always feels like it's moving fast and there's "barely any left." Header label is a fixed motivational string: *"Maximize your potential."*
- **Pre-work mapping (from `PRODUCT_SENSE.md`):** Known objections explicitly addressed — no time to study (→ "15 min/day", study-time question), fear of mistakes (→ Step 5 reframe), "other apps teach words not speaking" (→ Step 8 AI differentiator), trust (→ guarantees, secure-payment, 19M/79M scale proof).

## 2. Step-by-Step Walkthrough

Fuel legend: (+) refill / (−) spend / (=) neutral-priming.

### step-1 — Intro question (`single_step_choice`, node 63:8409)
- **Headline:** *"Speak English like a native!"* / sub: *"Have you studied English before?"*
- **Options:** `Yes` (green check img) / `No` (red cross img), each with chevron.
- **Captured:** `promovaStudiedEnglishBefore = yes|no`.
- **Lever:** Expectation match + near-100%-yes first micro-commitment (investment escalation: zero-effort binary tap). Legal footer already present (trust gate, screen 1). Lavender background (brand signal).
- **Branching:** None — both answers → step-2. (Answer stored but never used to route.)

### step-2 — Age (`single_step_choice`, node 63:8450)
- **Headline:** *"What's your age?"* / *"Age helps us personalize your learning"*
- **Options:** `18-29 / 30-39 / 40-49 / 50+` with couple thumbnails.
- **Captured:** `promovaAgeRange`.
- **Lever:** "We personalize" justifies the ask (data framed as for-the-user, not marketing). Progress header first appears here. **No branching** despite age being a classic segmentation axis.

### step-3 — Welcome promise (`value_prop_story`, 63:8495)
- **Headline:** *"Yay, glad you're here!"* / **Body:** *"Practice only 15 minutes a day and speak like a native in 30 days!"*
- **Visual:** happy couple hero. CTA `Continue`.
- **Lever:** Fuel refill after two asks. Two anchors planted: low effort (**15 min/day**) + fast result (**30 days**). Validation ("glad you're here").

### step-4 — Confidence stats (`social_proof`, 63:8587)
- **Headline:** *"Thanks for sharing!"* / *"Based on your goal, we're crafting a personalized plan to help you reach it faster."*
- **Visual:** `stats-card.png` outcome stat image. CTA `Continue`.
- **Lever:** Commitment/consistency ("thanks for sharing" rewards the answer) + the word **"crafting … plan"** implies work is already happening for them (sunk-cost priming). (=)

### step-5 — Fear of mistakes (`single_step_choice`, 63:8601)
- **Headline:** *"Do you worry about making mistakes in English?"*
- **Tip card (poke→soothe):** *"Mistakes mean progress!"* + *"Feeling unsure is normal, but overcoming doubts helps you learn faster. Your plan will boost your confidence along the way."*
- **Interaction:** 5-emoji confidence scale `👎 🤏 😐 👍 👍` — **pre-selected at index 2** (neutral). CTA `Continue`.
- **Captured:** `promovaMistakeReaction` (the emoji).
- **Lever:** Surfaces the #1 emotional objection then immediately relieves it (Poke→Soothe→Empower). Pre-selected answer = lower friction, and "your plan will boost your confidence" pre-sells the product as the cure.

### step-6 — Before/after (`value_prop_story`, 63:8666)
- **Headline:** *"Let us help you succeed!"* / **Body:** *"93% of users say Promova helped them reach their goals."*
- **Visual:** `before-after.png`. CTA `Continue`.
- **Lever:** Stat-backed social proof + transformation visualization. (+)

### step-7 — Income relevance (`single_step_choice`, 63:8680)
- **Headline:** *"Does your salary or income depend on your English skills?"*
- **Options:** `Definitely, it's important! 💰` / `Not really 🚫` / `Maybe 🤔` / `It could help me earn more 📈`.
- **Captured:** `promovaIncomeImportance`.
- **Lever:** Raises the stakes / higher-level value (money, career). Even "Not really" sits beside three money-framed options, planting the idea. **No branching.**

### step-8 — AI differentiator (`value_prop_story`, 63:8726)
- **Eyebrow:** *"Boost your income"* / **Headline:** *"20x faster with AI"*
- **Body:** *"Other apps teach words. Promova helps you speak. Practice with AI and gain confidence."*
- **Visual:** `ai-boost.png` acceleration graph. CTA `Continue`.
- **Lever:** Category reframe / competitor takedown ("words vs. speak") + a hero number (**20x**) the brain anchors to. Directly answers the "other apps don't build speaking confidence" objection.

### step-9 — Test feelings (`single_step_choice`, 63:8744)
- **Headline:** *"Your feelings about taking English tests?"*
- **Options:** `Love it! 🥰` / `It's okay 👌` / `Not a fan 😕` / `Stress me out! 😵`.
- **Captured:** `promovaTestFeeling`.
- **Lever:** Pre-frames the upcoming assessment as emotionally safe; harvests anxiety so step-10 can soothe it. **No branching** (the soothing copy on step-10 is static regardless of answer — a missed personalization opportunity).

### step-10 — Quick test intro (`progress_interstitial`, 63:8790)
- **Headline:** *"No worries,"* / *"We're here to help you improve step by step."*
- **Tip card:** *"Let's start with a quick test to see where you are. You've got this!"* Visual: `quick-test.png` tablet. CTA `Continue`.
- **Lever:** Soothe + empower beat. Also the **`quiz` entry point lands here** (see §3).

### step-11 — Vocabulary test (`multi_select_choice`, 63:8808)
- **Headline:** *"How many English words do you know?"* / *"Mark the Beginner words you know well!"*
- **Interaction:** 25-word chip grid; **pre-selected defaults = `['vacancy','headache','letter']`**.
- **Captured:** `promovaKnownWords` (array).
- **Lever:** Real effort/investment screen ("ability" — only spends fuel) but feels like a fun game. The pre-seeded selections lower friction and, critically, the result is **hard-coded later** (Step 15 always shows "573 words / Beginner") regardless of what you tap — self-generated-value theater.

### step-12 — Community proof (`social_proof`, 63:8912)
- **Headline:** *"Great job on completing the test!"* / *"Your results will be ready soon. Keep going!"* then **`Join 19M+ people`** / *"Become a part of a growing global community…"*
- **Visual:** `world-map.png`. CTA `Continue`.
- **Lever:** Effort reward + bandwagon social proof (19M). "Results ready soon" creates a curiosity/open-loop pulling toward Step 15.

### step-13 — Daily study time (`single_step_choice`, 63:8926)
- **Headline:** *"How much time can you study daily?"*
- **Options:** `Casual ✌️ 5 min/day` / `Regular 👌 10 min/day` / `Serious 👊 15 min/day` / `Determined 🤘 20+ min/day` (right-label shows minutes).
- **Captured:** `promovaStudyTime` (the minutes string).
- **Lever:** Commitment device — user self-selects intensity, framing the plan as their choice. Tiered labels nudge toward "Serious/Determined." **No branching** (answer doesn't change the plan shown).

### step-14 — Topic interest (`single_step_choice`, 63:8972)
- **Headline:** *"Do topics like this interest you?"* / *"People who use this reach their goal 2x faster"*
- **Visual:** `interest-grid.png`. **Interaction:** binary `👎 / 👍`.
- **Captured:** `promovaLikesTopics = true|false`.
- **Lever:** Micro-yes + a planted **2x** stat. Even a thumbs-down routes forward identically.

### step-15 — Learning profile (`summary_confirmation`, 63:9013)
- **Headline:** *"Here's your learning profile"* / *"Based on your answers"*
- **Content (all hard-coded):** Summary "Vocabulary: 573 words"; a rail from **Beginner (Today)** → **Pre-Intermediate (in 3 months)**; skill card *"You can recognize familiar words and basic phrases…"*; 4 profile rows: Current level **Beginner**, Goals **Discover new cultures**, Focus **Reading**, Style **Listening-oriented**.
- **Lever:** The payoff for all prior effort + the **future-state projection** (the single highest-impact pattern per best-practices, +15%). Dated, ranged ("in 3 months", no guarantee) so it stays compliant. CTA `Continue`.
- **Note/risk:** Profile is static, not derived from answers — see §8.

### step-16 — Analysis loader (`progress_interstitial`, 63:9101)
- **Copy:** *"Analyzing your preferences…"* with animated **% ring** (starts 27, +9 every 180ms → 100, then auto-advances after 500ms).
- **Priming real estate:** **`19+ million people` already learning** + auto-scrolling **testimonial carousel** (Endah789, Pam, Inna Vladi — 5-star, "Verified" badges, real dates).
- **Lever:** Manufactured-effort loader (work-for-you illusion) doubling as social-proof priming. `?previewStepLock=1` freezes auto-advance for QA/screenshots.

### step-17 — Email capture (`form_input`, 63:9358)
- **Headline:** *"Enter your email to get your personal plan"*
- **Fields:** email input (regex-validated `/.+@.+\..+/`, CTA disabled until valid); marketing opt-in checkbox **pre-checked**; privacy reassurance row with lock icon (*"We respect your privacy…"*); a **gift-card teaser image** (`gift-card.png`).
- **Captured:** `promovaEmail`, `promovaMarketingOptIn`; also `setUser({email})`.
- **Lever:** Email framed as *required to receive the plan* (function, not marketing). Gift teaser dangles a reward to pull the user past the highest-friction ask. Pre-filled dummy email (`tsarmari@solidgrove.ai`) is a dev placeholder — see §8.

### paywall — Long-form offer (`paywall_offer`, 63:9395) — see §4

### subscription-started — Handoff (`subscription_handoff`)
- **Copy:** kicker *"Promova unlocked"*, *"Your learning plan is ready."* App Store + Google Play buttons, QR code (generated via api.qrserver.com against a universal link), *"Open Promova now"* deep-link.
- **Behavior:** UA-sniffs platform (`ios|android|desktop`), auto-attempts the mobile deep link after 500ms (once, sessionStorage-guarded). Reads `payment_intent` + `redirect_status` query params and fires `payment_checkout_succeeded` / `payment_checkout_returned` analytics, deduped per intent.

## 3. Branching, Experiments & Entry Points

- **Branching:** **None.** `choiceTargetsByStepId = {}` and `stepRouteRulesById` is a fully linear chain step-1→…→step-17→paywall→subscription-started. `resolveConfiguredNextStep` ignores `context`/attributes entirely. Every answer is stored via `setAnswer` but **no answer ever changes the route or the content shown** (Step 15 profile and Step 11 result are hard-coded). This is a *qualification/commitment* funnel, not a *personalization-routing* funnel.
- **Experiments:** **None.** `funnelExperiments = []` and `funnelConfig.graph.experiments = []`.
- **Entry points (`funnelEntryPoints`):**
  - `default` → `step-1` (hints: web, default, promova) — the standard top-of-funnel.
  - `quiz` → `step-10` (hints: quiz, placement-test) — skips the warm-up/motivation block and drops users straight into the vocabulary test. Used for traffic already sold on the quiz hook.
  - `paywall` → `paywall` (hints: paywall, checkout) — direct-to-offer, e.g. retargeting / returning users.
- **Back navigation:** Every quiz screen's `ProgressHeader` has a back button (`goToStep(previousStepId)`) computed from the runtime-steps array; step-1 has no back.

## 4. Paywall Architecture

Single long scroll (`PaywallStep`). Top→bottom:

1. **Sticky urgency topbar:** *"Discount expires in"* + live `MM:SS` countdown (starts at **9:53**, ticks down, floors at 0 — never resets) and a `Get my plan` button that smooth-scrolls to the pricing card. Honest-urgency pattern (#12).
2. **Hero card:** **`Speak like you've always wanted to`** + app preview image + 4 benefit bullets (Courses from experts / Personal plan / Slang, idioms, everyday phrases / Speaking practice with AI). No CTA above fold inside hero — first CTA is in the pricing card just below.
3. **Pricing card (`Save more with longer plans`):** 3 radio plans, **3-months pre-selected** (`useState('three-months')`):
   - Trial week — was $43.99 → **$8.39** ($1.19/day)
   - 1 month — was $43.99 → **$23.99** ($0.79/day)
   - 3 months — was $84.99 → **$41.99** ($0.49/day) — **`Best value`** badge.
   - Per-day pricing on every tier (makes price feel tiny). Anchoring via crossed-out `oldPrice`.
4. **Offer card:** *"Special offer • Promo code applied"* `LIMITED-SAVE-52` + the same live countdown (earned/applied-discount feeling, #8/#3 in case study).
5. **Primary CTA:** **`Start learning`** (black button) → stores `promovaSelectedPlan` → `goToStep('subscription-started')`.
6. **Guarantee line:** *"14-day money-back guarantee • Cancel anytime"* directly under CTA.
7. **Secure-payment card:** *"Your payment is secured"* + payment-methods image + legal entity (*Unlimited Promova Limited, … Limassol, Cyprus*).
8. **FAQ (`People often ask`):** 3 rows (Why do I need the app? / How do I get access? / How do I cancel?) — **decorative only, no expand handler** (static `+`).
9. **Proof / guarantee banner:** money-back image + *"Full refund if it's not for you … 14-day money-back guarantee."*
10. **`What you get`:** 5 benefit rows (Everyday words / Local culture: jokes, slang / Clear pronunciation / Speaking practice / Fast progress) — benefit-first framing.
11. **Scale proof grid:** **`79M` downloads worldwide** + **`1,190,000` 5-star reviews**.
12. **`What's inside`:** 4 content/asset cards (12 English tenses PDF, Pronunciation AI test, Phrasal verbs handbook, Speak like a CEO course) — tangible deliverables.
13. **Bottom CTA:** repeat **`Start learning`** + auto-renew/cancellation legal disclosure.
14. **Legal footer** (Terms / Privacy / Subscription / Money-Back).

Pattern adherence: CTA repeated (top scroll-button, mid, bottom), pricing shown once but reinforced by offer card, guarantee repeated near each conversion zone, future-state was shown pre-paywall (Step 15) rather than on the paywall itself. **No Apple/Google Pay button** on the paywall (best-practice #10 not implemented — checkout is handed off to subscription-started/external).

## 5. Upsell / Downsell / Cancellation Flow

- **Upsell / downsell:** **None.** No order-bump, no post-purchase upsell screen, no checkout-exit recovery modal. Paywall CTA goes straight to `subscription-started`. The only "price ladder" is the 3 plan tiers (longer = cheaper/day), which functions as a soft AOV nudge toward the 3-month plan.
- **Checkout-close down-sell (best-practice #13):** **Not present** — checkout is not an in-page modal here, so there's no close-recovery layer.
- **Cancellation:** Handled outside the funnel by `/manage-subscription` (`src/app/manage-subscription/page.tsx`) — a plain account page listing subscriptions with `Cancel` / `Renew` buttons (calls `apiService.updateSubscription`). **No retention/save-offer or cancellation-survey flow** — a cancel just sets `cancelAtPeriodEnd`. This is a clear gap versus mature subscription funnels.

## 6. High-Performance Techniques Observed

1. **Expectation-match opener** — Screen 1 headline = the ad's fluency promise; first question is a frictionless near-100%-yes binary.
2. **Ask/give rhythm** — value/story screens (3,4,6,8,10,12) interleave between question screens so no 3 asks stack without a refill. Matches the fuel model precisely.
3. **Future-state projection before price** — Step 15 dated Beginner→Pre-Intermediate-in-3-months path is the conviction centerpiece (the +15% pattern), kept compliant with ranges/no guarantee.
4. **Manufactured-effort loader doubling as social proof** — Step 16 % ring + auto-scrolling verified 5-star testimonials + "19M people."
5. **Stacked, layered social proof** — 93% success (S6), 19M community (S12), 19M+ (S16), 79M downloads + 1.19M reviews (paywall). Numbers escalate toward the offer.
6. **Commitment escalation** — easy binary → segmentation → emotional admissions (fear, test stress) → a self-selected study-intensity pledge (S13) → email. Each step raises sunk cost.
7. **Objection-pre-handling** — every known objection (time, mistakes, "apps teach words", trust) is neutralized on a dedicated screen *before* the paywall.
8. **Per-day price reframe + anchoring** — every tier shows crossed-out price and a $/day figure ($0.49/day on best value).
9. **Honest-ish urgency** — live countdown + applied promo code (`LIMITED-SAVE-52`) carried from topbar into offer card; "earned discount" feel.
10. **Pre-selected best-value plan + pre-checked opt-in + pre-seeded answers** — defaults steer the high-margin choice and reduce friction at every interaction.
11. **Progress understatement** — `/28` denominator on an ~18-screen flow keeps the bar feeling fast and "almost done."
12. **Risk reversal at the CTA** — 14-day money-back + cancel-anytime + secure-payment + named legal entity clustered around the buy button.
13. **Tangible deliverables on paywall** — "What's inside" shows concrete PDFs/courses/AI tests, not abstract features (converts "subscription" into "a stack of stuff I get").

## 7. Notable Copy & Microcopy Tricks

- **`20x faster with AI`** under eyebrow `Boost your income` — number + outcome, competitor reframe (*"Other apps teach words. Promova helps you speak."*).
- **`Mistakes mean progress!`** — reframes the core anxiety into a growth signal in 3 words (poke→soothe).
- **`Practice only 15 minutes a day and speak like a native in 30 days!`** — low effort + fast result + the entry promise restated.
- **`Maximize your potential`** — persistent header mantra, keeps the higher-level goal salient through every screen.
- **`Here's your learning profile` / "Based on your answers"** — frames hard-coded content as personalized output (Hitchcock: user concludes the plan is theirs).
- **Email as gatekeeper:** *"Enter your email to get your personal plan"* — function framing, not "subscribe to our newsletter," beside a gift teaser.
- **`Save more with longer plans`** — positions the longest commitment as the *thrifty* choice, inverting the usual "annual = expensive" intuition.
- **`Full refund if it's not for you`** — loss-framed, casual, lowers perceived risk more than formal guarantee language.
- **Study-time labels (`Casual / Regular / Serious / Determined`)** — identity labels, not just durations, nudging upward self-selection.
- **"Results will be ready soon. Keep going!"** — open loop sustaining momentum across the back half.

## 8. Weaknesses / Risks / Things to Avoid

1. **Zero answer-driven personalization.** Every `setAnswer` is dead weight for routing/content. The Step-15 profile (573 words, Beginner, "Reading", "Discover new cultures") and the Step-11 result are **hard-coded** regardless of input. If a user taps every vocab word or selects "Determined / income definitely matters," the funnel still shows the identical Beginner profile — credibility risk if a user notices, and a large untapped lift (adaptive feedback ≈ +7%, per best-practices). The S9 test-feeling answer doesn't even change S10's soothing copy.
2. **Dummy data shipped in components.** Email field defaults to `tsarmari@solidgrove.ai` and marketing opt-in defaults checked — the placeholder email is a dev artifact that must not reach production; pre-checked marketing consent is also a GDPR/consent risk for EU traffic (Cyprus entity → EU exposure).
3. **Non-functional FAQ.** The three "People often ask" rows have a static `+` and no click handler — they look interactive but don't expand. The most objection-heavy real estate ("How do I cancel?") answers nothing.
4. **Countdown integrity.** Timer starts at 9:53 and floors at 0 without resetting or gating the offer — purely cosmetic urgency. Fine as a pattern, but the discount never actually expires, so it's a soft-deceptive cue to flag in QA/compliance.
5. **No Apple/Google Pay at the point of purchase** — best-practice #10 (one-tap wallet under prices, +10–15%) is unimplemented; payment is punted to an external/handoff step, adding friction at peak intent.
6. **No retention layer.** No upsell, no downsell, no checkout-exit recovery modal, and no cancellation save-offer/survey — `/manage-subscription` just cancels. Leaves ARPU (#13, +15%) and churn-save value on the table.
7. **Entry-point/progress mismatch.** The `quiz` entry point drops users at step-10, but the progress header still computes against `STEP_TOTAL = 28` with hard-coded `current` values authored for the full flow — a quiz-entry user sees a confusing/jumpy bar.
8. **Profile claims are unsourced.** "93% of users reach their goals", "2x faster", "20x faster with AI", "573 words" — strong numeric claims with no citation; acceptable as marketing but worth a compliance/substantiation check given the EU entity.
9. **Single-file architecture.** All 18 screens live in one 1,588-line `promova.tsx`; the per-step files are re-export stubs. Fine for a template, but every edit touches the same file (merge-conflict and blast-radius risk noted in repo memory's "file-splitting refactor" TODO).
