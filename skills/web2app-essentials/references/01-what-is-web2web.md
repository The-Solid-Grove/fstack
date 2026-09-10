# 1. What Web2Web is and why we chose this channel

## Lesson outcome

You'll be able to tell Web2Web apart from ordinary app acquisition, and to see which part of the growth comes from the funnel itself and which comes from the new acquisition-and-sales system.

Last reviewed: September 10, 2026.

## Ways to sell a subscription app

| Model | Path | Purchase | Who controls billing |
| --- | --- | --- | --- |
| Native app purchase | Ad → store → install → app onboarding | In the app | App Store / Google Play |
| Web pre-sell → app purchase | Ad → web pre-sell → store → install → app paywall | In the app | App Store / Google Play |
| Web2Web for an app | Ad → web funnel → web checkout → app | On the web | App company / payment partner |
| Web product | Ad → web funnel → web checkout → browser product | On the web | Web company / payment partner |

In this course, **[Web2Web](/resources/web2app-glossary#web2web)** means the ad click and the purchase both happen on the web. After the purchase, the user can install or open the app and get paid access there.

Whether the app may surface an external purchase path, and whether the same offer must also use store billing, depends on the app category, storefront, and program. Check the current Apple and Google rules for every market before launch.

The name is easy to misread. The product does not have to be browser-only. "Web2Web" describes the acquisition and transaction layer, not the place where the user gets all of the value. The market, and our own earlier materials, often call this same path **web-to-app with web checkout**. Industry terminology is not standardized: [RevenueCat's 2026 guide](https://www.revenuecat.com/blog/growth/web-to-app-funnels) uses web-to-app as the umbrella term and calls the pay-on-web-before-download version "web-to-web." Inside this course we use one name: Web2Web.

## Live Web2Web funnels to study

The fastest way to understand the model is to walk through several live funnels in different categories. Each one starts with a concrete promise, collects context on the web, builds value before showing the price, and sells access through a web checkout.

![Opening screens from Headway, Promova, and Fastic show how Web2Web funnels adapt the same model to self-growth, language learning, and fasting.](/images/web2web-course/lesson-01-live-funnel-examples.webp)

| Product | Industry | Live funnel | What to inspect |
| --- | --- | --- | --- |
| Headway | Self-growth / book summaries | [Open funnel](https://onboarding.makeheadway.com/) | How the first screen continues the ad promise and makes the first tap easy. |
| Promova | Language learning | [Open funnel](https://english-improve.com/) | How diagnostic questions and a projected future state make the offer feel personal. |
| Fastic | Fasting / weight loss | [Open funnel](https://web.fastic.com/) | How goal segmentation starts a long personalized journey. |
| PawChamp | Dog training | [Open funnel](https://paw-champ.com/) | How the dog's name and the owner's answers carry through the funnel. |
| Hint | Astrology / palmistry | [Open funnel](https://try.hint.app/) | How a palm scan becomes the product mechanism and gates the personalized result. |
| Stylix | Personal style | [Open funnel](https://sub.stylix.app/) | How a visual identity hook leads into color and wardrobe personalization. |

We checked these links on September 9, 2026. They are third-party funnels, so the route, offer, or variant you see can change by campaign, country, device, or date. A live funnel is useful evidence of execution, not proof that its unit economics are profitable.

## Proof it works at scale

Web revenue is already part of large subscription businesses. [RevenueCat's State of Subscription Apps 2026](https://www.revenuecat.com/state-of-subscription-apps-2026/), based primarily on 2025 data, reports web revenue in 41% of its highest revenue tier, versus 1.3% of its lowest. The report's overall dataset covers more than 115,000 apps and $16B in revenue. That shows adoption among larger businesses; it does not prove that adding a quiz caused their growth, and web revenue can come through several purchase paths.

[FunnelFox's 2026 report](https://funnelfox.com/state-of-web2app/) reports 82% web-funnel adoption among the top-grossing apps it analyzed and roughly 90% of subscription revenue from web among its funnel scalers. Those are separate populations. The report draws on ad-library analysis, partner intelligence, and platform data, without a disclosed sample size. It is vendor evidence of the channel's scale, not an audited market census or an expected result for a new entrant.

These reports answer whether established businesses use the channel. Your own cohort economics must answer whether it works profitably for your product. The figures are not directly comparable because their definitions and populations differ.

## Why we looked for a different model

Over three years we built more than 50 mobile apps. The portfolio is still profitable; its main acquisition channel was ASO, supported by Google Ads and TikTok marketing.

The apps were profitable, but further growth kept getting harder. Competition in the App Store increased, and organic demand was difficult to grow predictably.

We did not move an old app onto web payments. We built a new product together with a separate web funnel and paid acquisition system. By June 2026 it reached $2.5M annualized gross revenue, calculated as monthly revenue × 12 before fees and refunds. That is the result of the team's product, not FunnelsGrove revenue, and the specific causality cannot be attributed to a single screen or funnel change. The organic portfolio kept running in parallel.

My role covered product development, the funnel, and the whole technical side, working alongside UA and testing growth hypotheses. That is why the main takeaway from this experience is about the entire system, not one screen that happened to work.

## What changes in Web2Web

### 1. Acquisition changes

Native app campaigns can optimize for installs, selected in-app actions, or reported conversion value. On the web, you can instrument the funnel and checkout directly and send browser and server events. That usually gives a clearer view of the pre-purchase journey for campaign optimization and cohort analysis.

Complete attribution still does not exist. Browser privacy controls, consent choices, cross-device journeys, and ad platform limits all cause signal loss. The advantage of the web is more observable events and more control, not a magical 100% of the data.

### 2. The way you sell changes

App onboarding usually explains the interface and walks the user to the native paywall. A web funnel has to sell the solution to someone who has not installed the product yet. It continues the promise from the creative, helps the person understand their own situation better, shows a possible path, and only then presents the offer.

### 3. The economics change

A quoted web-processing rate can be below a store commission, but it is not the total cost. Compare processor and payment-method fees, currency conversion, fraud, disputes, tax operations, billing tools, and any applicable store-program fees.

The cash cycle changes too. Apple states that proceeds are paid within 45 days after the end of the fiscal month. Stripe supports daily payouts for some accounts, but settlement timing varies by country and account. A shorter payout cycle can let you put money back into acquisition sooner.

### 4. Responsibility changes

On the web, the team or its chosen provider must handle what the store used to handle:

- checkout and payment failures;
- subscription lifecycle;
- refunds and chargebacks;
- taxes;
- customer support;
- consent and billing disclosures;
- linking the web purchase to the app account.

Part of the apparent cost difference comes from moving work and risk to your team or provider.

## Why the funnel cannot be judged on its own

The simplified chain looks like this:

**Creative → first screen → funnel → email → paywall → checkout → purchase → app access → first useful action → renewal**

![Three Headway screens illustrate the job of a Web2Web funnel: continue the promise, capture intent, and present a paid offer.](/images/web2web-course/lesson-01-funnel-sequence.webp)

Each block affects the next one. The creative changes traffic quality. Price changes who buys. Checkout can lift first-purchase conversion and still bring in weaker cohorts. The app handoff may not affect purchase rate at all, yet still break activation and retention.

That is why the question "what is the funnel's conversion rate?" is almost always too narrow. The right question is: **which cohort did we get, what did it cost, and how much net value does it create over time?**

## When the advantage becomes real

Web2Web works when a team can do all of the following at the same time:

1. buy the right traffic;
2. keep the promise consistent between creative and funnel;
3. build enough perceived value before the paywall;
4. show clear recurring terms;
5. take the payment with minimal friction;
6. open paid access reliably;
7. measure cohort revenue after refunds and fees;
8. ship the next round of experiments.

If one of these parts is missing, the funnel can show attractive purchase numbers and still lose money.

## Exercise

Map your customer's current path from ad click to first useful action. For each transition, note:

- where the event happens: ad platform, web, store, or app;
- which ID links it to the previous step;
- which team owns the transition;
- which event proves the transition happened.

The blank spots will show the real difficulty of moving to Web2Web better than any funnel builder's feature list.

## Sources

### Platform rules and documentation

- [Apple: Measuring ad performance with AdAttributionKit](https://developer.apple.com/app-store/ad-attribution/) — privacy-preserving app-install attribution, conversion windows, postbacks, and conditional campaign data.
- [Google Ads: About bidding in App campaigns](https://support.google.com/google-ads/answer/7100895?hl=en) — optimization for installs, selected in-app actions, and conversion value.
- [Google Ads: Add a Google tag to your website](https://support.google.com/google-ads/answer/6331314?hl=en) and [Meta: Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/) — browser and server-side web conversion instrumentation.
- [Google Play Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en) — when Play Billing is required and which external purchase paths are available.
- [Apple: Auto-renewable subscriptions](https://developer.apple.com/app-store/subscriptions/) — App Store subscription proceeds and the Small Business Program rate.
- [Google Play: Service fees](https://support.google.com/googleplay/android-developer/answer/112622?hl=en) — Google Play fee tiers and programs.
- [Stripe: Pricing](https://stripe.com/pricing) — published web payment-processing fees; actual pricing varies by country, payment method, currency, and product.
- [Apple: Overview of receiving payments](https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments/) — App Store payment timing and fiscal-month reporting.
- [Stripe: Payouts](https://docs.stripe.com/payouts) — payout schedules, settlement timing, and country/account-dependent availability.
- [Stripe: How subscriptions work](https://docs.stripe.com/billing/subscriptions/overview) — the recurring-payment lifecycle, invoices, PaymentIntents, webhooks, and recovery responsibilities.
- [Stripe: Dispute and fraud card monitoring programs](https://docs.stripe.com/disputes/monitoring-programs) — dispute-rate monitoring, network programs, fees, and the risk of losing card-processing access.
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) — current rules for in-app purchases, subscriptions, previously purchased access, and external purchase paths by storefront.
- [FTC: Negative options—make them a positive](https://www.ftc.gov/business-guidance/blog/2016/09/negative-options-make-them-positive) — the US baseline for clear recurring terms, informed consent, and simple cancellation; other jurisdictions require separate review.

### Industry guides and datasets

Web2Web is practitioner terminology rather than a formal platform standard. The following sources come from subscription infrastructure and mobile measurement companies. They are useful for terminology, implementation patterns, and aggregate market observations, but each publisher has a commercial interest in the category.

- [RevenueCat: Web-to-app funnels—the complete 2026 guide](https://www.revenuecat.com/blog/growth/web-to-app-funnels) — explicitly distinguishes the web-payment-before-download path as web-to-web and covers its setup, trade-offs, offer design, and operational complexity.
- [RevenueCat Funnels documentation](https://www.revenuecat.com/docs/tools/funnels) — a concrete implementation model combining multi-step web acquisition, branching, authentication, web checkout, attribution parameters, and analytics events.
- [AppsFlyer: Unlock the value of web-to-app](https://www.appsflyer.com/blog/measurement-analytics/web-to-app-guide/) — a guide to cross-channel measurement, deep linking, attribution parameters, and post-install activity from web campaigns.
- [Adjust: Web-to-app](https://www.help.adjust.com/en/article/web-to-app) — technical guidance on preserving campaign data, attribution signals, and user context between a browser, an app store, and an app.

## Worksheet

[Open the channel-fit scorecard](templates/01-channel-fit-scorecard.md)
