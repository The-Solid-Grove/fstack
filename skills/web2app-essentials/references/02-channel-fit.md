# 2. Is Web2Web a fit for your app?

## Lesson outcome

You'll make a decision: run a full test, do research first, or keep acquisition inside the stores for now.

Last reviewed: September 9, 2026.

## Why existing revenue isn't enough

Existing revenue shows that the product can turn some users into paying customers. It does not prove Web2Web fit.

A product can have high MRR and a weak story before install. Or a strong quiz concept but not enough LTV for paid traffic. You need product, offer, and economics fit at the same time.

## Five signs of fit

### 1. The user wants to start solving the problem now

A web funnel works better with active demand. The final result may take months, but the decision to start has to make sense today.

Examples:

- start a meal plan;
- get a language-learning plan;
- cut screen time;
- prepare for an exam;
- find the right training routine.

If the problem is felt rarely and doesn't call for action, a paid click is hard to turn into a payment without a strong additional trigger.

> **Reference funnel — [Acely](https://acely.com/welcome-sat-1a):** SAT prep has a fixed test date and a measurable target score. Inspect how the page turns that deadline into a reason to start now.

### 2. The value can be explained before install

The buyer hasn't used the app yet. They have to understand, from the creative and the web experience:

- what will change;
- why their current approach isn't working;
- what the solution includes;
- why the product is right for them specifically.

If the value only becomes clear after several product sessions, consider a web-to-app pre-sell or a low-friction trial first.

> **Reference funnel — [Bold Voice](https://start.boldvoice.com/join/name):** “Improve your American accent” is understandable before install. Inspect how the funnel moves from that concrete outcome into questions about the learner.

### 3. Answers can change the experience or the recommendation

A quiz is useful when the question affects at least one of these:

- feedback;
- branch;
- result;
- plan;
- paywall message;
- first action in the product.

If every answer leads to the same generic pitch, a long quiz only burns attention.

> **Reference funnel — [Woofz](https://woofz.academy/sex_4?cohort=woofz22_v3):** the dog's age, profile, and training needs can change the plan. Inspect which questions could materially change the recommendation rather than just the copy.

![Acely, Bold Voice, and Woofz illustrate active demand, a clear pre-install promise, and meaningful personalization.](/images/web2web-course/lesson-02-fit-signals-1.webp)

### 4. There's a clear first useful action after purchase

Payment creates an expectation of immediate progress. The user should land in the product and do something useful:

- start their first focus session;
- create their first meal plan;
- complete their first lesson;
- see their personal dashboard;
- activate their first automation.

If the user sees another long onboarding with no result after checkout, some paid users will be lost before the value moment.

Grant access from a verified server-side payment event, not only from the checkout return page, so fulfillment still works when the redirect is interrupted.

> **Reference funnel — [12min](https://onboarding.12min.com/start?lng=en):** the first useful action can be as concrete as opening the first Microbook or learning journey. Inspect whether the promise makes that post-purchase start obvious.

### 5. Retention can pay back acquisition

A low intro price can buy a good-looking CAC. It doesn't guarantee a working business.

You need data or a reasonable hypothesis on:

- renewal curve;
- cancellation rate;
- refund rate;
- payment failures;
- gross margin;
- first useful action and retention.

> **Reference funnel — [Nerva](https://assessment.nervaibs.com/):** a personalized, multi-session program gives the team a plausible reason for users to return. The funnel can show the retention hypothesis; only renewal cohorts can prove the economics.

![12min and Nerva show two different retention hypotheses: repeat learning and a personalized program delivered over time.](/images/web2web-course/lesson-02-fit-signals-2.webp)

These are third-party funnels checked on September 9, 2026. Their routes, offers, and variants can change by campaign, country, device, or date. Use them to study execution, not as evidence that their unit economics are profitable.

## Red flags

Hold off on a full launch if:

- the app hasn't confirmed willingness to pay;
- you don't know who buys and why;
- the team can't connect a web buyer to app access;
- the only idea is to copy someone else's quiz and cut the price;
- paid traffic only pays back at an unrealistic renewal rate;
- nobody owns refunds, disputes, and support;
- the funnel's promise is stronger than what the product actually delivers.

## Scorecard

Score each item from 0 to 2.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Active problem | weak | occasional | user wants to start now |
| Explainable value | clear only after use | partly clear | clear before install |
| Personalization | decorative | changes copy | changes result/offer/product start |
| First useful action | undefined | takes several steps | available right after handoff |
| Economics | no data | rough model in place | cohort retention and target CAC in place |
| Delivery | access is manual/fragile | recovery exists | identity and entitlement are reliable |
| Operations | no owner | partly covered | support/risk process ready |

- **11–14:** you can design a controlled launch.
- **7–10:** close the weak spots first, then run a small validation.
- **0–6:** Web2Web will create more complexity than growth for now.

The score doesn't predict success. It makes assumptions visible.

## Choosing a new or existing product

An existing app is a fit if you can confidently sell its current value on the web, and if it's easy to open the same subscription access after a web purchase.

Technical compatibility is only one part of the decision. The purchase and access model also has to comply with the rules of every storefront where the app is distributed.

A new product makes sense if the channel requires a different promise, pricing, or first-use experience. We took this path: a separate product let us design acquisition, funnel, and app as one system. It costs more and moves slower, but it removes inherited constraints.

Don't turn our choice into a universal recipe. An existing app may have far more evidence, retention, and brand trust.

## Build, buy, or hybrid

The decision depends on where your competitive advantage sits.

| Approach | When it fits | Main risk |
| --- | --- | --- |
| Buy | you need to test a standard flow quickly and the team doesn't want to own infrastructure | product limits may get in the way of an unusual funnel or entitlement logic |
| Build | the funnel, data model, or pricing is a core part of the product, and engineering capacity is already there | months of development before the first market signal |
| Hybrid | a ready-made funnel/payment foundation plus your own app, data, and lifecycle integrations | unclear ownership boundaries between vendor and team |

Count more than the subscription fee or development cost. Include time to first test, speed of change, QA on the payment lifecycle, support for integrations, and the cost of mistakes after scale.

## The cheapest validation test

Before a full build, put together:

1. one winning or promising creative angle;
2. a 5–10 screen clickable funnel concept;
3. a personalized result preview;
4. a real offer and pricing model;
5. a clearly disclosed interest or waitlist CTA that does not collect payment details, or a small paid test if the offer and payment flow are legally and technically ready.

The goal isn't to test production polish. It's to test the chain of **message → intent → offer**.

## Exercise

Fill in the scorecard and write one paragraph:

> For [segment] with the problem [problem], we can use [funnel mechanism] to show [personal result] and sell [offer]. After purchase, the user gets [first useful action]. The channel works if [pLTV/payback condition].

If there are still blanks in that sentence, your next step is research, not build.

## Sources

The scorecard is our operating framework, not a platform benchmark. These sources validate the platform mechanics behind its delivery, economics, measurement, and operations criteria:

### Platform rules and documentation

- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) — subscription value and disclosure requirements, access to previously purchased content, and storefront-specific external purchase rules.
- [Apple: Supporting associated domains](https://developer.apple.com/documentation/Xcode/supporting-associated-domains) — the web-and-app association required for universal links and related handoff features.
- [Google Ads: About Web to App Acquisition Measurement](https://support.google.com/google-ads/answer/16440462) — measuring installs and first in-app conversions originating from web campaigns, plus the integration requirements and coverage limits.
- [Google Ads: About conversion values](https://support.google.com/google-ads/answer/13064207?hl=en) — optimizing and reporting against the value of conversions rather than conversion count alone.
- [Apple: Sales and Trends metrics and dimensions](https://developer.apple.com/help/app-store-connect/reference/reporting/sales-and-trends-metrics-and-dimensions/) — definitions for paid subscriptions, renewals, refunds, sales, and developer proceeds.
- [Stripe: Fulfill orders](https://docs.stripe.com/checkout/fulfillment) — server-side fulfillment through webhooks instead of relying only on a checkout success-page redirect.
- [Stripe: How subscriptions work](https://docs.stripe.com/billing/subscriptions/overview) — the subscription lifecycle, payment state, webhooks, and automated revenue recovery.
- [Stripe: Dispute and fraud card monitoring programs](https://docs.stripe.com/disputes/monitoring-programs) — the operational consequences of excessive disputes and the need to monitor payment health.
- [FTC: Advertising substantiation](https://www.ftc.gov/legal-library/browse/ftc-policy-statement-regarding-advertising-substantiation) — the requirement for a reasonable basis behind objective advertising claims.
- [Google Ads: Unavailable offers](https://support.google.com/adspolicy/answer/15937063?hl=en-GB) — the prohibition on advertising offers that users cannot actually obtain.
- [Google Play Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en) — Android billing and external purchase rules that affect the purchase-and-access model.

### Industry guides and datasets

These are vendor-published sources, so we use them for implementation patterns and aggregate context rather than as universal performance promises.

- [RevenueCat: Web-to-app funnels—the complete 2026 guide](https://www.revenuecat.com/blog/growth/web-to-app-funnels) — discusses which products may fit the channel, the trade-offs to test, and why category alone does not determine fit.
- [RevenueCat: State of Subscription Apps 2026](https://www.revenuecat.com/state-of-subscription-apps) — an aggregated dataset covering more than 115,000 subscription apps, $16 billion in revenue, and over one billion transactions across iOS, Android, and web; useful as market context, not as a Web2Web-specific benchmark.
- [AppsFlyer: Unlock the value of web-to-app](https://www.appsflyer.com/blog/measurement-analytics/web-to-app-guide/) — describes measurement gaps, handoff friction, and the need to evaluate web and app performance as one journey.

## Worksheet

[Open the channel-fit scorecard](templates/01-channel-fit-scorecard.md)
