# Lesson one-pagers

## Web2Web connects acquisition, payment, and access

Acquisition and purchase happen on the web; the buyer uses the paid product in an app or browser.

### Core rule

Ad → web funnel → checkout → paid access → first useful action

### What changes

- Measure pre-purchase behavior, with consent and attribution limits.
- Explain the value before full product use.
- Own web billing, support, and the subscription lifecycle.

### What must connect

- Ad promise → first screen → offer.
- Purchase identity → sign-in → paid access.
- Acquisition spend → net cohort value.

### What can fail

- Evaluating conversion without traffic quality or activation.
- Promising value the product cannot deliver.
- Scaling before renewals, refunds, and payback are understood.

### Decision check

Can you trace a buyer from ad click to first useful action and net cohort value?

## Check channel fit with evidence

A web funnel needs a clear promise, useful delivery, and realistic net economics. A long quiz is optional.

### Core rule

Record evidence: ready / uncertain / blocked

### Check the fit

- Demand now, value before purchase, and useful questions if used.
- First useful action, net economics, reliable access, and operating owners.
- Mark each ready, uncertain, or blocked, with evidence.

### Choose the next step

- Test when the promise, offer, delivery, and loss limit are clear.
- Research assumed demand, willingness to pay, or retention.
- Fix payment-to-access or support blockers before charging.

### Keep the test small

- One audience and creative promise.
- A short clickable journey, credible preview, and real offer.
- Use an honest interest test, or payment only when delivery is ready.

### Decision check

What evidence supports the audience, mechanism, offer, first useful action, and payback condition?

## Scale on net cohort value and cash payback

Cheap first purchases can hide weak renewals, refunds, fees, and slow cash recovery.

### Core rule

Net pLTV > CAC, with margin and affordable payback

### Model the chain

- CPM → CTR → CPC → purchase rate → CAC.
- First charge + renewals − refunds, disputes, fees, taxes, and variable costs.
- Payout timing and reserves → cash payback → affordable spend.

### Define the cohort

- Separate geography, source, funnel, plan, and offer.
- State the value horizon and prediction method.
- Replace forecasts with observed renewals as cohorts mature.

### Before scaling

- Test conservative, base, and optimistic assumptions.
- Keep contribution positive and payback within available cash.
- Verify results across creatives and traffic mixes.

### Decision check

When will the next acquisition spend return as cash, and what supports the forecast?

## Connect payment, identity, and paid access

Each system needs a durable identifier, a source of truth, and a recovery path.

### Core rule

A browser success page does not prove payment

### Keep distinct

- Attribution: where the customer came from.
- Authentication: who the customer is.
- Entitlement: which paid access is active.

### Verify the purchase

- Link checkout to an internal user ID.
- Verify signed webhooks and process duplicates idempotently.
- Update billing, access, and analytics from trusted server state.

### Plan recovery

- Delayed webhooks; processing, failed, or repeated payments.
- Lost links, wrong accounts, and existing app installs.
- Cancellation, expiry, renewal failure, refunds, and disputes.

### Decision check

Who owns each purchase and access state, its source of truth, and its recovery rule?

## Research the decision before the screens

Use customer evidence and real product capabilities to choose the promise, mechanism, and offer.

### Core rule

Evidence → promise → mechanism → result → offer

### Find evidence

- Product behavior, retained cohorts, support, and reviews.
- Customer language from interviews and sales conversations.
- Competitor patterns as hypotheses to test.

### Define the promise

- Choose an audience and trigger for seeking help.
- Explain current barriers, desired progress, and emotional stakes.
- Support the promised result with product evidence.

### Choose the format

- Assessment when answers support a meaningful result.
- Plan or calculator when inputs change the output.
- Demo or direct offer when value is clear without a quiz.

### Decision check

Can each claim and personalized result be traced to evidence or product behavior?

## Make every screen worth the effort

Questions ask for attention; useful feedback and evidence help people decide whether to continue. Mental energy is a metaphor, not a score.

### Core rule

Recognize the problem → explain value → demonstrate fit → offer

### Return useful value

- Continue the ad promise.
- Give relevant feedback, explanation, or proof.
- Show what the answers actually change.

### Limit effort

- Ask questions that affect feedback, fit, or product use.
- Give each screen one main idea and next action.
- Remove repetition, fake processing, and decorative personalization.

### Check the sequence

- Purpose: what does this screen help the person understand?
- Value: what do they receive for their effort?
- Transition: does the next screen fulfill the action’s promise?

### Decision check

Would removing this screen weaken understanding, confidence, or useful personalization?

## Make the offer and payment clear

The paywall explains the purchase; checkout supports payment. Optional upsells must preserve access to what was already bought.

### Core rule

Clear value, billed totals, and next action

### Explain the offer

- Connect included value to the funnel’s demonstrated result.
- Use genuine discounts and deadlines only.
- Show conditions for any guarantee or refund offer.

### Support payment

- Keep the selected plan, charge today, and renewal terms consistent.
- Offer supported wallets with a card fallback.
- Handle processing, declines, retries, and checkout closure.

### Evaluate results

- Compare verified purchase ARPU and net cohort value.
- Track renewals, refunds, and disputes.
- Measure upsell take rate; require separate authorization.

### Decision check

Can the buyer explain what they get, pay now, and pay at renewal?

## Recover paid access through account identity

Deep links ease handoff. Account identity and verified subscription state must recover access when links fail.

### Core rule

Purchase identity → sign-in → server-verified access

### Fast path

- Offer the installed app or correct store after purchase.
- Use an opaque, short-lived handoff reference.
- Bring the buyer near the first useful action.

### Recovery

- Include the app link and purchase identity in the receipt.
- Support sign-in with the purchase email.
- Let support resolve access using internal or payment customer IDs.

### Measure each step

- Verified purchase → handoff click → first open.
- First open → sign-in → entitlement granted.
- Entitlement → first useful action.

### Decision check

Can the buyer recover correct access without the redirect or deep link?

## Connect events to net cohort value

Stable IDs and reconciled events connect product behavior, acquisition, and financial results.

### Core rule

Spend → identity → verified revenue → net cohort value

### Record completion

- Track rendered views and valid completions, not clicks alone.
- Verify purchases and renewals on the server.
- Use event IDs to deduplicate and reconcile.

### Keep shared dimensions

- User, funnel version, experiment, source, and creative.
- Offer, plan, payment method, geography, device, and currency.
- Cohort date and value horizon.

### Read three views

- Daily: spend, delivery, and breakage.
- Cohort: renewals, refunds, net pLTV, and payback.
- Reconciliation: analytics against payment-provider records.

### Decision check

Do acquisition, product, and finance use the same IDs, amounts, and value definition?

## Continue the ad promise in the funnel

The ad sets an expectation for a specific audience. The opening, result, and offer must fulfill it.

### Core rule

Creative promise → first-screen expectation

### Map the promise

- Audience → trigger → problem or desire → angle.
- Hook → promise → first screen → relevant result.
- Result → offer → first useful action.

### Test clearly

- Separate angle, hook, format, talent, and execution changes.
- Use distinct creatives and sufficient exposure.
- Deduplicate browser and server purchase events.

### Expand with evidence

- Develop several executions of proven angles.
- Track activation, renewals, and refunds by creative.
- Avoid depending on one successful asset.

### Decision check

Does the opening fulfill the expectation created by the ad?

## Test the largest verified bottleneck

Fix correctness first. Then test a written hypothesis with a primary outcome, guardrails, and a decision rule.

### Core rule

Prioritization aid: Impact × Confidence ÷ Effort

### State the hypothesis

- Change X for audience Y.
- State the expected metric change and meaningful effect to detect.
- Explain the evidence and expected mechanism.

### Choose the work

- Fix broken routes, payments, events, access, and disclosures.
- Then address the largest economic constraint.
- Treat priority scores as estimates, not experimental evidence.

### Protect the decision

- Set exposure, allocation, sample, and duration; choose fixed-horizon or sequential analysis.
- Check allocation/exposure quality; follow the planned stopping rule.
- Evaluate net economics, activation, refunds, and risk; record rollout or rollback.

### Decision check

What decision or learning will the test produce, including when it shows no uplift?

## Own the risks of web billing

Clear terms, reliable access, subscription management, and support keep the channel operable.

### Core rule

Prevent billing confusion and access failures

### Prevent

- Align the ad, offer, descriptor, receipt, and delivered access.
- Show charges, renewal terms, cancellation, and any guarantee conditions.
- Check applicable privacy, consent, storefront, tax, and billing requirements.

### Operate

- Distinguish failed payments, refunds, and chargebacks.
- Give support payment, customer, and access context.
- Maintain cancellation, refund, and access-recovery paths.

### Monitor

- Track disputes by reason, offer, geography, source, and cohort.
- Assign owners and provider-specific action thresholds.
- Use dispute-prevention services when scale and risk justify them.

### Decision check

Can you detect and resolve missing access, renewal confusion, and dispute spikes promptly?

## Launch one complete, measurable journey

Start with a controlled test. Add spend, markets, and offers as delivery and cohort evidence justify it.

### Core rule

One audience → one offer → paid access → net cohort value

### Before traffic

- Fit evidence, three economics scenarios, budget, and loss limit.
- Supported promise, prototype, checkout, and first useful action.
- Verified payment, access, recovery, analytics, and support.

### First traffic

- One primary market and a few distinct creatives.
- Daily checks of delivery, payment, access, support, and risk.
- Find the earliest broken step before interpreting later conversion.

### Before scaling

- Net pLTV exceeds CAC with margin and affordable payback.
- Access, reconciliation, retention, refunds, and disputes remain stable.
- Several creatives work; the next test has a clear purpose.

### Decision check

Can the data distinguish traffic, funnel, offer, payment, access, and retention problems?
