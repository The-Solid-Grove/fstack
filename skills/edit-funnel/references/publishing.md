# Publishing an edited funnel

Read this when the requested delivery includes a hosted draft, preview, or
production release. Continue from the verified canonical folder selected by
[Edit Funnel](../SKILL.md). Every command below uses that folder and the
resolved API URL. Verify its workspace/funnel identity before a hosted write.

## 1. Establish the authorized delivery stage

Reuse the user's existing authorization for this funnel and environment.
Local-only work stops before hosted source writes. Draft delivery authorizes
the selected source path; preview delivery additionally authorizes publishing
preview. Production requires explicit authorization for the target domain.
When a stage is missing authorization, finish local verification and ask only
for that stage. Passing checks does not grant publication permission.

Read the current managed `docs/funnelsgrove/qa/publish.md`. Confirm the target,
review local changes, and inspect the connection state:

```bash
fgrove --api-url <api-url> status --dir <local-dir>
git -C <local-dir> status --short
fgrove --api-url <api-url> github status --dir <local-dir>
```

Run the Git command only when the folder is a Git checkout. **MUST** run
`fgrove validate --dir <local-dir>` and resolve blocking diagnostics before
hosted writes. Complete the applicable local tests and QA from the main skill.

## 2. Deliver source through one path

For a GitHub-connected funnel, use its connected repository and branch. Review
and commit only the intended source changes; preserve the repository's required
review and merge workflow. Verify the upstream before pushing:

```bash
git -C <local-dir> push
```

After the intended commit reaches the connected branch, pull it into the draft.
A feature-branch push alone does not update a draft connected to another branch.

```bash
fgrove --api-url <api-url> github pull --dir <local-dir>
fgrove --api-url <api-url> github status --dir <local-dir>
```

`fgrove github pull` writes GitHub source into the hosted draft; it is not a
local Git refresh. Wait for that pull job to complete or report skipped, then
confirm the draft contains the intended commit before publishing. A failed or
unresolved job is a blocker. Do not also use `fgrove sync up` for the same diff.

For a funnel without GitHub source sync:

```bash
fgrove --api-url <api-url> sync up --dir <local-dir> --message '<summary>'
```

If source conflicts, follow [Local workspace](local-workspace.md) to preserve
and reconcile changes in the canonical folder, then repeat validation and
affected QA before retrying. A request to deliver only a draft ends here with
the synced version and local verification evidence.

## 3. Verify the preview candidate

Publishing uses the hosted draft. Complete source delivery first; a publish
command does not upload local edits.

When preview publication is authorized:

```bash
fgrove --api-url <api-url> publish --dir <local-dir> --env preview --message '<summary>'
```

Record the returned URL, version ID and sequence when available. Open the URL
and use `qa-funnel` to test the first step, changed screens, their routes, and
affected paywall/checkout/conversion paths. Major changes and production
candidates require the [full checklist](../../qa-funnel/references/checklist.md).
For image changes and production candidates, verify the `imageVariants` stage
and optimized AVIF/WebP delivery with the original fallback, plus actual
manifest-driven next-step loading. Name unavailable evidence explicitly.

Before production, establish that successful preview QA covers the exact
candidate using matching version IDs, sequences, or deployment/source evidence.
An old preview of another version does not cover the current candidate. Reuse
an existing matching preview and its relevant QA evidence; otherwise obtain any
missing preview authorization, publish the candidate to preview and run full QA.
Further source changes invalidate the earlier candidate's verification.

Missing required preview QA blocks release readiness unless the user explicitly
accepts that specific risk. Record accepted exceptions without labeling the
unperformed checks as passed.

## 4. Publish and verify production

Confirm the selected funnel and authorized domain immediately before release.
Use the domain provided or confirmed by the user:

```bash
fgrove --api-url <api-url> publish --dir <local-dir> --env production --domain <domain> --message '<summary>'
```

Record the live URL, version ID and sequence when available, then run the
required production QA against that deployed version. Use test-mode payments
or the already approved equivalent; publication permission does not authorize
real charges or changing real customer subscriptions.

Report preview and production URLs, the evidence that versions match, source
delivery path, checks and results. If production QA fails or cannot run,
distinguish the completed deployment from unverified release readiness and
give the concrete blocker or explicitly accepted exception.
