# Acely (Edtech / SAT-AI test prep) — Live Funnel Walkthrough

> Walked: 2026-06-15 (capture date from repo history).

## Overview
- **URL:** https://acely.ai (redirects to acely.com). Marketing homepage → "Try Acely for free" launches the onboarding quiz funnel.
- **Entry promise:** "Your personal study trainer for the SAT & ACT. / Smarter than a prep course. More personal than a tutor. A fraction of the cost." Hero social proof: "1480 — Ava increased her SAT score by 110 points in 2 months."
- **Personalizes on:** which test (SAT/ACT/Both), who's taking it (student vs parent), test date/urgency, emotional state about the test, how they handle confusion, when/how they study, their biggest blocker, post-practice-test feeling, learning-style, deepest motivation (college/scholarship/pride/pressure), and what makes prep "worth it." Builds toward a target-score plan.
- **Step count:** ~12 quiz screens + value/empathy interstitials, then result → account → invite-parent → paywall. Progress bar visible throughout.
- **Paywall reached?** YES — full pricing observed.

## Flow Walkthrough (ordered)
1. **Homepage hero** → "Your personal study trainer for the SAT & ACT." CTA **Try Acely for free**. (Cookie banner — chose Reject Non-Essential.)
2. **Q: Test** → "Which test are you taking?" SAT / ACT / Both / I'm not sure yet. ("Skip for now" present.) Auto-advance.
3. **Q: Who** → "Who's taking the SAT?" I'm the one taking it / I'm a parent supporting my student. (Branches messaging student vs parent.)
4. **Q: Timing (urgency)** → "When do you plan to take the test?" Less than 2 months / 2–6 months / More than 6 months / Not sure yet.
5. **Q: Emotion (poke)** → "Be honest, how are you feeling about the SAT?" Totally fine / A little nervous but manageable / Pretty stressed if I think about it / Honestly, it weighs on me a lot.
6. **Empathy interstitial (soothe + proof)** → "That feeling is completely normal. / Students just like you have improved their score with a plan built around their needs." Before/After card **1370 → 1520 (↑150 PTS)** + testimonial "Acely made me feel much more confident and prepared on test day!" — David, Real SAT Student. CTA Continue.
7. **Q: Confusion behavior** → "When you hit something you don't understand, what do you usually do?" Look it up myself / Skip it and hope it doesn't show up / Ask someone (teacher, tutor, parent) / I haven't really gotten that far yet.
8. **Q: Study time** → "When do you study best?" Mornings/free periods / After school or late night / Weekends / Whenever I can fit it in.
9. **Q: Session quality (pain)** → "What does your typical study session look like?" Focused and consistent / Starts strong, then I lose focus / Usually last-minute cramming / I haven't started studying yet.
10. **Value interstitial (reframe + AI diagnostic)** → "Most students study the wrong things for too long. / Acely targets your weak spots so every session counts. **20 minutes a day beats hours of unfocused prep.**" "Study plan updating" pill + personalized "BIGGEST OPPORTUNITIES" card (Craft and Structure 56% accuracy, Inference 72%, Information and Ideas 68%).
11. **Q: Learning style** → "Which of these sounds most like you?" exact plan to follow / options and flexibility / work better under pressure / understand not memorize.
12. **Q: Blocker** → "What's getting in the way of studying right now?" Procrastination / I don't know where to start / School is already overwhelming / I'm studying but my score isn't moving.
13. **Q: Practice-test feeling** → "How do you feel after taking a practice test?" Motivated / Kind of defeated, honestly / Confused about what to do next / I avoid taking them.
14. **Feature-sell interstitial** → "Ask anything. Acely explains until it clicks." AI-chat mockup (student: "why isn't the answer C?" → Acely answer explanation) + testimonial "I was able to get in-depth explanations when I got stuck. Then I could practice the new strategies I learned." — Ella, Acely student.
15. **Q: Motivation (higher-level value)** → "What would hitting your goal score change for you?" It opens up college options / It could mean scholarship money / It would prove something to myself / It would take a lot of pressure off.
16. **Q: Worth-it value** → "What would make test prep feel actually worth your time?" Knowing exactly what to focus on / Short sessions that fit into my day / Seeing my score go up / Clear step-by-step guidance.
17. **Result/plan summary** → "1520" target-score gauge + "Acely was made for students like you. / Here's your path to your goal score:" 01 Get your personalized plan → 02 Train on your weak spots → 03 Watch your score climb. CTA **Get your free plan** with "3-DAYS FREE" + "SCORE IMPROVEMENT GUARANTEE" badges.
18. **Account creation** (/create-account) → "Your path to a higher score starts here." Continue with Google / Continue with Apple / OR email + first + last name → Continue. (Passwordless — advanced with research email + name; no password/OTP demanded.)
19. **Invite-parent upsell** (/invite-parent) → "Add a parent or guardian — They'll get progress updates and **take care of billing**, so you can focus on studying." Email + name fields, or **Skip for now**. (Skipped.)
20. **PAYWALL** (/payment) — see below.

## Paywall Architecture
- **Headline:** "Enjoy a 3-day free trial. No charge today." Trust checklist: "Trusted by 50,000+ students / Guaranteed score improvement or your money back / Cancel anytime, no questions asked."
- **Tiers (exact):**
  - **Annual — $49/mo, $588 billed annually**, badge **"SAVE $1,200"**, pre-selected default. Subcopy: "Achieve your personal best across multiple test dates."
  - **Quarterly — $99/mo, $297 billed quarterly**, badge **"MOST POPULAR."** "Get ready for your upcoming test without last-minute cramming."
  - **Monthly — $149/mo, $149 billed monthly.** "Make the most out of the study time you have left."
- **Anchor/reframe:** Monthly $149 anchors the annual down to $49/mo; "$1,200 saved" frames the annual against 12× monthly. Per-month framing on every tier.
- **Trial terms:** 3-day free trial, "your card won't be charged until the end of your trial on 06/19" (date dynamically = today+3, reinforcing urgency). Auto-renews; cancel anytime in account settings.
- **Order summary:** ACELY-ANNUAL $588.00 / TOTAL AFTER TRIAL $588.00 / **Total due today $0.**
- **Social proof:** ★★★★★ "I was overprepared to retake the SAT and was ten times more confident." — Camden, Acely Student.
- **Guarantee:** "Money-Back Guarantee — We guarantee an increase of at least **200 points on the SAT and 5 points on the ACT.** If not, we'll provide a full refund." (a remarkably bold, specific performance guarantee).
- **Payment:** Card (number, MM/YY, CVC) + a **"Bank" option carrying a "$5 back" incentive** to push ACH (lower processing fees / harder to dispute) + Country + ZIP + Add promo code. **Powered by Stripe.** No Apple Pay / Google Pay express buttons observed (card + bank only).
- **Urgency/timer:** No countdown timer; urgency comes from the dynamic trial-end date and the test-date framing collected earlier. CTA **Start My Free Trial**.
- **Checkout-close downsell:** Not triggered (did not attempt to close).

## Standout Techniques (vertical-unique)
- **Emotion-first questioning specific to test anxiety** ("Be honest, how are you feeling about the SAT?" → "Honestly, it weighs on me a lot") — a textbook Poke→Soothe→Empower beat ("That feeling is completely normal" + Before/After). Edtech sells relief from anxiety as much as a score.
- **Live "AI diagnostic" mockups** (BIGGEST OPPORTUNITIES with per-skill accuracy %; AI-chat "why isn't the answer C?") make the differentiated value (adaptive AI tutor that targets weak spots) tangible mid-funnel — Hitchcock-style, the student concludes "this finds exactly what I'm bad at."
- **Parent-as-payer architecture.** The "Who's taking the SAT?" branch and the dedicated "Add a parent or guardian… take care of billing" step explicitly route the purchase decision to the paying adult — unique to a minor-targeted product.
- **Specific performance guarantee** (+200 SAT / +5 ACT or full refund) is a strong risk-reversal that few competitors will match and directly answers "will this actually work for me."
- **"$5 back" bank-pay nudge** — steers users to ACH over card (cheaper fees, fewer chargebacks) with a small bribe.
- **Dynamic trial-end date in copy** ("charged at the end of your trial on 06/19") personalizes urgency without a fake timer.

## Notable Copy & Microcopy
- "Smarter than a prep course. More personal than a tutor. A fraction of the cost."
- "That feeling is completely normal."
- "Most students study the wrong things for too long. … 20 minutes a day beats hours of unfocused prep."
- "Ask anything. Acely explains until it clicks."
- "Watch your score climb."
- "Enjoy a 3-day free trial. No charge today." / "Total due today $0."
- "We guarantee an increase of at least 200 points on the SAT and 5 points on the ACT. If not, we'll provide a full refund."

## Weaknesses / Risks
- **Price shock potential:** monthly is $149/mo — high; users who don't notice the annual default may balk. The "SAVE $1,200" framing leans hard on the annual to make the others look reasonable.
- **Bold +200pt guarantee** invites refund abuse and is operationally risky if score gains don't materialize; the "Learn more" terms likely have conditions (usage minimums) that could frustrate claimants.
- **Card required for a "free" trial** with auto-renew at $588 is a classic trial-to-paid friction/complaint vector, mitigated only by the "cancel anytime" copy.
- **Minor-data sensitivity:** collecting a teen's email/name then routing billing to a parent must be handled carefully (COPPA/age-of-consent); the flow does ask "who's taking it" but doesn't gate by age.
- No express wallets (Apple/Google Pay) on the paywall — adds mobile checkout friction for the teen demographic that lives on phones.
