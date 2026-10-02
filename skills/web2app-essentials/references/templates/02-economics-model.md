# Economics model

Use one currency and decimal rates in calculations: 2% = 0.02.

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

Check units: `CPC = (CPM ÷ 1,000) ÷ CTR`. At $20 CPM and 2% CTR, CPC is $1.
