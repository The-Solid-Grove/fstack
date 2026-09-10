# PR integration and skill revision

Follow-up to the [initial review](2026-09-10-open-prs.md), after the user
explicitly requested merging useful work, closing the remaining proposals,
and revising the skills themselves.

## Disposition

The integration branch retains the original commit ancestry for PRs **#14,
#15, #16, #17, #18, #19, #20, #22, #23, #24, #26, #27, and #28**. Merge this
branch with a merge commit so those original PRs are recognized as integrated.

Three proposals are selected for closure after integration:

- **#21:** keep the create-funnel simplification (cherry-picked `b399d05`),
  omit the global viewport scanner. Ordinary image dimensions and comparisons
  should not require an allowlist change.
- **#25:** preserve both documentation changes, omit the dedicated evidence-tag
  audit. The proposed scanner misses unknown tags and creates a separate
  maintenance surface for a single checklist.
- **#29:** omit the audit-of-audits suite. Filename mentions do not prove tests
  execute; its central promise fails for commented-out invocations. #14 runs
  actual suites and preserves their failures; #27/#28 cover installer behavior.
  The deferred research notes in #29 remain accessible in its closed PR body.

## Corrections before integration

- Match complete skill references and explicit copy-bank aliases instead of
  accepting arbitrary prefixes or suffixes.
- Reject empty provenance markers. Distinguish known capture dates from
  unknown dates with repository import records; include Nebula in coverage.
- Validate literal URL fragments, preserve plain underscores, handle duplicate
  heading collisions, and ignore examples inside inline code. The scanner
  remains limited to the Markdown forms documented in its module, not a full
  CommonMark parser. See [GitHub section-link conventions](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links).
- Move Imprint to partially walked funnels and remove speculation about the
  cause of Nebula's outage.
- Correct the scope of state-law statements, vendor benchmark populations,
  recovery attribution, and observational paywall data. Primary sources and
  verification limits are in the [source check](../research/2026-09-10-pr-source-verification.md).

## All five skills reviewed

- **create-funnel:** retain the simpler workflow and finish copy/image work
  when the user requested it, rather than always deferring it.
- **edit-funnel:** reuse authorization already given for the target/environment;
  run required QA directly; identify the fstack checklist's location clearly.
- **writing-funnel-copy:** handle scoped screen edits and reviews with relevant
  context and output; reserve full-funnel pre-work for full-funnel tasks.
- **preview-funnel:** use the bundled theme by default and honor explicitly
  requested branding, layouts, and assets.
- **web2app-essentials:** retain dated-update precedence; replace the duplicated
  benchmark card with module lookups and population/date caveats.

Contract validation, source-backed claims, complete-flow QA for major edits,
and production preview coverage remain in place. The five-skill directory
structure is preserved.

## Verification

Regression tests were observed failing before the fixes at the existing audit
interfaces. All 14 integrated shell suites pass locally, including installer
behavior tests and the formerly failing update-block suite. The README cover
was visually inspected. CI must also pass on the final publication candidate.

## Final review

### Standards

The independent review found an unconditional publishing-authorization
completion condition and an incorrect recovery-module pointer. Both were
corrected: local-only tasks can complete without publication authorization,
and the lookup now distinguishes acquisition from email recovery. No code
fix defect was reported.

### Spec

The independent review found the same recovery pointer and an unconditional
full-framework read in the scoped-copy workflow. The pointer and workflow
step were corrected. No remaining blocking requirement gap was identified.
