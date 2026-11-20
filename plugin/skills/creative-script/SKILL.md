---
name: creative-script
description: "Use when a picked ad Concept in FunnelsGrove Creatives needs its script, or a person's own script needs to become scenes with seconds and a credit estimate before production. Saves the script on the Concept for the person to approve."
---

# Creative Script

Before the first fstack skill in a conversation, run the [update check](https://github.com/The-Solid-Grove/fstack/blob/main/docs/getting-started.md#agent-update-check): in a git checkout it applies a safe update automatically; reread this file if it reports `updated`, and offer any update it could not apply without blocking the task. Skills installed with the skills CLI (`npx skills add`) have no checkout: skip the check and continue.

Turn a Concept into a script a person can approve in two minutes: scenes with their seconds, pictures, lines and words on screen, and what producing it will cost. Writing is free; nothing is generated here.

The work needs the `fgrove` CLI connected to the account and the Creatives Platform. Every command takes `--project <project>` and prints JSON.

## 1. Find the work

```bash
fgrove creatives inbox                # agent.scripts: picked Concepts without a script; agent.conceptNotes: open notes on scripts
fgrove creatives concepts show K012   # the Concept with its hook, format, origin and script
```

Take the Concept the person named, else every entry of `agent.scripts`, oldest first.

## 2. Read before writing

The Concept's Angle (`fgrove creatives angles get <angle>`), the Variations it builds on (look at their files), the brand's kit, and the product screens the ad shows. A script the person pasted is theirs: keep its words and order, and change only what cannot be produced or said.

**Done when** you know the one promise of the ad, who speaks, and what the first three seconds show.

## 3. Choose the cheapest way to make it

Plates of words over pictures with music; a narrator over pictures; people who speak on camera. Each step up costs more and takes longer, because every speaking take can go wrong. Use the cheapest one the idea survives, and say which.

## 4. Write the scenes

One line per scene: its number and seconds, the picture, the voice (the exact line and who says it) and the words on screen. Rules that keep it producible:

- The hook is scene 1 and fits in three seconds.
- One action per scene; a scene of 2 to 5 seconds.
- A claim is one the product can back; say "faster", not a number nobody measured.
- The last scene is the end card with the offer.
- Hooks to test go under the body as variants, each replacing scene 1.

Put two lines above the scenes: the total length, and the estimate (generated clips, keyframes, voices and music at the project's prices; `fgrove creatives credits` shows the balance).

**Done when** the scenes add up to the length, every line has a speaker, and the estimate is stated.

## 5. Save and answer

```bash
fgrove creatives concepts update K012 --script-file script.md
fgrove creatives notes done <noteId> --concept K012 --reply "Scene 4 says 'faster' now."
```

Saving a script moves an idea to the script stage. Close each open note on the Concept that the new script answers, with what changed.

## 6. Hand over

Give the person the Concept's code and three lines: the way it is made, the length and the estimate. Approving is theirs, on the Concept's page. Production waits for it and belongs to [creative-produce](../creative-produce/SKILL.md).
