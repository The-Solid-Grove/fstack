# Nebula (Astrology) — Live Funnel Walkthrough

## Overview
- **URL attempted:** https://appnebula.co (also tried https://appnebula.co/en/ and https://appnebula.co/en/witch-power/)
- **Vertical:** Astrology / spiritual guidance (web-to-app subscription quiz)
- **Status: SKIPPED — funnel unreachable from this environment.**

## Why skipped
Nebula did not serve a usable funnel during this session, after 4+ retries across multiple entry paths:

- **Apex `https://appnebula.co/`** returned a hard infrastructure error: `upstream connect error or disconnect/reset before headers. retried and the latest reset reason: local connection failure` (Envoy/Istio gateway 5xx — backend unreachable).
- **`https://appnebula.co/en/`** returned an HTTP **200 but an empty stub** document: ~39 characters of HTML, **0 `<script>` tags**, empty `<body>` (0 chars of text), no console output, and **no follow-on network requests** (no JS bundle, no API/XHR calls). The SPA never hydrated.
- **`https://appnebula.co/en/witch-power/`** stayed blank/white and the URL did not advance — same non-hydrating shell.

This is a server-side / edge outage or geo-block on Nebula's infrastructure, not a client-side issue I can work around (the document loads but the application bundle is never served/executed). No quiz screens, copy, or paywall were observable.

## Recommendation
Re-attempt later (likely transient gateway issue) or from a different network/region. Nebula's funnel is well-documented as a long astrology quiz (gender → relationship status → birth date/time/place → goals → personalized birth-chart + "cosmic" reveals → email gate → trial-priced paywall with per-day reframe, Apple/Google Pay, discount timer, and a checkout-exit downsell), but **none of that could be verified live here**, so it is intentionally not recorded as observed.
