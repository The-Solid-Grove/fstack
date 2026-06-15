# PawChamp (Pets / Dog Training) — Live Funnel Walkthrough

## Overview
- **URL:** https://paw-champ.com → quiz at `/questionary/quiz/quizMain` → paywall at `/questionary/landing-5/...?breed=Labrador&age=Adolescent`
- **Entry promise:** "BECOME A BETTER PET PARENT WITH Modern Personalized Dog Training." App-based, certified-trainer, positive-reinforcement dog obedience.
- **Personalizes on:** dog age, sex, breed, neuter status, target skill, specific behavior problems (leash pulling, barking, etc.), known cues, personality traits, stress triggers, owner's relationship goals, daily time budget, upcoming event/deadline, and the **dog's name** (echoed throughout: "Buddy's obedience plan", "Here's Buddy's profile"). Breed + age are even passed in the paywall URL.
- **~Step count:** ~25+ screens (age → demographics → goal → behavior problems → cues → personality → stress → relationship goals → time → event/date → name → profile → loader w/ 2 interrupt modals → email gate → marketing opt-in → result → paywall).
- **Paywall reached?** YES — full paywall + value-stack modal + checkout payment screen + checkout-close downsell all captured.

## Flow Walkthrough (ordered)
1. Landing — scrolling "Tap to get 60% off" ticker, Product Hunt "#1 Product of the Day", CTA "Take the Quiz". Detailed **PawChamp-vs-Traditional-Training comparison table** anchoring PawChamp ~€9.99/wk / ~€40/mo against Dog Boarding Schools $1,350–$6,000/mo, Group/Individual trainings $120–$2,000/mo, etc. (sourced to a 2024 Dogster price guide).
2. **/quizMain age gate** — "Choose your dog's age": Puppy / Adolescent / Adult / Senior (image cards, auto-advance).
3. Sex — Boy / Girl (♂/♀ icons).
4. Breed — chips (Mixed/Labrador/Pit Bull/German Shepherd/etc.) + "Another breed" dropdown; Next Step.
5. Spayed/neutered — Yes/No.
6. "What would you like to improve?" — Improve obedience / Learn commands / Build a strong bond (emoji).
7. Problem activation w/ dog photo — "Does your dog refuse to pay attention to you?" Yes ignores / Sometimes / No.
8. Recency probe — "When was the last time your dog ignored your command?" Today/Yesterday/This week/This month.
9. **Behavioral issues multi-select** (each with a real dog photo): Excessive energy, Aggression, Leash pulling, Separation anxiety, Excessive barking, Destructive behavior, House soiling.
10. "Does your dog beg for food?" Yes/No (emoji).
11. Known cues multi-select (Name, Sit, Down, Touch, Give a Paw, Leave it, Stop, Come, Stay, Heel...).
12. Slider "How important is obedience to you?" 0–10 (Doesn't matter → Extremely important).
13. "Cool!" interstitial w/ 30-day calendar graphic: "we are creating a dog training program just perfect for your **Labrador**!" (breed echo).
14. Personality multi-select (Easygoing/Mischievous/Curious/Fearless/Friendly/Shy/Leader…).
15. Slider "How important is your dog's socialization?"
16. Stress-triggers multi-select w/ dog photo (Around other animals / Meeting strangers / Home alone / Loud noises / Travelling / Vet).
17. Slider "How friendly is your dog?" — playful labels **Devil → Angel**.
18. Bonding question w/ family photo: "How do you perceive your dog?" Guard / Best friend / Kid / Family Member (higher-level value).
19. Relationship-goal multi-select (Become closer / Establish leadership / Set boundaries / Understand him better).
20. Slider — self-rated knowledge "strengthening the bond" (I need more info → I'm totally prepared).
21. Feature pre-sell — "ask questions to a qualified dog handler online?" Yes/No (sets up the 24/7 expert feature).
22. Commitment — "How much time are you ready to spend?" 5/10/15/20 min/day.
23. Deadline anchor — "Do you have any important event coming up? (Vacation/Wedding/Birth/…) Having something to look forward can be a great motivator." → then "When is your event?" (week/month/few months/year).
24. **Future-state projection** — "The last plan you'll ever need to fix Buddy's behavior challenges. We predict you'll increase Buddy's obedience level by **6 July 2026 — Just in time for Vacation**" with a rising obedience curve tied to the chosen event date.
25. **Loader** — "Creating Buddy's personalized training plan… 115 thousand dog owners have chosen PawChamp" + rotating Trustpilot-style 5★ testimonials. Two mid-loader **interrupt micro-questions** ("Adolescent dogs sometimes show territorial aggression — had this problem?" and "Finalizing your plan — Has Buddy ever had obedience training?").
26. **Email gate** — "Enter your email to get Buddy's personalized obedience plan" + privacy reassurance ("We never send spam").
27. Marketing opt-in — "receive emails with **special offers**, tips and **free gifts**?" Yes I'm In / I'm not interested.
28. Result — "Your 3-month dog obedience plan is ready!" w/ Buddy's obedience curve.
29. **PAYWALL** (below).

## Paywall Architecture
- **Live countdown timer:** "Reserved price for: 09:57" counting down (verified ticking — 09:57 → 09:05 over the session). Scarcity anchor.
- **Hero:** before/after split — "Now" (stressed woman, red-tinted) vs "Your Goal" (happy woman with calm dogs). Stat blocks: Buddy's obedience **Low → Normal**, Training Level **Intermediate → Advanced** (segmented progress bars).
- **Personalized recap:** Goal "Improve obedience", Behavioral problems "Leash pulling, Excessive barking" (pulled from quiz).
- **3 tiers, per-day reframe with strike-through:**
  - 1-MONTH: €1.67/day → **€0.67/day** (€19.99 billed)
  - 3-MONTH: €0.89/day → **€0.36/day** (labeled MOST POPULAR)
  - 6-MONTH: €0.67/day → **€0.27/day** (cheapest per-day anchor)
- **Billing/trial terms (verbatim):** "I agree to pay **€19.99** for my plan and that if I do not cancel 24 hours before the end of the **1-month introductory plan, it will convert to a €49.99 subscription** … every 1-month thereafter until I cancel." So €19.99 intro → €49.99/mo rolling. (Note: this is an introductory-price model, not a free trial.)
- **CTA:** "GET MY PLAN" (coral) + "30-DAY MONEY-BACK GUARANTEE" badge directly below.
- **Below fold:** "What you get" 7-item benefit list (incl. "50+ games … as a bonus"); 3 named before/after success stories (Jupiter/leash pulling, Cooper/aggression, Luna/hyperactivity); FAQ that sells ("how is this different", "not food-motivated", "I don't have time"); Trustpilot 5★ reviews; pricing block repeated; guarantee restated. Phone number +1 (478) 217-7806 and "FONTADELLA LIMITED, Limassol, Cyprus" footer.
- **Value-stack modal (after selecting a plan):** "Your plan for Buddy's — 1-Month Full access. Based on Buddy's profile we added these features: Personal dog trainer support €129.99→**€0**, 50+ DoggyGames €9.99→€0, Separation anxiety €24.99→€0, Why is my dog barking? €16.99→€0, Hyper dog €39.99→€0" — ~€220 of bonuses framed as free.
- **Checkout modal:** "Select a payment method — **PayPal** (pre-selected) / Credit Card (Visa/MC/Amex/Discover)." Total **€19.99**, "Introductory discount — You just saved **€251.99**", itemized (Training plan €49.99→€19.99, all modules €0). Yellow "**PayPal Buy Now**" button + "THE SAFER, EASIER WAY TO PAY". **No Apple Pay / Google Pay** — PayPal + card only.
- **Checkout-close downsell (exit-intent):** closing the payment modal triggers "**Did you know?** 65% of users who started dog training with PawChamp advanced in their goals within the first month" + two-line comparison chart + "We want you to find success so we are offering the **additional discount** on Buddy's Obedience Plan." CTA "GOT IT" (re-presents a further-discounted offer).

## Standout Techniques (vertical-unique)
- **Pet name as the personalization spine** — "Buddy" is woven into the profile screen, loader, projection ("increase Buddy's obedience by 6 July"), result, paywall recap, and even the bonus modal. Owner's emotional investment in the *dog* is the lever, not the owner's own self-image.
- **Competitor-cost anchor on the landing page** — explicit $1,350–$6,000/mo boarding-school and $120–$2,000/mo trainer figures (cited to Dogster) make a €0.27–€0.67/day subscription feel trivial. Pets vertical leans hard on "professional training is expensive" substitution.
- **Event-deadline → projected completion date** ("Just in time for Vacation") — turns the user's own answer into a self-generated deadline that the plan timeline is mapped onto.
- **Mid-loader interrupt micro-questions** keep the user tapping during the fake "Creating plan…" wait, preventing drop-off and gathering 2 more data points.
- **Photo-rich problem screens** (real dogs barking/fighting/begging) make each behavior question visceral.
- **Bonus stacking that totals ~€220 free** right before the payment method screen, immediately followed by "You just saved €251.99".

## Notable Copy & Microcopy
- "The last plan you'll ever need to fix Buddy's behavior challenges."
- "We predict you'll increase Buddy's obedience level by 6 July 2026 — Just in time for Vacation."
- Slider labels "Devil … Angel" and "I need more information … I'm totally prepared."
- "We say no to prong collars, punishments, yelling, and dominance-based training" (FAQ — values-aligned positioning against aversive methods).
- Downsell: "We want you to find success so we are offering the additional discount."

## Weaknesses / Risks
- **Intro-to-€49.99/mo jump** is steep and buried in fine print; €19.99 → €49.99/month rolling charge is a likely source of chargebacks/refund disputes (note dedicated phone line + email-only cancellation, which adds friction).
- **No Apple/Google Pay** at checkout — only PayPal + card; on mobile this is meaningfully higher friction than one-tap wallets that competitors offer, likely depressing mobile conversion.
- **"This chart is for illustrative purposes only"** disclaimers on every projection chart signal the obedience-level forecast is invented, which a skeptical user may notice.
- Very long quiz (~25 screens) with several sliders/multi-selects stacked — heavy ability-cost; relies on the dog-name personalization and frequent give-screens to keep fuel up.
