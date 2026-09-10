# 7. Paywall, checkout, and upsells

## Lesson outcome

You'll design a payment sequence that turns accumulated desire into a clear offer, removes payment friction, and doesn't hide recurring terms.

## The paywall continues the funnel

The paywall shouldn't be the first place you explain the product. It gathers value that has already been loaded into a single decision.

At this moment the user has four questions:

1. Is this actually for my situation?
2. What exactly do I get?
3. How much do I pay today, and later?
4. What happens after I pay?

If the funnel promised a personal result, the paywall has to repeat it. If the quiz identified a goal, plan duration, or barrier, the offer should show how that shaped the recommendation.

## Three conversion mechanics worth testing

### 1. A real discount with a countdown

A timer keeps the offer in short-term memory and adds urgency. It only works if the mechanics are honest:

- the discount exists;
- the end time survives a refresh;
- the offer changes once it expires;
- checkout gets the same price the paywall showed.

In one production funnel we built a staged offer state: the initial timed discount persisted, and closing checkout could open a separate recovery offer. This is harder than a visual timer: it needs persistent timestamps, consistent price logic, and protection against a flash of the wrong price.

### 2. Money-back guarantee

A guarantee reduces perceived risk if it:

- actually applies;
- states the window and the conditions;
- has a simple request path;
- is backed by a support process.

Don't write "no questions asked" if the team then demands lengthy proof or hides the contact channel.

### 3. Inline Apple Pay / Google Pay

A wallet button next to the selected plan shortens the gap between the decision and the payment. Show only a method that is genuinely available, and keep a clear card fallback.

Wallet availability depends on device, browser, domain, and payment configuration. A disabled shell shouldn't look like a working button.

A card payment may require 3-D Secure or another form of Strong Customer Authentication. Design the challenge, return URL, processing, and failure states. Don't treat the redirect after a challenge as confirmation of payment before server verification.

## Pricing architecture

It usually makes sense to start with 2–3 options so you can test:

- plan duration;
- default selection;
- order;
- first-period price;
- renewal price;
- price framing per day/week/month;
- intro offer vs regular subscription.

The default plan is a product recommendation, not a decorative badge. Explain why that duration matches the outcome.

Show these together:

- amount charged today;
- billing period;
- next charge amount and date/condition;
- auto-renewal;
- cancellation path.

The smallest number on the screen shouldn't create a false impression of the real charge.

## Intro offers and trials

A cheap entry point raises first-purchase conversion but changes buyer quality. The bigger the gap between the initial and the renewal price, the higher the risk of cancellation, failed rebill, refund, and dispute.

Our $1 weekly-trial test produced a lot of Meta purchases but weak renewal afterwards. It became a good example of why you can't judge an offer by the CPA of the first payment. The economics of that experience are covered in [the lesson on CAC, pLTV, and cash payback](03-economics.md).

For every intro offer, model these in advance:

- conversion to first payment;
- first renewal success;
- voluntary cancellation;
- insufficient-funds failures;
- refund/dispute rate;
- D0/D30/D365 net ROAS.

## Checkout

A minimal checkout has:

- one clear action;
- a suitable wallet as the fast path;
- a card fallback;
- as few required fields as possible;
- mobile/in-app-browser compatibility;
- visible support and secure-payment context;
- an exact match with the selected plan;
- handling for processing, failure, cancel, and retry.

Don't send the user to a success state from a frontend callback before server verification.

## Checkout-close recovery

Someone who opened checkout and closed it is different from a random visitor. You can test one recovery step:

- explain a term that wasn't clear;
- offer a different plan;
- show a legitimate additional discount;
- return them to the selected plan without losing state.

A recovery offer can cannibalize full-price sales if it appears too early or to everyone. Keep a holdout group with no offer and measure separately:

- recovered purchases;
- how many control users came back and bought without a discount;
- changes in AOV, refunds, and pLTV.

## Follow up with people who have not purchased

Unpaid checkout recovery is different from helping a paid customer get access. If the person supplied an email and the required permission, a short follow-up sequence can return them to a useful result, clarify the offer, or address a specific objection. Use the actual goal or drop-off point without exposing sensitive quiz answers.

Define eligibility, trigger, timing, message purpose, offer, and sequence end. Before every send, suppress people who purchased, unsubscribed, or otherwise became ineligible. Keep unsubscribe available and keep service-delivery communication separate from marketing where required. A reminder must not claim a result or discount that is no longer available.

Test the sequence against an eligible no-send holdout. Measure incremental net revenue after discounts and refunds, alongside complaints and opt-outs. Revenue attributed to recovery messages does not prove that those sales would otherwise have been lost. Start with a timing hypothesis suited to the product instead of treating another funnel's schedule or claimed uplift as a benchmark.

[FunnelFox's email recovery guide](https://blog.funnelfox.com/retargeting-emails-in-web2app/) illustrates the sequence pattern; it is vendor guidance, not a causal estimate of email-only impact.

## Post-purchase upsell

An upsell appears after the main purchase is confirmed and solves an adjacent problem. It should:

- follow logically from the creative/funnel theme;
- state clearly whether the payment is one-time or recurring;
- have its own explicit authorization;
- not disguise itself as a confirmation button;
- not block access to the product already purchased.

In our actual implementation we separated the subscription purchase and the one-click one-time offer into different product types and server-verified events. That matters for analytics, refunds, and support.

## What to measure

- paywall view → checkout open;
- checkout open → purchase;
- method availability and method share;
- failure rate and reason;
- plan mix;
- first payment value;
- upsell take rate;
- first renewal;
- cancel/refund/dispute by offer;
- ARPU and pLTV, not just conversion.

## Exercise

Write a paywall spec:

1. personalized result headline;
2. result/plan preview;
3. pricing options and a deliberate default;
4. exact today/renewal disclosure;
5. wallet and card flow;
6. guarantee;
7. support/cancel/refund links;
8. checkout-close behavior;
9. optional upsell with separate consent;
10. events for every state.

Then run a test: show the screen to someone with no context for five seconds. They should correctly state the amount charged today, the renewal, and what they get.

## Sources

- [Stripe: payment status updates](https://docs.stripe.com/payments/payment-intents/verifying-status)
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

## Worksheet

[Open the paywall and checkout spec](templates/06-paywall-checkout-spec.md)
