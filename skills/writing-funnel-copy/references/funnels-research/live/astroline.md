# Astroline (Astrology) — Live Funnel Walkthrough

> Walked: 2026-06-15 (capture date from repo history).

## Overview
- **URL:** https://sub.astroline.today (lands on `/quiz-pp` — the palm-reading quiz variant)
- **Vertical:** Astrology / natal-chart personalization, with a relationship/"best match" angle layered on top
- **Entry promise:** "Personalized astrology report with powerful predictions" — "Complete a 1-minute quiz to get a personalized prediction." (Honest disclaimer immediately under it: "The result is not guaranteed and may vary from case to case.")
- **Personalizes on:** Full natal-chart inputs — gender, birth date (→ zodiac), birth **time**, birth **place**; then future goals, favorite color, and classical element. Computes Sun/Moon/Ascendant + modality + polarity.
- **Length:** 14 steps (progress reads "N/14"). Note the counter advances on transitions, so several screens share a number.
- **Paywall reached?** **NO.** Step 13/14 is a hard **palm-photo gate** (camera capture or file upload) that runs real ML hand-detection. With no camera and a synthetic uploaded image, it returns "Oops! Sorry, we couldn't spot a hand in your photo." There is **no skip link**. The paywall (step 14, after an email/loader) sits immediately behind this gate but could not be reached without a genuine photo of a hand. All 13 preceding steps were fully captured.

## Flow Walkthrough
| Step | Screen type | Quoted copy | Options | Lever | Branch notes |
| --- | --- | --- | --- | --- | --- |
| 1 | Intro + first question | "Personalized astrology report with powerful predictions" / "Select your gender to start" | Female / Male / Non-binary (icon cards) | Expectation match + zero-effort first commitment (gender ≈ 100% answerable) | Gender likely branches copy/avatar (we chose Female → female avatar later) |
| 2 | Birth-date picker | "When's your birthday?" / "It's also important to know your date of birth for making complete and accurate predictions" | Zodiac-sign grid **cross-bound** to a Month/Day/Year wheel | Investment escalation; precision = credibility | Picking a sign moves the date wheel and vice-versa (clever 2-way binding) |
| 3 | Birth-time picker | "Do you know your birth time?" / "This helps us find out where planets were placed in the sky at the moment of your birth" | Time wheel (12:00 AM) + **"I don't remember"** escape link | Authenticity/precision priming; low-friction opt-out | "I don't remember" advances without data |
| 4 | Birth-place autocomplete | "Where were you born?" / "The place is important to explore your core personality traits, needs, and desires" | City autocomplete (geo-defaulted placeholder e.g. Lisbon) | Completes the natal-chart data trio (date+time+place) | — |
| 5 | Confirm place → **priming loader** | "Mapping your birth chart…" | Rotating checklist: 🔮 inner self, 💓 emotional side, 👤 outer self, 🧠 intellectual, ❤ approach to love, 💪 strengths, 🚀 changes, 🧩 challenges, 🧭 approach to life, 🦋 transformations, 🌙 intuition & dreams | **Value-loading loader** — each line previews a value the report delivers; rotating natal-chart graphic | Pure give-screen after the effort cluster |
| 5→6 | Birth-chart reveal | "Your chart shows a rare spark — let's discover your best match" | Glowing natal-chart wheel + computed **Pisces Moon / Capricorn Sun / Aries Ascendant** | Self-generated value (Hitchcock) + flattering specificity ("rare spark"); seeds the "best match" relationship hook | Placements computed from entered date |
| 6 | Chat-bubble reveal | "Your chart shows a rare spark — let's discover your best match" (typed out letter-by-letter in a speech bubble from an avatar) | Continue (disabled until type-on finishes) | Conversational pacing; "rare spark" highlighted teal | — |
| 6→7 | **Forecast-accuracy meter** | "Forecast accuracy" 0% → animates to 34% / "The cosmic energy is building up! Share a bit more to reveal what's driving you" | Liquid-fill orb gauge | **Investment meter** — frames remaining questions as raising your accuracy %; commitment device | Re-shown at 7 & 8 |
| 8 | Multi-select goals | "What are your **goals** for the future?" | ❤ Family harmony, 💼 Career, 💊 Health, 💍 Getting married, 🌎 Traveling, 🎓 Education, 👥 Friends, 👩‍🍼 Children | Motivation/value capture → drives paywall promise; explicit Continue | Multi-select |
| 9 | Single-select (tap-advance) | "Which of the following colors do you prefer?" / "The color is important for better personalization" | Red / Yellow / Blue / Orange / Green / Violet (color swatches) | Low-effort momentum keeper; auto-advances on tap | — |
| 10 | Single-select (tap-advance) | "Which element of nature do you like the best?" / "The element of nature is important for better personalization" | Earth / Water / Fire / Air | The 4 classical astrology elements → feels diagnostic; auto-advances | — |
| 11 | **Identity card** | "You — Woman • Capricorn • Earth" | Capricorn-glyph avatar; **Cardinal** (Modality), **Feminine** (Polarity); "Your Details" → Pisces Moon / Capricorn Sun / Aries Ascendant | Identity mirror + investment recap; reflects all inputs back as a rich profile | Card content driven by all prior answers |
| 11→12→13 | Chat-bubble reveals (repeat) | "Your chart shows a rare spark — let's uncover how you can use this power!" | Continue (disabled until typed) | Re-anchors the "rare spark" frame; builds toward CTA | Same card persists across 11–13 |
| 13 | **Palm-photo gate** | "Take a photo of your left palm" / "These readings are for entertainment purposes only and should not be taken as 100% accurate" / "Privacy is a priority for us. We only process non-identifiable data to ensure anonymity" | Hand outline w/ life-area labels (👩‍🍼 Children, 💼 Career, 💞 Marriage, ⏳ Big Change, 💸 Money); buttons "Take a photo" (camera) / "Upload palm photo" | Adds a **second reading modality (palmistry)** to multiply perceived value right before paywall; privacy reassurance to defuse the obvious "why do you want my hand?" objection | **Hard gate** — real ML hand-detection; failed photo → "Oops! Sorry, we couldn't spot a hand in your photo" → only "Let's try again" |
| 14 | (Not reached) | — | — | Email gate + paywall expected here | Gated behind step 13 |

## Paywall Architecture
**Not reached** — blocked by the palm-photo ML gate at step 13/14. Forensics from `localStorage` confirm a billing store exists with keys: `purchase`, `purchased`, `paymentMethod`, `discountEndDate`, `specialOfferEndDate`, `trialPrice`, `postcode` — implying the paywall uses a **trial price**, a **discount countdown** (`discountEndDate`) and a separate **special-offer countdown** (`specialOfferEndDate`, i.e. a checkout-exit / second-offer timer). Pricing values were empty pre-paywall, so exact prices/tiers could not be recorded this session.

Per Astroline's known pattern (not verified live here), the paywall is typically a trial-priced weekly subscription with a per-day reframe and an introductory discount timer; treat the above as inferred, not confirmed.

## Standout Techniques
- **Two-way bound date/zodiac picker (step 2):** selecting a zodiac sign scrolls the date wheel and vice-versa — reduces friction and reinforces the astrology framing.
- **Natal-chart data trio as credibility ramp (steps 2–4):** date → time → place, each justified by a one-line "why we need this" that ties the input to better/"complete and accurate" predictions. Escalating personal-info commitment.
- **Priming loader as value catalog (step 5):** "Mapping your birth chart…" lists 11 value categories the report covers — turns dead time into a feature preview (System-1 familiarity + give-screen after effort).
- **Hitchcock reveal (step 5→6):** never says "your report is amazing"; shows a real computed chart + "rare spark" and lets the user conclude their own specialness.
- **Forecast-accuracy investment meter (steps 6–8):** a fill-gauge that rises as you answer — reframes effort questions as *increasing your own result quality*, exploiting completion/consistency bias.
- **Identity mirror card (step 11):** a polished "You — Woman • Capricorn • Earth" card with Modality/Polarity/placements — recaps every input as a flattering identity, deepening sunk-cost before the paywall.
- **Conversational chat-bubble pacing:** repeated avatar speech bubbles type out copy and disable Continue until finished — controls tempo and forces the message to land.
- **Palmistry value-multiplier before paywall (step 13):** stacks a second divination modality (palm reading across Children/Career/Marriage/Money) on top of astrology to inflate perceived value at the highest-intent moment — with a pre-emptive privacy reassurance.

## Notable Copy & Microcopy
- Honest expectation-setting: "The result is not guaranteed and may vary from case to case." (step 1) and "These readings are for entertainment purposes only and should not be taken as 100% accurate" (step 13) — compliance + trust.
- Each data ask is justified: "important to know your date of birth for making complete and accurate predictions" / "where planets were placed in the sky at the moment of your birth" / "explore your core personality traits, needs, and desires."
- Motivational nudge on the gauge: "The cosmic energy is building up! Share a bit more to reveal what's driving you."
- Flattery hook reused 3×: "Your chart shows a rare spark — let's uncover how you can use this power!"
- Privacy defusal: "Privacy is a priority for us. We only process non-identifiable data to ensure anonymity."

## Weaknesses / Risks
- **Palm-photo gate is a real drop-off risk and an automation/edge-case fragility.** Requiring a left-palm photo (camera or upload) with ML detection and *no skip path* will lose users without a usable camera, privacy-averse users, or anyone whose photo fails detection. The only failure affordance is "Let's try again" — a dead end if the user can't satisfy it. (We hit exactly this: synthetic image → "couldn't spot a hand," no way forward.)
- **Slow cross-fade transitions** between screens (multi-second fades) add perceptible latency and burn a little fuel on every step.
- **Progress counter is misleading** — the same "N/14" number is shown across several distinct sub-screens (e.g. the chart reveal + chat bubble share a number), so the "1-minute quiz" promise vs. actual step count may feel longer than advertised.
- **Repetition of the "rare spark" bubble** across steps 11–13 risks feeling padded to users who notice the identical line three times.
- Desktop rendering of this mobile-first SPA leaves large empty side margins (cosmetic; not a conversion issue on intended mobile traffic).
