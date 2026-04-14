# Tasks — Glofox Team Dashboard

Work through these one at a time. Do not start the next task until the current one is verified working.

**Status key:** `[ ]` = not started · `[~]` = in progress · `[x]` = done · `[!]` = blocked

---

## Phase 1 — Foundation

### Task 1: Scaffold data file and generator script
- [ ] Create `data/q2_plan.json` with initial structure (targets, empty actuals, placeholder activities)
  - NA target: 1,052 | EMEA target: 750 | APAC: null (TBC)
  - April total: low 486, high 503, AOP 659
  - Add 2–3 placeholder activities per team member (Paula to fill in real ones)
- [ ] Create `scripts/generate_dashboard.py`
  - Load JSON, calculate weeks elapsed, pacing %, run rate needed
  - Load template, render with Jinja2, write `index.html`
- [ ] Verify: `python scripts/generate_dashboard.py` runs without errors

### Task 2: Build dashboard template
- [ ] Create `dashboard/template.html` — self-contained HTML/CSS/JS
- [ ] Header section: title, week label, last updated
- [ ] Regional pacing cards (3-column): NA | EMEA | APAC
  - Target, actuals, pacing %, run rate, status badge, progress bar
- [ ] April spotlight section: total range vs AOP, regional breakdown
- [ ] Activities in flight: card per team member with activity rows
- [ ] Verify: `generate_dashboard.py` outputs a valid `index.html` and it opens correctly in browser

### Task 3: Git setup and GitHub Pages
- [ ] `git init` in `team-dashboard/`
- [ ] Set git config: `user.email = paula@trainerize.com`, `user.name = Paula`
- [ ] Create `.gitignore`
- [ ] Initial commit (all files)
- [ ] Create repo on GitHub: `paulabartis/glofox-team-dashboard`
- [ ] Push `main` branch
- [ ] Enable GitHub Pages (Settings → Pages → main branch, root)
- [ ] Verify: dashboard loads at `https://paulabartis.github.io/glofox-team-dashboard/`

---

## Phase 2 — Real Data

### Task 4: Populate activities with real Q2 initiatives
- [ ] Paula reviews and fills in actual Q2 activities per team member in `q2_plan.json`
- [ ] Regenerate and push

### Task 5: First weekly update
- [ ] Update actuals in `q2_plan.json` with first week of Q2 SQL data
- [ ] Update `last_updated` date
- [ ] Regenerate, commit, push

---

## Phase 3 — Enhancements (backlog)

- [ ] Weekly pacing trend chart (SVG line chart, no external libs)
- [ ] APAC targets — add once Angharad confirms
- [ ] MQL pacing layer (in addition to SQL)
- [ ] Activity history / completed items toggle
- [ ] Slack-friendly summary export (markdown text block)
