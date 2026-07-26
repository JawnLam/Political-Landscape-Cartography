---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-session-type
title: "PLC_Session — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-07-24
Needs_Processing: false
type_namespace: plc
type_version: "1.2"
---

# PLC_Session

## Purpose

Append-only log of one AI-operator working session. Captures the activity performed, the files touched, the decisions made, and the next-activity recommendation. Per D22 + D24, a single Type carries all 16 session activities via the `plc_Activity` enum.

## Cardinality and grain

- **N per sphere.** One file per session.
- **Lives at**: `Spheres/<Sphere>/Sessions/<YYYY-MM-DD>_<NNN>_<ACTIVITY>.md`
- **Filename pattern**: date + sequential ordinal within sphere + activity enum (per Convention 5)

## Durability mode

**Mode A — Append-only.** Once the session closes (session-end protocol fires), the file is sealed for that session. Subsequent sessions create new files.

A session-in-progress file is editable; once committed at session-end, never edit.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Session` |
| `Item_ID` | string | `session-<sphere-slug>-<NNN>` |
| `Title` | string | `"<Sphere Name> — Session <NNN> — <ACTIVITY>"` |
| `Date_Added` | ISO date | Session start date |
| `Date_Modified` | ISO date | Session-end date |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Session_Number` | integer | Sequential within sphere |
| `plc_Activity` | enum | One of the 16 standalone activities (see below) |
| `plc_Session_Started_At` | ISO datetime | |
| `plc_Session_Ended_At` | ISO datetime | |
| `plc_Operator_Mode` | enum | Mirrors manifest (recorded for audit, since mode can in principle change) |
| `plc_Files_Touched` | list[link] | Every Item file edited or created |
| `plc_Reciprocal_Update_Count` | integer | Per `06-STATE-PERSISTENCE.md` discipline — number of reverse-pointer updates applied |
| `plc_Next_Activity_Recommended` | enum | What the AI proposed as next |
| `plc_Next_Activity_Chosen` | enum | What the operator chose (may differ; "later" permitted) |
| `AI_Instructions` | string | Default `""` |

### `plc_Activity` enum (per D24)

16 standalone activities:

- `SPHERE_OPEN`
- `SPHERE_CLOSE`
- `PRACTITIONER_ASSESSMENT`
- `OPC_DIAGNOSE`
- `ACTOR_UPDATE`
- `CAMPAIGN_LIFECYCLE`
- `RUN_CYCLE`
- `ANALYZE_CYCLE`
- `FORECAST_CYCLE`
- `QUARTERLY_AUDIT`
- `SCAN`
- `UNCOVER`
- `ESTIMATE`
- `MOVE_LOOKUP`
- `THEORIST_LOOKUP`
- `EXPORT_SHAREABLE`

The two embedded gates (`ALTERNATIVES-AUDIT`, `ETHICAL-ACCOUNTING`) are NOT standalone session activities — they fire inside `RUN_CYCLE`. They do not appear in this enum.

`RUN_CYCLE` walks the 14-constituent operator-facing order on the **LSPI formal spine** (lifecycle / failure / non-destructive rule families, with σ-fork and guard logging per Pillar 4 / Pillar 2) — see `03-SESSION-PROTOCOL.md` § "The LSPI formal spine", the full rule catalogue and state machine in `09-LSPI-RULES.md`, and the `PLC_Cycle` Type's LSPI sections. The AI administers the walk; it never computes it (F11).

## Required body sections

```markdown
# <Sphere Name> — Session <NNN> — <ACTIVITY>

## Activity Recap
<One paragraph: what activity ran; what triggered it; what was accomplished.>

## Files Touched
<Bulleted list of every Item file edited or created. Each bullet: file path + one-line of what changed.>

## Decisions Made
<Bulleted list of decisions made this session. Sphere-level decisions are flagged for elevation to `_sphere-decisions.md`.>

## Reciprocal Updates Applied
<Count + brief summary. Per `06-STATE-PERSISTENCE.md` — the audit count.>

## Gate Outcomes (RUN_CYCLE only)
<For RUN_CYCLE sessions only. Both gates' completion status with timestamps OR override justifications. F8 prevention.>

## Activity-Specific Block
<Section varies by activity. For OPC_DIAGNOSE: which sections diagnosed. For UNCOVER: what was uncovered. For QUARTERLY_AUDIT: 5-part protocol outcomes — perception-gap, Eight Benefits, actor-trajectory, forecast calibration (v1.2+), belief hygiene (v1.2+) — (+ 4 consultant additions if consultant mode). Etc.>

## Open Threads
<Anything raised this session that wasn't resolved. Carried to next session.>

## Next Activity Recommendation
<What the AI proposed. Justification.>

## Next Activity Chosen
<What the operator chose. If different from recommendation, brief reason captured.>

## Cross-References
- Sphere: <link>
- Prior session: <link>
- Items materially affected: <links>
```

## Relation slots

| Direction | Relation | Target Type | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 1 |
| Out | `plc_Files_Touched` | varies | 0..N |
| In (implicit) | `Source:` from `_sphere-decisions.md` entries | PLC_Sphere_Decisions | 0..N |

## Reciprocal-update discipline

- The session log is the *publication* of the session's reciprocal-update work. The count in `plc_Reciprocal_Update_Count` is the audit signal.
- When a sphere-level decision is captured in `## Decisions Made` and flagged for elevation, the corresponding `_sphere-decisions.md` entry cites this session log.

## Worked example (abbreviated)

```markdown
---
type: PLC_Session
timestamp: "2026-06-10T00:00:00Z"
Item_ID: session-acme-corp-008
title: "Acme Corp — Session 008 — RUN_CYCLE"
Date_Added: 2026-06-10
Date_Modified: 2026-06-10
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Session_Number: 8
plc_Activity: RUN_CYCLE
plc_Session_Started_At: "2026-06-10T09:00:00"
plc_Session_Ended_At: "2026-06-10T11:45:00"
plc_Operator_Mode: consultant
plc_Files_Touched:
  - "[[cycle-0008]]"
  - "[[principal-sam-ceo]]"
  - "[[actor-carol-cfo]]"
  - "[[actor-robert-board-chair]]"
  - "[[acme-corp-state]]"
  - "[[acme-corp-decisions]]"
plc_Reciprocal_Update_Count: 7
plc_Next_Activity_Recommended: ANALYZE_CYCLE
plc_Next_Activity_Chosen: later
AI_Instructions: ""
---

# Acme Corp — Session 008 — RUN_CYCLE

## Activity Recap
RUN_CYCLE on Cycle-0008: Robert (board chair) coalition mapping. Cycle progressed planning → active → engaged. Capability-gate cleared; first move executed (Tactic 0044 — coalition signal exchange). Phase log opened.

## Files Touched
- `[[cycle-0008]]`: created; populated Interest through capability-gate constituents; gates completed; status `engaged`
- `[[principal-sam-ceo]]`: `plc_Principal_Funnel_Sharpness` 4 → 4 (no change); coaching theme note added
- `[[actor-carol-cfo]]`: perception confirmed `defensive` (3/3 cold-reading); history appended
- `[[actor-robert-board-chair]]`: `plc_Actor_Completeness` 2 → 3 (network position now mapped)
- `[[acme-corp-state]]`: OPC Current Summary § 13.1.1 refreshed; state history appended
- `[[acme-corp-decisions]]`: no new sphere-level decisions

## Decisions Made
- Cycle-level: Tactic 0044 selected as first engaged move; Tactic 0029 deferred to next cycle.
- Sphere-level: none.

## Reciprocal Updates Applied
7 updates: 4 Actor `plc_Last_Updated_Cycle` pointers; 2 Tactic `plc_Cited_In_Cycles` updates; 1 Campaign `plc_Active_Cycles` add.

## Gate Outcomes
- **ALTERNATIVES-AUDIT § 15:** Completed 2026-06-10T10:15:00. 10 constructive approaches walked; 2 surfaced moves (Tactic 0044 + 0029) entered considered set.
- **ETHICAL-ACCOUNTING § 11:** Completed 2026-06-10T10:42:00. 3 × 10 harm-category grid walked. No overrides.

## Activity-Specific Block (RUN_CYCLE)
Constituents Interest through capability-gate completed in-session. Execution through Outcome (Phase Log) will populate as track-and-detect signals come in over the next ~2 weeks. Refinement + Lessons + cycle close targeted for Session 010 or 011.

## Open Threads
- Robert's perception read is still inferred — need direct signal in next 2 weeks
- Elena's confidence-of-leadership audience hasn't been tested this cycle

## Next Activity Recommendation
ANALYZE_CYCLE on Cycle-0007 (closed last session) — extract lessons before they fade. ~45 min session.

## Next Activity Chosen
later — operator deferred to next week. Will be queued.

## Cross-References
- Sphere: [[acme-corp-manifest]]
- Prior session: [[session-acme-corp-007]]
- Items materially affected: cycle-0008, principal-sam-ceo, actor-carol-cfo, actor-robert-board-chair
```

## Anti-patterns

- **Editing a closed session log.** Append-only. If a fact in the log was wrong, the correction goes in the next session's `## Activity Recap`.
- **Skipping `plc_Reciprocal_Update_Count`.** This field is the F5-prevention audit signal. If 0, it's worth questioning whether all reciprocal updates were missed or simply none were needed this session.
- **Conflating session activity with the activity-specific block content.** The activity enum lives in frontmatter; the activity-specific block carries the substance. Both required.
- **Letting `## Files Touched` drift from actual files edited.** This is the manifest the next session reads to understand what changed.
- **Omitting the gate-outcomes block for RUN_CYCLE sessions.** F8 prevention requires the gate timestamps or override justifications surface here.
- **Auto-populating `plc_Next_Activity_Chosen`.** Operator disposes (P10). Even "later" is an operator choice that must be captured explicitly.
