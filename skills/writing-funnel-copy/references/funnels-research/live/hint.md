# Hint (Astrology) — Live Funnel Walkthrough

> Walked: 2026-06-15 (capture date from repo history).

## Overview
- **URL:** https://try.hint.app → redirects to **https://hint.app/palmistry** (the palmistry-led variant)
- **Vertical:** Astrology + **palmistry** hybrid (palm-scan reading enriched with astrology), web-to-app subscription
- **Entry promise:** "Find your happiness with highly-personalized predictions" — three expectation-setting pills: **1-min Quiz · Palm scan · Personalized guide**. Disclaimer "For entertainment purposes only" on the landing.
- **Personalizes on:** gender, date of birth (→ Sun sign), the life area you want insight into (Love/Health/Career — primary **branch**), relationship status (Love branch), favorite element, favorite color, head-vs-heart decision style, and a **palm scan** photo.
- **Length:** ~11–12 quiz steps + email gate + promo reveal + long-scroll paywall. Progress bar fills steadily; no numeric counter.
- **Paywall reached? YES — fully captured** (URL `hint.app/landing-paywall`). The palm-scan ML gate (which blocked Astroline) was passed here because Hint's "Choose File" upload accepted a synthetic canvas-drawn hand image (less strict detection than Astroline's). Email gate used the throwaway `funnel.research@example.com`. No payment info entered.

## Flow Walkthrough
| Step | Screen type | Quoted copy | Options | Lever | Branch notes |
| --- | --- | --- | --- | --- | --- |
| 1 | Intro hero | "Find your happiness with highly-personalized predictions" + pills **1-min Quiz / Palm scan / Personalized guide** | "Let's begin" | Expectation match; sets the 3 deliverables upfront; "For entertainment purposes only" compliance | — |
| 2 | **Early social-proof interstitial** | "25 Million+ people have seen their Palm reading with Hint" + 5★ testimonial "It's changed my life!" (Rebecca Bauman) | "Continue" | Trust gate resolved *before* skepticism peaks; live-activity "900+ users have seen their Palm Reading today"; press logos (Mashable, The Sun, HELLO!) | Placed at position 2 — textbook "proof before skepticism" |
| 3 | Single-select | "What's your gender? — In Palmistry, everyone is a blend of masculine and feminine, so it helps to know yours." | Male / Female (illustrated avatars) | Zero-effort first commitment; the "why we ask" justification reduces friction | — |
| 4 | Date input | "What's your date of birth? — Your birth date reveals your core personality traits, needs and desires." | mm/dd/yyyy text field → "Next" | Investment escalation; cleaner than a wheel picker | Drives Sun sign used later ("Cancer Sun") |
| 5 | **Mechanism/priming interstitial** | "Your palms hold a wealth of information about your fate and personality" | "Continue" | Mechanism-before-ask: primes the value of the palm scan with a symbol-covered palm graphic | — |
| 6 | **Primary branch question** | "What aspects of your life do you wish to gain insight into through palmistry?" | Love & Relationship / Health & Vitality / Career & Destiny (only 3 — simplified) | Motivation capture; selection branches downstream copy | Chose Love → relationship-status follow-up appears |
| 7 | Single-select (branched) | "So we can get to know you better, please tell us your relationship status." | Single / In a relationship / Engaged or married / Recently out of something / It's complicated | Self-relevance; only shown on the Love branch | Confirms branching off step 6 |
| 8 | Single-select | "Which element resonates with you the most?" | Earth / Water / Fire / Air (icons) | Astrology framing; low-effort momentum | tap-to-advance |
| 9 | Single-select | "Which color do you like the most?" | Red / Yellow / Blue / Orange / Green / Violet | Engagement filler (shared question-bank w/ other quizzes) | tap-to-advance |
| 10 | Single-select | "Do you make decisions with your head or your heart?" | Heart / Head / Both | Personality input that maps to palm "head line vs heart line" | tap-to-advance |
| 10→ | **Adaptive feedback interstitial** | "Based on our data, **44% of Cancer Sun people** also make decisions using their heart." | "Continue" | Adaptive personalized feedback — combines computed Sun sign + their answer = "the app sees me" | Stat references the birth date entered |
| 11 | **Palm-scan gate (intro)** | "Let's scan your palms — Follow the on-screen instructions, so we can analyze your palm lines and reveal your future, and the secrets of your destiny!" + "No biometric data is collected. All recognition processes are performed on your device." | "Let's do it" | Adds palmistry value-multiplier; privacy reassurance defuses the obvious objection | — |
| 12 | Palm capture | "Take a picture of your palm as instructed" with a **Correct vs Wrong** framing diagram | "Take a picture now" → action sheet: **Take Photo** (camera) / **Choose File** (file) | Good UX (shows right/wrong framing); ML hand-detection | File upload accepted a synthetic hand image (less strict than Astroline) |
| 12→ | Scan/analysis interstitial | Detected fingertip dots + "Life line" overlay on the photo; "We are putting together a comprehensive Palmistry Reading just for you! Wow, looks like there is a lot we can tell about your love life, emotions and problems you might face." | (auto) | Self-generated value; visible "AI analyzing your hand" payoff | — |
| 13 | **Email gate** (`/email`) | "Get your Reading now! Where should we send it?" | Email field + "I accept the Terms & Conditions and Privacy Policy" checkbox → "Continue"; "We securely store your data and don't share it with third parties." | Data capture framed as delivery ("where should we send it"); a teaser result preview (Love locked 🔒 / Health unlocked 🟢 / Wisdom / Career) seeds curiosity + loss aversion | — |
| 14 | **Promo-code reveal** (`/promo-code`) | "You get an exclusive one-time promo code **for a 93% discount**" — code **MYHINT93** | "Continue" | Earned-discount feeling; pre-applied coupon carried into paywall | — |
| 15 | **Paywall** (`/landing-paywall`) | "Your Palm Reading Is **Ready!**" | (see below) | Conversion | — |

## Paywall Architecture
- **URL:** `hint.app/landing-paywall`
- **Sticky top urgency banner:** "Your Report offer: €1.00! Ends in **14:57**" — a **live countdown** (observed ticking down: 14:57 → 14:42 → 14:18). Honest-ish urgency; resets on revisit.
- **Sticky bottom CTA bar:** "Your Personalized Offer Reserved **14:57**" + **Get My Prediction** button (always visible).
- **Hero:** "Your Palm Reading Is Ready!" beside the user's **annotated palm scan** with floating result callout cards — *Children, Big love at, Big change at, Money success at* — several showing **locked padlocks** (loss aversion: the results exist but are gated).
- **Trust block:** "Unlimited insights for life transformation", "900+ users have seen their Palm Reading today", "Trusted by over 25 million people" (5★). Live-activity toast: "**Luis just found out when he'll meet his soulmate**" / "**996 people joined today**" / avatar stack "+993". "WHY YOU CAN TRUST HINT'S PALMISTRY READING" = Authentic Palmistry Expertise / Astrology-Infused Insights / Personalized Connection. "FEATURED IN": The Globe and Mail, Benzinga, Barchart, Yahoo, plus a scrolling press carousel (Forbes, Mashable, The Sun, HELLO!, Daily Mail).
- **Offer (single plan — no tier ladder):** "**Try Hint for 7 days**". 3 benefit checks (detailed palm interpretation; personality/life-path/hidden-potential insights; palmistry+astrology guidance).
- **Pricing / trial terms:** "**Your 7-day trial will cost only €1.00. Afterwards, it will be €29.99/month until you cancel.**"
- **Discount / anchor:** "Promo Code **MYHINT93** Applied — You save 93%". **Total due: ~~€14.99~~ → €1.00** (crossed-out anchor + "You save 93%" in green).
- **Payment stack (under price, wallet-first):** **PayPal → Buy with  Apple Pay → Google Pay → Credit or debit card.** Wallet/express options sit directly beneath the price and above card entry — exactly the recommended ordering.
- **Below the fold:** "How does Hint work?" (3-step: send palm scan → we analyze → reading generated), ongoing-support promise ("Talk with a palm reading specialist anytime"), a palmistry mini-education list ("Love line shows your attitude to love…", "A long thumb indicates good fortune", "Head line reflects your intelligence", etc.), and a 3-testimonial block (Rebecca Bauman "It's changed my life!", Mika Ryan "I've finally found a true love", Amanda Holmes "I've found a job I really enjoy"). Footer: Customer Support / How to Cancel, legal links, US company address (Hint America Inc, Claymont DE).
- **Future-state visualization:** the annotated palm + locked callouts function as the personalized "your results are ready behind this paywall" hook.
- **Checkout-close downsell:** Could **not** be triggered — payment is **inline (non-modal)** on the paywall (no checkout modal to close), and a browser back-navigation just returned to the promo-code screen with no exit-intent offer. So no second-offer/downsell modal was observed this session.

## Standout Techniques
- **Expectation-setting pill row on screen 1** ("1-min Quiz · Palm scan · Personalized guide") tells users exactly what the experience involves — reduces mid-funnel surprise at the palm-scan ask.
- **Social proof at position 2** (before any real questions) — resolves threat/ally/hierarchy up front with 25M users, a testimonial, live counts, and press logos.
- **"Why we ask" justification on every data question** (gender "blend of masculine and feminine"; birth date "reveals your core personality"; place not used here but pattern is consistent) — lowers friction on personal asks.
- **Adaptive personalized feedback** ("44% of Cancer Sun people also decide with their heart") — dynamically merges computed Sun sign + the just-given answer; high "this app understands me" payoff.
- **Palm scan as the core value-multiplier**, primed two screens earlier ("Your palms hold a wealth of information…") and reinforced with a Correct/Wrong framing guide, then an AI-overlay analysis animation — a strong self-generated-value (Hitchcock) moment.
- **Result-preview teaser at the email gate** (Love locked / Health unlocked bars) — curiosity + loss aversion right before data capture.
- **Earned discount → pre-applied coupon:** a dedicated "you get an exclusive one-time promo code MYHINT93 (93% off)" screen, then the code shows **already applied** on the paywall with a crossed-out €14.99 anchor. Makes the €1.00 trial feel won, not generic.
- **Dual live countdown (top banner + sticky bottom bar)** keeps the €1.00 offer salient through the whole long-scroll paywall.
- **Wallet-first payment ordering** (PayPal/Apple Pay/Google Pay above card) minimizes friction at peak intent.
- **Locked-result padlocks on the palm callouts** visualize exactly what the purchase unlocks.

## Notable Copy & Microcopy
- "Find your happiness with highly-personalized predictions."
- "In Palmistry, everyone is a blend of masculine and feminine, so it helps to know yours."
- "Your palms hold a wealth of information about your fate and personality."
- "Based on our data, 44% of Cancer Sun people also make decisions using their heart."
- "No biometric data is collected. All recognition processes are performed on your device." (privacy defusal, repeated at the scan step)
- "We securely store your data and don't share it with third parties." (email gate)
- "Your Report offer: €1.00! Ends in 14:57" / "Your Personalized Offer Reserved" (urgency)
- "You get an exclusive one-time promo code for a 93% discount" → code **MYHINT93**.
- "Your 7-day trial will cost only €1.00. Afterwards, it will be €29.99/month until you cancel." (clear, compliant trial→renewal disclosure)
- Live-activity: "Luis just found out when he'll meet his soulmate" / "996 people joined today".

## Weaknesses / Risks
- **Palm-scan gate is still a drop-off / privacy risk** (camera or file upload required), though Hint mitigates better than Astroline: it offers a **file-upload fallback**, a clear Correct/Wrong framing guide, and on-device/no-biometric reassurance — and its detection is lenient enough to accept imperfect images (which is also a quality risk: it "found" a Life line on a crude synthetic hand, undercutting the "real expert reading" claim).
- **Steep €14.99→€1.00 (93% off) anchor** may read as gimmicky; the "Report offer" anchor price (€14.99) is modest, so the 93% framing leans on a small absolute number.
- **Renewal cliff:** €1.00 trial → **€29.99/month** is a large jump; disclosed in body text but easy to under-weight next to the big "€1.00" and timer. Refund/cancel friction is a likely complaint vector.
- **Single plan, no tier ladder** — no annual/quarterly option to anchor against or to lift LTV; leaves money on the table vs. a multi-tier paywall.
- **No checkout-close downsell observed** — because payment is inline rather than a modal, there's no natural exit-intent recovery layer on the paywall itself (a missed ARPU-recovery opportunity vs. modal-checkout funnels).
- **Repeated "Rebecca Bauman / It's changed my life!" testimonial** appears both at the early interstitial and again on the paywall — eagle-eyed users may notice the reuse.
- Minor copy typo on the paywall benefit list: "**Gain Receive** personalized guidance…".
