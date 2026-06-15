# Heartify (Health / Heart Monitoring) — Live Funnel Walkthrough

## Overview
- **URLs:** https://heartify.world → `/auth/signin` (app login gateway); marketing site at https://heartify.io.
- **Entry promise:** "#1 heart health app" / "Heart Health Monitor — Personalized all-in-one app to monitor your wellness." Measures heart rate + HRV using the phone camera + flashlight + finger (PPG).
- **Personalizes on:** Unknown from the web — the personalization quiz is inside the iOS app, not on the web.
- **~Step count:** Web has no quiz. App-only onboarding.
- **Paywall reached?** NO — **hard-blocked**. There is no web quiz-to-paywall funnel. Both `heartify.world` CTAs ("Sign In" / "Create Account" / "Start your Journey") route to `/auth/signin`, and "Create Account" goes straight to `/auth/signup/email` demanding **email + password + Terms consent** before any content. Per the no-account / no-password rule I stopped here. The marketing site heartify.io also gates on a Medical Disclaimer modal and its "Get Started" CTAs likewise point to the auth wall / App Store. The real quiz-to-paywall lives inside the iOS app (Heartify is "free-to-download and available on the iOS platform").

## Flow Walkthrough (what was observable on the web)
1. **heartify.world** → immediately `/auth/signin`: "Welcome to Heartify — #1 heart health app" with two buttons: **Sign In** (red) / **Create Account** (dark). Left panel shows isometric health-metric tiles (sleep, activity bars, heart/ECG, running figure, clipboard/report). Cookiebot consent banner (Necessary/Preferences/Statistics/Marketing toggles; chose **Deny** — easy reject available).
2. **Create Account** → `/auth/signup/email`: hard wall. Fields: Email address, Your password, checkbox "I agree to Terms of Use and consent to processing of my personal data under Privacy Policy", "Continue". No quiz precedes it. **Stopped — cannot create account / enter password.**
3. **heartify.io (marketing site)** — gated by a **Medical Disclaimer modal (Agree/Disagree)** that must be acknowledged before browsing. Disclaimer is unusually prominent and repeated in the footer.

## Paywall Architecture
NOT reached (app-gated, account required). No pricing, tiers, trial terms, timer, Apple/Google Pay, or downsell were observable on the web.

## Standout Techniques (vertical-unique — observed from marketing site)
- **Compliance-first gating** distinctive to the health/medical vertical: a mandatory Medical Disclaimer modal (Agree/Disagree) on heartify.io, plus heavy repeated disclaimers — "Not intended for medical use. Always consult your doctor," "HEARTIFY LLC IS NOT A LICENSED MEDICAL CARE PROVIDER," "The App is not a clinical pulse oximeter." This both manages legal liability and, paradoxically, builds a kind of candor-based trust.
- **Anti-AI trust signal:** "We do not use any neural networks or AI at all in any of our calculations or metrics for your safety." — deliberately positioned as a safety/trust differentiator in a vertical where users fear black-box health claims.
- **Hardware-free measurement hook:** "All you need is a camera, flashlight, and your finger" — the camera-PPG heart-rate measurement is the novelty/curiosity hook (the demo screen shows "65 bpm — Measuring").
- **Feature framing around outcomes:** Heart Rate Monitor, Detailed Report, Health Insights, Special Tests ("heart recovery rate and your 10-year cardiovascular risk"), Expert Content (100+ pieces), Exporting Reports ("to share with your doctor").
- **App-store-funnel model:** unlike the other three (web quiz → web paywall), Heartify pushes users straight to the iOS app, so the monetizing quiz/paywall happens in-app behind account creation — a structurally different acquisition path.

## Notable Copy & Microcopy
- "#1 heart health app."
- "Heartify measures your heart rate and HRV with your phone's camera."
- "Special tests to assess your heart recovery rate and your 10-year cardiovascular risk."
- Disclaimer: "Not intended for medical use. Always consult your doctor. Heartify does not provide medical advice."
- Review: "I can measure my heart rate with an iPhone camera! Awesome technology! — Emma."

## Weaknesses / Risks
- **Web dead-ends at an account wall** with no value delivered first — a web visitor who clicks "Start your Journey" hits email+password immediately, which is high friction and offers zero of the quiz-style value-loading the other funnels use. Likely a deliberate app-redirect strategy, but on web it reads as an abrupt gate.
- **Medical/legal disclaimers are very heavy** and front-loaded (Agree/Disagree modal + repeated all-caps text) — necessary for compliance but can spook a cautious health user before any benefit is shown.
- **iOS-only** — no Android, no web product; cuts off a large share of traffic at the door.
- Could not assess pricing, trial mechanics, or paywall psychology because they are app-internal.

## Why skipped / blocked
Heartify has no public web quiz-to-paywall funnel. The web is a thin App-Store gateway whose only forward path is account creation (email + password). Creating accounts and entering passwords are prohibited actions, so the walkthrough was stopped at the signup wall after documenting all visible marketing/offer content.
