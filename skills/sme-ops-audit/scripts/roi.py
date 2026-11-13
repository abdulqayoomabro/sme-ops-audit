#!/usr/bin/env python3
"""ROI calculator for SME Ops Audit.

Input: a JSON file with either a list of opportunities or
{"currency": "PKR", "opportunities": [...]}.

Each opportunity:
  name                      str    required
  hours_saved_per_week      float  staff hours freed per week            (default 0)
  hourly_cost               float  cost of one staff hour; or give
  monthly_salary            float  -> hourly = salary / 208              (default 0)
  loss_avoided_per_month    float  errors, waste, bad debt avoided/month (default 0)
  extra_revenue_per_month   float  only if the owner can justify it      (default 0)
  setup_cost                float  one-time: software, hardware, setup, training (default 0)
  monthly_cost              float  subscriptions, hosting, support       (default 0)
  confidence                str    "owner" | "estimate" | "assumption"   (default "estimate")

Output: a markdown table per opportunity plus totals, 12-month net benefit and
payback in months. Usage:
  python3 roi.py opportunities.json [--lang en|ur] [--json]
"""
import argparse
import json
import math
import sys

WEEKS_PER_MONTH = 52 / 12
HOURS_PER_MONTH = 208  # 48 h/week, common 6-day week in Pakistan

LABELS = {
    "en": {
        "name": "Opportunity", "hours": "Hours saved/month", "benefit": "Monthly benefit",
        "cost": "Monthly cost", "net": "Net/month", "setup": "Setup cost",
        "payback": "Payback (months)", "y1": "12-month net", "conf": "Basis",
        "total": "TOTAL", "never": "never",
        "note": "Estimates built from the inputs above, not guarantees.",
    },
    "ur": {
        "name": "Mauqa", "hours": "Ghante bache/mahina", "benefit": "Mahana faida",
        "cost": "Mahana kharcha", "net": "Saaf faida/mahina", "setup": "Shuru ka kharcha",
        "payback": "Paisa wapas (mahine)", "y1": "12 mahine ka saaf faida", "conf": "Bunyad",
        "total": "KUL", "never": "kabhi nahi",
        "note": "Ye andaze upar diye gaye numbers par mabni hain, guarantee nahi.",
    },
}
CONF = {"en": {"owner": "Owner said", "estimate": "Estimate", "assumption": "Assumption"},
        "ur": {"owner": "Owner ne bataya", "estimate": "Andaza", "assumption": "Farz kiya"}}


def num(d, key):
    v = d.get(key, 0) or 0
    try:
        v = float(v)
    except (TypeError, ValueError):
        sys.exit(f"'{key}' must be a number in '{d.get('name', '?')}', got {v!r}")
    if v < 0:
        sys.exit(f"'{key}' cannot be negative in '{d.get('name', '?')}'")
    return v


def calc(op):
    if not op.get("name"):
        sys.exit("Every opportunity needs a 'name'.")
    hourly = num(op, "hourly_cost") or num(op, "monthly_salary") / HOURS_PER_MONTH
    hours_m = num(op, "hours_saved_per_week") * WEEKS_PER_MONTH
    benefit = hours_m * hourly + num(op, "loss_avoided_per_month") + num(op, "extra_revenue_per_month")
    cost = num(op, "monthly_cost")
    setup = num(op, "setup_cost")
    net = benefit - cost
    payback = (setup / net if net > 0 else math.inf) if setup else 0.0
    return {
        "name": op["name"], "confidence": op.get("confidence", "estimate"),
        "hours_per_month": hours_m, "monthly_benefit": benefit, "monthly_cost": cost,
        "net_per_month": net, "setup_cost": setup, "payback_months": payback,
        "net_12_months": net * 12 - setup,
    }


def money(v, cur):
    return f"{cur} {v:,.0f}"


def fmt_payback(p, lab):
    return lab["never"] if math.isinf(p) else f"{p:.1f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--lang", choices=["en", "ur"], default="en")
    ap.add_argument("--json", action="store_true", help="print machine-readable results")
    a = ap.parse_args()

    with open(a.file, encoding="utf-8") as f:
        data = json.load(f)
    cur = "PKR"
    if isinstance(data, dict):
        cur = data.get("currency", cur)
        data = data.get("opportunities", [])
    if not data:
        sys.exit("No opportunities found.")

    rows = [calc(op) for op in data]
    tot = {k: sum(r[k] for r in rows) for k in
           ("hours_per_month", "monthly_benefit", "monthly_cost", "net_per_month", "setup_cost", "net_12_months")}
    tot["payback_months"] = (tot["setup_cost"] / tot["net_per_month"] if tot["net_per_month"] > 0 else math.inf) \
        if tot["setup_cost"] else 0.0

    if a.json:
        clean = lambda r: {k: (None if isinstance(v, float) and math.isinf(v) else v) for k, v in r.items()}
        print(json.dumps({"currency": cur, "opportunities": [clean(r) for r in rows], "total": clean(tot)}, indent=2))
        return

    L, C = LABELS[a.lang], CONF[a.lang]
    head = [L["name"], L["hours"], L["benefit"], L["cost"], L["net"], L["setup"], L["payback"], L["y1"], L["conf"]]
    print("| " + " | ".join(head) + " |")
    print("|" + "|".join(["---"] + ["---:"] * 7 + ["---"]) + "|")

    def line(r, name, conf):
        cells = [name, f"{r['hours_per_month']:.0f}", money(r["monthly_benefit"], cur), money(r["monthly_cost"], cur),
                 money(r["net_per_month"], cur), money(r["setup_cost"], cur), fmt_payback(r["payback_months"], L),
                 money(r["net_12_months"], cur), conf]
        print("| " + " | ".join(cells) + " |")

    for r in rows:
        line(r, r["name"], C.get(r["confidence"], r["confidence"]))
    line(tot, f"**{L['total']}**", "")
    print(f"\n_{L['note']}_")


if __name__ == "__main__":
    main()
