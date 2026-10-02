---
name: create-funnel
description: Use when creating a new hosted FunnelsGrove funnel from one of three templates, downloading its source, and establishing the product brief and Design.md before customization. Use for new funnel projects; use edit-funnel for an existing funnel.
---

# Create Funnel

Create through the connected FunnelsGrove account, then download the new funnel's source with the CLI. The three template cards describe different starting structures; choose for the product and journey, then establish its own identity in `Design.md`.

## FunnelsGrove Contract Gate

For every implementation-facing task:

1. **MUST** read `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` before choosing step metadata or changing code.
2. **MUST** derive step classification, answers, routing, analytics, and helpers only from those managed docs; **NEVER** copy them from research teardowns.
3. **MUST** run `fgrove validate` after the change and resolve every blocking diagnostic before preview, sync, or publish.

These gates remain mandatory when tests and builds pass, the change looks small, a deadline is urgent, or someone asks to skip them.

## 1. Connect and choose

Run the Fstack checkout's `scripts/ensure-fgrove-cli`, then:

```bash
fgrove whoami
fgrove projects list
fgrove templates list
fgrove templates show <template-slug>
```

A connected `fgrove` account and an existing project are prerequisites. If authentication is missing or expired, guide the user through `fgrove login`, then recheck `whoami`. Resolve the workspace and project from supplied context; ask only when the target is ambiguous. Never substitute a local-only scaffold or another user's funnel.

Read the actual CLI cards, including descriptions and create examples. Recommend one based on the requested journey, explain the fit briefly, and resolve the choice with the user unless already specified. The initial catalog uses `default`, `one-page`, and `one-page-v2`. Read available choices from the connected account: the catalog owns names, offered keys and pinned demo/source versions. Open the returned demo through an available browser tool and inspect its actual screens for the exact journey; CLI descriptions explain the initial patterns. A withdrawn choice is unavailable for new creation. If the demo cannot be inspected, record that limitation and keep its exact screen structure unconfirmed.

Use the supplied product name as the funnel name unless a different name or naming convention is specified. Settle the destination. Default to `funnels/<kebab-name>` in a FunnelsGrove workspace; elsewhere use a new named subdirectory. Preserve existing folders. A request to create a new funnel authorizes this template creation and source download. The API also builds its initial preview automatically; tell the user this before creation.

If `templates` or `funnels create` is unavailable after updating, report the installed version and missing command. Use a released CLI with these commands before continuing this workflow.

Completion: authenticated account, unambiguous project/workspace, selected template, new funnel name, and unused destination.

## 2. Create through the API and download

Generate and record one UUID creation key before invoking the command. Reuse it for a retry of this same creation; use a fresh key for another funnel.

```bash
fgrove funnels create --workspace <workspace> --project <project> \
  --template <template-slug> --name <funnel-name> \
  --idempotency-key <creation-key> --json
fgrove sync down --workspace <workspace> --funnel <returned-funnel-id> --dir <dest>
fgrove docs --dir <dest>
```

Creation waits only for downloadable draft source, while the initial preview continues independently. Download the returned funnel ID with `sync down`; `funnels clone` is for copying an existing funnel and is not this workflow. If creation times out or fails after the server accepted it, follow the printed recovery instructions and retain its ID/key; a local failure is not evidence that no hosted funnel exists.

Read the downloaded `AGENTS.md` and `docs/funnelsgrove/START-HERE.md`. Managed documentation is the implementation authority, including the exact step-type pages for edited screens. Preserve generated runtime configuration, source structure, image optimization, and ignored environment files.

Completion: new hosted funnel ID, downloaded source and sync manifest, and current managed docs. An account or setup failure remains a named blocker; a filesystem copy does not satisfy this step.

## 3. Ask the product and design essentials

Immediately after downloading, use [the intake and Design.md guide](references/intake-and-design.md). Reuse facts and assets already supplied. Ask only unanswered essentials in one compact round, in the user's language, with proposed defaults where helpful.

Create `<dest>/Design.md` during this step, even for scaffolding-only work. Record confirmed facts, proposed choices, and unresolved questions separately. Resolve the decisions needed for the requested customization before changing screens; keep remaining unknowns explicit. Existing product design documents are inputs to this file, not a replacement for it.

Completion: the essential questions have been asked and answered or explicitly deferred; a product-specific `Design.md` exists with concrete reusable visual decisions and links to supplied evidence. While answers are pending, label the brief provisional and name which decisions block customization. Creation and brief completion do not imply a completed design or verified funnel.

## 4. Customize within scope

Use `Design.md` and the downloaded contracts to update identity, requested content and assets. Inspect the selected template rather than assuming it has a fixed number of questions, a paywall B variant, discount-on-close, or a particular payment integration.

- Review package/config/manifest metadata, browser title, visible copy, imagery, legal links and sample product claims. Replace starter identity with the actual product; use the real funnel name in metadata. Retained sample content must be identified in the handoff.
- Keep user-facing routes meaningful. Register new images in the manifest and on their owning steps according to managed asset/preloading contracts; retain build-time raster compression and variants.
- Keep offer terms, prices, proof and legal details tied to supplied facts. Track missing facts in the brief instead of inventing them.

Use `writing-funnel-copy` when creating or revising the journey's copy. For a full visual design, reach an available `design-funnel` workflow with the intake and `Design.md`; otherwise implement the authorized design directly from those inputs. A scaffolding-only request ends with a working starter and its design brief, not an invented complete product funnel.

## 5. Verify and hand off

Install using the downloaded project's package manager and lockfile. For customization or a ready-to-use funnel, run its available tests, lint and build commands. **MUST** run `fgrove validate --dir <dest>` before delivery and every sync/publish. Validation is required for scaffolding-only work too.

For a creation-and-brief-only request, deliver the hosted ID, downloaded source, `Design.md`, question status and validation evidence; identify runtime/payment QA as outside that requested scope. For customization or a ready-to-use funnel, start the local app and exercise the selected template's actual flow and branches. Use `qa-funnel` and managed `docs/funnelsgrove/qa/` instructions for the requested scope. Report unavailable checkout/provider configuration as specific blockers; distinguish tested flow from untested payments.

When delivery includes hosted changes, use `fgrove sync up` for a funnel without GitHub sync, or commit/push and `fgrove github pull` for a connected repository, then publish preview and verify it. Production publication requires explicit user authorization. The API's original starter preview does not include later local customization until it is synced and published.

Return the chosen template and why, workspace/project and funnel ID, local folder, `Design.md`, completed checks, retained sample content, and remaining blockers. Include the customized preview URL only when it has actually been published and verified.
