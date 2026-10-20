---
name: brainstorm-funnel-tests
description: "Use when turning a funnel's analytics for a period into recommendations and A/B test ideas: the period's dashboard metrics with one focus area (first step, quiz or paywall), steps whose drop-off exceeds the threshold, and tests grilled in rounds, prototyped as radically different variants and converged to one hypothesis and variant each, rendered as a shareable funnelsgrove PDF."
---

# Brainstorm Funnel Tests

Before the first fstack skill in a conversation, run the [update check](../../docs/getting-started.md#agent-update-check): it applies a safe update automatically; reread this file if it reports `updated`, and offer any update it could not apply without blocking the task.

Turn a period of funnel analytics into recommendations and a few simple, testable ideas: pick **one focus area**, flag the **leaking steps**, **diverge** into several radically different variants per step, **converge** on one per step with the user, then render a branded PDF. Every section is optional. The PDF opens with the recommendations, then explains them: the period's dashboard metrics, the focus area against benchmarks, the drop-off above the threshold, and one page per test with the step's drop-off, one hypothesis, and the current and proposed screens side by side. Everything here is a throwaway prototype; creating experiments, changing the funnel, or publishing requires its own authorization through `edit-funnel`.

## Grilling rounds

Decisions belong to the user; facts belong to you. Read the analytics, funnel source, live preview and existing variants yourself, using a sub-agent for long lookups, and never ask the user for something you can look up.

Each round asks the whole **frontier**: every open decision whose prerequisites are settled. A question that depends on another question in the same round waits for the next one. Number each question and give your recommended answer:

```
❓ **Q1** - **<title>**: <question, with the options>

➡️ <recommended answer and the one-line reason>
```

Wait for the answers, recompute the frontier, and continue. Act on a decision only after the user answers it.

## 1. Read the data

Ask for the period on every run; it can be any range of complete days. Offer the last 7 or the last 3 days ending yesterday as defaults, and use the user's dates when given. Download the dashboard's numbers and draft the report from them, so no figure is retyped:

```bash
fgrove analytics conversions --project <project> --funnel <funnel> --from <yyyy-mm-dd> --to <yyyy-mm-dd> --format json --out analytics.json
python3 scripts/analytics_to_report.py analytics.json --product <Product> > report.json
```

The draft holds the period, the metrics with their change against the previous period of the same length, the funnel stages, and the steps before the paywall in path order. Without CLI access, collect the funnel (preview or production URL, or local source), the step IDs in funnel order, and drop-off by step from the analytics screenshot or table, with entered/lost counts and the period. A chart sorted by drop-off is not funnel order, and steps have different denominators, so never multiply them into a conversion. Reconcile totals that disagree (for example, answers that do not sum to visitors who continued).

Rank candidates by visitors lost, then by traffic reaching the step. Compare the entry step with the *Reach second step* benchmark in [funnel best practices](../writing-funnel-copy/references/funnel-best-practices.md). Confirm a suspected broken route or missing button on the real preview, and report a confirmed defect as a bug rather than an idea. Note existing variants on candidate steps to avoid overlapping tests.

**Choose one focus area.** Compare each area's share of visitors with its range in FBP-031: *first-step conversion* (completed the first step, 30–60%), *quiz completion* (reached the paywall, 10–20%) and *paywall conversion* (started checkout, 8–15%). Focus on the area furthest below its range; when none is below, take the one with the worst change against the previous period. Write the recommendation the cover leads with as one sentence of at most 160 characters (`summary`: what to change and why), then up to three lines on why and up to three on what to do, each at most 110 characters.

**Flag leaking steps.** A step after the entry step leaks when more than 7% of its visitors leave; the email step leaks above 20%. The paywall and later steps belong to the paywall focus area. The renderer applies this rule; write one note per leaking step of at most 160 characters with the likely cause and the next move, including when traffic is too small to test. The note is also that step's recommendation on the cover, so write it as advice, not a label.

**Done when** the focus area is chosen, every leaking step and test candidate has its drop-off, lost visitors and live screen, and the caveats are written down.

## 2. Grill the scope

Run a round on the period (when the user has not named it), the focus area, the steps to test (recommend the focus area's step and the leaking steps with the most visitors lost, up to three), their launch order, and the PDF language (recommend the language of the people who will read it).

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

Before rendering, run one more round that shows everything the report would say: the period, the focus area with its why and actions, the note for each leaking step, and each test with its hypothesis, metric and variant. Ask what to include, recommending all of it; leave out what the user rejects (drop `focus`, a `dropoffs` note or a test) and rewrite what they correct. Render only after they confirm.

Complete the report JSON described in [report format](references/report-format.md): `focus`, `dropoffs` and `tests`. For `current`, use the real step URL with its buttons visible; FunnelsGrove previews show a single step at `https://<preview-host>/<step-id>?previewFrame=1&previewStepLock=1`. For `proposed`, use the variant's screen URL or a screenshot. Then run, from this skill's directory:

```bash
python3 scripts/render_report.py <report.json> <out.pdf>
```

The script captures URLs at 375 × 667 and 3x scale, computes the sample per variant, and writes `<out>.html` and `<out>-screens/` next to the PDF. It requires Chrome or Chromium; pass `--chrome <path>` when it is not found. Fix a length warning by shortening the copy.

Open the PDF and inspect every page: text fits, both screens loaded fully (no blank frame, cookie banner, loader or expired timer), the numbers match the analytics, and the language is right. A preview without live prices can leave the paywall loading; capture production instead only with analytics, pixel and other write requests blocked, so the capture adds no visitor. Deliver the PDF path with one line per test, and record the ideas that lost with their hypotheses as the backlog for the next round. Ask before sending the PDF to an external service or person.
