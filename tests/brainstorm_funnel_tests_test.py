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
        forms = rr.STRINGS["ru"]["tests"]
        self.assertEqual([rr.plural_ru(n, forms) for n in (1, 3, 5, 11, 22)],
                         ["A/B-тест", "A/B-теста", "A/B-тестов", "A/B-тестов", "A/B-теста"])

    def test_renders_russian_report(self):
        code, page, _ = self.render(report())
        self.assertEqual(code, 0)
        for text in ("58,0%", "Ушли 1 870 из 3 224 вошедших", "step-1-b",
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


if __name__ == "__main__":
    unittest.main()
