# 8. App handoff: email, deep links, and entitlement

## Lesson outcome

You'll design a path where a web buyer gets app access even after losing the deep link, switching device, or waiting on a delayed payment confirmation.

## A purchase is not product access

After checkout, the user expects one thing: to start using what they paid for. But web and app live in different sessions, browsers, and identity contexts. This transition is the **[app handoff](/resources/web2app-glossary#app-handoff)**.

Four separate problems need solving:

1. **Identity:** who bought?
2. **Billing:** is the payment/subscription actually active?
3. **Entitlement:** what access should open?
4. **Handoff:** how do you get the user to their first useful action?

A deep link only helps with the last problem, and partly with attribution.

## Why deep links are not enough

In one early iOS implementation, first-click deep-link attribution survived for roughly 60% of installs. This measured attribution among installs, not the share of buyers who reached the app. It was enough to show that a deep link could improve the path, but could not be the only path to paid access.

A deep link can be lost when:

- the app is not installed yet;
- the install breaks the browser session;
- the user opens the store but comes back later;
- the universal link is configured incorrectly;
- the browser/webview changed its behavior;
- the person moved to a different device.

Don't build paid access so that a deep link firing is the only key.

## The durable bridge is account identity

Before checkout, collect a valid email and create a stable internal `user_id`. After the purchase:

1. the backend links `user_id` to the payment customer and subscription;
2. the user signs into the app with the same email or identity provider;
3. the app backend finds the entitlement by internal ID;
4. paid access opens from verified subscription state.

Even if attribution is lost, the buyer still gets the product.

Email should not be the only primary key. It works as a recovery mechanism people understand, while the internal user ID is what links systems.

## The ideal handoff uses both paths

### Fast path

- the success screen detects the platform;
- it offers `Open app` or a store button;
- the deep/universal link carries a safe handoff token or user reference;
- an installed app opens the right screen;
- a fresh install tries to restore attribution/intent after first launch.

### Recovery path

- the purchase confirmation goes out by email;
- the email contains an open/install link;
- the app offers sign-in with the purchase email;
- a resend magic link is available;
- support can find the subscription by email, internal ID, or payment customer ID.

We stopped judging delivery by deep-link attribution alone and started measuring the full path separately, from verified purchase to app sign-in to first useful action. These metrics have different denominators, so they cannot be stacked into a single before/after chart.

## The handoff screen

The success screen should show:

- payment status;
- the email/account the purchase is attached to;
- what was bought;
- the primary button for the current device;
- a QR code for moving from desktop to phone;
- App Store/Google Play links, when they are set up;
- instructions to "sign in with this email";
- a recovery/support path.

Don't put secrets, entitlement flags, or raw subscription data in the QR code or deep link. Pass an opaque identifier or a short-lived signed token, and verify state on the server.

## Paid access state

The entitlement service should answer:

- is the product/plan active?
- through what date does access run?
- is the payment processing or failed?
- is the subscription canceled with the paid period still running?
- was there a refund or a dispute?
- are there additional one-time purchases?

The app refreshes access on login, on foreground/open, and on important lifecycle events. Don't rely on a local cache alone.

## Email sequence for the ones who did not arrive

Build a separate operational sequence for paid users with no app sign-in:

1. immediately: receipt plus "continue in app";
2. a few hours later: a reminder with the same account email;
3. the next day: an explanation of the first useful action;
4. a support message if paid access is still not activated.

This is transactional/onboarding communication. Don't add marketing without the corresponding consent.

## Manage subscription

App settings and email both need a clear link to subscription management. The user should see:

- the current plan;
- the next billing date and amount;
- payment status;
- a cancel/reactivate action;
- the active-until date after cancellation;
- support contact.

Cancellation should not immediately take away access that has already been paid for, unless the offer says otherwise.

## What to measure

```text
purchase verified
→ success screen viewed
→ open/install click
→ app first open
→ sign in
→ entitlement granted
→ first useful action
```

Break it down by:

- iOS/Android/desktop purchase;
- app already installed vs new install;
- deep link vs email recovery vs manual login;
- time to sign in;
- time to first useful action;
- support contact and refund.

## Exercise

Draw three journeys:

1. the app is already installed;
2. the app is not installed;
3. the purchase happens on desktop, the product gets used on phone.

For each one, plan for the deep link being lost. If the person can still sign in and get the right access, the architecture holds up in the real world.

## Sources

- [Stripe: using webhooks with subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks)
- [Apple: supporting universal links](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)

## Worksheet

[Open the identity and entitlement map](templates/07-identity-entitlement-map.md)
