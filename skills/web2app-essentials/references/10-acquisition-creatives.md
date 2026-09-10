# 10. Paid acquisition and performance creatives

## Lesson outcome

You'll build a creative-to-funnel test plan in which the ad promise, the first screen, and the offer work as a single story.

## The creative starts the funnel

An ad does more than deliver traffic. It selects the audience, shapes awareness, and sets an expectation. That is why "creative is targeting" is a useful operating model, even when the campaign relies on platform targeting.

Every creative answers four questions in advance:

- who should recognize themselves;
- which situation activates the need;
- which mechanism or outcome triggers the click;
- what the person expects to see after the click.

If the funnel starts a different story, you are paying for curiosity you cannot follow through on.

## Creative-to-funnel map

| Element | Definition |
| --- | --- |
| Segment | a specific group and context |
| Trigger | what has just happened |
| Pain/desire | what the person wants to avoid or achieve |
| Angle | which interpretation of the problem is used |
| Hook | the first words or frame |
| Promise | what the person expects after the click |
| First screen | how the funnel confirms the promise |
| Result | what the funnel helps the person understand or get |
| Offer | what is being sold |

Build a separate map for each angle. Don't send ten different promises into one generic funnel when their awareness levels and desired results differ.

## What to test in a creative

Keep the dimensions separate:

- **angle:** problem, aspiration, mechanism, identity, comparison;
- **hook:** question, claim, visual interruption, demonstration;
- **format:** UGC, product demo, static, explainer, before/after;
- **proof:** product behavior, real testimonial, data, authority;
- **CTA:** assessment, plan, result, direct offer.

An iteration changes execution inside a winning angle. A new angle tests a different reason to buy. Don't mix the two in reporting.

## Creative metrics

Primary:

- CAC;
- D0 and predicted cohort ROAS;
- contribution pLTV/CAC;
- the spend a creative can sustain.

Diagnostic:

- CPM;
- hook/hold rate;
- CTR;
- CPC;
- click → second screen;
- paywall views per 1,000 impressions;
- purchases per 1,000 impressions.

A high CTR can mean a strong hook and the wrong buyers. A low CPM can bring in an audience with poor renewal. Diagnostic metrics explain the result, but they do not replace economics.

## Campaign test design

For every creative test, specify in advance:

1. geo and audience constraints;
2. funnel version;
3. optimization event;
4. budget and stop conditions;
5. attribution window;
6. success metric;
7. minimum spend/conversions needed for a decision;
8. guardrails: refunds, activation, pLTV quality.

Broad targeting is often a reasonable baseline on Meta, but that is a hypothesis, not a law. Platform algorithms, account maturity, market, and signal quality all change. Test broad against meaningful alternatives on your own account.

Don't carry app-install benchmarks over directly. Web traffic competes in a different auction and moves the user toward a different goal: a click plus a long funnel requires more intermediate decisions, but it gives you first-party behavioral signal and a web purchase. Build a new baseline from your own chain, from impression to net cohort value.

## Browser and server events

Before launch, lock down the event definitions and joins from the [analytics lesson](09-analytics-and-forecasting.md). Acquisition should not define what `purchase` means on its own.

Send key events through both browser and server when the platform supports both paths. Use a single event ID for deduplication.

Before optimizing for Purchase, check that:

- the event fires only after verified payment;
- currency and value are correct;
- test purchases stay out of production data;
- browser/server duplicates are not counted twice;
- refunds and downstream quality are available in internal analytics;
- restricted categories do not block the chosen event or parameters.

A server-side event does not recover lost consent and does not override platform policies. It makes signal delivery more reliable within the limits you are allowed to work in.

## Creative production system

Keep a record of:

- an idea backlog with source and angle;
- raw assets and licenses;
- versioned creative files;
- the link from creative ID to funnel version;
- test results and learnings;
- winner iterations;
- fatigue/refresh history.

The key KPI for this process is the number of quality creative hypotheses that reached a sufficient test. The number of exported videos is useless on its own.

## How the funnel improves creatives

A web funnel collects answers before purchase. Use aggregate, consented data to understand:

- which goals come up most often;
- which answers correlate with purchase and retention;
- which segment reaches first value;
- where a promise attracts weak cohorts.

These insights feed back into creative briefs. The funnel becomes a research surface, and creatives become the way to test the segments you found.

## Scale

Increase spend when:

- the funnel and event delivery are technically stable;
- the economics hold on a mature or reasonably predicted cohort;
- the result does not depend on a single lucky day;
- the creative keeps absorbing spend without a sharp rise in CAC or deterioration in net ROAS;
- purchase-to-app activation and refund/dispute guardrails are not degrading.

After you scale, traffic composition changes. Treat a budget increase as a new observation period, not an automatic continuation of the test result.

## Exercise

Create three creative angles. For each one, fill in the map and produce:

- two hooks;
- two formats;
- the matching first screen;
- one funnel/result;
- one offer;
- stop/scale rules.

Don't launch combinations where the ad and the first screen cannot be checked as a single promise chain.

## Sources

- [Meta Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/)

## Worksheet

[Open the creative-to-funnel map](templates/04-creative-funnel-map.md)
