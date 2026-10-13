# Report format

`scripts/render_report.py` reads one JSON file. Relative image paths resolve from the JSON file's directory.

## Fields

| Field | Required | Meaning |
| --- | --- | --- |
| `lang` | no | `ru` (default) or `en`. Labels, number format and date follow it. |
| `product` | yes | Product name shown on every page. |
| `funnel` | no | Funnel name or route, shown on the cover. |
| `date` | yes | ISO date of the analysis, for example `2026-10-13`. |
| `traffic_note` | no | Short note above the cover chart, for example the visitors and period. |
| `mde_pp` | no | Detectable change in percentage points used for sample sizes. Default `5`. |
| `steps` | yes | Drop-off by step: `id`, `drop` (percent, 0–100), optional `lost` and `entered`. The cover shows every tested step and the largest other drop-offs, up to eight. |
| `tests` | yes | Proposals in launch order. |

Each test:

| Field | Required | Meaning |
| --- | --- | --- |
| `step` | yes | Step ID; must appear in `steps`. |
| `title` | yes | Human step name, for example `Email`. |
| `hypothesis` | yes | One sentence, at most 180 characters. |
| `changes` | no | Up to two short lines, at most 70 characters each, naming what changes or stays. |
| `metric` | yes | Primary metric, a few words. |
| `current` | yes | URL or image of the current step. |
| `proposed` | yes | URL or image of the proposed variant. |
| `variant` | no | Variant ID. Default `<step>-b`. |
| `sample_per_variant` | no | Overrides the computed sample. |

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
