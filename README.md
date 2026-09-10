![An illustrated journey from a web ad through a quiz and paywall to a growing mobile app](assets/web-to-app-growth.png)

# fstack — Skills for Web-to-App Growth

Agent skills for the work between an ad click and an app subscriber.

Building a funnel means making a lot of connected decisions. What did the ad promise? What should the quiz ask? When has the user seen enough value to pay? And does the whole thing work on their phone?

**fstack gives your agent a workflow for each part:** research the market, write the copy, click through a prototype, build the funnel, and improve it. Five skills, with supporting research and checklists you can read and adapt. Use the one you need, or work through them together.

Built for growth teams, marketers, and builders using **Codex or Claude Code**. Research and copy can be used independently; building and hosted editing use **FunnelsGrove**.

[Install](#install) · [Explore the skills](#the-skills) · [See the workflow](#how-the-skills-fit-together) · [Contribute](#develop)

## Install

Clone the pack and link the skills to your agent:

```bash
git clone https://github.com/The-Solid-Grove/fstack.git ~/.fstack
cd ~/.fstack
./setup --host auto --skip-fgrove-cli
```

Choose a single agent with `--host codex` or `--host claude`. Auto detects installed agent commands and falls back to both when neither is found.

The installer creates symlinks in `~/.codex/skills/` and/or `~/.claude/skills/`. Keep the checkout: those links point to its files. Re-running setup refreshes the links.

For research and copy, you need Git, Bash, and your agent. For clickable previews, the bundled workflow also uses Python 3 and browser access.

<details>
<summary><strong>Building or editing with FunnelsGrove</strong></summary>

Hosted work also needs Node.js 18+, npm, and access to FunnelsGrove:

```bash
npm install -g @funnelsgrove/cli
fgrove login
```

Run `./setup --host auto` without `--skip-fgrove-cli` to check and update the global CLI against npm as part of setup.

`create-funnel` needs access to a FunnelsGrove monorepo checkout containing `apps/funnel-template`. The published CLI does not include that template. The skill helps locate the checkout before scaffolding.

</details>

Then give your agent a task:

```text
Use writing-funnel-copy to plan a quiz-to-paywall funnel for my app.
Start by asking about the product, audience, ad promise, and screen count.
```

## The skills

| Skill | Reach for it when… | What you get |
| --- | --- | --- |
| [web2app-essentials](skills/web2app-essentials/SKILL.md) | You need to understand the economics or choose what to investigate. | Answers grounded in the bundled research, with benchmarks, sources, and caveats. |
| [writing-funnel-copy](skills/writing-funnel-copy/SKILL.md) | You need to turn a product and an ad promise into a convincing flow. | Funnel strategy, screen-by-screen copy, paywall structure, and experiment ideas. |
| [preview-funnel](skills/preview-funnel/SKILL.md) | You want to feel the flow before building it. | A temporary, clickable local mockup for reviewing copy and pacing. |
| [create-funnel](skills/create-funnel/SKILL.md) | You are starting a new FunnelsGrove funnel. | A branded project scaffolded from the funnel template and checked locally. |
| [edit-funnel](skills/edit-funnel/SKILL.md) | You need to change an existing hosted funnel. | A local edit, preview, QA, and publishing workflow. |

### Understand the funnel before changing it

**[web2app-essentials](skills/web2app-essentials/SKILL.md)** covers acquisition, creatives, onboarding, experiments, pricing, payments, analytics, growth process, and compliance. It routes questions to the relevant research instead of loading the whole library. Ask a specific question, or use it to learn web2app module by module.

```text
Use web2app-essentials to explain how to diagnose drop-off between
onboarding and purchase. Separate benchmarks from assumptions and
show which events we would need to measure.
```

### Give every screen a job

**[writing-funnel-copy](skills/writing-funnel-copy/SKILL.md)** starts with your product, audience, entry promise, and screen count. It works through the story, questions, proof, and offer before returning a screen-by-screen spec. The supporting library includes a psychology framework, paywall guidance, and funnel teardowns.

```text
Use writing-funnel-copy for a language-learning app aimed at busy adults.
The ad promises practice for real conversations. Ask for the missing
product context, then draft the flow, paywall, and A/B test ideas.
```

### Read the copy by clicking through it

**[preview-funnel](skills/preview-funnel/SKILL.md)** turns finished copy into a small local HTML/CSS/JS mockup. A warm paper-and-copper design keeps the screens pleasant to review. Tap through choices, check the pacing, and see whether the headline and sticky CTA fit on a phone.

```text
Use preview-funnel to turn this screen-by-screen copy into a clickable
local mockup. Check every screen and leave it open for copy review.
```

The mockup is temporary. It is a review artifact; building the product is a separate step.

### Start with a working funnel template

**[create-funnel](skills/create-funnel/SKILL.md)** scaffolds from the FunnelsGrove template, applies your branding, installs dependencies, and checks the flow locally. The template includes quiz screens, email capture, paywall variants, and subscription management.

```text
Use create-funnel to start a funnel for my language-learning app.
Use the approved copy and brand assets, then verify the full local flow.
```

### Improve the funnel you already have

**[edit-funnel](skills/edit-funnel/SKILL.md)** syncs the existing funnel, reads its project contract, and works through changes with local preview and QA. It accounts for local changes and GitHub sync before refreshing the draft, then checks preview coverage before production publishing.

```text
Use edit-funnel for <workspace>/<project>/<funnel>. Update the onboarding
with this approved copy, check every branch in local preview, and report
what is ready to publish.
```

## How the skills fit together

**Research → Write → Preview → Build → Iterate**

Start with `web2app-essentials` to frame a question. Use `writing-funnel-copy` to turn the product context into screens, then `preview-funnel` to review them. Build with `create-funnel`, or use `edit-funnel` when the funnel already exists.

You can enter at any point. An existing funnel may only need a copy review. A new teammate may only need the research library.

<details>
<summary><strong>What the build and edit workflows check</strong></summary>

- **Project contract.** The synced project's `AGENTS.md` and `docs/funnelsgrove/START-HERE.md` define implementation behavior. Research teardowns supply ideas; the managed docs govern metadata, answers, routing, and analytics. Run `fgrove validate` before preview, sync, or publish.
- **Screen fit.** Run a content-fit audit in local preview at small `375x667`, medium `393x852`, large `402x874`, and desktop-small `1280x800`.
- **Complete flow.** Cover every step, branch, and active A/B experiment, including paywall discounts, checkout, wallet buttons, registration, required links, and cancellation when a test subscription is available.
- **Publishing.** Ask whether to publish. Verify the production candidate has a matching preview build, complete preview QA before production publish, and run production QA after an explicitly requested production publish.
- **Image performance.** Keep AVIF/WebP generation enabled and verify the image-variant stage. Use manifest-driven next-step image preloading.
- **Readable URLs.** Use meaningful route slugs for public screens, rather than `/step-1` paths.

See the [full funnel QA checklist](docs/funnel-qa-checklist.md) and the [edit workflow](skills/edit-funnel/SKILL.md) for the exact steps.

</details>

## Update

```bash
cd ~/.fstack
git pull --ff-only
./setup --host auto --skip-fgrove-cli
```

Because the skills are linked, pulling updates changes the installed files. Commit your own adaptations before updating. Omit `--skip-fgrove-cli` when you also want setup to check and update the CLI.

## Team setup

Each teammate installs the pack. Add a short pointer to your project's `AGENTS.md` or `CLAUDE.md`:

```markdown
Use fstack for web-to-app funnel work: web2app-essentials for research,
writing-funnel-copy for strategy and screen copy, preview-funnel for
clickable copy review, create-funnel for new FunnelsGrove projects,
and edit-funnel for hosted changes. Read the matching SKILL.md and
follow the project's managed FunnelsGrove docs for implementation.
```

## Uninstall

Remove the installed symlinks first. This preserves directories if you replaced a link with your own copy:

```bash
for host in ~/.codex/skills ~/.claude/skills; do
  for skill in create-funnel edit-funnel preview-funnel writing-funnel-copy web2app-essentials; do
    link="$host/$skill"
    if [ -L "$link" ] && [ "$(readlink "$link")" = "$HOME/.fstack/skills/$skill" ]; then
      rm "$link"
    fi
  done
done
```

If you used a different checkout path, substitute it in the target check. You can then remove the checkout once you have saved any changes you want to keep.

## Develop

Each skill has a `skills/<name>/SKILL.md` entry point. Supporting research, examples, and styles live beside it in `references/`; Codex interface metadata lives in `agents/openai.yaml`.

Keep entry points focused on when to act, what to read, and what completion means. Put detailed material in linked references so it is loaded when the task needs it.

Run the smoke checks or every available suite:

```bash
bash tests/smoke.sh

# All suites, including research and reference audits
for suite in tests/*.sh; do
  bash "$suite" || exit "$?"
done
```

Current version: `0.5.8`

---

Made by [The Solid Grove](https://github.com/The-Solid-Grove). README organization inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills): focused practices you can understand, adapt, and combine.
