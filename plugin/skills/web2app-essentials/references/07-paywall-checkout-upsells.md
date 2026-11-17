# 7. Paywall, checkout, and upsells

Turn demonstrated value into an informed purchase decision. The paywall should answer: does this fit, what is included, what is charged now and later, and how does access begin?

## Offer and pricing

Reflect the answers that genuinely shaped the recommendation. Test supported plan durations, ordering, defaults, introductory prices, and price framing. Explain a recommended plan's fit.

Keep these together before purchase:

- Included access and the actual initial charge and covered period.
- Renewal amount, timing/condition, and automatic-renewal terms.
- Trial or introductory terms, if offered.
- Cancellation, support, and applicable refund information.
- What happens immediately after payment.

Per-day or per-week equivalents remain secondary to billed totals. Judge introductory offers by renewal, cancellation, failed collection, refunds/disputes, and net value over time—not first-payment conversion alone. Use the [economics model](03-economics.md) for D0 actuals and later realized or forecast ROAS.

## Optional mechanics

| Mechanic | Conditions |
| --- | --- |
| Timed discount | A real discount, persistent expiry, a changed offer after expiry, and the same price in checkout. |
| Money-back guarantee | A real policy with a clear window, conditions, request path, and support process. |
| Wallet payment | Show only available methods and provide a supported fallback. Availability depends on device, browser, domain, and configuration. |

Treat these as experiments, not required paywall sections or guaranteed conversion improvements.

## Checkout and recovery

Use one clear action, necessary fields only, mobile/in-app-browser support, and an exact match to the selected plan. Handle authentication challenges, returns, processing, failure, cancellation, and retries. Verify payment on the server before showing a successful purchase; a browser callback or redirect is insufficient.

After checkout closes, a recovery step can clarify terms, offer another plan or a genuine discount, or restore the selected plan. Preserve the ability to decline. Use a no-offer holdout to distinguish incremental purchases from customers who would have returned at full price. Compare net revenue, order value, refunds, and pLTV.

### Unpaid follow-up

Email recovery is separate from helping a paid customer obtain access. For eligible people with the required permission, define the trigger, timing, useful message, offer, and stopping condition. Use the actual goal or drop-off point without exposing sensitive answers.

Before each send, exclude purchasers, unsubscribed recipients, and anyone otherwise ineligible. Keep unsubscribe available, distinguish marketing from service delivery, and reference only results or offers that remain available.

Test against an eligible no-send holdout. Measure incremental net revenue after discounts/refunds, complaints, and opt-outs; attributed sales alone do not prove recovery. Choose timing for the product.

[FunnelFox's email recovery guide](https://blog.funnelfox.com/retargeting-emails-in-web2app/) offers a useful sequence example; its vendor guidance is not a causal estimate of email impact.

## Post-purchase upsell

Offer an adjacent benefit only after the main purchase is verified. State its separate price and whether it recurs, obtain explicit authorization, and allow an easy decline with access to the original purchase intact.

Keep subscription and one-time purchases distinct in billing, verified events, refunds, and support. A saved payment method is not authorization for another charge.

## Measurement and exercise

Track paywall-to-checkout and checkout-to-purchase rates with their respective stage denominators. Also track method availability/share, failure reasons, plan mix, first-payment value, upsell take rate, first renewal, cancellations/refunds/disputes by offer, and ARPU/pLTV.

Write the specification: relevant result and preview; supported plans and any recommended default; exact charges and terms; payment methods and failure states; any genuine guarantee; support/cancellation/refund links; recovery behavior; optional upsell consent; and events for each state.

Ask a reader to explain what they receive, what is charged now, what renews, and how access starts. Revise anything they misunderstand.

## Worksheet

[Open the paywall and checkout spec](templates/06-paywall-checkout-spec.md)
