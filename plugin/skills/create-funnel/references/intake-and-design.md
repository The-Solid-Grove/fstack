# Product intake and Design.md

Read after downloading the new funnel, before changing its identity or screens. Reuse the user's existing brief, answers, branding and references; bundle only missing essentials into one short round.

## Essential questions

1. **Product and promise:** What does the product do, for whom, and what result can it truthfully promise? Request the product/site/store link when available.
2. **Audience and arrival:** Who is entering, from which ad/channel, in which language and market? What promise has the ad already made?
3. **Journey and offer:** What should the visitor do: quiz, direct purchase, registration, download? What paid offer and post-purchase access already exist? Record known pricing, trial, renewal/cancellation terms and payment configuration; defer unknowns explicitly.
4. **Identity:** Which logo, colors, fonts, product screens and assets must be kept? When none exist, propose a direction suited to the product and audience, with a brief reason.
5. **Visual reference:** Which examples should guide layout and tone? What should be avoided? Inspect accessible references and keep brand requirements distinct from inspiration.
6. **Scope:** Is this a starter with a design brief, or a customized copy/design/flow with preview delivery? What content or decisions are already approved?

Use the answers to decide the work, not to create a long questionnaire. If the user defers a nonessential answer, record it and continue the authorized scope. Consequential unknowns such as offer terms remain unresolved until answered; suggested colors can be marked as provisional.

## Create Design.md

Write `Design.md` at the funnel root immediately during intake. Use the real product name and the user's working language. Keep it concrete enough to guide the next screen without asking again:

- **Brief:** product, audience, arrival promise, language/market, selected template, conversion goal and requested scope.
- **Sources and status:** links to inspected product/brand/reference assets; distinguish observed requirements, accepted decisions, proposals and open questions.
- **Direction:** a short rationale connecting visual choices to the product and audience. The template supplies structure; the product supplies identity.
- **Typography:** font families/sources/fallbacks, weights and heading/body/button sizes.
- **Semantic palette:** actual color values and roles for canvas, surface, primary action, text, muted text, border, success/error and selected states; contrast/legibility expectations.
- **Layout:** content widths, spacing scale, radii, screen gutters and responsive behavior, including short mobile screens and persistent CTA areas where used.
- **Controls:** buttons, inputs, choice cards, focus/selected/disabled/error states, progress and loading presentation.
- **Assets and motion:** photo/illustration/icon direction, actual asset locations and modest motion/reduced-motion behavior.
- **Content and offer constraints:** voice, supported proof, legal/offer facts and missing configuration; link fuller approved copy instead of duplicating it.
- **Open decisions:** unanswered essentials, proposed defaults and what each uncertainty blocks.

Preserve and extend an existing `Design.md`; retain its confirmed decisions and reconcile any conflict with the user. Keep theme implementation in the selected template's existing styling system. This file records product design intent; managed `docs/funnelsgrove/*` owns runtime contracts.

## Completion check

A downstream agent must be able to tell the target product from the starter and build a coherent next screen from `Design.md`. A renamed template heading, a generic checklist, or silently inherited starter branding does not meet this bar. For a starter-only request, proposed design defaults and clearly recorded unknowns are acceptable; describe that status in the handoff.
