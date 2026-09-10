# Keiki (Parenting / Kids Early Learning) — Live Funnel Walkthrough

> Walked: 2026-06-15 (capture date from repo history).

## Overview
- **URL:** https://get.keiki.app (quiz) → /offer/ (paywall)
- **Entry promise:** Mascot (dragon-fruit character) "Choose your child's age / To create personal learning plan." App store positioning: "Preschool learning games & cartoons for kids."
- **Personalizes on:** child age & gender, siblings, extracurriculars, parent relationship + parent age + daily routine/work, learning setup preference, realistic daily time, child's strengths & challenges as a learner, favorite activity types + favorite way to learn, likes challenge/building, topics liked, main goal, offline/online focus, academic/emotional/social skills to focus on, desired progress speed, child's name.
- **~Step count:** 21 numbered quiz steps + Congratulations + 4 "would this be useful?" bonus-bundle screens + 1 final timeline Q + interactive plan-build loader + email gate + child-name + projection + scratch-card discount → paywall. ~30+ screens total.
- **Paywall reached?** YES — full pricing, scratch-card discount, projection, and checkout modal captured. No card entered. Email gate used funnel.research@example.com (marketing opt-in left unchecked, no password).
- **Cookie consent:** clean "Reject All" available — clicked it.

## Flow Walkthrough
1. **Age gate** (entry) — mascot "Choose your child's age / To create personal learning plan." 0-2 / 3-4 / 5-6 / 7+.
2. **Gender** (2/20) — "Choose the gender of your child" Boy / Girl (with emoji avatars).
3. **Siblings** — "Does your child have siblings?" X / ✓.
4. **Extracurriculars** — "Does your child have extracurricular activities?" X / ✓.
5. **Relationship** — "Who are you to the child?" Parent / Grandparent / Relative / Specialist / Other.
6. **Parent age** — "What's your age? / It helps us get to know you better" 18-24 … 45+.
7. **Routine** — "What best describes your day?" Work full-time / part-time-remote / Stay-at-home parent / Not working (Continue).
8. **Reassurance interstitial** — "A plan that fits your life 💛 / We personalize learning activities to match your schedule and daily routine — simple, realistic, and doable."
9. **Learning setup** — "What learning setup works best for your family?" Independent activities / Activities we can do together / A mix of both.
10. **Daily time** — "How much learning time feels realistic for your day?" 5-10 / 10-20 / 20-30 / 45+ min.
11. **Personalized validation** — "Amazing! Your time brings real progress / With 20-30 minutes, your child can make deeper progress every week."
12. **Strengths** — "What are your child's strengths as a learner?" Creative / Curious / Hardworking / Focused.
13. **Challenges** — "What are your child's challenges as a learner?" Easily frustrated / Easily distracted / Slow to learn / Unmotivated (multi + Continue).
14. **Personalized solution interstitial** — "Distraction affects many kids! / Did you know that 72% of parents face this challenge? Through interactive games designed to stimulate cognitive skills, Keiki helps children reduce distractions by 35%." (responds to "easily distracted").
15. **Favorite activities** — "What type of activities does your child like the most?" Cartoons / Offline / Reading books / Playing games (multi).
16. **Favorite way to learn** — "Choose your child's favorite way to learn" hands-on / listening to stories / watching video / playing educational games.
17. **Likes challenge** — "Does your child like to be challenged?" X / ✓.
18. **Likes building** — "Does your child like to build things?" X / ✓.
19. **Topics** — "Pick the topics your child likes" Sea life / Space / Vehicles / Nature / Cooking (multi).
20. **Section transition** — "Your preferences / We need it to understand how you would like to see your child learning process."
21. **Main goal** — "What's your main goal right now?" Help my child catch up / Keep progress on track / Give my kid fun solo time / Other (parent-goal lever).
22. **Focus medium** — "What type of activities do you want the learning plan to focus on?" Offline / Online / Both equally.
23. **Testimonials** (responds to picks) — "Keiki makes learning Reading and Math fun and easy!" 5★ (Mary34, Mr.jake).
24. **Academic skills** — "Choose academic skills you want your child focus on" Reading / Writing / Speaking / Basic math / Logic thinking (multi).
25. **Emotional skills** — "Choose emotional skills you want your child focus on" Managing emotions / Dealing with disappointment / Coping with stress / Developing a positive self-image.
26. **Social skills** — "Choose social skills you want your child focus on" Being kind / Following rules / Playing cooperatively / Apologizing / Communication.
27. **Congratulations** — "Congratulations 🎉 / We're preparing your child's personalized learning plan based on your answers." → then ✓ to proceed.
28-31. **4 bonus-bundle interest screens** ("Would this be useful for your family?" X/✓, each shows a worksheet bundle): "Ready for school" 7-week program (125 pages) / "Discipline your child" (212 pages) / "Parenting / motivate your child" (19 pages) / "Internet safety" (32 pages). Builds perceived value of bundled bonuses.
32. **Child's learning profile** — child photo, recap (Gender: Girl, Age: 3-4, Extracurricular: Yes), "Current progress level (Based on your quiz answers)" gauge Just starting → On track → Ahead (near On track), Focus areas: Reading, Basic math. (Self-generated value.)
33. **Timeline** — "How fast do you want to see progress?" In a few weeks / In 1-2 months / No strict timeline (anchors projection).
34. **Improvement forecast** (point-B) — "Your child's learning improvement forecast / With Keiki, your child can boost core skills and reach the goal in 4 weeks" ascending Week1-4 bars; "This chart is for illustrative purposes only."
35. **INTERACTIVE PLAN-BUILD LOADER** — circular "0→100% / Reviewing answers → Setting goals → Adjusting game difficulty → Creating learning plan" + "Over 12 000 000 happy parents around the world" + rotating 5★ testimonials. Between stages, **3 commitment popups** ("Do you want to include worksheets / songs / fairy tales in your personal plan?" No/Yes) keep the parent tapping.
36. **EMAIL GATE** — "Enter email to get learning materials right now" + email field + opt-in checkbox (unchecked default: "I would like to receive learning materials, promotions, discounts and special offers from Keiki via email"). No password.
37. **Child's name** — "What's your child's name?" (personalizes the paywall — e.g. "Mia").
38. **Personalized projection** (/offer/) — "Discover how Mia will progress in just 4 weeks" multi-line chart (Academic skills, Discipline, Social skills) Week1-4 + checklist "Offline and online activities / Safe & Ad free / Baby-friendly interface."
39. **SCRATCH-CARD DISCOUNT** — "Scratch to unlock Mia's special gift" — physically scratch-to-reveal "61% discount for your child's Learning Plan / Promo code MIA_2026" (personalized code). Then a forced-delay "Continue (5 sec)" button.
40. **PAYWALL** (with the 61% applied).

## Paywall Architecture
- **Personalized comparison (above):** "Now → Your goal" — Now: Academic skills Intermediate, Discipline Frequent tantrums; Goal: Academic skills Advanced, Discipline Well behaved.
- **Urgency timer (live):** sticky header "🎁 -61% with code / 09:53" + body "Code MIA_2026 applied – 10 min left!" counting down; "Get my plan" CTA repeated in header and inline.
- **Value-stack before price:** benefit list "Innovating way of learning with your child" (1. No more feeling overwhelmed; 2. Reduce tantrums and behavior issues; 3. Stay motivated/engaged; 4. Have more time for yourself; 5. Forget guilt about screen time). Stats: "12,000,000 Kids used our products / 300+ activities / 94% parents satisfaction." Anchoring: "save up to $500 annually on educational materials / 50% of the time you usually spend calming/motivating." "Instant and unlimited access to: 7+ weeks learning plan, educational app, worksheets on 10+ skills (new monthly), progress report."
- **Pricing (3 tiers, per-day framed, crossed-out anchors — 61% applied):**
  | Tier | Anchor | Discounted | Per-day | Badge |
  |---|---|---|---|---|
  | 1 month | ~~€39.99~~ | €10.73 | €0.36/day | Best value for you (default) |
  | 3 months | ~~€59.99~~ | €19.51 | €0.22/day | — |
  | 6 months | ~~€89.99~~ | €34.14 | €0.19/day | — |
- **Billing terms:** "We've automatically applied discount to your first subscription price €10.73. ...your subscription will be automatically renewed at full price of €39.99 at the end of subscription term. You may cancel in settings or via support@get.keiki.app... Additional purchases / up-sales may be offered." (Discounted first term → full €39.99 rollover; explicit upsell warning.)
- **Social proof:** "As featured in: Common Sense Media, CNN, Trustpilot, Aptoide, techtarget.com"; "Join 12 million happy parents around the world / 4,6★ Average rating on App Store and Google Play"; named reviews (Vadym_vad, Eve_26, Nmes Sam).
- **Payment (checkout modal):** "Select your payment method / Mia's Learning Plan / Promo code MIA_2026 / 09:19", Total: ~~€39.99~~ **€10.73**. **Fast payment / PayPal default ("PayPal Buy Now")** + Credit card (Visa/Mastercard/Discover/Amex). Paywall footer payment row: Visa, MC, Maestro, Discover, PayPal, Amex. "Pay safe & secure." No Apple/Google Pay shown.
- **Checkout-close behavior:** closing the payment modal (X) just returns to the pricing list — there is no further exit-intent discount, because the **scratch-card already serves as the discount mechanism** (61% pre-applied, framed as a "special gift" the parent "won").
- **Company:** "FT SICH, IFZA Business Park, DDP, Building A1, Unit 21379-001, Dubai, United Arab Emirates."

## Standout Techniques
- **Conversational mascot-led quiz:** every question is framed as the dragon-fruit character speaking in a speech bubble — warm, gamified, low-friction tone matched to anxious parents.
- **Child-centric self-generated value:** "Your child's learning profile" gauge + named projection ("how Mia will progress in 4 weeks") make the parent picture their specific child's gains; the personalized promo code (MIA_2026) deepens ownership.
- **Bonus-bundle "would this be useful?" sequence:** four yes/no worksheet-bundle previews (125+212+19+32 pages) inflate perceived value before any price is shown — pure value-loading.
- **Scratch-card discount as a "won gift":** the 61% is revealed through a physical scratch interaction, reframing a standard discount as an earned reward (and the only discount lever, replacing a separate exit-intent downsell).
- **Interactive loader with commitment popups** ("include worksheets/songs/fairy tales?") keeps the parent actively choosing during the wait, like Ahead.
- **Parent-benefit framing over child-benefit:** "Have more time for yourself," "Forget feeling guilt about screen time," "Reduce tantrums" — sells to the parent's relief, not just the child's skills.

## Notable Copy & Microcopy
- "The personalized promo code: MIA_2026."
- "72% of parents face this challenge... Keiki helps children reduce distractions by 35%."
- "With our learning plan you save up to $500 annually."
- "Forget feeling guilt about screen time."
- "Code MIA_2026 applied – 10 min left!"
- "Turn the screen time of your child into education."

## Weaknesses / Risks
- **Clunky tap-to-advance UX:** many single-select screens require a second click to advance and the page resets scroll on each transition, repeatedly hiding the Continue button below the fold — a real friction/abandonment risk on desktop.
- **Evergreen urgency:** the "10 min left / 09:53" timer is the usual fake-scarcity pattern; the 61% is a pre-set "scratch" outcome, not a genuine limited offer.
- **Trial→rollover surprise:** €10.73 first term silently rolls to €39.99 (monthly for the 1-month plan); terms disclosed but in dense fine print, plus an explicit "additional purchases / up-sales may be offered" warning.
- **Per-day price illusion:** "€0.36/day" headline obscures the €39.99 recurring charge.
- **Sensitive parenting data + bonus bait:** collects child age/gender/behavior ("frequent tantrums," "discipline") and dangles a "Discipline your child" bundle; the heavy emphasis on tantrums/behavior could feel manipulative to some parents.
- **Offshore entity (Dubai/IFZA):** support-email-only cancellation and a UAE free-zone company may raise refund/accountability concerns for EU/US buyers.
- **Pricing inconsistency vs per-day math:** the 3-month tier's per-day (€0.22) is barely cheaper than 1-month (€0.36) only because the longer term spreads cost — the "Best value" badge sits on the 1-month plan, which is actually the worst per-day value, a mild dark-pattern nudge toward the higher-churn monthly.
