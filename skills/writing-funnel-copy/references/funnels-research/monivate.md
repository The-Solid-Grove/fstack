# Monivate Funnel — Research Notes

> Source: `funnels/rag-catalog/monivate` — `src/steps/step-01.tsx` … `step-14.tsx` via shared `MonivateUi.tsx` primitives.

## 1. Overview

**Vertical (confirmed):** Personal-finance / investing-literacy education. Monivate sells a subscription to a "personalized wealth-growth plan" — structured lessons that turn a curious beginner into a "Confident Investor." It is *not* a get-rich product; the copy is careful to position it as an education/skills product (see the explicit disclaimer "it's not a guarantee or a promise of result" on the paywall). This is the money/finance + motivation hybrid the name implies ("Mon"-ey + moti-"vate").

**Audience (from `PRODUCT_SENSE.md` + copy):** Adults early in their financial-literacy journey, curious about investing, passive income, and practical personal finance. Mobile web first (viewport hard-set to 390×844 in `funnel.config.ts`).

**Entry promise:** Ads promise a *tailored* wealth-growth plan and "a clear path to become a confident investor." Screen 1 honors this immediately with "Let's Create Your Wealth Growth Plan."

**Shape:** A clean **14-step linear quiz-to-paywall**. No branching, no experiments wired, no post-purchase upsell/downsell steps inside the funnel. The whole flow is a single value-accumulation ramp that dumps the user onto one long-form paywall (`step-14`).

**Tech structure:**
- `src/config/funnel.sequence.ts` — flat array `step-1` … `step-14`.
- `src/config/funnel.routing.ts` — every step has a single `{ type: 'route', to: next }` rule. `choiceTargetsByStepId` is **empty `{}`** and `funnelExperiments` is **empty `[]`** — so there is zero per-answer divergence.
- `src/config/funnel.steps.ts` / `funnel.manifest.ts` — manifest with step `type`/`name` metadata.
- Steps are **real source files** in `src/steps/step-01.tsx … step-14.tsx` (not re-exports). All render through shared primitives in `src/components/shared/MonivateUi.tsx` and CSS module `styles/shared/monivate.module.css`.
- Answers are written to a flat attribute bag via `useFunnel().setAttribute(key, value)` (helper `useMonivateSingleSelect`). None of the captured attributes are ever read back to alter routing or copy — personalization is **theatrical, not data-driven** (see §8).

**Brand/visual:** Vibrant purple (`#8d34ff` accent), high-contrast white cards, emoji as low-cost emotional signal, green = "good/goal", orange/red = "current/weak."

**Progress illusion:** The progress header shows "**N / 24**" with a percent, but the funnel is only **14 screens** and most screens have no progress bar at all. Step 3 says "3 / 24" (12.5%), step 9 says "20 / 24" (79%). The denominator 24 is fictional — it makes each tap feel like more progress than it is and undercounts how close the paywall is.

---

## 2. Step-by-Step Walkthrough

### step-1 — Gender (`intro_hero`, name `gender`)
- **Headline:** "Let's Create / Your Wealth Growth Plan" · subtitle "Select your gender:" · header eyebrow "Welcome to Quiz!"
- **Options:** Male / Female (2 image cards). Writes `gender`.
- **Value loaded:** Expectation match — repeats the ad's "wealth growth plan" promise within the first 3 seconds. The choice is effortless (near-100% answerable), giving the first micro-commitment.
- **Lever:** Investment escalation (start with the easiest possible tap) + commitment bias. Legal links (Terms, Privacy, Subscription Terms, About) sit under the fold — quietly resolving the "is this a scam / subscription trap" trust gate without drawing attention.
- **Branching:** None — always → step-2.

### step-2 — Age range (`intro_hero`, name `age-range`)
- **Headline:** "Let's optimize your plan according to your age"
- **Options:** 18-25 / 26-35 / 36-45 / 46+ (image cards). Writes `ageRange`.
- **Value:** Reinforces "your plan is being personalized." Word "optimize" implies a tuning engine behind the scenes.
- **Lever:** Sustained low-effort investment; the "optimize … to your age" framing seeds the Hitchcock idea that the result is computed *for them*.
- **Branching:** None → step-3.

### step-3 — Primary financial goal (`progress_interstitial`, name `goal-priority`)
- **Progress:** "About you · 3 / 24 · 12.5%" (first appearance of the progress header + back button).
- **Headline:** "What is your goal?" · subtitle "Please select **the most important** one:"
- **Options (single-select list w/ icons):** Financial independence / Early retirement / Grow wealth / Passive income / Other. Writes `primaryGoal`.
- **Value:** Activates the user's *higher-level value* (the emotional destination). Forcing "the most important one" makes them name their deepest motivation — which the paywall later promises to deliver.
- **Lever:** Self-identification / commitment. 5 options = within the "max 5 on first real question" best-practice.
- **Branching:** None → step-4. (Note: despite naming a goal, the funnel never adapts to it.)

### step-4 — Desired annual income (`progress_interstitial`, name `income-target`)
- **Progress:** "About you · 5 / 24 · 20.83%" (jumps from 3 to 5 — invisible "questions" inflate progress).
- **Headline:** "Your desired annual income level is"
- **Options (2-col compact grid):** $50.000 / $100.000 / $150.000 / $200.000 / $250.000 / $350.000 or more. Writes `desiredIncome`.
- **Value:** **Future-value anchoring.** Getting the user to *pick a big number* plants a concrete dollar target that the later projection chart and paywall meters implicitly promise to move toward. The number is self-generated, so it's their own aspiration, not Monivate's claim.
- **Lever:** Hitchcock self-generated value + aspiration anchoring.
- **Branching:** None → step-5.

### step-5 — Saving habit (`single_step_choice_emoji`, name `saving-habit`)
- **Progress:** "Financial mindset · 11 / 24 · 45.83%" (big jump 5→11).
- **Headline:** "Is saving money a habit for you?"
- **Options (emoji cards):** 💸 "I do not save money" / 💵 "I've tried to save but it didn't work for me" / 💰 "I save only if I want to buy something" / 💎 "I'm saving all the time". Writes `savingHabit`.
- **Value:** Light **problem activation / guilt poke** — most users will pick a self-critical answer ("tried but it didn't work"), priming the pain the product relieves. New section label "Financial mindset" acts as a pattern interrupt.
- **Lever:** Poke (guilt) — but note there is **no immediate soothe** beat (framework would flag this). Emoji do the emotional softening.
- **Branching:** None → step-6.

### step-6 — Learning topics (`multi_select_choice`, name `interest-topics`)
- **Progress:** "Learning program · 13 / 24 · 54.17%".
- **Headline:** "I am interested in..." · subtitle "Please specify a few"
- **Options (11 chips, multi-select):** Trends, Stocks, Crypto, Market Analysis, Forex, Bonds, Real Estate, Passive income, Commodity, Budgeting, Risk Assessment. Writes `learningTopics[]`. Continue disabled until ≥1 selected.
- **Value:** Builds the *contents* of "your personalized learning plan" in the user's head — every chip they tap is a feature they now feel the product owes them.
- **Lever:** Investment escalation (more effort now that only committed users remain) + self-generated feature list. New section "Learning program" reframes from diagnosis to product.
- **Branching:** None → step-7.

### step-7 — Asset interests (`multi_select_choice`, name `asset-interests`)
- **Progress:** "Learning program · 15 / 24 · 62.5%".
- **Headline:** "I'm interested in assets of..." · subtitle "Please specify a few"
- **Options (12 branded logo chips):** Pfizer, Visa, Nvidia, Apple, Walmart, Ethereum, Google, Microsoft, McDonald's, Meta, Bitcoin, Netflix. Writes `assetInterests[]`. Continue disabled until ≥1.
- **Value:** **Borrowed credibility / trust transfer** — surrounding the product with blue-chip and famous-crypto logos makes Monivate feel legitimate and concrete ("I'll learn to invest in *Apple*, *Bitcoin*"). Tangible, recognizable assets bypass System-1 skepticism.
- **Lever:** Social proof / authority by association; deeper personal investment.
- **Branching:** None → step-8.

### step-8 — Wealth-growth potential summary (`summary_confirmation`, name `results-summary`) — KEY GIVE-SCREEN
- **Header eyebrow:** "Your Result: Awesome!🔥" · centered brand.
- **Headline:** "Your **wealth-growth** potential summary"
- **Content:** Animated **Readiness Score ring counting up to 83.9** (animates +2.4 every 28ms), a smiling photo pointing at the ring, and a 4-bar chart: Knowledge **5.3/10** (red), Income **6.5/10** (orange), Motivation **8.3/10** (yellow), Mindset **8.9/10** (green). Sticky "Continue".
- **Value:** The first big **fuel refill** after 5 ask-screens. The bar design is deliberate: **Mindset/Motivation high, Knowledge low** → "you have the drive, you're just missing the *knowledge* — which is exactly what we sell." It validates the user (ally) while opening the precise gap the product fills.
- **Lever:** Confirmation + validation ("you're Awesome"), Hitchcock (the count-up animation feels *calculated from their answers*), and a manufactured "knowledge deficit" that motivates purchase. The 83.9 number is **hard-coded** and reused verbatim on the paywall.
- **Branching:** None → step-9.

### step-9 — Daily time commitment (`progress_interstitial`, name `time-commitment`)
- **Progress:** "Learning program · 20 / 24 · 79.17%".
- **Headline:** "Show your commitment to achieve your goal!" · subtitle "I'm ready to spend..."
- **Options:** 5 / 10 / 15 / 20 min/day, plus a full-width "1 hour/day". Writes `dailyCommitment`.
- **Value:** **Commitment screen** (consistency bias). Framing it as "*show your commitment*" makes selecting a time feel like a personal pledge. Even "5 min/day" is a yes; the layout nudges toward the smaller, easy-to-agree numbers while the standout 1-hour option flatters ambitious users.
- **Lever:** Consistency/commitment bias + low-friction goal confirmation.
- **Branching:** None → step-10.

### step-10 — Final confidence check + analysis loader (`intro_hero`, name `final-question-investing-confidence`)
- **Header eyebrow:** "You're almost there!" · back button.
- **Headline:** "Tailoring your plan to growing wealth..." with two **analysis progress lines**: "Analysing your goals 100% ✓" and "Gathering skills to improve" animating 0→30%.
- **Question card:** caption "To move forward specify" → "Are you good with investing and stock trading?" with **No / Yes** buttons. Writes `investingConfidence`.
- **Social proof:** ★★★★★ "1.1 million people choose us".
- **Value:** Loader = priming real estate ("the system is building *your* plan"). The question is a clever trap: **either answer sells the product** — "No" = you need us; "Yes" = you'll love advanced lessons. The 30% stall implies "there's more plan to unlock if you continue."
- **Lever:** Hitchcock (live "analysis"), social proof (1.1M), and a no-lose binary.
- **Branching:** None — both Yes and No → step-11 (the answer changes nothing).

### step-11 — Email capture (`multi_select_choice`, name `email-capture`) — DATA CAPTURE
- **Header eyebrow:** "You're almost there!" · back.
- **Headline:** "Please enter your email to get your individual plan to growing **your wealth!**" · subtitle (above title) "Just one more thing left ..."
- **Fields:** Email input (pre-filled placeholder `tsarmari@solidgrove.ai` — a dev artifact, see §8), tappable **domain-suggestion chips** (@gmail / @yahoo / @hotmail / @outlook / @icloud) that auto-complete the address, an opt-in checkbox "I would like to receive tips, how-to and other information from Monivate via email 📫", reassurance "We respect your privacy. No spam, we promise 🤞", and Continue (disabled until value contains `@` and `.`). Writes `email`, `emailOptIn`.
- **Value:** Email framed as the **key to unlock the result** ("enter your email to *get* your individual plan"), not as marketing. The domain chips slash typing friction at the highest-drop-off moment.
- **Lever:** Data capture as a value gate + friction removal + privacy soothe.
- **Branching:** None → step-12.

### step-12 — Industry-news opt-in (`intro_hero`, name `industry-news-opt-in`)
- **Header eyebrow:** "You're almost there!"
- **Headline:** "Do you want to receive emails with the **latest industry** trends?" + envelope illustration.
- **Options:** Primary button "Yes, I'm up to it!" / secondary text link "Industry news isn't my priority". Writes `industryNewsOptIn`.
- **Value:** A second, lower-stakes yes after the email yes (foot-in-the-door escalation). Both paths advance; this exists mainly to harvest a marketing-consent flag and to keep yes-momentum.
- **Lever:** Commitment laddering; the secondary option is styled as a de-emphasized text link (decoy-style nudge toward "Yes").
- **Branching:** None → step-13.

### step-13 — Individual plan preview (`summary_confirmation`, name `individual-plan-preview`) — FUTURE-STATE PROJECTION
- **Header eyebrow:** "You're almost there!"
- **Headline:** "Your individual plan to growing **your wealth**!" · subtitle "Based on your answers you have a chance to gain the necessary skills to grow your wealth and become" → big badge "**Confident Investor**" → "**by April, 2026**".
- **Chart:** SVG growth curve from a "Now" marker up to a "Your Goal" marker across a **dated timeline (Feb / Mar / Apr / May)**.
- **Value:** The **dated future-state projection** — the single strongest pre-paywall device. It converts the abstract goal into a concrete *destination with a deadline* ("Confident Investor by April 2026"), and the rising curve makes the transformation feel inevitable and already underway.
- **Lever:** Future pacing + date-based timeline (mirrors the case-study "where you are today vs. 4 months out" tactic). "Based on your answers" sells personalization even though the curve is static. Note the careful "you have a *chance* to" hedge.
- **Branching:** None → step-14 (paywall).

### step-14 — Paywall (`paywall_offer`, kind `paywall`, name `paywall`) — see §4.

---

## 3. Branching, Experiments & Entry Points

- **Per-answer branching:** **None.** `choiceTargetsByStepId = {}`; every step uses a hard `{ type: 'route', to: next }`. Yes/No on step-10 and Yes/No on step-12 both fall through to the same next step. All answers are stored but never routed on.
- **Experiments:** **None active.** `funnelExperiments = []` in both `funnel.routing.ts` and `funnel.config.ts`. The routing engine *supports* experiment variants (`ExperimentRouteRule`, `resolveExperimentVariantKey`, traffic-percent variants) but none are configured. This is scaffolding for future A/B tests, not live splits.
- **Entry points (`funnelEntryPoints`):**
  - `default` → `step-1` (source hints: `web`, `default`, `monivate`) — the normal ad entry.
  - `paywall` → `step-14` (source hints: `paywall`, `checkout`) — a **direct-to-paywall deep link**, used for returning/retargeted traffic or "skip the quiz" links. Runtime can also be locked to the initial step (`lockToInitialStep`).
- **Runtime resolution:** `resolveRuntimeInitialStepId` honors a requested step id from the URL (`/[stepId]`) but falls back to `step-1` if invalid. So any step is directly addressable by path, but only `step-1` and `step-14` are blessed entry points.
- **Conditional copy/UI:** None driven by answers. The only "conditional" UI is cosmetic: animated counters (step-8 score, step-10 loader) and disabled-until-valid Continue buttons (steps 6, 7, 11).

---

## 4. Paywall Architecture (step-14)

A single long, scrollable paywall card. Top-to-bottom:

1. **Sticky purple hero header:** brand mark + "Choose your plan!" + a bright gradient **"Try Now!"** button (top-right) — an always-visible CTA shortcut. (The header CTA is decorative/no-handler in code; the real purchase button is below.)
2. **Now → Goal before/after hero image:** left "Now" = worried woman with a piggy bank; right "Goal" = confident woman in red with floating green growth bubbles **+13% / +32% / +72% / +27% / +56%**. Classic visceral transformation; the percent bubbles let the brain self-generate a return number (Hitchcock).
3. **Comparison meters:** two columns, "Now" vs "Goal," each showing **Investing Skills** and **Passive Income Potential**. Now = ~40-60% "Average"; Goal = 85-93% "🔥 High." Quantifies the gap the subscription closes.
4. **Disclaimer (small, muted):** "Everything is in your hands, it's not a guarantee or a promise of result." — compliance hedge directly under the projection.
5. **Readiness score recap:** "Your readiness score: **83.9%**" (purple) — reloads the step-8 number into short-term memory. Followed by a soft-gradient card: "Start investing right after our personalized program!"
6. **Urgency / reframe copy:** "The best day to invest was yesterday!" then "Investing is not a rocket science! Anyone can do it, and we'll show you how!" — kills the "investing is too complex / only for experts" objection.
7. **Objection-buster card:** "📊 NO need to be a Wall Street expert / 🎓 NO need for a Financial degree / 🚀 You can start with our courses!"
8. **Benefit list (features as outcomes):** "Curious about investing? Monivate makes it easy! In your personalized learning plan you'll get:" → ✓ Understand stock trends, market dynamics, and portfolio growth · ✓ Learn to take control of your finances and build habits that last · ✓ Discover practical ways to grow your wealth over time.
9. **Pricing — "Choose your plan" (2 tiers):**
   - **12 weeks:** "3 day free trial", **$0.99**, "billed weekly after trial."
   - **1 year (highlighted, "Most popular"):** **$39.99**, "$0.76/day."
   - Per-day reframing on the annual plan ($0.76/day) makes the larger price feel trivial; the weekly $0.99 "trial" anchor makes $39.99/year look like a steal.
10. **Single CTA:** **"GET PLAN NOW"** → only action is `setAttribute('selectedPlan', 'one-year')` (defaults selection to the annual plan; checkout handoff is wired via the runtime/payments SDK, not in this file).
11. **Trust row:** Visa / Mastercard / PayPal / Apple Pay pills (payment legitimacy; Apple Pay present but as a logo pill, not a one-tap wallet button — a missed best-practice, see §8).
12. **Guarantee section:** green "100% Money-Back Guarantee Policy" on a textured background — "Claim a full refund within 30 days of purchase if you do not achieve initial results and can demonstrate you followed the program." (Conditional guarantee — refund requires *demonstrating you followed the program*, which limits real exposure.)
13. **Testimonials:** "People love us 💜" + two reviews — John Welsh (★★★★★, "built real confidence in investing… finally started investing consistently") and Anna O'Neill (★★★★☆, "lessons are short and practical… a clear map instead of random advice"). The 4-star (not 5) review adds believability.

**Paywall ordering vs. best-practice:** Follows the canonical sequence well — hero/transformation → value gap → score recap → objection handling → benefits → pricing → CTA → trust → guarantee → testimonials. **Missing/weak:** no second pricing block lower down, no repeated CTA after the testimonials, no countdown timer, no FAQ, and no functional Apple/Google Pay button. CTA appears effectively once (plus the decorative header "Try Now!").

---

## 5. Upsell / Downsell / Cancellation Flow

- **In-funnel:** There are **no** `subscription-started`, upsell, downsell, or cancellation steps. The funnel terminates at `step-14`; the paywall has no `goNext` — purchase is handed to the payments runtime (`@funnelsgrove/payments`) outside these files. There is **no checkout-close down-sell modal** (the best-practice ARPU recovery layer is absent).
- **Post-purchase surface:** A standalone **`/manage-subscription`** page (`src/app/manage-subscription/page.tsx`) lists active subscriptions and offers **Cancel** / **Renew** buttons via `apiService.updateSubscription({ action })`. It shows user id, email, subscription status, period end, and "Will cancel at period end" vs "Auto-renew is active." This is a plain account-management utility — **no retention offer, no save-the-cancel discount, no cancellation survey.** A pure functional cancel, not a designed cancellation funnel.
- **Net:** Monivate is a quiz→single-paywall product. All monetization weight is on the one paywall; there is no engineered AOV expansion or churn-save layer in this template.

---

## 6. High-Performance Techniques Observed

1. **Expectation match on screen 1** — "Let's Create Your Wealth Growth Plan" repeats the ad promise instantly; the gender tap is a zero-effort first commitment.
2. **Self-generated future value (Hitchcock), twice anchored** — user picks their *own* desired income ($50k–$350k, step-4) and their *own* deepest goal (step-3); the paywall's green +13/+32/+72% bubbles and Now→Goal meters let the brain compute its own ROI. Monivate never states a dollar promise.
3. **Manufactured knowledge deficit (step-8)** — the readiness bars are tuned so Mindset/Motivation are high and *Knowledge* is low, framing the product as the one missing piece. Validating ("Awesome!🔥 83.9") while opening a precise gap.
4. **Animated "calculation" theater** — count-up score ring (step-8) and the "Analysing your goals 100% ✓ / Gathering skills 30%" loader (step-10) make a static result feel computed from the user's answers.
5. **Dated future-state projection (step-13)** — "Confident Investor **by April 2026**" over a Feb–May rising curve. Concrete destination + deadline = the strongest single pre-paywall device, matching the case-study "dated timeline beats static before/after" finding.
6. **Inflated progress denominator (N/24 over 14 real screens)** — every tap reads as more progress than it is, and the paywall arrives "sooner" than the 24-count implies.
7. **Commitment laddering** — name a goal → name income → "show your commitment" time pledge (step-9) → email yes → industry-news yes (step-12). Each yes makes the next easier and dropping off feel wasteful.
8. **No-lose binary question (step-10)** — "Are you good with investing?" sells the product on both Yes and No.
9. **Borrowed credibility (step-7)** — wrapping the product in Apple/Nvidia/Bitcoin/Visa logos transfers blue-chip legitimacy onto an unknown brand.
10. **Friction kill at the worst drop-off point** — tappable email-domain chips (step-11) remove typing at the data-capture gate.
11. **Per-day price reframing** — annual $39.99 shown as "$0.76/day"; $0.99 weekly trial anchors the comparison.
12. **Objection pre-emption on the paywall** — "NO Wall Street expert / NO Financial degree," "not rocket science," conditional money-back guarantee — directly answers the audience's known fears (too complex, only for experts, refund safety).
13. **Believability via imperfection** — one testimonial is 4 stars, not 5.

---

## 7. Notable Copy & Microcopy Tricks

- **"Welcome to Quiz!"** eyebrow on step 1-2, then **"You're almost there!"** repeated on steps 10/11/12 — a persistent "nearly done" nudge through the highest-friction stretch (email + opt-ins).
- **"the most important one"** (step-3) bolded — forces a single highest-emotion goal rather than a low-commitment multi-pick.
- **"optimize your plan according to your age"** / **"Tailoring your plan to growing wealth…"** / **"Based on your answers…"** — relentless personalization language over content that never actually personalizes.
- **"Show your commitment to achieve your goal!"** (step-9) — reframes a boring time question as a pledge (consistency bias).
- **"Just one more thing left …"** above the email title (step-11) — minimizes the perceived ask at the data gate.
- **"We respect your privacy. No spam, we promise 🤞"** — emoji-softened privacy soothe right where trust dips.
- **"Industry news isn't my priority"** as the decline label (step-12) — a self-labeling opt-out that's mildly unflattering, nudging "Yes."
- **"The best day to invest was yesterday!"** — loss-aversion / urgency without a fake timer.
- **"Investing is not a rocket science! Anyone can do it, and we'll show you how!"** — collapses the core objection in one line; the "NO need to be a Wall Street expert / NO Financial degree" trio reinforces it.
- **"you have a *chance* to … become Confident Investor"** and the muted **"it's not a guarantee or a promise of result"** — careful compliance hedging woven into aspirational copy (finance vertical).
- **Emoji as cheap emotional carriers** throughout: 💸💵💰💎 (saving-habit ladder), 🔥 (result/goal heat), 💜 (testimonials), 📊🎓🚀 (objection card), 📫🤞 (email reassurance).
- **Conditional guarantee wording:** "if you do not achieve initial results **and can demonstrate you followed the program**" — sounds generous, limits actual refund exposure.

---

## 8. Weaknesses / Risks / Things to Avoid

1. **Personalization is fake.** Every captured attribute (`gender`, `ageRange`, `primaryGoal`, `desiredIncome`, `savingHabit`, `learningTopics`, `assetInterests`, `dailyCommitment`, `investingConfidence`) is stored and **never read back**. The score (83.9), bars, "Confident Investor by April 2026," and paywall meters are **hard-coded for every user**. The repeated "based on your answers" claims are unbacked — a QA/honesty risk and a missed lift opportunity (real adaptive feedback is a documented +7%).
2. **Dev artifact shipped to users:** step-11 pre-fills the email field with `tsarmari@solidgrove.ai`. A real user can tap Continue and submit a stranger's/dev's address. Should be an empty field with a placeholder. **Flag for fix.**
3. **No real Apple/Google Pay button.** Apple Pay appears only as a static trust *pill*; the best-practice one-tap wallet button under the price options (documented +10-15%) is absent.
4. **CTA under-repeated on a long paywall.** Effectively one real purchase button ("GET PLAN NOW"); no repeated CTA after testimonials, no second pricing block, no FAQ, no timer. The paywall is long but only closes once.
5. **No checkout-close down-sell and no cancellation-save flow.** No ARPU-recovery modal on checkout abandon; `/manage-subscription` cancels with zero retention offer or exit survey. Pure leakage.
6. **Guilt poke without soothe (step-5).** "I do not save money / tried but it didn't work" applies negative self-judgment with no immediate reassurance beat — risks burning fuel for sensitive users.
7. **Progress denominator is dishonest (N/24 over 14 screens).** Effective as a nudge but inconsistent (jumps 3→5→11→13→15→20) and could read as buggy; also no progress bar on the hero/summary screens, so the "/24" only appears intermittently.
8. **Misleading manifest `type`s.** Several steps are typed `multi_select_choice` (e.g. step-11 email capture, which is really a form) — analytics/QA keyed off `type` would misclassify them.
9. **Pricing clarity gap.** Two plans with mismatched framing — "12 weeks / 3-day trial / $0.99 billed weekly" vs "1 year / $39.99 / $0.76/day". The weekly-billed-but-labeled-"12 weeks" tier is confusing and a potential compliance/refund-dispute trigger if the recurring weekly charge isn't crystal clear at checkout.
10. **Thin, unverifiable proof.** "1.1 million people choose us" and two generic testimonials with stock-style avatars; no app-store rating, download count, press, or methodology/authority block (a documented finance-vertical trust lever left on the table).

---

### Summary of standout techniques (5 lines)
1. Twin Hitchcock anchors — user picks their own desired income *and* deepest goal early, then the paywall's green +13/+32/+72% bubbles and Now→Goal meters let the brain self-generate the ROI Monivate never promises.
2. Manufactured knowledge deficit: the step-8 readiness bars are rigged high on Mindset/Motivation and low on Knowledge, framing the product as the single missing piece while flattering the user ("Awesome! 83.9").
3. Dated future-state projection ("Confident Investor by April 2026" over a Feb–May rising curve) plus animated "Analysing your goals 100% ✓" theater make a fully hard-coded result feel computed from the answers.
4. Commitment laddering + a no-lose binary ("Are you good with investing?" sells on both Yes and No), an inflated N/24 progress count, and per-day price reframing ($39.99/yr → $0.76/day) carry intent into the single long paywall.
5. Biggest gaps to avoid copying: personalization is purely theatrical (no captured answer ever changes routing/copy), a dev email is pre-filled in the capture field, and there's no functional wallet button, checkout down-sell, or cancellation-save layer.
