---
type: PLC_Campaign
Item_ID: campaign-<slug>
title: "<Campaign Name> — Campaign"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Campaign_Name: "<Campaign Name>"
plc_Principal_Owner: "[[principal-<slug>]]"
plc_Lifecycle_Stage: planning   # planning | executing | dormant | archived
plc_End_State_Criteria: "<Specific outcome that closes the campaign. Required — vague closures defeat the lifecycle scale.>"
plc_Member_Actors: []
plc_Active_Cycles: []
plc_Started_Date: <YYYY-MM-DD>
plc_Closed_Date: ""
AI_Instructions: ""
---

# <Campaign Name> — Campaign

## Current

### Scope
<One paragraph: what this campaign is for; what outcome closes it; what's explicitly out of scope.>

### Arc Summary
<Where the campaign is right now. Cycle-progress summary.>

### Member Cohort
- **<Actor Name> (<Role>)** — <role in this campaign>

### Active Cycles
- <links to currently-open cycles in this campaign>

### Lifecycle Stage Notes
<Why current stage; what would trigger transition.>

## Membership History
<Append-only. Date prefix. ADD or REMOVE.>

- <YYYY-MM-DD>: ADD: <actor> as <role>. Reason: Campaign opened.

## Cross-References
- Sphere: [[<sphere-slug>-manifest]]
- Principal: [[principal-<slug>]]
- Active cycles: <links>
- Closed cycles in this campaign: <links>
