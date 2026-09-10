# Launch QA

## Flow

- [ ] Every screen and branch opens and terminates correctly
- [ ] Back, refresh, and return preserve valid state
- [ ] Email validation and account recovery work
- [ ] All experiments assign and track variants correctly

## Devices and browsers

- [ ] Small, medium, and large mobile viewports
- [ ] Desktop purchase path
- [ ] iOS Safari and Android Chrome
- [ ] Meta/Instagram/TikTok in-app browsers used by your traffic
- [ ] No overlap, clipping, horizontal scroll, or unreachable CTA

## Payment

- [ ] Displayed and charged plan/price/coupon match
- [ ] Wallets appear only when available; card fallback works
- [ ] Processing, failure, cancel, and retry states work
- [ ] Test payment produces one verified server purchase
- [ ] Upsell has a separate offer and authorization
- [ ] Refund and cancellation paths work

## Handoff and product

- [ ] Installed-app path works
- [ ] New-install path works
- [ ] Desktop-to-phone path works
- [ ] Lost-deep-link email/login recovery works
- [ ] Entitlement reflects active, pending, canceled, and expired states
- [ ] First useful action is reachable and measured
- [ ] Subscription-management link works

## Analytics

- [ ] UTMs/click IDs survive to the cohort record
- [ ] Browser and server events deduplicate
- [ ] Amount/currency/product values reconcile with the provider
- [ ] Funnel version and experiment variant are present
- [ ] Test data is excluded from production reporting

## Trust and operations

- [ ] Today/renewal terms are clear
- [ ] Terms, Privacy, and Refund links work
- [ ] Support contact is visible
- [ ] Receipt and cancellation confirmation arrive
- [ ] Statement descriptor is recognizable
- [ ] Refund/dispute monitoring has an owner

Launch owner:

Test budget/loss limit:

Stop conditions:

Scale conditions:

Known limitations accepted for this test:
