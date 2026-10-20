# Report format

`scripts/render_report.py` reads one JSON file. Relative image paths resolve from the JSON file's directory. `scripts/analytics_to_report.py` drafts it from `fgrove analytics conversions --format json` output, filling everything except `focus`, `dropoffs` and `tests`.

The PDF has a cover with the recommendations, then a page for each section present: `metrics`, `focus`, `dropoffs`, and one page per test. At least one of `focus`, `dropoffs` and `tests` is required.

## Fields

| Field | Required | Meaning |
| --- | --- | --- |
| `lang` | no | `ru` (default) or `en`. Labels, number format and date follow it. |
| `product` | yes | Product name shown on every page. |
| `funnel` | no | Funnel name or route, shown on the cover. |
| `date` | yes | ISO date of the analysis, for example `2026-10-13`. |
| `period` | no | `{"from", "to"}` ISO dates of the analysed days; shown instead of `date` on the cover and metrics page. |
| `traffic_note` | no | Short note above the cover chart, for example the visitors and period. |
| `currency` | no | Currency code for money metrics. Default `USD`. |
| `metrics` | no | Dashboard metrics: `id`, `value` (percent for rates, a count for `visitors`, major units for `net_revenue` and `arppu`), optional `num`, `den` and `trend` (relative change in percent against the previous period). Renders the metrics page. |
| `stages` | no | Counts for the funnel chart on the metrics page: `visitors`, `quiz_starts`, `email_adds`, `paywall_views`, `checkout_starts`, `subscriptions`. |
| `focus` | no | `area` (`first_step`, `quiz` or `paywall`), `why` and `actions`: up to three lines each, at most 110 characters. Needs the area's metric in `metrics`. |
| `dropoffs` | no | Notes by step ID for the steps above the threshold, at most 160 characters each. Its presence renders the drop-off page. |
| `mde_pp` | no | Detectable change in percentage points used for sample sizes. Default `5`. |
| `steps` | yes | Drop-off by step in funnel order, entry step first: `id`, `drop` (percent, 0–100), optional `lost` and `entered`. The cover shows every tested and leaking step and the largest other drop-offs, up to eight. |
| `tests` | no | Proposals in launch order. |

Each test:

| Field | Required | Meaning |
| --- | --- | --- |
| `step` | yes | Step ID; must appear in `steps` unless the test gives `drop`. |
| `drop`, `lost`, `entered` | no | Numbers for a step outside `steps`, such as the paywall: `drop` is the share that did not start checkout. |
| `title` | yes | Human step name, for example `Email`. |
| `hypothesis` | yes | One sentence, at most 180 characters. |
| `changes` | no | Up to two short lines, at most 70 characters each, naming what changes or stays. |
| `metric` | yes | Primary metric, a few words. |
| `current` | yes | URL or image of the current step. |
| `proposed` | yes | URL or image of the proposed variant. |
| `variant` | no | Variant ID. Default `<step>-b`. |
| `sample_per_variant` | no | Overrides the computed sample. |

## Focus areas and thresholds

Each focus area compares a share of visitors with the FBP-031 practitioner range: `first_step` uses `visitor_to_quiz_start` (30–60%), `quiz` uses `visitor_to_finish_quiz` (10–20%), and `paywall` uses `visitor_to_checkout` (8–15%). The focus page shows all three and highlights the chosen one.

A step leaks when its `drop` exceeds 7%, or 20% for a step whose ID contains `email`. The entry step (the first in `steps`) never leaks; it belongs to the `first_step` area. Leaking steps are ordered by visitors lost; the page shows up to four notes.

## Sample size

Unless overridden, the sample per variant is a fixed-horizon, two-sided two-proportion calculation: baseline pass rate `1 − drop`, alternative `baseline + mde_pp`, α = 0.05, power 80%, normal approximation, rounded up. It is planning sensitivity, not a forecast of lift; the cover footer states this.

## Example

```json
{
  "lang": "ru",
  "product": "IQNIO",
  "funnel": "IQ test · main",
  "date": "2026-10-13",
  "traffic_note": "3 224 посетителя за период",
  "steps": [
    {"id": "step-1", "drop": 58.0, "lost": 1870, "entered": 3224},
    {"id": "email-capture", "drop": 32.7, "lost": 151, "entered": 462},
    {"id": "race-position", "drop": 24.6, "lost": 333, "entered": 1354},
    {"id": "apples-left", "drop": 8.4}
  ],
  "tests": [
    {
      "step": "step-1",
      "title": "Первый шаг",
      "hypothesis": "Если поставить кнопку «I’ve memorized it» прямо под словом, больше людей начнут тест — следующее действие станет очевидным.",
      "changes": ["Короткий контекст: «Let’s start your IQ test»", "Конкретная кнопка рядом со словом вместо Continue внизу"],
      "metric": "Переход на следующий шаг",
      "current": "https://iq-test-preview-main.funnelsgrove.org/step-1?previewFrame=1&previewStepLock=1",
      "proposed": "step-1-b.png"
    }
  ]
}
```
