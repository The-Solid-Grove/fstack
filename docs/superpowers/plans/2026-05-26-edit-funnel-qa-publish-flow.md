# Edit Funnel QA Publish Flow Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the `edit-funnel` skill so agents local-preview first, ask before publishing, run preview QA, then publish production and run production QA.

**Architecture:** Keep this as documentation-driven workflow guidance because `fstack` is a skill pack. Use smoke assertions to prevent the key workflow gates from regressing.

**Tech Stack:** Markdown skills/docs, Bash smoke tests.

---

## Chunk 1: Workflow Documentation And Smoke Coverage

### Task 1: Add failing smoke assertions

**Files:**
- Modify: `tests/smoke.sh`

- [ ] **Step 1: Write the failing smoke assertions**

Add assertions in `check_skill` for these required concepts:

```bash
assert_contains "$skill/SKILL.md" 'local preview'
assert_contains "$skill/SKILL.md" 'Ask the user whether to publish'
assert_contains "$skill/SKILL.md" 'preview URL'
assert_contains "$skill/SKILL.md" 'production URL'
assert_contains "$skill/SKILL.md" 'submit email|add.*email'
assert_contains "$skill/SKILL.md" 'test payment|payment path'
assert_contains "$skill/SKILL.md" 'larger discount'
assert_contains "$skill/SKILL.md" '/manage-subscription'
assert_contains "$skill/SKILL.md" 'cancellation flow'
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/smoke.sh`

Expected: FAIL because the current skill does not yet contain the new QA and publish gate wording.

### Task 2: Update skill workflow

**Files:**
- Modify: `skills/edit-funnel/SKILL.md`

- [ ] **Step 1: Implement the workflow text**

Update `Workflow` so the path is: edit, local preview, adjust, repeat local preview, ask whether to publish, publish preview, run QA, publish production when explicitly requested, run production QA.

- [ ] **Step 2: Add the QA checklist**

Add full QA bullets for email, test payment, close/reopen checkout for larger discount, and `/manage-subscription` cancellation.

- [ ] **Step 3: Tighten completion gate**

Require local preview verification before publish, preview QA after preview publish, and production QA after production publish.

- [ ] **Step 4: Run smoke test**

Run: `bash tests/smoke.sh`

Expected: PASS.

### Task 3: Update README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update the usage sequence**

Make the documented flow match the skill: local preview first, ask whether to publish, preview QA, then production publish and production QA when requested.

- [ ] **Step 2: Run smoke test**

Run: `bash tests/smoke.sh`

Expected: PASS.
