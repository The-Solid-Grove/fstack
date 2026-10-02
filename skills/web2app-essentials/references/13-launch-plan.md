# 13. Your first launch plan

Reduce markets, offers, and integrations for the first launch while preserving the complete customer path:

**One segment → one promise → funnel → clear offer → checkout → identity → paid access → first value → lifecycle/support → cohort economics.**

## 1. Decide whether the channel can work

Complete the [fit worksheet](templates/01-channel-fit-scorecard.md) and [economics model](templates/02-economics-model.md). Set segment, target CAC, margin, maximum cash payback, test budget, and loss limit. Check the market's distribution and billing rules.

**Gate:** if even a credible upside case cannot pay back acquisition, revise the plan before building.

## 2. Define the promise and offer

In the [research and offer brief](templates/03-research-offer-brief.md), explain the problem, mechanism, result, first product action, included access, price, renewal terms, and supporting evidence.

**Gate:** the value must be understandable before install, and the product must deliver what is promised.

## 3. Prototype the whole journey

Use the [screen map](templates/05-screen-map.md) and [paywall spec](templates/06-paywall-checkout-spec.md) to connect the creative, questions, feedback, branches, result, offer, and handoff. Identity requests need a useful purpose.

Test comprehension with the target segment: what are they buying, what do they pay, and what happens next? Resolve misunderstandings before implementation.

## 4. Build reliable delivery and measurement

Connect acquisition, visitor/user IDs, funnel versions, payments, entitlement, login, and events. Use the [identity map](templates/07-identity-entitlement-map.md), [event dictionary](templates/08-event-dictionary.md), and [join worksheet](templates/12-end-to-end-join.md). Include idempotent payment processing, subscription management, recovery, and service messages.

**Gate:** verify payment on the server and provide paid-access recovery when the deep link fails.

## 5. Verify the critical paths

Complete the [launch QA checklist](templates/11-launch-qa.md), including:

- Branches, invalid input, back/refresh, and return visits.
- Relevant devices and in-app browsers.
- Matching plan, coupon, displayed price, and charge.
- Wallet/card payment, processing, failure, retry, and checkout close.
- One verified purchase and deduplicated events.
- Installed/new app, desktop-to-phone, and lost-link recovery.
- Correct access, first value, cancellation, refund, and support.
- Disclosures and event/payment reconciliation.

**Gate:** resolve payment, access, measurement, and required customer-control failures before traffic.

## 6. Run controlled traffic

Use a small set of creatives, recorded campaign IDs/funnel versions, and predefined spend limits. Monitor technical, payment, and support issues. Avoid simultaneous changes that obscure the baseline. Stop at critical failures or the agreed loss limit.

## 7. Read the cohort before scaling

Follow the chain: traffic quality → entry-screen reach → paywall → checkout → verified purchase → product activation → cancellations/refunds → renewal → forecast versus actual.

Increase spend when:

- Mature or defensibly forecast net cohort value exceeds CAC by the agreed margin.
- Cash payback and payout timing fit the reserve.
- Payments reconcile; access and recovery work.
- Activation, retention, refunds, and disputes support the model.
- Support/risk owners are ready; results extend beyond one lucky day or creative.

Recheck these conditions after increasing budget because traffic quality can change.

## 8. Choose the next experiment

Prioritize correctness, then the largest economic constraint. Use the [experiment card](templates/09-experiment-card.md) to record the hypothesis, metric, guardrails, evidence, decision, and learning.

Expand markets or funnels when economics and operating capacity support them. Calendar milestones alone do not justify scale.

**Output:** a [launch brief](templates/13-launch-brief.md) with decisions, QA evidence, risks, owners, budget, stop/scale rules, and first experiments.
