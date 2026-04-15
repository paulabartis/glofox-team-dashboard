# Tasks — Glofox Team Dashboard

Work through these one at a time. Do not start the next task until the current one is verified working.

**Status key:** `[ ]` = not started · `[~]` = in progress · `[x]` = done · `[!]` = blocked

---

## Phase 1 — Foundation

### Task 1: Scaffold data file and generator script
- [x] Create `data/q2_plan.json` with targets, actuals, activities, and CVR data
- [x] Create `scripts/generate_dashboard.py` (Jinja2, pacing %, run rate, live trajectory)
- [x] Verified: runs without errors

### Task 2: Build dashboard template
- [x] Header: title ("Grow Demand Team"), week label, last updated
- [x] Tab nav: Overview | Roadmap
- [x] Overview — April Spotlight: banner, progress bar, 3 region cards with pace arrows + CVR line
- [x] Overview — Q2 Scenario Range table: 6 scenarios with % of target per geo, Live Trajectory row
- [x] Overview — April 11-day build table: paid + NP breakdown per region
- [x] Roadmap tab: activities filtered by Month / Region / Impact type
- [x] Verified: generates valid index.html, opens correctly in browser

### Task 3: Git setup and GitHub Pages
- [x] Repo created: `paulabartis/glofox-team-dashboard`
- [x] GitHub Pages live: `https://paulabartis.github.io/glofox-team-dashboard/`
- [x] `.nojekyll` in root (prevents Jekyll mangling Jinja2 output)

---

## Phase 2 — Weekly Upkeep

### Task 4: Populate activities with real Q2 initiatives
- [x] All 32 activities seeded from XLSX (Paid / Non-Paid / Web-SEO buckets)
- [x] Each activity has: title, bucket, status, impact, region, owner, target_week, kpi, sql_impact, segment
- [ ] Paula to update status / notes as initiatives progress

### Task 5: Weekly data update (first due w/c Apr 21)
- [ ] Update `actuals.q2_to_date` and `actuals.april` in `q2_plan.json`
- [ ] Update `targets.april.current_pacing` (11-day → 30-day extrapolation per region)
- [ ] Update `april_11d` table rows (paid + NP actuals per region)
- [ ] Update `april_11d.cvr_trend` (blended CVR per region, mar stays fixed, update apr)
- [ ] Update `meta.last_updated`
- [ ] Regenerate + commit + push (see `implementation.md` for exact commands)

---

## Phase 3 — Enhancements (backlog)

- [ ] APAC targets — add once Angharad confirms (currently 90 AOP placeholder)
- [ ] Weekly pacing trend sparkline (SVG, no external libs) — show trajectory over Q2 weeks
- [ ] MQL pacing layer alongside SQL pacing
- [ ] Activity status update flow — easy way for team members to update their own rows
- [ ] Slack-friendly summary export (markdown text block for weekly standup)
- [ ] Completed activities toggle on Roadmap tab
