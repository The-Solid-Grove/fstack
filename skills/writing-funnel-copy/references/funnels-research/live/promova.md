# Promova (Language learning) — Live Funnel Walkthrough

## Overview
- **URL:** https://english-improve.com (funnel slug `app-bm-v3`); paywall on `english-improve.com/sierra/amethyst-sales-page-cc/...`
- **Entry promise:** "Speak English like a native!" — speak fluently fast.
- **Personalizes on:** prior study experience, age, skills to improve (Speaking/Vocabulary/Pronunciation/Listening/Grammar/Writing/Reading), main goal (Career boost/Work/Discover cultures/Keep mind sharp/School), self-assessed vocabulary (word-marking), motivation needs.
- **~Step count:** 27 quiz steps + loader + email gate + scratch-card + plan preview + promise gate + paywall (~32 total screens).
- **Paywall reached?** YES — full pricing, checkout modal, and exit downsell captured.

## Flow Walkthrough
1. **Hook (screen 1)** → binary Q → "Speak English like a native!" / "Have you studied English before?" Yes / No. Near-100% yes; first effortless micro-commitment.
2. **Social proof reveal (screen 1b)** → give-screen → "19+ million people / already use Promova" + callout "Promova's AI-powered immersion makes learning fast and natural." CONTINUE.
3. **Age (2/27)** → single-select → "What's your age?" / "Age helps us personalize your learning" — 18-29 / 30-39 / 40-49 / 50+. Section header throughout: "Maximize your potential".
4. **Validation (3/27)** → empower screen → "Yay, glad you're here!" / "Practice only 15 minutes a day and speak like a native in 30 days!" (concrete timeframe anchor).
5. **Improve areas (4/27)** → multi-select → "What do you want to improve?" / "You can choose more than one option" — Speaking, Vocabulary, Pronunciation, Listening, Grammar, Writing, Reading.
6. **Goal (5/27)** → multi-select → "What is your main goal now?" — Career boost, Work, Discover new cultures, Keep mind sharp, For school/university.
7. **Vocabulary estimator (20/27)** → interactive word grid → "How many English words do you know? / Mark the Intermediate words you know well!" — user taps known words (approve, promotion, confidence, prejudice, empathy, erudite…). Feeds a self-generated vocab count.
8. **Motivation rating (25/27)** → emoji scale (thumbs-down→thumbs-up) → "Do you need help getting started and staying motivated?" → reveal: "High five! Small wins can make a big difference. Keep up the great work, you're on the right track!"
9. **Interest confirm (26/27)** → thumbs up/down → "Do topics like this interest you? / People who use this reach their goal 2x faster".
10. **Results / learning profile (27/27)** → "Here's your learning profile / Based on your answers" — Summary card: **Vocabulary: 451 words** (self-generated from step 7), a Beginner→Pre-Intermediate slider labeled "Today → in 3 months", "Your English skills" description, Current level: Beginner, Learning goals: Career boost, Focus areas: Speaking, Pronunciation.
11. **Loader (screen 28)** → circular % progress 4→98% "Analyzing your preferences…" with "23+ million people already learning with Promova" (note: jumped from 19M earlier) + verified review carousel (Endah789 ★★★★★ "I love this app! It helps me to speak with correct pronounciation…").
12. **Email gate** → "Enter your email to get your personal plan" + "We respect your privacy and are committed to protecting your personal data!" + unchecked marketing opt-in. After typing, reveals trust badges (EdTechX Awards, Forbes "25 Most Promising Startups", Apple "Popular App to Try") + gift box "Something special awaits you next".
13. **Scratch-card promocode** → "Your personal plan is ready 🎉 / Scratch to reveal your bonus" → drag to scratch reveals "**43% discount** on your personal English plan" + Promo code **LIMITED-SAVE-43** (auto-applies at checkout).
14. **Plan preview** → "Your 3-month plan to reach Pre-Intermediate / Based on your current level: A1 → A2" — card "11 Units, 15 min per day, Career boost"; week roadmap "Built for you on proven learning methods" (Wks 1-4 First wins A1→Strong A1; Wks 5-8 Confidence; Wks 9-12 Real-life fluency Comfortable A1→A2).
15. **Promise gate** → ritual commitment → "Before I get started, I promise to… trust the process, celebrate small wins, and not worry about being perfect" / "tap and hold to promise" (press-and-hold seal). *Note: this gate could not be driven via synthetic events; bypassed by navigating to the paywall URL directly.*

## Paywall Architecture
- **Sticky header:** "Discount expires in 09:57" live countdown + black "GET MY PLAN" CTA.
- **Hero:** "Speak like you've always wanted to" + phone mockup; benefit list: Courses from language experts · Personal plan for your goals · Slang, idioms, everyday phrases · Speaking practice with AI.
- **Pricing ("Save more with longer plans" / repeated as "Start speaking confidently"):**
  | Tier | Anchor → Now | Per-day |
  | --- | --- | --- |
  | Trial week | ~~$43.99~~ **$8.39** | $1.19/day |
  | 1 month | ~~$43.99~~ **$23.99** | $0.85/day (badge "SPEAK FLUENTLY") |
  | 3 months | ~~$84.99~~ **$41.99** | **$0.49/day** (default/best-value) |
  - "Special offer • Promo code applied: LIMITED-SAVE-43" with its own 09:50 timer; CTA "START LEARNING".
- **Per-day reframe:** yes ($0.49/day for 3-month flagship).
- **Trial / auto-renew terms:** "if you don't cancel at least 24 hours prior to the end of the 3 months introductory period, you will automatically be charged the full price of $84.99 every 3 months until you cancel." Processed by **Unlimited Promova Limited, Limassol, Cyprus.**
- **Social proof:** "Join over 19M people" · 7M+ satisfied users · 15M+ downloads · 1,100,000 users achieved goals · App ratings 4.6★ (62.1K) / 4.8★ (202K). Named testimonials with level jumps (Tom 🇺🇸 A2→B2 in 3mo; Anna 🇵🇱 A2→B2 in 2mo; Nick 🇪🇸 B2→C2 in 6mo).
- **Guarantee:** "14-day money-back guarantee • Cancel anytime" / "Full refund if it's not for you — Not seeing progress in 14 days? Get your money back, no questions asked." Plus "Your payment is secured" (Visa Secure, Mastercard ID Check, PCI DSS badges).
- **Urgency/timer:** YES, live 10-min countdown (resets on the downsell).
- **Checkout modal (2 steps):**
  - Step 1/2 value stack: "91% of Promova learners reach the language level they aimed for"; bundles add-ons as FREE — 3 months plan ~~$84.99~~ $41.99, AI conversation practice ~~$50.99~~ **$0.00**, Writing with AI feedback ~~$33.99~~ $0.00, Native speaker videos ~~$22.99~~ $0.00, Culture & traditions ~~$20.99~~ $0.00, Ad-free learning ~~$27.99~~ $0.00.
  - Step 2/2 "Select payment method": "$41.99 to start today, then billed $84.99 / 3 months starting Jun 18, 2026", promo code shown. **Fast payment** (PayPal + Apple Pay + Google Pay) listed first; **Pay with a card** (Visa/Mastercard/Maestro) pre-selected by default.
- **Checkout-close downsell:** closing the modal triggers "Special discount offer for you / Choose a plan" with a FRESH yellow 09:57 timer and CHEAPER intro prices: Trial week $4.99→$29.99/mo ($0.71/day); 1 month −60% $11.99→$29.99/mo ($0.43/day); **3 months −40% $29.99→$49.99/3mo ($0.36/day, pre-selected)**. Intro prices undercut the main paywall ($4.99 vs $8.39 trial; $29.99 vs $41.99 for 3-month).

## Standout Techniques (vertical-unique)
- **Vocabulary self-estimation** ("mark the words you know") → surfaces a concrete "451 words" number on the results screen. Pure Hitchcock self-generated value, language-learning-specific.
- **CEFR-level future-state slider** (A1→A2, Beginner→Pre-Intermediate "in 3 months") — visualizes the transformation in standardized terms learners recognize.
- **Week-by-week CEFR roadmap** ("First wins → Confidence → Real-life fluency") justifies the 3-month plan length.
- **Gamified scratch-card promocode** — turns the discount into a reciprocity gift the user "earns" by interacting.
- **"Promise" ritual gate** (tap-and-hold pledge) — physical micro-commitment escalation right before the paywall.
- **Value-stack checkout modal** that re-prices premium add-ons as $0.00 to make the subscription feel like a bundle steal.

## Notable Copy & Microcopy
- "Speak English like a native!" (entry, mirrors ad).
- "Practice only 15 minutes a day and speak like a native in 30 days!" (effort + timeframe anchor).
- "People who use this reach their goal 2x faster."
- "91% of Promova learners reach the language level they aimed for."
- "Something special awaits you next" (gift-box tease before scratch card).
- "Not seeing progress in 14 days? Get your money back, no questions asked."

## Weaknesses / Risks
- **Inconsistent social-proof numbers** (19M → 23M → "Join over 19M" → 7M satisfied + 15M downloads) undermines credibility on close reading.
- **Aggressive auto-renew** ($84.99 every 3 months) buried under a friendly $0.49/day frame; relies on users not reading the fine print.
- **Downsell undercuts main offer** — a savvy user learns to abandon checkout to get a better price, training price-shopping behavior and cannibalizing full-price conversions.
- **Promise/scratch gates add friction** that can leak fuel for low-motivation users right before payment.
- Long funnel (27 quiz steps) + slow ~30s loader risks drop-off; only committed users reach the paywall (by design, but a lot of effort spent).
