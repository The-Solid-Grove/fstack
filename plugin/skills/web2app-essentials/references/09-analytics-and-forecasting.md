# 9. Analytics, attribution, and revenue model

Connect advertising spend, funnel behavior, payments, and product use so decisions reflect the value of the customers acquired.

## Connect three views

| View | Question it answers |
| --- | --- |
| Product | Where do people continue, leave, or reach their first useful result? |
| Marketing | Which source, campaign, and creative brought those people, and what did it cost? |
| Financial | What net value does each acquisition cohort create, and when does its cash pay back the spend? |

Use stable IDs to connect the views. Campaign names are labels; raw platform IDs are the keys for matching records.

## Define events before collecting them

Use the [event dictionary](templates/08-event-dictionary.md) to record each event's trigger, producer, properties, unique ID, destination, owner, and QA example.

| Stage | Events to distinguish |
| --- | --- |
| Funnel | `funnel_started`, `screen_viewed`, `screen_completed`, `email_submitted` |
| Checkout | `paywall_viewed`, `checkout_opened`, `payment_started`, `payment_failed` |
| Purchase | `purchase_verified`, `upsell_purchased` |
| Delivery | `app_handoff_clicked`, `app_signed_in`, `entitlement_granted`, `first_value_completed` |
| Lifecycle | `subscription_renewed`, `subscription_canceled`, `refund_created`, `dispute_created` |

Keep the meanings precise:

- A view means the screen rendered; completion means a valid action finished.
- Opening checkout, attempting payment, and a verified purchase are different events. The backend confirms purchase and renewal from payment state.
- A cancellation request and the date access ends may differ. Record both. A refund and a dispute are separate events.
- Use stable event IDs, UTC timestamps, integer minor currency units plus currency, and a versioned schema. Exclude test data and deduplicate browser/server copies of the same event.
- Send personal information only where needed and permitted; keep sensitive quiz answers out of advertising events.

Link events to visitor/session and internal user IDs, funnel/version, experiment/variant, source and campaign IDs, geo/device, offer/plan/payment method, billing references, and product platform/version. Preserve relevant consent state and attribution touches.

## State the denominator

Track the path from first screen to second screen, paywall, checkout, verified purchase, sign-in, entitlement, first value, and renewal. For every conversion rate, state who is counted and over what window.

For example, deep-link attribution among installs and app sign-ins among verified buyers measure different things. They cannot be combined into one improvement claim.

## Keep attribution separate from incrementality

Maintain first-touch, last-eligible-touch, purchase-session, platform-reported, and unattributed views; include self-reported source when available. Choose the primary model and window before campaign or experiment decisions and keep them stable.

Attribution assigns credit. It does not prove that advertising caused the sale. Use a suitable holdout or geographic experiment when an incrementality decision warrants it. Web data still has consent, browser, view-through, and cross-device gaps.

## Report cohort value

At source → campaign → creative level, show spend, verified new buyers, CAC, gross and net day-0 revenue, actual cumulative net value, predicted value, prediction error, payback, activation, refunds, and disputes.

The model follows this chain:

```text
spend → clicks → buyers → plan mix → first revenue + renewals + upsells
→ refunds / disputes / fees / taxes / variable costs
→ net cohort value → cash payback and contribution
```

Separate **plan** (original assumptions), **actual** (measured results), and **forecast** (actuals plus future predictions). Keep new and repeat revenue distinct, update forecasts as cohorts mature, and backtest them. Use the definitions in [economics](03-economics.md), including payout delays for cash payback.

Daily reports find spend, event, checkout, and handoff failures. Cohort reports support retention, value, and scale decisions. A daily revenue rise does not establish better long-term economics.

## Verify one complete journey

Before traffic, walk every material branch and payment method. Check that the charged amount, currency, and product match one verified server purchase; campaign and variant IDs reach the cohort record; sign-in and entitlement resolve to the same buyer; and refund/cancel events reconcile.

Complete the [end-to-end join worksheet](templates/12-end-to-end-join.md): **ad click → funnel events → payment → app user → entitlement → first value**. Resolve missing links and test-data leakage before relying on reports. For sample size and experiment decision rules, use [experimentation](11-experimentation.md).
