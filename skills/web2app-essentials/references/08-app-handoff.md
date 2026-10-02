# 8. App handoff: email, deep links, and entitlement

The **[app handoff](/resources/web2app-glossary#app-handoff)** connects a verified web purchase to the first useful product action, even after a lost link, device change, or delayed payment.

## Identity is the durable bridge

Keep four questions separate:

- **Identity:** who bought?
- **Billing:** what payment or subscription state is verified?
- **Entitlement:** what access does that state grant?
- **Handoff:** how does the person enter the product?

Link checkout to a stable internal buyer ID, the payment customer, and the purchased subscription or product. After sign-in, the backend resolves entitlement through that identity. Email supports sign-in and recovery; it is not the sole database key.

Deep links help navigation and attribution. Installation, changed browsers, delayed returns, configuration errors, or another device can break them. Paid access must still work through authenticated account recovery.

## Provide fast and recovery paths

| Path | Required behavior |
| --- | --- |
| Fast | Offer the appropriate open-app or store action. Open the relevant screen for installed apps; restore intent after installation where supported. |
| Recovery | Send purchase/access instructions, provide sign-in using the purchase identity and a working resend path, and let support locate the purchase by account or payment identifiers. |

On the handoff screen show verified payment status, purchased plan, attached account/email, the device-appropriate action, supported store links or a desktop-to-phone QR code, and recovery instructions.

Links and QR codes should carry an opaque identifier or short-lived signed token, not secrets, raw subscription data, or entitlement flags. Verify identity and billing state on the server.

## Keep access and subscription state clear

The entitlement service should report current products, access end dates, processing/failed payments, cancellation with remaining access, refunds/disputes, and one-time purchases. Refresh from the server on sign-in, foreground/open, and important lifecycle changes; a local cache alone is insufficient.

Subscription management should show the plan, next billing date and amount, payment status, supported cancel/reactivate actions, access end date after cancellation, and support. Honor access through the disclosed paid-through date.

For paid customers who have not signed in, plan receipt/access instructions, a reminder, first-use guidance, and support follow-up. Choose timing for the product and stop the sequence when its purpose is fulfilled. Keep service delivery separate from marketing permission. This is a different audience from unpaid checkout recovery.

## Measure delivery separately from attribution

```text
Verified purchase → handoff screen → open/install action
→ first app open → sign-in → entitlement granted → first useful action
```

Report buyer activation using verified buyers as the denominator; label individual transition rates separately. Deep-link attribution among installs uses a different denominator and is not buyer activation.

Break results down by purchase device, existing versus new installation, and deep link versus email recovery versus manual sign-in. Measure time to sign-in and first useful action, support contacts, and refunds.

## Exercise

Map journeys for an installed app, a fresh installation, and desktop purchase followed by phone use. In each, lose the deep link and delay payment confirmation. Verify that the correct buyer can recover access without another purchase.

## Worksheet

[Open the identity and entitlement map](templates/07-identity-entitlement-map.md)
