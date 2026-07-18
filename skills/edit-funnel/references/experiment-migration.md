# Experiment Migration And Staged Variants

Rules for porting experiments between funnels and for landing variant steps
before the experiment is live. Every rule below comes from the Blessly v3
experiment migration (2026-07-16/17), where each violation shipped and needed
a follow-up fix in the funnel repo.

## Keep inactive variants unbranched

A variant step that is not yet part of a running platform experiment lands as
a normal manifest step: registered in the step registry, content and editor
files in place, edges converging into the live flow via `goNext()`.

It must NOT:

- appear in the default flow's edges as a reachable next step,
- be declared as a manifest `branches` entry.

Branch declarations and traffic routing belong to the platform experiment. A
hand-authored branch for a not-yet-started experiment ships dead routing,
breaks flow-shape tests, and has to be reverted ("keep inactive entry variants
unbranched"). Pin this with a test that asserts the staged variant ids are
absent from `branches` and unreachable from the entry step, while still
present in `funnelManifest.steps`.

## Never copy experiment ids across funnels

Experiment rows, PostHog flags, and `src/config/experiments.generated.ts`
belong to one funnel id. When porting an experiment to another funnel:

- Port only the variant step code, content, and assets.
- Recreate the experiment in the FunnelsGrove UI/API against the new funnel
  id; the platform regenerates `experiments.generated.ts`.
- Write experiment tests against the stable experiment `name`, source step,
  variant route targets, weights, and labels — never against generated ids.
- Assert every experiment route target exists in `funnelManifest.steps`.
- Allow `paused` state during preview QA; forbid `stopped`. Verify the final
  `running` state as its own late task, after the platform sync.

## Navigation ports as edges, not targets

Old variant code often hardcodes its next step (`goToStep('step-3')`). The
target flow usually converges somewhere else. Replace every hardcoded
navigation with `goNext()` plus a manifest edge into the new flow's
convergence step. A ported variant must never navigate to a step id from the
source funnel.

Entry variants must also stay navigation contract-safe inside the step UI: no
raw `<a href target="_blank">` anchors (legal links included) — render such
text through contract-safe elements or the shared navigation helpers the
managed docs prescribe.

## Managed docs bundle is generated, not edited

`.funnelsgrove-docs.json`, `funnel-docs.config.json`, and every
`funnelsgrove:generated` block under `docs/funnelsgrove/` are refreshed by
`fgrove docs`, and their hashes must match the bundle metadata. Hand-editing a
bundle version, CLI version, or generated block breaks bundle compatibility
and gets reverted. If the managed docs look stale, run `fgrove docs --dir
<local-dir>`; never bump the metadata yourself.

## Ported assets re-enter the pipeline

Images copied from the source funnel are new assets in the target: register
them in `funnelManifest.assets` with `width`/`height`, attach them to the
variant step's `assetIds`, and keep them on the build-time AVIF/WebP path (see
the Image Performance Lock in SKILL.md). Do not carry over source-funnel
preload maps.

## Control files are already the control

When migrating an experiment into a rebuilt funnel, the rebuilt funnel's
current entry and paywall steps ARE the control variants. Do not overwrite
them with the source funnel's control files — port only the alternative
variants, and keep the target's control byte-identical.
