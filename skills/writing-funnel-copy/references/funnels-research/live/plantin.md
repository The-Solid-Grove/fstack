# Plantin / PlantIn (Gardening / plant care + identification) — Live Funnel Walkthrough

> Walked: 2026-06-15 (capture date from repo history).

## Overview
- **URL:** https://quiz.myplantin.com
- **Entry promise:** Not observable — the funnel never rendered past its splash screen.
- **Personalizes on:** Unknown (could not reach any question).
- **Step count:** Unknown.
- **Paywall reached?** NO — **SKIPPED: the quiz is hung on its loading splash and never initializes.**

## Status: SKIPPED (site-side hang)
The PlantIn quiz at quiz.myplantin.com loads to a pulsing brand splash (green tulip/PlantIn logo on a white background) and never advances to the first screen.

Troubleshooting performed (well beyond the 1-retry threshold):
- Reloaded the page 4 times (including a `?utm_source=research` variant).
- Waited 30+ seconds cumulatively across attempts.
- Clicked the splash center (no effect).
- `read_page` (interactive filter) returned **no interactive elements** — the page is just the loader.
- Console: **no errors/exceptions.**
- Network: all Next.js app assets (`_next/static/...` JS/CSS/fonts), favicon, and the document returned **200**. The only failures were Google `googletagmanager.com/.../ccm/collect` tracking pings returning **503** (cosmetic, analytics only). Critically, **no app-backend/config/experiment XHR ever fires** — only TikTok pixel (`analytics.tiktok.com/api/v2/pixel`) and other analytics calls. The quiz's own content/config API is never requested, so the splash has nothing to transition to.

**Likely cause:** the funnel's quiz-config / experiment-assignment backend is unreachable or gated from this environment (e.g., geo/region gating to specific ad-traffic locales, a missing required ad-network parameter the app waits on, or the backend host being blocked by the sandbox network). It is a client-init stall, not a crash. A real ad-click from a targeted geo/device would likely supply the parameter/cookie the app is waiting on.

## What was observable
- Brand: **PlantIn** — green tulip/sprout logo, clean white splash, Next.js SPA, "Quiz • PlantIn" page title.
- Analytics stack present: Google gtag/Ads (AW-17491749224, AW-636277487), TikTok pixel, Amplitude, Smartlook session recording — i.e., a heavily tracked paid-acquisition quiz funnel typical of the vertical.

## Standout Techniques / Notable Copy / Paywall Architecture / Weaknesses
Not assessable — funnel did not render. (For the gardening vertical, comparable funnels typically personalize on plant types owned, experience level, light/space conditions, and pain points like overwatering/wilting, then sell an identification + care-reminder subscription. Could not confirm any of this for PlantIn live.)

## Recommendation
Re-attempt from a US/ad-targeted IP and/or with a full ad-style URL (real utm_source/utm_campaign + click id) that the app's init may require, or test on a mobile user-agent, since these quizzes are usually mobile-first and may gate desktop/sandbox traffic.
