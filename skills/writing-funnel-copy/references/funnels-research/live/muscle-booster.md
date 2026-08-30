# Muscle Booster (Fitness) — Live Funnel Walkthrough

> Walked: 2026-06-15 (capture date from repo history).

## Overview
- **URL:** https://plan.muscle-booster.io (onboarding) → /payment (paywall)
- **Entry promise:** "Personalized workout plan according to your age" — age-gated entry, instant tap-to-start (no welcome screen).
- **Personalizes on:** age, biological sex, goal (Muscle Gain / Weight Loss), current + target body type, motivations, target muscle zones, exercise frequency/history, push-up capacity, daily walking, post-stair feeling, energy between meals, sleep, water intake, workout location, weekly workout goal, height/weight/BMI, exact age, special occasion + event date, email.
- **~Step count:** 36 numbered steps (progress shown "Step N/36"), plus loader + email opt-in + plan-ready interstitials.
- **Paywall reached?** YES — full pricing, before/after, downsell, and checkout modal captured. Stopped at payment sheet (no card entered).

## Flow Walkthrough
1. **Age gate** (entry) — "Personalized workout plan according to your age / Select your age". Options: 25-35, 36-45, 46-55, 56+. Lever: instant relevance + age = primary plan input. ToU/Privacy/Refund consent embedded as fine print (no separate cookie wall).
2. **Gender** (Step 2/36) — "Select your gender". Body copy primes science: "Biological sex is a factor that affects your BMR (metabolic rate)..." Options: Female / Male.
3. **Welcome interstitial** (Step 3) — "Welcome to your Muscle Booster journey!" + "we'll ask a few questions to get to know you better." Fuel refill / expectation-set. CTA Continue.
4. **Goal** (Step 4/36, GOALS) — "What is your goal?" Muscle Gain / Weight Loss. **Primary personalization branch.**
5. **Current body type** (Step 5) — "Choose your body type" Skinny / Average / Overweight, with body photos.
6. **Target body type** (Step 6) — "Choose a target body type" Fit / Bulk / Extra bulk (point-B visualization w/ muscular photos).
7. **Motivation** (Step 7/36, MOTIVATION) — multi-select "What motivates you to exercise?" Improving health / Boosting immune system / Looking better / Building strength and endurance / **Boosting libido** (male-vertical lever). Requires Continue.
8. **Target zones** (Step 8) — "Choose your target zones" Chest/Arms/Belly/Back/Legs/Full body (muscle-map multi-select).
9. **Nostalgia/commitment** (Step 9) — "When were you last at your perfect weight?" 0-6mo … More than 3 years ago / Never. Activates problem awareness.
10. **Reassurance interstitial** — "Everyone's body is different / No matter what your starting point, we're here to support you throughout the journey." Soothe beat.
11. **Interest tag-cloud** (Step 11) — "What are you interested in?" ~13 chips (Weight loss, Body sculpting, Strength, Muscle Gain, Libido boost, etc.). Multi-select + Continue.
12. **Exercise frequency** (Step 12) — "How regularly do you exercise?" Never / not regularly / Regularly. Subcopy: "...measure your workout consistency, which is vital for overall fitness."
13. **Sedentary** (Step 13) — "Do you have a sedentary lifestyle?" Yes/No.
14. **Push-ups** (Step 14, FITNESS LEVEL) — "How many push-ups can you do?" Up to 5 / 5-10 / 10-20 / 20+ / I don't know.
15. **Walking** (Step 15) — "How much do you walk daily?" <1h / 1-2h / 2h+.
16. **Stairs** (Step 16) — "How do you feel after climbing the stairs?" Out of breath / A little tired but good / Energized. Subcopy primes cardiovascular framing.
17. **Energy between meals** (Step 17, LIFESTYLE) — "How do you feel between meals?" sleepy when hungry / tired after eating / always energized.
18. **Sleep** (Step 18) — "How much sleep do you get?" <5h … Over 8h.
19. **Water** (Step 19) — "What's your water consumption like?" tea/coffee only … 10+ glasses.
20. **Fitness-level RESULT reveal** (Step 20, FITNESS LEVEL) — **Hitchcock self-generated value.** "Your fitness level is beginner / 50 total score / 🥉 Great for a start!" + score bars: Consistency 20/30, Strength 10/30, Endurance 20/30. "Muscle Booster will customize your workout plan with short and effective workouts..."
21. **Workout location** (Step 21) — "Choose your workout location" Home / Gym / Hybrid (with coach photos + descriptions).
22. **(unsampled — skipped a couple in transition)**
23. **Weekly goal** (Step 23) — "How often would you like to exercise? / This is your weekly workout goal." 1-7 days; **"OUR RECOMMENDATION" badge on 2 days/week** (anchored default).
24. **Height** (Step 24) — "How tall are you?" in/cm toggle. Good-to-know box: "Calculating your body mass index — BMI is widely used as a risk factor for the development of or the prevalence of several health issues."
25. **Current weight** (Step 25) — "What is your current weight?" kg/lbs. **BMI poke (light guilt, amber callout):** "Your BMI is 27.8, which is considered overweight. You should pay more attention to your weight. We will use your index to tailor a weight loss program."
26. **Target weight** (Step 26) — green **soothe/empower callout:** "HEALTH BENEFITS: lose 11% of your weight — There's scientific evidence that some obesity-related conditions improve with 10% or higher weight loss: a reduced chance of having a heart attack, lower blood sugar, and decreased inflammation in blood vessels."
27. **Exact age** (Step 27) — "What is your age?" Good-to-know: "We ask your age to create your personal plan — Older people tend to have more body fat than younger people with the same BMI."
28. **Summary of fitness level** — BMI gauge "You - 27.8" in OVERWEIGHT (red) vs "Normal - 21.5"; red callout "Risks for an unhealthy BMI — Our programs are designed to ease you into working out..."; Lifestyle: Sedentary, Exercise: No regular workouts, Activity level: Average + body image. Commitment lock-in.
29. **Special occasion** (Step 29) — "Is there a special occasion you want to gain muscle for? / You're more likely to reach your goal if you have something important to aim for." Vacation/Competition/Important date/Extreme sports/Birthday/Beach trip/Reunion. Deadline lever.
30. **Event date** (Step 30) — "When's your event?" date picker (pre-filled). Privacy line "Your data will not be shared with any third parties." + "SKIP THIS QUESTION."
31. **Projected-result graph** (Step 31, PERSONAL DETAILS) — point-B: "The one and only plan you'll ever need to gain muscle. According to the information you have provided us, you'll achieve your goal weight of **80kg by Aug 03, 2026.** Get ready to amaze everyone at your vacation." Weight curve 90kg → 84kg → Expected result 80kg.
32. **LOADER w/ social proof** — "Creating your personalized plan… 2% → 100%". Rotating proof: "65 million users have chosen our app" → user-photo cluster → trust badges (App Store **171K 5-star ratings**, **38.9M workouts completed**, Google Play **193K 5-star ratings**) → "Personal plan created / One of the best health & fitness apps."
33. **#1 app interstitial** — "#1 fitness app* / Lose fat and get fit / *SensorTower, 2021, Android & iOS by downloads / Create an account to save your data." Continue.
34. **Email gate** (Step 34) — "Enter your email to get your personalized **Weight Loss** plan!" (note: switched goal label to Weight Loss based on BMI, despite Muscle Gain selection). "65 MILLION USERS HAVE CHOSEN US" + privacy reassurance. **No password required.**
35. **Email opt-in** — "Do you want to receive emails with Muscle Gain tips and product updates?" SURE, I'M IN! / "I DON'T WANT TO RECEIVE TIPS OR UPDATES" (declined).
36. **Plan-ready** — "Your 4-week Plan to Gain Muscle is ready!" upward weight chart ("for illustrative purposes only"). → /payment.

## Paywall Architecture
- **Hero / before-after (above fold):** "Now vs Goal" comparison table with body images (overweight → muscular, chevron arrows). Now: Body fat 15-24%, low Muscle mass bars. Goal: Body fat 6-14%, full Muscle mass bars. Recap chips: Level **Beginner**, Target weight **80 kg**.
- **Urgency timer (live):** top bar "61% discount reserved for: 09:58" counting down + red bar "This offer ends in 09:XX min." Timer is real and ticking.
- **Pricing (3 tiers, all "Save 61%", framed per-day):**
  | Tier | Anchor (full) | Discounted total | Per-day | Badge |
  |---|---|---|---|---|
  | 1-WEEK TRIAL → 4-WEEK PLAN | ~~€17,77~~ / ~~€2,53~~ | €6,93 | **€0.99/day** | (default selected) |
  | 4-WEEK PLAN | ~~€38,95~~ / ~~€1,25~~ | €15,19 | **€0.49/day** | MOST POPULAR |
  | 12-WEEK PLAN | ~~€66,65~~ / ~~€0,74~~ | €25,99 | **€0.28/day** | RECOMMENDED FOR YOU |
- **Per-day reframe:** giant "€0⁹⁹ per day" styling dominates each card; crossed-out anchor prices on both total and per-day.
- **Trial / renewal terms (fine print):** "We've automatically applied the discount to your first month period. After the first month, your subscription will be automatically renewed at the full price of **€38,95 per month**... renewed every month until you cancel." (Intro price → full €38.95/mo rollover.)
- **Social proof:** App Store 171K 5-star, Google Play 193K, 38.9M workouts, 65M users; four named text testimonials (Ian A., carollee227, Derek84, cedricjb14); "Our users meet their goals — Wilfred de Guzman, USA" success case.
- **Guarantee:** "30-day money-back guarantee" link near CTA + full block: "...willing to return your money if you don't see visible results and can prove that you followed our plan."
- **Pricing repeated twice** (top + bottom of page) with the same timer.
- **Checkout modal:** "Checkout — 1-week intro 17,77 EUR, 61% introductory price discount −10,84 EUR, **Total: 6,93 EUR for 1 week**." Payment: **One-click payment default with PayPal, Apple Pay, Google Pay shown prominently (above Credit card)**; Credit card is the collapsed secondary option.
- **Checkout-close downsell (strong):** closing the checkout X fires a "Did you know?" modal (strength +30% With vs Without training chart, "Today → in 18 weeks") with copy "We want you to become stronger... so we are offering you a special discount for your muscle gain program." → **timer resets to 09:57 AND discount jumps 61% → 69%; tiers re-price to "Save 71%" (4-week €0.36/day €11,29; 12-week €0.21/day €19,29).**

## Standout Techniques
- **BMI weaponization across 3 screens** (calculate → poke "overweight" → empower "lose 11%" → red-zone gauge summary) builds a problem the product solves, with science-flavored good-to-know boxes.
- **Self-generated fitness score** (50/100, color-coded sub-scores) lets the user conclude "I'm a beginner who needs this."
- **Event/deadline capture** ("When's your event?") personalizes the projected date ("80kg by Aug 03, 2026... amaze everyone at your vacation") — Hitchcock point-B.
- **Loader as social-proof theater:** slow 0→100% with rotating 65M users / photo wall / store-rating badges — converts effort time into trust.
- **Goal relabeling:** silently switches Muscle Gain → "Weight Loss plan" on the email screen based on BMI, keeping the highest-intent framing.
- **Aggressive close-intent downsell** with timer reset + deeper discount (61%→69%→71% tiers).

## Notable Copy & Microcopy
- "Your BMI is 27.8, which is considered overweight. You should pay more attention to your weight."
- "lose 11% of your weight — ...a reduced chance of having a heart attack, lower blood sugar, and decreased inflammation in blood vessels."
- "The one and only plan you'll ever need to gain muscle."
- "Get ready to amaze everyone at your vacation."
- "65 million users have chosen our app."
- "We want you to become stronger, healthier, and better looking, so we are offering you a special discount."
- Disclaimer honesty: "This chart is for illustrative purposes only and results may vary for each individual."

## Weaknesses / Risks
- **Fake-urgency credibility:** the "61% discount reserved for 09:58" countdown visibly resets to a fresh 10:00 on close — a savvy user sees the timer is theater, which can erode trust.
- **Goal/label inconsistency:** choosing "Muscle Gain" but being sold a "Weight Loss plan" (and "4-week Plan to Gain Muscle") is confusing and feels like the funnel ignored the answer.
- **Long funnel (36+ steps):** heavy ask-load; relies on frequent reveals to avoid fuel depletion, but several consecutive single-select lifestyle questions (sleep/water/walking/stairs) risk fatigue with thin per-screen value.
- **Trial→rollover surprise risk:** €6.93 "1-week" intro silently rolls to €38.95/month; the renewal terms are present but in low-contrast fine print under the CTA.
- **Per-day price illusion vs. monthly reality:** "€0.99/day" headline obscures the actual €38.95/mo recurring charge.
