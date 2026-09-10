---
name: preview-funnel
description: Use when turning finished funnel copy, screen-by-screen funnel specs, PLAN.md sections, or research-derived funnel copy into a temporary clickable local mockup for copy review, especially before committing to final design or FunnelsGrove implementation.
---

# Preview Funnel

## Overview

Build a simple, temporary click-through that makes funnel copy easy to read,
tap through, and critique. Favor plain static HTML/CSS/JS and one reusable
screen renderer. Structure stays low-fidelity, but the preview should look
good by default: use the bundled warm-editorial stylesheet
(`references/preview-style.css`) instead of inventing ad-hoc neutral styling.

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
   - `styles.css` — copy `references/preview-style.css` from this skill into
     the preview directory verbatim; do not write styles from scratch
   - `steps.mjs` or `steps.json` for copy data
   - `app.mjs` for navigation and choice state
4. Render one reusable mobile screen: progress header, headline, support copy,
   optional choice cards, optional notes/proof rows, and a sticky bottom CTA.
5. Follow the Visual Style section below. The goal is still copy flow review,
   not final design approval — but the preview should be pleasant to read and
   feel like a real product, not a wireframe.
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

## Visual Style

The default look is "candlelit stationery": a dark warm stage with a vignette
and film grain around a cream paper phone screen, a single copper accent, a
serif display face (Fraunces) for headlines, and a humanist sans (DM Sans) for
everything else. It is defined once in `references/preview-style.css` — copy
it in as `styles.css` and build markup from its class names.
`references/example.html` is a working three-screen sample (choice, info with
a proof card, projection with a stat box) that shows the expected markup and
renderer wiring — mirror its structure rather than inventing new markup:

- Stage (page): `.stage-title` (italic serif) / `.stage-subtitle` (small caps;
  put the source copy path here) above the phone, `.stage-nav` for
  back/restart controls under it.
- Phone: `.phone > .screen` — the bezel, notch, copper edge glow, and paper
  grain all come from `.phone`'s own CSS; no extra markup.
- Screen anatomy, top to bottom: `.app-name` (small caps between hairlines),
  `.progress > i` (fill width = step progress), `.step-num`
  (`<strong>03</strong> / 12`), `.content` (scrollable; children get a
  staggered entrance animation, and short content auto-centers vertically),
  `.cta` (pinned to the bottom).
- Copy: `.hero` (serif headline, one per screen; wrap a key phrase in `<em>`
  for a copper italic), `.hero-sm`, `.body-text`, `.note` (italic serif
  caveat), `.quote` (left-bordered italic).
- Choices: `.options > button.opt`; each gets a radio ring automatically;
  toggle `.selected` on tap (copper ring, border, and tint come from CSS).
- Proof and letters: `.card-paper` with optional `.from` label and
  `.letter-text` for quoted letter copy; `.tag` for PRO/MOST POPULAR pills;
  `.stat-box` with `.num` and `.label` for counters.
- Buttons: `.btn` primary (disable until a required choice is made),
  `.btn-ghost` secondary.

Rules:

- Never introduce pure black, pure white, or default-blue anything; every
  color on screen must come from the `:root` custom properties.
- Headlines use the display serif; do not set body copy in it.
- If the product has its own established brand palette and the user wants it,
  swap only the `:root` custom properties (accent, screen, stage, text tones)
  and keep every class and layout rule unchanged.
- Emojis are fine as lightweight visual anchors (matching the copy spec), but
  no external images or icon fonts.

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
