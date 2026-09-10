# 11. Experiments and growth process

## Lesson outcome

You'll build an experiment backlog and a process that turns observations into validated decisions.

## Growth is a conveyor

A funnel that works today does not stay that way on its own. Creatives burn out, traffic mix shifts, prices go stale, payment acceptance varies by geo, competitors copy offers.

A growth system continuously moves hypotheses through stages:

```text
observation
→ hypothesis
→ evidence
→ impact model
→ design
→ build
→ QA
→ run
→ analysis
→ rollout or rollback
→ learning
```

The value of an experiment is not only uplift. It should change what the team knows.

## What a good hypothesis looks like

Format:

> If we change **X** for **segment Y**, then **metric Z** will change by **expected range**, because **evidence/mechanism**.

Write down:

- problem/observation;
- proposed change;
- evidence;
- target audience;
- expected impact and assumptions;
- primary metric;
- guardrails;
- sample/duration rule;
- implementation scope;
- decision rule.

"Let's make the paywall prettier" is not a hypothesis. "Show the personalized plan result above pricing to keep continuity with the funnel; we expect verified purchase ARPU to rise without making refunds worse" is a testable idea.

## Where hypotheses come from

- funnel step data;
- session recordings;
- support/refund reasons;
- retained cohort behavior;
- quiz-answer segments;
- competitor mechanics;
- user interviews;
- winning creatives;
- technical failures;
- prior winning tests.

In funnel audits we routinely look for correctness defects, not just marketing hypotheses: dead routes, a plan selector that changes the UI but not the charged product, or personalization that isn't tied to the answer. These are conversion and trust bugs. Technical QA often produces a stronger hypothesis than a new animation.

## Prioritization

Use a simple score:

```text
Priority = Impact × Confidence ÷ Effort
```

For your first backlog, use a 1–5 scale for each factor; for Effort, `5` means the most expensive and slowest test. The scale is there to compare items within one team, not to produce objective truth.

### Impact

Estimate it through your financial model. How does a change in CR, AOV, renewal, or refund rate affect net revenue?

### Confidence

Evidence, from strongest to weakest:

1. your own repeatable experiment;
2. your own behavioral/cohort data;
3. direct user research;
4. a pattern observed in similar funnels;
5. opinion.

### Effort

Count design, copy, engineering, analytics, traffic, QA, and time-to-learn.

## What to test first

Fix correctness problems first:

- a broken route;
- payment mismatch;
- a missing event;
- mobile layout failure;
- a paid user without entitlement;
- inaccessible cancellation;
- wrong disclosure.

Then look for the largest economic bottleneck:

- first-screen drop;
- weak ad-to-funnel match;
- paywall reach;
- checkout conversion;
- offer/plan mix;
- app activation;
- renewal/refunds.

Cosmetic tests come after structural problems.

## A/B test or a new funnel

Use an A/B test when the audience and promise are the same, traffic is sufficient, and the change can be isolated.

Launch a separate funnel when the segment, creative promise, product angle, or offer changes so much that the variants stop being one experience.

Small traffic requires large contrastive hypotheses. A micro copy change cannot be reliably separated from noise when sales volume is low.

## Metrics

The primary metric depends on the experiment, but tie the final decision to economics:

- verified purchase ARPU;
- contribution per visitor;
- predicted cohort value per visitor;
- net ROAS.

Guardrails:

- refund/dispute rate;
- first renewal;
- app activation;
- first useful action;
- support contacts;
- technical error rate.

CR can win while ARPU loses. ARPU can rise and refunds can take the effect back later. Keep a cohort review running after rollout.

## Experiment integrity

Before launch, fix in writing:

- unit of randomization;
- eligibility and exposure event;
- sample-size method;
- minimum runtime to cover seasonality;
- primary and secondary metrics;
- stopping rule;
- exclusions;
- data-quality dashboard.

Don't stop a test at the first attractive p-value. Don't change a variant or traffic allocation without recording it. Don't run tests at the same time that conflict on the same part of the journey.

### Record the analysis method

The experiment card should name the analysis tool/engine and version, fixed-horizon or sequential method, planned allocation, decision thresholds, and runtime/sample requirements. Freeze these before exposure begins. A dashboard's familiar p-value label does not tell you whether repeated looks are supported.

For a fixed-horizon analysis, follow the planned endpoint rather than stopping when the result first looks favorable. If you need continuous decisions, select and configure a method designed for sequential testing. [Statsig's SPRT documentation](https://docs.statsig.com/experiments/advanced-setup/sprt) is one implementation example; its method and setup are not interchangeable with every other sequential option.

### Check allocation before interpreting lift

Compare observed assignment/exposure counts with the planned traffic split. A sample ratio mismatch (SRM) can signal broken randomization, missing events, eligibility changes, or a treatment-dependent logging problem. Investigate the cause before treating the estimated lift as trustworthy; do not fix it by casually dropping inconvenient users.

[Microsoft Research's SRM guidance](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/) explains why this is a data-integrity check, not evidence that a variant won or lost.

## Operating rhythm

A small team can combine roles, but you need clear ownership for:

- UA/creative;
- product/funnel;
- design;
- delivery/engineering;
- analytics;
- payments/support.

Weekly:

- review live experiments;
- unblock delivery;
- check data quality;
- debrief completed tests;
- pick the next hypotheses.

Monthly:

- plan vs actual;
- count of valid experiments;
- win rate by source and placement;
- cumulative economic impact;
- prediction accuracy;
- recurring bottlenecks in the process.

Test count is only useful when quality is high enough. Don't turn a throughput KPI into a stream of meaningless button-color tests.

## Experiment card

Use the full [experiment card](templates/09-experiment-card.md). It captures the priority score, MDE, sample-size method, stopping rule, QA, and rollout/rollback in one place.

## Exercise

Collect 20 observations, turn the best 10 into hypotheses, score Impact/Confidence/Effort, and take the top three. At least one should fix end-to-end correctness, one should address the main economic bottleneck, and one should open up new learning.

## Worksheet

[Open the experiment card](templates/09-experiment-card.md)
