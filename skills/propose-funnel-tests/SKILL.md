---
name: propose-funnel-tests
description: "Use when turning a funnel's steps and drop-off by step into A/B test recommendations: choosing the steps to test, writing one hypothesis per step, building and checking the proposed variant, and rendering a shareable funnelsgrove PDF with the drop-off, hypothesis and current versus proposed screen."
---

# Propose Funnel Tests

Before the first fstack skill in a conversation, run the [update check](../../docs/getting-started.md#agent-update-check): it applies a safe update automatically; reread this file if it reports `updated`, and offer any update it could not apply without blocking the task.

Turn drop-off data into a few simple, testable proposals. The deliverable is a branded PDF: a cover with drop-off by step, then one page per test with the step's drop-off, one hypothesis, and the current and proposed screens side by side. Proposals are local prototypes; creating experiments, changing the funnel, or publishing requires its own authorization through `edit-funnel`.

## 1. Collect inputs

- **Funnel:** preview or production URL, or local source, and the step IDs in funnel order.
- **Drop-off by step:** an analytics screenshot or table with each step's drop-off, and entered/lost counts where shown. Record the period.
- **Scope:** the steps the user named, or propose the strongest candidates (three by default).

Ask only for inputs that block the work. Note data caveats before using numbers: a chart sorted by drop-off is not funnel order, and steps have different denominators, so never multiply them into a conversion. Reconcile totals that disagree (for example, answers that do not sum to visitors who continued).

## 2. Choose and order the steps

Rank candidates by visitors lost, then by traffic reaching the step. Compare the entry step with the *Reach second step* benchmark in [funnel best practices](../writing-funnel-copy/references/funnel-best-practices.md). Fix correctness first: confirm a suspected broken route or missing button on the real preview, and report a confirmed defect as a bug, not a test. Check the funnel source for active or existing variants on the same step and avoid overlapping tests. The final order is the launch priority.

## 3. Write one hypothesis per step

Ground each proposal in FBP-004, FBP-005, FBP-007, FBP-012 to FBP-015 and FBP-032 from the [funnel best practices](../writing-funnel-copy/references/funnel-best-practices.md) and the [experimentation lesson](../web2app-essentials/references/11-experimentation.md).

- One sentence, at most 180 characters: *If <change>, more people will <action>, because <mechanism>.* Write it in the report language.
- Separate the observation from the assumed cause; drop-off alone does not explain why people leave.
- Change only what the hypothesis needs. Keep the task, answers, their order and scoring, timers, consent text and the step's position.
- Remove noise rather than adding it: no invented scores or claims, no paid-plan disclaimers before the paywall, no visible label that repeats the headline and placeholder (keep the accessible name).
- Name the variant `<step-id>-b`. Use the step's next-step reach per assigned visitor as the primary metric unless the step has a more direct outcome, such as a saved email.

## 4. Build and check the proposed screen

Use [preview-funnel](../preview-funnel/SKILL.md) to build one temporary screen per proposal, cloning the live step's fonts, colors and spacing. Match the control's scale: measure the current step in the browser (headline and body size, CTA height, label size and color, answer card height) and keep the variant equal unless the hypothesis changes it. A smaller or paler variant tests visual weight, not the hypothesis. Keep CTA label contrast at least 4.5:1.

Run [qa-funnel](../qa-funnel/SKILL.md) design and functional checks on every variant at each [visual pass](../qa-funnel/references/checklist.md#visual-pass) breakpoint. Show the variants and hypotheses to the user and revise before rendering the PDF.

## 5. Render the PDF

Write the report JSON described in [report format](references/report-format.md). For `current`, prefer the real step URL with its buttons visible; FunnelsGrove previews show a single step at `https://<preview-host>/<step-id>?previewFrame=1&previewStepLock=1`. For `proposed`, use the prototype screen URL or a screenshot. Then run, from this skill's directory:

```bash
python3 scripts/render_report.py <report.json> <out.pdf>
```

The script captures URLs at 375 × 667 and 3x scale, computes the sample per variant, and writes `<out>.html` and `<out>-screens/` next to the PDF. It requires Chrome or Chromium; pass `--chrome <path>` when it is not found. Fix any length warning by shortening the copy, not by shrinking the layout.

Open the PDF and inspect every page: text fits, both screens loaded fully (no blank frame, cookie banner or loader), the numbers match the analytics, and the language is right. Deliver the PDF path with one line per test. Ask before sending the PDF to an external service or person.
