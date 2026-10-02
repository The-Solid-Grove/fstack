# Funnel Screens references

Use [Funnel Screens](https://www.funnelsgrove.com/funnel-screens) as an optional
reference source. When its CLI capability is available, inspect it for the
journey's actual patterns. Existing user-selected references remain authoritative
for the selection; service availability does not change that choice.

## Discover and inspect through the CLI

Check `fgrove references --help` and each relevant subcommand's help for the
installed release. These read operations discover reference material; they do
not select or modify the user's hosted funnel.

```bash
fgrove references categories --json
fgrove references list --json
fgrove references list --category <category> --step-type <step-type> --json
fgrove references show <funnel-id> --json
fgrove references steps <funnel-id> --json
fgrove references step <funnel-id> <step-id-or-position> --json
```

Use the supported `--site-url <site-url>` option when a different Funnel Screens
site is requested. Select category/type values from the CLI's returned values,
and use returned identities and URLs instead of constructing image paths.
For a supplied link containing funnel and screen IDs, retain both and inspect
the surrounding ordered journey as context.

Read the available recognized visible text (`content.text`), buttons/options, and
`visualDescription` alongside each step's image and provenance. Open the actual
images with the available image/browser tool before selecting a composition.
Recognition may be absent, incomplete or mistaken: distinguish observed text
from uncertain readings and visual inference. Metadata or a cover image alone
does not establish that a screen is suitable.

For each chosen example, record source URL, funnel/screen IDs when available,
image URL, capture date when supplied, the inspected content/controls,
composition being adapted and uncertainty. Inspect full-height images where
the pattern includes content below the initial viewport. If image generation
needs local reference files, obtain them through an available permitted tool
and retain their source identity.

Reference screen types, visible text, buttons/options and visual descriptions
are observations of another journey. They do not define target claims, prices,
selection semantics or implementation metadata. The target's approved copy owns
its content; managed FunnelsGrove docs own implementation contracts. Incomplete
captures, unknown types and loading/retry states require visual judgment; reaching
a paywall does not certify the journey's quality or branch coverage.

## When the service or a pattern is unavailable

If the command is missing, access fails, the response cannot be interpreted or
a needed pattern is absent, report the specific limitation and continue with
supplied reference images, the browser library, or inspected product/brand screens.
Keep the user's selected reference and use complementary material for a named
gap. When no reference for a pattern is accessible, record that absence and
create its mockup from the approved content and shared `Design.md`; do not claim
to have inspected an example. Missing optional reference access does not block
the entire design.

This workflow consumes references. Capturing third-party libraries, archiving
images, operating storage services and changing the reference database belong
to separate maintenance work.
