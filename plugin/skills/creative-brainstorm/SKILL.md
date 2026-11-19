---
name: creative-brainstorm
description: "Use when planning new ad creatives for a FunnelsGrove project: new Concepts for its Angles from the product, the audience and past results, or mixes and iterations of the Variations that won. Saves Concepts (hook, format, how it is made) for a person to pick."
---

# Creative Brainstorm

Before the first fstack skill in a conversation, run the [update check](https://github.com/The-Solid-Grove/fstack/blob/main/docs/getting-started.md#agent-update-check): in a git checkout it applies a safe update automatically; reread this file if it reports `updated`, and offer any update it could not apply without blocking the task. Skills installed with the skills CLI (`npx skills add`) have no checkout: skip the check and continue.

Fill a project's **Ideas** with Concepts worth producing. A Concept is one planned ad under an Angle: a hook, a format and how it will be made. Everything here is free: no image, video or credit is spent, and nothing is produced until a person picks a Concept and approves its script.

The work needs the `fgrove` CLI connected to the account and the Creatives Platform, which FunnelsGrove switches on per workspace. Every command below takes `--project <project>` and prints JSON.

Two requests arrive here. **New**: Concepts for Angles from the product and the audience. **Mix**: Concepts recombined from the Variations that won ("mix the winners", "iterate on what works"). Pick the branch from the request; when it names neither, do Mix if the project has winners and New for the Angles it leaves uncovered.

## 1. Read the ground

```bash
fgrove creatives angles list        # status, counts of launched / Go / winners, key elements, iteration ideas, notes
fgrove creatives variations list    # hooks, format, launched, test_result, winner, comment
fgrove creatives concepts list      # what is already planned, produced or dropped
fgrove creatives brand-kits list    # tone and what to avoid, per brand
```

Read the product itself (its funnel or site) and look at the winners' files, not only their names. Ask the person only what these do not answer.

**Done when** you can name: the working Angles and what their winners have in common; the Angles with nothing in Ideas or Scripts; what failed and why, from the comments; and every Concept already planned or dropped, so none is proposed twice.

## 2. Diverge

**New.** For each chosen Angle write three Concepts that disagree about the **mechanism**: who speaks, what is shown in the first second, what proves the claim. Three wordings of one idea are one Concept.

**Mix.** Take the winners apart into hook (the first three seconds), body (the demonstration or the story), format (UGC, drama, voice-over, static) and Angle. Recombine one part at a time, so a result can be read later:

- the hook of one winner on the body of another;
- a winner's body in another format;
- a winner's hook on an Angle not tested with it;
- one winner with a single part changed (an **iteration**).

Ad platforms may treat near-identical ads as one. Make the set differ in theme, persona or format, not in wording.

**Done when** each Concept changes a named part and no two differ only in words.

## 3. Save the Concepts

For each Concept: a title of at most six words, the hook as it will be said or shown, the format code from the project's dictionary, how it is made in a few words ("UGC, 30 s"), and where it came from.

```bash
fgrove creatives concepts create --angle C005 --title "The drawer challenge" --format vd \
  --hook "I locked my phone in a drawer for seven nights." --treatment "UGC, 30 s" \
  --source mix --origin <winner variation name> <other variation name>
```

`--source` is `brainstorm`, `mix` or `iteration`; a mix or an iteration names its Variations with `--origin`. A Concept needs an Angle: search first (`fgrove creatives angles search "<idea>"`), and create a new Angle as an idea only when none fits (`angles create --status idea`).

**Done when** every Concept is saved and has its code (`K012`).

## 4. Hand over

Give the person one table: code, title, Angle, hook, what it changes and why it should work. Say that picking and dropping is theirs, on the Concepts page of Creatives, and that a picked Concept goes to [creative-script](../creative-script/SKILL.md). Stop here.
