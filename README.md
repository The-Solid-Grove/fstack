# fstack

A small skill pack for building and editing web funnels with AI agents.

- `create-funnel` — scaffold a new funnel from the FunnelsGrove funnel template (copy, reskin, verify, optional hosted wiring).
- `edit-funnel` — local editing loop for FunnelsGrove hosted funnels (sync, preview, QA, publish).
- `writing-funnel-copy` — quiz-to-paywall copy and conversion strategy.
- `preview-funnel` — temporary local click-through mockups for reviewing funnel copy, styled with the bundled "candlelit stationery" stylesheet.

Current version: `0.5.7`

## Requirements

- Git, Bash
- Node.js 18+ and npm (for the FunnelsGrove CLI)
- Codex and/or Claude Code
- FunnelsGrove CLI for hosted funnel work:

  ```bash
  npm install -g @funnelsgrove/cli
  fgrove login
  ```

## Install

```bash
git clone git@github.com:The-Solid-Grove/fstack.git ~/.fstack
cd ~/.fstack
./setup --host auto
```

Single host: `./setup --host codex` or `./setup --host claude`.

| Host | Skill directory |
| --- | --- |
| Codex | `~/.codex/skills/<skill-name>` |
| Claude Code | `~/.claude/skills/<skill-name>` |

The installer creates idempotent symlinks back to this checkout. By default it
also checks the installed `fgrove` CLI against the latest `@funnelsgrove/cli`
on npm and updates it when newer. Skip that check with `--skip-fgrove-cli`.

## Update

```bash
cd ~/.fstack
git pull --ff-only
./setup --host auto
```

## Use `create-funnel`

```text
Use $create-funnel to start a new funnel for <AppName> from the funnel
template, verify the full flow locally at small 375x667, medium 393x852,
large 402x874, and desktop-small 1280x800, and wire the hosted funnel only
when I ask.
```

The skill copies `apps/funnel-template` from a funnelsgrove monorepo checkout
(never `fgrove create` from the global CLI — the npm package does not ship
templates), reskins the name/branding, installs dependencies, runs checks, and
walks the full flow locally including the paywall's two-stage discount. The
template ships working quiz steps, email capture, the ClaimBee-derived paywall
with discount-on-close, a paywall B variant for experiments, Apple Pay/Google
Pay slots, and subscription management. When adding steps, user-facing URLs must
be meaningful slugs rather than `/step-1` style routes; internal ids or filenames
may stay sequential if the project already uses that convention.

## Use `edit-funnel`

Ask the agent to use the skill against a target funnel:

```text
Use $edit-funnel to edit <workspace>/<project>/<funnel>. Change <copy/screen>,
run local preview, ask whether to publish, publish preview if approved, run QA,
verify preview coverage for the production candidate, and publish production
only after approved preview QA.
```

The skill syncs the funnel locally, reads its `AGENTS.md`/`agent.md`, makes
edits, runs checks, opens local preview, and loops until ready. Before
refreshing a synced directory, it checks local git state and GitHub sync state,
checkpoints local changes, and merges any newer remote draft intentionally.
When GitHub is connected, source changes go through normal git commit/push,
then `fgrove github pull` syncs GitHub into the hosted draft; the agent must not
also run `fgrove sync up` for the same diff. When GitHub is not connected, it
downloads the current hosted draft into a temporary clean directory and uses
that as the merge source. After creating or editing any step, it runs a
content-fit audit in local preview at all four default breakpoints: small
`375x667`, medium `393x852`, large `402x874`, and desktop-small `1280x800`.
Update local project packages with the package manager already used by the
synced tree.
Use `npm outdated`, `pnpm outdated`, yarn, or bun as appropriate, and never
introduce a second lockfile. Ask whether to publish before any deploy. Publish
returns a deployment id and preview URL; poll deployment status by id when the
CLI/API exposes it, and watch the stage metadata (`publishBuild`,
`stageTimings`, runtime environment, and image-variant stages) before declaring
a deploy stuck. Before production publish or post-publish production QA, verify
whether the current production candidate already has a matching preview build.
If it does not, publish to preview first and run the full QA checklist on that
preview URL. Only run production QA after an explicit production publish.

For new steps, keep `path` values semantic and user-readable. Sequential ids and
`step-NN-*` filenames are fine for code ordering, but public URLs should be
meaningful route slugs, not `/step-1`.

Image performance is part of every image-touching edit. Keep the publish build's
raster optimization and AVIF/WebP variant generation enabled, and verify the
`imageVariants` stage when publishing. Funnel images should be declared in
`funnelManifest.assets` and attached to steps with `assetIds`, then preloaded
with the ClaimBee/Blessly pattern: first-viewport images use the framework's
normal priority/preload path, while the shell warms only likely next-step images
at low priority instead of preloading the whole funnel.

Full QA is described in `docs/funnel-qa-checklist.md`. It includes every step,
branch, and active A/B experiment; paywall and checkout paths; Apple Pay and
Google Pay button appearance; checkout/payment behavior; complete registration;
required links; and `/manage-subscription` cancellation when a test subscription
is available. Production publish is opt-in — pass the target domain explicitly.

## Use `writing-funnel-copy`

```text
Use $writing-funnel-copy for a <product> funnel. Ask for the required product
context first, then return the strategy and screen-by-screen copy.
```

The skill asks for product, audience, entry promise, and screen count, then
returns pre-work, transformation arc, screen specs, paywall architecture, and
A/B ideas. Reference material lives under
`skills/writing-funnel-copy/references/`. Once copy is drafted, it should offer
to use `preview-funnel` when a temporary local visualization would make review
easier.

## Use `preview-funnel`

```text
Use $preview-funnel to turn this finished funnel copy into a temporary local
click-through mockup, keep the styling simple, run a local server, and verify
the sticky CTA at small 375x667, medium 393x852, large 402x874, and
desktop-small 1280x800.
```

The skill creates throwaway static HTML/CSS/JS outside tracked source, usually
under a `mktemp` directory, so product-specific preview artifacts do not stay in
the repo. It uses simple building blocks: progress header, headline, support
copy, choice cards, notes/proof rows, and sticky bottom buttons. It reports the
local URL, how to restart the server, and whether the temporary files were
removed or left for review.

## Use `web2app-essentials`

```text
Use $web2app-essentials: what conversion should we expect from paywall to
purchase, and which onboarding mechanics have measured uplift?
```

The skill is a Q&A knowledge base for web2app and quiz-to-paywall funnels —
benchmarks, paid acquisition, onboarding mechanics, monetization, payments,
analytics, growth process, and compliance. It routes each question to the
matching module under `skills/web2app-essentials/references/` and answers with
the corpus's concrete numbers and caveats. Ask it to "teach web2app" for a
module-by-module learning path. It is reference-only: implementation work
still goes through `create-funnel`, `edit-funnel`, and `writing-funnel-copy`.

## Team setup

Use a shared global checkout. Add this to your project `AGENTS.md` or
`CLAUDE.md`:

```markdown
Use fstack for FunnelsGrove funnel work. Use `create-funnel` to start a new
funnel from the template, `edit-funnel` for hosted edits, `writing-funnel-copy`
for quiz-to-paywall strategy, and `preview-funnel` for temporary local copy
mockups. Always run local preview, ask before publishing, verify preview
coverage for the production candidate, run preview QA before any production
publish, and run production QA after production publish. For new steps, use
meaningful public route paths even when ids or filenames are sequential. For
image edits, keep build-time image optimization enabled and use
manifest-driven next-step image preloading.
```

Each teammate runs:

```bash
git clone git@github.com:The-Solid-Grove/fstack.git ~/.fstack
cd ~/.fstack && ./setup --host auto
```

## Uninstall

```bash
rm -f ~/.codex/skills/create-funnel ~/.claude/skills/create-funnel
rm -f ~/.codex/skills/edit-funnel ~/.claude/skills/edit-funnel
rm -f ~/.codex/skills/preview-funnel ~/.claude/skills/preview-funnel
rm -f ~/.codex/skills/writing-funnel-copy ~/.claude/skills/writing-funnel-copy
rm -f ~/.codex/skills/web2app-essentials ~/.claude/skills/web2app-essentials
rm -rf ~/.fstack
```

## Develop

```bash
bash tests/smoke.sh
```

Smoke checks validate the README, installer syntax, skill frontmatter, and
temporary Codex/Claude Code installs.
