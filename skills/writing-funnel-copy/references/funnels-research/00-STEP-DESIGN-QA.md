# Step Design & Content QA (per-screen)

Run this against **every individual step** of a funnel — during copy drafting, after
build, and on the preview URL. It complements `00-QA-CHECKLIST.md`:

- `00-QA-CHECKLIST.md` = **funnel-level** QA (conversion completeness + functional defects).
- This file = **step-level** QA (design, copy, imagery, color, typography of one screen).

It follows the Mental Fuel model from `../funnel-psychology-framework.md`: every step
either adds fuel (motivation, validation, insight) or burns it (effort, confusion,
selling). Every check below traces back to that.

**Evidence legend** — each rule is tagged so we don't enforce folklore as law:

| Tag | Meaning |
| --- | --- |
| `[V]` | Verified by adversarial fact-check against a primary/quantitative source |
| `[P]` | Practitioner pattern (teardowns, CRO case studies) — strong default, not proof |
| `[S]` | Platform/accessibility standard (WCAG, Apple HIG) — non-negotiable |
| `[F]` | fstack framework rule (funnel-psychology-framework.md) |
| `[✗]` | Refuted or confounded — do NOT enforce as a rule (see §8) |

Mark each check ✅ pass / ⚠️ weak / ❌ fail.

---

## 0. Anatomy of a well-designed step

The reference layout for a quiz/content step, top to bottom, on a mobile viewport
(~390×844). Deviate deliberately, not accidentally.

```
┌─────────────────────────────┐
│ ← thin progress bar (honest)│  small, quiet, never the loudest element
│                             │
│  HEADLINE ≤6 WORDS          │  largest text on screen, one idea
│                             │
│  ┌───────────────────────┐  │
│  │   VISUAL (~30-50% of  │  │  carries THE value message of this step;
│  │   viewport height)    │  │  animated if anything is animated
│  └───────────────────────┘  │
│                             │
│  Body: max 1-2 short        │  ≥16px; a stat or icon row beats a
│  sentences.                 │  paragraph every time
│                             │
│  [ option ]  [ option ]     │  ≤5 one-tap options, short labels
│  [ option ]                 │  — OR —
│                             │
│ ┌─────────────────────────┐ │
│ │      CONTINUE CTA       │ │  highest-contrast element on the step,
│ └─────────────────────────┘ │  full-width, ≥44px tall, reachable thumb zone
└─────────────────────────────┘
```

The 3-second test governs everything: a user glances for 3 seconds and swipes —
what stuck? If the answer is "nothing" or "a nice picture," the step fails. `[F]`

One more invariant: headline + visual + interaction (options or CTA) must all be
visible without scrolling on a standard mobile viewport. If the step needs a scroll
to find the button, the visual is too big or the copy is too long. (Paywall is the
one exception: it scrolls by design, but its hero + first CTA must fit above the fold.)

---

## 1. Fuel & content checks (every step)

- [ ] **One value.** The step loads exactly one specific value/idea into the user's
      head. Two ideas = split or cut. `[F]`
- [ ] **Fuel direction is known.** You can say whether this step is an *ask* (spends
      fuel) or a *give* (adds fuel). No 3 asks in a row without a give between. `[F]`
- [ ] **Expectation match.** The step delivers what the previous step's CTA or
      question implied. Broken promise chains are the fastest fuel drain. `[F]`
- [ ] **Hitchcock check.** The user concludes value themselves from evidence
      (numbers, comparisons, their own inputs reflected back); the copy never claims
      "this is amazing." `[F]`
- [ ] **Question copy earns its answer.** Every question visibly unlocks something
      on the next screen; never ask without showing why the answer mattered. `[F]`
- [ ] **Sensitive questions get affirmation microcopy** after answering ("Thanks for
      sharing — that's a hard first step"), and sensitive/personal questions sit late
      in the flow, never in the first screens. `[P — Noom teardown, verified easy-first
      ordering [V]]`
- [ ] **Ranges, not promises.** Results shown as ranges; the user anchors high on
      their own. No exact guaranteed outcomes, ever, in regulated verticals. `[F]`

## 2. Copy checks

- [ ] **Headline ≤6 words**, scannable in 1 second, states the step's one value. If
      it needs more words, the idea isn't clear yet. `[F]`
- [ ] **Body ≤2 short sentences** — and for tap-through quiz steps, aim for **one
      sentence per screen**; users absorb it at a glance or not at all. `[F]` `[P]`
- [ ] **Numbers beat prose.** If it can be said with a number, an icon+stat, or a
      comparison, it is not said with a sentence. `[F]`
- [ ] **Tone = confident expert**, "we found this for you," never "buy now" energy.
      No bold text inside good-to-know/priming callouts. `[F]`
- [ ] **Problem steps use PAS** (Problem → Agitate → Solve) as the default structure;
      agitation is relieved before the step ends (poke → soothe → empower). `[P]` `[F]`
- [ ] **Testimonials follow Before → After → Experience**, never generic praise, and
      pair one emotional quote with one statistic. `[P]`
- [ ] **Customer vocabulary.** Copy uses the audience's own words (from reviews,
      research, PRODUCT_SENSE.md), not marketing-speak. VoC rewrites are among the
      biggest documented copy lifts. `[P — Copyhackers +400% CTR case]`

### CTA copy

- [ ] **First-person phrasing**: "Start **my** plan," "Get **my** results" — not
      "your". `[P — Unbounce +90% case; widely replicated]`
- [ ] **Starts with a command verb**, ideally a receive-verb ("Get", "See", "Unlock")
      over a work-verb ("Submit", "Register"). Generic "Submit" is a documented
      loser. `[P]`
- [ ] **2-4 words** on the button; specific beats generic ("Get my free quote" >
      "Order information", +38% in the classic test). `[P]`
- [ ] **Objection microcopy under the paywall/email CTA**: "free", "no credit card",
      "takes 2 minutes", "cancel anytime" — preempt cost, time, commitment. `[P]`
- [ ] **Exactly one primary CTA per step.** No competing actions, no exit links.
      `[P — single-CTA pages 13.5% vs 11.9%]`
- [ ] **"Free" is load-bearing.** If the offer has a free component, the word "free"
      appears on or beside the button; removing free-framing measurably kills
      click-through. `[V — Microsoft test: −64% clicks]`

## 3. Image & visual checks

- [ ] **The step has a visual, and the visual carries the value.** Default is an
      image/illustration/animation on every content step; a step may go text-only
      only when the headline+options ARE the content (plain question steps with
      icon/emoji options count as having visuals). Decoration-only images fail. `[F]`
- [ ] **Biggest element = value carrier.** The largest visual element communicates
      the step's message; if the biggest thing on screen is decorative, redesign. `[F]`
- [ ] **Motion budget.** If anything animates, it's the value-carrying element;
      decoration stays static. `[F]`
- [ ] **Faces are used deliberately, not by default.** A face captures 35-45% of
      attention but communicates 0% value unless the face IS the message. Use real
      human photos on testimonial/social-proof steps — photo testimonials are
      measurably more memorable than text-only (p=0.0035) `[V]` — and keep faces OFF
      steps where they'd steal attention from the value visual. `[F]` Human-photo
      lifts elsewhere are real but not universal: test, don't assume. `[P]`
- [ ] **Real photos, never obvious stock.** Users detect stock photography and it
      reads as low-trust. `[P]`
- [ ] **Gaze direction:** if a face appears near a CTA, it looks toward the CTA or
      the value element, not at the camera edge. `[P — directional-cue heuristic]`
- [ ] **Logos: recognizable or none.** High-profile logos are recalled and build
      trust (p=0.009) `[V]`; unknown-brand logos and raw follower counts are not
      recalled and waste space `[V]`.
- [ ] **Before/after imagery is a hypothesis, not a rule.** The claim that it
      reliably lifts paywall conversion failed verification `[✗]` — allowed where
      compliant and honest, but never required, and always A/B tested.
- [ ] **Loader/processing steps prime, never blank-wait**: rotating status messages
      seed value concepts, optionally a micro-question or proof line. A fake
      "building your plan" loader before the paywall is a verified lift (~10-11%)
      — but it must look like real work. `[V]` `[F]`

## 4. Color checks

- [ ] **No hue rules — contrast rules.** There is no best-converting button color;
      what converts is how strongly the CTA contrasts with its surroundings. Never
      "fix" a funnel by making buttons red/green/orange. `[V — CXL; confounded
      classic tests documented [✗]]`
- [ ] **Three simultaneous contrasts on the CTA** `[P — EyeQuant/NASA luminance
      guidance]`:
      1. luminance contrast between button and page background,
      2. contrast between button text and button fill,
      3. hue visibly distinct from surrounding elements.
- [ ] **The CTA is the single highest-contrast element on the step.** If the brand's
      dominant page color is X, the CTA is not X or X-adjacent (the real lesson of
      the famous red-vs-green test). `[V]`
- [ ] **Accent color is reserved.** The CTA/selection accent appears on the CTA and
      selected states only — not scattered on icons, borders, and decorations,
      which dilutes the hierarchy. `[P]`
- [ ] **Size never substitutes for contrast** — a bigger low-contrast button still
      loses to a smaller high-contrast one. `[P — EyeQuant Sephora/Uniqlo]`
- [ ] **Selected option state is unmistakable** (fill or border + check, not a subtle
      tint), and unselected options remain clearly tappable. `[P]`
- [ ] **Follow web conventions where they exist** (links look like links; Bing's
      link-blue finding shows convention itself converts). `[P]`
- [ ] **Accessibility floor:** text contrast ≥4.5:1 (normal text) / ≥3:1 (large text
      and UI components) per WCAG AA — including text placed over images (use an
      overlay/scrim when needed). `[S]`

## 5. Typography & sizing checks

- [ ] **One headline per step**, visually dominant: roughly 1.5-2× body size
      (≈24-32px vs 16-17px body on mobile). If the headline and body look similar,
      hierarchy failed. `[P]` `[F-derived]`
- [ ] **Body text ≥16px on mobile.** Also: any text `<input>` uses font-size ≥16px
      so iOS Safari doesn't zoom the viewport on focus. `[S]`
- [ ] **When the number is the value, the number is the biggest text on screen**
      (stat callouts, savings, projections) — set it display-size, not inline. `[F]`
- [ ] **Short lines, generous spacing:** body lines ~45-75 characters, no
      wall-of-text blocks; option labels ≤4-5 words each. `[S/P]`
- [ ] **≤2 typefaces**, consistent weights; bold reserved for the headline and key
      numbers — never bold inside priming callouts. `[F]`
- [ ] **Image-to-text balance:** visual ≈30-50% of viewport height; headline never
      smaller than option-label text; the whole step (headline + visual + CTA) fits
      the fold as per §0. `[P]` `[F-derived]`

## 6. Layout & interaction checks

- [ ] **Passes the 3-second test** (see §0). `[F]`
- [ ] **Touch targets ≥44×44px**, CTA full-width in the bottom thumb zone. `[S]`
- [ ] **≤5 answer options**, one question per step; ranges instead of exact numbers
      for demographics/budgets (splitting fields into one-per-screen is a verified
      abandonment reducer). `[P]` `[F]`
- [ ] **Progress indicator present and honest** — never jumps backward, never >100%,
      denominator not wildly inflated vs. real screen count (see funnel-level B5). `[P]` `[F]`
- [ ] **Step transition is instant** — no client-side redirects, no spinner between
      steps; hundreds of milliseconds of added latency measurably hurt. `[V — Kohavi]`
- [ ] **Nothing competes with the forward action**: no nav bar, no footer links, no
      secondary buttons (except a deliberate, quiet "skip"/back affordance). `[P]`

## 7. Step-type overlays

Apply on top of §§1-6 depending on what the step is:

| Step type | Extra checks |
| --- | --- |
| **Question (ask)** | Near-100%-agreement phrasing early in funnel; easiest/least invasive questions first `[V]`; answer feedback ties choice to the plan `[F]` |
| **Interstitial (give)** | Delivers a real insight/validation, not filler; ideally reflects a prior answer back (personalization is the point) `[P]` |
| **Social proof** | Photo + name + Before/After/Experience structure `[P]`; audience-matched numbers ("500,000 men in their 40s") `[P]`; appears early (~Q3) and again pre-paywall `[F]` |
| **Loader / processing** | Rotating status copy referencing the user's actual inputs; duration 3-6s; progress feels like computation `[V]` `[F]` |
| **Projection / results** | Range not promise `[F]`; anchored to the user's stated goal/date; reflects ≥1 real input (personalization-integrity — see funnel-level B1) |
| **Email capture** | Framed as functionally necessary, placed ~⅓+ into the funnel, consequence stated ("we'll send results here") `[P]` `[F]` |
| **Paywall** | Hero + first CTA above the fold; per-day reframe; this file's §§2-5 apply to every block; full paywall QA lives in funnel-level A5/C1 and `funnel-paywall-best-practices.md` |

## 8. Myths — do NOT enforce these

Rules that sound authoritative but failed verification. Flagging one of these as a
"fix" is itself a QA failure:

1. **"Use [red/green/orange] buttons — it converts best."** No hue wins; the famous
   case studies were confounded (missing or low-prominence control buttons). `[✗ V]`
2. **"Before/after photos on the paywall are a proven lift."** Refuted 0-3 in
   verification. Testable hypothesis only — and a compliance risk in health. `[✗]`
3. **"Human faces always increase conversion."** Strong lifts exist (Medalia +95%)
   but so do null results; faces also steal attention budget. Deliberate use + test. `[✗/P]`
4. **"Shorter funnels convert better."** Verified opposite for fitness/wellness:
   longer flows convert better; friction, not length, kills funnels (Noom: up to
   113 screens). `[V]`
5. **"A huge A/B win proved it."** Extreme deltas are usually artifacts (Twyman's
   law) — most ideas fail when properly tested; treat any single case study,
   including the ones cited here, as a default, not a law. `[V — Kohavi]`
6. **"Optimize step CTR."** Steps exist to convert the funnel, not themselves;
   a change can lower step clicks while raising purchases (price-display effect).
   Judge changes on the ultimate action. `[V — Kohavi]`

---

## Scoring

Per step: **Pass** = no ❌ and ≤2 ⚠️. Any ❌ in §1 (fuel/content) or §4 (CTA
contrast) blocks the step — those are the checks with the strongest evidence
behind them.

Per funnel: run this on every step, then run `00-QA-CHECKLIST.md` at funnel level.
The highest-ROI step-level failures to hunt first:

1. Headline over 6 words / two ideas per step (§2)
2. Decoration-only imagery or a face stealing the value message (§3)
3. CTA not the highest-contrast element (§4)
4. Ask-streaks with no give (§1)
5. Dishonest progress or laggy transitions (§6)

---

## Appendix: key verified findings (sources)

- Photo testimonials → higher recall, p=0.0035; recognizable logos p=0.009; follower
  counts n.s. — CXL Institute eye-tracking study: https://cxl.com/research-study/social-proof/
- No universally best CTA color; contrast over hue; confounded classic tests —
  CXL: https://cxl.com/blog/which-color-converts-the-best/
- Free-framing (−64% clicks when replaced by priced buy button), ultimate-action
  metric, most-ideas-fail, latency harm, Twyman's law — Kohavi et al., Online
  Controlled Experiments: https://kdd.org/exploration_files/v12-02-8-UR-Kohavi.pdf
- Longer onboarding converts better (fitness); loader screen +10-11%; easy-first
  question ordering — Noom funnel interview (Paddle, Fix That Funnel):
  https://www.paddle.com/studios/shows/fix-that-funnel/noom-full-interview
- Noom funnel: up to 113 screens, 10-15 min; email gate ~⅓ in — RevenueCat teardown:
  https://www.revenuecat.com/blog/growth/web-to-app-onboarding-funnel/
- Practitioner corpus (CTA copy, faces, VoC, micro-commitments, paywall test win
  rates): Copyhackers, CXL CTA guide, EyeQuant, VWO, Flint, Heyflow, RevenueCat
  paywall guide, Airbridge — see `00-LIVE-FINDINGS.md` and this folder's teardowns
  for the in-house evidence.
