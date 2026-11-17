# 4. The whole system: from click to paid access

Map acquisition, payment, identity, access, and measurement as one journey:

```text
Ad → funnel → paywall → checkout → optional upsell
→ open/install product → sign in → paid access → first useful action
→ renewal / cancellation / recovery
```

Place email or account capture where the product needs it. The user sees a sequence; the underlying systems update independently.

## Keep five layers distinct

| Layer | Responsibility |
| --- | --- |
| Acquisition | Landing URL, UTMs, click/campaign/creative IDs, first and last eligible touch, consent state. Capture on the first server request where possible. |
| Funnel | Anonymous `visitor_id`, answers, experiment assignments, and their link to a stable `user_id` when identity is established. Email is changeable, not a primary key. |
| Billing | Backend links among the internal buyer, provider customer, checkout/payment, subscription, offer, invoices, refunds, and disputes. |
| Product | Authentication identifies the user; entitlement determines current access. Neither depends on successful attribution or a deep link. |
| Analytics | Stable visitor/user and event IDs, timestamps, funnel/version, variants, source, offer/plan/payment method, country, device, and browser. |

A lost click ID can affect attribution without changing paid access. A success URL or app-opening link is not proof of payment.

## Make the server authoritative

1. Create checkout on the backend for a known internal buyer and payment customer.
2. Let the customer authorize payment.
3. Verify the provider's signed webhook and process it idempotently.
4. Store billing state and derive entitlement from that verified state.
5. Send deduplicated server purchase events to analytics and the ad platform.
6. Show the verified status and access handoff in the browser.

This flow must work after browser closure, duplicate delivery, delayed payment, or a later subscription change.

## Define lifecycle states

Distinguish checkout created, payment processing, trialing, active, past due, canceled with access through period end, expired/unpaid, refunded, and disputed. A single `is_paid` flag cannot express these differences.

For each state, specify entitlement, visible status, service messages, analytics events, retry/reactivation behavior, and support ownership. Canceling renewal can leave the current paid period active.

## Design recovery and ownership

Cover these failures alongside the happy path:

- Closed checkout, unavailable wallet, failed or delayed payment, duplicate webhooks or purchases.
- Mistyped email, different sign-in identity, or lost session/answers.
- Existing installation, fresh installation, or a lost deep link.
- Failed renewal, refund/dispute, or cancellation with remaining access.

Assign owners for click capture, funnel state, payment, entitlement, handoff, lifecycle support, and measurement. Paid access and subscription management must remain recoverable when the normal redirect fails.

## Exercise

Draw the happy path and relevant failure paths. For each event record its source of truth, identity, idempotency key, retry behavior, visible state, analytics event, and owner. Confirm that one authoritative payment record can be traced to the correct entitlement and first useful action.

## Worksheet

[Open the identity and entitlement map](templates/07-identity-entitlement-map.md)
