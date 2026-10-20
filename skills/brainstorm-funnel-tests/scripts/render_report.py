#!/usr/bin/env python3
"""Render a shareable funnel recommendations PDF from report JSON.

Usage:
  render_report.py REPORT.json OUT.pdf [--html-only] [--chrome PATH]

Sections are optional: period metrics and the focus area, drop-off above the
thresholds, and A/B tests. The report format is documented in
../references/report-format.md. Screens may
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
MAX_NOTE = 160
MAX_FOCUS_LINES = 3
MAX_FOCUS_LINE = 110
MAX_DROPOFF_CARDS = 4
# A step leaks when its drop-off exceeds the threshold; the entry step belongs to the focus area.
DROP_THRESHOLD = 7.0
EMAIL_DROP_THRESHOLD = 20.0
# Focus areas: key metric (share of visitors) and the FBP-031 practitioner range, plus context metrics.
AREAS = {
    "first_step": ("visitor_to_quiz_start", (30, 60), ()),
    "quiz": ("visitor_to_finish_quiz", (10, 20), ("quiz_start_to_email",)),
    "paywall": ("visitor_to_checkout", (8, 15), ("paywall_to_checkout", "checkout_to_subscription")),
}
TILES = ("visitors", "visitor_to_quiz_start", "quiz_start_to_email", "visitor_to_finish_quiz", "paywall_to_checkout",
         "checkout_to_subscription", "paywall_to_subscription", "visitor_to_subscription", "net_revenue", "arppu")
MONEY = {"net_revenue", "arppu"}
STAGES = ("visitors", "quiz_starts", "email_adds", "paywall_views", "checkout_starts", "subscriptions")
CURRENCY = {"USD": "$", "EUR": "€", "GBP": "£"}

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
        "days": ("день", "дня", "дней"),
        "focus_title": "{product}: фокус —<br><em>{area}</em>",
        "dropoffs_cover": "{product}: <em>отвалы</em><br>и что с ними делать",
        "row_focus": "Фокус: {area}",
        "metrics_title": "Метрики за период",
        "metrics_note": "{period} · изменение — к предыдущему периоду такой же длины",
        "funnel": "Воронка",
        "of_visitors": "{p} визитов",
        "focus_h": "Главный фокус: {area}",
        "focus_note": "Ориентиры — доля визитов на первом экране (практические диапазоны, не гарантия результата)",
        "focus_tag": "Фокус",
        "benchmark": "ориентир {lo}–{hi}%",
        "status": ("ниже ориентира", "в ориентире", "выше ориентира"),
        "why": "Почему",
        "actions": "Что делать",
        "trend": "к пред. периоду",
        "dropoffs_h": "Отвалы по шагам",
        "dropoffs_rule": "Порог — больше {t}% ушедших на шаге, для email — больше {e}%. "
        "Первый шаг и paywall оцениваются в разделе фокуса.",
        "dropoffs_none": "Ни один шаг не превышает порог — тестировать отдельные шаги квиза пока не нужно.",
        "dropoffs_more": "Ещё {n} над порогом — в таблице слева",
        "threshold": "порог {t}%",
        "dhead": ("Шаг", "Отвал", "Ушли"),
        "area": {"first_step": "конверсия первого шага", "quiz": "проходимость квиза", "paywall": "конверсия paywall"},
        "area_metric": {"first_step": "прошли первый шаг", "quiz": "дошли до paywall", "paywall": "начали оплату"},
        "metric_names": {
            "visitors": "Визиты", "visitor_to_quiz_start": "Прошли первый шаг",
            "quiz_start_to_email": "Первый шаг → email", "visitor_to_finish_quiz": "Дошли до paywall",
            "paywall_to_checkout": "Paywall → checkout", "checkout_to_subscription": "Checkout → подписка",
            "paywall_to_subscription": "Paywall → подписка", "visitor_to_subscription": "Визит → подписка",
            "visitor_to_checkout": "Визит → checkout", "net_revenue": "Чистая выручка", "arppu": "ARPPU",
        },
        "stage": {"visitors": "Визиты", "quiz_starts": "Первый шаг", "email_adds": "Email",
                  "paywall_views": "Paywall", "checkout_starts": "Checkout", "subscriptions": "Подписки"},
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
        "days": ("day", "days", "days"),
        "focus_title": "{product}: focus on<br><em>{area}</em>",
        "dropoffs_cover": "{product}: <em>drop-offs</em><br>and what to do",
        "row_focus": "Focus: {area}",
        "metrics_title": "Metrics for the period",
        "metrics_note": "{period} · change vs the previous period of the same length",
        "funnel": "Funnel",
        "of_visitors": "{p} of visitors",
        "focus_h": "Main focus: {area}",
        "focus_note": "Ranges are shares of first-screen visitors (practitioner ranges, not targets)",
        "focus_tag": "Focus",
        "benchmark": "range {lo}–{hi}%",
        "status": ("below range", "within range", "above range"),
        "why": "Why",
        "actions": "What to do",
        "trend": "vs previous period",
        "dropoffs_h": "Drop-off by step",
        "dropoffs_rule": "Threshold: more than {t}% leave the step, more than {e}% for email. "
        "The entry step and the paywall belong to the focus section.",
        "dropoffs_none": "No step exceeds the threshold, so single quiz steps need no test yet.",
        "dropoffs_more": "{n} more above the threshold, see the table",
        "threshold": "threshold {t}%",
        "dhead": ("Step", "Drop-off", "Left"),
        "area": {"first_step": "first-step conversion", "quiz": "quiz completion", "paywall": "paywall conversion"},
        "area_metric": {"first_step": "completed the first step", "quiz": "reached the paywall",
                        "paywall": "started checkout"},
        "metric_names": {
            "visitors": "Visitors", "visitor_to_quiz_start": "First step completed",
            "quiz_start_to_email": "First step → email", "visitor_to_finish_quiz": "Reached paywall",
            "paywall_to_checkout": "Paywall → checkout", "checkout_to_subscription": "Checkout → subscription",
            "paywall_to_subscription": "Paywall → subscription", "visitor_to_subscription": "Visitor → subscription",
            "visitor_to_checkout": "Visitor → checkout", "net_revenue": "Net revenue", "arppu": "ARPPU",
        },
        "stage": {"visitors": "Visitors", "quiz_starts": "First step", "email_adds": "Email",
                  "paywall_views": "Paywall", "checkout_starts": "Checkout", "subscriptions": "Subscriptions"},
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

    def num(self, x: float) -> str:
        return f"{x:g}".replace(".", self.s["decimal"])

    def pct(self, p: float) -> str:
        return f"{p:.1f}".replace(".", self.s["decimal"]) + "%"

    def date(self, iso: str) -> str:
        d = dt.date.fromisoformat(iso)
        return f"{d.day} {self.s['months'][d.month - 1]} {d.year}"

    def plural(self, n: int, forms: tuple[str, str, str]) -> str:
        return plural_ru(n, forms) if self.lang == "ru" else forms[0 if n == 1 else 1]

    def tests(self, n: int) -> str:
        return self.plural(n, self.s["tests"])

    def period(self, p: dict) -> str:
        a, b = dt.date.fromisoformat(p["from"]), dt.date.fromisoformat(p["to"])
        days = (b - a).days + 1
        m = self.s["months"]
        if a == b:
            span = self.date(p["from"])
        elif (a.year, a.month) == (b.year, b.month):
            span = f"{a.day}–{b.day} {m[a.month - 1]} {a.year}"
        else:
            span = f"{a.day} {m[a.month - 1]} – {self.date(p['to'])}"
        return f"{span} · {days} {self.plural(days, self.s['days'])}"

    def money(self, v: float, currency: str) -> str:
        sym = CURRENCY.get(currency)
        n = self.int(round(v)) if v >= 100 else f"{v:.2f}".replace(".", self.s["decimal"])
        return f"{sym}{n}" if sym else f"{n} {currency}"

    def metric(self, m: dict, currency: str) -> str:
        if m["id"] == "visitors":
            return self.int(m["value"])
        if m["id"] in MONEY:
            return self.money(m["value"], currency)
        return self.pct(m["value"])


def load_report(path: Path) -> tuple[dict, list[str]]:
    """Validate the report; return it with non-blocking length warnings."""
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in ("product", "date", "steps"):
        if not data.get(key):
            raise ReportError(f"missing required field `{key}`")
    data.setdefault("tests", [])
    if not (data["tests"] or data.get("focus") or "dropoffs" in data):
        raise ReportError("nothing to render: add `focus`, `dropoffs` or `tests`")
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
        if t["step"] not in steps and not isinstance(t.get("drop"), (int, float)):
            raise ReportError(f"test {i}: step `{t['step']}` is not in `steps` and the test has no `drop`")
        if len(t["hypothesis"]) > MAX_HYPOTHESIS:
            warnings.append(f"test {i}: hypothesis is {len(t['hypothesis'])} chars (keep ≤ {MAX_HYPOTHESIS})")
        changes = t.get("changes", [])
        if len(changes) > MAX_CHANGES or any(len(c) > MAX_CHANGE for c in changes):
            warnings.append(f"test {i}: keep ≤ {MAX_CHANGES} changes of ≤ {MAX_CHANGE} chars")
    metrics = {m["id"]: m for m in data.get("metrics", [])}
    if data.get("focus"):
        focus = data["focus"]
        if focus.get("area") not in AREAS:
            raise ReportError(f"focus.area must be one of {sorted(AREAS)}")
        if AREAS[focus["area"]][0] not in metrics:
            raise ReportError(f"focus needs metric `{AREAS[focus['area']][0]}` in `metrics`")
        for key in ("why", "actions"):
            lines = focus.get(key, [])
            if not lines or len(lines) > MAX_FOCUS_LINES or any(len(x) > MAX_FOCUS_LINE for x in lines):
                warnings.append(f"focus.{key}: write 1–{MAX_FOCUS_LINES} lines of ≤ {MAX_FOCUS_LINE} chars")
    if "dropoffs" in data:
        notes = data["dropoffs"]
        for st in leaking_steps(data["steps"]):
            if not notes.get(st["id"]):
                warnings.append(f"dropoffs: step `{st['id']}` is above the threshold but has no note")
        for sid, note in notes.items():
            if len(note) > MAX_NOTE:
                warnings.append(f"dropoffs: note for `{sid}` is {len(note)} chars (keep ≤ {MAX_NOTE})")
    return data, warnings


def threshold(step_id: str) -> float:
    return EMAIL_DROP_THRESHOLD if "email" in step_id.lower() else DROP_THRESHOLD


def leaking_steps(steps: list[dict]) -> list[dict]:
    """Steps after the entry step whose drop-off exceeds the threshold, most visitors lost first."""
    hits = [st for st in steps[1:] if st["drop"] > threshold(st["id"])]
    return sorted(hits, key=lambda st: (-st.get("lost", 0), -st["drop"]))


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


def page_header(data: dict, meta: str) -> str:
    return (f'<header><img class="logo" src="{(BRAND / "logo-light.svg").as_uri()}" alt="funnelsgrove">'
            f'<span class="meta">{html.escape(data["product"])} · {meta}</span></header>')


def trend_html(f: Fmt, trend: float | None) -> str:
    if trend is None:
        return ""
    cls, arrow = ("up", "▲") if trend >= 0 else ("down", "▼")
    return f'<p class="trend {cls}">{arrow} {f.pct(abs(trend))} <span>{f.s["trend"]}</span></p>'


def arrow_html(f: Fmt, trend: float | None) -> str:
    if trend is None:
        return ""
    cls, arrow = ("up", "▲") if trend >= 0 else ("down", "▼")
    return f' <i class="{cls}">{arrow} {f.pct(abs(trend))}</i>'


def render_cover(data: dict, f: Fmt, tested: dict[str, int], leaks: list[dict]) -> str:
    s, e = f.s, html.escape
    steps = {st["id"]: st for st in data["steps"]}
    tests = data["tests"]
    metrics = {m["id"]: m for m in data.get("metrics", [])}
    focus = data.get("focus")
    if focus:
        title = s["focus_title"].format(product=e(data["product"]), area=s["area"][focus["area"]])
    elif tests:
        title = s["title"].format(product=e(data["product"]), n=len(tests), tests=f.tests(len(tests)))
    else:
        title = s["dropoffs_cover"].format(product=e(data["product"]))

    rows = []  # (title, value, tag); tests outside leaking steps serve the focus when there is one
    leak_ids = {st["id"] for st in leaks} if "dropoffs" in data else set()
    other = [(i, t) for i, t in enumerate(tests, 1) if t["step"] not in leak_ids]
    if focus:
        tags = [s["area_metric"][focus["area"]]] + [s["test_n"].format(i=i) for i, _ in other]
        rows.append((s["row_focus"].format(area=s["area"][focus["area"]]),
                     f.pct(metrics[AREAS[focus["area"]][0]]["value"]), " · ".join(tags)))
    for st in leaks if "dropoffs" in data else []:
        tag = s["test_n"].format(i=tested[st["id"]]) if st["id"] in tested else ""
        rows.append((st["id"], f.pct(st["drop"]), tag))
    for i, t in other if not focus else []:
        drop = (steps.get(t["step"]) or t)["drop"]
        rows.append((t["title"], f.pct(drop), s["test_n"].format(i=i) if leak_ids else ""))
    agenda = "".join(f"""
      <li><span class="n">{i}</span><span>{e(title_)}{f'<small>{tag}</small>' if tag else ''}</span><span class="d">{value}</span></li>"""
        for i, (title_, value, tag) in enumerate(rows, 1))

    hits = set(tested) | leak_ids
    ranked = sorted(data["steps"], key=lambda st: -st["drop"])
    shown = [st for st in ranked if st["id"] in hits]
    shown += [st for st in ranked if st["id"] not in hits][:max(0, MAX_CHART_STEPS - len(shown))]
    shown = sorted(shown[:MAX_CHART_STEPS], key=lambda st: -st["drop"])
    top = max(st["drop"] for st in shown) or 1
    bars = "".join(f"""
      <div class="bar{' hit' if st['id'] in hits else ''}">
        <span>{e(st['id'])}</span>
        <span class="track"><span class="fill" style="width:{st['drop'] / top * 100:.1f}%"></span></span>
        <span class="val">{f.pct(st['drop'])}</span>
        <span class="tag">{s['test_n'].format(i=tested[st['id']]) if st['id'] in tested else ''}</span>
      </div>""" for st in shown)
    when = f.period(data["period"]) if data.get("period") else f.date(data["date"])
    sub = " · ".join(e(x) for x in (data.get("funnel"), when) if x)
    order = "" if focus or "dropoffs" in data else f"<br>{s['order']}"
    note = " · ".join(e(x) for x in (data.get("traffic_note"), s["chart_note"]) if x)
    foot = f'<p class="foot">{s["footer"].format(mde=data.get("mde_pp", 5))}</p>' if tests else ""
    return f"""
  <section class="page cover">
    <div>
      <img class="logo" src="{(BRAND / 'logo-dark.svg').as_uri()}" alt="funnelsgrove">
      <h1>{title}</h1>
      <p class="sub">{sub}{order}</p>
      <ol>{agenda}</ol>
    </div>
    <div class="chart"><h2>{s['chart']}</h2><p>{note}</p>{bars}</div>
    {foot}
  </section>"""


def render_metrics(data: dict, f: Fmt) -> str:
    s, e = f.s, html.escape
    cur = data.get("currency", "USD")
    metrics = {m["id"]: m for m in data["metrics"]}
    tiles = []
    for mid in TILES:
        m = metrics.get(mid)
        if m is None:
            continue
        ratio = f'<p class="ratio">{f.int(m["num"])} / {f.int(m["den"])}</p>' if "num" in m and "den" in m else ""
        tiles.append(f"""
        <div class="tile"><p class="tl">{s['metric_names'][mid]}</p><p class="tv">{f.metric(m, cur)}</p>{ratio}{trend_html(f, m.get('trend'))}</div>""")
    stages = ""
    if data.get("stages"):
        st = data["stages"]
        base = st.get("visitors") or 1
        cols = "".join(f"""
          <div class="stage"><span class="sv">{f.int(st[k])}</span><span class="sp">{f.pct(st[k] / base * 100)}</span>
            <span class="col"><span style="height:{max(st[k] / base * 100, 1.5):.1f}%"></span></span><span class="sl">{s['stage'][k]}</span></div>"""
            for k in STAGES if k in st)
        stages = f'<div class="stages"><p class="label">{s["funnel"]}</p><div class="cols">{cols}</div></div>'
    when = f.period(data["period"]) if data.get("period") else f.date(data["date"])
    return f"""
  <section class="page sheet">
    {page_header(data, s['metrics_title'])}
    <h2 class="h">{s['metrics_title']}</h2>
    <p class="note">{e(s['metrics_note'].format(period=when))}</p>
    <div class="tiles">{''.join(tiles)}</div>
    {stages}
  </section>"""


def render_focus(data: dict, f: Fmt) -> str:
    s, e = f.s, html.escape
    focus = data["focus"]
    metrics = {m["id"]: m for m in data["metrics"]}
    cards = []
    for area, (key, (lo, hi), context) in AREAS.items():
        m = metrics.get(key)
        if m is None:
            continue
        v = m["value"]
        scale = max(hi * 1.5, v * 1.15)
        status = s["status"][0 if v < lo else 1 if v <= hi else 2]
        lines = "".join(
            f'<p class="ctx"><span>{s["metric_names"][c]}</span><b>{f.pct(metrics[c]["value"])}{arrow_html(f, metrics[c].get("trend"))}</b></p>'
            for c in context if c in metrics)
        name = s["area"][area][:1].upper() + s["area"][area][1:]
        on = area == focus["area"]
        cards.append(f"""
      <div class="area{' on' if on else ''}">
        <p class="an">{name}{f'<span class="ftag">{s["focus_tag"]}</span>' if on else ''}</p>
        <p class="av">{f.pct(v)}</p><p class="am">{s['area_metric'][area]}{arrow_html(f, m.get('trend'))}</p>
        <div class="bench"><span class="band" style="left:{lo / scale * 100:.1f}%;width:{(hi - lo) / scale * 100:.1f}%"></span>
          <span class="mark" style="left:{min(v / scale, 1) * 100:.1f}%"></span></div>
        <p class="bs">{status} · {s['benchmark'].format(lo=lo, hi=hi)}</p>
        {lines}
      </div>""")
    why = "".join(f"<li>{e(x)}</li>" for x in focus.get("why", []))
    actions = "".join(f"<li>{e(x)}</li>" for x in focus.get("actions", []))
    return f"""
  <section class="page sheet focus">
    {page_header(data, s['focus_tag'])}
    <h2 class="h">{s['focus_h'].format(area=f'<em>{s["area"][focus["area"]]}</em>')}</h2>
    <p class="note">{s['focus_note']}</p>
    <div class="areas">{''.join(cards)}</div>
    <div class="plan">
      <div><p class="label">{s['why']}</p><ul>{why}</ul></div>
      <div><p class="label">{s['actions']}</p><ol>{actions}</ol></div>
    </div>
  </section>"""


def render_dropoffs(data: dict, f: Fmt, tested: dict[str, int], leaks: list[dict]) -> str:
    s, e = f.s, html.escape
    notes = data["dropoffs"]
    leak_ids = {st["id"] for st in leaks}
    ranked = sorted(data["steps"][1:], key=lambda st: -st["drop"])[:12]
    scale = max([st["drop"] for st in ranked] + [EMAIL_DROP_THRESHOLD]) * 1.08
    rows = "".join(f"""
        <div class="drow{' hit' if st['id'] in leak_ids else ''}">
          <span class="did">{e(st['id'])}</span>
          <span class="track"><span class="fill" style="width:{st['drop'] / scale * 100:.1f}%"></span>
            <span class="tick" style="left:{threshold(st['id']) / scale * 100:.1f}%"></span></span>
          <span class="val">{f.pct(st['drop'])}</span>
          <span class="lost">{f.int(st['lost']) if 'lost' in st else ''}</span>
        </div>""" for st in ranked)
    cards = []
    for st in leaks[:MAX_DROPOFF_CARDS]:
        lost = (s["lost"].format(lost=f.int(st["lost"]), entered=f.int(st["entered"]))
                if "lost" in st and "entered" in st else "")
        tag = f'<span class="ttag">{s["test_n"].format(i=tested[st["id"]])}</span>' if st["id"] in tested else ""
        cards.append(f"""
        <div class="dcard"><p class="eyebrow"><span class="chip">{e(st['id'])}</span>{tag}</p>
          <p class="dn">{f.pct(st['drop'])}<span>{lost} · {s['threshold'].format(t=f.num(threshold(st['id'])))}</span></p>
          <p class="dnote">{e(notes.get(st['id'], ''))}</p></div>""")
    if not leaks:
        cards.append(f'<p class="none">{s["dropoffs_none"]}</p>')
    elif len(leaks) > MAX_DROPOFF_CARDS:
        cards.append(f'<p class="more">{s["dropoffs_more"].format(n=len(leaks) - MAX_DROPOFF_CARDS)}</p>')
    rule = s["dropoffs_rule"].format(t=f.num(DROP_THRESHOLD), e=f.num(EMAIL_DROP_THRESHOLD))
    return f"""
  <section class="page sheet drops">
    {page_header(data, s['dropoffs_h'])}
    <h2 class="h">{s['dropoffs_h']}</h2>
    <p class="note">{rule}</p>
    <div class="dgrid">
      <div class="dtable"><div class="drow dhead"><span>{s['dhead'][0]}</span><span></span><span class="val">{s['dhead'][1]}</span><span class="lost">{s['dhead'][2]}</span></div>{rows}</div>
      <div class="dcards">{''.join(cards)}</div>
    </div>
  </section>"""


def render_tests(data: dict, f: Fmt, screens: dict[tuple[int, str], str]) -> list[str]:
    s, e = f.s, html.escape
    steps = {st["id"]: st for st in data["steps"]}
    tests = data["tests"]
    total = len(tests)
    mde = data.get("mde_pp", 5)
    pages = []
    for i, t in enumerate(tests, 1):
        st = steps.get(t["step"]) or t
        lost = (f"<b>{s['lost'].format(lost=f.int(st['lost']), entered=f.int(st['entered']))}</b>"
                if "lost" in st and "entered" in st else "")
        n = t.get("sample_per_variant") or sample_per_variant(1 - st["drop"] / 100, mde / 100)
        changes = "".join(f"<li>{e(c)}</li>" for c in t.get("changes", []))
        variant = t.get("variant") or f"{t['step']}-b"
        pages.append(f"""
  <section class="page test">
    {page_header(data, s['test_of'].format(i=i, n=total))}
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
    return pages


def render_html(data: dict, screens: dict[tuple[int, str], str]) -> str:
    f = Fmt(data["lang"])
    steps = {st["id"] for st in data["steps"]}
    tested = {t["step"]: i for i, t in enumerate(data["tests"], 1) if t["step"] in steps}
    leaks = leaking_steps(data["steps"])
    pages = [render_cover(data, f, tested, leaks)]
    if data.get("metrics"):
        pages.append(render_metrics(data, f))
    if data.get("focus"):
        pages.append(render_focus(data, f))
    if "dropoffs" in data:
        pages.append(render_dropoffs(data, f, tested, leaks))
    pages += render_tests(data, f, screens)
    css = (SKILL_DIR / "assets" / "report.css").read_text(encoding="utf-8")
    css = css.replace("SORA_URL", (BRAND / "Sora-variable.ttf").as_uri())
    return f"""<!doctype html>
<html lang="{data['lang']}"><head><meta charset="utf-8"><title>{html.escape(data['product'])} — funnelsgrove</title>
<style>{css}</style></head><body>
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
