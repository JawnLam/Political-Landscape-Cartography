---
type: PLC_Cycle
Item_ID: cycle-<NNNN>
title: "Cycle <NNNN> — <one-line agenda summary>"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Campaign: ""   # "[[campaign-<slug>]]" or empty for sphere-direct cycle
plc_Principal_Owner: "[[principal-<slug>]]"
plc_Cycle_Number: <integer>
plc_Cycle_Status: planning   # planning | active | engaged | closed | e_immutable
plc_Update_Mode: D   # D | E — flips to E only when status: e_immutable
plc_Started_Date: <YYYY-MM-DD>
plc_Closed_Date: ""
plc_Sealed_Date: ""
plc_Actor_Touched: []
plc_Slash_Constituents: []   # System 1: slash addressing
plc_OPC_Diagnostic_Refs: []   # System 2: OPC hierarchical IDs (e.g., "13.1.1")
plc_Tactic_IDs_Considered: []   # System 3: Catalogue IDs (e.g., "0029")
plc_Tactic_IDs_Selected: []
plc_Strategy_Number_Selected: 0   # 1-16 or 0 if none
plc_Clusters_Engaged: []   # e.g., ["C12", "C44"]
plc_Theorists_Invoked: []
plc_Alternatives_Audit_Completed_At: ""   # ISO datetime or empty if skipped (then log override)
plc_Ethical_Accounting_Completed_At: ""   # ISO datetime or empty if skipped
plc_Accounting_Overrides: []   # ["<gate>:<justification>"]
AI_Instructions: ""
---

# Cycle <NNNN> — <one-line agenda summary>

## Agenda
<The principal's articulated agenda for this cycle. ADAPT "A" beat. One paragraph.>

## Landscape Assessment
<Current sphere read going into the cycle. Citations to OPC IDs and Actor files.>

## OPC Self-Diagnosis
<Where the principal stands across the OPC sections most material to this agenda.>

## Principal Funnel
<The funnel narrowed for this specific cycle. Decision criteria.>

## ALTERNATIVES-AUDIT § 15 Pass (Gate 1)
<Walk through OPC § 15's 10 constructive approaches. For each: relevant? considered? proposed move?>

**Completed:** <ISO datetime>  OR  **Skipped — override justification:** <text>

## ETHICAL-ACCOUNTING § 11 Pass (Gate 2)
<Walk through OPC § 11: 3 harm scopes × 10 categories + 5 ethical frameworks weighting.>

**Completed:** <ISO datetime>  OR  **Skipped — override justification:** <text>

## Considered Moves
<Full considered-moves set with Catalogue IDs, theorist invocations, slash addressing.>

## Selected Moves
<Narrowed set after gates. Why these; why not the others.>

## Engaged Moves
<Status flips to `engaged` when first move executes.>

### Move 1: <Catalogue ID> — <Tactic Name>
- Engaged: <ISO datetime>
- Slash address: <string>
- Target actors: <links>
- Intended outcome: <string>

## Phase Log
<Append-only entries as track-and-detect signals come in.>

- <date>: <event>

## Refinement
<What OPC sections updated; what Principal funnel sharpening occurred; reciprocal updates pushed.>

## Lessons
<What worked; what didn't; what to carry into next cycle. Status flips to `closed`.>

## Cross-References
- Sphere: <link>
- Campaign: <link>
- Principal: <link>
- Actors touched: <links>
- Prior cycle: <link>
