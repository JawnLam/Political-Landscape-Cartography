---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-campaign-type
title: "PLC_Campaign — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
type_namespace: plc
type_version: "1.0"
---

# PLC_Campaign

## Purpose

A bounded political effort with a defined end-state — a multi-cycle thread the principal is driving toward a specific outcome. Sits above Cycles (one Campaign typically spans 3-20 cycles) and below the sphere itself. Per D22, Campaign is a first-class progression scale with its own lifecycle enum.

## Cardinality and grain

- **0..N per sphere.** A sphere may have no campaigns (event-driven posture) or several (parallel initiatives).
- **Lives at**: `Spheres/<Sphere>/Campaigns/<Campaign-Slug>.md`

## Durability mode

**Mode D — Append-friendly current+history.**

- **`## Current` block** — overwrite zone for scope, member cohort, lifecycle stage, current arc summary
- **`## Membership History` block** — append-only log of actor add/remove events

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Campaign` |
| `Item_ID` | string | `campaign-<slug>` |
| `Title` | string | `"<Campaign Name> — Campaign"` |
| `Date_Added` | ISO date | Campaign start |
| `Date_Modified` | ISO date | Most recent material update |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Campaign_Name` | string | |
| `plc_Principal_Owner` | link | `[[principal-<slug>]]` — which principal is driving this campaign |
| `plc_Lifecycle_Stage` | enum | `planning \| executing \| dormant \| archived` (per D22) |
| `plc_End_State_Criteria` | string | Specific outcome that closes the campaign |
| `plc_Member_Actors` | list[link] | Actors currently in the campaign cohort |
| `plc_Active_Cycles` | list[link] | Currently-open cycles attached to this campaign |
| `plc_Started_Date` | ISO date | |
| `plc_Closed_Date` | ISO date | Empty until lifecycle reaches `archived` |
| `AI_Instructions` | string | Default `""` |

## Required body sections

```markdown
# <Campaign Name> — Campaign

## Current

### Scope
<One paragraph: what this campaign is for; what outcome closes it; what's explicitly out of scope.>

### Arc Summary
<Where the campaign is right now in its trajectory. Cycle-progress summary.>

### Member Cohort
<List of member actors with their role in this campaign.>

### Active Cycles
<Cycles currently in flight that belong to this campaign.>

### Lifecycle Stage Notes
<Why current stage; what would trigger transition. Especially material when `dormant` (why? for how long?) or `archived` (closure reason: end-state achieved | end-state unreachable | principal abandoned).>

## Membership History
<Append-only. Member add/remove events.>
- <date>: ADD: <actor> as <role>. Reason: <brief>.
- <date>: REMOVE: <actor>. Reason: <brief>.
...

## Cross-References
- Sphere: <link>
- Principal: <link>
- Active cycles: <links>
- Closed cycles in this campaign: <links>
```

## Relation slots

| Direction | Relation | Target Type | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 1 |
| Out | `plc_Principal_Owner` | PLC_Principal | 1 |
| Out | `plc_Member_Actors` | PLC_Actor | 0..N |
| Out | `plc_Active_Cycles` | PLC_Cycle | 0..N |
| In | `plc_Member_Of` (from Actor) | PLC_Actor | 0..N |
| In | `plc_Campaign` (from Cycle) | PLC_Cycle | 0..N |

## Reciprocal-update discipline

- `plc_Member_Actors` ↔ each Actor's implicit campaign membership view. When adding an Actor, record the membership in `## Membership History`.
- `plc_Active_Cycles` ↔ each Cycle's `plc_Campaign` field. When a Cycle closes, remove from `plc_Active_Cycles` (the Cycle persists as a closed/sealed reference elsewhere).
- When `plc_Lifecycle_Stage` transitions to `archived`, `plc_Closed_Date` populates AND a final entry appends to `## Membership History` noting closure.
- When a Campaign goes `dormant`, surface in next QUARTERLY-AUDIT to confirm intent.

## Lifecycle stage semantics

| Stage | Allowed transitions | Meaning |
|-------|---------------------|---------|
| `planning` | → `executing` or → `archived` | Defined but no cycles yet executed |
| `executing` | → `dormant` or → `archived` | At least one cycle active or recently closed |
| `dormant` | → `executing` or → `archived` | Paused without closure; QUARTERLY-AUDIT confirms intent |
| `archived` | (terminal) | Closed; reason captured in `### Lifecycle Stage Notes` |

## Worked example

```markdown
---
type: PLC_Campaign
timestamp: "2026-06-13T00:00:00Z"
Item_ID: campaign-succession-q3
title: "Succession-Q3 — Campaign"
Date_Added: 2026-05-01
Date_Modified: 2026-06-13
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Campaign_Name: "Succession-Q3"
plc_Principal_Owner: "[[principal-sam-ceo]]"
plc_Lifecycle_Stage: executing
plc_End_State_Criteria: "Board succession plan ratified by 2026-12-31 with Sam's operating mandate preserved (3-1 family voting bloc maintained)."
plc_Member_Actors:
  - "[[actor-carol-cfo]]"
  - "[[actor-david-coo]]"
  - "[[actor-robert-board-chair]]"
  - "[[actor-elena-independent-director]]"
plc_Active_Cycles:
  - "[[Cycle-0007]]"
  - "[[Cycle-0008]]"
plc_Started_Date: 2026-05-01
plc_Closed_Date: ""
AI_Instructions: ""
---

# Succession-Q3 — Campaign

## Current

### Scope
Preserve Sam's operating mandate through the 2026 succession-planning cycle. Specifically: (1) prevent Carol's shadow-CEO consolidation; (2) maintain 3-1 family voting bloc in Sam's favor; (3) keep independent directors confident in Sam's leadership through Q4. **Out of scope:** family-personal succession dynamics not surfacing at the board.

### Arc Summary
Two cycles completed; two cycles active. Cycle-0007 closed with Sam's Q2 mandate signal preserved. Cycle-0008 currently engaged on Robert (board chair) coalition mapping. Trajectory: holding ground; resource-shift detection needed on Carol's coalition expansion.

### Member Cohort
- **Carol Reyes (CFO)** — primary opposition; defensive posture (since 2026-06-10)
- **David (COO)** — Carol's ally; ambivalent toward Sam
- **Robert (board chair, family)** — swing; the lever for 3-1 → 3-1 maintenance
- **Elena (independent director)** — confidence-of-leadership audience; not voting on succession but sets external perception

### Active Cycles
- [[Cycle-0007]] (closed 2026-06-10) — Q2 mandate signal preservation
- [[Cycle-0008]] (active, engaged past the capability-gate (first move executed)) — Robert coalition mapping

### Lifecycle Stage Notes
`executing` since Cycle-0007 capability-gate. Will transition `archived` when board succession plan ratifies (target 2026-Q4) or when end-state becomes unreachable (Sam exit, Carol succession-bid succeeds).

## Membership History
- 2026-05-22: ADD: Robert (board chair). Reason: Recognized as swing in 3-1 family voting bloc.
- 2026-05-08: ADD: Elena (independent director). Reason: External perception audience.
- 2026-05-01: ADD: Carol (CFO), David (COO). Reason: Primary opposition cohort at campaign start.

## Cross-References
- Sphere: [[acme-corp-manifest]]
- Principal: [[principal-sam-ceo]]
- Active cycles: [[Cycle-0007]] (closed), [[Cycle-0008]]
- Closed cycles in this campaign: [[Cycle-0007]]
```

## Anti-patterns

- Letting `plc_Active_Cycles` accumulate closed cycles. When a Cycle closes, remove it from the active list; it persists in cross-references but doesn't pollute the working set.
- Leaving `plc_End_State_Criteria` vague. Without a specific closure condition, the campaign is open-ended and will never archive — defeating the lifecycle scale.
- Forgetting to flip `dormant` campaigns to `executing` when they resume. QUARTERLY-AUDIT catches this; better to catch in-session.
- Adding a member Actor without a `## Membership History` entry. The audit trail is the point.
