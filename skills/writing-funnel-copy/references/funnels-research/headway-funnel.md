# Headway Funnel — Research Notes

> Source: `funnels/rag-catalog/headway-funnel` — `src/steps/index.ts` is the source of truth (repo also carries stale ClaimBee scaffold debris; see risks).

## 1. Overview

- **Brand:** Headway (40M+ user self-growth / micro-learning app; nonfiction book summaries + insights). Brand assets, logo, legal entities ("LibroTech Inc." US / Nicosia Cyprus) all real-Headway-styled.
- **Vertical:** Self-growth / habit-building / learning / psychology (subscription). Domain tags in `rag.meta.json`: `self-growth, habit-building, learning, psychology, subscription`.
- **Entry promise:** "Become the most interesting person in the room" + "3-minute quiz" (step-1 hero). This is the ad-match headline, repeated verbatim at the result screen (step-21) and implicitly at the paywall.
- **Target audience:** Mobile-first (viewport 390×780) self-improvement seekers, busy people who "can't find time to sit and read," aspirational learners who admire high-achievers.
- **Quality score:** **0.95** (`rag.meta.json`) — the highest-tier reference funnel in the catalog.
- **Total step count:** 24 active nodes = 22 quiz/paywall steps (`step-1` … `step-22`) + `subscription-started` handoff. The real content for steps 1–22 lives in **one brand file**: `src/steps/headway.tsx` (each `step-NN.tsx` re-exports from it). Post-purchase placeholder files exist but are mostly NOT wired in — see §3 and §5.

> **Important caveat for synthesis:** The funnel directory contains two distinct paywall/post-purchase layers. The **live, polished Headway funnel** is `step-22` (in `headway.tsx`). A second set of files — `step-32-paywall.tsx`, `step-34-upsell-form.tsx`, `step-35-cancellation.tsx` — are leftover **scaffold from a different "ClaimBee / unclaimed-settlements money" template** and are NOT in the active sequence (`src/steps/index.ts` only registers `step-1…22` + `subscription-started`). They are documented in §5 for completeness but should be treated as template debris, not Headway's real flow. `PLAN.md` / `PRODUCT_SENSE.md` describe a generic 7-step template and are stale relative to the shipped 22-step Headway build.

---

## 2. Step-by-Step Walkthrough

All copy below is quoted from `src/steps/headway.tsx`. Progress bar is a 4-dot "PROFILE / PATTERNS" tracker. Routing is strictly sequential (§3).

| # | Step id | Type | Headline / key copy | Options | Value loaded | Psychological lever | Branching |
|---|---------|------|---------------------|---------|--------------|---------------------|-----------|
| 1 | `step-1` | intro / commitment | **"Become the most interesting person in the room"** · "3-minute quiz" | 4 age cards w/ photos: 18-24, 25-34, 35-44, 45+ (tap = answer + advance) | Aspiration + effort estimate ("3-min"). Age card *is* the first question — zero-friction start. | Expectation match (ad headline), investment escalation (first tap is trivial), commitment bias. Effort cap framed ("3-minute"). | none (→ step-2). Sets `ageRange`. |
| 2 | `step-2` | social-proof | **"40+ million people already use the Headway app"** + Daily Mail pull-quote "a bite-sized learning app for those who strive to grow" + "MENTIONED IN" Yahoo/Forbes/TechCrunch/Entrepreneur logos | none (passive) | Trust gate / authority. Placed at screen 2 = before skepticism peaks. | Social proof (40M), authority/press logos, trust-gate resolution. No selling. | none. |
| 3 | `step-3` | question | **"What is your age?"** | 18-24 / 25-34 / 35-44 / 45+ | Re-confirms age (data redundancy → personalization feel). Easy yes-momentum. | Micro-commitment, confirmation shortcut. Progress dot turns active. | none. Re-sets `ageRange`. Back→step-2. |
| 4 | `step-4` | question | **"Select your gender"** | 👨 Male / 👩 Female / 🧑 Other | Profile data; another trivial tap. | Investment escalation, commitment bias. | none. Sets `gender`. |
| 5 | `step-5` | interstitial / value-prop | **"Yay, glad you are here!"** — "We'll help you with self-growth. First, let's dive into your personality and tailor your personal plan." Animated brain-rocket. | none | Fuel **refill** after 2 ask-screens (3+4). Validation + personalization promise. | Fuel refill, ally signal, personalization priming ("tailor your personal plan"). | none. |
| 6 | `step-6` | multi-select question | **"Choose areas you'd like to elevate"** · sub: "The choice won't limit your experience" | 12 chips: Emotions, Motivation, Nutrition, Habits, Self-confidence, Mindset, Self-care, Exercise, Empathy, Love & relationships, Personal Finance, Creativity | Self-segmentation; user invests in defining their own goals (multi-select = deeper investment). | Self-generated value (Hitchcock — user authors their plan), micro-commitment. Reassurance subcopy removes "wrong answer" friction. | none (multi-select, no per-answer branch). Sets `growthAreas`. |
| 7 | `step-7` | interstitial / value-prop | **"Understand big ideas in minutes instead of hours!"** — "Cover any book in just 15 minutes… make the most of your time" | none | Core mechanism/benefit reveal (speed). Refill after the effortful step-6. | Anchoring (minutes vs hours), fuel refill, value-loading. | none. |
| 8 | `step-8` | question (aspirational) | **"Whose life principles, success, and personality inspire you the most?"** | 9 role-model photo cards: Steve Jobs, Richard Branson, LeBron James, Oprah, Emma Watson, Serena Williams, Jeff Bezos, Kevin Hart, Brené Brown | Identity aspiration — ties self-growth to admired achievers. High-engagement (faces). | Aspiration/identity, self-generated value, borrowed authority. | none. Sets `roleModel`. (No auto-advance — selection only.) |
| 9 | `step-9` | question | **"Are you a big-picture or detail-oriented person?"** | 🔭 Big-picture / 🔍 Detail-oriented | Personality profiling → "personalized plan" justification. | Confirmation, commitment, personalization priming. | none. Sets `mindsetStyle`. |
| 10 | `step-10` | emoji-scale question | **"Do you always know what you want exactly?"** | 5-point emoji scale 👎👎🤷👍👍 (index 1-5) | Self-reflection prompt; sets up empathy beat in step-11. | Self-generated value, micro-commitment. | none. Sets `clarityScore`. |
| 11 | `step-11` | interstitial / response | Same Q repeated + response card: **"We understand! 🫂"** — "We'll consider the growth points you've picked to craft the most relevant plan for your needs." (scale frozen on 🤷) | none | Adaptive-style feedback / empathy refill directly after the answer. | Answer-feedback acknowledgment (best-practice #3/#4), poke-soothe-empower (soothe), fuel refill. | none. |
| 12 | `step-12` | progress-interstitial (chart) | **"Motivation is your key to success!"** — "You're twice as motivated when you see your goals clearly… keep them in focus even when the going gets tough." Animated bar chart. | none | Mechanism education ("why your current state happens"); justifies the plan. | Authority via data viz, anchoring ("twice as motivated"), Hitchcock (user concludes plan = motivation). Progress dots advance. | none. |
| 13 | `step-13` | progress-interstitial (chart) | **"Over the last month, our users have read 303,600+ book summaries!"** — "Join our community of avid learners…" Animated learning diagram. Label switches to **"PATTERNS"**. | none | Social proof with a concrete number; community belonging. | Social proof (specific stat beats vague), bandwagon. | none. |
| 14 | `step-14` | question (yes/no) | **"Choose the books that seem interesting to you"** — shows *Deep Work* cover | No / Yes (icons) | Content preview + engagement; primes "the app has real books." | Micro-commitment, product-tangibility, self-generated relevance. | none (both → step-15). Sets `bookInterest`. |
| 15 | `step-15` | social-proof (map) | **"Join over 40M+ people"** + pill **"Over 5M users in your location"** + world map | none | Localized social proof ("in your location" = personalized bandwagon). | Social proof, localization, belonging. `legal="none"` (clean). | none. |
| 16 | `step-15b` | multi-select question | **"Do you have a specific reason for self-growth?"** | 9 reasons w/ emoji: Getting a promotion 👩‍💼, Becoming an entrepreneur 📊, Relationship commitment 👩‍❤️‍👩, Parenthood 👨‍👩‍👧, Major life transition ✈️, Mental/emotional well-being 🤯, Financial milestone 🏦, Retirement planning 🏖, Grief and loss ☁️ | Deep motivation capture — the emotional "why." High personal investment. | Self-generated value (user names their own stakes), commitment, emotional anchoring. | none (multi-select). Sets `selfGrowthReasons`. |
| 17 | `step-16` | question (timing/commitment) | **"Set your goal on timing"** · "Pick the amount of time you will spend on self-development daily" | 🤙 Easy 5 min/day · 👌 Common 10 min/day · 🤘 Serious 15 min/day · 💪 Intensive 20+ min/day | Commitment device (daily-time pledge); seeds the "15 min/day" claim reused on paywall. | Commitment screen (best-practice #9), consistency bias, goal-setting. | none. Sets `dailyTimeGoal`. |
| 18 | `step-17` | loader (interactive) | **"We are crafting your learning experience…"** — animated "Setting goals" progress to **49%**, then a mid-loader micro-question **"Do you self-reflect?"** (No/Yes) + 5★ review snippet "Enjoyed by 40M+ people / by LisJefhb": "Devoting **15 min a day**… will bring you an **improved** person." `autoAdvanceMs: 2600`. | mid-loader Yes/No (cosmetic) | Turns dead loader time into engagement + social proof + reinforces 15-min pledge. | Loader-as-priming real estate, loader personalization question (best-practice #6), labor illusion (builds perceived effort/value). | auto-advances after 2.6s. |
| 19 | `step-18` | summary-confirmation (loader) | **"We are crafting your learning experience…"** — animated checklist ticking: Goals ✓ Growth areas ✓ Content ✓ Challenges ✓ | none | Reflects back everything the user invested → "this plan is built from MY answers." | Labor illusion, commitment recap, self-generated value. | none. |
| 20 | `step-19` | email capture | **"Achieve your goal with Headway"** · "Enter your email to create a personal account" + awards badges. Legal/consent microcopy inline. | email input | Data capture framed as account creation (function, not marketing). | Investment escalation (real identifier late), framing as necessary, trust (awards). | none. Sets `email`. No hard validation gate. |
| 21 | `step-20` | summary-confirmation (result) | **"Your personal growth plan is ready"** — "Based on your answers, we crafted a self-growth plan." Animated curve **Now → 54 books per month**, dated **FEBRUARY 26 → MARCH 29**, + "you will need an iPhone or Android" note. | none | The payoff / future-state projection with a dated timeline. | Future-state visualization (best-practice #5/#11), dated timeline (case-study AOV pattern), Hitchcock (brain fills optimistic outcome). | none. |
| 22 | `step-21` | value-prop (comparison) | **"Become the most interesting person in the room"** (ad headline echo) — "Based on your answers, we crafted a self-growth plan." Comparison figure: full books vs key insights + recent Headway activity. | none | Pre-paywall reframe: full books (slow) vs Headway insights (fast). Closes the loop to entry promise. | Expectation-match bookend, anchoring (full book vs insight), value recap. | none → paywall. |
| 23 | `step-22` | **paywall** | See §4. **"Choose your plan"**, 60%-discount timer 9:53, 3 tiers, per-day pricing, features, FAQ, reviews, store ratings, dual price blocks. | plan select + Continue | Convert accumulated value. | Anchoring, loss aversion (timer), social proof, per-day framing, CTA repetition. | terminal (→ subscription-started conceptually). |
| 24 | `subscription-started` | post-purchase handoff | **"Congratulations! Your subscription has started."** App Store / Play links, auto deep-link, QR code, "Send link to email." | store/app links | Fulfillment + app-install handoff; tracks `payment_checkout_succeeded`. | Reduces post-purchase friction, platform-aware deep-linking. | auto-opens app on mobile; desktop shows QR. |

---

## 3. Branching, Experiments & Entry Points

- **Routing model:** Purely **linear/sequential**. `funnel.routing.ts` `legacyStepRouteRulesById` hard-wires `step-1→2→3→…→22` with `{ type: 'route' }`; `funnel.manifest.ts` rebuilds the same sequential edges. There is **no conditional edge, no per-answer divergence, and no live experiment** anywhere in the active funnel.
- **Experiments:** `funnelExperiments` resolves to `[]` (`legacyFunnelExperiments` empty; no `graph.experiments` in config). The infrastructure for A/B exists — `FunnelExperimentConfig`, `resolveExperimentVariantKey`, variant→step routing, control-fallback — but nothing is configured. Reusable scaffold, not active.
- **Conditional-edge infra (unused):** `resolveNextStepFromGraph` supports `edgesByStepId` with `when.conditionId` that fires on `attributes[conditionId] === true`, with an unconditional fallback edge. None populated.
- **Entry points:** Single default — `{ id: 'default', stepId: 'step-1', isDefault: true, sourceHints: ['web','default','headway'] }`. `getDefaultEntryPointStepId()` → `step-1`.
- **Answers captured but never branched on:** `ageRange`, `gender`, `growthAreas`, `roleModel`, `mindsetStyle`, `clarityScore`, `bookInterest`, `selfGrowthReasons`, `dailyTimeGoal`, `email`. They drive perceived personalization (the "we crafted YOUR plan" framing on steps 18/20) but do not change the path or the paywall — personalization is **theatrical, not algorithmic**. This is itself a deliberate, low-cost technique.
- **Choice-target map:** `choiceTargetsByStepId` is `{}` — no yes/no fork is routed; both step-14 answers go to step-15.
- **Post-purchase / off-sequence files** (NOT reachable in the linear flow):
  - `step-34-upsell-form.tsx` (`upsell-form`): a generic "Add priority support" upsell with Accept→`paywall` / Skip→`cancellation`. Self-describes as "scaffolded by default and can be rewired in routing config." Not registered.
  - `step-35-cancellation.tsx` (`cancellation`): a real 4-stage manage/cancel flow (see §5). Reachable only via a `Manage subscription` link, which exists in the **ClaimBee** `step-32-paywall`, not in the live Headway `step-22`. So in the live funnel it is effectively orphaned.
  - `step-32-paywall.tsx`: full alternate "ClaimBee" settlements paywall — different brand/domain. Not in sequence.

---

## 4. Paywall Architecture (`step-22`, `StepTwentyTwo` in `headway.tsx`)

A long-form, scroll-driven paywall with the price block rendered **twice** (a light-theme block near the top, a dark-theme block at the bottom).

- **Top urgency bar (sticky-feel):** `headway-pw22-reserve` — **"60% discount reserved for: 9:53"** + a **Continue** button. Repeated as a banner inside the dark bottom block (`60% / DISCOUNT RESERVED FOR / 9:53`). Note: the timer is **static "9:53"** in this build (no live countdown in `step-22`), i.e. decorative urgency.
- **Hero / offer block (light) — `PaywallBlock theme="light"`:** Heading **"Choose your plan"** + 3 plan cards + disclaimer + Continue CTA + "Pay safe & secure" + a row of payment-provider logos (PayPal, **Apple Pay**, **Google Pay**, Visa, Mastercard, Maestro, Discover, Amex).
- **Pricing tiers + anchoring (`planRows`):**
  | Plan | Old price | Price | Save tag | Per-day | Badge |
  |------|-----------|-------|----------|---------|-------|
  | 1 month | ~~$27.36~~ | **$13.41** | Save 51% | ~~$0.91~~ → **$0.45/day** | — |
  | **3 months** | ~~$49.98~~ | **$19.98** | Save 60% | ~~$0.56~~ → **$0.22/day** | **MOST POPULAR** (pre-selected default) |
  | 12 months | ~~$108.14~~ | **$52.99** | Save 51% | ~~$0.30~~ → **$0.15/day** | — |
  - **Anchoring stack:** struck-through old price + "Save X%" + struck-through old per-day + bold per-day. The mid tier carries the highest "Save 60%" and the MOST POPULAR badge and is the default selection — classic decoy/center-stage steering.
  - **Per-day framing:** every tier renders price as a big `$0` + small fraction + "PER DAY" — makes spend feel trivial ("$0.22/day").
- **Disclaimer (renewal honesty):** "We've automatically applied discount to your first subscription price… your subscription will be automatically renewed at full price of **$49.98** at the end of chosen subscription term… manage via your personal account." Discount-feels-earned + compliance.
- **Features-as-benefits (`paywallFeatureItems`), "What you get with Headway":** 1500+ nonfiction book summaries · 5000+ life-changing insights · Habit tracker · Self-growth challenges · "Save & memorize favorite book insights with the Spaced Repetition feature." (Star-bulleted; outcome-tilted but partly feature-named.)
- **FAQ (secretly-sells):** "Why do I need the Headway app?", "How do I get access to the app?", "How can I cancel my subscription?" — addresses need, access, and cancellation-risk objections.
- **Social proof block:** "People love the Headway app" / "Become a member of our global community of **40 million people**" + 4 Instagram-style review cards (mr.rageright, mcogbonna, thefinestyler, thisinnagirl) with avatars + 5★, each with a real-sounding testimonial (e.g., "simplifies books into super condensed but easy-to-digest snippets… I recommend to anyone who's busy").
- **Store-rating trust stamps:** App Store **4.7 (67K ratings)** + Google Play **4.3 (38K ratings)** with rendered star bars.
- **Second price block (dark) — `PaywallBlock theme="dark"`:** repeats "Choose your plan," same 3 tiers, same Continue CTA, same safe-pay + provider logos, plus the 60% reserved banner. This is the re-close after value (best-practice paywall step 6).
- **CTA repetition:** "Continue" appears in the top reserve bar, the light block, and the dark block (3×).
- **Apple Pay placement:** Provider logos (Apple Pay/Google Pay among them) sit directly **below** each plan list, matching the "wallet under prices" best practice — though in `step-22` they are presented as a **logo strip (`aria-hidden`)**, i.e. trust signalling rather than a live one-tap Apple Pay button. (A live Stripe Express/Apple Pay button + `$1` trial exists in the off-sequence `step-32` ClaimBee paywall, not here.)
- **Guarantee / before-after:** The live Headway `step-22` does **not** render a money-back badge or a before/after transformation block (those live in the ClaimBee `step-32` scaffold). The before/after is instead front-loaded as the step-20 dated growth-curve and step-21 comparison.

---

## 5. Upsell / Downsell / Cancellation Flow

> All three exist as files; in the **live Headway sequence** only `subscription-started` runs. The rest are reusable template scaffold (and partly belong to the ClaimBee variant). Documented for the playbook because the *patterns* are transferable.

- **Post-purchase handoff (`subscription-started`, live):** "Congratulations! Your subscription has started." Platform-detects UA → auto-assigns deep link (iOS/Android/universal), attempts auto-open after 500ms (dedup via `sessionStorage`), renders a **QR code** for desktop, "Open app now," and "Send link to email" (mailto). Tracks `payment_checkout_succeeded` / `payment_checkout_returned` from Stripe redirect params. Reduces install friction at the moment of highest intent.
- **Upsell (`upsell-form`, scaffold, not wired):** "Special Offer — Add priority support for your first month." Email field + **Accept offer** (→ back to paywall) / **Skip offer** (→ cancellation). A post-purchase one-more-thing pattern; explicitly self-labeled placeholder.
- **Checkout-close downsell:** In the live `step-22` there is none. The ClaimBee `step-32` scaffold implements the real pattern: a `StripePaymentPopup` modal (checkout opens in-page); closing it is the recovery hook, with a **"$1 trial / 7-day trial"** offer and a secondary "Choose your plan" block lower down — matching best-practice #13 (checkout pop-up down-sell, ARPU +15%).
- **Cancellation / save flow (`cancellation`, scaffold):** A genuine 4-stage manage flow — (1) list active subscriptions, (2) **"Tell us why you want to cancel"** with 7 reasons (too expensive 💰, don't use enough 📱, couldn't figure out 🙁, not enough value 😐, found alternative 📦, technical issues 🛠️, taking a break ⏳), (3) confirm, (4) done. Calls `apiService.updateSubscription({action:'cancel'})`. **Notably it captures the cancel reason but offers no save-offer/discount/pause counter** before cancelling — a missed retention opportunity (see §8).

---

## 6. High-Performance Techniques Observed

Concrete things in THIS funnel mapped to framework patterns (cite step ids):

- **Expectation-match bookending** — exact ad headline "Become the most interesting person in the room" opens (`step-1`) and reappears at the result (`step-21`); "3-minute quiz" caps effort expectation up front. (Psych framework §8 Section A; Conversion intervention 1.)
- **Zero-friction first tap** — `step-1` makes the age cards *themselves* the first question (photo cards, tap = answer + advance). Easiest-possible first interaction → investment escalation. (Psych §7.)
- **Trust gate resolved by screen 2** — `step-2` fronts "40+ million people" + Daily Mail quote + press logos *before* any question deepens, placing proof before skepticism peaks. (Psych §6; Conversion intervention 2.)
- **Ask/give cadence (fuel management)** — never 3 asks in a row: Q3-Q4 (ask) → `step-5` welcome refill; `step-6` (ask) → `step-7` benefit reveal; `step-10` (ask) → `step-11` "We understand 🫂" refill. (Psych §2 asymmetry.)
- **Answer-acknowledgment / empathy feedback** — `step-11` mirrors the step-10 answer with "We'll consider the growth points you've picked." (Conversion #3/#4.)
- **Self-generated value (Hitchcock)** — `step-6` (pick growth areas), `step-15b` (name your own deep reason), `step-8` (pick a role model). The user authors the plan; the funnel only reflects it back ("we crafted YOUR plan," steps 18/20). (Psych §4.)
- **Mechanism-before-solution education** — `step-12` "you're twice as motivated when you see your goals clearly" teaches *why* before selling the plan. (Conversion case-study lesson.)
- **Specific-number social proof** — `step-13` "303,600+ book summaries this month," `step-15` "Over 5M users in your location," paywall "67K / 38K ratings." Specific beats vague. (Psych §3 social proof.)
- **Commitment screen** — `step-16` daily-time pledge (Easy/Common/Serious/Intensive); the chosen "15 min/day" is then echoed in the loader review and paywall. (Conversion #9.)
- **Labor-illusion loaders as priming real estate** — `step-17` (animated 49% "Setting goals" + mid-loader micro-question + 5★ review) and `step-18` (checklist ticking Goals/Growth areas/Content/Challenges). Dead time → perceived effort + social proof. (Psych §10 loading screens; Conversion #6.)
- **Loader personalization micro-question** — "Do you self-reflect?" inside `step-17`. (Conversion #6.)
- **Future-state visualization + dated timeline** — `step-20` animated curve "Now → 54 books/month," dated FEB 26 → MAR 29. (Conversion #5/#11 + case-study dated-timeline AOV pattern.)
- **Email framed as function** — `step-19` "Enter your email to create a personal account," not "join our list." (Psych §8 Section E.)
- **Per-day price reframing + multi-anchor** — paywall renders "$0.22 PER DAY" with struck old price + old per-day + "Save 60%." (Paywall best-practice step 2.)
- **Decoy / center-stage steering** — 3-month tier carries highest "Save 60%" + MOST POPULAR + is pre-selected default. (Paywall pricing.)
- **CTA & price repetition** — paywall shows the price block twice (light + dark) and "Continue" ≥3×. (Paywall key principles.)
- **Honest-renewal disclaimer + "discount auto-applied"** — makes the deal feel earned while staying compliant. (Conversion "make discounts feel earned.")
- **Frictionless fulfillment** — `subscription-started` auto deep-links / QR / email handoff at peak intent.

---

## 7. Notable Copy & Microcopy Tricks

- **"3-minute quiz"** (step-1) — caps perceived effort before the first tap.
- **"The choice won't limit your experience"** (step-6) — removes "what if I pick wrong" friction on multi-select.
- **"Yay, glad you are here!"** (step-5) — warm, non-salesy validation; "we'll tailor your personal plan" primes personalization.
- **"We understand! 🫂"** (step-11) — emotional soothe immediately after a self-doubt question.
- **"Understand big ideas in minutes instead of hours"** (step-7) — time-anchor benefit, not a feature.
- **"Over 5M users in your location"** (step-15) — localized bandwagon; "in your location" personalizes generic social proof at zero data cost.
- **"We are crafting your learning experience…"** (steps 17–18) — possessive "your," present-progressive "crafting" = labor illusion.
- **"Your personal growth plan is ready"** + "Based on your answers, we crafted a self-growth plan" (step-20) — ownership + reciprocity framing.
- **"Devoting 15 min a day… will bring you an improved person"** (step-17 review) — testimonial that reinforces the user's own step-16 time pledge.
- **"60% discount reserved for: 9:53"** — "reserved" implies the deal is personally held for *you* (scarcity + ownership), stronger than "expires."
- **"We've automatically applied discount to your first subscription price"** — discount-feels-earned; pairs honesty (full renewal price $49.98 stated) with a win.
- **Per-day price typography** — giant `0` + tiny `22` + "PER DAY" makes the number read as near-free.
- **Result headline = ad headline** (steps 1 & 21) — closes the loop; the reward literally restates the promise that got them in.

---

## 8. Weaknesses / Risks / Things to Avoid

- **Static urgency timer.** `step-22`'s "60% discount reserved for 9:53" is hard-coded text with no live countdown (the live countdown logic exists only in the off-sequence ClaimBee `step-32`). A visibly frozen timer can read as fake and erode trust — best practice wants an honest, *moving* countdown.
- **Apple Pay is a logo, not a button (live paywall).** In `step-22` the wallet/provider row is `aria-hidden` decoration; there is no real one-tap Apple Pay/Express checkout wired into the live Headway paywall (it exists only in `step-32`). This forfeits the +10-15% wallet-payment uplift the framework calls for.
- **No money-back guarantee or before/after on the live paywall.** The guarantee badge and transformation block live in the unused `step-32` scaffold. `step-22` relies on FAQ + reviews + ratings but never explicitly removes the "risk of loss" objection at the CTA — a clear gap vs. paywall best-practice steps 7/5/8.
- **No save-offer in cancellation.** `cancellation` collects the cancel reason then cancels immediately — no pause / discount / downgrade counter-offer keyed off the stated reason (e.g., "too expensive" → offer discount). Missed retention/ARPU.
- **Personalization is theatrical, not functional.** 10 answers are captured but none branch the flow or alter the plan/paywall. Low-risk and cheap, but leaves adaptive-feedback (+7%) and quiz-result-tied pricing (case-study AOV) value on the table.
- **Template debris in the repo.** Two conflicting brand layers (Headway live vs. ClaimBee scaffold `step-32/34/35`) plus stale `PLAN.md`/`PRODUCT_SENSE.md` describing a generic 7-step flow. Risk of editing the wrong paywall; anyone iterating must confirm `src/steps/index.ts` is the source of truth for what ships.
- **Redundant age question.** Asked on `step-1` (cards) and again on `step-3`. Intentional (re-engagement / data confidence) but technically a repeated ask with no new value — borderline fuel waste if the audience notices.
- **Orphaned manage/cancel link.** The `cancellation` flow is only linked from the unused ClaimBee paywall, so in the shipped funnel there's no in-flow path to "Manage subscription," which the FAQ promises exists.
