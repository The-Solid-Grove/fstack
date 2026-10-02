# 10. Paid acquisition and performance creatives

An ad selects an audience and creates an expectation. The first screen, result, and offer must continue that promise.

## Map each angle

Use the [creative-to-funnel map](templates/04-creative-funnel-map.md) to connect:

| Element | Decision |
| --- | --- |
| Segment and trigger | Who recognizes the problem, and why now? |
| Angle | Which reason to buy is being tested? |
| Hook | What opening words or image earn attention? |
| Format and proof | How is the idea shown, and what supports it? |
| Promise | What should the person expect after clicking? |
| First screen and result | How does the funnel fulfill that expectation? |
| Offer | What is sold, on what terms, and with what first useful action? |

A new angle tests a different reason to buy; an iteration changes its execution. Track them separately and match each promise to its funnel.

## Separate outcomes from diagnostics

Judge creatives by CAC, net cohort ROAS at a stated horizon, contribution pLTV/CAC, and the spend they can sustain. Use CPM, CTR, CPC, video engagement, second-screen reach, and purchases per 1,000 impressions to explain the result.

High CTR and cheap first purchases can still produce weak cohorts. Build a web baseline from impression to net value; app-install benchmarks describe a different path.

## Define the test

Before launch, record:

- Geo, audience, creative IDs, and funnel version.
- Optimization event, attribution model/window, and primary metric.
- Budget, required evidence, stop rule, and scale rule.
- Refund, activation, and cohort-value guardrails.

Treat targeting choices, including broad targeting, as hypotheses. Keep angle, hook, format, and funnel changes distinguishable enough to explain the result.

## Verify the purchase signal

Use the event definitions in [analytics](09-analytics-and-forecasting.md). Before optimizing for purchase, confirm:

- Payment is verified on the backend before the event fires.
- Value, currency, product, and customer IDs are correct.
- Browser and server copies share an event ID and deduplicate.
- Test transactions stay out of production reporting.
- Refunds and downstream activation remain visible internally.
- The event and its parameters comply with applicable consent and platform restrictions.

Server events improve delivery reliability; they do not recover consent or remove attribution gaps.

## Run a repeatable creative process

Keep a backlog, licensed assets, creative versions, funnel mapping, results, and fatigue history. Count useful tests, not videos exported.

Use aggregate, permitted funnel insights in new briefs: recurring goals, segments reaching first value, answers associated with retention, and promises attracting weak cohorts. Correlation suggests a hypothesis to test.

## Increase spend when the evidence holds

Scale when measurement is stable, mature or defensibly predicted cohorts meet the economics target, and activation/refund/dispute guardrails hold. Results should extend beyond one lucky day or short-lived creative.

Recheck after increasing budget: audience mix and acquisition cost can change. Use [experimentation](11-experimentation.md) for controlled comparisons.

**Output:** a completed creative map, a small set of distinct hypotheses, matching funnel destinations, and explicit stop/scale conditions.
