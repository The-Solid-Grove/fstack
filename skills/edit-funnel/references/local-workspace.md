# One local folder per funnel

Keep one canonical working folder for each `(API URL, workspace ID, funnel ID)` on this computer. Names and slugs help identify the target; immutable IDs identify its saved folder. A new conversation, edit, preview, or publish is not a reason to download another checkout.

## Resolve and find

Use the target established in the main skill; resolve its immutable IDs from the user's link, current project, previous handoff, and read-only CLI results. `fgrove status --dir <path>` reports API and local identity, not whether source is dirty or current. The default API is `https://api.funnelsgrove.com/trpc`; respect the requested API or `FUNNELSGROVE_API_URL` instead when set.

Use the installed fstack checkout's helper (resolve skill symlinks physically, as in the [update workflow](../../../docs/getting-started.md#agent-update-check)):

```bash
node <fstack-checkout>/scripts/funnel-workspace.mjs find \
  --api-url <api-url> --workspace <workspace-id> --funnel <funnel-id>
```

The helper remembers paths outside the installed pack, under `$XDG_STATE_HOME/fstack/funnels` when that base is absolute, otherwise `~/.local/state/fstack/funnels`. It stores only identity and the physical folder path. It reads `.funnelsgrove-sync.json` on every lookup; it never downloads source or changes a funnel.

| Result | Action |
| --- | --- |
| `found` | Reuse the returned `path`. If the user explicitly supplied a different folder, reconcile the two before changing the canonical mapping. |
| `not_found` | Check the current folder, user-supplied path, and known project/funnel roots for an existing matching sync manifest. Adopt that folder before considering a new download. |
| `stale` | Locate the moved folder from project context and bounded nearby searches. Establish that it is the intended relocation before replacing the saved mapping; reuse the user's supplied path when that decision is already clear. A missing folder or manifest is not evidence that local work is disposable. |
| Error: identity mismatch, corrupt record, or conflicting registration | Preserve the folder and record; establish the correct identity/path before editing or syncing. |

Search only likely project roots, including hidden sync manifests while excluding `.git` and dependencies. Do not crawl the whole computer. If several folders match, choose the canonical one with the user and preserve the others. Do not silently pick the newest modification time or overwrite one copy with another.

An existing manifest records workspace/funnel IDs and a sync baseline; it does not prove API provenance. Establish the API from known project context or prior delivery evidence when first adopting a legacy folder. Ask only if that origin remains uncertain. Explicit CLI target flags can override a mismatching manifest, so check the identity before using them; they do not make a mismatched folder safe.

## First download

If no matching folder exists, use the user's requested persistent location or the project's existing funnel root. With neither available, use `~/funnelsgrove/funnels/<key>` with the helper's returned identity key. Check the destination first: an existing nonempty folder without a matching manifest must be preserved. A readable custom path is fine; the registry makes it reusable afterward.

Download only into a new or empty target:

```bash
fgrove --api-url <api-url> sync down --workspace <workspace-id> \
  --funnel <funnel-id> --dir <local-dir>
```

When download and manifest creation succeed, remember the folder. If download fails partway, inspect and recover that target; do not abandon it and invent `-v2`, `-new`, or timestamped working copies. `fgrove funnels clone` creates another hosted funnel and is not a local checkout operation.

## Remember the folder

After verifying an existing folder or completing its first download:

```bash
node <fstack-checkout>/scripts/funnel-workspace.mjs remember \
  --api-url <api-url> --workspace <workspace-id> --funnel <funnel-id> \
  --dir <local-dir>
```

The helper validates the manifest, resolves symlink aliases, and keeps the existing canonical mapping. To record a relocation or a user-selected replacement, add `--replace` only after establishing that choice; the helper changes the record, not either folder. A busy registry write can be retried after the other operation finishes. Preserve an unexplained lock or corrupt record for inspection.

Use the returned physical `path` as `<local-dir>` for the rest of the task. Record it with API/workspace/funnel identity in the handoff. If the registry is unavailable, continue only with an independently verified folder, report that persistence failed, and keep its absolute path in the handoff rather than creating another checkout.

## Refresh in the same folder

Inspect existing local changes and the hosted/GitHub status before refreshing. Preserve the current branch and local work; a local checkpoint can help recovery, but **a clean Git status or WIP commit does not mean source matches the CLI sync baseline**.

```bash
fgrove --api-url <api-url> status --dir <local-dir>
# If this folder is a Git checkout:
git -C <local-dir> status --short
fgrove --api-url <api-url> github status --dir <local-dir>
fgrove --api-url <api-url> sync rebase --dir <local-dir>
```

`sync rebase` merges the current hosted draft into this same folder, retaining local edits and advancing the baseline when successful. It leaves source unchanged when it finds conflicts and creates a local backup before applying a merge. Check the diff and rerun validation after a successful refresh. Return to the [contract-reading step](../SKILL.md#2-read-the-current-implementation-contracts), including its explicit documentation refresh even when rebase is a no-op; use `fgrove env pull --dir <local-dir>` with the same API when only environment settings need refreshing. Keep `.env*` private.

A `sync rebase` failure is a recovery decision, not permission to force a download. Read the actual diagnostics and managed sync guidance. If the installed CLI lacks rebase after the version check, identify that limitation before choosing a preservation strategy.

For GitHub-connected funnels, integrate relevant Git changes with ordinary Git while preserving the working branch and local changes. `fgrove github pull` means **GitHub → hosted draft**, a hosted write; use it only in the authorized [delivery workflow](publishing.md), not as an automatic local refresh. Continue locally against the known hosted baseline if that hosted update is outside the requested scope, and report any freshness limitation.

## Conflicts and exceptional recovery

Use the managed sync guidance and reported conflicting paths. Temporary directories are acceptable to inspect a remote snapshot or recover a lost baseline; keep them clearly marked as scratch and outside the canonical registry. Reconcile the source **and its matching sync baseline** deliberately, then continue in the remembered folder. Repeatedly committing the same conflicting files does not resolve a sync-baseline conflict.

Preserve `.funnelsgrove-sync.json`, local source, ignored environment files, and recovery backups. A missing manifest needs recovery from a valid backup or an intentional merge with a fresh export; never fabricate a baseline to make sync appear clean. `sync down --force` intentionally replaces source paths and requires the user's explicit discard decision for those changes. Its backup is recovery material, not a substitute for that decision.
