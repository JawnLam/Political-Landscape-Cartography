---
type: PLC_Sphere_State
Item_ID: <sphere-slug>-state
title: "<Sphere Name> — Sphere State"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Latest_OPC_Diagnostic: ""   # "[[opc-<YYYY-MM-DD>]]"
plc_Latest_OPC_Diagnostic_Date: ""
plc_Engagement_Status: pre_engagement
plc_Active_Cycles_Count: 0
plc_Active_Campaigns_Count: 0
plc_Actor_Count: 0
AI_Instructions: ""
---

# <Sphere Name> — Sphere State

## Decided
<Current sphere-level positions. Overwrite zone. Each bullet briefly cites the decision source (`_sphere-decisions.md` § OR session log).>

- <position> (_sphere-decisions.md §<NNN>)

## OPC Current Summary
<Rollup of `plc_Latest_OPC_Diagnostic`. Only surface sections with material signal. Diagnostic file is canonical; this is the quick-reference.>

### Power Structure (§1)
<one paragraph or omit if not material>

### Stakeholders & Actors (§2)
<one paragraph or omit>

### Dynamics (§13)
<one paragraph or omit>

### Trajectory (§14)
<one paragraph or omit>

## State History
<Append-only. Date prefix. One line per material shift. Never edit prior entries.>

- <YYYY-MM-DD>: Sphere opened. (Session <date>_000_SPHERE-OPEN.md)

## Cross-References
- Manifest: [[<sphere-slug>-manifest]]
- Decisions log: [[<sphere-slug>-decisions]]
- Latest OPC: <link or empty>
- Active cycles: <links>
- Active campaigns: <links>
