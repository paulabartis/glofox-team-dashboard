# Design Guidelines — Glofox Team Dashboard

## Principles

- **Clarity over decoration.** Every element earns its place.
- **Scannable in 30 seconds.** A team member should know the status of pacing and their activities at a glance.
- **Consistent with the Glofox paid dashboard.** Same palette and card style so it feels like a suite.

---

## Color Palette

Match the existing Glofox paid dashboard (`dashboard/template.html`).

| Token | Hex | Use |
|-------|-----|-----|
| `bg-dark` | `#0f1117` | Page background |
| `bg-card` | `#1a1d27` | Card background |
| `bg-card-alt` | `#1e2133` | Alternate card / section bg |
| `border` | `#2a2d3e` | Card borders |
| `text-primary` | `#e8eaf0` | Main text |
| `text-muted` | `#8b8fa8` | Labels, secondary text |
| `accent-blue` | `#4f8ef7` | Primary metric, links |
| `accent-green` | `#2ecc71` | On track |
| `accent-amber` | `#f39c12` | At risk |
| `accent-red` | `#e74c3c` | Behind / blocked |
| `accent-purple` | `#9b59b6` | Highlights / April spotlight |

---

## Status Indicators

### Pacing Status (Regional Cards)

| Condition | Label | Color |
|-----------|-------|-------|
| ≥ 95% of pace | On Track | Green |
| 80–94% of pace | At Risk | Amber |
| < 80% of pace | Behind | Red |
| APAC target TBC | TBC | Muted |

### Activity Status (Team Cards)

| Status value | Badge color |
|-------------|-------------|
| `active` | Green |
| `in progress` | Blue |
| `blocked` | Red |
| `complete` | Muted gray |

### Impact Tier (Activity Cards)

| Tier | Display |
|------|---------|
| `high` | Bold label |
| `medium` | Normal |
| `low` | Muted |

---

## Layout

- Max-width: `1200px`, centered
- Section padding: `24px`
- Card gap: `16px`
- Border radius: `8px`

### Regional Pacing Cards
- 3-column grid (NA | EMEA | APAC) on desktop
- Each card: target, actuals to date, pacing %, run rate needed, status badge
- Progress bar showing % of Q2 elapsed vs % of target achieved

### April Spotlight
- Horizontal card spanning full width
- April total: range (486–503) vs AOP (659)
- Simple `<progress>` or bar per region

### Activities in Flight
- 1 card per team member, 2–3 columns grid
- Team member name + role as card header
- Activity rows: title | status badge | impact | target week

---

## Typography

```css
font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif;
```

| Element | Size | Weight |
|---------|------|--------|
| Page title | 24px | 600 |
| Section heading | 14px uppercase | 600, letter-spacing 0.08em |
| Card metric (big number) | 32px | 700 |
| Card label | 12px | 400, muted |
| Body / activity text | 14px | 400 |
| Badge | 11px | 600, uppercase |

---

## What to Avoid

- No external CDN fonts or icon libraries (self-contained only)
- No animations — static and readable
- No mobile breakpoints needed for v1 (desktop only)
- No login wall or interactivity beyond hover states
