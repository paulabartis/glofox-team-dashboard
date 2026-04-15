# Implementation — Glofox Team Dashboard

## Architecture

**Fully static.** No backend, no APIs, no auth.

```
data/q2_plan.json              ← Paula edits this weekly
        ↓
scripts/generate_dashboard.py  ← Reads JSON, renders template, writes index.html
        ↓
dashboard/template.html        ← Jinja2 HTML/CSS/JS source
        ↓
index.html                     ← Committed to repo → GitHub Pages serves it
```

---

## Weekly Update — What to Change in `q2_plan.json`

These are the only fields that change week to week. Everything else (targets, scenarios, activities) stays fixed unless there's a structural change.

### 1. Meta
```json
"meta": {
  "last_updated": "2026-04-21"   ← update to Monday of current week
}
```

### 2. Q2 actuals to date (cumulative)
```json
"actuals": {
  "q2_to_date": { "NA": 0, "EMEA": 0, "APAC": 0 },
  "april":      { "NA": 0, "EMEA": 0, "APAC": 0, "total": 0 }
}
```
`q2_to_date` = total SQLs since Apr 1. `april` = April-only raw SQLs (used for Live Trajectory calc).

### 3. April 11-day pacing (or latest partial-month actuals)
```json
"targets": {
  "april": {
    "current_pacing": { "NA": 243, "EMEA": 166, "APAC": 25, "total": 434 }
  }
}
```
This is the extrapolated full-month forecast (raw actuals × 30 / days elapsed). Update every week.

### 4. CVR trend (blended per region, April actual)
```json
"april_11d": {
  "cvr_trend": {
    "NA":   { "mar": 0.207, "apr": 0.189 },
    "EMEA": { "mar": 0.187, "apr": 0.188 },
    "APAC": { "mar": 0.340, "apr": 0.176 }
  }
}
```
`mar` stays fixed (March actuals baseline). Update `apr` each week with latest blended CVR.

### 5. April 11-day build table (if you want to refresh the detailed table)
Inside `april_11d.regions.[NA/EMEA/APAC].paid` and `.non_paid`:
- `apr_mql`, `apr_sql`, `apr_cvr`, `delta` — update with latest actuals

---

## Regenerate + Push

```bash
# From the team-dashboard directory:
python3 scripts/generate_dashboard.py

git add index.html data/q2_plan.json
git commit -m "chore: update Q2 pacing — week of Apr 21"

# Inject PAT, push, restore URL:
git remote set-url origin "https://paulabartis:PAT@github.com/paulabartis/glofox-team-dashboard.git"
git push origin main
git remote set-url origin "https://github.com/paulabartis/glofox-team-dashboard.git"
```

---

## Dashboard Sections (current state)

### Tab 1: Overview
| Section | What it shows |
|---|---|
| April Spotlight banner | Current pacing SQL vs AOP 659, gap, % below |
| Progress bar | 11-day pacing % vs AOP |
| 3 region cards | Pacing SQL, AOP, gap, progress bar, pace arrows vs March, Total/Paid/NP CVR |
| Q2 Scenario Range | 6 rows: Worst / Hold-Rate / Live Trajectory / Q2 Current Pacing / Best Case / AOP. Projected SQL + % of Q2 AOP per geo. |
| April 11-day build | Paid + NP breakdown per region with Mar/Apr SQL, CVR, AOP, delta |

### Tab 2: Roadmap
| Section | What it shows |
|---|---|
| Filter bar | Month (All/Apr/May/Jun) · Region (All/NA/EMEA/APAC) · Impact type (All/CVR/Volume) |
| 3 activity columns | Paid / Non-Paid / Web & SEO — 32 activities with status badge, impact tier, sql_impact, owner |

---

## Activity Schema (`data/q2_plan.json`)

```json
{
  "title": "Search NA — Competitor RSA audit + MindBody copy test",
  "bucket": "paid",
  "status": "in progress",
  "impact": "high",
  "region": "NA",
  "owner": "Aman",
  "target_week": "April",
  "kpi": "CVR",
  "sql_impact": "+174",
  "segment": "SMB"
}
```

**Status values:** `not started` · `in progress` · `complete` · `blocked`
**Impact values:** `high` · `medium` · `low`
**KPI values:** `CVR` · `MQL` · `SQL` · `Traffic`
**Bucket values:** `paid` · `non_paid` · `web_seo`

---

## Key URLs

- **Live dashboard:** `https://paulabartis.github.io/glofox-team-dashboard/`
- **Repo:** `https://github.com/paulabartis/glofox-team-dashboard`

---

## File Structure

```
team-dashboard/
├── CLAUDE.md
├── masterplan.md
├── implementation.md        ← this file
├── design-guidelines.md
├── tasks.md
├── index.html               ← generated output (committed)
├── .nojekyll                ← prevents GitHub Pages Jekyll processing
├── .gitignore
├── dashboard/
│   └── template.html        ← Jinja2 template (all CSS/JS inline)
├── scripts/
│   └── generate_dashboard.py
└── data/
    └── q2_plan.json         ← single source of truth
```

---

## Status Thresholds

| Pacing % | Status | Colour |
|---|---|---|
| ≥ 95% | on_track | Green |
| 80–94% | at_risk | Amber |
| < 80% | behind | Red |
| target null | tbc | Muted |
