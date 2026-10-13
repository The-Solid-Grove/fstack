---
name: brainstorm-funnel-tests
description: "Use when turning a funnel's steps and drop-off by step into A/B test ideas: grilling scope and choices in rounds, prototyping several radically different variants per step, converging on one hypothesis and variant each, and rendering a shareable funnelsgrove PDF with the drop-off, hypothesis and current versus proposed screen."
---

# Brainstorm Funnel Tests

Before the first fstack skill in a conversation, run the [update check](../../docs/getting-started.md#agent-update-check): it applies a safe update automatically; reread this file if it reports `updated`, and offer any update it could not apply without blocking the task.

Turn drop-off data into a few simple, testable ideas: **diverge** into several radically different variants per step, **converge** on one per step with the user, then render a branded PDF. The PDF has a cover with drop-off by step, then one page per test with the step's drop-off, one hypothesis, and the current and proposed screens side by side. Everything here is a throwaway prototype; creating experiments, changing the funnel, or publishing requires its own authorization through `edit-funnel`.

## Grilling rounds

Decisions belong to the user; facts belong to you. Read the analytics, funnel source, live preview and existing variants yourself, using a sub-agent for long lookups, and never ask the user for something you can look up.

Each round asks the whole **frontier**: every open decision whose prerequisites are settled. A question that depends on another question in the same round waits for the next one. Number each question and give your recommended answer:

```
❓ **Q1** - **<title>**: <question, with the options>

➡️ <recommended answer and the one-line reason>
```

Wait for the answers, recompute the frontier, and continue. Act on a decision only after the user answers it.

## 1. Read the data

Collect the funnel (preview or production URL, or local source), the step IDs in funnel order, and drop-off by step from the analytics screenshot or table, with entered/lost counts and the period. A chart sorted by drop-off is not funnel order, and steps have different denominators, so never multiply them into a conversion. Reconcile totals that disagree (for example, answers that do not sum to visitors who continued).

Rank candidates by visitors lost, then by traffic reaching the step. Compare the entry step with the *Reach second step* benchmark in [funnel best practices](../writing-funnel-copy/references/funnel-best-practices.md). Confirm a suspected broken route or missing button on the real preview, and report a confirmed defect as a bug rather than an idea. Note existing variants on candidate steps to avoid overlapping tests.

**Done when** every candidate has its drop-off, lost visitors and live screen, and the caveats are written down.

## 2. Grill the scope

Run a round on the steps to test (recommend the top three by visitors lost), their launch order, and the PDF language (recommend the language of the people who will read it).

## 3. Diverge

For each chosen step, write three ideas, at most five, that disagree about the **mechanism**: clarity of the next action, value before effort, reduced effort, proof, or framing of the task. Ground each in FBP-004, FBP-005, FBP-007, FBP-012 to FBP-015 and FBP-032 from the [funnel best practices](../writing-funnel-copy/references/funnel-best-practices.md) and the [experimentation lesson](../web2app-essentials/references/11-experimentation.md). Ideas that differ only in color or wording are tweaks; redo one until each idea changes the hierarchy, the primary action or the framing.

Give every idea a one-sentence hypothesis of at most 180 characters, in the report language: *If <change>, more people will <action>, because <mechanism>.* Keep the observation separate from the assumed cause.

Prototype the ideas with [preview-funnel](../preview-funnel/SKILL.md) as one board per step: a single mobile screen whose `?variant=` switches between `a`, the live step in an iframe, and the ideas `b`, `c`, `d`. Add `assets/switcher.js` from this skill for the floating ← / → bar. Hold every idea to these rules:

- **Same scale:** measure the live step in the browser (headline and body size, CTA height, label size and color, answer card height) and match it unless the idea changes it. A smaller or paler variant tests visual weight, not the idea. Keep CTA label contrast at least 4.5:1.
- **Same task:** keep the task, answers, their order and scoring, timers, consent text and the step's position.
- **Less noise:** no invented scores or claims, no paid-plan disclaimers before the paywall, no visible label that repeats the headline and placeholder (keep the accessible name).

Hand over the board URLs with each idea's hypothesis.

## 4. Converge

Run a round with one question per step: which idea goes to the test. Recommend one with its reason; the user may combine parts of several ("the headline from B with the button from C"). Build the chosen variant as `<step-id>-b` and run [qa-funnel](../qa-funnel/SKILL.md) design and functional checks at each [visual pass](../qa-funnel/references/checklist.md#visual-pass) breakpoint. Show the result and keep grilling until the user confirms every variant.

For each test, settle the primary metric: next-step reach per assigned visitor, unless the step has a more direct outcome such as a saved email. Write at most two short lines on what changes or stays.

**Done when** the frontier is empty: every chosen step has one confirmed variant, hypothesis and metric.

## 5. Render the PDF

Write the report JSON described in [report format](references/report-format.md). For `current`, use the real step URL with its buttons visible; FunnelsGrove previews show a single step at `https://<preview-host>/<step-id>?previewFrame=1&previewStepLock=1`. For `proposed`, use the variant's screen URL or a screenshot. Then run, from this skill's directory:

```bash
python3 scripts/render_report.py <report.json> <out.pdf>
```

The script captures URLs at 375 × 667 and 3x scale, computes the sample per variant, and writes `<out>.html` and `<out>-screens/` next to the PDF. It requires Chrome or Chromium; pass `--chrome <path>` when it is not found. Fix a length warning by shortening the copy.

Open the PDF and inspect every page: text fits, both screens loaded fully (no blank frame, cookie banner or loader), the numbers match the analytics, and the language is right. Deliver the PDF path with one line per test, and record the ideas that lost with their hypotheses as the backlog for the next round. Ask before sending the PDF to an external service or person.
