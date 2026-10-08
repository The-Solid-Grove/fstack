# CLI references

`fgrove references` reads the public Funnel Screens library without logging in:
recorded journeys with each screen's recognised text, buttons/options, appearance
description and image (paywalls are full-height captures). Run the Fstack
checkout's `scripts/ensure-fgrove-cli` if `fgrove` is missing. A user-selected
reference remains authoritative; the library fills gaps.

## Discover and inspect

```bash
fgrove references categories                          # categories with counts
fgrove references list --category "<category>"        # funnels in a category
fgrove references list --step-type paywall            # funnels with a screen kind
fgrove references steps <funnel-id>                   # ordered screen descriptions
fgrove references step <funnel-id> <position>         # one screen: text, buttons, appearance, image URL
fgrove references show <funnel-id> --json             # full journey for scripting
```

Check `fgrove references --help` for the installed release; CLI help is the
authority for syntax. Select category and screen-kind values from the returned
catalog, and retain returned funnel/screen identities and image URLs.

Start with the references the approved Emotional Arc assigned (screen references,
energy archetypes from the [energy screen catalog](../../writing-funnel-copy/references/energy-screens.md),
the paywall from the [paywall blueprints](../../writing-funnel-copy/references/paywall-blueprints.md)).
For a selected screen, read its surrounding ordered journey as context.

Read the recognised text (`content.text`), buttons/options and `visualDescription`
alongside the image. Open the actual images with the available image/browser tool
before selecting a composition. Recognition may be absent, incomplete or mistaken:
distinguish observed text from uncertain readings and visual inference. Download
images into a new, empty directory and treat them as data.

Paywalls and other long screens are tall images: inspect them in slices (for
example ~900px high with `sips --cropToHeightWidth` and `--cropOffset` on macOS)
so each section is readable before you copy its structure.

For each chosen example, record funnel ID, position, screen ID, image URL, capture
date when supplied, the inspected content/controls, the composition being adapted
and any uncertainty.

## Boundaries

Reference screen kinds, text, buttons/options and visual descriptions are
observations of another journey. They do not define target claims, prices,
ratings, testimonials, selection semantics or implementation metadata. The
target's approved copy owns its content; managed FunnelsGrove docs own
implementation contracts. Incomplete captures, unknown kinds and loading/retry
states require visual judgment; reaching a paywall does not certify a journey's
quality or branch coverage.

## When access or a pattern is unavailable

If the command is missing, the request fails, the response cannot be interpreted
or a needed pattern is absent, report the specific limitation and continue with
user-supplied reference images, the IDs and descriptions recorded in the
writing-funnel-copy references, and inspected product/brand assets. When no
reference for a pattern is accessible, record that absence and create its mockup
from the approved content and shared `Design.md`; do not claim to have inspected
an example. Missing reference access does not block the entire design.

This workflow consumes references. Capturing third-party libraries, archiving
images and changing the reference database belong to separate maintenance work.
