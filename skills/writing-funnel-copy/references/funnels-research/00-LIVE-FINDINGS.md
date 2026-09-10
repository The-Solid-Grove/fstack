# Live-Funnel Findings — What 20+ Real Web2Web Funnels Actually Do

Synthesis of **live browser walkthroughs** of funnels from `funnels.xlsx` (the
Webfunnels.club curated set), one per `live/*.md`. This complements the
10 code-level teardowns: the live walks reveal what code can't — **real prices, real
timer/rollover behavior, real checkout-close downsells, and the gating mechanics** that
gate real users.

**Funnels walked (~24 across ~20 verticals).** Full paywall reached: Hint, Muscle
Booster, Fastic, Ahead, Keiki, Coursiv, IQ Brain, PawChamp, Promova, Colonbroom, Blesse,
Acely. Partial/structure or pricing-only: Astroline, Headway, Blinkist, Imprint, Luvly,
LoveStrive, Geozilla, Stylix, Femia, Heartify, Blushed, Nebula, Plantin.

---

## 1. The universal paywall pricing architecture (confirmed live, near-identical everywhere)

Almost every subscription funnel ships the **same** price construction:

1. **3 tiers**, mapped to duration: trial-week / 1-month / **3-month (pre-selected "Most
   Popular"/"Best value")** / sometimes 6–12-month.
2. **Per-day reframe** as the headline number, over a **crossed-out anchor**:
   - Muscle Booster €0.28–0.99/day · Fastic €0.22–0.86/day · Ahead €0.16–0.65/day ·
     Keiki €0.19–0.36/day · PawChamp €0.27–0.67/day · Promova €0.49/day · Coursiv tiers.
3. **Discounted FIRST TERM → much higher rollover**, buried in fine print — the single
   most consistent (and most compliance-risky) pattern:
   - Muscle Booster €15.19 → **€38.95/mo** · Fastic €9.99 → **€39/mo** ·
     Ahead €31.99/3mo → **€79.99/3mo** · Keiki €10.73 → **€39.99** ·
     Coursiv €19.99/4wk → **€39.99/4wk** · IQ Brain **$1.98 today → $28.80/mo** ·
     PawChamp €19.99 → **€49.99/mo** · Hint €1.00 trial → **€29.99/mo**.
4. **A countdown timer that is evergreen (resets / never really expires)** — present on
   essentially every funnel: "10:00", "14:57", "9:59", "16:50", "24h". Treat as the
   default, not the exception.

**Takeaway:** the per-day number and the crossed-out anchor are the conversion levers;
the rollover price is the monetization. If you build this, you MUST disclose the rollover
clearly (it's the top legal exposure) — but the *structure* is table stakes.

## 2. Checkout-close exit-intent downsell is REAL and COMMON (correcting the code-teardown)

The local catalog funnels had downsell *files* but mostly unwired — so I'd flagged
downsell as "rare." **Live, it is everywhere and it fires:**

- Muscle Booster: close checkout → timer resets, discount deepens **61% → 69% → 71%**.
- Ahead: close → "65% saw improvement" → bumps to **70% off** (3mo €31.99 → €23.99).
- Promova: close → **$41.99 → $29.99**, trial **$8.39 → $4.99**.
- Colonbroom: **"I do not want this special offer"** decline-framed downsell.
- PawChamp: exit-intent "additional discount."
- Keiki: the **scratch-card** discount *replaces* a separate exit downsell.

**Takeaway:** a close-triggered deeper offer (or a gamified earned-discount that
pre-empts it) is standard. Ship one.

## 3. New mechanic: the "withhold the result, pay to reveal" paywall

A curiosity-gap monetization distinct from the value-recap paywall — the funnel computes
a result, shows a teaser, and **locks the actual answer behind payment:**

- **IQ Brain:** 20 timed Raven's-style puzzles → shows only a *range* ("100–120, higher
  than 80%") with the exact score behind a "?" → **$1.98 trip-wire** to unlock. Includes
  an **anti-gaming guardrail** that rejects uniform answers (protects result credibility).
- **Geozilla:** fake "Searching… connecting to cellular base station" loader → map zoom →
  **"Number located! City: HiddenCity"** → pay/account to reveal.

**Takeaway:** when the product's value IS a result (score, location, match, diagnosis),
withholding it behind a low trip-wire converts on pure curiosity. Pair with a guardrail
so the result stays believable.

## 4. Gamified earned-discount + name-personalized promo codes (confirmed live)

- Keiki scratch-card → **`MIA_2026`** (child's name) "applied, 10 min left."
- Coursiv → **`Alex_15jun2026_1q3B`** (name + date).
- Promova → scratch card → **`LIMITED-SAVE-43`**; Hint → **`MYHINT93`** pre-applied.

The personalized code makes the discount feel *issued to you*, not generic. Common and
effective.

## 5. Wallet pay is NOT universal (nuance vs. best practice)

Best-practice says "Apple/Google Pay above card (+10–15%)." In the wild it's **mixed**:

- Present: Muscle Booster (Apple+Google+PayPal), Coursiv (Apple only), Hint
  (PayPal→Apple→Google→card).
- **Absent (PayPal + card only):** Fastic, Ahead, Keiki, PawChamp, IQ Brain, Acely,
  Colonbroom, Blesse.

PayPal is the most consistently present alternative payment. Wallet pay is a real
opportunity many top funnels still skip — but PayPal-as-the-one-tap-option is the de-facto
minimum.

## 6. Gating mechanics — and which verticals live in-app, not on web

Real funnels gate hard, both to qualify intent and (often) because the paywall lives in
the native app:

- **Biometric/photo gates:** palm scan (Astroline, Hint), selfie "color/skin analysis"
  (Stylix, Luvly) — a no-skip lock-in right before the result. High commitment, but also
  a hard drop-off point and a research/edge-case blocker.
- **Account+password walls before paywall:** Imprint, Heartify, Geozilla, LoveStrive.
- **App-Store-only paywalls (no web checkout):** AI companions (Blushed/Blush — partly to
  navigate NSFW + payment policy), women's health (Femia), heart health (Heartify).
- **Outright down/blocked at walk time:** Nebula (edge outage), Plantin (init hung),
  LoveStrive ("not accepting new users"), Headway quiz route errored.

**Takeaway:** choose web-vs-app paywall deliberately. Verticals with platform-policy risk
(NSFW, medical) or strong retention-in-app tend to push the paywall into the app and use
the web funnel only to capture the email/install.

## 7. Vertical-specific levers worth stealing

| Vertical | Distinct lever (observed) |
| --- | --- |
| Astrology | Birth data + palm scan = self-generated value; "Forecast accuracy" meter that rises as you answer (effort reframed as result quality). |
| IQ test | Timed puzzles + **locked score reveal** + anti-gaming guardrail; $1.98 trip-wire → high monthly. |
| Income / finance | **Job-security FOMO** ("falling behind colleagues"; "humans with AI replace humans without"); dated shareable **certificate**. |
| Pets | **Pet-name** woven throughout + dated projection ("obedience up by 6 July, just in time for Vacation") + competitor-cost anchor (boarding $1,350–6,000/mo). |
| Ecommerce supplement | **Per-bottle supply-duration** pricing (3-mo vs 6-mo supply), real shipping checkout, "+SECRET GIFT", Ozempic comparison. |
| Religion | **Name-on-cover physical product** with live preview; **one-time purchase**, not subscription; faith-native proof (scripture + clergy). |
| Edtech (test prep) | **Per-MONTH** pricing (not per-day), **test-anxiety** emotional framing ("that feeling is normal"), **parent-as-payer** routing, score-improvement money-back guarantee (+200 SAT). |
| Geo / utility | **Fear/safety** not self-improvement; fake "searching cellular tower" theater + located-but-hidden reveal. |
| Beauty / face-yoga | Selfie analysis; **cosmetologist-cost substitution** ("–56% money on clothes" / "vs €X cosmetologist"). |
| Language | **Vocab self-estimation** ("mark words you know" → "451 words" + level slider); **tap-and-hold to promise** ritual. |
| Mental / EQ | Clinical authority (Oxford/Cambridge/Harvard), psychometric Likert battery, **AI-pocket-therapist** positioning, in-loader commitment popups. |

## 8. Net adjustments to the playbook (from live evidence)

1. **Add the rollover line to the QA + tricks docs as a first-class item** — it's
   universal and the biggest compliance exposure. Disclose it clearly.
2. **Downsell is standard, not rare** — every serious funnel has a close/scratch deeper
   offer. (Corrects the code-teardown's "rare" note.)
3. **Evergreen timers are the norm** — keep flagging them as an honesty risk, but know
   the whole industry ships them.
4. **Add "withhold-the-result" as a paywall archetype** alongside the value-recap paywall.
5. **Wallet pay is upside, PayPal is the floor** — don't assume Apple/Google Pay; ensure
   at least PayPal one-tap.
6. **Decide web vs in-app paywall by vertical** (policy/medical/NSFW → app; most
   self-improvement → web).

See `00-MUST-DO-TRICKS.md` (live addendum) and `00-QA-CHECKLIST.md` (live addendum) for
these folded into the actionable lists.
