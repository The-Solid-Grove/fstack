#!/usr/bin/env python3
"""Draft report JSON from `fgrove analytics conversions --format json` output.

Usage:
  analytics_to_report.py ANALYTICS.json [--product NAME] [--lang ru|en] > report.json

Fills `period`, `metrics`, `stages` and `steps` with the dashboard's numbers so
they are never retyped. The agent then writes `focus`, `dropoffs` and `tests`.
Steps keep the analytics path order (entry step first) and stop before the
paywall: the paywall and post-purchase steps belong to the paywall focus area.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

RATE_METRICS = (
    "visitor_to_quiz_start", "quiz_start_to_email", "visitor_to_finish_quiz", "paywall_to_checkout",
    "checkout_to_subscription", "paywall_to_subscription", "visitor_to_subscription",
)
# Mirrors the dashboard's post-paywall classifiers (projectAnalyticsFunnelPathChart.service.ts).
POST_PAYWALL = ("paywall", "checkout", "upsell", "manage-subscription", "subscription-started",
                "subscription-success", "registration", "handoff")


def is_quiz_step(step_id: str) -> bool:
    s = step_id.lower()
    if "email" in s:
        return True
    return s != "subscription" and not any(k in s for k in POST_PAYWALL)


def convert(a: dict, product: str | None, lang: str) -> dict:
    by_id = {m["id"]: m for m in a["metrics"]}
    metrics = [{"id": "visitors", "value": a["totals"]["visitors"]}]
    for mid in RATE_METRICS:
        m = by_id.get(mid)
        if m is None:
            continue
        prev = m.get("previousPeriod") or {}
        metrics.append({"id": mid, "value": round(m["rate"] * 100, 2), "num": m["numerator"],
                        "den": m["denominator"], "trend": prev.get("trendPercent")})
    t = a["totals"]
    if t["visitors"]:
        metrics.append({"id": "visitor_to_checkout", "value": round(t["checkoutStarts"] / t["visitors"] * 100, 2),
                        "num": t["checkoutStarts"], "den": t["visitors"]})
    ov = a["overview"]["totals"]
    metrics += [{"id": "net_revenue", "value": ov["netRevenueMinor"] / 100},
                {"id": "arppu", "value": round(ov["arppuMinor"] / 100, 2)}]
    steps = [{"id": s["stepId"], "drop": round(s["dropoffRate"] * 100, 1), "lost": s["dropoffs"], "entered": s["users"]}
             for s in a["funnelPath"] if s["users"] > 0 and is_quiz_step(s["stepId"])]
    return {
        "lang": lang,
        "product": product or a["project"]["name"],
        "funnel": a["funnel"]["name"],
        "date": dt.date.today().isoformat(),
        "period": {"from": a["from"], "to": a["to"]},
        "currency": a["overview"].get("currency", "USD"),
        "metrics": metrics,
        "stages": {"visitors": t["visitors"], "quiz_starts": t["quizStarts"], "email_adds": t["emailAdds"],
                   "paywall_views": t["paywallViews"], "checkout_starts": t["checkoutStarts"],
                   "subscriptions": t["subscriptions"]},
        "steps": steps,
        "focus": {"area": "", "why": [], "actions": []},
        "dropoffs": {},
        "tests": [],
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("analytics", type=Path)
    ap.add_argument("--product")
    ap.add_argument("--lang", default="ru", choices=("ru", "en"))
    args = ap.parse_args(argv)
    data = convert(json.loads(args.analytics.read_text(encoding="utf-8")), args.product, args.lang)
    json.dump(data, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
