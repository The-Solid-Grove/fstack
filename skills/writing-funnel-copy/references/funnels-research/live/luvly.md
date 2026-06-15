# Luvly (Beauty / Face Yoga) — Live Funnel Walkthrough

## Overview
- **URL:** https://quiz.luvly.care (landed on cohort `luvly_intro_fast`, route `/ageAsIntro`)
- **Entry promise:** "GET YOUR 20s FACE SHAPE BACK" — anti-aging / facial rejuvenation without cosmetic procedures.
- **Personalizes on:** age band (first screen), main goal, face-yoga familiarity, current skin satisfaction, multi-select focus areas, skincare routine depth, products used, sun habits, cosmetologist frequency, diet/sugar/vegetables/water intake, gender.
- **~Step count:** Long. Progress bar shows 4 sections, each containing many sub-screens (~20+ screens total even in the "fast" cohort). Sectioned into ~4 phases: Goals/Education → Lifestyle → (Photo/Result) → Plan/Paywall.
- **Paywall reached?** NO — blocked at the `/photoResult` "Connecting to database" loader. The progress bar was stuck at 0%. Root cause confirmed via JS: `document.hidden === true` (automation tab treated as backgrounded). Overriding the Visibility API + dispatching `visibilitychange`/`focus` did not advance it, indicating the loader also waits on a backend result that is gated on a selfie/photo I did not provide (route is literally named `photoResult`). Paywall lies one section beyond this loader.

## Flow Walkthrough (ordered)
1. **/ageAsIntro** — Age gate as intro. Copy: "GET YOUR 20s FACE SHAPE BACK / Select your age to start." Options: 18-29 / 30-39 / 40-49 / 50+. Lever: immediate personalization + commitment bias (effortless first tap). Hero = woman's face with dotted face-yoga massage points overlaid (the value is the visual).
2. **/goalVariant2** (Step 1) — "What is your main goal?" Tighten skin / Lose face fat / Get rid of wrinkles. Lever: goal capture, segments the promise.
3. **/haveYouHeard** — "Have you heard about Face Yoga before?" Not sure / I know a few things / Yes, I know everything about it. Auto-advances on tap. Lever: branches into education depth.
4. **/whatIsFaceYoga** — GIVE/education reveal (triggered by "Not sure"). "What is **face yoga**, anyway?" + "So how does it work?" Lists Massage (boosts circulation, lymphatic drainage, releases tension) and Acupressure techniques (preventing headaches, releasing sinuses, sleep quality). CTA "Ok, got it!". Lever: value-loading + mechanism credibility.
5. **/satisfyWithSkinCondition** — Emoji-led: "Are you satisfied with your skin condition?" 😍 Yes keep forever / 🙃 small improvements / 🥹 No, lots of problems. Lever: problem activation.
6. **/obTags** — Multi-select chips "Choose your focus": Face sculpting, Fresh complexion, Healthy habits, Collagen boost, Consistent routine, Even skin tone, Blemish reduction, Mental health, Double chin reduction, Stress relief, Face lifting, Detox. Lever: lets user self-load many value categories.
7. **/skinCareRoutine** — "Do you have daily skin care routine?" morning+evening / only morning / only evening / no routine. Problem activation.
8. **/careCosmetics** — Multi-select products in routine (Cleanser, Toner, Serum, Moisturizer, Eye cream, Face mask, Exfoliators, Lip treatment, None).
9. **/sunSafety** — "Do you put sunscreen on?" always / sunny only / sometimes / rarely / never.
10. **/visitToCosmetologist** — "How often do you visit a cosmetologist?" — sets up the cost-comparison reframe.
11. **/cosmetologistVsLuvly** — GIVE/reframe screen: "Get a glow-up with a combination of unique face yoga exercises and a personalized skin care routine while reducing visits to a cosmetologist… you will feel much more confident with your reflection in the mirror after a couple of days." Lever: positions Luvly as cheaper substitute for cosmetologist (anchoring against expensive alternative).
12. **/eatingPatterns** — meals per day. (Section 1 completes here — checkmark.)
13. **/diet** — specific diet (No specific diet / Vegetarian / Gluten-free / Vegan / Other).
14. **/sugar** — added-sugar frequency (Everyday/Often/Sometimes/Never).
15. **/vegetables** — greens/vegetables frequency.
16. **/dailyWater** — interactive: tap 10 glass icons to set water intake (engaging micro-interaction, not a list).
17. **/gender** — Female / Male.
18. **/photoResult** (Section 2 complete) — Loader: "Getting healthy skin just became easy with Luvly" + before/after photo pair + testimonial "Paula, 32 y.o.: For the last 10 months I have been practicing face yoga daily. And now I look much younger than I used to 7 years ago." Progress: "Connecting to database" 0%→(blocked). **Blocked here.**

## Paywall Architecture
NOT reached live. From the funnel structure, the paywall sits in section 3-4 after the photo/result loader and a likely email gate. (Publicly, Luvly is known to run a hard timer-based weekly/4-week trial paywall with per-day reframe and Apple Pay; not verified in this session so omitted to avoid fabrication.)

## Standout Techniques (vertical-unique)
- **Age-as-intro hero**: instead of a welcome screen, the very first screen is the age question over a face with dotted face-yoga massage zones — the value (where you'll work) is the visual, and the first tap is effortless (commitment bias).
- **Mechanism education** ("What is face yoga / how it works") loaded immediately after the user admits "Not sure" — converts ignorance into curiosity-satisfied conviction.
- **Cosmetologist-vs-Luvly cost reframe**: anchors a cheap subscription against expensive in-person cosmetologist visits — beauty-vertical-specific substitution anchor.
- **Interactive water-glass picker**: gamified ability-screen that feels like a give, not an ask.
- **Photo/selfie result mechanic**: funnel personalizes on the user's own face (the `photoResult` route), creating self-generated before/after expectation. (Also the gate that blocked automation.)

## Notable Copy & Microcopy
- Hero: "GET YOUR 20s FACE SHAPE BACK".
- "What is **face yoga**, anyway?" (curiosity headline, keyword highlighted in brand coral).
- Reframe: "…while reducing visits to a cosmetologist."
- Testimonial loader: "Paula, 32 y.o. … now I look much younger than I used to 7 years ago. It still brings a smile to my face when I look in the mirror."

## Weaknesses / Risks
- **Very long lifestyle-question block** (diet/sugar/vegetables/water/cosmetologist) in section 1-2 — heavy ask-cluster with thin give-screens between, risks fuel depletion before the payoff.
- **Loader fragility**: the result loader is visibility/network-gated and stalled at 0% in a background/automation context — a real user on a flaky connection or with JS-timer throttling could get stuck before ever seeing the paywall (revenue leak).
- Diet/vegan questions feel only loosely connected to a face-yoga product; relevance dip risks "why are you asking this" fuel loss.
