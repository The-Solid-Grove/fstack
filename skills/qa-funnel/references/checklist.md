# Full funnel QA checklist

Use with [QA Funnel](../SKILL.md) for full preview, release-candidate, and post-publish production QA. Apply [design checks](design.md) to every screen.

## Preview and production evidence

Record workspace/project/funnel, environment, URLs, version ids or sequences, and evidence that preview matches the production candidate or deployed version. Missing matching preview QA is a release blocker; inspect production anyway and report the gap. Publishing or creating a preview follows `edit-funnel` and existing target-specific authorization.

## Full Funnel Coverage

Verify the funnel as a user would move through it:

- Open the first step and confirm the page loads without runtime errors.
- Verify every step opens the expected page.
- Verify every branch opens the expected page, including negative, skipped,
  ineligible, discount, upsell, downsell, and exit paths that the funnel
  supports.
- Verify every active A/B experiment variant opens a page and can continue to
  the next expected step.
- Submit email or identity capture with test data and confirm the next expected state.
- Exercise back, refresh, resume, invalid input, duplicate taps, and supported failure/retry paths. Verify answers and personalization survive as the managed contract specifies.
- Check expected analytics events and identifiers through available authorized evidence; ensure step and purchase events are not duplicated. Record unavailable analytics access separately.
- Check browser console and network errors when a browser tool is available.

## Visual Pass

This table is the single source of viewport sizes for every fstack skill.
Check each breakpoint twice: **layout** at the full screen size and **first
view** at the area actually visible when the page loads.

| Breakpoint | Layout | First view (≈) | Baseline |
| --- | --- | --- | --- |
| small | `375x667` | `375x548` | iPhone SE and smaller-width stress check |
| medium | `393x852` | `393x660` | iPhone 15/16 |
| large | `402x874` | `402x680` | iPhone 17 Pro |
| desktop-small | `1280x800` | `1280x700` | 13-inch MacBook, Chrome |

First-view sizes are approximate: mobile Safari with its bars expanded at page
load (Instagram and Facebook in-app browsers are similar), and a maximised
desktop browser below the menu bar. When a real phone or the target in-app
browser is available, measure `window.innerHeight` there and use that value;
record whether measured or default sizes were used.

**First view** — resize the browser window (or emulated viewport) to the
first-view size and load each screen:

- Question and energy screens show the headline, every single-choice option
  (or the dominant evidence) and the primary or sticky CTA without scrolling.
- The sticky CTA covers no option, input, validation message or disclosure.
- Long screens (long multi-select lists, paywalls) may scroll, but the headline
  and the CTA are visible at load.

**Layout** — at the full size:

- Nothing intersects or overlaps: text never collides with images, cards,
  badges, dialogs, or the action bar.
- The continue button sits on an opaque (non-transparent) bottom bar and stays
  visible on every step, including while content scrolls beneath it.
- No horizontal scroll, clipped or truncated content, or broken images.
- Disabled button states render visibly and enable when input becomes valid.

## Image Performance

For image edits, image-heavy steps, and every preview-to-production candidate:

- Confirm raster images stay on the build-time optimization path. A publish
  should report the `imageVariants` stage through `publishBuild.stageTimings`,
  CLI output, or deployment metadata; if that data is unavailable, name it.
- Confirm preview or production serves optimized AVIF/WebP variants when the
  browser sends matching `Accept` headers, with the original image as fallback.
- Confirm edited images are declared in `funnelManifest.assets` with width and
  height and attached to the relevant steps through `assetIds`.
- Confirm first-viewport images use the framework's priority/preload path, and
  the flow shell warms only likely next-step images at low priority. Do not
  preload the full funnel image set up front.

## Paywall And Checkout

Verify the paywall and checkout experience end to end:

- Open every paywall used by the funnel and confirm prices, products, discounts,
  guarantees, terms, and primary calls to action are correct.
- Open checkout from each paywall path and confirm the checkout loads.
- Verify Apple Pay and Google Pay buttons appear when supported by the test
  browser, region, device, and payment configuration. Wallet buttons silently
  fail when the funnel domain and checkout return URLs are not configured in
  the Stripe dashboard (payment method domains and return-URL allowlist); for
  new funnels or new domains, confirm that Stripe configuration exists and
  report missing configuration as a named blocker, not a pass.
- Complete a test payment, or verify the payment path with the target-approved
  equivalent when real payment is not appropriate.
- When the funnel supports a checkout-close offer, verify the configured recovery action, acceptance, and decline path. Confirm the resulting plan, coupon, first charge, and renewal match the reopened checkout. Check a larger second-stage discount only when the product specifies that mechanic.
- Confirm successful payment returns to the expected success, onboarding, or
  registration state and grants the purchased entitlement to the correct test account. Verify app/web access and recovery links where supported.
- Verify declines, interruption, retry, and duplicate submission do not show false success or create duplicate charges, using supported test fixtures.

## Complete Registration

Verify the complete registration page after payment or the equivalent terminal
state:

- Confirm the page loads from the expected funnel path.
- Complete the registration form with valid test data.
- Verify validation errors for required fields when practical.
- Confirm submission reaches the expected next state.
- Verify every visible link leads to the correct destination, including terms,
  privacy, support, login, app, and account-management links.

## Subscription Management

When an eligible test subscription is available (never cancel a real customer subscription under QA authorization):

- Visit `/manage-subscription` or the configured management route.
- Verify the user can reach the subscription-management experience.
- Verify the cancellation flow for the eligible test subscription.
- Confirm cancellation state, access-through date, and follow-up messaging are correct. Verify a retention offer does not obstruct cancellation.

## Reporting

Report the QA result with:

- Preview-build verification result.
- URLs tested.
- Steps, branches, A/B variants, paywalls, checkout paths, and registration
  paths tested.
- Payment method or payment-path equivalent used.
- Apple Pay and Google Pay button result.
- Subscription-management result.
- Browser and breakpoint assumptions, including layout and first-view results
  for each [visual pass](#visual-pass) breakpoint and whether first-view sizes
  were measured or the defaults.
- Image optimization and next-step preload result when images changed or the
  run is a preview-to-production candidate.
- Blockers, skipped checks, unavailable third-party services, missing test
  credentials, or accepted risks.

If any required flow cannot run because test credentials, payment mode, an
existing subscription, route support, or third-party services are unavailable,
report it as a named blocker or explicit unavailable item.
