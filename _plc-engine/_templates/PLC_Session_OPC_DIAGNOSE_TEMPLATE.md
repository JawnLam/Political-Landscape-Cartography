---
type: PLC_Session
Item_ID: session-<sphere-slug>-<NNN>
title: "<Sphere Name> — Session <NNN> — OPC_DIAGNOSE"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Session_Number: <NNN>
plc_Activity: OPC_DIAGNOSE
plc_Session_Started_At: "<YYYY-MM-DDTHH:MM:SS>"
plc_Session_Ended_At: "<YYYY-MM-DDTHH:MM:SS>"
plc_Operator_Mode: consultant
plc_Files_Touched: []
plc_Reciprocal_Update_Count: 0
plc_Next_Activity_Recommended: ""
plc_Next_Activity_Chosen: ""
AI_Instructions: ""
---

# <Sphere Name> — Session <NNN> — OPC_DIAGNOSE

## Activity Recap
<One paragraph: which diagnostic ran; full / partial / seed scope; what triggered it.>

## Files Touched
- `[[opc-<YYYY-MM-DD>]]`: created; <sections covered>
- `[[<sphere-slug>-state]]`: OPC Current Summary refreshed
- (prior active diagnostic if applicable): flipped to archived

## Decisions Made
- **Sphere-level:** <any sphere-level decisions flagged for elevation>

## Reciprocal Updates Applied
<count>: prior diagnostic state flip; sphere-state rollup regeneration; any actor/principal updates triggered by diagnostic findings.

## Activity-Specific Block (OPC_DIAGNOSE)
- **Scope:** full | partial | seed
- **Sections covered:** <list>
- **Headline reads:** <3-5 bullets>
- **§16 outcome (consultant mode):** <green | flagged item + mitigation>
- **§17 outcome (consultant mode):** <green | flagged item>
- **Supersedes:** <prior diagnostic link or empty>

## Open Threads
- <items raised by the diagnostic that need follow-up activities>

## Next Activity Recommendation
<Typically RUN_CYCLE or ACTOR_UPDATE based on diagnostic findings.>

## Next Activity Chosen
<operator's choice>

## Cross-References
- Sphere: [[<sphere-slug>-manifest]]
- Diagnostic created: [[opc-<YYYY-MM-DD>]]
- Prior session: <link>
