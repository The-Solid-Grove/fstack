# 3. Economics: CAC, pLTV, ROAS, and cash payback

Build a model that connects acquisition cost, cohort value, and the cash needed to grow.

## Compare like with like

**[pLTV](/resources/web2app-glossary#pltv) > [CAC](/resources/web2app-glossary#cac)** is useful only when pLTV has a defined horizon, cost basis, and forecast uncertainty. Profitability and the ability to fund growth are separate questions.

For one traffic cohort:

```text
Clicks = Impressions × CTR
Paywall views = Clicks × CR(click → paywall)
Purchases = Paywall views × CR(paywall → purchase)
CAC = Spend ÷ Purchases
```

Use compatible counting units throughout. For funnel reach, divide unique viewers of a step by unique first-screen visitors; count actual views, not button taps. For a transition rate, use the preceding stage as the denominator. Compare the same geography, device, source, offer, and time window.

Conversion changes multiply across steps, but can also change buyer quality. Judge the resulting cohort, not one improved transition or a cheaper first purchase.

## Calculate cohort value

Track first payments, upsells, renewals, refunds, disputes, fees, taxes, and variable delivery/support costs by acquisition cohort. Separate source, geography, funnel, plan, and offer where they produce different economics. A monthly revenue average mixes cohorts of different ages.

```text
Gross collected revenue
− discounts and credits not already reflected
− refunds
− chargebacks and dispute fees
− payment processing
± FX settlement effects
− VAT / sales tax
− variable product and support costs
= net cohort value before acquisition
− acquisition spend
= contribution after acquisition

Realized LTV_Dn = realized net cohort value through day n ÷ original cohort buyers
pLTV_Dn = predicted net cohort value through day n ÷ original cohort buyers
```

Failed payments are absent from collected revenue; track lost collections without subtracting them again. Keep the same gross or net definition across dashboards.

**Example:** 100 buyers produce $1,000 in first payments, then $1,100 and $700 in renewals: $2,800 gross. Subtract $140 refunds, $84 processing, $280 tax, and $100 variable cost. Net value is $2,196, or **$21.96 realized LTV per buyer** at the observed horizon.

For immature cohorts, forecast future renewals using similar mature cohorts or conservative scenarios. Label forecasts separately from actuals, and backtest prediction error. First-payment conversion alone cannot establish that an introductory offer is profitable.

## ROAS and cash payback

Using the net-value definition above:

```text
Net ROAS_Dn = cumulative net cohort value through day n ÷ cohort acquisition spend
```

Always label the horizon and whether the numerator is realized or forecast. D0 describes immediate recovery of acquisition spend; D30 or D365 adds later value. Forecast D365 ROAS is not collected cash.

**Cash payback** is the first day cumulative cohort cash payouts, after refunds, fees, taxes, and payout delay, cover acquisition spend. A profitable long-term forecast can still exhaust cash before payback.

Model opening cash, spending pace, payout delay, refund timing, renewal schedule, and a minimum operating reserve.

## Build three scenarios

Create downside, base, and upside cases with these inputs:

| Area | Inputs |
| --- | --- |
| Acquisition | CPM, CTR, implied CPC, click-to-purchase conversion |
| Offer | First price, plan mix, upsell take rate |
| Retention | First renewal rate, later renewal curve |
| Costs | Refunds, disputes, processing, tax, variable costs |
| Cash | Payout and refund timing, spending pace, opening cash, reserve |

Report CAC, D0 net ROAS, pLTV at D30/D90/D365, cash payback day, and maximum spend before the reserve is exhausted.

Before increasing spend, check cohort maturity or forecast support, net value after costs, traffic-mix changes, purchase-to-product activation, dispute levels, payout capacity, and performance across several creatives.

## Exercise

Use the three scenarios to identify:

- Break-even CAC at D30 and D365, and a target CAC allowing the required margin.
- Spend the business can carry until cash payback.
- The most influential input: CTR, funnel conversion, price, renewal, or refunds.

## Worksheet

[Open the economics model](templates/02-economics-model.md)
