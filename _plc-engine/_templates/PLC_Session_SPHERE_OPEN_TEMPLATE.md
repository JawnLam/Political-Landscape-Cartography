---
type: PLC_Session
Item_ID: session-<sphere-slug>-000
title: "<Sphere Name> — Session 000 — SPHERE_OPEN"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Session_Number: 000
plc_Activity: SPHERE_OPEN
plc_Session_Started_At: "<YYYY-MM-DDTHH:MM:SS>"
plc_Session_Ended_At: "<YYYY-MM-DDTHH:MM:SS>"
plc_Operator_Mode: consultant
plc_Files_Touched: []
plc_Reciprocal_Update_Count: 0
plc_Next_Activity_Recommended: ""
plc_Next_Activity_Chosen: ""
AI_Instructions: ""
---

# <Sphere Name> — Session 000 — SPHERE_OPEN

> Bootstrap session. Protocol: `BOOTSTRAP-NEW-SPHERE.md` (pre-engagement → CQ1-CQ8 → optional CQ9-CQ10 → materialization → readiness statement).

## Activity Recap
<One paragraph: who opened the sphere, in which mode, what the engagement is for, what was materialized.>

## Files Touched
- `[[<sphere-slug>-manifest]]`: created
- `[[<sphere-slug>-state]]`: created; OPC seed + bootstrap entry
- `[[<sphere-slug>-decisions]]`: created; entry §001 "sphere opened"
- `[[principal-<slug>]]`: created
- `[[actor-<slug>]]`: stub created (× <N>)

## Decisions Made
- **Sphere-level:** <bootstrap decisions locked — scope, close criteria, guardrails, mode>

## Reciprocal Updates Applied
<count>: principal ↔ manifest; principal ↔ campaign (if any); actor stubs ↔ manifest.

## Activity-Specific Block (SPHERE_OPEN)

- **Pre-engagement:** <§§ 16-17 complete (consultant, mandatory) | lighter-touch pass (principal-self) | deferred + justification>
- **Manifest created:** <sphere name, slug, engagement kind, horizon, domain validity>
- **Principal(s) registered:** <name/placeholder + role each>; co-principal conflict discipline: <text or "n/a — single principal">
- **Initial actor cast (CQ4):** <N> stubs created — <names or [ACTOR-N] placeholders>
- **OPC seed (CQ5):** <headline reads captured into `_sphere-state.md` `## OPC Current Summary`>; full diagnostic scheduled: <when>
- **Guardrails (CQ7):** <ethical + scope boundaries the operator set at open>
- **Redaction profile chosen:** <audit-trail-full | principal-private | internal-leadership-summary | external-board-summary | peer-consultant-share> — <why>
- **First campaign / cycle scoped (CQ6):** <campaign or cycle named, or "none — first cycle to be scoped next session">
- **Engagement stage:** pre_engagement → <routine, if quality gates passed | held at pre_engagement + blocker>
- **Readiness statement:** <the one-liner read back to the operator>

## Open Threads
- <what the bootstrap deliberately deferred>

## Next Activity Recommendation
<Typically OPC_DIAGNOSE (full) if only a seed exists; ACTOR_UPDATE if a consequential actor is still a stub; ANALYZE_CYCLE if CQ6 surfaced an in-flight cycle.>

## Next Activity Chosen
<Operator's choice, including "later".>

## Cross-References
- Sphere: [[<sphere-slug>-manifest]]
- Sphere state: [[<sphere-slug>-state]]
- Decisions log: [[<sphere-slug>-decisions]]
- Principal(s) / actor stubs created: <links>
