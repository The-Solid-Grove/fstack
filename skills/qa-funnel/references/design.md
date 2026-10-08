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

## Reference comparison

When an inspected source is available, open the target and the matched source
screen at comparable readable size. Check that their narrative jobs and controls
are compatible before comparing composition. A question grid and a result chart
are not interchangeable because they share colors or a source funnel.

Compare headline/visual/action hierarchy, content density, choice grouping,
spacing and CTA placement. Record **borrowed composition**, **intentional target
brand/copy differences**, and **unintended drift or defects** separately. The
approved copy and `Design.md` remain authoritative: preserving target meaning,
option counts, offer disclosures and brand can require a deliberate departure.
Reference prices, claims, logos and testimonials are not evidence for the target.

For a paywall cloned from a reference, list both section orders side by side.
The target keeps the reference's section order, repeated CTAs and sticky
elements unless the approved copy records a deliberate change; every section
has target content or a visible open slot, and billing disclosures remain
readable before the CTA.

Save or link the source and target artifacts with screen IDs/revisions in the
QA record. If no compatible source is accessible, record that limitation and
inspect against the approved content/style; do not report a reference comparison
as passed. The [opening feedback checkpoint](../../design-funnel/SKILL.md#first-three-screen-feedback-checkpoint)
uses these comparisons when presenting the first actual designs to the user.

## Per-screen calibration loop

For every new or revised target screen in an authorized design/edit task, repeat **compare → Design QA → correct → recheck** before marking the revision ready for review or extending its pattern. An inspection-only QA request reports findings and returns corrections/document edits to the owning workflow unless those edits are already authorized:

1. Open the actual target, exact copy, `Design.md` and matched source. Compare hierarchy, density, controls and action placement; record borrowed structure, intentional differences and defects. If the source is unavailable, name the limitation and review against the target contract.
2. Review text and composition together. Identify what the visitor must understand and decide now; remove repetition, shorten wording and move optional explanation to an appropriate detail surface. Retain meaningful choices, evidence qualifications, fit limits and all required offer/billing disclosures. A source's word count is context, not a quota.
3. Correct the target and canonical copy together. Preserve approved strategy, answer semantics and transitions. Return consequential strategy/arc changes to their existing approval workflow; ordinary wording/layout corrections proceed within scope. Keep readable type and reachable content rather than shrinking essential text to fit.
4. Reopen the corrected artifact and rerun affected checks. A previous revision's pass never transfers automatically; shared style/copy changes invalidate affected screens. Record current screen ID/revision, comparison, findings, corrections, evidence and pass/fail/blocked status in `design-qa.md`.
5. Reconcile the output documents: current `COPY.md` or equivalent, `Design.md`, screen map, QA report and approval/status record must describe the same revision. Remove stale active instructions, obsolete duplicate copy and broken links. Keep superseded assets or history clearly labeled and outside the current handoff; preserve unrelated work.

Completion: every in-scope screen has a current comparison or named source limitation, a text/design review, resolved required defects or an explicit exception, and consistent output documents. State image-direction results separately from pending rendered behavior; this loop does not replace the first-three-screen user feedback checkpoint.

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
- Check the rhythm against the approved arc and the [cadence rules](../../writing-funnel-copy/references/funnel-rhythm-template.md#cadence-rules): an energy screen by screen 3, no more than 3 questions in a row early (4 later), energy screens that reflect the preceding answer, varied archetypes, and plan reveal → email → paywall at the close. Report a deviation the arc does not explain as a content finding; cadence is a tested default, not a conversion guarantee.
- Each energy screen's dominant visual carries its proof (rating block, chart, level bar, product UI, testimonial) rather than decoration, and keeps the composition of its archetype so the rhythm stays visible.
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
