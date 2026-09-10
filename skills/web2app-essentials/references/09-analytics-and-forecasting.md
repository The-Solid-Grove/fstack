# 9. Analytics, attribution, and revenue model

## Lesson outcome

You'll build an event dictionary and one dataset that connects spend, funnel behavior, payments, and product activation.

## Three layers of analytics

### Product analytics

Shows what the user did inside the funnel and the app.

### Marketing analytics

Connects source, campaign, ad, and creative to cost and the acquired cohort.

### Financial analytics

Turns collected revenue into net cohort value, prediction, cash payback, and plan-vs-actual.

When the layers live apart, UA sees cheap purchases, product sees activation, finance sees refunds, and nobody sees the business as a whole.

## Event dictionary

The minimum set:

| Event | When it fires | Key properties |
| --- | --- | --- |
| `funnel_started` | first screen shown | funnel/version/source |
| `screen_viewed` | screen actually rendered | screen ID, branch, variant |
| `screen_completed` | valid action finished | screen ID, answer |
| `email_submitted` | identity stored | user ID, method |
| `paywall_viewed` | offer shown | paywall/offer/default plan |
| `checkout_opened` | checkout ready for action | plan, method |
| `payment_started` | user confirmed the attempt | provider intent/session |
| `payment_failed` | provider reported a failure | normalized reason |
| `purchase_verified` | backend confirmed the payment | product, price, currency, event ID |
| `upsell_purchased` | separate purchase verified | product, price |
| `app_handoff_clicked` | move to app/store | target/method |
| `app_signed_in` | account verified in the app | user ID |
| `entitlement_granted` | paid access opened | entitlement/state |
| `first_value_completed` | first useful action completed | action type |
| `subscription_renewed` | invoice paid | cycle, net value |
| `subscription_canceled` | cancellation effective/requested | reason, active until |
| `refund_created` | refund initiated | amount, reason |
| `dispute_created` | provider/network reported a dispute | amount, reason/network |

## Event rules

- `viewed` means a real render, not route intent.
- The backend creates the purchase on a verified payment state.
- Every event has a stable unique ID.
- All timestamps are stored in UTC.
- Money is stored as integer minor units plus currency.
- Test mode is separated from production.
- The event schema is versioned.
- PII is not sent to systems without necessity and permission.

## Shared dimensions

Attach or link:

- internal `user_id`;
- anonymous visitor/session ID;
- funnel ID/version;
- experiment ID/variant;
- first-touch and chosen attribution touch;
- campaign/adset/ad/creative IDs;
- geo/device/browser;
- answers/segments;
- offer/plan/coupon/payment method;
- payment customer/subscription references;
- app platform/version.

Campaign names change. Use raw platform IDs for joins and keep names as labels.

## Funnel report

Build the conversion ladder:

```text
first screen
→ second screen
→ email
→ paywall
→ checkout
→ verified purchase
→ app sign-in
→ entitlement
→ first useful action
→ renewal
```

For each rate, state the denominator and the time window. "Handoff rate" can mean the share of buyers, of clicks, or of installs. Those are three different metrics.

## Attribution

Keep several views instead of hunting for one truth:

- first touch;
- last eligible touch;
- purchase-session touch;
- platform-reported attribution;
- unattributed/direct;
- self-reported source, if you collect it.

For operational campaign decisions, pick the primary model in advance and don't change it mid-test. For incrementality, use separate geo/holdout methods when scale justifies them.

A web click gives you more first-party observations than the direct app-install path. It does not remove Safari restrictions, consent loss, view-through uncertainty, or cross-device gaps.

## The main report: spend vs cohort value

At the source → campaign → creative level, show:

- spend;
- verified new buyers;
- CAC;
- gross D0 revenue;
- net D0 revenue;
- actual cumulative net revenue;
- predicted net value;
- prediction error;
- payback status;
- app activation;
- refunds/disputes.

Update pLTV as the cohort matures. Prediction without backtesting turns into self-persuasion fast.

## Revenue model

The model runs in one direction:

```text
spend
→ clicks
→ purchases
→ plan mix
→ first revenue
→ renewals/upsells
→ refunds/disputes/fees/tax
→ net cohort value
→ payback and contribution
```

Keep three sets:

- **plan:** assumptions before launch;
- **actual:** measured data;
- **forecast:** actual to date plus updated predictions.

Show new and repeat revenue separately. Growth that requires constantly increasing new acquisition while repeat revenue stays weak has a different risk profile.

## Daily and cohort views

The daily dashboard is for anomalies:

- traffic/spend;
- event delivery;
- checkout failures;
- purchase volume;
- gross cash;
- handoff failures.

The cohort dashboard is for decisions:

- renewal;
- cancellation;
- refunds;
- disputes;
- product activation;
- actual vs predicted LTV.

Don't make long-term economics decisions from a daily revenue chart.

## Data QA

Before traffic:

1. walk through every branch;
2. make a test payment with each supported method;
3. check the server event and deduplication;
4. compare the charged amount with the event value;
5. check campaign IDs in the payment cohort;
6. wait for app sign-in and entitlement;
7. test the refund/cancel lifecycle;
8. confirm that production dashboards exclude test data.

## Example: MDE and test size

Say the baseline click-to-purchase conversion is 3.0%. The team wants to detect at least a 20% relative lift, which means a rise to 3.6%.

At two-sided alpha 5%, power 80%, and equal allocation, the approximate calculation for a difference of two proportions gives about **13,914 eligible click users per variant**. If the funnel gets 1,000 such users per day, the test takes roughly 28 days for two variants, before adjusting for data loss and day-of-week effects.

This is a planning example, not a universal threshold. Fix the baseline, the absolute and relative MDE, the unit of analysis, alpha, power, allocation, and the calculation method before launch. If the required sample is out of reach, test a larger change, or decide based on economics and the full body of evidence instead of declaring random noise a winner.

## Exercise

Create an event dictionary with owner, trigger, producer, destination, schema, and QA example. Then fill in the [end-to-end join worksheet](templates/12-end-to-end-join.md) for one test user journey and match up:

**ad click → funnel events → payment object → app user → entitlement → first value**.

If the join needs an email spreadsheet or manual lookups across several dashboards, your analytics is not ready for scale.

## Sources

- [Stripe: Events API](https://docs.stripe.com/api/events)
- [Stripe: subscription webhooks](https://docs.stripe.com/billing/subscriptions/webhooks)

## Worksheet

[Open the event dictionary](templates/08-event-dictionary.md)
