# Stylix (Style / personal styling) — Live Funnel Walkthrough

## Overview
- **URL:** https://sub.stylix.app (mobile-style centered web funnel; desktop renders narrow column)
- **Entry promise:** "Look and feel your best in clothes that flatter you" + social proof "100 000+ women changed their lives with Stylix." Hero shows a woman with an overlaid "Light Summer / Best colors" palette card — signals the core deliverable is a personal color + style analysis.
- **Personalizes on:** age, style goals (top-3), ideal-wardrobe aesthetic, wardrobe utilization, struggles, height/weight, body shape, body parts to accentuate, silhouette correction goals, location/climate, everyday lifestyle, brand price tier, seasonal budget, aesthetic, and finally a face-photo color analysis.
- **Step count:** Quiz UI counts "17" steps (progress is segmented Goals → Struggles → Fit → Lifestyle → Colors), then continues past 17 into a loader + final "color power" gate. ~20+ real screens including motivation/loader interstitials.
- **Paywall reached?** NO — hard-blocked at a mandatory face-photo gate ("Take a photo of yourself for a color analysis," Take a photo / Upload face photo, no skip). Per the no-biometric rule I stopped here. Pricing not observed.

## Flow Walkthrough (ordered)
1. **Landing/Hero** → entry. Copy: "Look and feel your best in clothes that flatter you" / "100 000+ women changed their lives with Stylix." Visual: woman + "Light Summer / Best colors" swatch row. CTA: **Start**. Lever: expectation match + social proof + curiosity (what's MY palette?). (Cookie banner via CookieScript; declined non-essential via Decline All.)
2. **Intro** → "Know which colors and styles work for you" / "Answer a few questions about your looks and fashion goals to let our AI stylist create a perfect wardrobe for you." CTA Continue. Lever: frames effort as AI-personalization.
3. **Color-analysis teaser (give)** → animated face split into a warm side (red, ✗) vs cool side (blue, ✓). Lever: demonstrates the "flattering colors" value visually before asking anything.
4. **Q: Age** → "How old are you?" / "We'll tailor a guide to your age, lifestyle, personal style, challenges, and goals." Options: Under 18 / 18–24 / 25–31 / 32–38 / 39–45 / 46+. Auto-advances on tap (low effort first question).
5. **Q: Goals (multi, top-3)** → "With Stylix, I hope to…" Options: Define my personal style / Discover my flattering colors / Learn to dress my body shape / Discover stylish cuts and fits / Keep up with fashion trends / Learn to mix and match clothes / Create a wardrobe for my lifestyle / None of the above. Lever: commitment + self-segmentation.
6. **Motivation refill** → "Imagine a closet where every piece sparks joy" / "We'll craft your personal style roadmap so every outfit feels unmistakably you." Then a roadmap diagram (Goals→Struggles→Fit→Lifestyle→Colors) showing the journey ahead.
7. **Q: Ideal wardrobe** → "What best describes your ideal wardrobe?" Versatile and comfy / Classy and polished / Elegant and chic / Bold and unique / None of the above.
8. **Q: Wardrobe utilization (pain)** → "How much of your current wardrobe do you wear regularly?" 10% / 25% / 50% / 75% / More than 90%. Lever: activates the "I have nothing to wear / wasted closet" pain.
9. **Q: Struggles (multi)** → "What are your biggest wardrobe struggles? Select as many as you like." Choosing versatile pieces / modern cuts / flattering colors / clothes that fit well / Combining colors and patterns / Combining different styles / Something else.
10. **Motivation refill (anchoring graph)** → "Let's find styles that make you feel unstoppable" / "To curate your perfect wardrobe, let's quickly map out your natural features." Rising "Confidence level vs Time" curve with "With Stylix" line above "On Average."
11. **Q: Height** → "Your height" (Inch/Cm toggle; Ft/In fields, validates input).
12. **Q: Weight** → "Your weight" (Lb/Kg toggle).
13. **Q: Body shape** → "What is your body shape?" illustrated grid: Hourglass / Bottom Hourglass / Top Hourglass / Spoon / Inverted Triangle / Triangle / Rectangle.
14. **Q: Accentuate (multi)** → "Which parts of your body do you prefer to accentuate?" Waist / Legs / Shoulders / Bust / Other.
15. **Q: Silhouette goals (multi)** → "Is there anything you want to correct in your silhouette?" I want to appear slimmer / define my curves / appear taller / appear shorter / balance my top and bottom / I am happy with my silhouette.
16. **Milestone (commitment)** → "Your wardrobe plan is almost ready" / "Just a few final steps — let's tailor it to your lifestyle, aesthetic, and budget." CTA **Let's Do It!** Progress-map graphic (Goals→Fit→Lifestyle).
17. **Q: Location** → "I live in…" / "We'll customize your capsule wardrobe for your local climate and lifestyle." Geolocated prefilled (e.g., "Lisbon, Área Metropolitana de Lisboa, Portugal"). After confirming, shows **live local weather** (Temp 37°C, Humidity 8%, UV index 0) — Hitchcock-style proof the personalization is real.
18. **Q: Lifestyle (multi)** → "What best describes your everyday lifestyle?" Office and business meetings / Errands and casual hangouts / Cultural events and date nights / Creative workshops and parties / Something else.
19. **Q: Brand tier** → "Which fashion brands do you prefer?" Budget-friendly / Mid-range / Luxury. (price-sensitivity qualifier)
20. **Q: Budget (anchor)** → "What is your seasonal shopping budget?" Less than $200 / $200–$400 / $400–$800 / $800–$1200 / $1200+. Lever: anchors a future subscription against hundreds in clothing spend.
21. **Q: Aesthetic (image cards)** → "Which aesthetic best reflects your style?" Casual / Classy / Feminine / Artsy (street-style photos).
22. **Loader (priming)** → "Preliminary progress… Stylix will help you save on clothes through precise personalization." Animated coin-stack graphic resolving to **"–56% money spent on clothes"** (Without Stylix App tall stack vs With Stylix App small stack). Counts 1%→100% slowly (~40s).
23. **Final commitment gate** → "89 % done — let's unlock your color power" / "Just one step left to reveal your full personal style guide." Declining "Overspending risk vs Style match" curve. CTA **Let's Make It 100%!**
24. **Photo intro** → "Now, let's scan your face to complete color analysis" / "Our AI Stylist will suggest colors that highlight your natural beauty." CTA **I'm Ready for Analysis**.
25. **HARD GATE: Face photo** → "Take a photo of yourself for a color analysis" / "Take a solo close-up portrait without wearing glasses or other accessories." Privacy note: "We only store non-identifiable data and promptly delete it to ensure your safety." Options **Take a photo** / **Upload face photo** — no skip. **STOPPED HERE.**

## Paywall Architecture
Not reached — gated behind mandatory biometric/face-photo upload. The pre-paywall value stack that WOULD feed it: –56% clothing-spend savings claim, personalized color "season," body-shape fit rules, climate-aware capsule wardrobe, and a seasonal-budget anchor ($200–$1200+). Pricing, tiers, trial terms, and Apple/Google Pay placement could not be observed.

## Standout Techniques (vertical-unique)
- **Color "season" as the hero hook** ("Light Summer / Best colors" palette on screen 1) — the deliverable is identity-flavored ("discover your color power"), very style-vertical.
- **Live local weather injection** after the location step — turns an abstract "we personalize" claim into concrete, verifiable proof (Hitchcock self-generated belief).
- **Money-savings reframe in a fashion funnel** — the "–56% money spent on clothes" coin-stack loader reframes a style subscription as a money-SAVER, pre-justifying price against the seasonal-budget anchor collected two screens earlier.
- **Biometric face scan as the final lock-in** — investment escalation taken to its maximum: by the time you're asked for a selfie you've answered ~20 questions; the "color analysis" framing makes the selfie feel functionally necessary rather than data harvesting.
- **Segmented progress map** (Goals→Struggles→Fit→Lifestyle→Colors) reused across interstitials to show how far you've come and reduce abandonment.

## Notable Copy & Microcopy
- "100 000+ women changed their lives with Stylix."
- "Imagine a closet where every piece sparks joy."
- "Let's find styles that make you feel unstoppable."
- "Your wardrobe plan is almost ready — just a few final steps."
- "–56% money spent on clothes" (Without vs With Stylix App).
- "89 % done — let's unlock your color power."
- "Privacy matters to us. We only store non-identifiable data and promptly delete it to ensure your safety." (trust microcopy directly under the photo CTA — pre-empts the obvious privacy objection at the highest-friction step).

## Weaknesses / Risks
- **Mandatory face photo with no skip is a major drop-off cliff** placed BEFORE any price is shown — many users (and any privacy-cautious segment) will bail at 89% rather than upload a selfie. A "choose your colors manually" fallback would recover these.
- **Slow, lengthy loader** (~40s, 1→100%) on top of an already long ~20-screen quiz risks burning fuel late in the decision zone.
- **Heavy body-measurement + weight collection** (height, weight, body shape, parts to accentuate, silhouette "corrections") is sensitive and could feel judgmental for a style product; "I want to appear slimmer/shorter" framing may alienate some.
- The "–56% savings" claim is unsubstantiated on-screen (no source), a potential trust/regulatory risk.
