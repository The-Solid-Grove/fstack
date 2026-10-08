---
id: funnel-rhythm-template
title: Funnel Rhythm Template
summary: The default quiz-to-paywall skeleton, question/energy cadence rules, energy placement by trigger and the closing sequence, derived from the public Funnel Screens library.
intents:
  - research
  - plan
  - qa
---

# Funnel Rhythm Template

A funnel is two kinds of screens: **questions** that spend the visitor's energy and **energy screens** that pay it back with reassurance, proof, insight or excitement. It closes with a **plan**, an **email** and a **paywall**. This template sets the default order and pacing; the [psychology framework](funnel-psychology-framework.md) explains why it works, the [energy screen catalog](energy-screens.md) supplies each energy screen's formula and references, and the [paywall blueprints](paywall-blueprints.md) supply the paywall.

## What the reference library shows

Source: the public Funnel Screens library read through `fgrove references` (76 recorded journeys; 69 with 12+ screens; captured September 2026). Screen roles come from the library's recorded screen classification and our reading of the text.

| Observation | Value |
| --- | --- |
| Screens before the paywall | median 34 (middle half 24–46) |
| First energy screen | median position 4; position 2–4 in 35 of 65 funnels that have one |
| Energy share before the paywall | median 21%, top decile 32%+; Simply Piano 50%, Vocal Image 37%, Memory OS 35% |
| Longest run of consecutive questions | median 6; Simply Piano 3 |
| Closing screens | loading in ~3/4 of funnels, email in ~4/5, an explicit plan reveal in ~3/5, paywall last |
| First energy screen's archetype | authority burst in 43% of funnels; insight, mirror and projection never appear in the first six screens |
| Typical close | progress nudge → profile mirror → event or confidence question → outcome projection → loading → email → plan → paywall |
| Opening screen | most combine the ad promise ("Chair Yoga Workout Plan", "1-minute quiz") with a one-tap age, gender or goal question on image cards and a consent line |

Most recorded funnels are question-heavy. **This template deliberately follows the energetic end of the library (the Simply Piano style):** short question runs and frequent energy screens. These are observations of recorded funnels, not measured conversion effects; test changes with [measurement practices](funnel-best-practices.md#measurement-and-experiments).

## The skeleton

Default budget: **20–30 screens before the paywall** for a plan-based subscription; 12–18 for a simple utility.

| Section | Position | Job | Screens |
| --- | --- | --- | --- |
| **A · Hook** | 1 | Confirm the ad promise and get the first tap. | Promise headline + "1-minute quiz" + one-tap identity/goal/motivation question on image cards + privacy/terms line. |
| **B · Trust burst** | 2–3 | Pass the trust gate right after the first tap. | [Authority burst](energy-screens.md#authority-burst) (or [Expert backing](energy-screens.md#expert-backing) when scale proof is missing), then an easy question. |
| **C · Discovery loops** | to ~60% | Learn about them and repay every 2–3 questions. | Repeating `Q Q E` / `Q Q Q E` loops; each energy screen answers the loop's last answer (see [placement by trigger](#energy-placement-by-trigger)). Effort climbs the [investment ladder](funnel-psychology-framework.md#investment-ladder). |
| **D · Mirror and mechanism** | ~60–85% | Prove the answers became something; explain how it works. | [Profile mirror](energy-screens.md#profile-mirror), [Mechanism reveal](energy-screens.md#mechanism-reveal), [Comparison chart](energy-screens.md#comparison-chart), a commitment question (time per day, readiness), [Product preview](energy-screens.md#product-preview). |
| **E · Build-up** | 2–4 screens | Create anticipation, then deliver the reveal. | [Loading](#loading) that names the answer groups + proof or micro-questions → [Plan reveal](#plan-reveal) with a projection from their answers. |
| **F · Capture** | 1–2 | Save the plan. | [Email](#email) framed as saving/sending the plan; optionally a short post-email reassurance (support, experts, guarantee). |
| **G · Paywall** | last | Convert accumulated conviction. | A [paywall blueprint](paywall-blueprints.md) cloned from one reference. |

**Shorter funnels (10–15):** A → B → two discovery loops → mirror → loading + plan → email → paywall. **Longer funnels (35+):** add loops, never longer question runs; place a second proof screen (results proof or expert backing) in the middle third, and repeat the authority burst once before email.

## Cadence rules

Defaults for every new arc. A deviation needs a one-line reason in the arc (for example, a regulated health product using fewer outcome screens and more mechanism).

1. **Screen 1 asks.** It confirms the promise and asks a one-tap question. A promise-only intro is allowed only when the ad needs context; then the question comes at screen 2.
2. **First energy screen by screen 3** (latest 4). Default: an authority burst at screen 2.
3. **Short question runs.** At most 3 consecutive questions in the first half and 4 in the second half; 2–3 is the default loop.
4. **Energy share 30–45%** of pre-paywall screens (never below 25%). Count energy screens, the mirror and the plan reveal; not loading or email.
5. **Answer-linked energy.** An energy screen after a question opens by reflecting that answer or the doubt it raises ("Beginner? No worries…", "Great choice!").
6. **Vary archetypes.** Two consecutive energy screens never share an archetype; at least 4 different archetypes in a 20+ screen funnel. Progress from trust (authority, reassurance) to understanding (insight, mechanism, comparison) to personal proof (mirror, projection, plan).
7. **Escalate effort.** One-tap questions first; multi-select after at least two single-choice questions; numeric and sensitive questions after the trust burst and followed by reassurance within two screens; name and email last.
8. **Close with suspense.** Mirror → loading → plan reveal → email → paywall, or loading → email gate → plan reveal → paywall. The plan reveal always comes before the paywall, and the paywall repeats it.
9. **Every question has a use.** It feeds an energy screen, the mirror, the plan or the paywall summary. Remove a question whose use cannot be named.
10. **Two Hitchcock moments minimum.** At least two screens where the visitor sees their own inputs turned into something (mirror, first result, projection, matched catalogue) before the paywall.

## Energy placement by trigger

| After this | Use | Why it works |
| --- | --- | --- |
| The first tap (hook) | [Authority burst](energy-screens.md#authority-burst) | Confirms they chose well; passes the trust gate. |
| Experience, level or age ("never played", "beginner", "50+") | [Answer reassurance](energy-screens.md#answer-reassurance) | Removes "is this for someone like me?". |
| Goal, motivation or preference choice | [Choice payoff](energy-screens.md#choice-payoff) | Shows what the product does with their choice. |
| Pain, struggle or "what stops you" | [Insight reframe](energy-screens.md#insight-reframe) or [Comparison chart](energy-screens.md#comparison-chart) | "It's not you, it's the method." |
| Time, habit or schedule | [Mechanism reveal](energy-screens.md#mechanism-reveal) | Makes success feel achievable ("10 minutes is enough"). |
| Doubt, past failure, scepticism | [Results proof](energy-screens.md#results-proof) or [Expert backing](energy-screens.md#expert-backing) | Answers the barrier with proof. |
| 6–10 answers collected | [Profile mirror](energy-screens.md#profile-mirror) | Personalisation becomes visible. |
| Topic, genre or content preference | [Product preview](energy-screens.md#product-preview) | Their taste matched to real content. |
| A section start, or right after the authority burst | [Journey framing](energy-screens.md#journey-framing) | Says what the next questions unlock. |
| A long or effortful block, near the end | [Progress nudge](energy-screens.md#progress-nudge) | "Almost there", only when it is true. |
| Goal metric, mirror or event date, late | [Outcome projection](energy-screens.md#outcome-projection) | The goal becomes reachable by a date. |
| Just before email or paywall | A second [Authority burst](energy-screens.md#authority-burst) or [Expert backing](energy-screens.md#expert-backing) | Final trust push. |

## Closing sequence

Observed orders before the paywall (69 funnels): **loading → email → plan** (12, e.g. `12-min-05197187bb`, `addmile-6d81adcc79`, `growfood-barry-wilson`), **plan/projection → loading → email** (12, e.g. `dancebit-d6d0da508c`, `harna-c2cc0f618f`), **loading → email** with the plan on the paywall (11), **loading → plan → email** (`headway-live`, `dr-kegel-7775f87029`), **plan → email** without a loader (`simply-piano`).

### Loading

- **Headline:** "Creating your {goal} plan…" / "Analysing your answers…".
- **Progress rows:** 3–5 rows named after answer groups the plan really uses (Goals · Level · Schedule · Preferences).
- **While it runs:** a rating/testimonial carousel under the bar, or 1–2 yes/no micro-questions ("Do you finish what you start?") that also feed the plan.
- **References:** `headway-live` #56–57 (micro-question inside the loader), `harna-c2cc0f618f` #38 (testimonial under progress), `leaply-0b5c2f1884` #35–36 (named analysis rows).

### Plan reveal

- **Headline:** "{Name}, your {goal} plan is ready!" or the outcome itself ("Read and play sheet music in 19 days").
- **Hero:** projection chart now → goal by a date/week count derived from their answers, plus 2–4 plan chips from answers (goal, level, minutes/day).
- **Honesty:** "Illustrative, based on your answers" footnote; ranges for health, money and body outcomes.
- **References:** `simply-piano` #19, `headway-live` #60, `leaply-0b5c2f1884` #39, `betterme-bd3b48ded3` #59, `growfood-barry-wilson` #23.

### Email

- **Headline:** "Where should we send your plan?" / "Enter your email to get your personal {plan}".
- **Body:** one line of purpose; privacy reassurance under the field; separate unticked marketing consent where required.
- **CTA:** "Get my plan" / "Continue". Optional trust badges (awards, store ratings) below.
- **References:** `dancebit-d6d0da508c` #33, `simply-piano` #23, `leaply-0b5c2f1884` #37, `growfood-barry-wilson` #22 (email gate before the plan).

## Worked strip: Simply Piano

`Q E Q Q Q E Q Q M E Q E Q E Q E Q E P E Q E @ E $` — 25 screens, energy share 50%, never more than 3 questions in a row, no loader.

| # | Screen | Content | Fuel |
| --- | --- | --- | --- |
| 1 | Q · hook, image cards | "What motivates you to play the piano?" + store awards | − |
| 2 | E · authority burst | "You're in good hands!" #1 piano app, 10+ years, 4.7★ | ++ |
| 3–5 | Q × 3 | Age · has a piano? · played before? | − − − |
| 6 | E · answer reassurance | "No worries, you're in the right place!" + learners who started at this level | ++ |
| 7–8 | Q × 2 | Learning style · practice frequency (with a pro tip) | − − |
| 9 | M · profile mirror | "You are HERE" level bar + their age, frequency, experience, style | ++ |
| 10 | E · mechanism reveal | "Unlock new possibilities with the Simply Method" + 3 benefit rows | + |
| 11 | Q · multi-select | Goals, up to 3 | −− |
| 12 | E · choice payoff | "Awesome choice! … you've already started" | + |
| 13 | Q | Best way to help you learn | − |
| 14 | E · comparison chart | Motivation curve: with Simply Piano vs other methods + learner survey figure | ++ |
| 15 | Q · multi-select | Music genres | −− |
| 16 | E · choice payoff / product preview | "Great choices! Our 5000+ song catalog…" album collage | + |
| 17 | Q · scale | "How familiar is this feeling?" | − |
| 18 | E · mechanism reveal | Real-time note-recognition feedback | + |
| 19 | P · plan reveal | "Read and play sheet music in 19 days" chart | ++ |
| 20 | E · product preview | "Here's what's waiting for you" app mockup + 4 benefits | + |
| 21 | Q · image cards | Choose your first song | − |
| 22 | E · choice payoff (Hitchcock) | "In 1 day you'll be able to play: Symphony No. 40" | ++ |
| 23 | @ · email | "Create your free account to save your preferences" | −− |
| 24 | E · expert backing | Designed by music teachers, 24/7 support, Trinity College recognition | + |
| 25 | $ · trial paywall | Timer, family/individual plans, trial toggle, card form | − |

Reference claims (ratings, user counts, survey figures) describe Simply Piano only; they are not evidence for another product.

## Reading a reference rhythm with the CLI

`fgrove references` reads the public library without login.

```bash
fgrove references categories                         # categories with funnel/screen counts
fgrove references list --category "Music"            # funnels in a category
fgrove references list --step-type social-proof      # funnels containing a screen kind
fgrove references steps <funnel-id>                  # ordered screen descriptions
fgrove references step <funnel-id> <position>        # one screen: text, buttons, appearance, image URL
fgrove references show <funnel-id> --json            # full journey for scripting
```

To build a reference strip, run the Fstack checkout's `scripts/reference-strip <funnel-id> [<funnel-id> …]`: it prints the strip, energy share, longest question run, first energy screen and one line per screen. Its mapping is a first pass from the recorded screen kinds; read the screens to separate a profile mirror (`M`) from a plan reveal (`P`) and to name each energy archetype. Then open the images of the screens you will borrow from. Record funnel ID and position for each borrowed screen in the arc's Reference column. If the CLI is unavailable, use the IDs and descriptions recorded in this template and the catalog, and say that the images were not inspected.
