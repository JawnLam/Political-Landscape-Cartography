---
type: PLC_Principal
Item_ID: principal-<slug>
title: "<Principal Name> — Principal"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Principal_Name: "<Name or [PRINCIPAL] placeholder>"
plc_Principal_Role: "<Position/title>"
plc_Authority_Scope_Unilateral: "<What can be decided alone>"
plc_Authority_Scope_Coalition: "<What requires alliance>"
plc_Authority_Scope_Forbidden: "<What cannot be touched>"
plc_Current_Agenda: "<One-paragraph current Agenda summary>"
plc_Principal_Funnel_Sharpness: 0   # 0=Unstated 1=Vague 2=Drafted 3=Operational 4=Sharp 5=Deeply held
plc_Funnel_Last_Refined_Date: ""
plc_Engagement_Status: active   # active | coaching_paused | closed_out
plc_Active_Campaigns: []
AI_Instructions: ""
---

# <Principal Name> — Principal

## Current

### Funnel
**Agenda:** <one sentence>

**Decision criteria** (sharpness <level>):
1. <criterion>
2. <criterion>
...

### Authority Scope
- Unilateral: <summary>
- Coalition: <summary>
- Forbidden: <summary>

### Active Coaching Themes
<What the operator is currently working with the principal on.>

### Mastery Signals
<Evidence of the current sharpness level. What earned this score; what would justify moving up.>

## Engagement History
<Append-only. Material role / scope / status shifts. Dated.>

- <YYYY-MM-DD>: Engagement opened; principal added.

## Mastery History
<Append-only. Funnel-sharpness changes with reason. Dated.>

- <YYYY-MM-DD>: Sharpness 0 (baseline at engagement start).

## Cross-References
- Sphere: [[<sphere-slug>-manifest]]
- Active campaigns: <links>
- Most recent cycle: <link>
