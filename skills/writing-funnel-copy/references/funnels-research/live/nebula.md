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

## Update (verified August 2026): operator named in FTC enforcement action

Nebula's operator, Obrio Ltd., is a defendant in *FTC v. GM Universeapps Ltd.*, No. 4:26-cv-05232 (N.D. Cal.) — the FTC's June 2026 action against a group of 15 corporations and 8 individuals behind quiz-funnel subscription apps (~$250M global revenue 2023–mid-2025). Timeline: complaint filed June 2, 2026; ex parte TRO with asset freeze June 4; stipulated preliminary injunction June 30 (Growthmind Labs, Gurudocs, Evertech, Yolo Brothers, AmoApp + five individuals); preliminary injunction as to the remaining defendants, including Obrio, entered per the FTC's July 20, 2026 docket update. The complaint alleges FTC Act §5 and ROSCA violations: quiz-driven commitment building paired with obscured auto-renewal terms and deliberately hard cancellation. Sources: [FTC case page](https://www.ftc.gov/legal-library/browse/cases-proceedings/growthmindwisey), [complaint PDF](https://www.ftc.gov/system/files/ftc_gov/pdf/Growthmind-Wisey-Complaint.pdf).

Two consequences for this corpus:

- **The outage above now has a plausible cause.** The walkthrough attempt found appnebula.co serving gateway errors and non-hydrating stubs; that is consistent with an operator under an asset freeze winding infrastructure down, though the outage itself was recorded before the connection was known and the link is inferred, not confirmed.
- **Use Nebula as a structure reference only, never a compliance reference.** The quiz architecture (progressive personalization, per-day price reframe, checkout-exit downsell) remains a widely copied pattern. But the enrollment-and-cancellation posture — the part the FTC complaint targets — is now a documented anti-pattern: clear auto-renewal disclosure and easy cancellation are the compliance floor, and this case shows the enforcement downside of treating them as conversion levers.
