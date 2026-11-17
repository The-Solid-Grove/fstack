# 12. Payments risk, support, and compliance

Web billing brings responsibility for payment failures, subscription changes, refunds, disputes, taxes, privacy, and customer support. Set up these basics before accepting real payments.

## Distinguish the payment outcomes

| Outcome | Meaning | Response |
| --- | --- | --- |
| Failed payment | Money was not collected. | Check the reason; use a supported retry or request customer action. |
| Refund | The merchant returns a collected payment. | Reconcile the amount, billing state, access, and customer confirmation. |
| Dispute / chargeback | The cardholder challenges a payment through the bank. | Follow the provider's process; track the disputed amount and fees separately. |

Disputes can follow fraud, an unrecognized charge, unexpected renewal, or difficulty canceling. Treat support and billing clarity as prevention.

## Recover renewals consistently

Separate retryable failures from cases requiring an updated payment method or other customer action. Define the provider-supported retry policy, stop condition, grace period, entitlement state, and messages.

Reconcile invoice/payment state before another attempt so retries do not duplicate charges. A failure does not authorize a different amount or an unrelated saved card. Measure recovered net revenue together with complaints, duplicate payments, and access errors.

## Make billing and recovery understandable

Before payment, show:

- What access is included and whether the offer recurs.
- Today's charge, billing period, renewal amount, and trial/intro conditions.
- How to cancel, obtain support, and request a refund.
- Applicable Terms and Privacy information.

Keep required consent evidence. An upsell needs separate authorization. Send a receipt, use a recognizable statement descriptor, and confirm cancellation with the paid-through date where applicable.

Provide a straightforward subscription-management path showing plan, renewal, payment status, and cancellation. Optional retention offers must preserve a clear cancellation path and follow applicable rules.

Support should be able to find a customer through an internal or payment ID or verified contact details, inspect billing state, restore access, and handle cancellation/refund requests. Assign owners and response targets; record structured reasons so recurring problems reach the product backlog.

## Monitor risk using the right definitions

Track payment acceptance, failures, refunds, disputes, fraud signals, support response, paid-without-access cases, billing-email delivery, and payout holds or reserves. Break problems down by cohort, offer, source, geo, and provider where useful.

Use each network/provider's current rate formula and action thresholds. Account for the delay between payment and dispute. A prevention service may resolve some disputes early, often through refunds; evaluate coverage, prevented cases, false matches, cost, and effect on the relevant program metrics.

## Check each market and offer

In the [risk register](templates/10-risk-register.md), record applicable requirements, owner, review date, and evidence for:

| Area | What needs a current decision |
| --- | --- |
| Subscription terms | Disclosures, affirmative consent, trial/renewal reminders, cancellation channels, and refund obligations. |
| App distribution | Storefront, category, and program rules for web purchases, links, billing, reporting, and fees. |
| Privacy | Necessary data, purpose, storage, retention, access, consent, and deletion. |
| Taxes and merchant model | Selling markets, product classification, registration/reporting, invoices, and responsibility for collection. |

Rules differ across jurisdictions and change over time. Verify the actual markets and offer before launch and whenever either changes. General guidance is not a substitute for that review; preserve the supporting evidence in the project's register rather than treating an old course threshold as current.

Collect only useful funnel answers. Keep sensitive raw answers out of advertising systems, restrict access, and consider whether less sensitive data can answer the same question.

With a **payment service provider (PSP)**, the business usually remains the merchant and owns tax and related obligations. A **Merchant of Record (MoR)** takes on more responsibilities, with trade-offs in fees, checkout control, and customer relationships. Confirm the actual contract; compare the whole operating model.

## Test the unhappy path

Complete the register with **risk → signal → action level → owner → prevention → recovery → review cadence**. Include payment failure, unrecognized charge, renewal surprise, lost access, fraud, policy mismatch, and privacy incidents.

Then act as a customer: identify a charge, find support, recover login, inspect the subscription, cancel, request a refund, and receive confirmation. Verify that billing and access states remain correct throughout.

**Output:** a current market/offer checklist, an owned risk register, and tested billing, support, and access-recovery paths.
