"""
generate_dashboard.py
Glofox Team Dashboard generator.

Usage:
    python scripts/generate_dashboard.py

Reads:  data/q2_plan.json
Writes: index.html (from dashboard/template.html via Jinja2, or a stub if template absent)
"""

import json
import os
from datetime import date, datetime
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "q2_plan.json"
TEMPLATE_FILE = ROOT / "dashboard" / "template.html"
OUTPUT_FILE = ROOT / "index.html"


# ── Status helpers ─────────────────────────────────────────────────────────────
def pacing_status(pacing_pct, target):
    """Return status string based on pacing percentage."""
    if target is None:
        return "tbc"
    if pacing_pct is None:
        return "tbc"
    if pacing_pct >= 0.95:
        return "on_track"
    if pacing_pct >= 0.80:
        return "at_risk"
    return "behind"


def format_pct(value, decimals=1):
    """Format a decimal as a percentage string."""
    if value is None:
        return "—"
    return f"{value * 100:.{decimals}f}%"


def fmt(value, prefix="", suffix=""):
    """Format a number with comma separators, or return '—' for None."""
    if value is None:
        return "—"
    return f"{prefix}{value:,}{suffix}"


# ── Core calculations ──────────────────────────────────────────────────────────
def build_context(data):
    q2_start = date.fromisoformat(data["meta"]["q2_start"])
    today = date.today()
    last_updated = data["meta"]["last_updated"]

    days_elapsed = (today - q2_start).days
    weeks_elapsed = days_elapsed / 7
    weeks_remaining = data["meta"]["q2_weeks_total"] - weeks_elapsed
    expected_pct = weeks_elapsed / data["meta"]["q2_weeks_total"]

    # ISO week number
    week_number = today.isocalendar()[1]

    # ── Region cards ──
    regions = []
    for name in ["NA", "EMEA", "APAC"]:
        target_q2 = data["targets"]["q2"].get(name)
        actuals_q2 = data["actuals"]["q2_to_date"].get(name, 0)
        april_actual = data["actuals"]["april"].get(name, 0)
        april_aop = data["targets"]["april"]["aop"].get(name)
        april_pacing = data["targets"]["april"]["current_pacing"].get(name)
        cvr = data.get("cvr_march", {}).get(name, {})

        if target_q2 and expected_pct > 0:
            pacing_pct = actuals_q2 / (expected_pct * target_q2)
        else:
            pacing_pct = None

        run_rate_needed = None
        if target_q2 and weeks_remaining > 0:
            run_rate_needed = (target_q2 - actuals_q2) / weeks_remaining

        status = pacing_status(pacing_pct, target_q2)

        regions.append({
            "name": name,
            "target_q2": target_q2,
            "actuals_q2": actuals_q2,
            "expected_pct": expected_pct,
            "pacing_pct": pacing_pct,
            "pacing_pct_display": format_pct(pacing_pct),
            "run_rate_needed": run_rate_needed,
            "run_rate_needed_display": f"{run_rate_needed:.0f}/wk" if run_rate_needed else "—",
            "status": status,
            "april_actual": april_actual,
            "april_aop": april_aop,
            "april_current_pacing": april_pacing,
            "april_gap_vs_aop": (april_pacing - april_aop) if (april_pacing is not None and april_aop) else None,
            "cvr_paid": cvr.get("paid"),
            "cvr_np": cvr.get("np"),
            "cvr_paid_display": format_pct(cvr.get("paid")),
            "cvr_np_display": format_pct(cvr.get("np")),
        })

    # ── April overview ──
    april_actuals_total = data["actuals"]["april"]["total"]
    april_aop_total = data["targets"]["april"]["aop"]["total"]
    april_pacing_total = data["targets"]["april"]["current_pacing"]["total"]
    april_pacing_vs_aop = april_actuals_total / april_aop_total if april_aop_total else 0

    april = {
        "aop_total": april_aop_total,
        "current_pacing_total": april_pacing_total,
        "actuals_total": april_actuals_total,
        "pacing_vs_aop_pct": april_pacing_vs_aop,
        "gap_vs_aop": april_pacing_total - april_aop_total,
        "gap_display": f"{april_pacing_total - april_aop_total:+,}",
    }

    # ── Q2 scenarios ──
    q2_scenarios = data["targets"]["q2_scenarios"]

    return {
        "meta": data["meta"],
        "last_updated": last_updated,
        "week_number": week_number,
        "weeks_elapsed": round(weeks_elapsed, 1),
        "weeks_remaining": round(weeks_remaining, 1),
        "expected_pct": expected_pct,
        "regions": regions,
        "april": april,
        "q2_scenarios": q2_scenarios,
        "activities": data["activities"],
        # helpers available in template
        "fmt": fmt,
        "format_pct": format_pct,
    }


# ── Render ─────────────────────────────────────────────────────────────────────
def render(context):
    if TEMPLATE_FILE.exists():
        try:
            from jinja2 import Environment, FileSystemLoader
            env = Environment(
                loader=FileSystemLoader(str(TEMPLATE_FILE.parent)),
                autoescape=False,
            )
            template = env.get_template(TEMPLATE_FILE.name)
            return template.render(**context)
        except ImportError:
            print("WARNING: jinja2 not installed — writing stub. Run: pip install jinja2")

    # Stub output when template is absent or jinja2 missing
    regions_summary = "\n".join(
        f"  {r['name']}: {r['actuals_q2']:,} / {r['target_q2']:,} SQLs | "
        f"April pacing {r['april_current_pacing']:,} vs AOP {r['april_aop']:,}"
        for r in context["regions"]
    )
    april = context["april"]
    stub = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Glofox Team Dashboard — Stub</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
            background: #0f1117; color: #e8eaf0; padding: 40px; line-height: 1.6; }}
    h1 {{ color: #4f8ef7; }}
    pre {{ background: #1a1d27; border: 1px solid #2a2d3e; border-radius: 8px;
           padding: 20px; white-space: pre-wrap; }}
    .ok {{ color: #2ecc71; font-weight: 600; }}
  </style>
</head>
<body>
  <h1>Glofox Team Dashboard</h1>
  <p class="ok">generate_dashboard.py ran successfully — Week {context['week_number']} · {context['last_updated']}</p>
  <p>Template not found at <code>dashboard/template.html</code>. Create it to render the full dashboard.</p>
  <pre>
Q2 Pacing ({context['weeks_elapsed']} weeks elapsed):
{regions_summary}

April Overview:
  Current pacing: {april['current_pacing_total']:,} SQL (11-day extrapolation)
  AOP target:     {april['aop_total']:,} SQL
  Gap vs AOP:     {april['gap_display']} SQL

Activities loaded:
  Paid:      {len(context['activities'].get('paid', []))} items
  Non-Paid:  {len(context['activities'].get('non_paid', []))} items
  Web/SEO:   {len(context['activities'].get('web_seo', []))} items
  </pre>
</body>
</html>"""
    return stub


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Data file not found: {DATA_FILE}")

    with open(DATA_FILE) as f:
        data = json.load(f)

    context = build_context(data)
    html = render(context)

    with open(OUTPUT_FILE, "w") as f:
        f.write(html)

    april = context["april"]
    print(f"Done — index.html written ({OUTPUT_FILE.stat().st_size:,} bytes)")
    print(f"Week {context['week_number']} · {context['weeks_elapsed']} weeks elapsed")
    print(f"April pacing: {april['current_pacing_total']:,} SQL vs AOP {april['aop_total']:,} ({april['gap_display']})")


if __name__ == "__main__":
    main()
