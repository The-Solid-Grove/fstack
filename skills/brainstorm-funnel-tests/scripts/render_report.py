#!/usr/bin/env python3
"""Render a shareable funnel A/B test proposal PDF from report JSON.

Usage:
  render_report.py REPORT.json OUT.pdf [--html-only] [--chrome PATH]

The report format is documented in ../references/report-format.md. Screens may
be image paths (relative to the JSON file) or http(s) URLs; URLs are captured
at 375x667 and 3x scale with headless Chrome next to the output file.
The HTML is always written beside the PDF so pages can be inspected.
Dependency-free: Python 3.9+ standard library and Google Chrome/Chromium.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import math
import os
import shutil
import subprocess
import sys
import urllib.parse
from pathlib import Path
from statistics import NormalDist

SKILL_DIR = Path(__file__).resolve().parent.parent
BRAND = SKILL_DIR / "assets" / "brand"
VIEWPORT = (375, 667)
MAX_HYPOTHESIS = 180
MAX_CHANGES = 2
MAX_CHANGE = 70
MAX_CHART_STEPS = 8

STRINGS = {
    "ru": {
        "title": "{product}: <em>{n} {tests}</em><br>на главных отвалах",
        "tests": ("A/B-тест", "A/B-теста", "A/B-тестов"),
        "order": "Порядок — по приоритету запуска.",
        "chart": "Отвал по шагам",
        "chart_note": "шаги отсортированы по отвалу",
        "test_n": "Тест {i}",
        "test_of": "Тест {i} из {n}",
        "drop": "отвал на шаге",
        "lost": "Ушли {lost} из {entered} вошедших",
        "hypothesis": "Гипотеза",
        "metric": "Главная метрика",
        "sample": "Выборка",
        "per_variant": "{n} на вариант",
        "current": "Текущий",
        "proposed": "Предлагаемый",
        "footer": "Гипотезы и варианты — предложения для теста, не прогноз роста. "
        "Выборка: +{mde} п.п. к доле прошедших шаг, α = 0,05, мощность 80%.",
        "months": ("января", "февраля", "марта", "апреля", "мая", "июня", "июля",
                   "августа", "сентября", "октября", "ноября", "декабря"),
        "decimal": ",",
    },
    "en": {
        "title": "{product}: <em>{n} {tests}</em><br>for the biggest drop-offs",
        "tests": ("A/B test", "A/B tests", "A/B tests"),
        "order": "Ordered by launch priority.",
        "chart": "Drop-off by step",
        "chart_note": "sorted by drop-off",
        "test_n": "Test {i}",
        "test_of": "Test {i} of {n}",
        "drop": "drop-off on this step",
        "lost": "{lost} of {entered} visitors left",
        "hypothesis": "Hypothesis",
        "metric": "Primary metric",
        "sample": "Sample",
        "per_variant": "{n} per variant",
        "current": "Current",
        "proposed": "Proposed",
        "footer": "Hypotheses and variants are test proposals, not growth forecasts. "
        "Sample: +{mde} pp step pass rate, α = 0.05, 80% power.",
        "months": ("January", "February", "March", "April", "May", "June", "July",
                   "August", "September", "October", "November", "December"),
        "decimal": ".",
    },
}


class ReportError(Exception):
    pass


def sample_per_variant(baseline: float, mde: float, alpha: float = 0.05, power: float = 0.8) -> int:
    """Fixed-horizon two-sided two-proportion sample size per variant (normal approximation)."""
    p1, p2 = baseline, min(baseline + mde, 0.999)
    z = NormalDist().inv_cdf
    pbar = (p1 + p2) / 2
    n = (z(1 - alpha / 2) * math.sqrt(2 * pbar * (1 - pbar))
         + z(power) * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def plural_ru(n: int, forms: tuple[str, str, str]) -> str:
    if n % 10 == 1 and n % 100 != 11:
        return forms[0]
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return forms[1]
    return forms[2]


class Fmt:
    def __init__(self, lang: str):
        self.s = STRINGS[lang]
        self.lang = lang

    def int(self, n: int) -> str:
        return f"{n:,}".replace(",", " " if self.lang == "ru" else ",")

    def pct(self, p: float) -> str:
        return f"{p:.1f}".replace(".", self.s["decimal"]) + "%"

    def date(self, iso: str) -> str:
        d = dt.date.fromisoformat(iso)
        return f"{d.day} {self.s['months'][d.month - 1]} {d.year}"

    def tests(self, n: int) -> str:
        forms = self.s["tests"]
        return plural_ru(n, forms) if self.lang == "ru" else forms[0 if n == 1 else 1]


def load_report(path: Path) -> tuple[dict, list[str]]:
    """Validate the report; return it with non-blocking length warnings."""
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in ("product", "date", "steps", "tests"):
        if not data.get(key):
            raise ReportError(f"missing required field `{key}`")
    data.setdefault("lang", "ru")
    if data["lang"] not in STRINGS:
        raise ReportError(f"lang must be one of {sorted(STRINGS)}")
    dt.date.fromisoformat(data["date"])
    steps = {}
    for s in data["steps"]:
        if "id" not in s or not isinstance(s.get("drop"), (int, float)) or not 0 <= s["drop"] <= 100:
            raise ReportError(f"each step needs `id` and `drop` (0–100): {s}")
        steps[s["id"]] = s
    warnings = []
    for i, t in enumerate(data["tests"], 1):
        for key in ("step", "title", "hypothesis", "metric", "current", "proposed"):
            if not t.get(key):
                raise ReportError(f"test {i}: missing `{key}`")
        if t["step"] not in steps:
            raise ReportError(f"test {i}: step `{t['step']}` is not in `steps`")
        if len(t["hypothesis"]) > MAX_HYPOTHESIS:
            warnings.append(f"test {i}: hypothesis is {len(t['hypothesis'])} chars (keep ≤ {MAX_HYPOTHESIS})")
        changes = t.get("changes", [])
        if len(changes) > MAX_CHANGES or any(len(c) > MAX_CHANGE for c in changes):
            warnings.append(f"test {i}: keep ≤ {MAX_CHANGES} changes of ≤ {MAX_CHANGE} chars")
    return data, warnings


def find_chrome(explicit: str | None) -> str:
    candidates = [explicit, os.environ.get("CHROME"),
                  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                  "/Applications/Chromium.app/Contents/MacOS/Chromium",
                  *(shutil.which(n) for n in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"))]
    for c in candidates:
        if c and Path(c).exists():
            return c
    raise ReportError("Chrome/Chromium not found; pass --chrome or set CHROME")


def chrome(binary: str, *args: str) -> None:
    subprocess.run([binary, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--no-first-run", "--virtual-time-budget=9000", *args],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)


def capture(binary: str, url: str, out: Path) -> Path:
    """Screenshot a URL at the mobile viewport. The iframe keeps layout at 375px."""
    w, h = VIEWPORT
    wrapper = out.with_suffix(".html")
    wrapper.write_text(
        f'<!doctype html><body style="margin:0"><iframe src="{html.escape(url)}" '
        f'style="border:0;display:block;width:{w}px;height:{h}px"></iframe></body>')
    chrome(binary, "--force-device-scale-factor=3", f"--window-size={w},{h}",
           f"--screenshot={out}", wrapper.as_uri())
    wrapper.unlink()
    if not out.exists():
        raise ReportError(f"capture failed: {url}")
    return out


def resolve_screen(ref: str, base: Path, shots: Path, name: str, binary: str | None) -> str:
    if urllib.parse.urlparse(ref).scheme in ("http", "https"):
        if binary is None:
            return ref  # --html-only: leave the URL for a later capture
        shots.mkdir(parents=True, exist_ok=True)
        return capture(binary, ref, shots / f"{name}.png").as_uri()
    path = (base / ref).resolve()
    if not path.exists():
        raise ReportError(f"screen not found: {path}")
    return path.as_uri()


def render_html(data: dict, screens: dict[tuple[int, str], str]) -> str:
    f = Fmt(data["lang"])
    s, e = f.s, html.escape
    steps = {st["id"]: st for st in data["steps"]}
    tests = data["tests"]
    total = len(tests)
    mde = data.get("mde_pp", 5)
    tested = {t["step"]: i for i, t in enumerate(tests, 1)}

    ranked = sorted(data["steps"], key=lambda st: -st["drop"])
    shown = [st for st in ranked if st["id"] in tested]
    shown += [st for st in ranked if st["id"] not in tested][:max(0, MAX_CHART_STEPS - len(shown))]
    shown.sort(key=lambda st: -st["drop"])
    top = max(st["drop"] for st in shown) or 1
    bars = "".join(f"""
      <div class="bar{' hit' if st['id'] in tested else ''}">
        <span>{e(st['id'])}</span>
        <span class="track"><span class="fill" style="width:{st['drop'] / top * 100:.1f}%"></span></span>
        <span class="val">{f.pct(st['drop'])}</span>
        <span class="tag">{s['test_n'].format(i=tested[st['id']]) if st['id'] in tested else ''}</span>
      </div>""" for st in shown)
    agenda = "".join(f"""
      <li><span class="n">{i}</span><span>{e(t['title'])}</span><span class="d">{f.pct(steps[t['step']]['drop'])}</span></li>"""
        for i, t in enumerate(tests, 1))
    sub = " · ".join(e(x) for x in (data.get("funnel"), f.date(data["date"])) if x)
    note = " · ".join(e(x) for x in (data.get("traffic_note"), s["chart_note"]) if x)

    pages = []
    for i, t in enumerate(tests, 1):
        st = steps[t["step"]]
        lost = (f"<b>{s['lost'].format(lost=f.int(st['lost']), entered=f.int(st['entered']))}</b>"
                if "lost" in st and "entered" in st else "")
        n = t.get("sample_per_variant") or sample_per_variant(1 - st["drop"] / 100, mde / 100)
        changes = "".join(f"<li>{e(c)}</li>" for c in t.get("changes", []))
        variant = t.get("variant") or f"{t['step']}-b"
        pages.append(f"""
  <section class="page test">
    <header><img class="logo" src="{(BRAND / 'logo-light.svg').as_uri()}" alt="funnelsgrove">
      <span class="meta">{e(data['product'])} · {s['test_of'].format(i=i, n=total)}</span></header>
    <div class="body">
      <div class="copy">
        <p class="eyebrow"><span class="chip">{e(t['step'])}</span>{e(t['title'])}</p>
        <div class="drop"><span class="drop-n">{f.pct(st['drop'])}</span><span class="drop-l">{s['drop']}<br>{lost}</span></div>
        <p class="label">{s['hypothesis']}</p>
        <p class="hyp">{e(t['hypothesis'])}</p>
        <ul class="changes">{changes}</ul>
        <dl class="facts">
          <div><dt>{s['metric']}</dt><dd>{e(t['metric'])}</dd></div>
          <div><dt>{s['sample']}</dt><dd>{s['per_variant'].format(n=f.int(n))}</dd></div>
        </dl>
      </div>
      <div class="phones">
        <figure><figcaption><b>A</b>{s['current']}<code>{e(t['step'])}</code></figcaption>
          <div class="phone"><img src="{e(screens[(i, 'a')])}" alt=""></div></figure>
        <figure class="b"><figcaption><b>B</b>{s['proposed']}<code>{e(variant)}</code></figcaption>
          <div class="phone"><img src="{e(screens[(i, 'b')])}" alt=""></div></figure>
      </div>
    </div>
  </section>""")

    css = (SKILL_DIR / "assets" / "report.css").read_text(encoding="utf-8")
    css = css.replace("SORA_URL", (BRAND / "Sora-variable.ttf").as_uri())
    return f"""<!doctype html>
<html lang="{data['lang']}"><head><meta charset="utf-8"><title>{e(data['product'])} — A/B</title>
<style>{css}</style></head><body>
  <section class="page cover">
    <div>
      <img class="logo" src="{(BRAND / 'logo-dark.svg').as_uri()}" alt="funnelsgrove">
      <h1>{s['title'].format(product=e(data['product']), n=total, tests=f.tests(total))}</h1>
      <p class="sub">{sub}<br>{s['order']}</p>
      <ol>{agenda}</ol>
    </div>
    <div class="chart"><h2>{s['chart']}</h2><p>{note}</p>{bars}</div>
    <p class="foot">{s['footer'].format(mde=mde)}</p>
  </section>
{''.join(pages)}
</body></html>"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("report", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--html-only", action="store_true", help="write HTML without capturing or printing")
    ap.add_argument("--chrome", help="Chrome/Chromium binary")
    args = ap.parse_args(argv)
    try:
        data, warnings = load_report(args.report)
        for w in warnings:
            print(f"warning: {w}", file=sys.stderr)
        binary = None if args.html_only else find_chrome(args.chrome)
        out = args.out.resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        shots = out.with_name(out.stem + "-screens")
        base = args.report.resolve().parent
        screens = {(i, k): resolve_screen(t[key], base, shots, f"{i}-{k}-{t['step']}", binary)
                   for i, t in enumerate(data["tests"], 1)
                   for k, key in (("a", "current"), ("b", "proposed"))}
        page = out.with_suffix(".html")
        page.write_text(render_html(data, screens), encoding="utf-8")
        if binary:
            chrome(binary, "--no-pdf-header-footer", f"--print-to-pdf={out}", page.as_uri())
            if not out.exists():
                raise ReportError("Chrome did not write the PDF")
        print(out if binary else page)
        return 0
    except (ReportError, ValueError, json.JSONDecodeError, subprocess.SubprocessError) as err:
        print(f"error: {err}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
