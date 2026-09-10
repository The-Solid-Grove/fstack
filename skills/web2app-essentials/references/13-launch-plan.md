# 13. Your first launch plan

## Lesson outcome

You'll leave with a launch sequence that tests the channel with a small controlled test and preserves the data you need for the next decision.

## Don't start with a production-perfect system

Your first launch has to be complete enough to measure economics and deliver the value people paid for. It does not have to support every geo, payment method, language, and experiment type.

A good MVP cuts breadth, not the critical path.

Critical path:

```text
one segment
→ one creative promise
→ one funnel
→ one clear offer
→ one reliable checkout
→ one identity path
→ paid access
→ first useful action
→ lifecycle/support
→ cohort economics
```

## Phase 1. Decision and economics

- Fill in the channel-fit scorecard.
- Pick the segment and problem.
- Build a downside/base/upside model.
- Set target CAC, required margin, and max payback.
- Set the test budget and loss limit.
- Check storefront and policy constraints for the target geo.

**Gate:** if even the upside case doesn't pay back, don't build the funnel. Change the offer, the product, or the economics.

## Phase 2. Research and offer

- Collect reviews, interviews, support tickets, and product data.
- Write the entry promise.
- Define the mechanism and the result.
- Describe the price today and at renewal.
- Choose the first useful action.
- List the proof and claims you're allowed to use.

**Gate:** if you can't honestly explain the value before install, test a different funnel model or angle.

## Phase 3. Funnel prototype

- Creative-to-first-screen match.
- Screen map with energy impact.
- Relevant questions and give screens.
- Real branching.
- Personalized result.
- Email capture with a functional reason.
- Paywall and checkout prototype.
- Handoff journeys.

Run moderated tests with several people from the target segment. Test comprehension, not preference: what they expect, what they're buying, how much they pay, and what happens next.

## Phase 4. Technical build

- Stable visitor and user IDs.
- UTM and click capture.
- Versioned funnel manifest and routes.
- Payment customer and subscription binding.
- Verified webhook processing.
- Entitlement states.
- App login and recovery.
- Subscription management.
- Transactional email.
- Event dictionary and dashboards.

**Stop condition:** if a frontend success page is still the only proof of payment, or a deep link is the only access path, don't send real traffic until that's fixed.

## Phase 5. QA

Use the full [launch QA checklist](templates/11-launch-qa.md). The list below is a short route through it, not a replacement.

Walk through:

- Every answer and branch.
- Invalid and empty inputs.
- Refresh, back, and re-entry.
- Meta, Instagram, and TikTok in-app browsers.
- iOS and Android.
- Small and large mobile, plus desktop.
- Every payment method.
- Checkout close, retry, and failure.
- A test payment.
- Success → install/open → login → access.
- Paid-without-deep-link recovery.
- Cancellation and refund.
- Event and amount reconciliation.
- Privacy, terms, and refund links.

A visible button is not proof. Confirm that the selected plan, coupon, wallet, and charged product all match.

## Phase 6. Controlled traffic

- One primary geo.
- A small number of distinct creatives.
- Separate IDs and a naming convention.
- Spend gates set in advance.
- Daily technical monitoring.
- No parallel funnel tests in the first days.
- Manual review of support and payment cases.

The goal of the first phase is a readable baseline, not maximum revenue.

## Phase 7. Read the first cohort

Look at these in order:

1. Traffic delivery and creative diagnostics.
2. First and second screen drop.
3. Paywall reach.
4. Checkout and purchase.
5. App sign-in and first value.
6. Early cancellations and refunds.
7. First renewal and payment failures.
8. Prediction vs actual.

Don't raise spend on a cheap first purchase until downstream signals confirm the offer quality.

## Phase 8. First experiments

Prioritize:

1. Correctness bugs.
2. The largest funnel drop with a clear hypothesis.
3. An offer or pricing hypothesis with a financial model.
4. Creative angle expansion.
5. Handoff and activation improvement.

Run one meaningful change per area. Document the result and the learning.

## 30/60/90-day view

### Days 0–30

- A stable end-to-end flow.
- A baseline for the funnel and payments.
- First cohorts.
- Support and risk process.
- Correctness issues fixed.

### Days 31–60

- First structural experiments.
- Refined pLTV prediction.
- Creative refresh.
- Activation and refund improvements.
- A decision on the next segment or geo.

### Days 61–90

- Controlled scale, once the economics gate is met.
- A second funnel or angle, once you have enough evidence.
- Automated reporting and operations.
- A roadmap for the infrastructure that actually limits growth.

## Definition of ready to scale

- pLTV exceeds CAC with the agreed margin.
- Payback fits the cash plan.
- Event and payment reconciliation are stable.
- App access works, including the recovery path.
- The first useful action is measured.
- Early retention and refund signals don't contradict the model.
- Support answers billing and access cases.
- Dispute monitoring is on.
- Several creatives can sustain traffic.
- The next experiment pipeline is ready.

## Next step

FunnelsGrove helps app teams launch and scale web funnels. You can use this course as a standalone specification: fill in the worksheets first, then turn them into a funnel, integration, and experiment plan. The final worksheet combines those decisions into the short document your team uses for a go/no-go review.

## Worksheet

[Open the Web2Web launch brief](templates/13-launch-brief.md)
