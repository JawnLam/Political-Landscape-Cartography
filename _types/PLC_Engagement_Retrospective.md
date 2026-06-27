---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-engagement-retrospective-type
title: "PLC_Engagement_Retrospective — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
type_namespace: plc
type_version: "1.0"
---

# PLC_Engagement_Retrospective

## Purpose

The one-shot synthesis artifact at engagement close — the **Layer 2 mastery endpoint** per D23. Captures what was learned across the engagement (not within a single cycle): pattern recognition, UNCOVER-payoff log, what the operator now knows that they didn't at sphere-open, lessons that should propagate forward to other engagements (in consultant mode) or to the operator's ongoing practice (in principal-self mode).

Per D29 (added as the 16th Type during Q12). Distinct from per-cycle lessons (which live in `PLC_Cycle § Lessons`) — this is the cross-cycle retrospective.

## Cardinality and grain

- **One per sphere — created at SPHERE-CLOSE.**
- **Lives at**: `Spheres/<Sphere>/Engagement-Retrospective.md` (sphere root)

## Durability mode

**Mode E — Immutable.** Created once at SPHERE-CLOSE. Never edited after publication. The retrospective is the engagement's published record; mutability would defeat its archival purpose.

If the retrospective needs revision post-publication (e.g., factual correction surfaces months later), append a `## Post-Publication Note` block — **this is the one allowed exception to immutability**, and it must be dated, justified, and never overwrite prior content.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Engagement_Retrospective` |
| `Item_ID` | string | `retrospective-<sphere-slug>` |
| `Title` | string | `"<Sphere Name> — Engagement Retrospective"` |
| `Date_Added` | ISO date | SPHERE-CLOSE session date |
| `Date_Modified` | ISO date | Same as Date_Added (immutable; rare post-publication note touches) |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Engagement_Opened` | ISO date | Mirrors manifest |
| `plc_Engagement_Closed` | ISO date | SPHERE-CLOSE date |
| `plc_Engagement_Duration_Days` | integer | Closed - Opened |
| `plc_Cycles_Run_Count` | integer | Total Cycles in sphere |
| `plc_Campaigns_Run_Count` | integer | Total Campaigns in sphere |
| `plc_Opc_Diagnostics_Performed` | integer | Total full OPC diagnostics |
| `plc_Operator_Mode` | enum | `consultant \| principal_self` (mirrors manifest) |
| `plc_Close_Reason` | enum | `end_state_achieved \| end_state_unreachable \| principal_exit \| engagement_pause \| other` |
| `plc_Performed_In_Session` | link | `[[session-...]]` — SPHERE-CLOSE session |
| `AI_Instructions` | string | Default `""` |

## Required body sections

```markdown
# <Sphere Name> — Engagement Retrospective

## Engagement at a glance
<One paragraph: opened when, closed when, why closed, headline outcome.>

## What the Principal Now Knows That They Didn't at Open
<3-7 bullets. The funnel sharpening — what was vague at sphere-open and is now operational in the principal's working frame.>

## What the Operator Now Knows That They Didn't at Open
<3-7 bullets. Mode-aware:
- Consultant mode: lessons for the practitioner that propagate to other engagements
- Principal-self mode: lessons for the operator's ongoing political practice>

## UNCOVER-payoff Log
<Per D23 Layer 2 endpoint. List of UNCOVER sessions and what each surfaced. Include both successful uncovers AND failed/null uncovers (the null is data).>
- <date>: UNCOVER on <topic>. Surfaced: <finding>. Confirmed by: <evidence>.
- <date>: UNCOVER on <topic>. Surfaced: nothing material. (Null result — useful exclusion.)
...

## Pattern Recognition
<Multi-cycle patterns the engagement surfaced. Pattern Items created or refined during the engagement get cited here. Connect to theorist invocations if relevant.>

## OPC Trajectory
<How the sphere's OPC scores shifted from baseline to close. Section-by-section narrative for material shifts only.>

## Engaged-Move Audit Summary
<Per D16 — searchability across cycles. Aggregate the audit trail: total tactics considered, selected, engaged; strategies used; theorists invoked; gate overrides (per D9).>
- Tactics considered: <count>
- Tactics selected: <count>
- Tactics engaged: <count>
- Strategies invoked: <count + which>
- Theorists invoked: <list>
- ALTERNATIVES-AUDIT gates completed: <count> / <total cycles>
- ETHICAL-ACCOUNTING gates completed: <count> / <total cycles>
- Gate overrides: <list with justifications>

## What Didn't Work
<Honest enumeration of moves that backfired, perception reads that were wrong, predictions that missed. The retrospective's value depends on this being substantive, not defensive.>

## Carry-Forward Recommendations
<What the principal should carry into the next phase of their political work. For consultant mode: also what the consultant should carry into similar engagements.>

## Practitioner Reflection (consultant mode only)
<§§ 16-17 retrospective: what worked about the practitioner-engagement fit; what should change for future similar engagements.>

## Cross-References
- Sphere: <link>
- Final OPC diagnostic: <link>
- SPHERE-CLOSE session: <link>
- All cycles in this engagement: <listed by cycle ID>
- All campaigns in this engagement: <listed by campaign ID>

## Post-Publication Notes
<Empty at publication. Only appended if factual correction surfaces later. Each entry dated and justified. Never overwrite prior content.>
```

## Relation slots

| Direction | Relation | Target Type | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 1 |
| Out | `plc_Performed_In_Session` | PLC_Session | 1 |
| Out (implicit, in body) | references to every Cycle, Campaign, OPC_Diagnostic, Pattern in the sphere | various | N |

## Reciprocal-update discipline

- At publication, the manifest's `plc_Engagement_Status` flips to `closed` AND `_sphere-state.md` final entry references this retrospective.
- The Pattern Items refined during the engagement are not auto-updated by retrospective publication — they were updated in the sessions that surfaced them. The retrospective merely cites.
- Post-publication notes do not trigger reciprocal updates; they are sealed-document corrections, not graph mutations.

## Worked example (abbreviated)

```markdown
---
type: PLC_Engagement_Retrospective
timestamp: "2026-12-18T00:00:00Z"
Item_ID: retrospective-acme-corp
title: "Acme Corp — Engagement Retrospective"
Date_Added: 2026-12-18
Date_Modified: 2026-12-18
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Engagement_Opened: 2026-04-15
plc_Engagement_Closed: 2026-12-18
plc_Engagement_Duration_Days: 247
plc_Cycles_Run_Count: 14
plc_Campaigns_Run_Count: 1
plc_Opc_Diagnostics_Performed: 4
plc_Operator_Mode: consultant
plc_Close_Reason: end_state_achieved
plc_Performed_In_Session: "[[session-acme-corp-024]]"
AI_Instructions: ""
---

# Acme Corp — Engagement Retrospective

## Engagement at a glance
Opened 2026-04-15. Closed 2026-12-18 with end-state achieved: board succession plan ratified with Sam's operating mandate preserved (3-1 family voting bloc held). 247 days, 14 cycles, 1 campaign, 4 full OPC diagnostics.

## What the Principal Now Knows That They Didn't at Open
- Robert's swing read on relationship-tenure cues, not policy substance — the lever was social, not strategic
- Carol's defensive posture won't shift through perception-rebuilding alone; requires asymmetric data exposure (Tactic 0301 worked; Tactic 0029 didn't)
- Independent-director audience operates on quarterly cadence, not real-time signal
- ...

## What the Operator Now Knows That They Didn't at Open
- Family-board succession engagements benefit from explicit `plc_Coprincipal_Conflict_Discipline` even when only one principal is named (family directors function as adjacent principals)
- Cycle 5 over-relied on Cluster C44; should have surfaced Cluster C12 earlier
- §§ 16-17 quarterly refresh caught a §16.7 schedule-flexibility flag at Q3 that would have damaged the Q4 push

## UNCOVER-payoff Log
- 2026-07-15: UNCOVER on coalition-network. Surfaced: David-Carol coalition was older than apparent; preceded Sam's tenure. Confirmed by: Carol's resource history.
- 2026-09-22: UNCOVER on bridge-discovery (Robert ↔ Elena). Null result — no material bridge. (Useful exclusion: ruled out an entire move family.)
- 2026-11-08: UNCOVER on information-flow asymmetry. Surfaced: audit-committee channel gave Carol 48hr lead on financial signal. Confirmed by: Cycle-0012 timing analysis.

(... more UNCOVER entries ...)

## Pattern Recognition
- Family-succession-pressure-loop pattern (operator-extended) — refined across Cycles 6, 9, 12; documented in [[Pattern-Family-Succession-Pressure-Loop]]
- Lukes' three-dimensional power pattern — manifested in Carol's agenda-shaping authority through finance committee staffing; documented in [[Pattern-Three-Dimensional-Power-Agenda]]

## OPC Trajectory
§1 Power Structure: stable throughout. §2 Stakeholders: cast grew 8 → 14 actors. §13.1.1 change-initiator-posture stabilized at "earned-mandate" by Cycle 6 (was wobbling 1-5). §14 trajectory shifted from "moderate-uncertain" baseline to "high-confidence preservation" by Cycle 10.

## Engaged-Move Audit Summary
- Tactics considered: 47
- Tactics selected: 22
- Tactics engaged: 19
- Strategies invoked: 3 (#7 — coalition-preservation; #11 — asymmetric-data-exposure; #4 — pure-obstruction-counter)
- Theorists invoked: Schelling (8 cycles), Lukes (6), Cialdini (3), Pfeffer (2), Crozier (1)
- ALTERNATIVES-AUDIT gates: 13/14 completed (1 override — Cycle-0011 emergency signal preservation; justification logged)
- ETHICAL-ACCOUNTING gates: 14/14 completed
- Gate overrides: ALTERNATIVES-AUDIT Cycle-0011: "Time-critical signal; full §15 walk would have missed the window. Operator accepted truncated audit with §15.3 + §15.7 only."

## What Didn't Work
- Cycle-0005's bid to flip Carol via coalition signal exchange. Misread her resource-trajectory; she was past the point where coalition signal would shift her posture.
- 2026-07 UNCOVER attempt on Robert's family-relationship motivations. Pushed too hard into family-personal scope — operator pulled back per scope boundary. Useful boundary-test, but lost a session.

## Carry-Forward Recommendations
- Sam: maintain quarterly check-ins with Robert through 2027 board cycle even though primary engagement closed
- Operator (consultant): for future family-board succession engagements, default to mapping family-voting-bloc swing actor as primary lever — confirmed pattern across this engagement
- Operator (consultant): build "family-succession-pressure-loop" pattern into engagement intake CQs

## Practitioner Reflection
- §16 fit: green throughout except Q3 schedule-flexibility flag (mitigated)
- §17 engagement politics: stable; no surprises. Family-board structure made advisor-engagement boundaries cleaner than typical mid-market.

## Cross-References
- Sphere: [[acme-corp-manifest]]
- Final OPC: [[opc-2026-12-01]]
- SPHERE-CLOSE session: [[session-acme-corp-024]]
- All cycles: Cycle-0001 through Cycle-0014
- Campaigns: [[campaign-succession-q3]]

## Post-Publication Notes
(none)
```

## Anti-patterns

- Editing the body after publication. Sealed at SPHERE-CLOSE. Use `## Post-Publication Notes` for factual corrections only.
- Omitting `## What Didn't Work`. The retrospective's value depends on it. Defensive retrospectives propagate bad patterns forward.
- Cherry-picking the UNCOVER-payoff log to surface only successes. Null results matter for D23 Layer 2 mastery — they're the structural exclusions.
- Skipping `## Practitioner Reflection` in consultant mode. Per D11/D24, the §§ 16-17 retrospective is part of the consultant-mode end-of-engagement protocol.
- Publishing before the SPHERE-CLOSE session's gate checks pass (final OPC diagnostic complete, all open cycles closed or rescoped, no pending sphere-decision elevations).
