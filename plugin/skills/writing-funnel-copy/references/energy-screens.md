---
id: energy-screens
title: Energy Screen Catalog
summary: Thirteen energy-screen archetypes with their job, placement, copy and visual formulas, evidence needs, failure modes and three inspected reference screens each from the public Funnel Screens library.
intents:
  - research
  - plan
  - qa
---

# Energy Screen Catalog

Energy screens are the non-question screens that pay the visitor back between questions: they reassure, prove, explain or excite. Choose one archetype per energy screen in the Emotional Arc by its trigger (see [placement by trigger](funnel-rhythm-template.md#energy-placement-by-trigger)), record one reference screen, then write it with the archetype's formula.

## How to use

1. **Pick by trigger.** What did the visitor just answer, and what doubt does that raise? Choose the archetype whose job answers it.
2. **Open the reference.** `fgrove references step <funnel-id> <position>` prints the text, appearance and image URL; open the image before writing. Borrow composition and copy structure only.
3. **Reflect the answer first.** The first words echo the preceding answer or doubt ("Beginner? No worries…", "Great choices!").
4. **Let the evidence carry it.** The dominant visual is the proof: a number, rating block, chart, level bar, product UI or their own answers (the [Hitchcock principle](funnel-psychology-framework.md#the-hitchcock-principle-self-generated-value)).
5. **Use real material.** Every count, rating, study, expert and testimonial comes from the Pre-work energy inventory, or stays an open `[PROOF: …]` slot. If an archetype's evidence is missing, pick another archetype rather than inventing it.
6. **Keep the archetype's composition** in design so energy screens look different from questions and from each other.

## Overview

Library counts: 495 energy screens in 66 recorded funnels (September–October 2026). Position is the median screen number; "early" is the share of that archetype's screens in the first six.

| Archetype | Job: the visitor feels… | Screens | Median position | Early |
| --- | --- | --- | --- | --- |
| [Authority burst](#authority-burst) | "This is legit and popular. I'm in good hands." | 45 | 6 (12% through) | 53% |
| [Answer reassurance](#answer-reassurance) | "My weakness is normal, not a blocker." | 72 | 24 (43%) | 8% |
| [Choice payoff](#choice-payoff) | "My answer was heard and will be used." | 87 | 16 (44%) | 14% |
| [Mechanism reveal](#mechanism-reveal) | "I understand why this works (and others didn't)." | 31 | 12 (36%) | 16% |
| [Comparison chart](#comparison-chart) | "This beats the alternative or doing it alone." | 22 | 17 (57%) | 14% |
| [Insight reframe](#insight-reframe) | "I learned something that reframes my problem." | 46 | 24 (49%) | 0% |
| [Results proof](#results-proof) | "People like me got results." | 30 | 20 (54%) | 17% |
| [Expert backing](#expert-backing) | "Qualified people stand behind this." | 14 | 25 (62%) | 7% |
| [Profile mirror](#profile-mirror) | "They understand exactly where I am." | 27 | 30 (74%) | 0% |
| [Progress nudge](#progress-nudge) | "I'm almost there; quitting now would waste it." | 29 | 28 (69%) | 10% |
| [Outcome projection](#outcome-projection) | "My goal is reachable by a concrete date." | 31 | 33 (81%) | 0% |
| [Product preview](#product-preview) | "I can see what I'll get, and I want it." | 42 | 19 (69%) | 12% |
| [Journey framing](#journey-framing) | "I know what's next and why it's worth answering." | 19 | 10 (25%) | 37% |

Typical progression: trust (authority, framing, reassurance) → understanding (mechanism, insight, comparison, choice payoff) → personal proof (mirror, projection, preview, results). The most common openings are `Q AUTH Q FRAME Q MECH` (Headway, 12min) and `Q AUTH Q REASS Q AFFIRM` (BetterMe); the typical close is progress nudge → profile mirror → event or confidence question → outcome projection → loading → email.

## Authority burst

- **Place it:** right after the first tap (screen 2–3). It is the first energy screen in 43% of recorded funnels. Optionally repeat once just before email or paywall as a final trust push.
- **Copy:** headline = reassurance + scale ("You're in good hands!", "{N} people trust {product}"); one line tied to their segment; a proof row of rating · award · years · press.
  - "You're in good hands! Simply Piano has helped millions start their musical journey" (`simply-piano`)
  - "10 million people trust Dancebit with their fitness goals" (`dancebit-d6d0da508c`)
- **Visual:** a large number or claim centred, then a laurel rating tile, a press-logo grid with a quote card, or an avatar/map crowd. Sparse, one CTA.
- **Needs:** a real user or download count with its definition, store rating with source and date, award names with years, press that actually ran. Segment-specific counts must really vary by segment. Without these, use [Expert backing](#expert-backing) or [Mechanism reveal](#mechanism-reveal) at screen 2.
- **Fails when:** unattributed "#1", counts reused across products, numbers that drift within one funnel.

| Reference | Composition |
| --- | --- |
| `fgrove references step simply-piano 2` | Headline and subline, a lighter feature card ("The #1 piano learning app"), two metric columns (years teaching, star rating), wide CTA. |
| `fgrove references step headway-live 2` | Bordered panel with a big download number, a quote card and a 2×3 press-logo grid; CTA pinned at the bottom. |
| `fgrove references step betterme-bd3b48ded3 55` | Late variant: "What makes BetterMe a trusted choice" over three rows of award logo, title, issuer and year. |

## Answer reassurance

- **Place it:** right after an answer that admits weakness: beginner, no experience, pain, older age, failed before, anxiety, no time. The most common reply to a vulnerable answer.
- **Copy:** headline normalises the answer ("No worries…", "You're not alone", "X isn't weakness"); body gives one reason it isn't a blocker and how the plan adapts; optionally a sourced peer stat.
  - "No worries, you're in the right place!" (`simply-piano`)
  - "Cravings under stress aren't weakness. They are biology." (`unimeal-5a03b45d59`)
- **Visual:** a warm illustration or soft lifestyle photo above a short headline and 2–3 lines; few numbers; optional fact card.
- **Needs:** a source for any "N% of people" stat; an accurate caveat for pain or health conditions.
- **Fails when:** it dismisses a real concern, promises a cure, or says the same thing whatever the answer was.

| Reference | Composition |
| --- | --- |
| `fgrove references step simply-piano 6` | After "Have you played before?": two-line headline, body, piano-key illustration, lightbulb fact card with a peer figure, CTA. |
| `fgrove references step spilio-smalltalk-live 8` | Charcoal page, bold headline ("None of this is about who you are"), large metaphor illustration, one body line, pill CTA. |
| `fgrove references step unimeal-5a03b45d59 15` | Wide moody photo, large two-sentence headline turning shame into biology, one paragraph, CTA. |

## Choice payoff

- **Place it:** after a goal, preference, trait or time-budget answer; the most frequent archetype (18% of energy screens). Avoid two in a row without new information.
- **Copy:** headline praises or echoes the choice ("Great choices!", "Ten minutes a day!"); body says what the product does with that answer, ideally with a concrete inventory number.
  - "Great choices! Our 5000+ song catalog is at your disposal" (`simply-piano`)
  - "Yay for the extrovert team!" (`headway-live`)
- **Visual:** a content collage or before/after that pays off the answer (catalogue, posture), or a mascot/emoji reaction above a short headline.
- **Needs:** inventory numbers matching the live catalogue; promised features that are really in their plan.
- **Fails when:** praise ignores which option was chosen, or the payoff promises features the plan lacks.

| Reference | Composition |
| --- | --- |
| `fgrove references step simply-piano 16` | After a genre multi-select: three-line headline with the catalogue size, "New songs are added weekly", dense album collage with NEW tags, CTA. |
| `fgrove references step headway-live 21` | Section label, celebratory mascot with sparkles, left-aligned headline and three-line body, full-width CTA. |
| `fgrove references step neatsy-596914aef0 9` | After a pain question: before/after posture figures joined by an arrow, centred headline, body with the workout library size, CTA. |

## Mechanism reveal

- **Place it:** early to mid, after a goal or "do you know why…" question; often right after the authority burst.
- **Copy:** headline names the method or root cause ("Unlock new possibilities with the {Method}"); body = cause → how the method addresses it → "the good news: it's fixable"; or 3 benefit rows.
  - "Unlock new possibilities with the Simply Method" (`simply-piano`)
  - "Understand big ideas in minutes instead of hours!" (`headway-live`)
- **Visual:** one simple diagram (cycle, arrows, clock split, iceberg) or an annotated product photo; keep text short.
- **Needs:** accurate plain-language explanation; citations for physiological or scientific claims.
- **Fails when:** text walls, pseudo-science, or the same mechanism repeated across screens.

| Reference | Composition |
| --- | --- |
| `fgrove references step leaply-0b5c2f1884 28` | "Quick science moment": anatomical illustration band, coloured headline, short paragraph with highlighted terms, ends on "It's fixable". |
| `fgrove references step headway-live 6` | After the goals multi-select: clock diagram with two labels (learn / practise), bold headline, three-line body. |
| `fgrove references step simply-piano 10` | Method headline, explanatory line, three benefit rows with icons, trust line with laurels under the CTA. |

## Comparison chart

- **Place it:** after the visitor reveals prior attempts or their current approach (diets, pills, other apps, on their own), or as the first proof in method-led funnels.
- **Copy:** headline = us vs them ("{Method} is better than {alternative}") or "Most people {fail} because {reason}. That doesn't have to be you!"; one sentence on the gap plus a source line or "illustrative" label.
  - "On Jumpspeak, you learn Spanish by speaking it on day one" (`jumpspeak-353f9d6050`)
  - "We'll help you stay motivated — your way!" (`simply-piano`)
- **Visual:** two curves (brand rising or steady, alternative flat or yo-yo) or a two-column ✓/✕ table; brand colour on "us", grey on "them".
- **Needs:** data behind the curves or a clear "illustrative" label; a named study for numeric comparisons; a fair alternative.
- **Fails when:** unlabelled axes, data-free curves presented as findings, logo-only "sources", strawman alternatives.

| Reference | Composition |
| --- | --- |
| `fgrove references step jumpspeak-353f9d6050 3` | Split card: "Traditional apps" with red ✕ vs the product with green ✓; centred headline and subline. |
| `fgrove references step simple-8944e5974e 7` | Headline with highlighted words, two-curve area chart (restrictive diet vs method), one bold line. |
| `fgrove references step simply-piano 14` | Motivation curve "With Simply Piano" vs wavy "Other methods", survey figure in an accent colour, CTA. |

## Insight reframe

- **Place it:** mid-funnel, after a lifestyle or problem answer that a fact can reframe (sleep, water, procrastination, gave up before). Never in the first six screens of recorded funnels.
- **Copy:** headline = surprising fact or reframe ("Procrastination isn't laziness.", "The myth of 1,200 calories"); 2–3 sentences of explanation, a source line, and a link back to the plan.
  - "Procrastination isn't laziness." (`addmile-6d81adcc79`)
  - "90% of people describe their voice wrongly" (`vocal-image-2ef0b5846e`)
- **Visual:** one explanatory visual: cycle diagram, "what people see / don't see" split portrait, photo with a source line, or a big percentage.
- **Needs:** a real, specific source for every number.
- **Fails when:** unsourced percentages, big health claims behind a generic source badge, facts unrelated to the previous answer.

| Reference | Composition |
| --- | --- |
| `fgrove references step addmile-6d81adcc79 9` | Coloured headline, subline, circular photo ringed by four labelled stage cards with dashed arrows. |
| `fgrove references step hapday-c423da663c 28` | "What people see / don't see": colour vs greyscale twin portrait with two bullet columns. |
| `fgrove references step reverse-health-611fd3fb68 12` | After the sleep question: serif headline, rounded photo, two short paragraphs, "Source: …" line. |

## Results proof

- **Place it:** after the visitor names their outcome or pain; match the story to that answer. Spread across the funnel, with a cluster around loading and email.
- **Copy:** headline = the outcome in their words or a cohort stat ("8 out of 10 … improved …"); body = named person, age/location, before → change → timeframe, stars.
  - "Feel like yourself again — inside and out" (`simple-8944e5974e`)
  - "8 out of 10 men improved … by following the Kegel Plan" (`dr-kegel-7775f87029`)
- **Visual:** portrait or before/after photo above a quote card with stars, or a 10-figure pictogram with one review.
- **Needs:** consented real testimonials with a typical-results note; survey base, size and date for outcome stats.
- **Fails when:** review counts reused across products, stock-looking portraits, results without timeframe or base.

| Reference | Composition |
| --- | --- |
| `fgrove references step happyo-3a58b11411 20` | Large rounded portrait, verified badge, name/age/city, stars, three paragraphs with bolded phrases. |
| `fgrove references step simple-8944e5974e 15` | Outcome headline, name line with result and stars, short quote, side-by-side before/after photo. |
| `fgrove references step dr-kegel-7775f87029 19` | "User survey" pill, headline with a coloured number, 10-figure pictogram, dark review card. |

## Expert backing

- **Place it:** when the visitor must trust the plan's content (health, therapy, skills), after a referral-source question, or between email and paywall as a final trust push. Also a fallback for screen 2 when scale proof is missing.
- **Copy:** headline = "Designed by {experts}", "We work with certified {experts}" or a founder story; each person named with a specific credential.
  - "We work with top-tier certified experts" (`betterme-bd3b48ded3`)
  - "We'll guide you every step of the way" (`simply-piano`)
- **Visual:** headshot list (photo, name, credential), a single founder portrait with achievements, or an institution feature card.
- **Needs:** real, identifiable people with verifiable credentials and their actual role; institutions only when the product really draws on them.
- **Fails when:** placeholder names, "illustrative expert" profiles, logos implying endorsement.

| Reference | Composition |
| --- | --- |
| `fgrove references step betterme-bd3b48ded3 38` | Centred headline, three rows of square headshot, name and credential badge. |
| `fgrove references step memory-os-7d312b5a23 25` | Dark page, circular founder portrait, headline, divider, four trophy-icon achievement lines. |
| `fgrove references step simply-piano 24` | Post-email: large feature card ("Designed by Music Teachers") with illustration, two icon columns (support, institution). |

## Profile mirror

- **Place it:** after 6–10 answers or a measurement block; "here's where you are" before "here's where you'll be". Never in the first six screens of recorded funnels; often followed by an outcome projection within four screens. Strip code `M`.
- **Copy:** headline = "Every {learner} starts somewhere different" / "Here's your {X} profile"; a scale with a "You are HERE" marker, 3–4 attributes from their answers, one sentence linking it to the plan.
  - "Every learner starts somewhere different" (`simply-piano`)
  - "Based on your answers this is your anger level indicator" (`parenting-leader-c8a0b4d83a`)
- **Visual:** horizontal gradient scale or semicircle gauge with a labelled marker, then an attribute grid with icons.
- **Needs:** values genuinely derived from answers; correct formulas (BMI); sourced risk statements.
- **Fails when:** verdicts that never vary, unsourced scary risk boxes, attributes contradicting answers.

| Reference | Composition |
| --- | --- |
| `fgrove references step simply-piano 9` | Headline, gradient level bar Beginner → Skilled with "You are HERE", one line, dark 2×2 attribute panel. |
| `fgrove references step betterme-bd3b48ded3 48` | BMI scale with "You – 27.68" tooltip, beige risk callout, icon attributes left and full-body photo right. |
| `fgrove references step parenting-leader-c8a0b4d83a 31` | Two-line headline, five-segment gauge with needle, range chips, explanation box. |

## Progress nudge

- **Place it:** at section breaks, after an effortful block, before the last stretch. Only when it is true: the percentage must match the real progress bar and remaining screens.
- **Copy:** headline = a percentage or proximity ("Your plan is 94% ready!", "Almost done!") or effort praise ("That took some honesty"); body = "just a few more questions so we can …".
  - "Your personal growth plan is now 94% ready!" (`headway-live`)
  - "You're 72% of the way to your plan" (`spilio-smalltalk-live`)
- **Visual:** mascot or celebration illustration, big percentage in the brand colour, minimal text.
- **Needs:** honest progress; drop "90% of people never start"-style claims without a basis.
- **Fails when:** "almost there" far from the end, percentages that go backwards.

| Reference | Composition |
| --- | --- |
| `fgrove references step headway-live 32` | Mascot stepping into a portal, headline with a highlighted "94%", two-line body. |
| `fgrove references step asana-rebel-e580df44eb 7` | Party-popper emoji on a soft glow, large centred headline, grey body. |
| `fgrove references step spilio-smalltalk-live 19` | Progress line plus thanks for reflecting, thumbs-up illustration on a pale panel. |

## Outcome projection

- **Place it:** late, after the goal metric and the mirror, or after an event-date question; the most back-loaded archetype. The final plan reveal uses the same formula (see [closing sequence](funnel-rhythm-template.md#plan-reveal)).
- **Copy:** headline = "We predict you'll {goal} by {date}" / "Meet your future self"; a basis line ("Based on your answers…") and an illustrative or safe-rate note.
  - "We predict you'll speak clearly and confidently by December" (`vocal-image-2ef0b5846e`)
  - "We estimate you could be {goal} by {date}*" (`betterme-bd3b48ded3`)
- **Visual:** a curve from Now/Today to a goal tooltip with the date, or a Now vs Goal panel with stat rows.
- **Needs:** the basis of the projection or an "illustrative" label; safe-rate caveats for body and health goals; images that are not presented as the visitor.
- **Fails when:** precise dates on a chart labelled illustrative without a basis, stock bodies as "your future self".

| Reference | Composition |
| --- | --- |
| `fgrove references step betterme-bd3b48ded3 52` | Headline + estimate with asterisk, gradient descending curve with goal tooltip, small-print basis, quote card. |
| `fgrove references step vocal-image-2ef0b5846e 32` | "We predict you'll" headline, rising curve with a confidence band, Today → 3 months axis, basis sentence. |
| `fgrove references step simple-bac01cbcb2 93` | Future-self panel with Now/Goal tabs, two body images, stat bars, one-line promise. |

## Product preview

- **Place it:** after a preference or content question (show the content they chose), or as the bridge from quiz to plan. Keep runs to two screens.
- **Copy:** headline = "Here's what's waiting for you" / "{Thousands of X} are waiting!"; 3–5 check bullets with concrete counts.
  - "Here's what's waiting for you" (`simply-piano`)
  - "Grow smarter, not harder — with a personalized plan built 100% for you" (`growfood-barry-wilson`)
- **Visual:** phone mockup of the real app (plan, today list, progress) or a content collage, then check bullets.
- **Needs:** mockups of the real product; counts matching the live catalogue; deliverables described accurately.
- **Fails when:** long feature tours stall momentum; sample data implies results.

| Reference | Composition |
| --- | --- |
| `fgrove references step unimeal-5a03b45d59 25` | After "what matters in your meal plan?": tinted panel with an overlapping food-photo collage, headline, short paragraph. |
| `fgrove references step growfood-barry-wilson 17` | Dark page, headline with highlighted "100% for you", phone mockup with a floating Week 1 checklist. |
| `fgrove references step simply-piano 20` | Headline, horizontal app mockup, four benefit rows with check marks. |

## Journey framing

- **Place it:** after the authority burst (welcome plus personalisation promise) or at a section start ("Now let's …"). Early: 37% are in the first six screens.
- **Copy:** headline = welcome or "Now let's …"; body = why the next questions matter and what they unlock; CTA can name the next section.
  - "Glad you're here!" (`memory-os-7d312b5a23`)
  - "Now, let's estimate when you'll reach your goal" (`simple-8944e5974e`)
- **Visual:** mascot or hero photo with a short headline, or a minimal card with a "NEXT: …" pill.
- **Needs:** honest effort cues; quiz-length promises ("1-minute quiz") that match reality.
- **Fails when:** it only delays without saying what's next; "3-minute quiz" on a 60-screen funnel.

| Reference | Composition |
| --- | --- |
| `fgrove references step memory-os-7d312b5a23 5` | Dark gradient, mascot on a rocket, left headline "Glad you're here!", three-line body, CTA under the copy. |
| `fgrove references step golffit-assessment 7` | Near-black page, pulse icon, "NEXT: MOVEMENT SCREEN" pill, centred headline, CTA naming the next task. |
| `fgrove references step simple-8944e5974e 20` | Lifestyle photo on top, white rounded sheet with headline and two-line body. |

## Provenance and limits

Classified from the recorded text, appearance descriptions and preceding screen of 76 journeys (2,662 screens) in the public Funnel Screens library; the 39 references above were opened and inspected as images. Each recording is one path, so answer branching is not observed. Every number, rating, award, study, expert and testimonial quoted here is as displayed in the recordings and **unverified**; references model composition and copy structure, never evidence for another product. Loading screens and inline answer feedback on question screens also carry energy content (comparison, authority, reviews) but are not counted here.
