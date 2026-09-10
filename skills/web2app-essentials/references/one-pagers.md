# Lesson one-pagers

## Web2Web changes the whole growth system

The ad click and purchase happen on the web; the customer then enters the app with paid access. The advantage comes from redesigning acquisition, selling, billing, and delivery together.

### Core rule

Ad → web funnel → web checkout → app access

### What changes

- The click is captured on the web before store friction.
- The funnel explains and personalizes the offer before install.
- Your team owns web billing and the customer lifecycle.

### What must connect

- Creative promise → first screen → offer.
- Purchase identity → app sign-in → entitlement.
- Acquisition spend → net cohort value.

### What can break it

- Judging the funnel separately from traffic and product activation.
- A strong promise that the product cannot deliver.
- Scaling before refunds, renewals, and payback are visible.

### Decision check

Can you trace one customer from ad click to first useful action and net cohort value?

## Prove channel fit before building the funnel

Web2Web works when a real problem can be explained before install, personalized with consequences, and paid back by retained customer value.

### Core rule

Message → intent → offer → first useful action

### Strong fit signals

- The user wants to start solving the problem now.
- Answers can change the result, offer, or product start.
- A clear first useful action follows purchase.

### Score before build

- 11–14: design a controlled launch.
- 7–10: close weak spots, then validate small.
- 0–6: the channel adds more complexity than growth.

### Cheapest validation

- One promising creative angle.
- A 5–10 screen clickable concept and result preview.
- A real offer with an honest interest or payment test.

### Decision check

Can you finish the fit sentence without guessing the segment, mechanism, offer, first value, or payback condition?

## Scale on cohort economics, not first purchases

A cheap conversion can hide weak renewal, slow payback, refunds, and fees. Budget decisions need predicted net cohort value and cash timing.

### Core rule

pLTV > CAC — with margin and an affordable payback window

### Model the chain

- CPM → CTR → CPC → purchase rate → CAC.
- First charge → renewals → refunds → net pLTV.
- Payout timing → cash payback → safe spend.

### Separate cohorts

- Split by geo, source, funnel, plan, and offer.
- State the pLTV horizon and prediction method.
- Replace predictions with observed renewals as cohorts mature.

### Scale gate

- Economics stay positive after refunds, fees, and variable cost.
- Payback fits the available cash reserve.
- The result survives more than one creative and traffic mix.

### Decision check

If spend doubles tomorrow, when does that cash return and what evidence supports the pLTV forecast?

## One journey needs five connected identities

The customer sees one path, but acquisition, funnel, billing, product, and analytics each need a durable identity and a clear source of truth.

### Core rule

A browser success page is never proof of payment

### Keep distinct

- Attribution answers where the customer came from.
- Authentication answers who the customer is.
- Entitlement answers what paid access is active.

### Trusted purchase flow

- Create checkout for a known internal user ID.
- Verify signed payment webhooks idempotently.
- Update billing, entitlement, and analytics from server state.

### Design failure paths

- Delayed or duplicate webhook; failed or processing payment.
- Lost deep link, wrong email, or app already installed.
- Cancel, refund, dispute, renewal failure, or repeat purchase.

### Decision check

Can the team name the source of truth, retry rule, and user-facing state for both purchase and paid access?

## Research the decision before designing screens

A funnel becomes persuasive when it reflects a specific trigger, failed attempts, desired progress, emotional stakes, and proof the product can honestly support.

### Core rule

Evidence → promise → mechanism → result → offer

### Collect evidence

- Product behavior, retained cohorts, support, and reviews.
- Customer language from interviews and sales conversations.
- Competitor patterns as hypotheses, never proof.

### Build the promise

- Name one segment and the moment that starts the search.
- Explain why earlier attempts failed and what changes now.
- Show an observable result the product can deliver.

### Choose the mechanism

- Assessment when answers change the diagnosis.
- Plan builder or calculator when inputs create a concrete result.
- Guided demo or direct response when value is clearer in action.

### Decision check

Can every claim, branch, and personalized result be traced to evidence or real product behavior?

## Every screen adds or spends mental energy

The funnel earns attention by alternating small asks with useful feedback. By the paywall, enough desire and confidence must remain to make the purchase feel like the next step.

### Core rule

Expectation → recognition → mechanism → future → commitment → offer

### Add energy

- Match the ad promise immediately.
- Give feedback, progress, proof, or a useful interpretation.
- Show how answers change the result.

### Spend carefully

- Ask only questions that improve the story or result.
- Keep each screen to one thought and one action.
- Remove repetition, vague loaders, and decorative personalization.

### Audit each screen

- Job: why does this screen exist?
- Payoff: what does the customer receive for the action?
- Next: how does the answer affect what follows?

### Decision check

If this screen disappeared, would understanding, desire, confidence, or personalization get worse?

## The paywall must complete the funnel's promise

The paywall turns accumulated desire into a specific offer; checkout removes payment friction; an upsell extends the same outcome without blocking paid access.

### Core rule

Value continuity first; pricing mechanics second

### Paywall mechanics

- A real, time-bound discount when the deadline is genuine.
- A clear money-back guarantee with visible terms.
- Inline Apple Pay or Google Pay when available.

### Checkout clarity

- Show what is charged today, renewal amount, and frequency.
- Keep selected plan, displayed price, and charged product aligned.
- Handle wallet absence, decline, retry, and checkout close.

### Judge the offer

- Compare verified purchase ARPU and cohort value, not clicks.
- Watch renewal, refunds, and disputes after the first charge.
- Measure upsell take rate without delaying app access.

### Decision check

Can a customer state what they get, what they pay now, and what renews without reading fine print?

## Identity is the durable bridge to paid access

Deep links improve the fast path but can be lost. Paid access must recover through account identity and verified subscription state.

### Core rule

Purchase email → sign in → server-verified entitlement

### Fast path

- Success page offers open app or the correct store.
- Deep link carries an opaque, short-lived handoff reference.
- Installed users land near the first useful action.

### Recovery path

- Receipt email repeats the app link and purchase identity.
- The app supports sign-in with the purchase email.
- Support can recover access by internal or payment customer ID.

### Measure separately

- Verified purchase → handoff click → first open.
- First open → sign-in → entitlement granted.
- Entitlement → first useful action.

### Decision check

If the redirect and deep link both disappear, can the buyer still sign in and receive the correct access?

## Connect every funnel event to cohort value

Product, marketing, and financial analytics answer different questions. Stable identities and reconciled events let the team move from clicks to verified net revenue.

### Core rule

Spend → customer identity → verified revenue → net cohort value

### Instrument the path

- Track rendered views and valid completions, not button intent.
- Send verified purchases and renewals from the server.
- Keep event IDs for deduplication and reconciliation.

### Share dimensions

- User, funnel version, experiment, source, and creative.
- Offer, plan, payment method, geo, device, and currency.
- Cohort date and value horizon.

### Run two views

- Daily view for delivery, breakage, and current spend.
- Cohort view for renewals, refunds, pLTV, and payback.
- Reconciliation view for analytics vs payment-provider totals.

### Decision check

Can finance, UA, and product explain the same cohort with the same IDs, amounts, and value definition?

## The creative is the first screen of the funnel

A winning ad defines the audience, trigger, angle, and promise. The landing experience must confirm that promise before asking the customer to continue.

### Core rule

Creative promise = first-screen expectation

### Map the chain

- Segment → trigger → pain or desire → angle.
- Hook → promise → first screen → personalized result.
- Result → offer → first useful action.

### Test deliberately

- Separate angle, hook, format, talent, and execution variables.
- Use distinct creatives and enough spend to read the signal.
- Keep browser and server purchase events deduplicated.

### Scale safely

- Expand proven angles into multiple executions.
- Watch downstream activation, renewal, and refunds by creative.
- Refresh before one asset becomes the whole acquisition system.

### Decision check

Does the first funnel screen feel like the exact next frame of the ad that produced the click?

## Diagnose the bottleneck before choosing the test

Growth comes from a repeatable learning system. Fix correctness first, then test the largest economic bottleneck with a written hypothesis and decision rule.

### Core rule

Priority = Impact × Confidence ÷ Effort

### Write the hypothesis

- Change X for segment Y.
- Expect metric Z to move by a stated range.
- Name the evidence and mechanism before building.

### Order the backlog

- Broken routes, payments, events, access, and disclosures first.
- Then the largest funnel or economic constraint.
- Cosmetic ideas only after structural problems.

### Protect the decision

- Fix exposure, sample, duration, primary metric, and stopping rule.
- Use net economics plus refund, activation, and risk guardrails.
- Record rollout, rollback, result, and learning.

### Decision check

Will this experiment change a business decision or what the team knows, even if it produces no uplift?

## Web billing moves the risk onto your team

Payment acceptance is only the start. Clear terms, reliable access, support, refunds, subscription management, and dispute monitoring keep the channel operable.

### Core rule

Prevent confusion before you defend a charge

### Prevent

- Match the ad, offer, descriptor, receipt, and delivered access.
- Show charge today, renewal terms, guarantee, and cancellation.
- Test privacy, consent, storefront, tax, and billing obligations.

### Operate

- Separate failed payments, refunds, and chargebacks.
- Give support the customer, payment, and entitlement context.
- Maintain accessible cancel, recovery, and refund paths.

### Monitor

- Track disputes by reason, offer, geo, source, and cohort.
- Set provider-specific thresholds and named owners.
- Use chargeback prevention services as scale and risk require.

### Decision check

Can the team detect and resolve paid-without-access, renewal surprise, and dispute spikes before the provider intervenes?

## Cut launch breadth, never the critical path

The first launch needs one complete, measurable customer journey. Start controlled, read downstream quality, and earn the right to add spend, geos, offers, and automation.

### Core rule

One segment → one offer → paid access → cohort economics

### Before traffic

- Fit score, downside/base/upside economics, budget, and loss limit.
- Evidence-backed promise, prototype, checkout, and first value.
- Verified payment, entitlement, recovery, analytics, and support.

### First traffic

- One primary geo and a small set of distinct creatives.
- Daily technical, payment, access, support, and risk review.
- Read the first and second step before downstream conversion.

### Earn scale

- pLTV exceeds CAC with margin and affordable payback.
- Access, reconciliation, retention, refunds, and disputes are stable.
- Several creatives work and the next experiment is ready.

### Decision check

If the first cohort disappoints, will the data reveal whether the problem is traffic, funnel, offer, payment, access, or retention?
