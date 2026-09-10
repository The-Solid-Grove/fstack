# 12. Payments risk, support, and compliance

## Lesson outcome

You'll build a risk register and an operating process that protect customer trust and your ability to accept payments.

Last reviewed: September 10, 2026. Recheck the rules for your specific markets and app category before launch.

## What moves to your team

With web billing, your team owns:

- payment acceptance;
- billing communication;
- cancellation;
- refunds;
- fraud and disputes;
- taxes;
- privacy/consent;
- subscription disclosures;
- post-purchase support.

You can't bolt these processes on "after scale." A basic version of each has to exist before the first real payment.

## Failed payment, refund, and chargeback are different events

**Failed payment:** the money was never collected.

**Refund:** the merchant voluntarily returns a collected payment.

**Chargeback/dispute:** the cardholder challenges a payment through their bank; the processor withdraws the disputed amount and may add a fee.

A dispute doesn't have to come from fraud. It can happen because someone didn't recognize the descriptor, didn't understand the renewal, or couldn't cancel and get a refund quickly.

## Recover failed renewals deliberately

Separate recoverable declines from failures requiring customer action. Use the payment provider's supported retry policy, request a payment-method update when needed, and reconcile invoice/payment state before another attempt. Define the retry end, grace period, entitlement state, and communication for each outcome.

[Stripe Smart Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries) documents retry behavior and hard-decline limits. A failed renewal is not permission to silently change the amount or charge an unrelated saved card. Measure recovered net revenue together with duplicate charges, complaints, and continued access errors.

## Prevention starts with the experience

Before you add specialized services, get these in place:

- a recognizable statement descriptor;
- clear today/renewal terms;
- a purchase receipt;
- simple login/access recovery;
- visible support contact;
- self-service subscription management;
- cancellation confirmation;
- a reasonable refund process;
- reminder rules for the offers and jurisdictions where they apply.

Stripe recommends clear billing terms, easy cancellation, and a flexible refund policy as ways to reduce subscription disputes.

## Chargeback monitoring

Track these separately:

- disputes by card network/provider;
- fraud reports;
- dispute reason;
- cohort/offer/creative/geo;
- count and rate using the formula of the relevant program;
- time lag from transaction to dispute;
- prevented disputes and false matches.

Card-network programs and thresholds change. Use your provider's or the network's current documentation, not a number from an old course.

Our working rule: at roughly $5k in monthly web revenue, set up continuous monitoring and evaluate a chargeback prevention service. This is an internal operational heuristic, not an official threshold from Stripe or the card networks.

A chargeback prevention service receives an early signal about a possible dispute and tries to resolve it before the chargeback is registered, often through a fast refund. Coverage and the effect on network metrics differ by provider and by the type of fraud or dispute, so the service needs to be measured rather than treated as full protection.

## Support as part of the funnel

The main reasons people contact you:

- "I don't understand this charge";
- "I want to cancel";
- "I can't log in";
- "I paid, but access is blocked";
- "I want a refund";
- "I didn't expect a renewal."

Route each reason to an owner and a system action. Given an email, internal ID, or payment ID, support needs to be able to:

- find the customer;
- see payment/subscription state;
- restore access;
- cancel or refund;
- confirm the active-until date;
- record a structured reason.

These reasons feed back into the funnel, the paywall, the app handoff, and the product backlog.

## Subscription management

An online subscriber needs a simple online path to manage the subscription. The flow shows the current plan, renewal, payment status, and cancellation.

Make cancellation no harder than signup. A retention offer is acceptable only as a clear optional choice, and only where local rules allow it; the direct path to completing cancellation has to stay available.

## Billing disclosures

Before payment, state clearly:

- that a recurring subscription is starting;
- the amount charged today;
- the billing frequency;
- the subsequent amount;
- the terms of any trial/intro period;
- how and when to cancel;
- the refund policy;
- Terms and Privacy links.

Get affirmative consent and keep the evidence where applicable rules require it. A separate upsell requires its own clear authorization.

Don't bury material terms in barely visible copy. Brevity is fine; ambiguity isn't.

## Turn legal review into an offer checklist

For each market and offer, record the trial/intro period, renewal cadence, disclosure and consent evidence, reminder timing/content, cancellation channels, owner, official source, and review date. Store the evidence and reminder/cancellation test results with the [risk register](templates/10-risk-register.md). Update the checklist when either the offer or the applicable rule changes.

US federal and state obligations are separate. The FTC's amended negative-option rule was vacated in July 2025; [ROSCA](https://www.ftc.gov/legal-library/browse/statutes/restore-online-shoppers-confidence-act) and applicable state laws still need review. The [FTC's negative-option page](https://www.ftc.gov/legal-library/browse/rules/negative-option-rule) tracks the rule's status.

Small statutory differences matter in implementation:

- [Maine §1210-C](https://www.legislature.maine.gov/statutes/10/title10sec1210-C.html) allows a checkbox, electronic signature, or another affirmative action for renewal consent; a checkbox is not the only mechanism.
- [Maryland §14-1329](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&enactments=false&section=14-1329) covers reminders for free gifts or trials lasting more than 14 days, with a 3–21-day notice window and statutory exceptions. That is not a blanket rule for every discounted offer.
- [Connecticut §42-158ff](https://www.cga.ct.gov/2026/sup/chap_742d.htm) has an annual reminder requirement. Its specific disclosure before a retention offer concerns telephone cancellation; do not recast it as a universal rule for a web save-offer layout.
- [Virginia §59.1-207.46](https://law.lis.virginia.gov/vacodeupdates/title59.1/section59.1-207.46/) includes an in-person enrollment exception to its same-medium cancellation rule.

These examples explain why the checklist is per market and offer. They do not replace a review of all jurisdictions where you sell.

## Store rules

Whether external purchases and links are allowed depends on the storefront, the app category, and the program. Current Apple guidelines describe the US storefront and entitlement-based options in other regions separately. Google Play also runs different billing-choice, alternative-billing, and external-link programs, each with its own enrollment, reporting, and service-fee requirements.

Check policy before every launch market. Don't position Web2Web as a universal way to "get around Apple or Google." In this model, acquisition and purchase start on the web, but the app still has to comply with the rules of its distribution platform. Don't build the current commission and external-link regime into your long-term model as if it were fixed.

## Privacy and funnel answers

A quiz can collect data about health, finances, age, behavior, and other sensitive circumstances. Before you collect it, decide:

- which answers the service genuinely needs;
- where they're stored and for how long;
- who has access;
- which answers go to analytics/ad platforms;
- what consent and deletion path your target markets require;
- whether you can get the same learning from less sensitive data.

Don't send raw sensitive answers to advertising tools. Privacy review applies to event design as much as it does to the consent form.

## Taxes and merchant model

With a PSP, you usually remain the merchant and are responsible for applicable sales tax/VAT, invoices, and reporting. A Merchant of Record takes on more of those obligations, but it changes fees, checkout control, and the customer relationship.

The decision depends on:

- countries;
- product tax classification;
- revenue thresholds/nexus;
- payment methods;
- required checkout customization;
- internal finance/legal capacity.

Don't reuse a generic tax threshold from someone else's table. Get a review for your markets.

## Risk dashboard

Review weekly:

- payment acceptance and failure reasons;
- refunds;
- disputes and fraud signals;
- cancel rate;
- support volume and response time;
- paid-without-access cases;
- billing email delivery;
- chargeback-prevention outcomes;
- provider reserves/payout changes;
- policy/compliance incidents.

## Risk register

| Risk | Signal | Threshold/action | Owner | Prevention | Recovery |
| --- | --- | --- | --- | --- | --- |
| Paid, no access | support/event gap | investigate immediately | Product/Support | identity + entitlement QA | manual bind/recovery |
| Unrecognized charge | descriptor/dispute reason | trend review | Payments | clear descriptor/receipt | refund/support |
| Renewal surprise | cancel/refund reason | offer review | Growth/Legal | clear terms/reminders | refund/cancel |
| Fraud spike | provider/network signal | provider-specific | Risk | screening/capture rules | block/refund/respond |
| Policy mismatch | review rejection | before release | Product/Legal | storefront checklist | revise flow |

## Exercise

Walk the path as an unhappy customer:

1. find the charge on your statement;
2. find support;
3. recover your login;
4. open subscription management;
5. cancel;
6. request a refund;
7. get a confirmation.

Any dead end in this journey is a future dispute.

## Sources

- [Stripe: how disputes work](https://docs.stripe.com/disputes/how-disputes-work)
- [Stripe: preventing disputes](https://docs.stripe.com/disputes/get-started/prevention)
- [Stripe: monitoring programs and prevention](https://docs.stripe.com/disputes/monitoring-programs)
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Google Play: billing choice program](https://support.google.com/googleplay/android-developer/answer/17161464?hl=en)
- [FTC negative-option resources](https://www.ftc.gov/legal-library/browse/rules/negative-option-rule)

## Worksheet

[Open the risk register](templates/10-risk-register.md)
