# 11. Experiments and growth process

Use experiments to resolve a decision about the funnel. The useful output is evidence that changes what to build, keep, or stop.

## Start with the bottleneck

Find observations in funnel events, retained cohorts, interviews, support/refund reasons, recordings, creatives, and earlier tests. Competitor patterns can suggest ideas; they do not prove an effect for another product.

Fix correctness first: broken routes, incorrect charges, missing events, paid users without access, and inaccessible cancellation. Then investigate the largest economic constraint, from entry-screen loss through checkout, activation, renewal, and refunds.

Write a hypothesis:

> Changing **X** for **segment Y** should improve **metric Z**, because **evidence or mechanism**.

Record the observation, proposed change, assumptions, expected economic impact, scope, primary metric, guardrails, and decision rule in the [experiment card](templates/09-experiment-card.md).

## Prioritize and choose the comparison

Use `Impact × Confidence ÷ Effort` to compare a backlog. On a 1–5 scale, higher effort means a harder, slower test. This is a planning aid, not an objective prediction.

- **Impact:** estimate the effect on net value through conversion, price, renewal, or refunds.
- **Confidence:** prefer repeatable experiments and relevant cohort data, then direct research, comparable patterns, and opinion.
- **Effort:** include copy, design, engineering, measurement, QA, traffic, and time to learn.

Use an A/B test when audience and promise are comparable, the change is identifiable, and traffic supports a useful decision. A substantially different segment, promise, or offer may warrant a separate funnel. Low traffic favors larger meaningful differences over tiny wording tests.

## Choose metrics that answer the decision

Select one primary outcome, such as contribution per visitor, net ROAS, or cohort value per eligible user. Define the revenue window and denominator; “ARPU” alone is incomplete.

Track guardrails: refunds/disputes, first renewal, activation, first useful action, support contacts, and technical errors. Higher conversion can still reduce value. Continue cohort checks after rollout when renewal or refunds arrive later.

## Fix the analysis before exposure

Record:

- Randomization unit, eligibility, exposure event, and planned allocation.
- Baseline, absolute and relative minimum detectable effect (MDE).
- Sample-size method, uncertainty thresholds, and minimum runtime for relevant cycles.
- Analysis tool/engine and version; fixed-horizon or sequential method.
- Primary/secondary metrics, exclusions, stopping rule, and rollout/rollback conditions.
- Assignment, exposure, and event-quality checks.

For example, a 20% relative lift from 3.0% conversion means 3.6%, an increase of **0.6 percentage points**. The sample requirement depends on that difference, the unit of analysis, significance level, statistical power, allocation, and method. For a conventional fixed-horizon two-proportion calculation, state alpha and power explicitly. Estimate runtime from eligible traffic and allow for data loss and relevant weekly patterns.

If the sample is unaffordable, test a larger meaningful change or make a qualified decision from the available evidence. Do not label an inconclusive result a winner.

## Protect the result

For fixed-horizon testing, follow the planned endpoint. Continuous decisions require a method designed and configured for sequential analysis. A familiar p-value on a dashboard does not make repeated stopping decisions valid.

Before interpreting lift, compare observed assignment and exposure counts with the planned split. **Sample ratio mismatch (SRM)** can indicate broken assignment, missing events, changed eligibility, or treatment-dependent logging. Investigate it before trusting the estimate; dropping inconvenient users does not repair the design.

Record changes to variants or allocation. Avoid overlapping experiments that interfere with the same decision unless the design accounts for that interaction. Keep technical failures and data-quality exclusions visible.

## Close the loop

Move each test through hypothesis → design → build → QA → run → analysis → rollout/rollback → learning. Assign owners for delivery, acquisition, analytics, and payment/support effects.

Review active tests for data quality and delivery blockers. For completed tests, record uncertainty, guardrails, cohort follow-up, and the next decision. Review the backlog against recurring economic constraints and forecast error. Test volume matters only when tests produce trustworthy learning.

**Output:** a prioritized backlog and completed experiment cards with a decision rule, QA evidence, result, learning, and rollout or rollback plan.
