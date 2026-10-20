#!/usr/bin/env python3
"""Tests for the brainstorm-funnel-tests PDF renderer (HTML stage; no browser needed)."""

from __future__ import annotations

import base64
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "skills/brainstorm-funnel-tests/scripts"))

import analytics_to_report as ar  # noqa: E402
import render_report as rr  # noqa: E402

PIXEL = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8DwHwAFBQIAX8jx0gAAAABJRU5ErkJggg=="
)


def report(**overrides) -> dict:
    data = {
        "product": "Acme",
        "date": "2026-10-13",
        "steps": [
            {"id": "step-1", "drop": 58.0, "lost": 1870, "entered": 3224},
            {"id": "email-capture", "drop": 32.7},
        ],
        "tests": [
            {
                "step": "step-1",
                "title": "First step",
                "hypothesis": "If the button sits under the word, more people will start.",
                "changes": ["Button under the word"],
                "metric": "Next-step reach",
                "current": "https://example.com/step-1",
                "proposed": "b.png",
            }
        ],
    }
    data.update(overrides)
    return data


class RendererTest(unittest.TestCase):
    def render(self, data: dict) -> tuple[int, str, str]:
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            (tmp / "b.png").write_bytes(PIXEL)
            (tmp / "report.json").write_text(json.dumps(data))
            err = io.StringIO()
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
                code = rr.main([str(tmp / "report.json"), str(tmp / "out.pdf"), "--html-only"])
            page = tmp / "out.html"
            return code, page.read_text() if page.exists() else "", err.getvalue()

    def test_sample_size_matches_fixed_horizon_calculation(self):
        self.assertEqual(rr.sample_per_variant(0.42, 0.05), 1550)
        self.assertEqual(rr.sample_per_variant(0.754, 0.05), 1080)
        self.assertEqual(rr.sample_per_variant(0.673, 0.05), 1323)

    def test_russian_plural(self):
        forms = rr.STRINGS["ru"]["days"]
        self.assertEqual([rr.plural_ru(n, forms) for n in (1, 3, 5, 11, 22)],
                         ["день", "дня", "дней", "дней", "дня"])

    def test_renders_russian_report(self):
        code, page, _ = self.render(report())
        self.assertEqual(code, 0)
        for text in ("Наши рекомендации<br>для <em>Acme</em>", "If the button sits under the word", "58,0%", "Ушли 1 870 из 3 224 вошедших", "step-1-b",
                     "1 550 на вариант", "13 октября 2026", "Тест 1 из 1",
                     "https://example.com/step-1"):
            self.assertIn(text, page)

    def test_renders_english_and_sample_override(self):
        data = report(lang="en")
        data["tests"][0]["sample_per_variant"] = 2000
        code, page, _ = self.render(data)
        self.assertEqual(code, 0)
        for text in ("58.0%", "1,870 of 3,224 visitors left", "2,000 per variant", "13 October 2026"):
            self.assertIn(text, page)

    def test_unknown_step_is_an_error(self):
        data = report()
        data["tests"][0]["step"] = "missing"
        code, _, err = self.render(data)
        self.assertEqual(code, 1)
        self.assertIn("`missing` is not in `steps`", err)

    def test_missing_image_is_an_error(self):
        data = report()
        data["tests"][0]["proposed"] = "nope.png"
        code, _, err = self.render(data)
        self.assertEqual(code, 1)
        self.assertIn("screen not found", err)

    def test_long_copy_warns(self):
        data = report()
        data["tests"][0]["hypothesis"] = "x" * 200
        code, _, err = self.render(data)
        self.assertEqual(code, 0)
        self.assertIn("hypothesis is 200 chars", err)

    def test_leaking_steps_skip_entry_and_use_email_threshold(self):
        steps = [{"id": "step-1", "drop": 50.0}, {"id": "a", "drop": 7.0}, {"id": "b", "drop": 8.0, "lost": 10},
                 {"id": "email-capture", "drop": 19.0}, {"id": "c", "drop": 30.0, "lost": 50},
                 {"id": "email-2", "drop": 21.0, "lost": 5}]
        self.assertEqual([st["id"] for st in rr.leaking_steps(steps)], ["c", "b", "email-2"])

    def test_renders_metrics_focus_and_dropoffs(self):
        data = report(
            period={"from": "2026-10-13", "to": "2026-10-19"},
            metrics=[{"id": "visitors", "value": 52409},
                     {"id": "paywall_to_checkout", "value": 19.76, "num": 3596, "den": 18197, "trend": -11.3},
                     {"id": "visitor_to_checkout", "value": 6.86, "num": 3596, "den": 52409},
                     {"id": "net_revenue", "value": 52411.02}],
            stages={"visitors": 52409, "paywall_views": 18197},
            focus={"area": "paywall", "summary": "Start with the paywall: plans first.",
                   "why": ["Few start checkout."], "actions": ["Show plans first."]},
            dropoffs={"email-capture": "Email asks too early."},
            steps=[{"id": "step-1", "drop": 58.0, "lost": 1870, "entered": 3224},
                   {"id": "email-capture", "drop": 32.7, "lost": 151, "entered": 462},
                   {"id": "quiz-3", "drop": 6.0}],
        )
        data["tests"].append({"step": "paywall", "title": "Paywall", "drop": 80.2, "lost": 14601, "entered": 18197,
                              "hypothesis": "If plans come first, more people will pay.", "metric": "Paywall → checkout",
                              "current": "b.png", "proposed": "b.png"})
        code, page, err = self.render(data)
        self.assertEqual(code, 0, err)
        self.assertEqual(err, "")
        for text in ("13–19 октября 2026 · 7 дней", "52\u202f409", "▼ 11,3%", "3\u202f596 / 18\u202f197", "$52\u202f411",
                     "Главное — конверсия paywall", "Start with the paywall: plans first.",
                     "Шаг email-capture", "13–19 октября 2026 (7 дней)", "ниже ориентира · ориентир 8–15%",
                     "Show plans first.", "порог 20%", "Email asks too early.", "Ушли 14\u202f601 из 18\u202f197 вошедших",
                     "Тест 2 из 2"):
            self.assertIn(text, page)

    def test_leaking_step_without_note_warns(self):
        code, _, err = self.render(report(dropoffs={}))
        self.assertEqual(code, 0)
        self.assertIn("step `email-capture` is above the threshold but has no note", err)

    def test_focus_needs_its_metric(self):
        code, _, err = self.render(report(focus={"area": "quiz", "why": ["x"], "actions": ["y"]}))
        self.assertEqual(code, 1)
        self.assertIn("focus needs metric `visitor_to_finish_quiz`", err)

    def test_empty_report_is_an_error(self):
        code, _, err = self.render(report(tests=[]))
        self.assertEqual(code, 1)
        self.assertIn("nothing to render", err)


class AnalyticsToReportTest(unittest.TestCase):
    def test_converts_dashboard_numbers_and_stops_before_paywall(self):
        metric = lambda mid, n, d, trend: {"id": mid, "numerator": n, "denominator": d, "rate": n / d,
                                           "previousPeriod": {"trendPercent": trend}}
        analytics = {
            "from": "2026-10-13", "to": "2026-10-19",
            "project": {"name": "claimbee"}, "funnel": {"name": "claimbee-general"},
            "overview": {"currency": "USD", "totals": {"netRevenueMinor": 5241102, "arppuMinor": 3482.46}},
            "totals": {"visitors": 1000, "quizStarts": 700, "emailAdds": 300, "paywallViews": 350,
                       "checkoutStarts": 70, "subscriptions": 30},
            "metrics": [metric("visitor_to_quiz_start", 700, 1000, -1.5), metric("paywall_to_checkout", 70, 350, None)],
            "funnelPath": [
                {"stepId": s, "users": u, "dropoffs": l, "dropoffRate": l / u if u else 0}
                for s, u, l in (("claim", 1000, 300), ("email-capture", 400, 50), ("paywall", 350, 280),
                                ("subscription-started", 30, 0), ("subscriptions", 100, 5), ("manage-subscription", 0, 0))
            ],
        }
        data = ar.convert(analytics, "ClaimBee", "ru")
        self.assertEqual([s["id"] for s in data["steps"]], ["claim", "email-capture", "subscriptions"])
        self.assertEqual(data["steps"][0], {"id": "claim", "drop": 30.0, "lost": 300, "entered": 1000})
        metrics = {m["id"]: m for m in data["metrics"]}
        self.assertEqual(metrics["visitor_to_quiz_start"], {"id": "visitor_to_quiz_start", "value": 70.0,
                                                            "num": 700, "den": 1000, "trend": -1.5})
        self.assertEqual(metrics["visitor_to_checkout"]["value"], 7.0)
        self.assertEqual(metrics["net_revenue"]["value"], 52411.02)
        self.assertEqual(data["period"], {"from": "2026-10-13", "to": "2026-10-19"})
        self.assertEqual(data["product"], "ClaimBee")


if __name__ == "__main__":
    unittest.main()
