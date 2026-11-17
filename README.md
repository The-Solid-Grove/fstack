<img src="assets/web-to-web-growth.png" alt="Skills for Web-to-Web Growth" width="50%">

# FunnelsGrove for Claude

**Your funnel growth team, inside Claude.** Build web2app subscription funnels, make them look like the best in the category, and keep improving them with A/B tests, all from one conversation.

- **Build from anything.** Start from a Figma file, a competitor's funnel, or a product idea. Claude turns it into a quiz-to-paywall funnel hosted on FunnelsGrove, with checkout, registration and subscription management included.
- **Design that converts.** Claude works from the public Funnel Screens library: 2,700+ real screens recorded from 79 top subscription funnels, with energy-screen patterns and proven paywall structures. Every screen gets a job, and the whole journey feels like one product.
- **Test the design before you launch.** Funnel QA reviews copy, mobile layouts, every branch, checkout and subscription flows, and reports evidence and clear blockers.
- **Run experiments and improve.** Give Claude a funnel and a period. It reads the analytics, flags the steps that lose users, proposes radically different variants, converges on one hypothesis per test, and hands you a shareable report to launch from.
- **Learn the playbook.** The full FunnelsGrove Web-to-Web course is built in: channels, unit economics, payments, analytics and experiments.

Works in **Claude Code**, **Cowork** and **Codex**. Research, copy, previews and the reference library work without an account; building, publishing and analytics use a [FunnelsGrove](https://funnelsgrove.com) account.

## Installation

As a Claude plugin, from the Claude directory, or in Claude Code:

```bash
claude plugin marketplace add The-Solid-Grove/fstack
claude plugin install funnelsgrove@fstack
```

With the [skills CLI](https://skills.sh):

```bash
npx skills add The-Solid-Grove/fstack
```

Or from a git checkout that keeps itself up to date:

```bash
git clone https://github.com/The-Solid-Grove/fstack.git ~/.fstack
cd ~/.fstack
./setup --host auto --skip-fgrove-cli
```

The checkout route requires Git and Bash. Keep the checkout: the installer links your agent's skills to these files. The first fstack skill used in a conversation updates a clean `main` checkout to the latest release automatically; custom branches and local changes are left alone and an update is offered instead. Skills installed with the skills CLI are updated with `npx skills update`.

[Host options, FunnelsGrove setup, and updates →](docs/getting-started.md)

## The skills

### [Web-to-Web Essentials](skills/web2app-essentials/SKILL.md)

**Understand what to work on.** The [FunnelsGrove course](https://funnelsgrove.com/learn/web2web), available as text for your agent. Learn the full system or ask about acquisition, economics, onboarding, payments, and experiments. Invoke it as `web2app-essentials`.

### [writing-funnel-copy](skills/writing-funnel-copy/SKILL.md)

**Give every screen a job.** Turn your product, audience, and ad promise into a quiz-to-paywall story with an energetic rhythm: easy questions broken up by energy screens that reassure, prove, and excite, then a plan reveal, email, and a paywall cloned from a proven structure. Built on reference funnels from the public Funnel Screens library, a data-derived rhythm template, an energy screen catalog, and paywall blueprints. Improve a single screen or review an offer within its existing scope.

### [preview-funnel](skills/preview-funnel/SKILL.md)

**Feel the flow before building it.** Turn finished copy into a temporary clickable mockup. Review the questions, pacing, and calls to action in a local preview before committing to implementation.

### [design-funnel](skills/design-funnel/SKILL.md)

**Make the whole journey feel coherent.** Reuse `Design.md`, approved strategy and emotional arc, and complete copy. Compare similar screens from an inspected reference funnel, keep a distinct composition per energy screen, clone the paywall's section structure from its reference, show the first three actual designs for feedback, then complete the pattern set and implement/review the journey. Reference discovery uses the public `fgrove references` library (no login); otherwise continue with supplied references and `Design.md`.

### [create-funnel](skills/create-funnel/SKILL.md)

**Start from the right template.** Use your connected `fgrove` account to choose one of three templates, create a hosted funnel, download its source, and establish the product brief and `Design.md` before customization.

### [edit-funnel](skills/edit-funnel/SKILL.md)

**Improve the funnel you already have.** Reuse its remembered working folder, preserve local changes while refreshing source, and work through preview and QA. Publishing follows the target and environment you authorize.

### [qa-funnel](skills/qa-funnel/SKILL.md)

**Check the whole experience.** Review screen images, rendered design, mobile layouts, every branch, checkout, registration, and subscription management. Run it independently or verify the funnel after publishing, with evidence and clear blockers.

### [brainstorm-funnel-tests](skills/brainstorm-funnel-tests/SKILL.md)

**Turn analytics into recommendations and the next tests.** Give it the funnel and a period. It reads the dashboard's metrics, picks one focus area (first step, quiz or paywall), flags steps that lose more than 7% (20% for email), grills you on scope in short rounds, prototypes several radically different ideas for each test, converges on one variant and hypothesis per step with you, and renders a shareable PDF: recommendations first, then metrics, focus, drop-off, and current versus proposed screen on one page per test.

## Put them to work

**Research → Write → Preview copy → Design → Build → QA → Brainstorm tests → Iterate**

Start wherever your project is. For example:

```text
Use writing-funnel-copy to plan a quiz-to-paywall funnel for my product.
Start with the product, audience, and ad promise. Then use preview-funnel
to make the approved copy clickable for review.
```

[Sample requests](docs/sample-requests.md) · [Setup and maintenance](docs/getting-started.md) · [Funnel QA](skills/qa-funnel/SKILL.md)

## What the plugin runs and connects to

The plugin is a set of skills: Markdown instructions plus readable helper scripts that Claude runs only while a skill needs them. It declares no hooks, background processes or MCP servers.

- **FunnelsGrove CLI.** Hosted work and the reference library use the `fgrove` CLI. When it is missing, a skill asks Claude to install it with `npm install -g @funnelsgrove/cli@latest` (from the public npm registry).
- **FunnelsGrove services.** `fgrove references` reads the public Funnel Screens library at funnelsgrove.com without login. After you run `fgrove login`, the CLI sends the funnel source, copy, experiment and analytics requests you ask for to the FunnelsGrove API under your account. Credentials are stored by the CLI on your machine, never in this plugin.
- **GitHub.** A git checkout of this repository checks GitHub for a newer `main` once per conversation (`scripts/check-fstack-update`). Plugin and skills-CLI installs have no checkout and skip the check.
- **Local tools.** Previews, design mockups, QA evidence and reports are written to your working folder. `qa-funnel` drives headless Chromium through Playwright against the funnel URL you choose; if Playwright is missing it asks you to install it in your QA folder. `brainstorm-funnel-tests` renders its PDF with a local Chrome.

The plugin itself collects no data. Data you send to FunnelsGrove is handled under the [FunnelsGrove Privacy Policy](https://www.funnelsgrove.com/privacy) and [Terms](https://www.funnelsgrove.com/terms).

## Privacy Policy

See the [FunnelsGrove Privacy Policy](https://www.funnelsgrove.com/privacy). Questions: open an [issue](https://github.com/The-Solid-Grove/fstack/issues).

---

By [The Solid Grove](https://github.com/The-Solid-Grove). Inspired by the focused, adaptable approach of [Matt Pocock's skills](https://github.com/mattpocock/skills).
