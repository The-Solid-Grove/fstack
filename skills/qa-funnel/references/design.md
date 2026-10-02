# Funnel design QA

Apply these checks to every in-scope screen. Product and accessibility requirements are defects when broken; preferences about screen count, word count, colors, illustrations, and persuasion are test hypotheses.

## Evidence scope

Read the screen ID/revision, exact copy, selected reference, `Design.md`, artifact
or URL, and prior findings. Open the actual artifact before judging it.

- **Image:** check copy fidelity, option count and selection cues, hierarchy,
  reference composition, target brand/style, consistency with the other mockups,
  legibility, complete offer disclosures, clipping and visible defects. Inspect
  the full composition for long screens. A reference supplies design inspiration,
  not permission to reuse its claims or brand assets.
- **Rendered:** apply the image checks to the actual screen, then verify the
  layouts and states below. Reach the screen through its real flow and inspect
  incoming/outgoing navigation, selected/error/loading states and relevant long
  content. Whole-journey business-flow and release QA use the parent skill.

An image-direction pass leaves responsive behavior, semantic accessibility,
keyboard operation, font loading, CSS-pixel target sizes and functional checks
unverified. Mark required runtime checks **blocked — requires rendered UI**;
mark checks outside the requested scope **not applicable** with a reason.
Image evidence alone cannot establish a completed rendered design.

## Layout and accessibility

For rendered screens, inspect `375x667`, `393x852`, `402x874`, and `1280x800` CSS-pixel viewports. Also check reflow at 320 CSS pixels and enlarged text; the four baseline layouts alone are not an accessibility audit.

- Headline, visual, and primary action communicate one clear job. The main action is easy to find. Longer paywalls and enlarged text may scroll; content remains reachable.
- No horizontal overflow, overlap, clipped copy, broken images, or sticky bars covering content, focused controls, disclosures, or the last option. Bottom action bars have an opaque background and safe-area spacing.
- Check actual long answers, multi-line choices, validation errors, loading states, and the mobile keyboard. Focus remains visible and reading/tab order is coherent; dialogs manage focus and close predictably.
- Measure text contrast: 4.5:1 for normal text, 3:1 for large text, subject to WCAG exceptions. Required component boundaries and states need 3:1 non-text contrast. Selection/error cues have more than color alone.
- Prefer 44×44 CSS-pixel touch targets for comfort; WCAG 2.2 AA uses 24×24 or its stated spacing/equivalence exceptions. A 43px button is not automatically an AA failure.
- Body and input text around 16px is a practical mobile default, not a WCAG minimum. Verify labels, zoom, screen-reader names, meaningful image alternatives, and reduced-motion behavior where applicable.

## Content and imagery

- The first screen continues the actual ad promise. Each question has a product purpose, and later summaries reflect the user's answers accurately.
- Short, scannable headlines and concise supporting text form a clear hierarchy. Six-word headlines are a useful editing target, not a release blocker.
- A visual explains the benefit, mechanism, or choice. Decorative faces and animation should not obscure the offer. Test relevant portraits rather than imposing a ban.
- Alternate effort with useful feedback. Neither a fixed question cadence nor a prescribed funnel length guarantees conversion.
- Loaders describe work actually performed; progress and wait time are honest. Avoid fabricated searches, diagnoses, scores, and simulated certainty.
- Results, ranges, testimonials, ratings, logos, and before/after imagery need substantiation and permission where applicable. A range can still mislead.
- Email collection states its real purpose. Separate marketing permission where required. All prices, renewal terms, savings, timers, and guarantees agree with the real offer.

## Evidence

Record results in the task's `design-qa.md` or existing QA report: screen ID,
pattern/variant, revision, image/rendered scope, artifact/URL, copy/reference and
`Design.md` sources, viewport/state, check status, evidence and expected versus
actual result. Use **pass**, **fail**, **blocked** or **not applicable**, with reasons.
For defects, include severity and reproduction details. Capture screenshots for
the relevant viewport and state, with the defect annotated or described. Record
measured contrast and keyboard/zoom results separately from visual impressions.
Browser screenshots alone cannot establish a complete accessibility conformance claim.

Reopen corrected images/screens and update the evidence for that revision.
Shared token/component changes invalidate affected screen results. A screen's
required checks must pass or have a specifically accepted exception before it
is marked final; unavailable inspection capability remains blocked. Report
image-direction and rendered-design completion separately from function and
release readiness.

Sources: [WCAG text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), [target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).
