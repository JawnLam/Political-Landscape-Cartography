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
- **Augmented gate (v1.2+, optional):** **Verdict:** PASS | acquire `<q>` | rescope | re-probe | abandon. **Route fired:** <possession ∌ / sufficiency / inclusion / affordability / none — PASS>. **If re-probe:** VoI rationale <what decision the probe could change; why it beats acting now>; probe budget remaining: <n>.
- **ALTERNATIVES-AUDIT § 15:** Completed <ISO datetime>. <Brief: how many of 10 approaches surfaced moves into considered set.> OR **Skipped — override:** <justification>
- **ETHICAL-ACCOUNTING § 11:** Completed <ISO datetime>. <Brief: any flagged categories.> OR **Skipped — override:** <justification>

## Activity-Specific Block (RUN_CYCLE)
<Which of the 14 constituents completed this session (formal spine: the LSPI lifecycle/failure/non-destructive rule states — see 03-SESSION-PROTOCOL "The LSPI formal spine"). What remains for follow-up sessions.>

- **Cycle status transition:** <from> → <to>, <ISO datetime> — trigger: <what fired it>   # planning | active | engaged | closed | mooted | abandoned | e_immutable  (mooted, abandoned: v1.2+; abandon is admissible from any state)
- **Stance:** <adaptive | pre_committed_resource_careful | pre_committed_resource_batched> — <rationale, or "unchanged">
- **σ-forks encountered:** <count>; logged to cycle σ / Guard Log: <yes/no>
- **Guards resolved:** <possession / perception-validation readings made this session>
- **Operation Record entries appended:** <count> (append-only; projections primed; no overwrites)
- **Spawns / resumes:** <sub-cycles spawned or resumed this session, or "none">
- **Probe budget:** <remaining / not in use this cycle>

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
