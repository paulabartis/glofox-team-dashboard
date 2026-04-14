# Glofox Team Dashboard — Claude Code Instructions

## Rules

Read all PRD files before acting. Execute one task at a time from `tasks.md`. When done with a task, tell me what you did and how to test it.

**PRD files to read at the start of every session:**
- `masterplan.md` — What we're building and what success looks like
- `implementation.md` — Architecture, data sources, file structure
- `design-guidelines.md` — How the dashboard should look and feel
- `tasks.md` — Active task list; work top to bottom, one task at a time

---

## Overview

Internal team dashboard for Glofox SMB Demand Gen. Tracks weekly SQL pacing vs Q2 targets by region and shows key activities in flight by team member. Hosted on GitHub Pages.

## GitHub

- **Repo:** `github.com/paulabartis/glofox-team-dashboard` (to be created)
- **Pages URL:** `https://paulabartis.github.io/glofox-team-dashboard/`
- **Git email:** `paula@trainerize.com`
- **Branch:** `main` → deploys to GitHub Pages

## Key Files

```
team-dashboard/
├── CLAUDE.md                    ← You are here
├── masterplan.md                ← Goals and success criteria
├── implementation.md            ← Architecture and data sources
├── design-guidelines.md         ← Visual and UX standards
├── tasks.md                     ← Task list
├── index.html                   ← Main dashboard (output of generate_dashboard.py)
├── dashboard/
│   └── template.html            ← Source template with all JS/CSS baked in
├── scripts/
│   └── generate_dashboard.py    ← Reads data/ → writes index.html from template
└── data/
    └── q2_plan.json             ← Source of truth for targets + activities (manual update)
```

## Data Architecture

- `data/q2_plan.json` — manually maintained; holds Q2 targets, weekly actuals, and in-flight activities
- `scripts/generate_dashboard.py` — reads `q2_plan.json` + template → outputs `index.html`
- No Google Sheets dependency for this dashboard (self-contained)

## Git Push Pattern

PAT needed for push. Temporarily inject into remote URL:
```bash
git remote set-url origin "https://paulabartis:PAT@github.com/paulabartis/glofox-team-dashboard.git"
# push
git remote set-url origin "https://github.com/paulabartis/glofox-team-dashboard.git"
```
