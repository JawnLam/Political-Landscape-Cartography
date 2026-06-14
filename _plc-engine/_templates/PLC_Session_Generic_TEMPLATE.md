---
Item_Prototype: PLC_Session
Item_ID: session-<sphere-slug>-<NNN>
Title: "<Sphere Name> — Session <NNN> — <ACTIVITY>"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Session_Number: <NNN>
plc_Activity: SCAN   # SPHERE_OPEN | SPHERE_CLOSE | PRACTITIONER_ASSESSMENT | ACTOR_UPDATE | CAMPAIGN_LIFECYCLE | ANALYZE_CYCLE | FORECAST_CYCLE | SCAN | UNCOVER | MOVE_LOOKUP | THEORIST_LOOKUP | EXPORT_SHAREABLE
plc_Session_Started_At: "<YYYY-MM-DDTHH:MM:SS>"
plc_Session_Ended_At: "<YYYY-MM-DDTHH:MM:SS>"
plc_Operator_Mode: consultant
plc_Files_Touched: []
plc_Reciprocal_Update_Count: 0
plc_Next_Activity_Recommended: ""
plc_Next_Activity_Chosen: ""
AI_Instructions: ""
---

# <Sphere Name> — Session <NNN> — <ACTIVITY>

> Generic session template — use this when the activity is not RUN_CYCLE, OPC_DIAGNOSE, or QUARTERLY_AUDIT (those have specialized templates). Adapt the `## Activity-Specific Block` to fit the activity's protocol per `03-SESSION-PROTOCOL.md`.

## Activity Recap
<One paragraph: what activity ran; what triggered it; what was accomplished.>

## Files Touched
- <every file edited or created>

## Decisions Made
- **Activity-level:** <decisions internal to this activity's scope>
- **Sphere-level:** <decisions flagged for elevation, or "none">

## Reciprocal Updates Applied
<count> + brief summary

## Activity-Specific Block
<Adapt to the activity. Examples:
- SPHERE_OPEN: capture full CQ1-CQ8 answers + readiness statement
- ACTOR_UPDATE: which actors were updated; perception/resource shifts
- UNCOVER: what was uncovered (including null results)
- MOVE_LOOKUP: query + tactics surfaced
- THEORIST_LOOKUP: theorist queried + invocations into active cycles
- EXPORT_SHAREABLE: redaction profile used + audiences + artifacts produced
- ANALYZE_CYCLE: cycle analyzed + key lessons extracted
- FORECAST_CYCLE: forecast horizon + scenarios + confidence
- SCAN: scope scanned + findings
- CAMPAIGN_LIFECYCLE: lifecycle transitions + reasons
- PRACTITIONER_ASSESSMENT: §§ 16-17 outcomes
- SPHERE_CLOSE: closure reason + retrospective draft status>

## Open Threads
- <items raised but not resolved this session>

## Next Activity Recommendation
<What the AI proposed. Justification.>

## Next Activity Chosen
<Operator's choice, including "later".>

## Cross-References
- Sphere: [[<sphere-slug>-manifest]]
- Prior session: <link>
- Items materially affected: <links>
