# Astroline Funnel — Research Notes

## 1. Overview

**Vertical:** Astrology + palm reading ("spiritual" trust vertical).
**Shape:** 19-step quiz → palm-scan reveal → long-form scrolling paywall. Mobile-first (locked viewport 390×780).
**Entry promise (Step 1):** "Personalized astrology report with powerful predictions" + "Complete a 1-minute quiz to get a personalized prediction."
**Core mechanic:** Collect birth data (date/time/place) → render a *personalized* zodiac chart (sun/moon/ascendant) → escalate engagement via a "Forecast accuracy" gauge (34% → 67%) → capture a palm photo → animate an AI-style "palm scan" → gate the full reading behind a trial-priced subscription.

**Source-of-truth note:** `PRODUCT_SENSE.md` and `PLAN.md` are stale generic template docs (they describe a 7-step "claim/profile/activate" template and do not match the live funnel). There is **no `rag.meta.json`**, so no domain tags/intent/quality score exist in-repo. The real content lives entirely in `src/steps/step-01.tsx … step-19.tsx`. Step files are real source (not re-export shims); each exports its own component + `makeAstrolineStepMeta`.

**Routing model (`funnel.routing.ts` + `funnel.sequence.ts`):** Strictly linear step-1 → … → step-19 via `legacyStepRouteRulesById` (each step routes to `to: next`). No conditional edges, **no active A/B experiments** (`legacyFunnelExperiments = []`, graph experiments parsed but none configured). Two entry points exist: `default` → step-1, and `paywall` → step-19 (for direct paywall traffic / re-engagement).

**Transformation arc:** Anonymous curious user ("what do the stars say about me?") → someone holding a personalized cosmic identity (signs, modality, polarity, palm scores) who feels *seen* and wants the rest of "their" story.

---

## 2. Step-by-Step Walkthrough

Progress bar denominator is **/14** (`AstrolineTopBar total=14`) even though there are 19 steps — the counter under-reports remaining effort, and the displayed step numbers are deliberately offset (e.g. step-6 shows "5", step-7 shows "6"). This makes the quiz feel shorter than it is. All steps hide the default action bar (`hideActionBar: true`) and own their own CTAs.

### Step 1 — Gender (`step-1`, single_step_choice)
- **Headline:** "Personalized astrology report with powerful predictions"
- **Sub:** "Complete a 1-minute quiz to get a personalized prediction. The result is not guaranteed and may vary from case to case." (early disclaimer = trust gate + liability hedge)
- **Question:** "Select your gender to start" — Female / Male / Non-binary (♀ ♂ ⚧ glyphs)
- **Interaction:** tapping a card *immediately* advances (zero-friction first micro-commitment; no Continue button).
- **Loads:** `gender`. **Levers:** expectation match (ad → "personalized astrology"), investment escalation (start with the easiest possible tap), trust gate (clean branded screen, ☰ menu, logo).

### Step 2 — Birthday (`step-2`, value_prop_story)
- **Headline:** "When's your birthday?" / "It's also important to know your date of birth for making complete and accurate predictions."
- **Interaction:** 3-column iOS-style scroll wheel (Month/Day/Year, default year 2001). Continue is **disabled until the user interacts** (`hasInteracted`) — forces engagement.
- **Loads:** `birthday`, `birthDate{y,m,d}`, and computes `sunSign`/`sunSignGlyph`/`sunSignElement` via `getZodiacSign`. **Levers:** micro-commitment, *self-generated value setup* (the data the user gives now becomes "their" chart later).

### Step 3 — Birth Time (`step-3`, value_prop_story)
- **Headline:** "Do you know your birth time?" / "This helps us find out where planets were placed in the sky at the moment of your birth."
- **Interaction:** Hour/Minute/AM-PM wheel + a muted escape hatch "I don't remember" (sets `birthTimeUnknown`). Reduces drop-off for users who don't know.
- **Loads:** `birthTime` or `birthTimeUnknown`. **Lever:** authority/competence cue ("planets placed in the sky") makes the product feel methodical.

### Step 4 — Birth Place (`step-4`, form_input)
- **Headline:** "Where were you born?" / "The place is important to explore your core personality traits, needs, and desires."
- **Interaction:** Text input that **auto-detects city** via browser geolocation → reverse-geocode API (`/api/location/reverse`), falling back to IP lookup; placeholder shows "Detecting your city…". Pre-filling reduces typing friction and feels "smart."
- **Loads:** `birthPlace`, `birthCity`. **Levers:** ability-cost reduction (auto-fill), perceived intelligence/personalization.

### Step 5 — Chart Mapping loader (`step-5`, progress_interstitial, autoAdvance 2300ms)
- **Headline:** "Mapping your birth chart…" with an animated twinkling constellation chart.
- **Priming chips:** "🧩 Your challenges / 🧭 Your approach to life / 🦋 Your transformations / 🌙 Your intuition and dreams."
- **Levers:** **loading screen as free priming real estate** (seeds value categories the paywall will later sell), fuel refill after 3 ask-screens. First "give" beat.

### Step 6 — Chart Snapshot (`step-6`, value_prop_story) — FIRST REVEAL
- **Speech bubble (advisor avatar):** "Your chart shows a **rare spark** — let's discover your best match" ("rare spark" = flattering cold reading).
- **Shows:** personalized Moon / Sun / Ascendant signs with glyphs (computed from birth date).
- **Loads:** `astroProfile`, `moonSign`, `ascendantSign` (+ glyphs). **Levers:** **Hitchcock self-generated value** (their own birth data produced "their" chart → they conclude it's real), confirmation ("that's me"), payoff for the data they gave. Major fuel refill.

### Step 7 — Forecast Accuracy 34% (`step-7`, value_prop_story)
- **Headline:** "Forecast accuracy" with an orb gauge reading **34%**.
- **Speech bubble:** "The cosmic energy is building up! Share a bit more to reveal what's driving you."
- **Loads:** `forecastAccuracyCheckpoint: 34`. **Levers:** **completion bias / progress mechanics** (an explicit incomplete meter creates a goal-gradient pull to finish), curiosity gap. Frames further questions as *unlocking accuracy* rather than as effort.

### Step 8 — Relationship Status (`step-8`, single_step_choice)
- **Headline:** "To get started, tell us about your current relationship status."
- **Options (tap-to-advance):** In a relationship 💕 / Just broke up 💔 / Engaged 🥰 / Married 💍 / Looking for a soulmate 💫 / Single 😌 / It's complicated 🤔.
- **Loads:** `relationshipStatus`. **Lever:** emotional personalization fuel (later reused verbatim in the step-13 advisor line). Note: no per-answer branching — answer only personalizes copy.

### Step 9 — Future Goals (`step-9`, multi_select_choice)
- **Headline:** "What are your goals for the future?" with live "Selected: N/3" counter.
- **Options:** Family harmony ❤ / Career 💼 / Health 💊 / Getting married 💍 / Traveling 🌎 / Education 🎓 / Friends 👥 / Children 👩‍🍼.
- **Interaction:** caps at 3; **auto-advances 260ms after the 3rd pick** (no Continue). Forces prioritization and keeps momentum.
- **Loads:** `futureGoals` (first 3). **Lever:** investment + value targeting (primary goal is woven into step-13 line and the paywall floating tags).

### Step 10 — Color Preference (`step-10`, single_step_choice)
- **Headline:** "Which of the following colors do you prefer?" / "The color is important for better personalization."
- **Options:** Red/Yellow/Blue/Orange/Green/Violet (color swatches), tap-to-advance.
- **Loads:** `favoriteColor`. **Lever:** low-stakes pseudo-diagnostic question — feels personalizing, near-100% completion, keeps the "this is about ME" frame. (Astrologically arbitrary; pure engagement filler styled as science.)

### Step 11 — Nature Element (`step-11`, single_step_choice)
- **Headline:** "Which element of nature do you like the best?" / "The element of nature is important for better personalization."
- **Options:** Earth/Water/Fire/Air (textured swatches), tap-to-advance.
- **Loads:** `natureElement`. **Lever:** same as step 10 — frictionless personalization, ties thematically to zodiac elements.

### Step 12 — Profile Summary card (`step-12`, summary_confirmation, autoAdvance 2200ms)
- Renders `AstrolineDetailsCard` (default content: "You" / Modality / Polarity / Moon-Sun-Ascendant traits + 🐐 orb). Auto-advances. **Lever:** anticipation/reveal pacing; a "give" beat that previews the richer card on the next screen.

### Step 13 — Profile Summary + Advisor (`step-13`, summary_confirmation)
- **Speech bubble (personalized):** "Your **{Sun} chart in {City}** shows a **rare spark for {primary goal}** — let's align it with your **{relationship}** energy." — stitches together birthday + birthplace + goal + relationship into one tailored sentence.
- **Card:** full `AstrolineDetailsCard` with traits, modality, polarity, `{Color} • {Element} Focus`, `{Gender} • {Sun} • {Element}` meta.
- **Levers:** **peak personalization payoff** (every quiz answer is mirrored back → "they really see me"), commitment bias, cold reading. Strongest pre-paywall trust moment.

### Step 14 — Forecast Accuracy 67% (`step-14`, value_prop_story)
- **Headline:** "Forecast accuracy" orb at **67%** (nearly doubled from step 7).
- **Speech bubble:** "You're close to a big reveal! Confirm one last thing and see your full story."
- **Loads:** `forecastAccuracyCheckpoint: 67`. **Levers:** goal-gradient acceleration, near-completion urgency, sets up the palm-photo ask as the final "unlock."

### Step 15 — Palm Photo Prompt (`step-15`, form_input)
- **Headline:** "Take a photo of your left palm." Animated palm frame with orbiting topic chips: 👩‍🍼 Children / 💼 Career / 💞 Marriage / ⏳ Big Change / 💸 Money.
- **Interaction:** Live camera (`getUserMedia`, environment-facing, with capture modal) OR "Upload palm photo." Uploads via `apiService.uploadTempPhoto`; **graceful local fallback** if SDK keys absent (keeps flow alive in preview).
- **Disclaimers:** "These readings are for entertainment purposes only and should not be taken as 100% accurate" + "Privacy is a priority for us. We only process non-identifiable data to ensure anonymity."
- **Loads:** `palmPhotoUrl`, `palmPhotoSource`. **Levers:** **escalated investment** (giving a photo of your body is a big commitment that makes quitting feel wasteful), the orbiting chips pre-load the exact value categories the paywall sells, trust soothe (privacy + entertainment disclaimer placed *right at* the highest-anxiety ask).

### Step 16 — Palm Scan loader (`step-16`, progress_interstitial)
- Shows the user's **own uploaded palm photo** under a scanning overlay with dots/curve, a counter animating **44 → 100**, and rotating messages: "Analyzing your palm shape… / Scanning your fingers… / Identifying lines, mounts and plains… / Generating your palm reading result…"
- **Loads:** `palmScanScore`, `palmScanSource`. **Levers:** theatrical "AI is working on YOUR data" effect; using the real photo makes the analysis feel bespoke and credible (Hitchcock — the brain fills in "it found something").

### Step 17 — Palm Reading Report + Email (`step-17`, form_input) — DATA CAPTURE
- **Preview card ("Overview"):** the user's palm thumbnail + score bars **Love 85 / Health 80 / Wisdom 78 / Career 91** and teaser copy: "Your **Heart Line** demonstrates your emotional stability…" / "Your **Life Line** suggests several challenges that can affect you in the future." (positive + a soft worry hook).
- **Sheet headline:** "Sign up to understand yourself better with Astroline" + email input.
- **Privacy line:** "🛡 Your personal data is safe with us. We'll use your email for updates, receipts, and subscription details." (frames email as functional/required, not marketing — note it pre-discloses "subscription details," priming the paywall).
- **Loads:** `email` (validated). **Levers:** value-before-ask (show the report preview, then gate it), loss aversion ("Life Line suggests challenges"), Section E data capture framed as necessity.

### Step 18 — Palm Chat Setup loader (`step-18`, progress_interstitial, autoAdvance 2200ms)
- "Setting up our Palm Reading chat…" animated hand, static 58% bar. **Loads:** `palmChatReady`. **Lever:** final anticipation beat / handoff animation right before price; implies an ongoing personalized service (a "chat" advisor) the subscription unlocks.

### Step 19 — Paywall (`step-19`, paywall_offer / kind:paywall)
See Section 4.

---

## 3. Branching, Experiments & Entry Points

- **Branching:** None functional. Routing is strictly sequential (`legacyStepRouteRulesById`, each `{type:'route', to:next}`). `choiceTargetsByStepId` is empty; there are no yes/no `goChoice` divergences. Quiz answers (`relationshipStatus`, `futureGoals`, `favoriteColor`, `natureElement`, gender, birth data) **only personalize copy/visuals** (steps 6, 13, 17, 19) — they never change the path. `birthTimeUnknown` and the upload-failure fallback are graceful escape hatches, not route branches.
- **Conditional-edge engine exists but is unused:** `resolveNextStepFromGraph` supports `edgesByStepId` with `when.conditionId` attribute checks and experiment variant routing — the infrastructure is present but the live config defines none. Easy hook point for future A/B or per-answer routing.
- **Experiments:** none active. `funnelExperiments` resolves to `[]`. The framework supports `experimentId`/variants/`trafficPercent`/`routeToStepId` with a `control` fallback, but Astroline ships zero.
- **Entry points (`funnelEntryPoints`):**
  - `default` → `step-1` (sourceHints: web, default).
  - `paywall` → `step-19` (sourceHints: paywall, checkout) — direct-to-paywall entry for returning/retargeted users. Note step-19 reads personalization from attributes and **degrades gracefully** to defaults (Capricorn sun, Scorpio moon, Libra ascendant; marriage age 27 / money age 33) when entered cold with no quiz data.

---

## 4. Paywall Architecture

Single long scrolling page (`astro-screen-scroll`), `kind: paywall`. Checkout is handled by the runtime SDK (`StripePaymentPopup` bottom-sheet), not by an in-funnel step — `handleStartTrial` just records `selectedPlanId` + `paywallTermsAccepted` and the platform opens checkout.

**Section order (top → bottom):**
1. **Hero:** "Your **{Sun}** Palm Reading **Is Ready!**" — personalized to the user's computed sun sign. Orbiting "result" card built from the user's own palm photo, surrounded by floating teaser tags: "👩‍🍼 Children / 💞 Marriage / ⏳ **Big change at {marriageAge}** / 💸 **Money success at {moneyAge}**." Ages are derived from birth date (`23 + day%8`, `28 + month%9`) so they look like specific personal predictions. CTA: **"Get My Prediction."**
2. **Pricing block** ("Unlock predictions") — 3 trial tiers:
   - 1-Week Trial **$1** (was $4.99), "then 2-Week Plan $19.99" (muted)
   - 2-Week Trial **$5.49** (was $9.99), "then 2-Week Plan $19.99" — **"Most popular"** (default selected `week-2`)
   - 4-Week Trial **$9.99** (was $19.99), "then 1-Month Plan $29.99" — **"SAVE 50%"** (muted)
   - CTA **"Start Trial and Continue"** + terms checkbox: "…Start your 14-day trial for {price}. Then continue on a recurring plan until canceled." (Note inconsistency — tiers say 1/2/4-week trial, the checkbox says "14-day trial"; see §8.)
3. **"Guaranteed safe checkout"** trust strip.
4. **Palm reading card** — user's palm photo bg + Love/Health/Wisdom/Career bars (85/80/78/91) + Heart Line / Life Line copy ("you are very passionate…" + "physical health requires hard work to improve" — poke), "More data in the full report." CTA **"Get Full Report."**
5. **Professional advisors** — avatar cluster, "Gain insights from professional advisors." (authority).
6. **Shareable card** — "This card was made for you… share it with friends or partners." (ownership/identity + viral hook).
7. **Free 2026 Astrology Forecast** — bonus stack: Full Year Overview / Major Cosmic Events / Moon Calendar 2026 / Retrogrades Explained / Zodiac Forecasts, each with ✓. CTA **"Get 2026 Forecast"** (framed as a free gift bundled with the trial).
8. **Social proof:** "**3.4 million** users worldwide use Astroline to understand themselves better."
9. **Birth chart analysis** — "Your purpose and mission / hidden talents / priorities and values." CTA "Get Full Report."
10. **Compatibility profile** — relationships value. CTA "Get Full Report."
11. **Footer:** Privacy / Terms / Billing Terms links.

**Checkout popup (`StripePaymentPopup`, runtime):** bottom-sheet titled "Select your payment method." Shows an itemized **Original price → % OFF → Total** summary (built-in anchoring/discount framing), guarantee line "30 days moneyback guarantee. Cancel anytime.", **Apple Pay / Google Pay express checkout placed above the card fields** (`StripeExpressCheckout`), a "Continue with payment" button that scrolls to card fields, then "Confirm purchase," and "Powered by stripe." Closeable (× / overlay / Esc).

**Best-practice alignment:** personalized hero/future-state ✓, pricing repeated, CTA repeated ~6×, social proof number ✓, guarantee ✓, bonus stack ✓, wallet pay above card fields ✓, anchored crossed-out prices + "Most popular"/"SAVE 50%" badges ✓. **Missing:** named testimonials / before-after stories, FAQ block, visible countdown timer, money-back badge image (asset `paywall/money-back-badge.png` exists but isn't rendered in step-19).

---

## 5. Upsell / Downsell / Cancellation Flow

- **No in-funnel subscription-started, upsell, or downsell *step* exists.** The funnel terminates at the paywall (step-19); post-purchase confirmation and any upsell are owned by the platform/runtime, not this repo.
- **Down-sell is structural, inside the checkout popup:** `StripePaymentPopup` always renders the `Original price / N% OFF / Total` ledger (`getDiscountPercent`), so every checkout *feels* discounted regardless of plan. The popup is dismissible (overlay click / × / Esc) — the standard "close-checkout → recover" hook exists structurally, though no second-offer modal is wired in this repo.
- **Express-checkout friction removal:** Apple/Google Pay surfaced first in the popup = the conversion best-practice "wallet under prices."
- **Cancellation:** handled on a **separate route** `/manage-subscription` (`apiService.getManageSubscriptions` / `updateSubscription` with `action: 'cancel' | 'renew'`). It's a plain functional dashboard (status, period end, "Will cancel at period end" vs "Auto-renew is active," Cancel/Renew buttons) — **no retention/save offer, no downsell, no "are you sure" guilt screen**. Purely transactional. Branded "App Deals," not Astroline.

---

## 6. High-Performance Techniques Observed

1. **Self-generated value (Hitchcock) is the spine.** The user supplies birth date/time/place + a palm photo; the app reflects "their" chart, signs, ages, and palm scores back. Because the user generated the inputs, they conclude the output is true — far stronger than claims. (`getPersonalizedSigns`, step-6/13/19.)
2. **Tap-to-advance on choice screens** (steps 1, 8, 10, 11; auto-advance on 9, 12, 5, 16, 18) — near-zero friction, maximizes completion, and the very first interaction (gender) is a single effortless tap.
3. **Progress gauge as a goal-gradient engine** — explicit "Forecast accuracy 34% → 67%" reframes *more questions* as *unlocking your own result*, converting effort-spend screens into anticipation.
4. **Under-counting progress** — `/14` denominator and offset step numbers on a 19-step flow make it feel shorter; the bar is near-full well before the end.
5. **Loaders as priming real estate** — the chart-mapping and palm-scan loaders seed exactly the value categories ("challenges, transformations, intuition," "lines/mounts/plains") the paywall later monetizes.
6. **Escalating investment ladder** — gender tap → wheels → text → multi-select → **body photo** → email. The photo (step 15) is a large sunk cost placed right before the price, so abandoning feels wasteful (commitment bias).
7. **Personalization compounding** — each answer is reused: relationship+goal+city+sign stitched into the step-13 advisor sentence and the paywall hero/floating tags, so the paywall reads like a personal forecast, not a generic offer.
8. **Trust gating in a low-trust vertical** — disclaimers ("entertainment only," "non-identifiable data," "privacy is a priority") are placed exactly at the highest-anxiety asks (gender start, palm photo, email), and "professional advisors" + "3.4 million users" supply authority and social proof.
9. **Anchoring everywhere** — crossed-out prices on all 3 tiers, "Most popular" + "SAVE 50%" badges, and the checkout's mandatory "Original → % OFF → Total" ledger.
10. **Auto-detected birthplace** removes typing friction and signals competence ("it already knows me").
11. **Graceful degradation** — paywall and palm steps render sensible defaults when entered cold or when uploads fail, so the `paywall` entry point and preview never break.

---

## 7. Notable Copy & Microcopy Tricks

- **"Your chart shows a rare spark"** (step-6) — flattering, unfalsifiable cold reading; every user is "rare."
- **"The cosmic energy is building up! Share a bit more to reveal what's driving you"** (step-7) — reframes the next ask as a *reward unlock*, not a chore.
- **"You're close to a big reveal! Confirm one last thing…"** (step-14) — false-finish urgency right before the heaviest ask (the photo).
- **Poke → soothe pattern in readings:** "Heart Line… emotional stability" (soothe) paired with "Life Line suggests several challenges that can affect you in the future" / "physical health requires hard work" (poke = loss-aversion hook that only the paid report resolves).
- **Specific personalized predictions from arithmetic:** "Big change at {age}" / "Money success at {age}" computed from birthday digits — *feels* like precise prophecy, technically a deterministic formula.
- **Email framed as functional:** "We'll use your email for updates, receipts, and subscription details" — necessity framing + quietly pre-announces the subscription.
- **"This card was made for you… share it with friends"** — ownership language + built-in viral loop.
- **Score precision (85/80/78/91, "34%/67%")** — oddly specific non-round numbers read as "measured," bypassing skepticism.
- **"To get started, tell us about your current relationship status"** placed at step 8 — "to get started" *after* 7 steps reframes the deepest personal question as the real beginning.

---

## 8. Weaknesses / Risks / Things to Avoid

- **Trial-term inconsistency (compliance risk):** plan tiers advertise "1-Week / 2-Week / 4-Week Trial" but the terms checkbox says "Start your **14-day** trial for {price}." Mismatched trial length on the consent line is a refund/chargeback and app-store-review liability. Fix to one consistent term.
- **Pricing logic is ambiguous:** "$5.49 then 2-Week Plan $19.99" — unclear whether $5.49 is the trial charge or per-period, and "2-Week Plan $19.99" recurrence cadence isn't spelled out next to the price. High-converting but the renewal terms are buried; regulators/Apple increasingly require explicit "then $X every Y" at the selector.
- **Predictions presented as personal fact** ("Big change at 27," "Money success at 33," accuracy %s) rest only on an "entertainment purposes only" disclaimer at step 15 — not repeated on the paywall where the strongest predictive claims appear. Consider repeating the disclaimer near paywall claims.
- **Paywall is missing proven closers:** no FAQ (objection handling), no named testimonials / before-after stories, no visible countdown/urgency timer, and the existing `money-back-badge.png` asset is not rendered despite the guarantee being referenced only in the checkout popup. The guarantee should appear *on the paywall beside a CTA*, not just inside checkout.
- **No retention layer on cancellation:** `/manage-subscription` cancels with one tap and no save offer, no downsell, no pause option — pure revenue leakage. Also branded "App Deals," breaking the Astroline brand illusion mid-relationship.
- **Quiz answers are decorative, not diagnostic:** color/element/relationship/goals never branch the flow or change the price/offer — a clear A/B opportunity (e.g. route "Just broke up" / "Looking for a soulmate" to a compatibility-led paywall variant). The routing engine already supports conditional edges and experiments; none are used.
- **`/14` progress denominator on a 19-step funnel** is mildly deceptive; if users notice the bar "resetting" or steps exceeding 14 it can dent trust in a trust-sensitive vertical.
- **Privacy claim vs. reality tension:** "we only process non-identifiable data" appears on the palm-photo step, yet a palm photo + birth data + email is highly identifiable. Claim is legally risky if taken literally.
- **Stale repo docs:** `PLAN.md`/`PRODUCT_SENSE.md` describe a different 7-step template and will mislead anyone onboarding; no `rag.meta.json` means no quality/intent tagging for this catalog entry.
