---
type: PLC_Session
Item_ID: session-<sphere-slug>-<NNN>
title: "<Sphere Name> — Session <NNN> — SPHERE_CLOSE"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Session_Number: <NNN>
plc_Activity: SPHERE_CLOSE
plc_Session_Started_At: "<YYYY-MM-DDTHH:MM:SS>"
plc_Session_Ended_At: "<YYYY-MM-DDTHH:MM:SS>"
plc_Operator_Mode: consultant
plc_Files_Touched: []
plc_Reciprocal_Update_Count: 0
plc_Next_Activity_Recommended: ""
plc_Next_Activity_Chosen: ""
AI_Instructions: ""
---

# <Sphere Name> — Session <NNN> — SPHERE_CLOSE

> Closure session. Produces the engagement retrospective (D23 Layer 2) + the Layer 3 structured export, then seals.

## Activity Recap
<One paragraph: why the sphere is closing, against which close criteria, headline outcome.>

## Files Touched
- `[[retrospective-<sphere-slug>]]`: created (Mode E at publication)
- `[[<sphere-slug>-manifest]]`: `plc_Engagement_Status` → closed
- `[[<sphere-slug>-state]]`: final snapshot; State History entry appended
- `[[cycle-<NNNN>]]`: sealed (× <N>)

## Decisions Made
- **Sphere-level:** <close decision + criteria met; any carry-forward positions logged to `_sphere-decisions.md`>

## Reciprocal Updates Applied
<count>: final pass — cycles ↔ actors, tactics ↔ cycles, campaigns ↔ principal. Unrepaired F5 violations at close: <N>.

## Activity-Specific Block (SPHERE_CLOSE)

- **Close reason:** <end_state_achieved | end_state_unreachable | principal_exit | engagement_pause | other> — <against which `plc_Sphere_Close_Criteria`>
- **Final state snapshot:** cycles run <N> (closed <N> / mooted <N> / abandoned <N>); campaigns <N>; actors tracked <N>; OPC diagnostics <N>; last diagnostic <link>
- **Engagement retrospective:** [[retrospective-<sphere-slug>]] — <status: drafted / published>
- **Open detection records resolved (v1.2+, optional):** <each Detection Record set to stopped_acting / stopped_budget / archived, with reason>
- **Seal / immutability transition:** <N> cycles flipped `closed` → `e_immutable` (grace window observed); remaining unsealed: <N> + why. Retrospective sealed: <date>
- **Export profile used:** <audit-trail-full | principal-private | internal-leadership-summary | external-board-summary | peer-consultant-share> → `Exports/<YYYY-MM-DD>_<audience>_<slug>.md`
- **Handoff documentation (consultant mode, OPC § 17.7):** <what was handed to whom; what was withheld and why>
- **Engagement stage:** <prior> → closed

## Open Threads
- <anything intentionally left open at close — e.g., a paused engagement's resume conditions>

## Next Activity Recommendation
<Typically none — sphere is closed. If `engagement_pause`, note the resume trigger.>

## Next Activity Chosen
<Operator's choice, including "later".>

## Cross-References
- Sphere: [[<sphere-slug>-manifest]]
- Retrospective: [[retrospective-<sphere-slug>]]
- Final OPC diagnostic: <link>
- Prior session: <link>
