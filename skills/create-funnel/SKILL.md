---
name: create-funnel
description: Use when creating, scaffolding, or starting a new FunnelsGrove funnel project — "new funnel", "create a funnel", "start a funnel for an app", "scaffold from the funnel template" — before any funnel-specific steps or branding exist.
---

# Create Funnel

## Overview

Scaffold a new working funnel from the canonical funnel template, rebrand it, verify it locally, and optionally wire it to a hosted FunnelsGrove funnel. The template ships ready to sell: quiz steps, email capture, the ClaimBee-derived paywall with two-stage discount-on-close, a paywall B variant for experiments, Apple Pay / Google Pay slots, subscription-started, and manage-subscription.

**Do not use `fgrove create` from a globally installed CLI.** The npm package does not ship templates; it fails with `ENOENT ... funnels/rag-catalog/...` (and still exits 0). Scaffold by copying the template from a funnelsgrove monorepo checkout instead.

## Required Inputs

1. App/brand name (e.g. `FitBee`).
2. Destination directory. Default to the workspace `funnels/<kebab-name>` folder when working inside a funnelsgrove workspace; otherwise ask.
3. Path to a funnelsgrove monorepo checkout (contains `apps/funnel-template`). Ask if not findable.
4. Whether a hosted funnel should be wired now or later.

## Recipe

### 1. Copy the template

```bash
cp -R <funnelsgrove-checkout>/apps/funnel-template <dest>
cd <dest>
rm -rf node_modules .next out tsconfig.tsbuildinfo
```

### 2. Reskin

- `package.json` — `"name": "<kebab-name>-funnel"`.
- `funnel.config.json` — `name` and `description` for the new app; leave ids for hosted wiring.
- `src/config/funnel.manifest.ts` — `meta.title` and `meta.description`.
- `src/theme/theme.ts` — brand palette and fonts (or keep defaults until design exists).
- Rewriting the template's per-step copy and images in `src/steps/content/*.content.ts` is a separate, later task. When adding or replacing steps, keep user-facing `path` values meaningful, such as `/fitness-goal` or `/email-capture`, not `/step-1`. Sequential or ordered step ids and filenames are okay when they match the existing tree.

### 3. Install and check

```bash
npm install        # resolves @funnelsgrove/* from npm — needs current ^ ranges in package.json
npm run test:run && npm run lint && npm run build
```

If `@funnelsgrove/*` versions fail to resolve, the copied template predates the version bumps — update the three ranges to the latest published versions and re-install.
Keep the template's image build settings intact: the publish artifact build
compresses raster images and creates AVIF/WebP variants. Do not disable that
path or replace checked-in public/content images with remote URLs that bypass
build-time image reduction.

### 4. Verify locally

`npm run dev` (note the port it actually picks — it moves to 3001+ when 3000 is busy), then walk the full flow from the first step through email capture and paywall to subscription-started. Run the docs' QA checklist (`docs/qa-checklist.md` in the funnel tree): content-fit at 430x932 and 390x844, sticky CTA on an opaque bar, paywall countdown + promo card + discounted plan prices render. Dev mode runs Stripe in test mode with the template's test plan catalog.

The copied `.env.local` is the template's local dev config (API on `localhost:4001`); it is never synced, and `fgrove env pull` replaces it after hosted wiring. Opening checkout, the close-checkout special offer, and test payments need a reachable FunnelsGrove API with its database (local API + DB, or the published preview). Without one, the paywall shows a fetch error where checkout would start — report those three QA items as a named blocker and finish them on the preview URL.

When rewriting step images later, use the ClaimBee/Blessly image loading
contract: declare images in `funnelManifest.assets`, attach them to steps with
`assetIds`, use framework priority/preload for first-viewport images, and warm
only likely next-step image assets from the shell instead of preloading the full
funnel.

### 5. Wire hosted funnel (only when requested)

```bash
<fstack-checkout>/scripts/ensure-fgrove-cli
fgrove whoami
# hosted funnel must exist first: create it in the FunnelsGrove app, or clone one:
fgrove funnels clone --funnel <source-id-or-slug> --name <new-name>
fgrove use --project <project> --funnel <funnel-id-or-slug>
fgrove sync up --dir <dest> --message 'Initial import from funnel template'
fgrove docs --dir <dest>
fgrove env pull --dir <dest>
fgrove publish --env preview --message 'Initial template import'
```

QA the preview URL with the same checklist before any production talk. Real Apple Pay / Google Pay buttons require the domain and checkout return URLs to be configured in the Stripe dashboard — report unconfigured Stripe as a named blocker, not a failure.

## Quick Reference

| What | Where |
| --- | --- |
| Canonical template | `<funnelsgrove-checkout>/apps/funnel-template` |
| Steps / flow | `src/config/funnel.manifest.ts` |
| Experiments (empty, ready) | `src/config/experiments.ts` |
| Plans / discounts | `src/config/billing.plans.ts` (+ `billing.test.plans.ts`) |
| Paywall with discount-on-close | `src/steps/step-32-paywall.tsx` |
| Agent docs (after `fgrove docs`) | `AGENTS.md`, `docs/` in the funnel tree |

## Common Mistakes

- Running `fgrove create` from the global CLI — fails, see Overview.
- Editing `apps/funnel-template` in place instead of copying it out.
- Copying `node_modules`/`.next` along and shipping stale build state — delete them before install.
- Skipping the rebrand of `funnel.manifest.ts` meta — the builder then shows template branding.
- Treating missing wallet buttons in local dev as a defect — wallets need Stripe domain/return-URL config; verify on preview with Stripe configured.
- Creating user-facing URLs like `/step-1`, `/step-2`, or `/step-07`. Use a
  meaningful route slug even if the internal step id or filename is sequential.
- Leaving new step artwork outside `funnelManifest.assets`/`assetIds`, which
  prevents manifest-driven next-step preloading.
- Disabling build-time raster compression or AVIF/WebP variant generation.
- Publishing preview before the local QA checklist has passed.
