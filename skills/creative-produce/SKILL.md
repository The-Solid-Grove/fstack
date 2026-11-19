---
name: creative-produce
description: "Use when an approved ad Concept in FunnelsGrove Creatives is to be produced into finished videos or images, or when open notes on delivered creatives are to be applied: the board, the takes, the cut, and the revision that answers each note with what changed."
---

# Creative Produce

Before the first fstack skill in a conversation, run the [update check](https://github.com/The-Solid-Grove/fstack/blob/main/docs/getting-started.md#agent-update-check): in a git checkout it applies a safe update automatically; reread this file if it reports `updated`, and offer any update it could not apply without blocking the task. Skills installed with the skills CLI (`npx skills add`) have no checkout: skip the check and continue.

Make the ads people approved, and change the ones they sent back. You are judged on two things: the videos have no bloopers, and the person spent minutes, not hours.

The work needs the `fgrove` CLI connected to the account, the Creatives Platform and Creative Credits on the workspace. Every command takes `--project <project>` and prints JSON. Everything paid goes through the platform and its credits: clips, keyframes, voices and music.

## 1. Find the work

```bash
fgrove creatives inbox
```

- `agent.produce`: Concepts whose script a person approved. Go to **Produce**.
- `agent.variationNotes`, `agent.montageNotes`: open notes on delivered work. Go to **Revise**.
- `agent.scripts` and `agent.conceptNotes` belong to [creative-script](../creative-script/SKILL.md).

Take what the person named, else notes before new productions: an ad waiting on one fix is closer to a test than an ad not started.

## 2. Produce

The procedure ships in the CLI at the version of its commands. Read it and follow it step by step:

```bash
fgrove creatives montage guide
```

Around that procedure, hold four things:

1. **The Concept.** Read it (`fgrove creatives concepts show K012`) and start every Generation with `--concept K012`. The first one moves the Concept into production, and its videos land on the Concept's page.
2. **Stills before clips.** Make the board first (`montage start --keyframes-only`). A keyframe costs a tenth of a clip, and the story is judged on it.
3. **Gates.** Stop and show the person the work at the board (nothing else is paid before it passes) and at the rough cut (after it the lengths are frozen). One message: what to look at, how long it takes, the questions, your recommendation. Skip a gate only when the person said so.
4. **Money.** State the estimate before the board and the running total after every step. Ask before a video passes the amount the person set.

Approve the finished outputs into the Concept's Creative (`fgrove creatives generations approve`). Launching ads is the person's.

**Done when** the videos are Variations in Review, each checked against the guide's blooper list, and the report says what each gate decided and what was spent.

## 3. Revise

Each open note is a change to make. For each one:

1. **Locate it.** A note on a Variation names its Generation; a note on a Montage names its Shot, or none for the whole video. Open that Montage (`fgrove creatives montage show <generationId>`).
2. **Choose the smallest change that answers it.** Words on screen, subtitles, order and length change for the price of assembly. A wrong picture or movement needs a new take of that Shot; a wrong line needs a new take or a voice. Leave every other Shot as it is.
3. **Build it.** `fgrove creatives montage revise <generationId>` writes the cut sheet that reuses everything delivered; change only what the notes ask and start it. One build may answer several notes.
4. **Check it.** Compare the new render with the old one Shot by Shot: only the changed Shots differ.
5. **Deliver it.** Before replacing a Variation's file, read its `comment` and `launched`. A launched file is never replaced: put the new render beside it and tell the person.
6. **Close the note** with what changed and where to see it:

```bash
fgrove creatives notes done <noteId> --variation <variation name> --reply "New take: the phone lights up after she lifts it. Build 3."
fgrove creatives notes done <noteId> --generation <generationId> --reply "Music at 30%. Build 3."
```

A note you cannot act on stays open: ask the person what it means, in one question.

**Done when** every note you took is closed with a reply or asked about, and the person has one list: note, change, build, credits.

## Limits

- A brand's footage, ads and results go only to FunnelsGrove's generation providers.
- Call a thing checked only when a number measured it or a person saw it.
