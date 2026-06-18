---
name: preview-funnel
description: Use when Codex needs to turn finished funnel copy, screen-by-screen funnel specs, PLAN.md sections, or research-derived funnel copy into a temporary clickable local mockup for copy review, especially before committing to final design or FunnelsGrove implementation.
---

# Preview Funnel

## Overview

Build a simple, temporary click-through that makes funnel copy easy to read,
tap through, and critique. Favor plain static HTML/CSS/JS, one reusable screen
renderer, and low-fidelity building blocks over production design.

## Workflow

1. Find the source copy: `PLAN.md`, screen-by-screen spec, content files, or
   research notes. Record the source path in the mockup UI.
2. Create the preview outside tracked source, preferably:

   ```bash
   preview_dir="$(mktemp -d "${TMPDIR:-/tmp}/preview-funnel.XXXXXX")"
   ```

   Use a repo `.tmp/` directory only when the project already ignores it. Do
   not leave product-specific mockups in the repo unless the user asks to save
   them.
3. Build the smallest useful static app:
   - `index.html` for the shell
   - `styles.css` for low-fidelity mobile layout
   - `steps.mjs` or `steps.json` for copy data
   - `app.mjs` for navigation and choice state
4. Render one reusable mobile screen: progress header, headline, support copy,
   optional choice cards, optional notes/proof rows, and a sticky bottom CTA.
5. Keep visuals deliberately simple: boxes, labels, neutral colors, and clear
   spacing. The goal is copy flow review, not final design approval.
6. Start a local server from the temporary directory:

   ```bash
   cd "$preview_dir" && python3 -m http.server 5177
   ```

   If the port is busy, choose another available port and report the actual URL.
7. Open the URL in the browser. If the Browser plugin is available, use it for
   local preview and verification.
8. Click through the whole flow. Check small `375x667`, medium `393x852`,
   large `402x874`, and desktop-small `1280x800` for sticky CTA visibility, no
   clipped headline text, no overlapping controls, and scrollability where
   content exceeds the viewport.
9. Leave the server running only while the user is reviewing. Stop it and remove
   the temporary directory when the preview is no longer needed unless the user
   explicitly asks to keep it.

## Copy Data Shape

Use a compact data object so copy changes are easy:

```js
export const steps = [
  {
    id: "step-01",
    title: "Goal qualifier",
    kind: "choice",
    headline: "What matters most right now?",
    supportingText: "Choose the outcome that would make this feel worthwhile.",
    primaryAction: "Continue",
    secondaryAction: "Not now",
    choices: ["Save time", "Reduce stress", "Make progress"],
  },
];
```

## Completion

Report the local URL, source copy path, where the temporary files live, how to
restart the server, which breakpoint checks passed, and whether the temporary
files were removed or intentionally left for review.
