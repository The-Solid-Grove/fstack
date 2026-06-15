# Colonbroom (Physical goods / supplement subscription) — Live Funnel Walkthrough

## Overview
- **URL:** https://colonbroom.com (homepage = ecommerce store); quiz funnel at `/glp-1/...`, checkout at `/glp-1/shipping`.
- **Entry promise:** Homepage hero "Gut issues suck, but your life no longer has to." / "Support your digestive wellness with ColonBroom gut health supplements and gentle colon cleanse solutions." Quiz entry: "From cravings to control with up to 70% OFF" / "natural GLP-1 support."
- **Personalizes on:** gender, main health goal, GLP-1/craving symptoms, activity level, age, height, current & goal weight (→ BMI, metabolic age, projected weight-loss curve).
- **~Step count:** Spin-to-win popup → 12-question quiz → email gate → loader → 5 summary screens → product recommendation (pricing) → 3-step checkout (Shipping/Payment/Receipt). ~22 screens.
- **Paywall reached?** YES — full per-bottle subscription pricing + checkout shipping form reached. Did NOT enter address or payment (physical-goods guardrail).

## How a physical-product subscription funnel differs (key ask)
- **Sells in BOTTLE QUANTITIES framed as supply duration**, not app tiers: "3-Month supply = 30x3 servings, 3 bottles delivered" vs "6-Month supply = 30x6 servings, 6 bottles delivered."
- **Per-bottle price as the unit** (€34.74/bottle vs €25.83/bottle) — longer commitment lowers per-bottle cost (volume discount = subscribe-and-save logic).
- **It IS a subscription** ("Pause subscription anytime", "X bottles will be delivered") — recurring physical shipments, not one-time.
- **Shipping is a first-class concern:** courier logos (USPS, DHL, UPS), "Free Shipping", and a full **shipping-address form collected before payment** (3-step checkout: Shipping → Payment → Receipt). Country auto-detected ("Portugal (FREE shipping)").
- **Physical-product trust seals** unique to supplements: VEGAN, GLUTEN-FREE, MANUFACTURED IN USA, NON-GMO, plus a mandatory **FDA disclaimer** ("statements have not been evaluated by the FDA…").
- **No app/free-trial mechanic** — the "trial" concept is replaced by a money-back guarantee and a "+SECRET GIFT" / free-gift bundle.
- **Upsell/downsell via product mix** ("I do not want this special offer" decline link implies a downsell path) rather than feature-tier unlocks.

## Flow Walkthrough
1. **Lead-capture popup** → "SPIN TO WIN!" gamified discount wheel (5% / 10% / 15% OFF / FREE shipping / Mystery Discount) gated behind email. (Skipped/closed.)
2. **Homepage** → store hero + product carousel (GLP-1 Booster, Colon Cleanse & Detox, Premium Blend powder, ACV Gummies, Day/Night Fat Burner, Vitamin D3+K2); banner "SUMMER SALE UP TO 65% OFF"; CTA "TAKE A QUIZ".
3. **Quiz entry (`/glp-1`)** → "From cravings to control with up to 70% OFF" + benefit bullets (Appetite control, Healthy weight loss, Faster metabolism, Stubborn visceral fat burn); **gender select** (Female/Male). (Discount escalates 65%→70% on entry.)
4. **Q1/12** → single-select → "Let's get started! Please share your main health goal right now." — Lose weight, Stop emotional eating, Curb cravings, Stabilize blood sugar, Improve digestion, Boost energy & metabolism.
5. **Q2/12** → multi-select w/ educational framing → "GLP-1 controls hunger. When it's low, cravings spike. Do you notice any of these?" — Intense sugar cravings, Feeling hungry after eating, Overeating, Emotional eating, None. (Teaches the GLP-1 mechanism to prime the product.)
6. **Q9/12** → single-select → "Even the smallest movement can make a big impact. How active are you these days?" — No / Light / Moderate / Physically active.
7. **Q10/12** → number input → "What's your age? It helps us personalize your plan."
8. **Q11/12** → number input (Imperial/Metric) → "How tall are you? We use your height to personalize your results."
9. **Q12/12** → dual input → "What's your current and goal weight? We'll use it to personalize your plan." (current + goal kg → drives projections).
10. **Email gate (`/glp-1/email`)** → "Enter your email" + consent checkbox "By consenting you agree to our Privacy Policy" + "We don't send spam or share email addresses. We respect your privacy." (Rejected `example.com` as invalid; accepted a real-domain address.)
11. **Loader (`/glp-1/loading`)** → "Creating your agenda…" progress bar with testimonial: ★★★★★ "Works just like Ozempic / Finally broke through my weight loss plateau! … down to 160 … Works like Ozempic but without the side effects or cost." — Patricia K., Verified Customer.
12. **Summary 1 (`/summary/1`)** → "YOUR SET GOAL / Here's how GLP-1 Booster can help you shed stubborn weight" — projection chart Jun 2026 **82 kg → Sep 2026 69.4 kg** (markers -7.7 kg, -4.9 kg).
13. **Summary 2** → "YOUR FIRST MONTH / Turn small changes into big wins" — week curve 82→78→77→76 kg, callout "**-6kg in your first month**".
14. **Summary 3** → "Your personal summary" — Female / Age 42 / Height 168 / Weight 82 + BMI + Metabolic age cards.
15. **Summary 4** → "COLONBROOM VS OTHERS" comparison table (✓ targets anti-hunger hormone, breaks plateaus, burns visceral fat, clinically-researched, no prescription, natural/no fillers vs ✗ competitors).
16. **Summary 5** → "REAL STORIES / Users experience massive changes in less than a month" testimonial carousel (Aaliyah J. ★★★★★ "3 weeks in… lost 7 pounds… 20 lbs goal") + "COLONBROOM IS FEATURED IN" press logos.
17. **Recommendation (pricing) `/glp-1/recommendation`** → product offer (below).
18. **Checkout `/glp-1/shipping`** → Shipping form (name, street, apt, country, town, zip, email, phone) → Payment → Receipt. (Stopped here.)

## Paywall Architecture (Recommendation page)
- **Header:** "Summer Sale — SAVE UP TO **70%**" with a live **23:59:xx countdown** (24-hour timer, resets ~daily — soft urgency).
- **Hero:** "OUR RECOMMENDATION / Our recommendation for ultimate weight loss success" — "Based on your quiz data, we recommend starting with the **3-month subscription plan** … or a **6-month subscription plan**…"
- **Tiers (per-bottle pricing):**
  | Plan | Badge | Price | Includes |
  | --- | --- | --- | --- |
  | **3-Month supply** | MOST POPULAR · EFFECTIVE RESULTS (pre-selected) | **€34.74/bottle** | 30x3 servings, 3 bottles delivered, pause anytime |
  | **6-Month supply** | BEST VALUE · LONGER-LASTING ROUTINE | **€25.83/bottle** | 30x6 servings, 6 bottles delivered, pause anytime |
  - **Anchor:** 6-month is anchored as "BEST VALUE" (€25.83 vs €34.74/bottle = the longer-commitment discount).
  - **"+SECRET GIFT"** badge on the product image (free-gift reciprocity / mystery bundle).
- **No per-day reframe** (per-bottle instead). **No free trial** — replaced by free gift + guarantee.
- **CTA:** "TAKE THIS OFFER"; decline/downsell link "I do not want this special offer".
- **Trust block:** "SHIPPED BY TRUSTED COURIERS" (USPS, DHL, UPS); icons Free Shipping · Excellent Customer Support · Free Gift Included; product seals VEGAN / GLUTEN-FREE / MANUFACTURED IN USA / NON-GMO; FDA disclaimer.
- **Payment methods shown:** PayPal, Visa, Mastercard, Amex, **Stripe** (card-processor logos). No explicit Apple/Google Pay button on the recommendation page (those typically appear in the Stripe/PayPal checkout step).
- **Checkout:** 3-step Shipping → Payment → Receipt; country geo-defaults to "Portugal (FREE shipping)".
- **Downsell:** the "I do not want this special offer" link is the entry to a cheaper/alternative-product downsell (not pursued).

## Standout Techniques (vertical-unique)
- **Ozempic comparison positioning** — "Works just like Ozempic… without the side effects or cost" leverages the GLP-1/Ozempic cultural moment for a natural-supplement alternative.
- **Mechanism-education questions** ("GLP-1 controls hunger. When it's low, cravings spike") that teach the user the problem so the product reads as the obvious fix.
- **Spin-to-win wheel** as a gamified email-capture lead magnet on the storefront (ecommerce-specific).
- **Per-bottle / supply-duration pricing** = subscribe-and-save framing native to physical CPG.
- **Personalized weight-loss projection charts** (date-stamped to the visitor's real timeframe, e.g. Jun→Sep 2026) — Hitchcock self-generated value.
- **"+SECRET GIFT" mystery bundle** to boost perceived value without naming the gift.

## Notable Copy & Microcopy
- "Gut issues suck, but your life no longer has to."
- "From cravings to control with up to 70% OFF."
- "Works like Ozempic but without the side effects or cost." (testimonial)
- "-6kg in your first month."
- "Pause subscription anytime." (de-risks the recurring commitment)
- "I do not want this special offer." (downsell trigger phrased as self-denial)

## Weaknesses / Risks
- **Subscription framing can be obscured** — "supply" + "bottles will be delivered" can read as one-time to a skimming buyer; auto-renew/recurring billing terms not surfaced on the recommendation card (only "pause anytime").
- **Discount inconsistency / fake-urgency** — 65% (home) → 70% (quiz) and a 24h timer that resets daily undermine credibility; aggressive weight-loss claims (-6kg/month) plus Ozempic comparison invite regulatory scrutiny despite the FDA disclaimer.
- **Currency/geo mismatch risk** — pricing shown in EUR with Portugal auto-selected for shipping; users in other regions may distrust the localization.
- **Spin-to-win popup on entry** can feel spammy and trains discount-seeking before the value pitch lands.
- **Shipping-address friction** at checkout (full form) is a higher barrier than an app's email+card; cart abandonment risk is greater for physical goods.
