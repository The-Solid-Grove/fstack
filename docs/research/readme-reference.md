# README reference: Matt Pocock's skills

Reviewed 2026-09-10. Reference snapshot: `mattpocock/skills` at
`3cca18b368ae95cdbdebbff572ccafa662551015`. fstack baseline:
`d53eeb296bb19a49ec806db20fe3417e266f4f5a`.

## What the reference does

The README opens with theme-aware artwork, a clear audience title, a short
point of view, and installation. It explains practical failure modes before
ending with a linked skill directory. Its organizing idea is small,
composable practices. The useful lesson for fstack is that a visitor sees the
purpose and first action before operational detail. This is an editorial
interpretation of the [reference README](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/README.md).

The repository groups skills by discipline and keeps supporting material near
each skill. For example, the prototype entry routes to separate logic and UI
guides. This gives the main entry a clear job while readers load the detail
needed for their branch. Sources: [skill tree](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills),
[prototype entry](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/prototype/SKILL.md).

## What fstack already supports

fstack has five complementary skills: funnel research and learning, copy,
temporary previews, scaffolding, and hosted editing. Its current README mixes
the directory and installation with detailed publishing and image-handling
rules. Sources: [baseline README](https://github.com/The-Solid-Grove/fstack/blob/d53eeb296bb19a49ec806db20fe3417e266f4f5a/README.md),
[skill directory](https://github.com/The-Solid-Grove/fstack/tree/d53eeb296bb19a49ec806db20fe3417e266f4f5a/skills).

The existing split between compact entries and adjacent references already
fits the reference's composable approach. Preserve it. `web2app-essentials`
explicitly owns educational reference, while `writing-funnel-copy` owns copy
and strategy; implementation is routed through the funnel workflow skills.
Sources: [knowledge skill](../../skills/web2app-essentials/SKILL.md),
[copy skill](../../skills/writing-funnel-copy/SKILL.md).

## Recommended README

The user confirmed the title below; the remaining items are editorial recommendations:

1. Open with an original banner and **Skills for Web-to-App Growth**, the
   title confirmed by the user. Use a concrete subtitle covering quiz
   funnels, copy, paywalls, and the journey from an ad click to a subscriber.
2. Give the reader two short paragraphs on the practical outcome and how the
   skills work together. Avoid revenue promises or claims of guaranteed lift.
3. Put a linked five-row skill table above the fold: skill, when to use it,
   and what it produces.
4. Show the current checkout-based installation, then one first prompt.
   Keep host selection, updates, uninstall, and contributor instructions
   accessible in compact sections or a linked setup guide.
5. Explain the workflow as research → copy → preview → build → iterate.
   Make clear that each skill can also be used independently.
6. Give each skill a brief outcome description and one copyable prompt.
   Link authoritative workflow and QA documents for operational detail.
7. Credit the organizational inspiration with a plain link to Matt's repo.
   Use original artwork and wording.

The installation examples must reflect fstack's actual installer, including
its optional CLI check. Matt's marketplace commands are specific to his
distribution and should not be borrowed without implementation and testing.
Source: [fstack setup](../../setup).

## Warranted structure ideas

- Keep the current `skills/<name>/SKILL.md` layout for five skills. A larger
  categorized hierarchy adds migration cost without helping this small set.
- Retain topic-specific references and link directly to the relevant file
  from each entry; the knowledge skill already has a useful routing table.
- Keep user-facing skill summaries in the README and authoritative execution
  rules in skill files and the [QA checklist](../funnel-qa-checklist.md).
- Consider a short skills index only if the catalog grows enough that the
  README table stops being sufficient. No new router skill or setup workflow
  is needed merely to imitate the reference.
