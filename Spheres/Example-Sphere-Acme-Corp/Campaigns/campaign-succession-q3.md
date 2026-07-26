---
type: PLC_Campaign
timestamp: "2026-06-13T00:00:00Z"
Item_ID: campaign-succession-q3
title: "Succession-Q3 — Campaign"
Date_Added: 2026-05-01
Date_Modified: 2026-07-15
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Campaign_Name: "Succession-Q3"
plc_Principal_Owner: "[[principal-sam-ceo]]"
plc_Lifecycle_Stage: executing
plc_End_State_Criteria: "Board succession plan ratified by 2026-12-31 with Sam's operating mandate preserved (3-1 family voting bloc maintained; independent-director confidence intact through ratification window)."
plc_Member_Actors:
  - "[[actor-carol-cfo]]"
  - "[[actor-david-coo]]"
  - "[[actor-robert-board-chair]]"
  - "[[actor-elena-independent-director]]"
plc_Active_Cycles:
  - "[[cycle-0008]]"
  # cycle-0009 added 2026-06-20, removed 2026-07-15 on close; cycle-0010 added 2026-07-02, removed 2026-07-08 on close
plc_Started_Date: 2026-05-01
plc_Closed_Date: ""
AI_Instructions: ""
---

# Succession-Q3 — Campaign

## Current

### Scope
Preserve Sam's operating mandate through the 2026 succession-planning cycle. Specifically: (1) prevent Carol's shadow-CEO consolidation from reaching the point where her framing becomes the default board read of Acme's operational state; (2) maintain the 3-1 family voting bloc in Sam's favor by holding Robert's position; (3) keep the three independent directors confident in Sam's leadership through Q4 ratification window via consistent board-summary operational signal.

**Out of scope** (per sphere boundary `_sphere-decisions.md` § 001): family-personal succession dynamics that don't manifest at the board.

### Arc Summary
**Four cycles closed within campaign (Cycles 6, 7, 9, 10).** Cycle-0007 closed 2026-06-10 with Q2 mandate signal preserved; Sam's funnel sharpness advanced 3 → 4 in the close. Cycle-0009 closed 2026-07-15 with Robert's Q3 alignment obtained — on a **revised** objective, after the original position turned out to be one Robert could not occupy; its sub-cycle Cycle-0010 closed 2026-07-08 having acquired the finance-committee procedural clearance the parent's gate demanded. **One cycle still active** (Cycle-0008, status `engaged` past the capability-gate) — Robert coalition mapping, whose lessons-extraction has now been open since 2026-06-13 and is overdue.

Trajectory: campaign objective #2 (hold Robert, keep the bloc 3-1) is materially advanced — the Q3 agenda item is minuted with Robert's support on the record. Objective #1 (Carol's consolidation) is unchanged; the Q3 procurement-authority bid predicted at opc-2026-06-01 § 14.3 is still unobserved and is the next inflection point. What the campaign learned that it did not know in June: succession-adjacent items route through Carol's committee before they reach the board calendar, which puts a structural gate on the campaign's own path that no amount of actor-reading would have surfaced.

### Member Cohort

- **[[actor-carol-cfo]] (CFO)** — **Primary opposition.** Defensive posture (since 2026-06-10, confirmed 2026-06-13). Shadow-CEO consolidation in progress.
- **[[actor-david-coo]] (COO)** — Carol's ally; ambivalent toward Sam; cost-discipline-platform framing alignment with Carol
- **[[actor-robert-board-chair]] (board chair, family — swing)** — Ambivalent; the lever for 3-1 family voting bloc maintenance. Cycle-0008's central work.
- **[[actor-elena-independent-director]] (independent director)** — Allied; confidence-of-leadership audience for the three independent directors; not voting on succession but sets external perception that filters back through the family bloc.

### Active Cycles

- [[cycle-0008]] (active, engaged past the capability-gate as of 2026-06-13) — Robert coalition mapping; Tactic 0044 executed; phase log open for Robert-signal detection. **Aging:** open 30+ days past its planned window; surfaced as a workflow-drift anomaly at the 2026-07-24 quarterly audit.

Cycle-0009 and its sub-cycle Cycle-0010 were both carried here while running and were removed on close, per the closed-cycle rule. They are listed under Cross-References.

### Lifecycle Stage Notes
**Stage `executing`** since Cycle-0007 capability-gate (2026-06-08). Will transition `archived` when:
- (a) board succession plan ratifies (target 2026-Q4) with Sam's mandate intact → close reason `end_state_achieved`
- (b) Sam exits the role → close reason `principal_exit`
- (c) Carol's succession bid reaches structural point of inevitability → close reason `end_state_unreachable` (this would also likely trigger sphere-close consultation with Sam)

Closes are operator-explicit, not automatic.

## Membership History

- 2026-05-22: ADD: [[actor-robert-board-chair]]. Reason: Recognized as swing actor in 3-1 family voting bloc following Cycle-0005 coalition-mapping work. Critical to campaign objective #2.
- 2026-05-08: ADD: [[actor-elena-independent-director]]. Reason: External perception audience for the three independent directors. Critical to campaign objective #3.
- 2026-05-01: ADD: [[actor-carol-cfo]], [[actor-david-coo]]. Reason: Primary opposition cohort at campaign open; defensive precursor signals (Carol) + coalition alignment (David) already present.

## Cross-References

- Sphere: [[acme-corp-manifest]]
- Principal: [[principal-sam-ceo]]
- Sphere state: [[acme-corp-state]]
- Active cycles: [[cycle-0008]]
- Closed cycles in this campaign, on disk: [[cycle-0007]], [[cycle-0009]], [[cycle-0010]] (sub-cycle of 0009)
- Closed earlier in this campaign, referenced but not shipped in this cartridge: [[cycle-0006]]
- Pattern manifestation: [[pattern-family-succession-pressure-loop]]
