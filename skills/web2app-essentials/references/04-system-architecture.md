# 4. The whole system: from click to paid access

## Lesson outcome

You'll create a system map that connects advertising, funnel, payment, identity, app access, and analytics.

## Reference flow

```text
Ad
→ web funnel
→ email capture
→ paywall
→ checkout
→ optional upsell
→ install or open app
→ sign in
→ paid access
→ first useful action
→ renewal / cancellation / recovery
```

This flow only looks linear to the user. Inside, several systems run at once.

## Five independent layers

### 1. Acquisition identity

Stores where the visit came from:

- landing URL;
- UTMs;
- ad-platform click IDs;
- first touch and last eligible touch;
- creative/campaign/ad IDs;
- consent state.

Save these parameters on the first server request where possible. Browser scripts may fail to run or lose query parameters.

### 2. Funnel identity

Create an anonymous `visitor_id` on the first visit. After email capture, link it to a permanent `user_id`. All answers, experiment assignments, and events must keep belonging to the same person.

Don't use email as the only database key: email can be changed, mistyped, or arrive through different identity providers.

### 3. Billing identity

Links together:

- internal `user_id`;
- payment-provider customer ID;
- checkout/payment intent;
- subscription ID;
- product/price/offer;
- invoice and refund/dispute objects.

This link is created on the backend. A frontend success page is not proof of payment.

### 4. Product identity and entitlement

Authentication answers: **who is the user?**

Entitlement answers: **which paid value do they have access to right now?**

Attribution answers: **where did they come from?**

Don't merge these three jobs. A lost click ID must not shut off paid access. A deep link that fired must not, by itself, prove an active subscription.

### 5. Analytics identity

Every event gets stable IDs and properties:

- `user_id`;
- `funnel_id` and `funnel_version`;
- experiment variants;
- source/campaign/creative IDs;
- offer/plan/payment method;
- country, device, browser;
- event timestamp and event ID for deduplication.

## Server-authoritative purchase flow

The reliable sequence:

1. the frontend requests a checkout session for a known `user_id`;
2. the backend creates or finds the payment customer;
3. the user confirms payment;
4. the payment provider sends a signed webhook;
5. the backend verifies the webhook, makes processing idempotent, and stores billing state;
6. entitlement is updated from verified state;
7. a server-side purchase event goes to analytics and the ad platform;
8. the success page shows status and handoff, but does not create a trusted purchase on its own.

This protects you from refreshes, duplicate webhooks, forged success URLs, and asynchronous payment methods.

Stripe recommends tracking subscription activity through webhooks. The practical reason is broader: the browser can close, and a recurring payment can change state months after the first checkout.

## Subscription state machine

At minimum, distinguish:

- checkout created;
- payment processing;
- active;
- trialing;
- past due;
- canceled but active until period end;
- expired/unpaid;
- refunded;
- disputed.

Don't collapse all of this into a boolean `is_paid`. A user can cancel renewal, for example, and still keep access until the end of the paid period.

For each state, define:

- whether entitlement exists;
- what the user sees;
- which email they receive;
- what is sent to analytics;
- whether retry/reactivate is possible;
- who owns the support case.

## Failure paths to design up front

The happy path covers only some of your users. Map these too:

- checkout closed without payment;
- wallet unavailable;
- payment processing takes longer than a few seconds;
- webhook delayed or delivered twice;
- email entered incorrectly;
- app already installed;
- app installed after the deep link was lost;
- user signed in with a different email;
- renewal failed;
- user requested a refund;
- subscription canceled but access still valid;
- user purchased a second time.

Our main production lesson: you can't design the conversion path separately from the recovery and service paths. A person has to get their paid access and manage their subscription even when the redirect, the deep link, or the ordinary happy path didn't work.

## Ownership map

| Area | Primary owner | Check |
| --- | --- | --- |
| Click capture | UA + engineering | IDs survive until purchase |
| Funnel state | Product/growth | answers and variants aren't lost |
| Payment | Backend/payments | a verified webhook creates billing state |
| Entitlement | Backend + app | the app grants the right access |
| Handoff | Growth + app | the buyer reaches first useful action |
| Lifecycle | Payments/support | renewal, cancel, refund work |
| Measurement | Analytics | spend is connected to net cohort value |

## Exercise

Draw a sequence diagram for the happy path and at least eight failure paths. For each event, specify:

- the source of truth;
- the idempotency key;
- the user ID;
- retry behavior;
- the user-facing state;
- the analytics event.

If your team can't name a single source of truth for `purchase` and `paid access`, it's too early to send traffic.

## Sources

- [Stripe: using webhooks with subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks)
- [Stripe: payment status updates](https://docs.stripe.com/payments/payment-intents/verifying-status)

## Worksheet

[Open the identity and entitlement map](templates/07-identity-entitlement-map.md)
