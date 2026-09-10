# Canonical Web2Web course: useful Essentials gaps

Reviewed September 10, 2026. Compared the 13 canonical lessons and worksheet
structure at FunnelsGrove commit `7eb6254f8dc94684e9b3f39bf2b8c6ae2e37c78a`
with the 16 legacy Essentials modules. This is an editorial gap assessment,
with targeted primary-source checks, not validation of every legacy claim.
The [earlier source audit](2026-09-10-pr-source-verification.md) is the starting
point for the legal and vendor-evidence qualifications below.

Canonical files named below live under `apps/web/src/content/web2web/` in
the [course source tree](https://github.com/The-Solid-Grove/funnelsgrove/tree/7eb6254f8dc94684e9b3f39bf2b8c6ae2e37c78a/apps/web/src/content/web2web).

## Findings

The canonical course already covers the durable core more clearly than the
legacy pack: channel fit, cohort economics, cash payback, promise continuity,
server-verified billing, identity recovery, analytics, and launch gates.
Preserve this structure. The valuable additions are a small evidence section
and several concrete operating decisions, not wholesale module imports.

## Strong additions

| Canonical file | Recommended edit | Legacy inspiration / evidence |
| --- | --- | --- |
| `01-what-is-web2web.md` | Add “Evidence that the channel operates at scale” after the live examples and before the founder story. Use the scoped figures below; distinguish adoption from profitability and web revenue from this specific acquisition path. | Legacy `1.1`, “Proof it works at scale”; primary RevenueCat and FunnelFox reports below. |
| `11-experimentation.md` and `templates/09-experiment-card.md` | Add analysis engine/version, fixed-horizon versus sequential method, decision thresholds, planned allocation, and sample-ratio-mismatch check. Explain that early decisions require a method designed for repeated looks; ordinary fixed-horizon p-values cannot be treated that way. | Legacy `6.2` identifies analysis-mode drift. [Statsig SPRT](https://docs.statsig.com/experiments/advanced-setup/sprt) documents required setup and distinguishes SPRT from its separate sequential-testing option. [Microsoft Research](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/) explains why allocation mismatch is a diagnostic for biased experiment data. |
| `07-paywall-checkout-upsells.md` and `templates/06-paywall-checkout-spec.md` | Add a short unpaid-abandonment follow-up design: eligible audience, stated goal/drop-off segment, trigger, honest offer, suppression after purchase/unsubscribe, sequence end, and a no-send holdout. Keep it distinct from lesson 8's paid-user access-recovery messages. Use timings as testable starting hypotheses, not universal rules. | Legacy recovery guidance; [FunnelFox email article](https://blog.funnelfox.com/retargeting-emails-in-web2app/) supplies the concrete sequence. Its numerical recovery claims are vendor assertions; the [original 311-funnel write-up](https://blog.funnelfox.com/web-funnels-insights-and-trends/) groups email and paid retargeting. Omit a promised recovery percentage. |
| `12-risk-and-compliance.md` and `templates/10-risk-register.md` | Add an operational obligation matrix: market, offer/trial length, renewal cadence, reminder timing/content, cancellation channels, consent evidence, owner, official source, checked date. The course already says to check local rules, but the worksheet does not make that check actionable. | Legacy `7.1/7.2` adds jurisdiction detail; use the primary examples below without turning the lesson into a statute catalog. |
| `12-risk-and-compliance.md` | Add a small renewal-failure playbook: distinguish recoverable declines from cases needing customer action, use supported retries, request a payment-method update, reconcile invoice state before retry, and define grace/access handling. Measure recovered net revenue and duplicate-charge/support guardrails. | Legacy `4.2` has retry depth, but its arbitrary reduced-amount and alternate-card tactics should not transfer. [Stripe Smart Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries) documents supported retry behavior and hard-decline limits. |

### Suggested introduction evidence

Use two short paragraphs or a compact two-row table:

- RevenueCat's 2026 report, based primarily on 2025 data, reports that **41% of
  its highest revenue tier has web revenue, versus 1.3% of its lowest tier**.
  Its overall dataset includes more than 115,000 apps and $16B revenue. Web
  revenue includes several paths; this is evidence of adoption among larger
  businesses, not proof that adding a quiz causes growth. Source:
  [RevenueCat, web adoption by revenue tier and methodology](https://www.revenuecat.com/state-of-subscription-apps-2026/).
- FunnelFox's 2026 report reports **82% adoption among top-grossing apps** and
  **about 90% of subscription revenue from web among its funnel scalers**.
  Keep those populations explicit. Its sources include ad-library parsing,
  partner intelligence, and platform data; sample size is not disclosed.
  This is commercially interested evidence of a working channel at scale,
  not an audited market census or an expected result for a new entrant.
  Source: [FunnelFox report](https://funnelfox.com/state-of-web2app/).

The two percentages are not competing estimates: the datasets and definitions
differ. Keep the existing founder story and its gross annualized-revenue
definition separate. Do not reinstate the old SensorTower 2023 revenue table:
store estimates cannot establish revenue earned through web checkout.

### Small compliance examples that justify the worksheet

If examples improve comprehension, use two rather than listing every law:

- Maryland's relevant reminder provision covers free gifts or trials lasting
  more than 14 days, with a 3–21 day notice window and statutory exclusions.
  Source: [§14-1329(c), (e)](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&enactments=false&section=14-1329).
- Connecticut requires annual reminders for covered agreements. Its specific
  pre-retention disclosure provision concerns telephone cancellation; do not
  recast it as a universal requirement for a line above a web save offer.
  Source: [§42-158ff(d), (e)(3)(B)](https://www.cga.ct.gov/2026/sup/chap_742d.htm).

These primary details were checked in the earlier source audit. Maine consent
is not limited to a dedicated checkbox, and Virginia has an in-person
cancellation exception; preserve those corrections if their examples recur.

## Correct two existing statements during the update

1. `03-economics.md`, “Gross revenue is not money you can scale on”: the
   waterfall starts from **gross collected revenue** but then subtracts
   **unrecovered failed payments**. Uncollected amounts are already absent.
   Remove that deduction, or explicitly start from billed/expected revenue
   and reconcile unpaid amounts before reaching collected revenue. This is
   an internal arithmetic/accounting consistency finding; the worksheet's
   collected-revenue formula already avoids the duplicate deduction.
2. `10-acquisition-creatives.md`, “Scale”: “without a sharp drop in CAC” has
   the direction reversed. Use “without a sharp rise in CAC or deterioration
   in net ROAS.” This follows the course's own CAC definition.

## Preserve coverage; avoid unnecessary additions

- **02 channel fit:** existing scorecard and build/buy/hybrid section already
  cover legacy tool-selection guidance. No vendor comparison matrix needed.
- **03 economics / 09 analytics:** existing cohort, forecast, actual,
  prediction-error, cash-reserve, and denominator guidance is stronger than
  legacy universal benchmarks. Keep the synthetic examples; omit default
  LTV, price, conversion, and store-commission assumptions.
- **04 architecture / 08 handoff:** already cover identity, entitlements,
  delayed/duplicate events, fallback login, and operational email. Do not add
  a four-stage “become a payment processor” roadmap.
- **05 research / 06 narrative:** existing promise chain, consequential
  personalization, screen rules, and mental-energy model cover the durable
  legacy concepts. Research examples can remain in the copy skill; do not
  import a second encyclopedia of funnel tactics into these lessons.
- **10 acquisition:** existing angle/hook/format separation and creative
  production records are sufficient. Skip fixed ads-per-week quotas,
  platform acquisition news, and “human-passing AI” performance rules.
- **11 experiments:** analysis-mode fields are useful; vendor win-rate
  targets, fixed holdout percentages, and statistical-engine release history
  are unnecessary for this course. Keep program reviews qualitative unless
  the actual team has a consistent denominator for valid tests and wins.
- **12 risk:** do not transfer legacy advice to obscure descriptors,
  suppress renewal clarity, dilute disputed volume, or silently change the
  charge amount/method. The canonical customer-trust framing is stronger.
- **13 launch:** the phased launch and readiness criteria already cover the
  legacy optimization sequence. Link the improved worksheets into the
  existing phases; no additional launch framework is needed.

## Verification limits

This pass inspected the complete lesson outline and read the relevant full
lessons and templates for the recommendations above. It did not reopen every
third-party example funnel, audit private founder revenue, reproduce vendor
datasets, or verify every external link and legacy numerical claim. Only the
specified source-backed additions should be treated as checked. No course or
skill files were changed by this research task.
