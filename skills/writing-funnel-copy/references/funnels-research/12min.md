# 12min Funnel — Research Notes

> Source: `/Users/andrei/work/funnelsgrove/funnelsgrove/funnels/rag-catalog/12min`
> Vertical: book-summary / micro-learning (nonfiction summaries consumable in ~12 minutes), web-to-app annual subscription.
> Reconstructed from Figma nodes; 11 steps, fully linear, single long-form paywall.
>
> **Reference mode: `step-structure-only`.** This teardown is copy, visual, and interaction research—not current FunnelsGrove contract guidance. Do not copy its `type`/`kind`, answer writes, routing, shell/controller, helpers, or analytics; implementation must follow the synced project's `AGENTS.md` and `docs/funnelsgrove/START-HERE.md`.

## 1. Overview

**Product.** 12min ("microbooks") extracts the key ideas from bestselling nonfiction books into ~12-minute audio/text summaries. The funnel's job is to move a cold mobile visitor through a short profiling quiz into a long-form **annual** subscription paywall.

**Entry promise (the ad hook).** Per `PRODUCT_SENSE.md` the traffic promise is *"Become the most interesting person at the table with a personalized 12min plan."* Step 1's headline matches this verbatim ("Become the Most Interesting Person at the Table"), so expectation-match is honored within the first 3 seconds — exactly what the psychology framework demands of screens 1-2.

**Structural shape.** 11 steps, declared in `src/config/funnel.manifest.ts`:

| # | id | name | Observed interaction | Real function |
|---|------|------|------|------|
| 1 | step-1 | age-picker | Age-card choice | Hook + age segmentation (entry) |
| 2 | step-2 | book-interest | Yes/No choice | Yes/No micro-commitment on a book cover |
| 3 | step-3 | email-capture | Email form; legacy label invalid | Email + marketing opt-in |
| 4 | step-4 | plan-ready | Plan-ready recap | Animated "plan is ready" growth chart |
| 5 | step-5 | profile-improve-topics | Multi-select topic question | Multi-select topics ("Profile" progress) |
| 6 | step-6 | profile-learning-concepts | Concept value screen | "12 minutes, not hours" concept sell |
| 7 | step-7 | patterns-positive-framing | Motivational value screen | Motivational reframe ("Patterns" progress) |
| 8 | step-8 | patterns-social-proof | Social-proof screen | "300,000 microbooks last month" proof |
| 9 | step-9 | goal-selection | Multi-select goal question | Life-goal multi-select |
| 10 | step-10 | summary-bridge | Value bridge; legacy label invalid | Value bridge / callback to hook |
| 11 | step-11 | long-paywall | Purchasable paywall | Long-form annual paywall + FAQ |

**Important architecture note.** Unlike many funnels in this catalog, the step files are **not** thin re-exports of a single brand file. `src/steps/twelve-min-ui.tsx` only holds *shared chrome* — `TwelveMinHeader`, `TwelveMinProgress`, `TwelveMinStickyCta`, `TwelveMinStaticCta`, `useGoToPreviousStep`. The real copy and logic live in each `step-NN.tsx`. All quotes below are from the actual step source.

**Flow is strictly linear and deterministic.** `edgesByStepId` wires step-1→2→…→10→11 with no conditions. `experiments: []`, `choiceTargetsByStepId` empty (`docs/FLOW_CONFIG_AND_ROUTING.md` confirms). No per-answer divergence anywhere — every answer is stored and only used (implicitly) for the "personalized plan" framing, never to reroute.

## 2. Step-by-Step Walkthrough

### Step 1 — `step-1` / age-picker (entry age choice)
- **Headline:** "Become the Most Interesting Person at the Table" + kicker **"3-MINUTE QUIZ"**.
- **Options (4 image cards):** Age 18-24 / 25-34 / 35-44 / 45+, each labeled with a trailing "→".
- **Value loaded:** Expectation match with the ad; the "3-MINUTE QUIZ" kicker sets a low, finite time cost (mirrors the brand's own "12 minutes" promise — time is the product).
- **Lever:** Investment escalation done right — the very first interaction is a single zero-friction tap that *also* segments the user. Picking a card both answers and advances (`setAnswer('ageRange'); goNext()`), so there is no separate Continue button. No back button (`TwelveMinHeader` with no `showBack`) — you can't retreat from the entry.
- **Branching:** None. All four ages route to step-2. Age is captured but never used to reroute or change copy.

### Step 2 — `step-2` / book-interest (Yes/No choice)
- **Headline:** "Is this book interesting to you?" over a single **book cover** image (alt: *The Power of Habit*).
- **Options:** No / Yes (icon cards).
- **Value loaded:** Book-cover social proof + a near-100%-yes confirmation question (framework Section A: "first question must have a near-100% yes rate"). The Power of Habit is a famous, broadly appealing title.
- **Lever:** Yes-momentum / commitment bias. Either answer advances identically — the question exists to manufacture a micro-commitment and make the catalog feel personally relevant, not to branch.
- **Branching:** None. `handleChoice('yes'|'no')` both store `bookInterest` and call `goNext()` to step-3.

### Step 3 — `step-3` / email-capture (email form; legacy label invalid)
- **Contract annotation (`email-capture`):** `legacy-label-invalid`; exact implementation classification lives only in `docs/funnelsgrove/START-HERE.md` → `docs/funnelsgrove/steps/form_input.md`.
- **Headline:** "**Achieve your goals** with the 12min App." (first phrase highlighted).
- **Subtitle:** "Create an account to access your personalized plan."
- **Fields:** Email input (icon-prefixed) + optional checkbox "I want to receive exclusive offers, personalized content, and updates…".
- **Proof element:** An **awards card image** (`awards.png`) sits directly below the CTA — trust stamp at the exact moment of data hand-over.
- **Value loaded / lever:** Data capture framed as *function* ("access your personalized plan"), not marketing — textbook framework Section E. Awards graphic resolves the trust gate ("where do you rank") right when the user is asked to give something.
- **Notable risk:** No validation — `handleContinue` stores `email.trim()` and advances even if empty; marketing opt-in defaults **off** (good for compliance, weaker for list growth). This is an early, hard ask (email at step 3 of 11) placed *before* most value is loaded — aggressive sequencing.
- **Branching:** None.

### Step 4 — `step-4` / plan-ready — the payoff screen
- **Headline:** "Your personal development plan *is ready!*"
- **Subtitle:** "Based on your answers, we have created a development plan with readings that will help you improve exactly where you need to."
- **Hero:** An **animated SVG growth chart** (`requestAnimationFrame`, 1800ms) that draws an upward curve from "Now" to a date **3 months out** computed live (`addMonths(today, 3)`, `formatPlanDate`), with a floating badge "**20 books / per month**".
- **Footnote:** "*To use the 12min app, you need an Android or iPhone." (sets web-to-app expectation early.)
- **Value loaded:** Future-state visualization + self-generated value (Hitchcock). The brain watches the line rise and the date populate to *its* near future and concludes "I will be transformed in 3 months" — the funnel never literally promises it.
- **Lever:** This is the big motivation refill after three ask-screens (age, book, email). Dated timeline = the "where you are today vs. 4 months from now" technique from the conversion case study, here at 3 months. Sticky Continue CTA.
- **Branching:** None.

### Step 5 — `step-5` / profile-improve-topics (multi-select topic question)
- **Progress bar appears for the first time:** label "**Profile**", 20% fill, states `['dot','active','empty','empty']`.
- **Headline:** "What Would You Like to Improve?"
- **Options (12 chips, multi-select):** Understanding Emotions, Motivation, Nutrition, Habits, Self-Confidence, Mindset, Self-Care, Fitness Life, Empathy, Dating and Marriage, Personal Finances, Creativity.
- **Value loaded:** Personalization investment — broad menu lets nearly everyone find ≥3 relevant chips, deepening the "this plan is mine" feeling. Continue is **disabled until ≥1 selected** (`canContinue`), forcing engagement.
- **Lever:** Investment escalation + commitment. Stored as `improveTopics[]`.
- **Note vs. best practice:** 12 options violates the "max 5 on first quiz question" rule — but this is mid-funnel (committed users only), where the framework allows more complexity, so it's defensible.
- **Branching:** None.

### Step 6 — `step-6` / profile-learning-concepts — give screen
- **Progress:** "Profile" 28% (`['dot','active','empty','empty']`).
- **Hero image:** `chart-pie-profile.png`.
- **Headline:** "Learn Great Concepts in Minutes, Not Hours".
- **Body:** "Read or listen to the main concepts of any book in just 12 minutes… easier to find time to put learnings into practice."
- **Value loaded:** The core mechanism / time-scarcity reframe — "12 minutes, not hours" is the product's whole wedge. Pure give-screen (no ask) refilling fuel after the step-5 effort.
- **Lever:** Anchoring (12 min vs. hours of reading) + ability-objection pre-handling ("I don't have time").
- **Branching:** None.

### Step 7 — `step-7` / patterns-positive-framing
- **Progress jumps to "Patterns" 74%, states `['dot','check','active','empty']`** — note the section label changes from "Profile" to "Patterns" and the first stop now shows a check. (Implies the quiz has multiple labeled phases.)
- **Hero:** `bunny-books.png` mascot.
- **Headline:** "Focusing on the positive aspects is a great way to motivate yourself even more."
- **Body:** "The development plan we are creating for you will include books that will teach you how to stay positive and know when it is time to move on to your next achievements."
- **Value loaded:** Emotional momentum + reinforcing that a bespoke plan is actively being built. Friendly mascot lowers threat.
- **Lever:** Poke→soothe→empower in the lightest form; keeps the "plan is being built for *you*" narrative alive.
- **Branching:** None.

### Step 8 — `step-8` / patterns-social-proof
- **Progress:** "Patterns" **100%**, states `['dot','check','check','check']` — quiz visually "complete".
- **Hero:** `pie-work-routine.png`.
- **Headline:** "Last month, our users read/listened to over **300,000 microbooks!**"
- **Body:** "Join 12min and finally make time to learn in your busy life."
- **Value loaded:** Aggregate social proof placed late (right before the goal ask and paywall), bypassing analytical skepticism with a big concrete number.
- **Lever:** Social proof + loss-aversion-tinged "finally make time" (you've been failing to; join and fix it).
- **Branching:** None.

### Step 9 — `step-9` / goal-selection (multi-select goal question)
- **Headline:** "Do you have a specific goal at the moment?"
- **Options (8, emoji + label, multi-select):** 🙋 Get a promotion · 📊 Becoming an entrepreneur · 💑 Relationship commitment · 👨‍👩‍👧 Parenthood · ✈️ Major life transition · 🤯 Mental and emotional well-being · 🏦 Financial milestone · 🏖️ Retirement planning.
- **Value loaded:** Final, deepest personal-relevance commitment — ties book summaries to a concrete life ambition. Continue disabled until ≥1 selected. Stored as `currentGoals[]`.
- **Lever:** Commitment lock-in (framework Section D) immediately before the paywall — the user has now told the product what they want, so the offer feels like the answer to their own stated goal.
- **Branching:** None. Note the progress bar is **gone** on this screen (no `TwelveMinProgress`), subtly signaling "the quiz is over, this is the finish line."

### Step 10 — `step-10` / summary-bridge (value bridge; not a paywall)
- **Contract annotation (`summary-bridge`):** `legacy-label-invalid`; exact implementation classification lives only in `docs/funnelsgrove/START-HERE.md` → `docs/funnelsgrove/steps/summary_confirmation.md`.
- **Headline:** "Become the most interesting person at the table!" — **callback to the step-1 hook**, closing the loop.
- **Subtitle:** "Based on your answers, we have created your personal development plan."
- **Hero:** `mascot-compare.png` (before/after style mascot comparison).
- **Value loaded:** Bookend / payoff reminder. Restates that the personalized plan exists, refreshes short-term memory with the original aspiration right before price appears.
- **Lever:** Consistency / completion — you started wanting to be "the most interesting person at the table," and here's your plan. No header back button. Sticky Continue → paywall.
- **Branching:** None.

### Step 11 — `step-11` / long purchasable paywall — see §4.

## 3. Branching, Experiments & Entry Points

- **Branching: none.** The funnel is 100% linear (`edgesByStepId` is a straight chain; `funnelExperiments: []`; `choiceTargetsByStepId` empty). Every Yes/No, age, topic, and goal answer routes to the same next step. `resolveConfiguredNextStep` is purely sequential. Answers are *collected* (`ageRange`, `bookInterest`, `email`, `marketingOptIn`, `improveTopics`, `currentGoals`, `selectedPlan`, `paywallTimestamp`) but never used to personalize copy or reroute — all "personalization" is asserted in static copy ("Based on your answers…").
- **Entry points (two):**
  - `default` → `step-1` (the full quiz).
  - `offer` → `step-11` (deep-link straight to the paywall). `FunnelFlow` reads `?entryPoint=`/`?entry=`. This lets paid/retargeting traffic or returning users skip the quiz and land directly on the annual offer.
- **Experiment variants:** none defined. This is a single fixed flow — a clean baseline, not an A/B harness.
- **`/manage-subscription` route** exists as a separate app page (not in the funnel sequence) for viewing/cancelling/renewing live subscriptions — see §5.

## 4. Paywall Architecture (step-11)

A single long-scroll page (`tm-paywall-shell`) with a persistent sticky CTA. Structure top→bottom:

**Header / hero block**
- Logo + headline "**Learn fast and exceed your expectations**".
- Subtitle: "Join the 12min community of over **5,274,333 people**" — oddly-specific large number = stronger social proof than a round "5M+".
- **Countdown timer:** "**00:13:50**" with "Limited time offer". (Static string in source — a *displayed* ~14-minute urgency timer, not a live countdown in this reconstruction. Note the cleverness: ~14 min ≈ one microbook of attention.)

**Pricing block — two plans, annual pre-selected**
- **Premium Annual (selected):** badge "**40% OFF**", crossed-out "US$ 4.98/mo" → "**US$ 2.98/mo**", "Unconditional 7-day guarantee period". Radio shown selected by default (`is-selected`).
- **Premium Monthly (secondary, deselected):** "US$ 11.77/mo", "Unconditional 7-day guarantee".
- **Per-day-style framing via /mo on an annual plan:** quoting the annual plan as a small **monthly-equivalent** ($2.98/mo) next to the genuine monthly price ($11.77/mo) makes annual look ~4x cheaper per unit — strong anchoring. Decoy/anchor pattern: the monthly plan exists mainly to make annual obvious.

**Guarantee timeline box** (under the annual plan)
- "How the guarantee works:" → **Today** ("Start enjoying everything… request a refund within 7 days") → **Day 5** ("We send a reminder that your guarantee period is ending") → **Day 7** ("Last day to request your refund").
- This is a risk-reversal *and* a trial-mechanics explainer in one — the Day 5 reminder explicitly pre-empts the "I'll forget and get charged" fear, which paradoxically increases trust and conversion.

**FAQ accordion** (secretly-sells objection handling)
- 6 items, first ("What is 12min?") **expanded by default** (`useState('what-is')`) so the value definition is always visible. Only that one has answer copy in source; the rest (guarantee, change plan, premium access, cancel during trial, contact) are question-only stubs in this reconstruction.
- Single-open accordion (`setExpandedFaqId(isExpanded ? '' : faq.id)`).

**Footer:** physical address (Belo Horizonte/MG, Brazil) + "About • Terms of Use" — legitimacy/trust signals.

**CTA mechanics:** sticky "Continue" button (`tm-paywall-sticky-cta`). On click, `handleContinue` sets `selectedPlan='annual'` and `paywallTimestamp` — it **hard-codes annual regardless of which plan radio is shown**; there is no interactive plan toggle wired up (the monthly card is display-only). No Apple Pay / Google Pay button present.

**Against the paywall best-practice checklist:** Has hero, pricing (with crossed-out price + best-value highlight), guarantee, social-proof number, urgency timer, FAQ, company info. **Missing:** before/after transformation visuals, named testimonials/success story, repeated pricing block lower down, and wallet payment. Pricing is shown only once (best practice says ~3×).

## 5. Upsell / Downsell / Cancellation Flow

- **In-funnel upsell/downsell/checkout-exit downsell: none.** The funnel terminates at step-11; there is no post-purchase upsell step, no checkout modal, no exit-intent down-sell offer, and no second discounted offer on close. The "checkout pop-up down-sell" pattern from best practices is absent.
- **Cancellation:** handled outside the funnel by the standalone `/manage-subscription` page (`src/app/manage-subscription/page.tsx`). It lists active subscriptions and exposes plain **Cancel** / **Renew** buttons via `apiService.updateSubscription`. There is **no retention/save flow** — no "are you sure", no pause option, no win-back discount, no reason survey. Cancellation is frictionless (good for compliance/trust, a missed retention opportunity commercially).
- **Trial→paid mechanics** are communicated only via the paywall guarantee timeline (Today / Day 5 reminder / Day 7), not enforced in code here.

## 6. High-Performance Techniques Observed

1. **Perfect expectation match.** Step-1 headline = the literal ad promise ("most interesting person at the table"), and step-10 calls it back verbatim — a clean open-loop/close-loop bookend.
2. **Tap-to-advance first question.** Age cards both answer and progress with no Continue button → the lowest-possible-friction first commitment, while doing useful segmentation.
3. **Time as the hero value, repeatedly.** "3-MINUTE QUIZ" (step-1), "12 minutes, not hours" (step-6), ~14-min offer timer (step-11). For a busy-professional audience, the entire pitch is *time*, and it's anchored everywhere.
4. **Self-generated future state.** Step-4's animated curve + live-computed 3-month date lets the user's brain conclude the transformation rather than being promised it (Hitchcock principle), with a "20 books/month" anchor.
5. **Progress-bar theatre.** Two named phases ("Profile" then "Patterns"), with the second reaching 100% and three checkmarks at step-8 — manufacturing a sense of completion and sunk-cost before the goal question and paywall.
6. **Social proof escalated and late-placed.** Awards (step-3) → "300,000 microbooks last month" (step-8) → "5,274,333 people" (step-11), with the biggest, oddly-specific number adjacent to the price.
7. **Commitment lock-in right before price.** Step-9 goal selection forces the user to state a personal ambition immediately before the offer, so the subscription reads as the answer to *their* goal.
8. **Annual default + monthly-equivalent anchoring.** Annual pre-selected, priced per-month ($2.98/mo) beside true monthly ($11.77/mo) with a 40%-OFF badge and strikethrough.
9. **Guarantee-as-timeline.** The Today/Day 5/Day 7 box doubles as risk reversal and forgot-to-cancel insurance, defusing the #1 trial objection.
10. **Deep-link `offer` entry point** straight to the paywall for warm/retargeting traffic.

## 7. Notable Copy & Microcopy Tricks

- **"3-MINUTE QUIZ"** kicker — frames the whole funnel as cheap and finite up front.
- **"…access your personalized plan"** — email framed as a key to *your* asset, not a signup.
- **"is ready!"** (italic emphasis) — implies work was already done *for* the user; ownership/sunk value.
- **"…improve exactly where you need to."** — vague-specific personalization claim that feels tailored without committing to anything.
- **"Learn Great Concepts in Minutes, Not Hours"** — the core anchor compressed into a headline.
- **"…finally make time to learn in your busy life."** — light guilt ("you haven't") immediately resolved by the join CTA.
- **"Unconditional 7-day guarantee"** — the word *unconditional* removes the "what's the catch" reflex.
- **"Limited time offer" + 00:13:50** — urgency sized to feel real (minutes, not days) and thematically on-brand (~one microbook).
- **"over 5,274,333 people"** — precise count reads as a real database export, not marketing rounding.
- **Default-open "What is 12min?" FAQ** — the value definition is never hidden behind a tap.
- **Physical street address in footer** — quiet but strong legitimacy signal on the money screen.

## 8. Weaknesses / Risks / Things to Avoid

- **Email asked too early (step-3 of 11), before value is loaded** and with no input validation — empty/garbage emails advance. High drop-risk at a hard ask placed before the step-4/6/8 value reveals.
- **Plan selector is non-functional.** The monthly card is display-only; the radio can't be toggled and `handleContinue` always sets `selectedPlan='annual'`. Users who *want* monthly have no path — and CTA doesn't navigate to a checkout in this reconstruction (only sets answers).
- **Personalization is theatrical, not real.** Six answer sets are captured but never alter copy or routing. "Based on your answers, we created your plan" is identical for everyone — fine until a user notices, then trust erodes.
- **Static / possibly misleading urgency timer.** "00:13:50" is a hard-coded string, not a live or per-session countdown — if it never moves (or resets on reload) it reads as a fake-scarcity dark pattern; a compliance/trust risk.
- **Paywall missing proven closers:** no before/after, no named testimonials/success story, no repeated pricing block lower in the scroll, and **no Apple Pay/Google Pay** (best practices peg wallet pay at +10-15%). Pricing shown only once.
- **FAQ is mostly stubs** — 5 of 6 questions have no answer copy, so the "FAQ secretly sells" lever is half-built.
- **No recovery layer at all:** no checkout-exit downsell, no abandonment capture, and a frictionless `/manage-subscription` cancel with no save/retention/win-back flow.
- **No back button on entry, summary, or paywall** — intentional for momentum, but removes a correction path if a user mis-taps the first age card.
- **Step-5 shows 12 options** vs. the "max 5 on opening" guidance — acceptable mid-funnel, but worth A/B testing a trimmed set.
- **Heavy emoji use on step-9 goals** can read as low-trust on a screen that's doing serious commitment work right before the price.
