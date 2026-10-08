<img src="assets/web-to-web-growth.png" alt="Skills for Web-to-Web Growth" width="50%">

# Skills for Web-to-Web Growth

Agent skills for researching, writing, and building subscription web funnels.

A good funnel connects the ad promise, the questions, the offer, and the product. **fstack** gives your agent a set of focused practices for working on each part.

Use them together or pick the one you need. Read the instructions, adapt them to your product, and make them your own.

Works with **Codex** and **Claude Code**. The course covers Web-to-Web growth; copy and previews can be used independently. Building and hosted editing use **FunnelsGrove**.

## Installation

```bash
git clone https://github.com/The-Solid-Grove/fstack.git ~/.fstack
cd ~/.fstack
./setup --host auto --skip-fgrove-cli
```

Requires Git and Bash. Keep the checkout: the installer links your agent's skills to these files. The first fstack skill used in a conversation updates a clean `main` checkout to the latest release automatically; custom branches and local changes are left alone and an update is offered instead.

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

## Put them to work

**Research → Write → Preview copy → Design → Build → QA → Iterate**

Start wherever your project is. For example:

```text
Use writing-funnel-copy to plan a quiz-to-paywall funnel for my product.
Start with the product, audience, and ad promise. Then use preview-funnel
to make the approved copy clickable for review.
```

[Sample requests](docs/sample-requests.md) · [Setup and maintenance](docs/getting-started.md) · [Funnel QA](skills/qa-funnel/SKILL.md)

---

By [The Solid Grove](https://github.com/The-Solid-Grove). Inspired by the focused, adaptable approach of [Matt Pocock's skills](https://github.com/mattpocock/skills).
