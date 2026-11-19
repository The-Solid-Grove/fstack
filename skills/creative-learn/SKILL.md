---
name: creative-learn
description: "Use when ad test results are in and should be recorded in FunnelsGrove Creatives: the result on each launched Variation, the status and lessons of each Angle, finished Concepts, and the winners worth mixing next."
---

# Creative Learn

Before the first fstack skill in a conversation, run the [update check](https://github.com/The-Solid-Grove/fstack/blob/main/docs/getting-started.md#agent-update-check): in a git checkout it applies a safe update automatically; reread this file if it reports `updated`, and offer any update it could not apply without blocking the task. Skills installed with the skills CLI (`npx skills add`) have no checkout: skip the check and continue.

Close the loop: write what the tests showed where the next brainstorm will read it. A result that stays in an ads manager or a chat teaches nobody.

The work needs the `fgrove` CLI connected to the account and the Creatives Platform. Every command takes `--project <project>` and prints JSON.

## 1. Get the results

Ask the person for the numbers per ad for the period: spend, purchases or the event they judge by, and the dates. Take an export, a table or a screenshot. Read an ads account yourself only when the person connected one for you. The ad name is the Variation's name (it is the ad's `utm_content`).

Ask once for the rule that decides **Go**, **No Go** and **winner** (for example a cost per purchase under a target after a minimum spend) and use theirs. Apply the same rule to every ad.

**Done when** every launched Variation without a result has its numbers or is named as still running.

## 2. Record each Variation

```bash
fgrove creatives variations list
fgrove creatives variations update <variation> --launched true --result go --comment "TEST 12–18 Nov: $412 spend, 19 purchases, CPA $21.7"
```

Set `--launched`, `--result` (`go` or `no_go`) and `--winner` by the rule, and put the numbers with their dates in the comment. Read the comment before you write: add to it, keep what is there. `fgrove creatives variations update --help` lists the exact options.

## 3. Record each Angle

```bash
fgrove creatives angles update <angle> --status working --notes "<what the tests showed>" --iteration-ideas "<what to try next>"
```

An Angle's status follows its Variations: working while something wins, burned out when winners stop, failed after enough clean tries, under review while results are thin. Write the lesson as a sentence a stranger could act on: what was shown, to whom, and what happened.

## 4. Close the Concepts

A Concept whose Variations all have a result is done:

```bash
fgrove creatives concepts update K012 --stage done
```

## 5. Name what to make next

Give the person three short lists: winners worth an iteration and the part to change; working Angles with nothing in Ideas or Scripts; and what the losers have in common. Offer [creative-brainstorm](../creative-brainstorm/SKILL.md) for the first two. Stop here: what to make next is theirs.
