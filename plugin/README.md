<img src="assets/icon.png" alt="FunnelsGrove" width="96">

# FunnelsGrove for Claude

**Your funnel growth team, inside Claude.** Build web2app subscription funnels, make them look like the best in the category, and keep improving them with A/B tests, all from one conversation.

- **Build from anything.** Start from a Figma file, a competitor's funnel, or a product idea. Claude turns it into a quiz-to-paywall funnel hosted on FunnelsGrove, with checkout, registration and subscription management included.
- **Design that converts.** Claude works from the public Funnel Screens library: 2,700+ real screens recorded from 79 top subscription funnels, with energy-screen patterns and proven paywall structures. Every screen gets a job, and the whole journey feels like one product.
- **Test the design before you launch.** Funnel QA reviews copy, mobile layouts, every branch, checkout and subscription flows, and reports evidence and clear blockers.
- **Run experiments and improve.** Give Claude a funnel and a period. It reads the analytics, flags the steps that lose users, proposes radically different variants, converges on one hypothesis per test, and hands you a shareable report to launch from.
- **Learn the playbook.** The full FunnelsGrove Web-to-Web course is built in: channels, unit economics, payments, analytics and experiments.

Works in Claude chat, **Cowork** and **Claude Code**. Research, copy, previews and the reference library work without an account; building, publishing and analytics use a [FunnelsGrove](https://funnelsgrove.com) account.

## Install

Add **FunnelsGrove** from the Claude directory, or in Claude Code:

```bash
claude plugin marketplace add The-Solid-Grove/fstack
claude plugin install funnelsgrove@fstack
```

Building, publishing and analytics need a FunnelsGrove account and the `fgrove` CLI (`npm install -g @funnelsgrove/cli`, then `fgrove login`).

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

## Use FunnelsGrove in Claude chat (connector)

The FunnelsGrove connector lets Claude work with your FunnelsGrove account from any Claude chat, on web, desktop and mobile, without the CLI: read analytics, compare periods and channels, run A/B experiments and study the reference library. This plugin declares the same connector, so its tools also appear in Claude Code.

**Connect:** add **FunnelsGrove** from the Claude directory, or go to Settings → Connectors → Add custom connector and enter `https://api.funnelsgrove.com/mcp`. Sign in to FunnelsGrove and approve access. You need a FunnelsGrove account with access to a workspace and project.

| Tool | What it does | Access |
| --- | --- | --- |
| `search_reference_funnels`, `get_reference_funnel` | Browse the public library of recorded funnels: screens, text and images | Read |
| `list_workspaces_and_projects`, `list_funnels`, `get_funnel`, `list_funnel_templates` | See your workspaces, projects, funnels and templates | Read |
| `get_funnel_analytics`, `compare_funnel_periods` | Visitors, paywall views, checkouts, subscriptions and revenue for a period, and what changed against the previous one | Read |
| `get_step_dropoff`, `list_traffic_sources` | Drop-off by step, overall or for one UTM source, campaign or ad set | Read |
| `list_domains` | Your production domains and the funnel each one serves | Read |
| `list_experiments`, `get_experiment_results` | Your A/B experiments, their results and a significance verdict per metric | Read |
| `create_funnel` | Create a hosted funnel from a template and save a brief (for example one Claude wrote from a Figma file or a competitor's funnel); customize the screens with the skills above in Claude Code | Write |
| `create_experiment`, `start_experiment` | Set up an A/B experiment and start or resume it | Write |
| `stop_experiment` | Pause a running experiment | Write, changes live traffic |
| `publish_funnel` | Publish a funnel to its preview link, or to a production domain | Write, changes live traffic |

Two ready-made prompts: **Funnel performance report** (what changed, weakest steps and channels, experiment verdicts, next actions) and **Plan A/B tests** (weak steps, proven reference funnels, test proposals).

Claude asks before it runs a write tool. Try: "Show me paywalls from fitness funnels in the reference library", "What changed in my funnel this week compared with last week?", "Which campaign converts best?", "Is my paywall test significant yet?".

To disconnect, remove the connector in Claude's settings. Sign-in grants expire automatically; data is handled under the [FunnelsGrove Privacy Policy](https://www.funnelsgrove.com/privacy).

## What this plugin contains, runs and connects to

This plugin contains only Markdown instructions, reference documents and images, plus `.mcp.json`, which declares the remote FunnelsGrove connector (`https://api.funnelsgrove.com/mcp`). It bundles no scripts, hooks, local MCP servers or background processes. The full skill pack in [The-Solid-Grove/fstack](https://github.com/The-Solid-Grove/fstack) adds optional helper scripts (a Playwright funnel walker for QA, a PDF report renderer, a reference-strip tool, a local workspace registry and preview CSS); each skill that would use one says so and works without it.

- **FunnelsGrove CLI.** Hosted work and the reference library use the `fgrove` CLI. When it is missing, a skill asks Claude to install it with `npm install -g @funnelsgrove/cli@latest` from the public npm registry.
- **FunnelsGrove services.** `fgrove references` reads the public Funnel Screens library at funnelsgrove.com without login. After you run `fgrove login`, the CLI sends the funnel source, copy, experiment and analytics requests you ask for to the FunnelsGrove API under your account. The CLI stores its own credentials on your machine; this plugin never reads them.
- **Local files.** Previews, design mockups, QA evidence and reports are written to your working folder.

The plugin itself collects no data. Data you send to FunnelsGrove is handled under the [FunnelsGrove Privacy Policy](https://www.funnelsgrove.com/privacy) and [Terms](https://www.funnelsgrove.com/terms).

## Privacy Policy

See the [FunnelsGrove Privacy Policy](https://www.funnelsgrove.com/privacy). Questions: open an [issue](https://github.com/The-Solid-Grove/fstack/issues).

## License

MIT. See [LICENSE](LICENSE).
