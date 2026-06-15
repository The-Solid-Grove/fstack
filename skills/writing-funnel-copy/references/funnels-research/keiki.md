# Keiki Funnel — Research Notes

> Source: `funnels/rag-catalog/keiki` — a kids' early-learning app (parent = buyer, child = user).
> Brand mascot: **Didi** (the purple character). Quiz frames everything around "your child."
> `rag.meta.json` qualityScore **0.94**; domain intent: "Help parents build a calm daily kids-learning routine with short lessons, visible progress, and a playful mascot-led experience."

---

## 1. Overview

**Shape:** 15-screen quiz → long-form single-page paywall → post-checkout app-handoff (deep link). Strictly linear; no in-flow branching.

**Canonical sequence** (`src/config/funnel.sequence.ts`, mirrored in `funnel.steps.ts` and `src/steps/index.ts`):
`step-1 … step-15 → paywall → subscription-started`.

**Funnel section map** (against the psychology framework's six-section model):
- **A. Hook & first commitment** — steps 1–4 (age, gender, siblings, relation). Zero-friction one-tap taps; first question is age (~100% answerable).
- **B. Value loading 1** — steps 5–9 (day profile, plan-fit reassurance, distraction stat, activities, topics). Asks interleaved with gives.
- **C. Value loading 2 + feature sell** — steps 10–13 (testimonials, congrats/plan-building, learning profile summary, 2-month forecast bars).
- **D. Commitment lock-in** — step 14 (worksheets yes/no during a "Reviewing answers 50%" loader).
- **(E. Data capture)** — NOT present as a discrete email screen in the live flow. Email is collected implicitly at Stripe checkout. (The scaffolded `step-34-upsell-form` has an email field but is unwired — see §3.)
- **F. Paywall** — `paywall` (step-32 file) then `subscription-started` (handoff).

**Transformation sold:** "My child is distractible / behind / I feel guilty about screen time and overwhelmed" → "My child is On Track / Advanced / well-behaved, and I have a calm, doable daily plan (and time for myself)." This is made explicit by the paywall hero's Now → Your goal toggle.

**Entry promise / ad match:** The first screen is a child-age picker with subtitle "To create personal learning plan" — it immediately frames the experience as building a *personalized plan for your specific child*, honoring a typical "personalized early-learning plan" ad.

**Viewport:** 390×780 mobile-first (`funnel.config.ts`). Purple brand (`#5b45cd` / `#2f22a1` / `#3d2ec0`), green CTAs (`#58b956`), pink urgency accents (`#fd2793`).

**Mascot-led trust:** Didi's head + speech bubble (`KeikiQuestionPrompt`) tops every quiz question, so each question feels like the character asking — warm, low-pressure, parent-friendly. This is the funnel's signature trust/ally device.

---

## 2. Step-by-Step Walkthrough

### step-1 — Choose your child's age (`single_step_choice`, attr `childAge`)
- **Headline:** "Choose your child's age" · **Subtitle:** "To create personal learning plan"
- **Options (4, one tap):** `0-2`, `3-4`, `5-6`, `7+`
- **Header:** logo + "Log in" + menu; **no progress bar yet** (progress starts at step 2).
- **Lever:** Expectation match + investment escalation (easiest possible first tap; near-100% answerable). Self-generated personalization promise ("personal learning plan"). No selling.
- **Note:** Selecting routes straight to step-2 (`useKeikiSingleSelect` sets attribute + `goNext`). Action bar hidden — the option cards *are* the CTA.

### step-2 — Choose the gender of your child (`single_step_choice_emoji`, attr `childGender`)
- **Options:** 👦🏻 Boy / 👧🏍 Girl (2-up grid with emoji).
- **Progress appears:** "2/24" — note total is **24** while only 15 quiz screens exist (see §8, an honest-progress risk; the bar also jumps non-linearly: 2, 3, 5, 7, 11, 18…).
- **Lever:** Continued effortless micro-commitment; emoji lowers cognitive load and adds a tiny delight beat.

### step-3 — Does your child have siblings? (`single_step_choice`, attr `hasSiblings`)
- **Options:** large ✕ (red `#F47D83`) / ✓ (green `#A7D85F`).
- **Progress:** 3/24.
- **Lever:** Binary yes/no = fastest possible commitment; color-coded glyphs need zero reading. Data feeds the profile recap later (step-12 shows "Extracurricular activities: Yes").

### step-4 — Who are you to the child? (`single_step_choice`, attr `caregiverRole`)
- **Options (list):** Parent *(Mom or Dad)*, Grandparent, Relative *(Aunt or Uncle, Sibling, Cousin)*, Specialist *(Teacher, Therapist, Nanny)*, Other.
- **Progress:** 5/24 (skips 4).
- **Lever:** Identity confirmation + segmentation. Parenthetical notes reduce "which one am I?" friction. Quietly qualifies the buyer's relationship/authority over the child.

### step-5 — What best describes your day? (`progress_interstitial`, attr `dayType`)
- **Options:** Work full-time / Work part-time / remote / Stay-at-home parent / Not working right now.
- **Progress:** 7/24.
- **Lever:** Sets up the *time-scarcity* pain that step-6 immediately soothes ("a plan that fits your life"). Poke → soothe sequencing across two screens.

### step-6 — A plan that fits your life 💛 (`value_prop_story`, give-screen, no input)
- **Copy:** "We personalize learning activities to match your schedule and daily routine - simple, realistic, and doable."
- **Image:** `hero-plan.png` (parent + child reading).
- **Lever:** **Fuel refill** after 5 ask-screens. Directly answers the busy-parent objection ("I don't have time"). Reassurance, not a feature pitch.

### step-7 — Distraction affects many kids! (`social_proof` / insight, give-screen)
- **Copy:** "Did you know that **72% of parents** face this challenge? Through interactive games designed to **stimulate cognitive skills**, Keiki helps children reduce distractions by **35%**."
- **Lever:** Problem-mechanism reveal + normalization ("many kids," "72% of parents" — you're not a bad parent). Loss-aversion seed (distraction is a problem to fix). Specific numbers do the persuading (Hitchcock: parent concludes "my kid has this too"). Light guilt, immediately normalized = poke→soothe.

### step-8 — What activities does your child like most? (`progress_interstitial`, attr `favoriteActivities`)
- **Options w/ icons & checkmarks:** 🐙 Cartoons / 🛝 Offline activities (worksheets, handcrafting) / 📘 Reading books / 🧩 Playing games.
- **Progress:** 11/24.
- **Lever:** Personalization investment; the checkmark UI signals "your plan is being built from this." Sets up the worksheets upsell at step-14.

### step-9 — Pick the topics your child likes (`progress_interstitial`, attr `favoriteTopics`)
- **Options w/ icons:** 🐠 Sea life / 🪐 Space / 🚀 Vehicles / 🐤 Nature / 🍕 Cooking.
- **Progress:** 18/24.
- **Lever:** Deeper personalization; child-delight imagery keeps the parent emotionally invested in *their specific kid's* plan.

### step-10 — Keiki makes learning *Speaking* fun and easy! (`social_proof`, give-screen)
- **Two App-Store-style testimonial cards**, 5★ each:
  - *Mary34* (Dec 28, 2024): "Our kid loves Keiki! She's learning words so fast and enjoying the games. We're amazed by the content! ✨"
  - *Mr.jones* (Oct 3, 2024): "She's now speaking better because lessons feel like real playtime. We improved much faster than expected."
- **Lever:** Social proof placed *before* skepticism peaks (per case-study lesson). "Speaking" is the focus area that recurs at step-12 — primes the named outcome. "people like me" parent voices.

### step-11 — Congratulations 🚀 (`progress_interstitial`, give-screen)
- **Copy:** "We're preparing your child's personalized learning plan based on your answers."
- **Image:** `hero-congrats.png`.
- **Lever:** Reward beat + investment payoff framing ("based on your answers" = your effort produced this). Builds anticipation for the result.

### step-12 — Your child's learning profile (`summary_confirmation`)
- **Profile card:** child illustration + facts (Gender: Girl, Age: 3-4 years, Extracurricular activities: Yes).
- **"Current progress level"** scale (Just starting → On track → Ahead) with a marker + pill "Your child's level," subtitle "Based on your quiz answers."
- **Focus areas:** Speaking (with icon).
- **Lever:** Self-generated value — quiz answers reflected back as a "diagnosis" creates conviction the assessment is real and personal. Marker placement implies room to improve (gentle gap → motivation). **NOTE:** profile facts are hardcoded ("Girl", "3-4 years") and do NOT read the actual `childGender`/`childAge` attributes — a personalization gap (see §8).

### step-13 — Your child's learning improvement forecast (`value_prop_story`)
- **Copy:** "With Keiki, your child can boost core skills and reach the goal in **2 months**."
- **Animated bar chart** (3 rising bars + a "Goal" bar with dot), footer "Now → In 2 months," footnote "This chart is for illustrative purposes only."
- **Lever:** Future-state projection / progress visualization (framework pattern #5, +15%). Date/duration anchor ("2 months") makes the outcome concrete. Compliance footnote ("illustrative") hedges the projection.

### step-14 — Personalizing your child's learning plan (`single_step_choice`, attr `includeWorksheets` boolean)
- **Loader UI:** Didi mascot + "Reviewing answers — 50%" with a progress fill bar.
- **Embedded question card:** "Do you want to include worksheets in your personal plan?" → **No / Yes** buttons.
- **Lever:** Loader-personalization question (framework pattern #6, +3%) — turns dead processing time into one more micro-commitment and makes the plan feel custom. The "50% reviewing" framing implies the plan is mid-build and the user is co-authoring it.
- **Branching:** Both answers route to step-15 (sequential). The boolean is stored but does not alter the flow or paywall.

### step-15 — Discover how *JKNK* will progress in just 4 weeks (`social_proof` / projection)
- **Headline** highlights "**JKNK**" (a child-name/code token) and "**just 4 weeks**."
- **Animated line chart** (`chart-line.svg`), "Now → After 4 weeks," weeks 1–4 axis, subtitle "Chart for illustrative purposes only."
- **Lever:** Second, sharper future-state projection (now 4 weeks vs. step-13's 2 months) — accelerating the timeline right before price = momentum into the paywall. "JKNK" ties to the paywall promo code `JKNK_2026`, manufacturing a personalized-deal feeling.
- **Note:** "JKNK" is a literal placeholder string, not the real child name (personalization gap — see §8).

### paywall (`step-32-paywall.tsx`) — see §4.

### subscription-started (`step-33-subscription-started.tsx`)
- **Post-checkout handoff.** Detects platform from UA (iOS/Android/desktop), auto-fires the mobile deep link after 500ms (once, guarded by sessionStorage), shows App Store + Google Play buttons, a **QR code** (api.qrserver.com) for desktop→phone transfer, "Open app now," and "Send link to email."
- **Tracking:** reads `payment_intent` + `redirect_status` from the Stripe return URL and fires `payment_checkout_succeeded` / `payment_checkout_returned` (deduped by intent id).
- **Copy:** "Congratulations! Your subscription has started." + a recovery note: "In case the app asks you to subscribe again, open the same deep link one more time."
- **Lever:** Closes the web→app gap (the actual product lives in the app). Reduces post-purchase drop / refund risk by getting the parent into the app fast.

---

## 3. Branching, Experiments & Entry Points

**Routing is strictly linear.** `funnel.routing.ts`:
- `stepRouteRulesById` maps every step to a single `{ type: 'route', to: <next> }`. No per-answer divergence.
- `choiceTargetsByStepId` is **empty `{}`** — no yes/no fork is wired anywhere, including step-3 and step-14, whose answers are recorded but not routed on.
- `funnelExperiments` is **empty `[]`** — no A/B variants are active. The experiment-resolution machinery (`resolveConfiguredNextStep`, variant maps) exists but is dormant.

**Entry points** (`funnelEntryPoints`):
- `default` → `step-1` (sourceHints: web, default).
- `paywall` → `paywall` (sourceHints: paywall, checkout) — a direct-to-paywall entry for returning/retargeted traffic.

**Attributes captured** (none gate routing; all feed personalization/analytics): `childAge`, `childGender`, `hasSiblings`, `caregiverRole`, `dayType`, `favoriteActivities`, `favoriteTopics`, `includeWorksheets`.

**Scaffolded-but-unwired steps (dead in the live flow):**
- `step-34-upsell-form.tsx` (`upsell-form`): a "Special Offer — Add priority support" screen with email field; Accept → goToStep(paywall), Skip → goToStep(cancellation). **Not in `src/steps/index.ts`, not in the registry, not in the sequence.** Its own copy admits: "This optional upsell branch is scaffolded by default and can be rewired in routing config." Effectively template boilerplate, not part of Keiki.
- `step-35-cancellation.tsx` (`cancellation`): a full multi-stage manage/cancel flow. Also not in the sequence; reachable only via the standalone `/manage-subscription` route (see §5).

**Stale doc:** `PLAN.md` describes a generic 7-step "claim/profile/activate/eligibility/devices-selected/paywall" template — it does NOT match the shipped Keiki funnel and should be ignored for analysis.

---

## 4. Paywall Architecture (`step-32-paywall.tsx`)

A long-form, single-scroll paywall (`type: cancellation_offer`, `kind: paywall`) on the deep-purple brand background. The structure closely follows the paywall best-practices flow.

**Persistent urgency (two stacked sticky bars):**
1. Brand header (logo + menu).
2. Sticky offer bar: "🎁 -50% with code" + live **MM:SS countdown** (starts **09:55**, decrements every second to 0) + green "Get my plan" button (tracked source `sticky-top`).

**Above-the-fold hero — future-state visualization:**
- **Now / Your goal** toggle over `child-behaviour-change.png` with an "On Track" pill.
- Two metric columns comparing **Now vs. Goal**:
  - *Academic skills:* Intermediate (2/3 bars) → **Advanced** (3/3).
  - *Discipline:* **Frequent tantrums** (partial) → **Well behaved** (3/3).
  - Bars animate-fill on load (`keikiFillBar`).
- This is the framework's "visualize future state on the paywall" (#11, +10–15%) and makes the *behavioral* transformation (not just academic) visceral.

**Promo card:** Didi character + "-50% with code", code **`JKNK_2026`**, "applied - 10 min left!" + a pink clock chip mirroring the countdown. The code echoes the "JKNK" token from step-15 → earned/personalized-discount feeling.

**Primary CTA** ("Get my plan") repeats at: sticky bar, hero, and inside the plan card (tracked sources `sticky-top` / `hero-cta` / `plan-cta`).

**Trust & proof stack (in scroll order):**
- **As featured in:** Common Sense Media, CNN, Trustpilot, Aptoide, a media seal, techtarget.
- **Benefits block** "Innovating way of learning with your child" — 5 numbered, *parent-outcome-framed* benefits (verbatim):
  1. No more feeling overwhelmed
  2. Reduce tantrums and behavior issues
  3. Your child will stay motivated and engaged
  4. Have more time for yourself
  5. **Forget feeling guilt about screen time** — "plenty of educational games that will turn the screen time of your child in education"
  → Note these sell to the *parent's* emotional state (overwhelm, guilt, free time), not the child's skills.
- **Stats row:** **12,000,000** kids used our products · **300+** activities · **94%** parent satisfaction.
- **Savings (anchoring):** "save up to **$500 annually** on educational materials" + "**50%** of the time you spend calming down/motivating your child." Anchors the subscription price against a much larger external cost.
- **Access list:** 7+ week plan, the app + games, worksheets on 10+ skills (new monthly), child progress report.

**Pricing block ("Choose your plan"):** three tiers, per-day reframing, strikethrough anchors:
| Tier | Old | Now | Per day |
| --- | --- | --- | --- |
| 1 month — **"Best value for you"** badge, default selected | $39.99 | **$10.73** | $0.36 (was $1.33) |
| 3 months | $59.99 | $19.51 | $0.22 (was $0.67) |
| 6 months | $89.99 | $34.14 | $0.19 (was $0.50) |
- Per-day framing ("$0.36 per day") shrinks the price; strikethrough old prices anchor the discount.
- **Quirk:** the *1-month* plan carries the "Best value" badge and is pre-selected, even though the 6-month plan is cheapest per day — a deliberate nudge toward the lower-absolute-price commitment (lower entry friction, higher renewal count). The 3- and 6-month UI tiers both map to the same underlying checkout plan id (`secondPlanId`) (see §8).

**Risk reversal + legal:** "30-day money-back guarantee!" directly under the plan CTA. Legal line: discount auto-applied to first term ($10.73), auto-renews at full $39.99, cancel in settings or via support@get.keiki.app. "Pay safe & secure" + Visa/MC/Discover/PayPal/Amex icons.

**Late social proof:** "Join 12 million happy parents" · "4,6★ Average rating on App Store and Google Play" · 3 named App-Store-style reviews (Vadym_vad, Eve_26 — note Eve's "tried the free subscription first then paid" framing models the trial→pay journey, Nmes Sam).

**Footer:** KaulanaTech Limited, Delaware, USA + Money-Back / Privacy / Subscription Terms links.

**Checkout mechanics (`StripePaymentPopup` + `paywallCheckout.service.ts`):**
- CTA opens an in-page **bottom-sheet modal** (does NOT navigate away) → fires `payment_popup_opened` analytics with plan + amount + source.
- Payment intent is pre-created on mount (`prepareCheckout`) so the sheet opens warm.
- Sheet shows **Original price / % OFF / Total** breakdown, a guarantee line ("30 days moneyback guarantee. Cancel anytime."), an **Express Checkout (Apple Pay / Google Pay) block placed ABOVE the card form** (wallet-first, framework #10), then "Continue with payment" → reveals card `PaymentElement` → "Confirm purchase."
- On success, Stripe returns to `/subscription-started?payment_intent=…&redirect_status=…&source=stripe-checkout`.

---

## 5. Upsell / Downsell / Cancellation Flow

**In the live funnel: there is no upsell or downsell.** The flow ends at the paywall → subscription-started handoff.

**Downsell observation:** The conversion best-practices reference recommends a checkout-close down-sell modal. Keiki does **not** implement one — closing the `StripePaymentPopup` simply returns the user to the paywall (overlay click or × button → `setPopupOpen(false)`), with no recovery offer surfaced. Re-opening relies on the persistent paywall urgency (countdown + sticky CTA) rather than a deeper-discount popup. **This is a missed ARPU lever (see §8).**

**Upsell (`step-34-upsell-form.tsx`) — scaffolded, unwired.** Generic "Add priority support for your first month" + email capture. Accept → paywall; Skip → cancellation. Not registered, not reachable in production.

**Cancellation / manage subscription (`step-35-cancellation.tsx`):** a polished 4-stage flow, reachable only via the standalone `/manage-subscription` route — NOT part of the conversion funnel.
1. **subscriptions** — lists cancellable subscriptions (filters out already-canceled / cancel-at-period-end), support email, "Continue."
2. **why** — 7 reason tiles: 💰 too expensive, 📱 don't use enough, 🙁 couldn't figure it out, 😐 not enough value, 📦 found alternative, 🛠️ technical issues, ⏳ taking a break. (Reason stored as `manageSubscriptionReason`; no save-offer/retention interstitial is shown — selecting a reason goes straight to confirm.)
3. **confirm** — echoes reason + plan, "Cancel subscription" (calls `apiService.updateSubscription({action:'cancel'})`).
4. **done** — status updated + support email + "Return to home" (→ step-1).
- A simpler admin variant lives at `manage-subscription/page.tsx` (cancel/renew toggle, raw subscription metadata).
- **Retention gap:** the cancel flow harvests a reason but makes **no save attempt** (no pause, discount, or "are you sure"). Pure compliance-grade cancellation.

---

## 6. High-Performance Techniques Observed

1. **Mascot-asks-the-question framing.** Didi's head + speech bubble tops every quiz screen, so questions feel like a friendly character talking to the parent — resolves the trust gate (ally signal) with zero text claims, and softens data-collection.
2. **Effort→reward cadence.** Ask clusters (1–5, 8–9) are punctuated by give-screens (6 reassurance, 7 insight, 10 testimonials, 11 congrats) — textbook fuel-refill rhythm; never 3 raw questions back-to-back at the front.
3. **Buyer-vs-user emotional split, exploited well.** The whole funnel sells to the *parent's* feelings — overwhelm, guilt, lack of time, aspiration for the child — while the *child* is the delighted end-user (emoji topics, games). Paywall benefits #1/#4/#5 explicitly soothe parent overwhelm, free-time loss, and screen-time guilt (poke→soothe→empower on the framework's exact guilt lever).
4. **Two escalating future-state projections before price.** step-13 bars ("2 months") then step-15 line chart ("just 4 weeks") — accelerating timeline = momentum; paywall hero then converts the *behavioral* before/after (tantrums → well-behaved) visually.
5. **Self-generated "diagnosis."** step-12 reflects quiz answers back as a learning profile + "Current progress level" marker, so the parent concludes "this assessment is real and my kid has room to grow" — conviction they can't argue with.
6. **Anchoring stack on the paywall.** Strikethrough prices + per-day reframe ($0.36/day) + external-cost anchors ("$500/year on materials," "50% of your time") make the subscription feel trivially cheap.
7. **Earned-discount continuity.** The "JKNK" token in step-15's headline reappears as promo code `JKNK_2026` on the paywall ("applied - 10 min left!") — manufactures a personalized, time-boxed, already-earned deal.
8. **Honest-urgency apparatus.** ~10-minute live countdown in both a sticky bar and the promo card, consistent across the page; CTA repeated at every scroll section (sticky/hero/plan).
9. **Friction-minimized checkout.** Pre-warmed payment intent + in-page bottom-sheet (no navigation) + Apple/Google Pay above the card form + price-breakdown with % OFF + guarantee line.
10. **Web→app bridge engineered.** subscription-started auto-deep-links, offers QR for desktop, and pre-empts the "asked to subscribe again" confusion — protecting the conversion through to app activation.
11. **Proof breadth.** Press logos, 12M-kids / 94%-satisfaction stats, App-Store-style testimonials early (step-10) AND late (paywall), 4.6★ — proof both before skepticism and at the decision point.

---

## 7. Notable Copy & Microcopy Tricks

- **"To create personal learning plan"** (step-1 subtitle): converts the very first tap into a personalization investment, not a cold quiz question.
- **"Did you know that 72% of parents face this challenge?"** (step-7): normalization that removes parental shame while seeding a problem to fix — guilt poke immediately soothed by "many kids / many parents."
- **"reduce distractions by 35%" / "reach the goal in 2 months" / "just 4 weeks"** — specific numbers do the persuading; the parent's brain multiplies and concludes value (Hitchcock), while "illustrative purposes only" footnotes hedge compliance.
- **"Reviewing answers — 50%"** (step-14): frames a sales question as the plan being actively co-built from the parent's inputs.
- **Benefit titles framed as the parent's relief, not features:** "No more feeling overwhelmed," "Have more time for yourself," "Forget feeling guilt about screen time."
- **"Best value for you"** badge on the *cheapest-absolute* (1-month) plan — steers to the low-friction entry while implying it's the smart pick.
- **Per-day price split into `$` + big `0` + small `36` + "per day"** typographically shrinks the number visually, not just verbally.
- **"-50% with code … applied - 10 min left!"** — discount presented as already applied (loss-averse: act or lose it), reinforced by a ticking chip.
- **Review microcopy that models the buying journey:** Eve_26 — "at first I was reluctant… tried the free subscription… wouldn't hesitate to pay it every month." A testimonial that pre-handles the "is it worth paying?" objection.
- **"In case the app asks you to subscribe again, open the same deep link one more time"** — disarms a known post-purchase failure mode before it causes a refund.
- **Profile recap mirrors quiz facts** ("Extracurricular activities: Yes" from the siblings/extracurricular answer) to prove the funnel "listened."

---

## 8. Weaknesses / Risks / Things to Avoid

1. **Hardcoded personalization that contradicts user input.** step-12 always shows "Gender: Girl / Age: 3-4 years" regardless of `childGender`/`childAge`; step-15 headline says "**JKNK**" instead of the child's name; the paywall hero is fixed "tantrums → well-behaved." A father who picked "Boy, 7+" sees "Girl, 3-4." This is the funnel's biggest credibility risk and directly undercuts the self-generated-diagnosis lever. **QA: wire real attributes into the profile, the JKNK token, and ideally the promo code.**
2. **No name/email capture screen.** There is no Section-E data-capture step; email exists only at Stripe checkout. No lead recovery for drop-offs before payment, and no name to personalize the JKNK projection (which is why it's a placeholder).
3. **Misleading progress bar.** "x/24" total with only 15 quiz screens, and the numerator jumps non-linearly (2,3,5,7,11,18). Risk of "wait, it said 18/24 then paywall" expectation breaks; also some give-screens (6,7,10,11) show no progress bar at all, making perceived length inconsistent.
4. **No checkout-close downsell.** Closing the payment sheet offers no recovery offer — a known +~15% ARPU lever left on the table (framework #13). High-intent hesitators get nothing but the same paywall.
5. **Duplicate checkout plan ids.** In `planOptions`, the 3-month and 6-month tiers both use `secondPlanId` — the displayed 6-month price ($34.14) may not match the actual charged amount for that tier. **Verify the underlying plan catalog maps 1:1 to the three UI tiers before trusting the prices/renewal terms.**
6. **Legal/claims fragility.** Renewal terms cite a single price ($10.73 → $39.99) that only matches the 1-month tier; if a user buys 3/6-month, the legal line is inconsistent. "Illustrative only" footnotes cover the charts, but "reduce distractions by 35%" / "save up to $500 annually" are unsubstantiated specific claims that could draw scrutiny in a kids/education vertical.
7. **No commitment/pledge screen.** Despite being a behavior-change product (where a "commitment" screen typically adds +7–11%), there's no parental pledge or "I commit to a daily routine" beat before the paywall.
8. **Cancellation flow has no save attempt.** It collects a cancel reason then cancels — no pause/discount/retention offer, so churn isn't defended.
9. **Stale `PLAN.md`** describes an unrelated generic template; anyone using it to reason about Keiki will be misled. Treat as dead doc.
10. **Testimonial/proof authenticity unverifiable.** "12 million happy parents," press logos, and named reviews must be backed by real permissions/data, or they're a compliance and trust liability in a children's-product context.
