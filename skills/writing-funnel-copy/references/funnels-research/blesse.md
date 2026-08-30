# Blesse Funnel — Research Notes

> Source: `funnels/rag-catalog/blesse` — `src/steps/step-01.tsx` … `step-09.tsx` plus shared UI in `src/steps/blesse-ui.tsx`.

> **Reference mode: `step-structure-only`.** This teardown is copy, visual, and interaction research—not current FunnelsGrove contract guidance. Do not copy its `type`/`kind`, answer writes, routing, shell/controller, helpers, or analytics; implementation must follow the synced project's `AGENTS.md` and `docs/funnelsgrove/START-HERE.md`.

## 1. Overview

**Vertical:** Faith / Christian spirituality. The product is "Perfect Prayer" by Blesse — a *personalized Christian prayer-and-Bible-reading book* generated from the user's quiz answers. This is a faith-flavored variant of the standard "personalized book" quiz-to-paywall pattern (think astrology/self-help personalized-book funnels, ported to a Christian devotional audience).

**Source of truth confirming the vertical:**
- `rag.meta.json`: `domainTags: ["faith","spirituality","self-improvement","book-paywall"]`, `domainIntent: "Personalized Christian prayer-book onboarding and conversion flow"`, `brandTerms: ["Blesse","Perfect Prayer"]`, `qualityScore: 0.95`.
- `PRODUCT_SENSE.md`: Target = "Mobile users in the United States and similar English-speaking markets who want more structure in prayer life, stress relief, and daily faith routines." Traffic promise = "Get a personalized prayer book crafted for your needs and spiritual goals." Single-product paywall.
- `funnel.config.ts` meta title: "Blesse - Perfect Prayer Funnel"; viewport `390 × 780` (mobile-first).

**Shape:** 9 sequential screens, mobile viewport, single linear path. Steps are quiz → value-loading interstitials → fake "generation" loader → personalized result → cover personalization → one long-form scrolling paywall (`step-9`). The funnel is reconstructed from Figma (each step carries a `figmaNodeId`), so it mirrors a real shipped funnel screen-for-screen.

**Domain:** `info@blesse.co`. Sub-brands referenced in footer: "Perfect Prayer" and "Perfect Bible."

**Transformation arc:** Before = stressed, anxious, no prayer routine, disconnected from God, doesn't understand the Bible. After = calm, peaceful, daily routine, closer to God, owns a book "useful for the rest of your life."

**Architecture note:** Step files (`step-01.tsx` … `step-09.tsx`) are the real source — they are NOT thin re-exports. Shared UI primitives live in `src/steps/blesse-ui.tsx` (`BlesseProgressHeader`, `BlesseButton`, `BlesseArrowOption`, `BlesseRadioOption`, `BlesseInfoCard`). Styling is one shared CSS module `src/steps/styles/shared/blesse.module.css`.

---

## 2. Step-by-Step Walkthrough

### step-1 — `landing-intro` (entry with gender choice)
- **Headline:** "Personalized way to / spirituality" with product logo (`peace-logo.png`) and a user collage (`landing-collage.png`).
- **Promo bar (top):** "🎁 The Presentation of Jesus Day -70% OFF! 🎁" — anchors a discount before any price is seen; ties the offer to a liturgical calendar event for authenticity. Language selector (🇺🇸) for credibility/localization signal.
- **Benefit bullets:** "Feel closer to God / Develop a prayer routine / Find your inner peace / Understand God's word."
- **Answer options:** "Choose your gender" → **Male / Female** (`setAnswer('gender', …)`, auto-advances on tap).
- **Value loaded:** Expectation match with the ad ("personalized," "spirituality"); social proof via face collage.
- **Psychological lever:** Effortless first micro-commitment (gender = near-100% answerable, zero cognitive cost), per the investment-escalation principle. Promo bar plants loss-aversion/urgency early. Full SEO-style footer (Terms, Privacy, Contact, "© 2026 ALL RIGHTS RESERVED", "Disclaimer: results may vary") answers the trust gate (threat → "this is a legit company").
- **Branching:** none — `goNext()` → step-2. Gender is captured but never used to branch copy (missed personalization).

### step-2 — `journey-intro` (journey framing)
- **Progress header:** "Goals — 1/17 — 5.88%". Note: the funnel advertises a **17-step quiz** but only renders a handful; the progress bar is fictional pacing.
- **Headline:** "Your spiritual journey starts here!"
- **Key copy:** "We worked for five years to create [a] perfect quiz … to write [a] fully personalised prayer book **ONLY FOR YOU**." + "Remember, your answers will determine the content of this book, so be honest and read every question carefully."
- **CTA:** "Got it."
- **Psychological lever:** Effort-justification + authority ("five years"). The "be honest, read carefully" line is a classic commitment primer — it makes the user treat subsequent taps as meaningful inputs, raising perceived personalization and investment. No selling yet; pure fuel-refill / framing screen.
- **Branching:** none → step-3.

### step-3 — `primary-reason` (quiz question)
- **Progress:** "Goals — 2/17 — 11.76%". Hero illustration `reason-hero.png`.
- **Headline:** "What is your primary reason for wanting a prayer book?"
- **Answer options (single-tap arrow rows, auto-advance):**
  1. Reduce stress and anxiety
  2. Strengthen the relation with God
  3. Developing a regular practice
  4. Understand the bible better
  5. Increase focus and mindfulness
  6. Get over addiction
  7. Get over a difficult life situation
- **Value loaded / lever:** Self-segmentation; the user names their own pain (Hitchcock — they generate the problem). `setAnswer('primaryReason', …)`. Options span emotional pains (anxiety, addiction, hardship) and aspirational goals — wide net to mirror any visitor.
- **Branching:** none — every answer routes to step-4 (no per-answer divergence despite 7 emotionally distinct answers). Captured but unused for branching.

### step-4 — `daily-routine` (routine selector)
- **Progress:** "Get to know you — 4/17 — 23.53%" (note the jump from 2/17 to 4/17 — skipped/compressed steps imply a longer quiz than shown). Hero `routine-hero.png`.
- **Headline:** "What should your ideal daily routine include?"
- **Answer options (radio multi-list, default pre-selected = "Morning Prayer", explicit Continue):** Morning Prayer / Evening Prayer / Bible Verse / Mealtime Blessing / Journaling & Reflections / Bible Reading & Daily Devotional / Christian Meditation / Daily Affirmation / Bible Sleep Story.
- **Value loaded:** Daily-habit framing — the user designs their own routine, which makes the product feel like a daily companion (recurring value, not one-off). `setAnswer('idealRoutine', …)`.
- **Lever:** Pre-selected default reduces friction and nudges a "yes." Radio + explicit Continue = slightly higher commitment than step-3's auto-advance (investment escalation).
- **Branching:** none → step-5.

### step-5 — `benefits-summary` (benefit recap)
- **Progress:** "Goals — 7/17 — 41.18%".
- **Headline:** "Benefits of Your Personalized 'Perfect Prayer' Book."
- **Checklist (green check-circles):**
  - "Custom daily prayers tailored to your spiritual needs"
  - "No need for other prayer books or websites — everything's here"
  - "Stress-free way to connect with God daily"
  - "Curated Bible studies to deepen your faith"
  - "Content that will be useful for the rest of your life"
- **CTA:** "Got it."
- **Value loaded:** Value-loading give-screen (after two ask-screens). Each bullet maps a tangible value; "everything's here" handles the "I can do this free elsewhere" objection; "rest of your life" frames the price as a lifetime investment (anchoring against perceived cost).
- **Lever:** Confirmation + loss-aversion framing. Pure fuel refill.
- **Branching:** none → step-6.

### step-6 — `generation-progress` (auto-advancing generation)
- **Headline:** "We are now generating the content of your book."
- **Mechanic:** Animated circular progress ring eases from 0 → **78%** over `2400ms` (`STEP_SIX_AUTO_ADVANCE_MS`), then auto-advances (`actionBar.autoAdvanceMs`). It deliberately stops at 78%, not 100% — a perceived "almost done" tension that pulls the user forward.
- **Lever:** Labor illusion / operational transparency — the fake compute makes the personalization feel real and effortful ("System 2 sees work being done"). Builds the sunk-cost feeling: "my book is being made right now."
- **Branching:** none → step-7 (time-based).

### step-7 — `personalized-result` (personalized result recap)
- **Progress:** "Goals — 14/17 — 82.35%".
- **Headline:** "Would you look at that! Based on your preferences, we've created…"
- **Info card copy:** "We created personalized content crafted from the most powerful passages of Scripture — made just for you to feel closer to God and his peace."
- **Quantified stats (the payoff):**
  - 🙏 **1200+** Personalized Prayers
  - 📖 **140+** Selected Bible Readings
- **CTA:** "Got it."
- **Value loaded:** Hitchcock self-generated value — concrete big numbers ("1200+", "140+") let the user's brain conclude "this is substantial." First quantified proof of depth; pre-loads the paywall's content claims.
- **Lever:** Anchoring (big numbers), reward-after-effort (payoff for the quiz + loader). `goNext()` → step-8.

### step-8 — `cover-personalization` (cover form; not a paywall)
- **Contract annotation (`cover-personalization`):** `legacy-label-invalid`; exact implementation classification lives only in `docs/funnelsgrove/START-HERE.md` → `docs/funnelsgrove/steps/form_input.md`.
- **Progress:** "Personalisation — 17/17 — 100%" (quiz now "complete").
- **Headline:** "Personalise your book cover."
- **Interactions:**
  - **Cover color picker** (6 swatches: blue/black/green/pink/red/white) — live CSS `filter` recolors the `book-cover.png` preview in real time. Default = green.
  - **Name input:** "Put your name on the book" → `setAnswer('bookName', …)`.
  - **CTA:** "Continue" (`setAnswer('coverColor', …)`).
- **Value loaded:** Endowment effect / IKEA effect — the user customizes and "owns" the artifact before paying. Seeing *their* name on a real-looking cover makes walking away feel like abandoning something already theirs.
- **Lever:** Peak commitment + tangibility. This is the strongest single conversion device before the wall. `goNext()` → step-9.

### step-9 — `long-paywall` (long purchasable paywall)
A single long scrolling page (Figma `63:8271`). Sections top-to-bottom:
- **Hero headline:** "Well done, your Perfect Prayer is almost ready!"
- **Personalized cover** with overlay "**for MARI**" (hardcoded placeholder name — should bind to `bookName` from step-8; see Weaknesses).
- **CTA #1 ("Get your book")** — above the fold, tracks `paywallCtaPosition: 'top'` + timestamp.
- **"Sneak peek" content card:** "300+ Pages of tailored content for you / 1200+ Prayers based on your preferences / 140+ Selection of Bible, Scriptures readings / **97% Personalisation score**."
- **"Length of a daily practices" card:** clock icon + "Medium Length / 5 - 15 minutes" — answers the "does this fit my schedule?" objection.
- **Book-inside image** (`book-inside.png`) — product visualization.
- **CTA #2 ("Get your book")** — mid-page, tracks `'middle'`.
- **"Your mood in 3 months" chart card:** line chart from "Today" (low) to "May" (high), labels "Happy / Peaceful" — future-state visualization / before-after on an emotional axis with a dated timeline.
- **Social-proof stat card:**
  - 39% "Experienced the same triggers for stress and anxiety as you"
  - 68% "Felt that they could cope with anxiety much better"
  - 83% "Reported improvement in a sense of joy & happiness"
  - 91% "Said they feel connected to God better than ever before"
- **CTA #3 ("Get your book")** — bottom, tracks `'bottom'`.
- **Scripture verse:** "2 Kings 20:5 (NKJV) — 'I have heard your prayer, I have seen your tears; surely I will heal you.'" + priest-reading image.
- **Authority testimonial:** quote "The new God squad … it's been a blessing … grow closer to God and find the inner peace we all seek." attributed to **Fr. Peter Flant** with handwritten **signature image** + **priest portrait**.
- **Branching:** terminal screen. CTAs only record analytics (`setAnswer`) — actual pricing/checkout is delegated to the FunnelsGrove runtime/SDK; no price tiers, trial terms, or checkout modal are coded in the step itself.

---

## 3. Branching, Experiments & Entry Points

**Branching:** None active. The flow is strictly linear `step-1 → … → step-9`.
- The legacy routing config defines only sequential edges 1→2→3→…→9. `choiceTargetsByStepId` is empty (`{}`) — no yes/no per-answer routing.
- The manifest (`funnel.manifest.ts`) builds `sequentialEdgesByStepId` purely from sequence order.
- Quiz answers (`gender`, `primaryReason`, `idealRoutine`, `coverColor`, `bookName`) are all captured via `setAnswer` but **none drive routing or conditional copy.** Personalization is implied/cosmetic, not behavioral.

**Experiments:** None. `legacyFunnelExperiments = []` and no `graph.experiments` in `funnel.config.ts` (config has no `graph` key at all, so all graph parsers return empty and the legacy fallbacks apply). The routing engine *supports* deterministic-hash A/B assignment (`resolveExperimentVariantKey`, localStorage persistence per `(funnelId,userId,experimentId)`) and graph-based conditional edges via `conditionId`, but Blesse ships with the machinery dormant.

**Entry points (`legacyFunnelEntryPoints`):**
- `default` → `step-1` (`isDefault: true`, `sourceHints: ['web','default']`).
- `offer` → `step-9` (`sourceHints: ['paywall','checkout']`) — a direct-to-paywall entry, e.g. for retargeting or returning users who skip the quiz. Resolvable via `?entryPoint=offer` / `?entry=`.

**Conditional capability (unused here):** `FLOW_CONFIG_AND_ROUTING.md` documents a `cancellationRequested` condition pattern (route step-3 → step-7 when `flowIntent === "cancellation"`), but this is a template example, not wired into Blesse's live config.

---

## 4. Paywall Architecture

**Structure:** Single long-form scrolling paywall (`step-9`), preceded by a cover-personalization form (`step-8`, not a paywall). The paywall is content-and-proof heavy; the actual price/checkout UI is rendered by the FunnelsGrove SDK runtime for the purchasable screen, not hardcoded in the step.

**Above the fold:** Personalized headline ("almost ready!") + personalized cover with the buyer's name + immediate primary CTA. Matches the best-practice "hero block with CTA above the fold" rule.

**Value stack (below fold), in order:**
1. Content-depth recap (300+ pages / 1200+ prayers / 140+ readings / 97% personalization score) — reloads short-term memory with quantified value from step-7.
2. Time-fit card (5–15 min) — objection handling ("fits my schedule").
3. Product visualization (book interior image).
4. Future-state chart ("Your mood in 3 months", Today→May, Happy/Peaceful) — emotional before/after on a dated timeline.
5. "People like you" outcome stats (39/68/83/91%) — social proof placed right before the final CTA.
6. Scripture verse — vertical-specific emotional trust anchor.
7. Clergy testimonial (Fr. Peter Flant, signature + portrait) — authority proof tuned to the faith audience.

**CTA repetition:** Three identical "Get your book" buttons (top / middle / bottom), each tagged with `paywallCtaPosition` and `paywallCtaClickedAt` — instrumented to learn which scroll depth converts. Matches "repeat CTA at every major section."

**Discount/urgency:** Carried from step-1's "Presentation of Jesus Day -70% OFF" promo bar — an earned/event-based discount the user has seen since screen 1 (the loss-aversion anchor persists into the wall).

**Gaps vs. best-practice paywall checklist:** No visible price tiers, no per-day price breakdown, no crossed-out anchor price in the step code, no explicit money-back guarantee text (a `money-back-badge.png` asset exists in `public/paywall/` but is not referenced in `step-09.tsx`), no FAQ block, no Apple Pay/Google Pay row. These are presumably injected by the SDK paywall layer or simply absent from this reconstruction.

---

## 5. Upsell / Downsell / Cancellation Flow

- **Upsell / downsell:** None present. `PRODUCT_SENSE.md` confirms a "single-product paywall." No upsell or downsell step files exist; the funnel ends at `step-9`.
- **Cancellation:** No in-funnel cancellation/retention offer. There is a generic **`/manage-subscription`** page (`src/app/manage-subscription/page.tsx`) — an SDK-driven account screen that lists subscriptions and offers Cancel/Renew buttons via `apiService.updateSubscription({action:'cancel'|'renew'})`. It is a utilitarian management UI with **no save-offer, no downsell, and no retention copy** — a missed retention surface.
- **Checkout down-sell:** Not implemented in code (the best-practice "checkout-close modal down-sell" is absent).

---

## 6. High-Performance Techniques Observed

1. **Pre-applied, event-themed discount from screen 1.** "Presentation of Jesus Day -70% OFF" rides along the entire funnel — honest-feeling, calendar-anchored urgency rather than a generic timer.
2. **Effortless first commitment.** Gender tap on the landing screen = zero-cost yes that starts investment escalation; auto-advances with no Continue button.
3. **Effort-justification framing.** "We worked for five years to create [the] perfect quiz… ONLY FOR YOU" + "be honest, read carefully" turns taps into meaningful, personalized inputs.
4. **Fake generation loader stopped at 78%.** Labor illusion makes personalization feel real; the incomplete ring creates forward tension and a sunk-cost feeling ("my book is being made").
5. **Quantified Hitchcock payoff.** 1200+ prayers / 140+ readings / 300+ pages / 97% score — big concrete numbers the brain multiplies into "this is worth it," never a hard claim about outcomes.
6. **Endowment via cover personalization (step-8).** Color + name customization on a realistic cover preview makes the book feel owned before payment — the single strongest pre-wall lever.
7. **Daily-habit framing.** Routine builder (Morning Prayer, Sleep Story, etc.) positions the product as a recurring daily companion, justifying ongoing value / subscription.
8. **Emotional future-state timeline.** "Your mood in 3 months" chart (Today→May, Happy/Peaceful) — keeps focus on the transformation, not the spend.
9. **Vertical-tuned authority proof.** Scripture verse + clergy testimonial with handwritten signature and portrait — credibility currency that resonates specifically with a Christian audience.
10. **Instrumented CTA positions.** Three CTAs tagged top/middle/bottom with timestamps — built-in scroll-depth conversion analytics.
11. **Give/ask cadence.** Ask (gender) → frame → ask (reason) → ask (routine) → give (benefits) → give (loader) → give (result) → personalize → wall: motivation refills are interleaved so fuel never bottoms out.

---

## 7. Notable Copy & Microcopy Tricks

- **"ONLY FOR YOU"** (step-2) — the single all-caps phrase; exclusivity/personalization shout, used sparingly so it lands.
- **"Would you look at that!"** (step-7) — surprise/delight phrasing makes the payoff feel discovered, not delivered.
- **"No need for other prayer books or websites — everything's here"** (step-5) — kills the "I can find this free" objection inside a benefit.
- **"Content that will be useful for the rest of your life"** (step-5) — lifetime-value anchor that pre-discounts the price.
- **"Well done"** (step-9 hero) — congratulatory tone rewards the completed quiz and softens the transition to payment.
- **"Medium Length / 5–15 minutes"** framed as *selected for you* — turns a spec into personalization and answers a time objection.
- **"The new God squad"** testimonial headline — culturally warm, in-group language for the audience.
- **Progress labels segmented by phase** ("Goals", "Get to know you", "Personalisation") rather than a bare bar — narrative pacing that makes 17 steps feel purposeful.
- **Disclaimer "results may vary from person to person"** in the footer — compliance hygiene for a sensitive wellness/faith claim set.
- **"for MARI"** overlay on the cover — personalization theater (though hardcoded here; see below).

---

## 8. Weaknesses / Risks / Things to Avoid

1. **Captured answers never personalize anything.** `gender`, `primaryReason`, `idealRoutine` are stored but never branch copy or routing. A user who picks "Get over addiction" sees the identical generic "stress and anxiety" social-proof stat (39%) on the paywall. This is the biggest missed lever — the funnel *claims* deep personalization ("ONLY FOR YOU", "97% personalisation score") but delivers none behaviorally. Risk of an expectation/reality gap that hurts trust and refunds.
2. **Hardcoded "for MARI" on the paywall cover.** `step-09.tsx` renders a literal "for MARI" instead of binding to `bookName` from step-8. A real user who typed their name sees a stranger's name on "their" book — breaks the endowment effect entirely and looks broken. High-priority QA bug.
3. **Fabricated 17-step progress.** Only ~5 quiz screens render, but the bar counts to 17 (1/17, 2/17, 4/17, 7/17, 14/17, 17/17). Skipped numbers are visible (2→4, 7→14) and could read as buggy. The padding inflates perceived effort dishonestly.
4. **No price / guarantee / FAQ in the paywall code.** No tiers, per-day breakdown, crossed-out anchor, money-back text (the `money-back-badge.png` asset is unused), Apple/Google Pay, or FAQ. If the SDK doesn't inject these, the value-vs-price comparison and risk-reversal are incomplete.
5. **Unverifiable social proof in a sensitive vertical.** The 39/68/83/91% stats and "Fr. Peter Flant" testimonial have no cited source. In a faith/wellness context this carries credibility and (in some markets) regulatory risk if fabricated. Verify provenance before reuse.
6. **No retention/save flow.** Cancellation is a bare Cancel button on `/manage-subscription` — no downsell, pause, or win-back offer. Lost LTV.
7. **No upsell/cross-sell** despite an obvious adjacent product ("Perfect Bible" appears in the footer) — leaves AOV on the table.
8. **Gender asked but visually unused**, and only binary Male/Female — a small inclusivity/relevance risk for the audience, with no payoff since it doesn't personalize.
9. **Dormant experiment + branching machinery.** The routing engine supports A/B tests and conditional edges, but nothing is configured — so none of the per-answer personalization opportunities are being tested.
