# fstack Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first installable fstack skill pack with README, setup script, and `edit-funnel` skill.

**Architecture:** Keep a single repository checkout as the source of truth. `setup` symlinks skill directories into host-specific skill folders, and users update by pulling the checkout and rerunning `setup`.

**Tech Stack:** Bash, Markdown, YAML, Codex/Claude Code skill directory conventions, FunnelsGrove CLI (`fgrove`).

---

## File Structure

- `README.md`: user-facing documentation.
- `setup`: idempotent host installer.
- `skills/edit-funnel/SKILL.md`: skill workflow.
- `skills/edit-funnel/agents/openai.yaml`: Codex UI metadata.
- `tests/smoke.sh`: validation suite.

## Chunk 1: Smoke Tests

### Task 1: Add Failing Smoke Test

**Files:**
- Create: `tests/smoke.sh`

- [ ] **Step 1: Write the failing test**

Create a shell script that checks required files, README sections, setup syntax, skill frontmatter, absence of template placeholder markers, optional skill validation through `quick_validate.py`, and dry-run installs into temporary Codex and Claude homes.

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/smoke.sh`

Expected: FAIL because `setup` and `skills/edit-funnel` do not exist yet.

## Chunk 2: Installer and Skill

### Task 2: Implement Minimal Installer and Skill

**Files:**
- Modify: `README.md`
- Create: `setup`
- Create: `skills/edit-funnel/SKILL.md`
- Create: `skills/edit-funnel/agents/openai.yaml`

- [ ] **Step 1: Create the skill scaffold**

Run the Codex skill creator `init_skill.py` for `edit-funnel`, then replace the template content.

- [ ] **Step 2: Implement `setup`**

Add Bash installer with `--host codex|claude|auto`, `--repo-root`, `--skills-dir`, and `--help`. It should symlink every directory under `skills/` into the chosen skill directory.

- [ ] **Step 3: Write README**

Document requirements, install commands for Codex and Claude Code, update flow, uninstall, `edit-funnel` usage, and notes for team/project installs.

- [ ] **Step 4: Write `edit-funnel`**

Document the `fgrove` edit workflow from target discovery through preview publish and verification, referencing the existing FunnelsGrove CLI skill without duplicating all command docs.

- [ ] **Step 5: Run validation**

Run: `bash tests/smoke.sh`

Expected: PASS.

## Chunk 3: Final Checks

### Task 3: Verify Worktree

**Files:**
- All changed files

- [ ] **Step 1: Check git diff**

Run: `git diff --check`

Expected: no whitespace errors.

- [ ] **Step 2: Check status**

Run: `git status --short`

Expected: only intended bootstrap files changed.
