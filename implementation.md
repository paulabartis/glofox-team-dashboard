# Implementation — Glofox Team Dashboard

## Architecture

**Fully static.** No backend, no APIs, no auth.

```
data/q2_plan.json          ← Paula edits this weekly (targets + actuals + activities)
        ↓
scripts/generate_dashboard.py  ← Reads JSON, renders template, writes index.html
        ↓
dashboard/template.html    ← HTML/CSS/JS source template (Jinja2 variables)
        ↓
index.html                 ← Final output, committed to repo → GitHub Pages serves it
```

---

## Data File: `data/q2_plan.json`

Single source of truth. Paula (or team lead) updates this weekly.

```json
{
  "meta": {
    "q2_start": "2026-04-01",
    "q2_end": "2026-06-30",
    "q2_weeks_total": 13,
    "last_updated": "2026-04-14"
  },
  "targets": {
    "NA": 1052,
    "EMEA": 750,
    "APAC": null
  },
  "actuals": {
    "NA": { "q2_to_date": 0, "april": 0 },
    "EMEA": { "q2_to_date": 0, "april": 0 },
    "APAC": { "q2_to_date": 0, "april": 0 }
  },
  "april_target": {
    "NA": 0,
    "EMEA": 0,
    "APAC": 0,
    "total_low": 486,
    "total_high": 503,
    "total_aop": 659
  },
  "activities": [
    {
      "owner": "Kaeli Allen",
      "title": "Activity name",
      "status": "active",
      "impact": "high",
      "target_week": "W3 May"
    }
  ]
}
```

---

## Script: `scripts/generate_dashboard.py`

1. Load `data/q2_plan.json`
2. Calculate derived metrics:
   - Weeks elapsed (today − q2_start) / 7
   - Pacing % = actuals_to_date / (weeks_elapsed / 13 × target)
   - Weekly run rate needed = (target − actuals_to_date) / weeks_remaining
3. Load `dashboard/template.html`
4. Inject data via Jinja2
5. Write to `index.html`

**Dependencies:** `jinja2` (already in `requirements.txt`)

---

## Template: `dashboard/template.html`

- Self-contained HTML file — all CSS and JS inline, no external CDN dependencies
- Uses Jinja2 `{{ variable }}` and `{% for %}` blocks
- Visual style: matches Glofox paid dashboard (dark navy + accent colors)

---

## GitHub Pages Setup

1. Create repo `glofox-team-dashboard` under `paulabartis` GitHub account
2. Push `main` branch
3. Settings → Pages → Source: `main` branch, root `/`
4. `index.html` at repo root is what GitHub Pages serves

---

## Update Workflow (weekly)

```bash
# 1. Edit actuals in data/q2_plan.json
# 2. Regenerate
python scripts/generate_dashboard.py

# 3. Commit and push
git add index.html data/q2_plan.json
git commit -m "chore: update Q2 pacing — week of Apr 14"
git remote set-url origin "https://paulabartis:PAT@github.com/paulabartis/glofox-team-dashboard.git"
git push origin main
git remote set-url origin "https://github.com/paulabartis/glofox-team-dashboard.git"
```

---

## File Structure

```
team-dashboard/
├── CLAUDE.md
├── masterplan.md
├── implementation.md
├── design-guidelines.md
├── tasks.md
├── index.html                  ← Generated output (committed)
├── .gitignore
├── dashboard/
│   └── template.html           ← Jinja2 template
├── scripts/
│   └── generate_dashboard.py
└── data/
    └── q2_plan.json            ← Manual data input
```
