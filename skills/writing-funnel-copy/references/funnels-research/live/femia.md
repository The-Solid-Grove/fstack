# Femia (Women's health / fertility & cycle tracker) — Live Funnel Walkthrough

> Walked: 2026-06-15 (capture date from repo history).

## Status: SKIPPED — interactive quiz-to-paywall not web-accessible
The live screen-by-screen quiz and in-funnel paywall could **not** be reached on the open web. `femia.io` redirects to the marketing site `femia.health`, which is an SEO/marketing + content site, not the interactive onboarding quiz. The actual quiz-to-paywall onboarding runs **in the iOS/Android app** (and on paid-ad landing pages not linked from the public site).

**URLs attempted (all failed to reach a quiz):**
- `https://femia.io` and `https://femia.health` → marketing homepage ("Conceive, nurture, and become a mom — All in one with Femia").
- `https://femia.io/quiz`, `https://femia.io/onboarding` → catch-all redirect back to the homepage (no quiz).
- `https://quiz.femia.health/` → redirects to homepage.
- `https://start.femia.io/`, `https://web.femia.health/` → DNS / frame error (do not resolve).
- Products menu → SEO content pages ("Getting pregnant app", "Prepare for pregnancy") with no quiz/"Take quiz"/"Get my plan" CTA in the DOM.

Per task rules (skip + note why after retries), I stopped after exhausting the obvious entry points rather than installing the app. Below is what IS observable from the public site + corroborating public sources for the vertical's positioning and pricing.

## Overview (from public marketing site)
- **URL:** https://femia.health (canonical; femia.io redirects here).
- **Entry promise / hero:** "Conceive, nurture, and become a mom — All in one with Femia." Positioned as "**Femia – fertility & pregnancy app**" and "#1 Fertility Tracker and Pregnancy App."
- **Personalizes on (per product pages):** cycle/ovulation tracking, body signals (cervical mucus, mood, BBT), conception goals, pregnancy stage.
- **Social proof on site:** "Join 1.2+ million users worldwide" (laurel-wreath badge), star ratings.
- **Paywall reached?** NO (in-app only).

## What's distinct about this vertical (women's health / cycle tracker) — from positioning
- **Goal-state segmentation up front** — fertility funnels typically branch on intent: *trying to conceive (TTC)* vs *tracking cycle / avoiding* vs *already pregnant*. The marketing copy foregrounds the TTC → pregnancy → postpartum journey ("Conceive, nurture, and become a mom").
- **Cycle/biometric data capture** as the personalization engine: last period date, cycle length, symptoms, BBT, cervical mucus — used to generate a personalized fertile-window/ovulation prediction (the self-generated value moment).
- **Medical-credibility framing** (doctor-developed, evidence-based) and a sensitive-data privacy posture are load-bearing trust gates for reproductive-health data.
- **Emotional, high-stakes destination** (becoming a parent) supports a strong point-B/future-state paywall hero rather than utilitarian feature lists.

## Public site content observed
- Homepage: hero "Conceive, nurture, and become a mom / All in one with Femia"; trust bar "Join 1.2+ million users worldwide"; section "Femia – fertility & pregnancy app" with an app mockup showing tiles: "Your chances to conceive today," "Your symptoms forecast," "Your pre-pregnancy to-do list."
- Products page ("Discover Femia's top products"): "Prepare for pregnancy — Learn best tips to conceive and prepare your body for healthy pregnancy" (What's inside).
- Getting-pregnant product page: "Trying to get pregnant? Stay ahead with Femia to pinpoint your prime conception days. Track ovulation, read your body signals, and get personalized tips for maximizing your chances of pregnancy." + "Join over 1.2 million women worldwide who trust Femia ovulation tracker." Feature trio: "Track fertility and ovulation," "Receive daily tips on fertility," "Log symptoms and get instant feedback."

## Pricing (from public/third-party sources, NOT seen in a live funnel)
- App Store subscription (varies by region; fixed per-country price shown in-app).
- Public reviews report a **3-month introductory offer ≈ €25.99**, then renewing to a higher rate (one Trustpilot reviewer cited **~£66 charged after the initial 3-month period**) — consistent with a discounted-intro → full-price auto-renew structure typical of app subscription paywalls. Treat exact figures as unverified (not captured live).

## Recommendation to complete this funnel properly
The Femia quiz-to-paywall must be captured **in the mobile app** (install Femia on iOS/Android and run onboarding) or via a **paid-ad landing URL** (Femia runs these on Facebook/Google with campaign-specific subdomains). A desktop browser on the public site cannot reach it. If a specific ad landing URL is supplied, the live walkthrough can be redone.

## Sources
- https://femia.health/ (marketing homepage)
- https://femia.health/products/getting-pregnant-app/ (product page)
- https://apps.apple.com/us/app/femia-fertility-pregnancy/id1615949241 (App Store listing)
- https://www.trustpilot.com/review/femia.io (pricing reports in reviews)
