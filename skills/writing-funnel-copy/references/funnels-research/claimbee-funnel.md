# ClaimBee Funnel — Research Notes

> Source: `funnels/rag-catalog/claimbee-funnel`. Copy quoted from `src/steps/content/*.content.ts`; routing from `src/config/funnel.manifest.ts` (`edgesByStepId`); pricing from `src/config/billing.plans.ts`; experiments from `src/config/experiments.ts`. RAG quality score 0.92.
>
> **Reference mode: `step-structure-only`.** This teardown is copy, visual, and interaction research—not current FunnelsGrove contract guidance. Do not copy its `type`/`kind`, answer writes, routing, shell/controller, helpers, or analytics; implementation must follow the synced project's `AGENTS.md` and `docs/funnelsgrove/START-HERE.md`.

## 1. Overview

**Product:** ClaimBee — a "find money you're owed" app. It scans legal/settlement databases (class actions, data-breach settlements, antitrust/privacy verdicts, hidden subscription fees) and helps the user auto-file eligible claims. `rag.meta.json` domainIntent: *"Help users discover and file eligible digital/privacy claims, then convert to subscription checkout."*

**Entry promise (Screen 1 headline):** *"People getting free money know one secret."* The ad-to-screen-1 match is curiosity + greed framing ("free money," "secret"), then immediately reframed as righteous recovery ("They take it back from big corporations") so it does not read as a scam.

**Transformation:** From *"I assume settlement money is fake / too complicated / not for me"* → *"There is real money already legally mine sitting in junk emails and forgotten purchases, and one app finds and files it for me."*

**Length & shape:** ~32 content screens + post-purchase. Classic six-section arc: Hook (1-3) → eligibility/value-loading via real settlements (4-14) → privacy/data-breach value block (15-23) → self-generated payout reveal (24-25) → product-vs-DIY commitment lock-in (26-30) → email capture (31) → paywall (32) → subscription handoff (33) / manage-subscription (35).

**Viewport:** fixed 430×932 phone shell (mobile-first, never scales below 430px).

**Core engine:** This is a textbook **Hitchcock self-generated-value** funnel. It never promises the user a number. It shows a *parade of real, cited settlement amounts* ($92/device, $135M, $2.5B, $725M, $425M, $50–$500 per breach email), asks personal qualifying questions between them, then runs a fake "calculating" scan and reveals a **range that animates up to $1,250** with the disclaimer *"final amount depends on verifying your usage."* The user's brain does the multiplication and owns the optimistic number.

**Pricing (live, `billing.plans.ts`):** weekly $7.99 ($1.14/day), monthly $29.99 ($1.00/day, tagged *"🔥 Most Popular Choice"*, default-selected), yearly $59.99 ($0.16/day). Staged discounts: 30% off (coupon `fg_30_off_one`, 10-min timer) on arrival; 46% off (`fg_46_off_once`) if the user closes checkout once.

## 2. Step-by-Step Walkthrough

Numbering follows file names and branches are noted per step. Routing descriptions summarize observed structure only; use the managed flow/controller contract when implementing them.

### Section A — Hook & first commitment

**`claim` (step-01; shared-Continue entry) — DEFAULT ENTRY**
- Headline: **"People getting / free money / know one secret"** (middle line accented in ClaimBee blue).
- No question, no CTA friction — just a shared Continue. Pure curiosity gap + expectation match.
- Lever: curiosity + greed; trust gate begins (clean visual quality). → `profile`.

**`claim-b` (step-01b)** — A/B variant of step 1 (experiment `claim-step-ab`, 50/50). Same headline content, different Figma node `6043:6332`. → `profile`.

**`profile` (step-02; shared-Continue content)**
- Headline: **"They / take it back / from big corporations."**
- Reframes "free money" as justice/recovery from corporations — kills the scam objection early (Trust Gate: "are you an ally"). → `activate`.

**`activate` (step-03; shared-Continue content)**
- Headline: **"ClaimBee / helps you claim / what is yours."** First brand introduction + bee mascot/glow.
- Lever: ally framing + product name priming. → `eligibility`.

### Section B — Eligibility & settlement value-loading

**`eligibility` (step-04; inline Yes/No interaction)**
- Headline: **"Have you owned or used any Android devices with cellular data?"** Buttons "✅ Yes" / "❌ No".
- Near-100%-yes targeting question; first real micro-commitment.
- **Branch:** `yes → active-google-claim`; `no → subscriptions` (skips the Google settlement highlight).

**`active-google-claim` (step-04b; status/value screen)** — *Yes branch only*
- Copy: *"Right now, Android users can file claims for the **active Google privacy settlement**."* Good-to-know: *"Eligible users may receive **up to $100 per user**."* Status bar: *"Checking active claim status…"*.
- Lever: real cited settlement + loader-as-priming. → `subscriptions`.

**`devices-selected` (step-05, multi-select interaction)** — **⚠ ORPHANED in live graph.** Asks *"Which of these devices have you used?"* (iPhone / Apple Watch / iPad / MacBook / None) "to calculate your potential device-specific compensation." Edges send it → `settlement`, but **nothing routes into it** (the old iPhone path was replaced by the Android `eligibility` question). Dead-but-present.

**`settlement` (step-07; status/value screen)** — **⚠ ORPHANED** (only `devices-selected` points to it).
- Copy: *"In early 2024, **iPhone owners** began receiving checks for the **'batterygate' settlement**."* Good-to-know: *"The average compensation was **$92 per device**."* Status: *"Connecting to FTC Registry…"*. This is the canonical Hitchcock data-point screen; still in the codebase as the legacy iPhone variant. → `subscriptions`.

**`subscriptions` (step-08; shared-Continue content)**
- Tag "Google settlement." Copy: *"Your Android data may qualify… Google privacy settlement is active… **Google set aside $135M for refunds**. Let's check what else may be waiting for you."*
- Lever: anchoring with a huge real number; "what else is waiting" opens the next curiosity loop. → `prime-question`.

**`prime-question` (step-09; inline Yes/No interaction)**
- *"Did you have an active **Amazon Prime** subscription at any point between 2019 and 2025?"*
- **Branch:** `yes → digital-rights`; `no → never-miss` (skips the Amazon $2.5B reveal).

**`digital-rights` (step-10; value story)** — *Prime-Yes branch*
- *"Your digital rights matter — The FTC ordered Amazon to pay out a record **$2.5 billion**. Why? Because they used confusing interface designs known as 'dark patterns' to sign people up without clear consent."*
- Lever: problem-mechanism reveal (dark patterns) + huge anchor; validates the user's latent grievance. → `never-miss`.

**`never-miss` (step-11; testimonial/value screen)**
- *"Never miss a payout you're owed. Our system tracks verified legal sources 24/7 to find payouts you didn't know existed."* Testimonial — George P., 5★: *"ClaimBee told me about money I was owed even though my friends and social feeds never mentioned it."*
- Lever: social proof placed early (per case-study "place proof before skepticism peaks"). → `delivery-apps`.

**`delivery-apps` (step-12; inline Yes/No interaction)**
- *"Did you use delivery apps like UberEats, DoorDash, or GrubHub during 2025?"*
- **Branch:** `yes → active-cases`; `no → claims-progress`.

**`active-cases` (step-13; shared-Continue content)** — *delivery-Yes branch*
- *"We are tracking active cases regarding hidden fees… Many of these services are currently facing lawsuits regarding non-transparent service fees."* → `claims-progress`.

**`claims-progress` (step-14; status/value screen)**
- *"See claims others miss — ClaimBee monitor trusted legal sources to catch hidden settlements and alert you the moment you qualify."* Status: *"Verifying claim deadlines…"*. → `digital-safety-intro`.

### Section C — Privacy / data-breach value block

**`digital-safety-intro` (step-15; section intro)**
- Tag "Privacy & Security." *"Now, let's talk about your **digital safety** — The largest compensation funds in recent years aren't from social media, but from **the companies you trusted with your personal data**."*
- Pattern interrupt introducing a new value category. → `facebook-question`.

**`facebook-question` (step-16, inline Yes/No)** — *"Did you have an active Facebook account between 2007 and 2024?"* **Branch:** `yes → facebook-breach`; `no → google-question`.

**`facebook-breach` (step-17; status/value screen)** — *FB-Yes branch* — *"This period 2007-2024 covers a massive data breach at **Facebook & Cambridge Analytica**."* Good-to-know: *"The settlement reached was **$725 million**."* → `google-question`.

**`google-question` (step-18, inline Yes/No)** — *"Do you use Google Maps or Google Search on your smartphone?"* **Branch:** `yes → privacy-right`; `no → data-breach-question`.

**`privacy-right` (step-19; value story)** — *Google-Yes branch* — *"Privacy is a right, not a setting. Google faced a **$425 million verdict** for tracking location data even when users explicitly turned 'Location History' off."* → `data-breach-question`.

**`data-breach-question` (step-20, inline Yes/No)** — *"Have you ever received an email with the subject line 'Notice of Data Breach'?"* **Branch:** `yes → spam-explainer`; `no → be-first-progress`.

**`spam-explainer` (step-21)** — *breach-Yes branch* — *"We get it — it looks like spam. But that email is effectively a check waiting to be cashed, often ranging **$50 to $500**. We help you turn those 'junk' emails into cash."* (Reframes a familiar object as money — strong self-generated value.) → `be-first-progress`.

**`be-first-progress` (step-22; status/value screen)** — *"Be the First to Know and File. Speed is your biggest advantage… we tell you about new money settlements days early… News sites are often 2 weeks late. We find settlements before they hit the headlines."* Status: *"Verifying claim deadlines…"*. (Builds the product's unique mechanism = speed/automation.) → `nyt-question`.

**`nyt-question` (step-23; Yes/No interaction)** — *"Did a The New York Times article bring you here?"* Authority/attribution probe. **Branch: both Yes and No → `payout-calculating`** (no divergence; likely an attribution-tagging question).

### Section D — Self-generated payout reveal

**`payout-calculating` (step-24; timed scan, auto-advance 20s)**
- 8 rotating scan frames (2.5s each): *"Analyzing device history…"*, *"Scanning data breach records (2018-2025)…"*, *"Matching profile with open Class Action lawsuits…"*, *"Identifying antitrust settlement eligibility…"*, *"Filtering out expired claims…"*, *"Cross-referencing FTC settlement registry…"*, *"Structuring claim groups…"*, *"Finalizing potential payout estimate…"*. Caption: *"Calculating your potential payout…"*.
- Lever: the loader-as-priming masterpiece — fake computation manufactures perceived personalization and effort. → `great-news`.

**`great-news` (step-25; result reveal)** — the conviction climax
- *"Great news! Based on your answers, you are **pre-qualified for 7 active class action lawsuits**."* "Your Potential Payout:" with an **animated SVG chart that counts up to $1,250** over 2s (`MAX_PAYOUT = 1250`, `step-25-great-news.tsx`). X-axis: 0 → "After 2 Weeks." Footnote: *"*The final amount depends on verifying your usage."* CTA "See how to claim."
- Lever: range-not-promise + self-generated number + pre-qualification framing ("pre-qualified for 7"). The chart rising to a date ("After 2 Weeks") doubles as a timeline projection. → `filing-simple`.

### Section E — Commitment lock-in

**`filing-simple` (step-26)** — *"Filing claims can be complex. We make it simple! ClaimBee replaces clunky government forms with a smart, step-by-step experience… strip away the confusing legal jargon."* (Solution mechanism after problem mechanism.) → `journey-choice`.

**`journey-choice` (step-27; custom two-card branch)**
- *"This is your journey — Which pace would you prefer?"* Two cards:
  - **ClaimBee** (badge "Recommended"): *"Auto-file all eligible claims in one click."*
  - **By Myself**: *"You will find court websites, download forms and mail them by yourself."*
- **Branch (in `step-27-journey-choice.tsx`):** `claimbee → relationship-status`; `by-myself → by-myself-warning`. Sets `journeyChoice` attribute. This is the explicit "product vs. DIY" commitment fork.

**`by-myself-warning` (step-28)** — *DIY branch* — *"Are you sure? Self-filing typically takes about **14 hours of work**. You will need to locate court dockets, navigate legal terminology, and monitor deadlines individually. Or, let us handle the heavy lifting. We can automatically file for all 7 lawsuits with a single digital signature."* Reveals the true effort cost, then one button back to the product. → `relationship-status` (rejoins main path).

**`relationship-status` (step-29; three-option branch)** — value multiplier
- *"One last thing to maximize your household's return — What is your current relationship status?"* Options: 💍 Married/Partnered, ⚖️ Divorced, 👤 Single. Defaults to "married." Sets attribute `relationship-status:family = (selected === 'married')`.
- **Branch:** `married → family-claims`; `divorced`/`single` → `email-capture`.

**`family-claims` (step-30)** — *married branch* — *"Get every dollar your family is owed — Track claims for every person in your house in one list. This ensures no money gets left behind."* (Loss-aversion family multiplier.) → `email-capture`.

### Section F — Capture + Paywall

**`email-capture` (step-31; email form)**
- **Contract annotation (`email-capture`):** `legacy-label-invalid`; exact implementation classification lives only in `docs/funnelsgrove/START-HERE.md` → `docs/funnelsgrove/steps/form_input.md`.
- *"Enter the email address for your official claims. Please double-check the spelling. This is the address where you will receive important case updates and payout notifications."*
- Lever: email framed as *operationally necessary* (where payouts go), not marketing. → `paywall`.

**`scratch-card` (step-31b; discount-reveal transition, not a paywall)** — **NOT in default path.**
- **Contract annotation (`scratch-card`):** `legacy-label-invalid`; exact implementation classification lives only in `docs/funnelsgrove/START-HERE.md` → `docs/funnelsgrove/steps/INDEX.md`.
- Full-screen scratch-to-reveal discount; user must erase ≥80% (auto-reveals after 10s on mobile). This screen has no purchasable plans. Reveals confetti + first discount label, resets paywall discount snapshot, → `paywall`. README: "no longer part of the default conversion path… stays available for direct experiments or previews."

**`paywall` (step-32)** — see Section 4. → `subscription-started`.

**`subscription-started` (step-33; post-purchase completion/handoff)** — see Section 5.
- **Contract annotation (`subscription-started`):** `legacy-label-invalid`; exact implementation classification lives only in `docs/funnelsgrove/START-HERE.md` → `docs/funnelsgrove/steps/complete_registration.md`.

**`manage-subscription` (step-35; account-management screen)** — see Section 5.

## 3. Branching, Experiments & Entry Points

**Entry points (`funnelManifest.entryPoints`):** `default` → `claim` (isDefault); `paywall` → `paywall` (direct paywall entry for ad/retarget traffic); `manage-subscription` → `manage-subscription` (post-purchase support, opened with `?user_id=…`).

**Experiment (`experiments.ts` + `funnel.config.ts`):** `claim-step-ab` — "ClaimBee first step," type `step`, status running, launched 2026-06-09. 50% control `claim` / 50% variant `claim-b`. Only one active experiment; only the first screen is split-tested. Both variants converge on `profile`.

**Conditional routes (per-answer divergence):**

| Step | Yes / primary | No / secondary |
|---|---|---|
| `eligibility` (Android) | → `active-google-claim` (then `subscriptions`) | → `subscriptions` (skip highlight) |
| `prime-question` (Prime) | → `digital-rights` ($2.5B reveal) | → `never-miss` |
| `delivery-apps` | → `active-cases` | → `claims-progress` |
| `facebook-question` | → `facebook-breach` ($725M) | → `google-question` |
| `google-question` | → `privacy-right` ($425M) | → `data-breach-question` |
| `data-breach-question` | → `spam-explainer` ($50–$500) | → `be-first-progress` |
| `nyt-question` | → `payout-calculating` | → `payout-calculating` (no divergence; attribution only) |
| `journey-choice` | `claimbee` → `relationship-status` | `by-myself` → `by-myself-warning` → `relationship-status` |
| `relationship-status` | `married` → `family-claims` | `divorced`/`single` → `email-capture` |

**Branch design pattern:** every "Yes" unlocks a *reward screen* (a cited settlement reveal); every "No" skips it. Answering Yes is rewarded with value, so the funnel trains yes-momentum without ever penalizing No with a dead end. The "No" path is strictly shorter, never broken.

**Orphaned/legacy steps:** `devices-selected` (step-05) and `settlement` (step-07, iPhone "batterygate" $92/device) remain in the manifest sequence and have outbound edges but **no inbound edge** in the live graph after the eligibility question was reworked from iPhone to Android. They are unreachable in normal flow (still directly route-accessible at `/devices-selected`, `/settlement`).

## 4. Paywall Architecture (`step-32-paywall.tsx` + `.content.ts`)

Renders only after stored discount state is restored (minimal white loading screen first) to avoid price/timer flicker.

**Sticky top bar:** *"⏰ Discount Expires in"* + blue MM:SS countdown ("minutes"/"seconds" labels) + header **GET MY PLAN** CTA (heartbeat pulse + ripple ring, scrolls to selected plan).

**Hero:** family illustration + pills *"Find hidden money and / claim what's yours."* Gold applied-promo strip directly under the hero: *"% Your promo code applied!"* — the visible code is always a **fake personalized month/year alias** (e.g. `apr_2026`) while checkout passes the real Stripe coupon id behind the scenes.

**Highlight block:** *"Get money you didn't know about — Discover settlement payouts you're owed from past purchases, ClaimBee finds them for you."*

**Plans (`Choose your plan`, monthly default-selected):**
- 1-Week $7.99 ($1.14/day)
- **1-Month $29.99 ($1.00/day) — "🔥 Most Popular Choice", taller card, default**
- 1-Year $59.99 ($0.16/day)
- While a discount is active, cards show crossed-out regular price + crossed per-day above the discounted values; emphasis (blue) only on the selected plan; the rest muted. Each row has a left radio with a green check on the active plan. Meta: "Money-back guarantee · Cancel anytime."

**Checkout (embedded modal, `SharedStripeCheckoutV2Dialog`):** Apple Pay / Google Pay slots render placeholders first, then swap to Stripe's real Express Checkout wallet buttons once availability confirms (desktop shows both; iOS→Apple Pay, Android→Google Pay). Green **GET MY PLAN** card CTA below wallets. Order summary shows Regular Price (crossed), "Your {percent}% Discount," "You just saved {amount} ({percent}% OFF)," promo code, Total. Trust strip: *"91% of users are satisfied with the plan and stay with us after its completion,"* "Pay safe & secure · Powered by Stripe," card-network logos, 30-day money-back line, renewal disclaimer.

**Feature grid ("Find, track, and claim in one place"):** AI claim assistant (*"reviews your info, finds matches, shows you what to do next"*); quick tiles — instant eligibility checks, see how much you could claim, **100+ new settlements found every month**, unlimited claim checks; "claim for your own past buys, bills, or services"; clear progress/tracking; **Personalized Money Alerts**. Every feature maps to a value loaded earlier in the funnel.

**Stories ("Stories from our users"):** 6 rotating quotes at fixed height (no layout shift). Standouts: Elizabeth L. *"saves me more money than it costs — this pays for itself"*; Michael M. *"Even if I unsubscribe, I feel like I got my money's worth with just one claim."* (Directly neutralizes the price objection and the "is it worth it" math.)

**FAQ ("More things you might want to know") — objection handling that secretly sells:**
- "Do you only cover big famous lawsuits?" → "We track it all… complete financial security."
- "What if I don't have the receipt?" → "Many settlements do not require proof of purchase… search your connected digital history."
- **"This sounds too good to be true. Is this a scam or a 'free money' scheme?"** → *"Not at all. We aren't generating 'free money'; we are simply helping you claim money that is already yours legally. Settlements are court-ordered compensations…"* (the central scam-killer).
- "Filing through an app — less likely approved?" → "No… legal validity is the same."
- "Are there hidden fees? Will you take a cut?" → "We do not take a surprise commission… the money you claim stays in your pocket."

**Guarantee:** compact 184px badge, *"Money-Back guarantee — If you're not satisfied, let us know within 30 days… You must demonstrate that you followed the program,"* links to refund policy.

## 5. Upsell / Downsell / Cancellation Flow

**Staged discount downsell (the only upsell mechanic, `billing.plans.ts` + paywall):**
1. First paywall visit starts a **30% off** offer (`fg_30_off_one`), 10-minute timer, `firstStartedAt` stored in local storage; timer derived from timestamp on refresh.
2. **If the user closes the embedded checkout without buying**, a themed **Special Offer** modal appears: gift-box image, centered **-46%** label, *"We want you to feel loved and happy so we are offering you a discount…"*, CTA "GET DISCOUNT." Accepting upgrades to **46% off** (`fg_46_off_once`), fresh 10-minute window, `secondStartedAt` stored, scrolls back to top.
3. After the upgraded offer expires, timestamps keep the offer marked completed — no later visit re-applies a discount; expired = subscription created with no coupon.
This is the "checkout-close down-sell" pattern from best-practices (ARPU recovery), implemented as deeper-discount-on-abandon rather than a separate product.

**Scratch-card (alternate reward path):** `scratch-card` (step-31b) can be inserted to make the first discount feel *earned* via interaction (confetti reveal) before the paywall — currently out of the default path, kept for experiments.

**Post-purchase handoff (`subscription-started`, step-33):** *"Congratulations! Your subscription has started."* QR code to install/open the mobile app; "Open app now" shown only on mobile; "Send link to email" fallback; iOS/Android/Web store links resolved from `funnel_end_users.document.attribution.firstTouch`; store badges hidden when project links aren't configured.

**Cancellation flow (`manage-subscription`, step-35):** direct entry via `?user_id=…`. Stages: subscriptions list (active cards + greyed past/cancelled rows) → **"Please tell us why you would like to cancel"** reason picker (💰 too expensive, 📱 don't use enough, 🙁 couldn't figure out how, 😐 didn't get value, 📦 found a better alternative, 🛠️ technical issues, ⏳ taking a break, ✍️ other) → confirm → "Subscription canceled!" The selected reason is persisted to the funnel user *before* cancellation (retention analytics). No save/win-back offer is shown in cancellation — it is a clean compliant exit.

## 6. High-Performance Techniques Observed

- **Hitchcock self-generated value, executed fully.** A drumbeat of real cited numbers ($92/device, $135M, $2.5B, $725M, $425M, $50–$500) with zero promise to the user, then a chart that animates to $1,250 with "*depends on verifying your usage." The user multiplies and owns the number.
- **Loader-as-priming, twice.** `payout-calculating` cycles 8 fake "scanning FTC registry / matching class actions / filtering expired claims" frames; interstitials say "Connecting to FTC Registry," "Verifying claim deadlines." Dead time manufactures perceived personalization, effort and authority.
- **Yes-momentum with reward branches.** Every Yes unlocks a value reveal; every No is a strictly shorter, never-broken path. Six consecutive qualifying questions, each rewarded, never penalized.
- **Give-after-ask cadence.** Questions are interleaved with reveal/social-proof/progress screens — no stack of three asks in a row.
- **Pre-qualification framing.** "Pre-qualified for 7 active class action lawsuits" — the same eligibility language fitness/finance funnels use to convert effort into entitlement.
- **Trust gate resolved in screens 2-3.** "take it back from big corporations" + "claim what is yours" answers "are you a scam / are you an ally" before any value is loaded.
- **Commitment fork (product vs. DIY) with effort reveal.** "By Myself = 14 hours of work / locate court dockets / monitor deadlines," then one button back to "single digital signature." Makes the product the user's own idea.
- **Household value multiplier.** Relationship-status → family-claims ("no money gets left behind") raises the self-generated total right before capture.
- **Email framed as functional.** "where you will receive payout notifications," "double-check the spelling" — gets real addresses, not throwaways.
- **Staged abandon-triggered discount (30%→46%)** with real Stripe coupons, plus per-day price anchoring ($1.00/day on the default monthly), plus "pays for itself / got my money's worth with one claim" testimonials that pre-empt the price math.
- **FAQ-as-sales.** The "too good to be true / scam" question is answered head-on inside the paywall, converting the single biggest barrier into reassurance.
- **Wallet-first friction removal.** Apple/Google Pay placeholders swap to real Stripe Express buttons; platform-aware (iOS→Apple, Android→Google).

## 7. Notable Copy & Microcopy Tricks

- **"free money know one secret"** — greed + curiosity gap as the entry hook, then instantly de-risked by "take it back from big corporations."
- **"Good to know:"** prefacing every settlement stat — soft, unbolded priming voice (per framework: bold triggers "I'm being sold to").
- **"that email is effectively a check waiting to be cashed"** — turns a familiar junk object (data-breach email) into money the user can picture.
- **"We get it — it looks like spam"** — mirrors the user's exact skepticism, then flips it.
- **"News sites are often 2 weeks late. We find settlements before they hit the headlines"** — manufactures a speed/scarcity advantage only the product provides.
- **"This is your journey"** + "Recommended" badge — soft-defaults the user to the product option.
- **"Are you sure?"** + "14 hours of work" — loss/effort framing on the DIY path.
- **"no money gets left behind"** — loss aversion at the family step.
- **Fake personalized promo alias `apr_2026`** shown to the user while the real Stripe coupon id rides behind it — makes the discount feel bespoke.
- **"Even if I unsubscribe, I feel like I got my money's worth with just one claim"** — a testimonial engineered to neutralize churn anxiety and the subscription objection simultaneously.
- **"91% of users are satisfied… and stay with us after its completion"** — social proof + retention reassurance at the payment moment.
- **Emoji answer buttons** ("✅ Yes / ❌ No") lower the cognitive cost of each tap.

## 8. Weaknesses / Risks / Things to Avoid

- **Manufactured authority/computation.** "Connecting to FTC Registry," "Cross-referencing FTC settlement registry," and 8 scan frames imply live lookups that almost certainly are timed animations (`setInterval` 2.5s; `great-news` is a fixed `MAX_PAYOUT = 1250` count-up). This is the strongest conversion lever **and** the biggest compliance/trust liability if real eligibility isn't actually checked — easy FTC/UDAP exposure for a money-claims product.
- **"Pre-qualified for 7 active class action lawsuits"** is presented as a personalized result but the "7" and the $1,250 ceiling appear hard-coded regardless of answers. If challenged, "based on your answers" is hard to defend. Prefer genuinely answer-derived ranges.
- **Orphaned legacy steps shipped in the manifest.** `devices-selected` (step-05) and `settlement` (step-07, iPhone "batterygate" $92/device) are unreachable in the live graph but still route-accessible at `/devices-selected` and `/settlement` — they reference iPhone framing that contradicts the current Android `eligibility` question, a QA/coherence risk. Remove or re-wire.
- **`nyt-question` has no real branch** (Yes and No both → `payout-calculating`) — an attention/fuel-spend with no per-answer payoff; only justified if it's genuinely used for attribution. Otherwise it violates the "never ask without showing why the answer mattered" rule.
- **Settlement amounts as headline numbers** ($2.5B, $725M, $425M) anchor toward totals the *individual* will never receive; the leap from fund size to personal payout is the user's inference (intentional Hitchcock), but it edges toward deceptive anchoring for a regulated vertical.
- **Discount honesty.** The "personalized" `apr_2026` promo alias is cosmetic; the 30%→46% abandon ladder is real but the visible "earned" framing is engineered. Defensible only while the coupons are genuinely applied (they are, per `billing.plans.ts`).
- **Guarantee has a catch:** "You must demonstrate that you followed the program" quietly conditions the "money-back guarantee" — fine legally, but undercuts the risk-reversal it advertises.
- **Single first-screen-only A/B test.** Only `claim-step-ab` is running; the high-leverage screens (great-news reveal, journey-choice, paywall discount ladder) aren't being experimented on yet.

---

### Standout techniques (5-line summary)
1. **Hitchcock self-generated value done right:** a parade of real cited settlement amounts + a $1,250 animated count-up shown as a *range with a usage disclaimer* — the funnel never promises, the user multiplies and owns the optimistic number.
2. **Loader-as-priming:** an 8-frame "Scanning FTC registry / matching class actions / filtering expired claims" fake-computation screen manufactures personalization, effort, and authority right before the payout reveal.
3. **Reward-branch yes-momentum:** every qualifying Yes unlocks a settlement reveal, every No is a strictly shorter never-broken path — six asks in a row with no penalty and no dead ends.
4. **Pre-qualification + commitment fork:** "pre-qualified for 7 lawsuits," then ClaimBee-vs-"By Myself (14 hours of work)" makes choosing the product the user's own idea, with a family multiplier before email capture.
5. **Abandon-triggered discount ladder + objection-killing paywall:** 30%→46% real Stripe coupons on checkout-close, per-day anchoring, "pays for itself with one claim" testimonials, and a FAQ that answers "is this a scam?" head-on.
