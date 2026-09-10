# Economics model

Use one currency throughout, and record whether each rate is a decimal or a percentage.

## Assumptions

| Input | Downside | Base | Upside | Source |
| --- | ---: | ---: | ---: | --- |
| Spend | | | | |
| CPM | | | | |
| CTR | | | | |
| Click → purchase CR | | | | |
| First collected amount | | | | |
| Plan mix | | | | |
| Upsell value/take rate | | | | |
| Renewal curve | | | | |
| Refund rate | | | | |
| Dispute loss/fees | | | | |
| Processing | | | | |
| Taxes | | | | |
| Variable delivery/support | | | | |
| Payout delay | | | | |
| Opening acquisition cash | | | | |
| Minimum cash reserve | | | | |

## Outputs

```text
Impressions = Spend ÷ CPM × 1000
Clicks = Impressions × CTR
Purchases = Clicks × Click-to-purchase CR
CAC = Spend ÷ Purchases
Net cohort value = collected revenue − refunds − disputes − processing − taxes − variable cost
Contribution pLTV_Dn = predicted net cohort value by day n ÷ buyers in the cohort
Net ROAS_Dn = cumulative net cohort revenue by day n ÷ spend
```

Target CAC:

Required pLTV/CAC margin:

Maximum payback:

Maximum test loss:

Scale condition:

## Cash plan

| Day/week | Ad spend | Cash collected | Provider reserve/hold | Refunds/disputes | Payout received | Closing acquisition cash |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| | | | | | | |

`Closing cash = opening cash − ad spend − other cash costs + payouts received`.

The model passes a unit check only when every multiplication and division uses compatible units. For CPM and CTR, use `CPC = (CPM ÷ 1,000) ÷ CTR`.

Reference check: with `$20 CPM` and `2% CTR`, `($20 ÷ 1,000) ÷ 0.02 = $1 CPC`.
