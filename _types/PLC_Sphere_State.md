---
type: Prototype
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-sphere-state-prototype
title: "PLC_Sphere_State — Prototype Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
prototype_namespace: plc
prototype_version: "1.0"
---

# PLC_Sphere_State

## Purpose

The operator's quick-reference layer over current sphere state. Single source of truth for "where does this sphere stand right now" — composed of decided positions and a rollup of the latest OPC diagnostic. Updated end-of-session by the AI when material state shifts.

## Cardinality and grain

- **One per sphere.**
- **Lives at sphere root**: `Spheres/<Sphere>/_sphere-state.md`

## Durability mode

**Mode D — Append-friendly current+history.** `## Decided` and `## OPC Current Summary` are overwrite zones; `## State History` is append-only.

Per D27 + D28.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Sphere_State` |
| `Item_ID` | string | `<sphere-slug>-state` |
| `Title` | string | `"<Sphere Name> — Sphere State"` |
| `Date_Added` | ISO date | Sphere-open date |
| `Date_Modified` | ISO date | Most recent material update |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Latest_OPC_Diagnostic` | link | `[[<diagnostic-id>]]` — the canonical full diagnostic this summary rolls up |
| `plc_Latest_OPC_Diagnostic_Date` | ISO date | When the canonical was performed |
| `plc_Engagement_Status` | enum | Mirrors manifest's `plc_Engagement_Status` |
| `plc_Active_Cycles_Count` | integer | Rollup; currently-open cycles |
| `plc_Active_Campaigns_Count` | integer | Rollup |
| `plc_Actor_Count` | integer | Rollup |
| `AI_Instructions` | string | Default `""` |

## Required body sections

```markdown
# <Sphere Name> — Sphere State

## Decided
<Current sphere-level positions. Overwrites in place as decisions evolve. Each bullet briefly cites the decision source (`_sphere-decisions.md` entry or session log).>

## OPC Current Summary
<Rollup of `plc_Latest_OPC_Diagnostic`. Maximum one paragraph per OPC section (17 sections total — be selective; not all sections are surfaced unless material).>

### Power Structure (§1)
### Stakeholders & Actors (§2)
### ... (other sections as material)

## State History
<Append-only log of material sphere-level state shifts. Each entry is dated and one-line. Never edit existing entries.>
- 2026-06-10: Engagement status shifted `pre_engagement` → `routine`. (Session 2026-06-10_003_SPHERE-OPEN.md)
- 2026-04-22: Sphere opened. (Session 2026-04-22_000_SPHERE-OPEN.md)

## Cross-References
<Pointers to manifest, decisions log, latest OPC diagnostic, active cycles, active campaigns.>
```

## Relation slots

| Direction | Relation | Target Prototype | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 1 |
| Out | `plc_Latest_OPC_Diagnostic` | PLC_OPC_Diagnostic | 1 |

## Reciprocal-update discipline

- The `## OPC Current Summary` is a rollup, not a canonical. If the rollup contradicts the linked `plc_Latest_OPC_Diagnostic`, the diagnostic file wins; regenerate the rollup.
- When a session log records a sphere-level decision, the corresponding bullet in `## Decided` is updated AND `_sphere-decisions.md` is appended (per the elevation discipline in `06-STATE-PERSISTENCE.md`).
- Engagement-status shifts here must match the manifest. If they diverge, the manifest is authoritative.

## Section discipline

- **`## Decided`** — overwrite zone. Edit in place. Don't accumulate stale bullets — when a position is superseded, remove it (the superseding decision is captured in `_sphere-decisions.md` immutably).
- **`## OPC Current Summary`** — overwrite zone. Refresh after every OPC-DIAGNOSE session or material session that materially shifts the read.
- **`## State History`** — append-only. Each entry one line. Date prefix. Cite session log.

## Worked example

```markdown
---
type: PLC_Sphere_State
timestamp: "2026-06-13T00:00:00Z"
Item_ID: acme-corp-state
title: "Acme Corp — Sphere State"
Date_Added: 2026-04-15
Date_Modified: 2026-06-13
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Latest_OPC_Diagnostic: "[[OPC-2026-06-01]]"
plc_Latest_OPC_Diagnostic_Date: 2026-06-01
plc_Engagement_Status: routine
plc_Active_Cycles_Count: 2
plc_Active_Campaigns_Count: 1
plc_Actor_Count: 12
AI_Instructions: ""
---

# Acme Corp — Sphere State

## Decided
- Sam's primary agenda through 2026-Q3: preserve operating mandate through succession-planning cycle. (_sphere-decisions.md §1)
- Carol (CFO) treated as `defensive` until perception shift detected; do not assume neutralizable in this engagement window. (_sphere-decisions.md §3)
- Family-personal dynamics beyond what shows up at the board are out of scope. (manifest charter; _sphere-decisions.md §1)

## OPC Current Summary
Rollup of [[OPC-2026-06-01]]. See diagnostic for full scoring detail.

### Power Structure (§1)
Family-board with professional CEO (Sam). 4 family directors + 3 independents. Family voting bloc presently 3-1 in Sam's favor; one swing.

### Stakeholders & Actors (§2)
12 actors mapped. Principal: Sam. Defensive: Carol (CFO), Robert (board chair, family). Allied: COO, head of sales. Ambivalent: 2 family directors. Unaware: 3 mid-level.

### Dynamics (§13)
Arc-dynamic: succession-pressure-loop. Opposition-posture: Carol's "shadow-CEO consolidation." Change-initiator-posture: Sam's "earned-mandate."

### Trajectory (§14)
Carol's resource consolidation if unchecked → succession destabilization Q4. 6-month horizon.

## State History
- 2026-06-10: Engagement status shifted `pre_engagement` → `routine` after first full cycle closure. (Session 2026-06-10_003_RUN-CYCLE.md)
- 2026-06-01: OPC diagnostic v2 performed; family voting bloc shifted. (Session 2026-06-01_OPC-DIAGNOSE.md)
- 2026-04-22: Sphere opened. (Session 2026-04-22_000_SPHERE-OPEN.md)

## Cross-References
- Manifest: [[acme-corp-manifest]]
- Decisions log: [[acme-corp-decisions]]
- Latest OPC: [[OPC-2026-06-01]]
- Active cycles: [[Cycle-0007]], [[Cycle-0008]]
- Active campaigns: [[Campaign-Succession-Q3]]
```

## Anti-patterns

- Letting `## Decided` bullets accumulate stale entries from superseded decisions. The append-only audit lives in `_sphere-decisions.md`; `## Decided` is the *current* view.
- Editing `## State History` entries. Append-only. Corrections are new append entries.
- Mixing OPC sections that aren't material into the rollup. The rollup is a quick-reference; if a section has no material signal, omit it.
- Forgetting to elevate sphere-level decisions to `_sphere-decisions.md`. The state file and decisions log update together at session-end.
