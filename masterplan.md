# Masterplan — Glofox Team Dashboard

## What We're Building

A lightweight internal HTML dashboard, hosted on GitHub Pages, that gives Paula and the Glofox SMB demand gen team a single view of:

1. **Weekly SQL pacing** — actuals vs Q2 targets by region (NA, EMEA, APAC)
2. **Key activities in flight** — what each team member owns this quarter, status, and impact tier

No logins, no data pipelines. A single `index.html` that gets regenerated when data is updated.

---

## Who It's For

| Audience | Use |
|----------|-----|
| Paula | Weekly status check; stakeholder share-out |
| Kaeli, Tanya, Angharad, Aman, Jaxon | Self-serve view of team activity and pacing |
| Lacey Ford / CRO stakeholders | Optional: link to share progress |

---

## Q2 Targets (source of truth)

| Region | Q2 SQL Target | Primary lever |
|--------|--------------|---------------|
| NA | 1,052 | CVR (goal 25%) |
| EMEA | 750 | CVR (goal 25%) |
| APAC | TBC (Angharad to confirm) | Paid expansion + CVR |

**Overall best-case operating plan:** 1,696 SMB SQLs

---

## Team Structure

| Name | Role | Focus |
|------|------|-------|
| Kaeli Allen | Demand Gen Manager | SMB demand gen |
| Tanya Stricker | Sr. Director, Demand Gen | NA + EMEA |
| Angharad Saynor | Demand Gen Lead | APAC |
| Aman Dayal | Performance Marketing Lead | Paid (Google, Meta) |
| Jaxon Lam | Sr. Director, Growth (PLG) | TZ / PLG growth |

---

## Dashboard Sections

### 1. Header
- Dashboard title, week number, last updated date

### 2. Q2 Pacing — Regional SQL Tracker
- Three region cards: NA | EMEA | APAC
- Each card shows:
  - Q2 target
  - Actuals to date
  - % paced (actuals / (weeks elapsed / 13 weeks × target))
  - Weekly run rate needed to hit target
  - Status indicator: on track / at risk / behind

### 3. April Spotlight
- April SQL target vs actuals (486–503 SQL vs 659 AOP)
- Simple progress bar per region

### 4. Activities in Flight — By Team Member
- Card per person (Kaeli, Tanya, Angharad, Aman, Jaxon)
- Each card lists their active Q2 initiatives with:
  - Activity name
  - Status: `active` | `in progress` | `blocked` | `complete`
  - Impact tier: `high` | `medium` | `low`
  - Target completion / go-live week

### 5. Footer
- Last updated timestamp
- Link to Q2 Demand Plan deck (optional)

---

## Success Criteria

- [ ] Dashboard loads correctly on GitHub Pages
- [ ] Pacing % and run rates calculate correctly based on weeks elapsed
- [ ] Data update requires only editing `data/q2_plan.json` + re-running `generate_dashboard.py`
- [ ] Looks clean and readable on desktop (not required on mobile)
- [ ] Paula can share the URL in Slack or email
