# 3. Economics: CAC, pLTV, ROAS, and cash payback

## Lesson outcome

You'll build a minimal financial model and define the CAC at which a funnel can be scaled.

## The core criterion

Our operational rule when scaling was the classic one:

> **[pLTV](/resources/web2app-glossary#pltv) > [CAC](/resources/web2app-glossary#cac)**

But the `>` sign hides important questions:

- Is pLTV gross or net?
- Over what horizon?
- How confident is the prediction?
- How much cash is needed before payback?
- Does it include refunds, taxes, processing, and support?

Without answers, "pLTV > CAC" becomes a tidy formula that can justify any budget increase.

## Break CAC into a chain

For a single traffic source:

```text
Clicks = Impressions × CTR
Paywall views = Clicks × CR(click → paywall)
Purchases = Paywall views × CR(paywall → purchase)
CAC = Spend ÷ Purchases
```

You can break this down further, screen by screen. That matters because several small improvements multiply.

Example:

- 10,000 clicks;
- 50% move to the second screen;
- 25% of those reach the paywall;
- 20% of paywall visitors buy.

That gives 250 purchases. If the traffic cost $10,000, CAC is $40.

Now lift each of the three conversion steps by 10% relative to baseline: `1.1³ ≈ 1.331`, so all else equal, purchases grow by roughly 33%. In practice the steps are not fully independent: a change in message or price can improve one transition and degrade cohort quality at the same time. That is why funnel optimization rarely comes down to one "magic screen".

## A starting check for funnel reach

For planning, our practitioner range for **reach second step is 30–60% of unique first-screen visitors**. Count people who actually viewed the second step, not just those who tapped the opening button. This is a working calibration range, not a representative industry benchmark or a promise for every product.

Keep geography, device, traffic, offer, and time window consistent. A low second-step rate is a reason to inspect the entry promise, loading, and interaction; the decision to ship a change still depends on net cohort value. Do not confuse this first transition with reaching the middle of onboarding.

## Measure LTV by cohort

Don't use the average revenue of all users in a month. It mixes new and old cohorts.

For each acquisition cohort, keep:

- first payment;
- upsell revenue;
- renewals by period;
- refunds;
- disputes;
- payment fees;
- taxes;
- variable delivery/support cost.

```text
Net cohort value = collected revenue
                 − refunds
                 − disputes and fees
                 − processing
                 − taxes
                 − variable cost

pLTV_Dn = predicted net cohort value by day n ÷ buyers in that cohort
```

Use separate curves for geo, source, funnel, plan, and offer. Buyers on an annual plan and buyers on a discounted weekly intro are different economic cohorts.

## A lesson from a cheap trial

In the first two months after launch we tested a weekly trial at $1. Meta delivered plenty of first purchases, but the follow-on renewal was too weak for our economics. The top of the funnel looked strong and the cohort looked weak.

This does not prove that a $1 trial never works. It shows the trap: an ad platform finds people who are good at completing the event you declared as the conversion. If that event means a cheap entry, the system can optimize for cheap entry rather than for durable value.

So compare offers by predicted net revenue, not by the number of first transactions.

## ROAS over time

```text
ROAS_D0 = cohort net revenue on day 0 ÷ cohort acquisition spend
ROAS_D30 = cumulative cohort net revenue through day 30 ÷ cohort spend
ROAS_D365 = predicted cumulative cohort net revenue through year 1 ÷ cohort spend
```

A single ROAS number without a horizon tells you nothing. Day-0 ROAS shows cash recycling. Long-horizon ROAS shows potential profitability. The business needs both.

### Synthetic pLTV example

Say a cohort has 100 buyers. They produced $1,000 in first-payment revenue, $1,100 on the first renewal, and $700 on the second: $2,800 gross. After $140 in refunds, $84 in processing, $280 in tax, and $100 in variable cost, $2,196 net cohort value remains.

```text
pLTV at this horizon = $2,196 ÷ 100 = $21.96 per buyer
```

For an immature cohort, predict future renewals from the retention curve of similar mature cohorts, or from conservative scenario ranges. Report the prediction separately from actuals, and backtest error separately from both.

## Cash payback matters more than a nice LTV/CAC

In this course, **cash payback** is the first day on which cumulative cash payouts from an acquisition cohort, after refunds, fees, taxes, and payout delay, cover the spend on that cohort.

Consider two offers:

- Offer A: CAC $25, 1Y pLTV $60, payback 120 days.
- Offer B: CAC $35, 1Y pLTV $55, payback 7 days.

With unlimited capital, A can look more attractive. With limited cash, B can grow faster, because it returns the acquisition budget to circulation almost immediately.

Add to the model:

- opening cash;
- daily/weekly spend;
- payout delay;
- refund timing;
- renewal schedule;
- minimum operating reserve.

## Gross revenue is not money you can scale on

By June 2026 the team's product reached $2.5M annualized gross revenue, calculated as monthly revenue × 12 before fees and refunds. A budget decision still needs the waterfall:

```text
Gross collected revenue
− discounts and credits not already reflected
− refunds
− chargebacks and dispute fees
− payment processing
± FX settlement effects
− VAT / sales tax
− variable product and support costs
= contribution before acquisition
− acquisition spend
= contribution after acquisition
```

Failed payments are already absent from collected revenue; track them as lost collection opportunities, rather than subtracting them again.

Use the same definition across every dashboard. If UA looks at gross ROAS while finance looks at net cash, the team will make different decisions about the same campaign.

## The minimum model before launch

Build three scenarios: downside, base, upside.

| Input | Downside | Base | Upside |
| --- | ---: | ---: | ---: |
| CPM | | | |
| CTR | | | |
| Implied CPC | | | |
| Click → purchase CR | | | |
| First price | | | |
| Plan mix | | | |
| First renewal rate | | | |
| Later renewal curve | | | |
| Upsell take rate | | | |
| Refund rate | | | |
| Processing + tax | | | |
| Payout delay | | | |

Outputs:

- CAC;
- D0 net ROAS;
- pLTV by 30/90/365 days;
- payback day;
- maximum safe spend before cash reserve is exhausted.

## Scale gate

Don't raise budget just because one day shows pLTV > CAC. Before scaling, check that:

1. the cohort is mature enough, or the prediction rests on similar cohorts;
2. economics stays positive after refunds and fees;
3. traffic mix has not changed;
4. purchase-to-product activation is not falling;
5. the payout schedule can fund the growth;
6. disputes sit in a safe range;
7. the result holds across several creatives, not one asset that burns out fast.

## Exercise

Build a spreadsheet with three scenarios. Then answer:

- what CAC is break-even at D30 and at D365;
- what CAC you are willing to buy at, given your required margin;
- how much spend you can carry until payback;
- which change moves the model most: CTR, funnel CR, price, renewal, or refund rate.

## Sources

- [Apple: overview of receiving payments](https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments/)

## Worksheet

[Open the economics model](templates/02-economics-model.md)
