---
name: design-funnel
description: Use when designing a funnel's visual system and full journey from existing Design.md, approved strategy and emotional arc, and complete screen copy, with inspected references and a representative image for every actual screen pattern. Use preview-funnel for copy-only review.
---

# Design Funnel

Before the first fstack skill in a conversation, follow the [update check](../../docs/getting-started.md#agent-update-check); offer available updates without blocking the task.

Turn approved content and the product's existing design direction into a coherent
visual system, prove it across the journey's actual screen patterns, then extend
it to every screen. For a scoped revision, apply these stages to the affected
patterns and screens while preserving accepted decisions.

The following contract gate applies when implementing in a managed FunnelsGrove
project. Image mockups and standalone clickable designs do not require hosted
infrastructure or managed runtime files.

## FunnelsGrove Contract Gate

For every implementation-facing task:

1. **MUST** read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` before choosing step metadata or changing code.
2. **MUST** derive step classification, answers, routing, analytics, and helpers only from those managed docs; **NEVER** copy them from research teardowns.
3. **MUST** run `fgrove validate` after the change and resolve every blocking diagnostic before preview, sync, or publish.

These gates remain mandatory when tests and builds pass, the change looks small, a deadline is urgent, or someone asks to skip them.

## 1. Reuse the design and approved content

Read the existing `Design.md`, product assets, approved Pre-work and Emotional
Arc, and complete screen copy from [writing-funnel-copy](../writing-funnel-copy/SKILL.md).
Record the source locations and approved versions being used. Preserve their
strategy, claims, offer, sequence, selection behavior and emotional progression.
Link existing artifacts instead of duplicating them into new files. The
Emotional Arc describes the visitor's progression; animation is a separate
design decision.

If required content is missing, use the copy workflow for only the missing or
changed scope and honor its approval handoffs before designing that scope.
If `Design.md` is missing or incomplete, use the [intake and design guide](../create-funnel/references/intake-and-design.md)
to establish the missing product decisions; this does not require creating a
hosted funnel. Ask only for facts or decisions that materially block the design.

Work in the project's established artifact location. For an existing synced
funnel, first resolve its [remembered working folder](../edit-funnel/references/local-workspace.md).
Keep generated design artifacts separate from delivered application source
according to the project's conventions.

Completion: the design has an identified product, reusable design constraints,
approved strategic sources, and usable content for every in-scope screen.

## 2. Inventory patterns and inspect references

Create or extend `screen-map.md` using the approved screen IDs. For each screen,
record its purpose, content source, visual intent, interaction/selection behavior,
important states, incoming/outgoing transition, and visual pattern. Group screens
only when one composition and control system genuinely serves their content.
Distinct layouts or states needing a different composition get their own variant.
These are design categories, not FunnelsGrove runtime metadata.

When accessible, prefer one coherent reference funnel with comparable audience,
journey and interactions. Reuse a user-selected funnel first; otherwise discover
a suitable source through the available reference access. Inspect the actual
screens and surrounding flow before borrowing a composition. Use complementary
sources only for named gaps, and record unavailable reference access rather than
claiming an inspection. A category match alone does not establish screen fit.

Select and inspect a reference for every actual pattern and variant. Use
[optional CLI references](references/cli-references.md) with a configured `fgrove`
account and reference access; the guide covers discovery, inspection and the
fallback when authenticated access is unavailable.

For each target screen, match a source screen by narrative job, control type,
option/content density and stage of the journey. Record why the pair is
compatible; matching source and target positions is not required.

Record the reference URL/image, source screen identity, inspected content and
composition being adapted beside each pattern. Map every target screen to a
pattern and its reference. A reference guides hierarchy and presentation;
the approved copy and `Design.md` remain the target's content and brand authority.
Mark uncertain observations and unsupported source claims explicitly.

Completion: every in-scope screen belongs to a documented pattern, each pattern
has an inspected reference or a named reference limitation, and the representative
screen plus necessary variants are selected from the actual journey. Coverage
comes from the funnel, not a fixed count or invented screens.

## 3. Review the opening, then settle the remaining patterns

### First-three-screen feedback checkpoint

For a new full journey or a redesign of its opening, design the **first three
actual screens in journey order** before extending the rest. If the journey has
fewer than three screens, show all of them. This is a review of actual target
content, not three arbitrary pattern examples. A scoped edit does not require
building unrelated screens; reuse explicit feedback on unchanged accepted
revisions and review the changed scope.

Use the normal available image-generation skill/tool to create screen images,
with inspected references, existing `Design.md`, exact copy, real option counts
and selection semantics. If the user requests another format or image generation
is unavailable, use a scoped alternative such as rendered mockups and identify
the format/limitation. Keep the same coverage and review requirements.

For every new or revised screen, use [qa-funnel](../qa-funnel/SKILL.md) with
exact copy, reference, `Design.md` and prior findings. Follow its
[per-screen calibration loop](../qa-funnel/references/design.md#per-screen-calibration-loop):
compare the source, review text and composition together, correct, reopen and
recheck. Reconcile copy, design, screen map, QA and approval/status documents
before presenting that revision. Current evidence belongs in `design-qa.md`.

**Show the three actual target screens to the user**, with their matched source
screens alongside or linked, and a short explanation of borrowed composition and
intentional brand/content differences. Supply readable individual images or a
reachable preview; a prompt or tiny contact sheet alone is insufficient.
Ask for feedback on hierarchy, tone and style. **Wait for the user's feedback
before designing later screens or implementing the full journey.** Record the
reviewed screen IDs/revisions and accepted feedback; revise and recheck affected
screens. Reuse explicit acceptance of those revisions instead of asking again.
This feedback is separate from strategy/arc approval and from runtime QA.

### Complete the pattern set

After incorporating opening feedback, create a separate mockup for each remaining
actual pattern and necessary layout/state variant. Use actual screen-map content,
including long copy and complete offer disclosures. Inspect the full composition
of long screens rather than a cropped viewport. Reuse accepted opening mockups
as visual context so later typography, imagery and controls stay coherent.

Save images and prompt/reference provenance in the existing design artifact
directory; link revisions to screen IDs and patterns. Every target screen keeps
its compatible reference mapping. Apply the same QA and reference comparison to
remaining mockups; correct failures before extending the affected pattern.

Review the representative set together and reconcile font families, weights,
sizes, semantic colors, spacing, widths, radii, controls/states, imagery, progress,
motion and responsive intent in the existing `Design.md`. Preserve confirmed
brand decisions; record accepted new choices. Ask for an additional style decision
only when one remains unresolved after the opening feedback.

Completion: the opening screens have been shown and feedback incorporated;
every actual pattern/necessary variant has a reviewed mockup; one coherent
visual system is recorded in `Design.md`; remaining image-versus-runtime checks
are explicit. Required unresolved decisions or defects block extension of the
affected design. Name unavailable reference coverage without inventing a comparison.

## 4. Implement the journey and verify every screen

Extend the reviewed patterns with each screen's actual copy and assets. Keep
the approved flow, branches and selection semantics, including relevant selected,
error, loading and back/next states. For an existing FunnelsGrove funnel, use
[edit-funnel](../edit-funnel/SKILL.md) in its remembered folder; use
[create-funnel](../create-funnel/SKILL.md) only for an authorized new hosted
funnel that has not yet been created. Follow their
managed contracts, source-preservation, validation and delivery workflows.
For a standalone clickable design, keep payments simulated unless integration
is explicitly in scope.

Run [qa-funnel](../qa-funnel/SKILL.md) design scope whenever a screen reaches its
final revision. Supply screen ID/revision, artifact or URL, copy, reference,
`Design.md` and prior findings. Apply the shared [calibration loop and design checks](../qa-funnel/references/design.md#per-screen-calibration-loop),
fix in-scope failures and recheck the changed revision. Shared style/component
changes invalidate affected screen results; refresh their evidence.

After the screens pass, walk the complete journey and reachable branches for
continuity, then run `qa-funnel` for the requested functional scope. Report
unavailable checks as blocked. A visual pass does not establish payment,
analytics, subscription or release readiness.

Completion: every in-scope screen has the approved content, mapped pattern and
reference, working transitions, and current rendered QA evidence or an explicitly
accepted exception. The whole journey has been exercised within the requested
scope; local or hosted delivery follows the user's existing authorization.

## Deliver

Return the representative mockups, clickable entry or implementation location,
updated `Design.md`, approved content/arc links, screen map and QA report.
Include the first-three-screen feedback record and source/target comparison
evidence so the accepted direction is reviewable.
Report pattern coverage, reference limitations, image-direction results,
rendered checks and remaining blockers separately. Include the canonical funnel
folder when applicable so the next edit resumes there. Design and copy approval
do not authorize hosted source writes or publication.
