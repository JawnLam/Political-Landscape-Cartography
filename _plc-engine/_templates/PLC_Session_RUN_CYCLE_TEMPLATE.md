---
type: PLC_Session
Item_ID: session-<sphere-slug>-<NNN>
title: "<Sphere Name> — Session <NNN> — RUN_CYCLE"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Session_Number: <NNN>
plc_Activity: RUN_CYCLE
plc_Session_Started_At: "<YYYY-MM-DDTHH:MM:SS>"
plc_Session_Ended_At: "<YYYY-MM-DDTHH:MM:SS>"
plc_Operator_Mode: consultant
plc_Files_Touched: []
plc_Reciprocal_Update_Count: 0
plc_Next_Activity_Recommended: ""
plc_Next_Activity_Chosen: ""
AI_Instructions: ""
---

# <Sphere Name> — Session <NNN> — RUN_CYCLE

## Activity Recap
<One paragraph: which cycle ran; what triggered it; what was accomplished. Note status transitions (planning → active → engaged).>

## Files Touched
- `[[cycle-<NNNN>]]`: <what changed>
- `[[principal-<slug>]]`: <what changed>
- `[[actor-<slug>]]`: <what changed>
- ...

## Decisions Made
- **Cycle-level:** <decisions internal to this cycle>
- **Sphere-level:** <decisions flagged for elevation to `_sphere-decisions.md`, or "none">

## Reciprocal Updates Applied
<count> updates: <brief summary of what reverse-pointers got wired>

## Gate Outcomes
- **ALTERNATIVES-AUDIT § 15:** Completed <ISO datetime>. <Brief: how many of 10 approaches surfaced moves into considered set.> OR **Skipped — override:** <justification>
- **ETHICAL-ACCOUNTING § 11:** Completed <ISO datetime>. <Brief: any flagged categories.> OR **Skipped — override:** <justification>

## Activity-Specific Block (RUN_CYCLE)
<Which of the 14 constituents completed this session. What remains for follow-up sessions.>

## Open Threads
- <items raised but not resolved this session>

## Next Activity Recommendation
<What the AI proposed. Justification.>

## Next Activity Chosen
<What the operator chose. Even "later" is a captured choice.>

## Cross-References
- Sphere: [[<sphere-slug>-manifest]]
- Prior session: <link>
- Items materially affected: <links>
