---
type: PLC_Campaign
timestamp: "2026-06-13T00:00:00Z"
Item_ID: campaign-succession-q3
title: "Succession-Q3 — Campaign"
Date_Added: 2026-05-01
Date_Modified: 2026-06-13
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
**Two cycles closed within campaign (Cycles 6 + 7).** Cycle-0007 closed 2026-06-10 with Q2 mandate signal preserved; Sam's funnel sharpness advanced 3 → 4 in the close. **One cycle active** (Cycle-0008, status `engaged` past the capability-gate) — Robert coalition mapping. Trajectory: holding ground on family-bloc preservation; resource-shift detection on Carol's coalition expansion is the active monitoring focus. Next predicted cycle initiation: late June 2026 on Elena confidence-signal maintenance.

### Member Cohort

- **[[actor-carol-cfo]] (CFO)** — **Primary opposition.** Defensive posture (since 2026-06-10, confirmed 2026-06-13). Shadow-CEO consolidation in progress.
- **[[actor-david-coo]] (COO)** — Carol's ally; ambivalent toward Sam; cost-discipline-platform framing alignment with Carol
- **[[actor-robert-board-chair]] (board chair, family — swing)** — Ambivalent; the lever for 3-1 family voting bloc maintenance. Cycle-0008's central work.
- **[[actor-elena-independent-director]] (independent director)** — Allied; confidence-of-leadership audience for the three independent directors; not voting on succession but sets external perception that filters back through the family bloc.

### Active Cycles

- [[cycle-0008]] (active, engaged past the capability-gate as of 2026-06-13) — Robert coalition mapping; Tactic 0044 executed; phase log open for Robert-signal detection

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
- Closed cycles in this campaign: [[cycle-0006]], [[cycle-0007]]
- Pattern manifestation: [[pattern-family-succession-pressure-loop]]
