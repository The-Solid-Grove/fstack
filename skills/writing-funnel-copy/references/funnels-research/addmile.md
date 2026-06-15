# Addmile Funnel — Research Notes

## 1. Overview

**Vertical:** Self-help / wellbeing / life-coaching subscription app ("Wellbeing Self-Coaching Program"). Adjacent to the Noom/mental-fitness category, but framed around *life direction, motivation, and emotional state* rather than weight or fitness. Brand: **AddMile**, operated by **GTHW App Limited** (Limassol, Cyprus) — a classic EU-incorporated quiz-to-sub publisher.

**Product (from `PRODUCT_SENSE.md`):** A guided self-coaching funnel that "diagnoses habits, motivation, and emotional state, then presents a tailored plan." Free quiz + insights upfront; monetized by a long-form subscription paywall.

**Target audience:** "Adults feeling stuck, low energy, distracted, or unmotivated." Mobile-first (viewport locked to 390×780 in `funnel.config.ts`).

**Entry promise (Step 1 headline):** *"Navigate Life Challenges And Shape Your Future"* + *"Take a 2-minute quiz to uncover the best Self-Coaching Program tailored to you."* The whole funnel is built to honor that "2-minute quiz → personalized program" promise.

**Architecture:** 19 steps, **strictly linear**. `funnel.sequence.ts` lists `step-1 … step-19`; `funnel.routing.ts` wires each step to the next with a plain `{ type: 'route', to: 'step-N+1' }` rule. No conditional edges, no live experiments (`legacyFunnelExperiments = []`). The routing engine *supports* graph edges, per-answer conditions, and A/B experiments, but this funnel uses none of them. Answers are captured as attributes (`setAttribute`) purely for analytics/personalization, never for branching.

**Step types** (from `funnel.steps.ts`): 8 `single_step_choice`, 6 `progress_interstitial`, 1 `multi_select_choice`, 1 `form_input` (email), 1 `paywall_offer`. The funnel correctly alternates ask-screens and give-screens (see §6).

**Transformation arc:** Before — stuck, drained, distracted, procrastinating, unmotivated. After — "Become Who You Meant To Be," in control, reignited passion, improved wellbeing within week 1.

---

## 2. Step-by-Step Walkthrough

> Source files: `src/steps/step-01.tsx` … `step-19.tsx`. All steps render inside the `AddmileHeader` (logo + back arrow + step label + progress bar) except the landing (compact header) and the two result/paywall screens.

### Step 1 — `step-1` · `single_step_choice` · Landing + Age gate
- **Headline:** "Navigate Life Challenges / And Shape Your Future" (rendered in brand blue `#1009ff`).
- **Sub:** "Take a **2-minute quiz** to uncover the best **Self-Coaching Program** tailored to you."
- **Prompt:** "Select your age"
- **Options:** `18-29 / 30-45 / 46-60 / 60+` → `setAttribute('ageRange')`.
- **Value loaded:** Expectation match with the ad; effortless first commitment.
- **Lever:** Investment escalation — start with the *easiest possible* tap (age), near-100% answer rate. No progress bar shown yet (compact header) so the journey feels unstarted/short. Legal footer present for trust gate (company name, T&C/Privacy).

### Step 2 — `step-2` · `single_step_choice` · Gender
- **Headline:** "How do you identify yourself?"
- **Options:** 🧔🏻 Male / 👩🏼 Female → `gender`.
- **Progress label:** "1 of 22", bar at **5%**.
- **Lever:** Second trivial micro-commitment; emoji adds System-1 warmth. Note the "of 22" denominator is a deliberate over-count (only 19 steps exist) — see §6/§8.

### Step 3 — `step-3` · `single_step_choice` · Lifestyle satisfaction
- **Headline:** "Are you satisfied with your current lifestyle?"
- **Options:** ✅ Yes / 🤔 Not Sure / 🚫 No (icon-only buttons with labels beneath) → `lifestyleSatisfaction`.
- **Label:** "2 of 22", **9%**.
- **Lever:** Problem activation. Most of the targeted audience answers "Not Sure" or "No," priming dissatisfaction the product will later resolve. Pure visual/emoji answer = low cognitive load.

### Step 4 — `step-4` · `single_step_choice` · Energy / drain frequency
- **Headline:** "How often do you feel drained or low on energy?"
- **Options:** 😫 Often / 😕 Sometimes / 😎 Never → `lowEnergyFrequency`.
- **Label:** "3 of 22", **14%**.
- **Lever:** Pain amplification; the emotive emoji faces let the user self-diagnose a problem.

### Step 5 — `step-5` · `progress_interstitial` (used as a question) · Distraction scale
- **Headline:** "How often do you find yourself getting distracted?"
- **Input:** 1–5 numeric scale, foot labels "Never … Always" → `distractionLevel`.
- **Label:** "4 of 22", **18%**.
- **Lever:** Another self-rated pain point; quantified scale primes a later "score/level" payoff (the Step 18 wellbeing-level chart).

### Step 6 — `step-6` · `progress_interstitial` (true give-screen) · Strategy reframe
- **Art:** 🔭 hero emoji.
- **Copy:** "This quiz isn't just a test — it's your **first step toward a clear strategy.** Discover what's holding you back and learn how to tackle life's challenges with confidence."
- **CTA:** Continue → `strategyIntroSeen`. No progress label (give-screens hide the counter).
- **Lever:** Fuel refill after 4 ask-screens. Reframes the quiz as already-valuable, and seeds "what's holding you back" (the blocker concept that resurfaces on the paywall as "Main blocker: Fear of failure").

### Step 7 — `step-7` · `progress_interstitial` (Likert question) · Procrastination agreement
- **Headline (quoted statement):** *"I tend to put off tasks, duties, or activities"*
- **Sub:** "Do you agree with this statement"
- **Input:** 5-emoji Likert 👎👎🤷👍👍 → `procrastinationAgreement` (1–5).
- **Label:** "5 of 22", **23%**.
- **Lever:** Self-labeling. Agreeing with a negative self-statement deepens problem ownership (consistency bias makes the later solution feel necent).

### Step 8 — `step-8` · `progress_interstitial` · Social proof
- **Headline:** "**800 000+ people** / Have chosen AddMile" (purple).
- **Visual:** Collage of 9 lettered avatar dots (A, M, R, D, N, L, S, J, K).
- **Sub:** "We've helped thousands of people to tackle their life challenges."
- **CTA:** Continue → `socialProofSeen`. No progress label.
- **Lever:** Early social proof / herd validation placed *before* skepticism peaks (matches the case-study advice "place social proof before skepticism peaks"). Also a fuel refill.

### Step 9 — `step-9` · `single_step_choice` · Stress-handling style
- **Headline:** "How do you usually handle stress and challenges?"
- **Options (5):** 🧘 stay calm / 💬 talk to someone / 💪 push through / 😵 "I get it, but it's hard to follow" / 😖 avoid it → `stressHandlingStyle`.
- **Label jumps to "10 of 22", 45%** (a big visible leap from "5 of 22" — progress acceleration trick, see §6).
- **Lever:** Personality/coping profiling; the 5-way self-identification increases the feeling of a tailored diagnosis.

### Step 10 — `step-10` · `progress_interstitial` · Transformation + authority
- **Art:** 🗺️🏆.
- **Headline:** "Transform Your Life — The Right Way!"
- **Copy:** "Our **Wellbeing Self-Coaching Program**, backed by **300+ certified coaches and experts**, uses proven techniques to help you tackle life's challenges — quickly and sustainably."
- **CTA:** Continue → `transformationIntroSeen`.
- **Lever:** Authority proof (300+ certified coaches) + solution mechanism introduction. First explicit naming of the product as the vehicle.

### Step 11 — `step-11` · `single_step_choice` · Motivation recency
- **Headline:** "When was the last time you felt motivated?"
- **Options (5):** I am right now / Few weeks ago / Less than a year ago / More than a year ago / Never, I think → `motivationRecency`.
- **Label:** "17 of 22", **77%** (another large jump).
- **Lever:** Nostalgia/loss framing — most users recall a *lapsed* motivated self, intensifying the gap the product closes.

### Step 12 — `step-12` · `multi_select_choice` · Current feelings
- **Headline:** "What's the dominant feelings that you're having right now?" · Sub: "Choose all that apply"
- **Chips (8):** Calm, Stressed, Confused, Motivated, Tired, Anxious, Hopeful, Overwhelmed → `dominantFeelings` (array). CTA disabled until ≥1 selected.
- **Label:** "18 of 22", **82%**.
- **Lever:** Emotional inventory; the multi-select raises investment and feeds the personalization on the next screen.

### Step 13 — `step-13` · `single_step_choice` (re-uses multi-select UI) · Feelings confirmation
- **Identical question/chips to Step 12.** Seeds the selection from `dominantFeelings` (fallback `['Confused','Hopeful']`), lets the user adjust, sets `dominantFeelingsConfirmed`.
- **Label:** still "18 of 22", **82%** (deliberately not advanced — a "confirm what you just said" beat).
- **Lever:** Commitment reinforcement; making the user re-affirm their emotional state hardens the self-diagnosis before the plan reveal. (Mechanically near-duplicate of Step 12 — flagged in §8.)

### Step 14 — `step-14` · `progress_interstitial` · Planning stat + near-finish push
- **Art:** 🧩.
- **Copy:** "Studies show that **72% of people who invest in proactive personal growth experience better life satisfaction.** A clear plan increases your chances of success." + "You're almost there — just a few final touches to tailor your program. Stay focused… transform your life with confidence! 🚀"
- **CTA:** Continue → `planningReminderSeen`.
- **Lever:** Statistic-as-priming (72%) + "almost there" momentum to push through the last ask-screens.

### Step 15 — `step-15` · `single_step_choice` · Daily time investment
- **Headline:** "How much time would you invest daily to turn things around?"
- **Options:** ✌️ 5 / 👌 10 / 🤟 20 / 💪 30 min/day → `dailyInvestmentMinutes` (number).
- **Label:** "21 of 22", **95%**.
- **Lever:** Commitment device (consistency bias) — the user *self-selects* an effort budget, pre-committing to using the product. Low minimum (5 min) lowers the "do I have time?" barrier (a known objection in PRODUCT_SENSE).

### Step 16 — `step-16` · `single_step_choice` · Readiness + success stat
- **Headline (purple):** "91% of people who followed our Program successfully improved their wellbeing."
- **Sub:** "Do you want to become one of them?"
- **Options:** 👍 "Yes, I'm fully ready!" / 🤔 "I want to, but I doubt it's possible" → `readinessLevel`.
- **Label:** "22 of 22", **100%**.
- **Lever:** Final yes-momentum framed against a 91% success stat; even the doubtful option keeps the user moving forward (both route to email capture). Loss aversion (don't be in the 9%).

### Step 17 — `step-17` · `form_input` · Email capture
- **Headline:** "Unlock Your Custom Program to Transform Your Life"
- **Sub:** "👥 Join 800K+ AddMile Users"
- **Card:** "🎁 We'll also send you a special bonus!"
- **Input:** email, validated via `/^\S+@\S+\.\S+$/`, CTA disabled until valid → `email`.
- **Note:** privacy/T&C reassurance under the field.
- **Lever:** Data capture framed as *unlocking the program* (function, not marketing) + a bonus gift incentive + social proof repeat. Placed at 100% progress so the email feels like the final unlock.

### Step 18 — `step-18` · `progress_interstitial` · Personalized insights / result
- **Headline:** "{FirstName}, It's Time To Become Who You Meant To Be" — `firstName` is parsed from the email local-part (`email.split('@')[0]`), fallback **"Maria"**.
- **Hero:** Animated SVG **growth curve** "Your Well-being Level:" rising from a red "Now" point to a green "After using AddMile" point; x-axis "Now → April" (relative future date).
- **Card bullets:** "Based on your situation and your goals · Practical, easy-to-follow · Backed by behavioral science methods."
- **CTA:** Continue → `insightsViewed`.
- **Lever:** Future-state visualization (the single highest-impact pre-paywall pattern). Self-generated value (Hitchcock) — the curve implies improvement without a hard numeric promise; the user fills in the optimism. Name personalization deepens the "this is mine" effect. No header/progress bar — this reads as a *results page*, not a quiz step.

### Step 19 — `step-19` · `paywall_offer` · Long-form paywall
See §4 for full architecture.

---

## 3. Branching, Experiments & Entry Points

- **Branching:** None. Every step routes unconditionally to the next via `legacyStepRouteRulesById` (`step-1→2→…→18→19`). The `funnel.manifest.ts` independently rebuilds the same sequential `edgesByStepId`. No per-answer divergence exists anywhere — e.g. the "I doubt it's possible" answer on Step 16 goes to the same email screen as "fully ready."
- **Experiments:** `legacyFunnelExperiments = []` and the config `graph` has no experiments, so `funnelExperiments` resolves empty. The routing layer fully supports A/B variants (`resolveNextStepFromGraph` reads `experiments` with traffic-split variants and a `control` fallback) — it's simply unused here. **Opportunity, not a feature in use.**
- **Entry points (`funnel.routing.ts` `legacyFunnelEntryPoints`):**
  - `default` → `step-1` (sourceHints: `web`, `default`) — the standard cold entry.
  - `paywall` → `step-19` (sourceHints: `paywall`, `checkout`) — a direct-to-paywall entry, e.g. for returning/retargeted users or paid-traffic that skips the quiz.
- **Conditional infra present but dormant:** `resolveNextStepFromGraph` supports `when.conditionId` edges that fire when `context.attributes[conditionId] === true`. None are defined, so all the captured attributes (`ageRange`, `gender`, `stressHandlingStyle`, `dominantFeelings`, `readinessLevel`, etc.) are currently analytics/personalization only.
- **Per-answer personalization (not branching):** Step 13 seeds from Step 12's `dominantFeelings`; Step 18 personalizes the headline from the captured `email`. These adapt *content*, not *route*.

---

## 4. Paywall Architecture

`step-19.tsx`. A long scrolling page (`addmile-screen-scroll`) with the pricing block rendered **twice** via a shared `PaywallPricingBlock` component. Default selected plan: **8-week (most popular)**.

**Sticky top bar (`60:2241`):** "This offer ends in: **09:54**" + a "Get my plan" button that smooth-scrolls to the second (repeated) pricing block (`#addmile-repeated-pricing`). Urgency persists through the whole scroll.

**Above-the-fold pricing block (`60:1426`):**
- **Personalized hero:** "**Maria Tsar**, Reach Your Full Potential" (hardcoded name — see §8).
- **Result recap row:** "Main blocker: 🫣 **Fear of failure**" | "Goal: 🖤🔥 **Reigniting passion**" — reloads the quiz's emotional framing as if computed from answers (actually hardcoded).
- **Promo card:** "🏷️ YOUR PROMO CODE APPLIED! ✓ **Mar_Feb2026**" with a `09:54` minutes:seconds countdown — the "earned/applied discount" pattern.
- **Three plans** with anchored crossed-out totals and per-day decomposition:
  | Plan | Old total | Now | Old/day | Now/day |
  |---|---|---|---|---|
  | 4-week | $47.98 | **$19.20** | $1.59 | **$0.64** |
  | 8-week *(Most popular)* | $74.98 | **$29.90** | $1.24 | **$0.50** |
  | 12-week | $95.97 | **$38.40** | $1.06 | **$0.43** |
  - Per-day price rendered as a large "$0" + small ".64 / PER DAY" pill to minimize perceived cost.
- **CTA:** "Continue" → sets `selectedPlanId` + `paywallIntent='continue'` (runtime handles checkout; the step itself does not mount Stripe).
- **Payment-logo row:** Visa, Apple Pay, PayPal, Mastercard, Amex, Discover.
- **Subscription note (compliance):** "…First 8-Week Plan are 29.90 USD, then 74.98 USD for 8-Week Plan. Cancel any time in Settings… Subscription Terms."

**Below the fold (in order):**
1. **Coaching upsell teaser (`60:1646`):** "🔥 50+% OFF on AddMile 1-on-1 video coaching — available after purchase" + coaches photo. (Pre-sells a post-purchase upsell; not a separate funnel step.)
2. **"Highlights of your plan" (`60:1658`):** 4 benefit bullets w/ icons — step-by-step plan based on triggers; proven techniques; 1-to-1 coaches; research-based content "feel better within 1st week."
3. **Social-proof block (`60:1702`):** 5 Trustpilot-style stars, "**113 543**", "4.8-star rating."
4. **Three testimonials (`60:1718`):** Ali / Lisa / David, each with avatar initial, 5 stars, dated (Feb–Jun 2025), recovery-story quotes.
5. **"Why People Love Our Plan" (`60:1831`):** Quick & easy (15 min/day) · Multiple formats · Continuous guidance ("accountability buddies").
6. **Repeated pricing block (`60:1876`)** — identical plans/promo/timer, `id="addmile-repeated-pricing"` (the scroll target). Second close after value loading.
7. **30-Day Money-Back Guarantee (`60:2096`)** with badge — risk reversal.
8. **FAQ (`60:2117`):** 10 collapsible questions (What is AddMile, How it works, Why coaching, Coaching vs therapy, Access, Privacy, Session limits, "What if I like to study on my own," Access duration, Tech support). Objection-handling that doubles as selling.
9. **Footer:** GTHW App Limited (Cyprus address), Terms/Privacy/Subscription links, Contact.

This closely follows the paywall best-practices flow: hero → pricing → benefits → social-proof numbers → testimonials → pricing (2nd) → guarantee → FAQ → company info. CTA + pricing repeated; guarantee near the close.

---

## 5. Upsell / Downsell / Cancellation Flow

- **In-funnel upsell/downsell:** None as discrete steps. The only upsell surface is the **"50+% OFF on 1-on-1 video coaching, available after purchase"** teaser embedded in the paywall (`60:1646`) — i.e. a post-purchase upsell is *promised* but not implemented as a screen in this funnel.
- **Checkout / down-sell modal:** The repo ships `StripePaymentPopup.tsx`, `StripeExpressCheckout.tsx`, `StripeCheckoutForm.tsx` (Apple/Google Pay express + card form in a modal), but **step-19 never imports or mounts them**. The paywall only sets `paywallIntent='continue'`; the host runtime is expected to open checkout. So the "checkout-close down-sell" pattern is *not* wired in this funnel.
- **Cancellation:** Handled by a standalone route, **`/manage-subscription` (`src/app/manage-subscription/page.tsx`)**, not an in-funnel cancellation-offer step. It lists active subscriptions via `apiService.getManageSubscriptions()` and lets the user **Cancel** (`cancelAtPeriodEnd`) or **Renew** via `apiService.updateSubscription({action})`. There is **no save/win-back offer, no discount intercept, no downsell** on cancel — a plain cancel button. (Notable gap vs. best practice; see §8.)

---

## 6. High-Performance Techniques Observed

1. **Frictionless first tap (age) with no progress bar** — Step 1 maximizes start-rate; the bar only appears at Step 2, so the user is already committed before they see "1 of 22."
2. **Ask/give cadence respected** — never more than ~4 consecutive ask-screens before a give/refill interstitial (Steps 6, 8, 10, 14 are pure motivation refills). Matches the fuel model.
3. **Progress acceleration / fake denominator** — labeled "of 22" though only 19 steps exist, and the numerator *leaps* ("5 of 22" → "10 of 22" → "17 of 22" → "21/22" → "22/22"). Late jumps create a "nearly done, don't quit now" sunk-cost push.
4. **Early social proof before skepticism** — 800K users at Step 8 (only ~5 questions in), then authority (300+ certified coaches) at Step 10.
5. **Stacked statistics as priming** — 72% (Step 14), 91% success (Step 16), 800K users, 113,543 reviews / 4.8 stars — numbers do the persuading instead of adjectives.
6. **Self-labeling questions** — agreeing with "I tend to put off tasks" (Step 7) and confirming feelings twice (Steps 12–13) make the user *author* their own problem, so the solution feels self-evident (consistency bias).
7. **Commitment device** — Step 15 makes the user pick a daily-minutes budget before seeing the price, pre-committing them to usage.
8. **Future-state result screen** — Step 18's rising wellbeing curve (Now → April) with name personalization is the emotional peak right before price; the curve implies a gain without a hard promise (Hitchcock self-generated value).
9. **Email framed as "Unlock"** — Step 17 collects email as the gate to the custom program + a bonus gift, not as marketing signup.
10. **Earned, pre-applied promo + dual timer** — "PROMO CODE APPLIED! Mar_Feb2026" + a sticky countdown and an in-card countdown make the discount feel personal and perishable.
11. **Double pricing block + sticky "Get my plan"** — two closes (cold + post-value) and a persistent scroll-to-checkout shortcut.
12. **Per-day price minimization** — "$0.50/day" rendered with a giant "$0" and tiny decimals; weekly totals shown as crossed-out anchors (~60% "discount").
13. **Risk reversal + objection FAQ** — 30-day money-back guarantee adjacent to the second CTA; 10-question FAQ that pre-empts the exact objections in PRODUCT_SENSE ("will this help me," "do I have time," "can I cancel," coaching-vs-therapy).
14. **Post-purchase upsell teaser on the paywall** — "50+% OFF 1-on-1 coaching after purchase" plants an AOV expansion before the first charge.

---

## 7. Notable Copy & Microcopy Tricks

- **Outcome-over-feature headlines:** "Become Who You Meant To Be," "Reach Your Full Potential," "Transform Your Life — The Right Way!" — identity/aspiration framing, ≤6 impactful words.
- **Question-as-mirror:** "When was the last time you felt motivated?" and the procrastination quote statement make users confront a felt gap.
- **Result recap as pseudo-diagnosis:** "Main blocker: Fear of failure / Goal: Reigniting passion" reads like a computed verdict (it's static) — strong personalization illusion.
- **"You're almost there — just a few final touches to tailor *your* program"** (Step 14): possessive + near-completion to reduce late drop-off.
- **Soft-doubt option that still advances:** Step 16's "I want to, but I doubt it's possible" validates hesitation without offering an exit — every path leads forward.
- **Gift hook at email:** "🎁 We'll also send you a special bonus!" — reciprocity + curiosity at the data-capture moment.
- **Per-day pill typography:** big "$0" + ".50 / PER DAY" — visual anchoring that the cost is negligible.
- **Promo code naming:** "Mar_Feb2026" looks like a real, time-bound, user-specific code (legitimizes urgency).
- **Benefit time-to-value claim:** "feel better within 1st week" and "Spend just 15 minutes a day" directly answer the time/efficacy objections.
- **Guarantee confidence framing:** "We are so confident you will achieve your goals, we offer a full refund…" — confidence transfer, not defensive hedging.

---

## 8. Weaknesses / Risks / Things to Avoid

1. **Hardcoded "Maria Tsar" / "Maria" on the paywall and Step 18 fallback.** The paywall hero literally reads "Maria Tsar, Reach Your Full Potential" regardless of the captured email/name, and Step 18 falls back to "Maria." For any non-Maria user this is a glaring personalization break that *destroys* the tailored illusion the funnel spent 18 steps building. **Highest-priority bug.**
2. **Hardcoded result recap** — "Main blocker: Fear of failure / Goal: Reigniting passion" never changes with answers, despite the funnel collecting stress style, feelings, motivation recency, etc. Wasted personalization signal and a risk if a user notices it doesn't match their inputs.
3. **Fake/inconsistent progress denominator ("of 22" with only 19 steps; jumps from 5→10→17).** Effective but deceptive; a savvy user who taps back will see the math doesn't add up. Borderline dark-pattern.
4. **Duplicate Steps 12 & 13** — near-identical "dominant feelings" multi-select. Burns fuel with an ask-screen that delivers no new value (no give-screen between two consecutive asks at 82%/82%). Candidate to merge or replace #13 with a reveal.
5. **Static "09:54" timer** — the countdown value is a literal string, not a running timer. If it never counts down (or resets on reload), the urgency is hollow and risks eroding trust / compliance exposure for false urgency.
6. **Typo in plan title:** "8-WEEK PLA" (missing "N") in `paywallPlans`. Visible copy defect on the most-popular plan.
7. **No branching / no live experiments** despite full engine support. All collected attributes (`stressHandlingStyle`, `dominantFeelings`, `motivationRecency`, `readinessLevel`, `dailyInvestmentMinutes`) are unused for routing or offer selection — large untapped personalization/AOV opportunity (e.g. recommend plan length from `dailyInvestmentMinutes`, adapt testimonial to coping style).
8. **Cancellation has no save/win-back flow.** `/manage-subscription` is a bare cancel/renew toggle — no pause, discount intercept, or downsell. Leaves retention revenue on the table vs. best practice.
9. **Checkout not wired in-funnel.** Step-19 only sets `paywallIntent`; the shipped Stripe popup/express components are unused here, so there's no in-page checkout modal and therefore no checkout-close down-sell layer.
10. **Compliance softness on stats.** "91% improved their wellbeing," "72% … better life satisfaction," "feel better within 1st week" are unsourced outcome claims in a wellbeing/mental-health-adjacent vertical — refund/ad-policy risk without cited studies; prefer ranges/eligibility language.
11. **Email/name parsing is naive** — `email.split('@')[0].split(/[._-]/)[0]` would render "john" from `john.doe@…` as the name, which can look sloppy when surfaced (and the paywall ignores it entirely in favor of "Maria").
