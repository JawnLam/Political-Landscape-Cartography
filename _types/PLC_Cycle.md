---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-cycle-type
title: "PLC_Cycle — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
type_namespace: plc
type_version: "1.0"
---

# PLC_Cycle

## Purpose

The interaction-cycle protocol (14 operational constituents per PLC's walk-through) from the Lam 2018 dissertation, instantiated as a first-class Item. Each Cycle is one disciplined pass through Agenda → Decide → Act → Perceive → Track (with the dissertation's interaction-cycle constituents including alternatives audit + ethical accounting gates). The **central operational Type** — RUN-CYCLE writes here; ANALYZE-CYCLE reads from here; the audit trail flows through here.

Per D20 + D24 + D28 + D9. Embeds the two mandatory gates (ALTERNATIVES-AUDIT + ETHICAL-ACCOUNTING) per D9.

## Cardinality and grain

- **N per sphere.** Open-ended count over engagement life.
- **Lives at**: `Spheres/<Sphere>/Cycles/Cycle-<NNNN>.md` (4-digit sequence, zero-padded)

## Durability mode

**Mode D → E.** The only Type with mode transition.

- During `cycle_status: planning | active | engaged | closed` → Mode D (revisable)
- On `cycle_status: e_immutable` → Mode E (sealed; no edits)
- 7-day grace window after `closed` before AI prompts for seal

Per D28.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Cycle` |
| `Item_ID` | string | `cycle-<NNNN>` |
| `Title` | string | `"Cycle <NNNN> — <one-line agenda summary>"` |
| `Date_Added` | ISO date | Cycle-open date |
| `Date_Modified` | ISO date | Most recent material update |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Campaign` | link | `[[campaign-<slug>]]` (optional; cycle can be sphere-direct) |
| `plc_Principal_Owner` | link | `[[principal-<slug>]]` |
| `plc_Cycle_Number` | integer | Sequence within sphere |
| `plc_Cycle_Status` | enum | `planning \| active \| engaged \| closed \| e_immutable` |
| `plc_Update_Mode` | enum | `D \| E` (mirrors status; D when status ∈ {planning, active, engaged, closed}; E when `e_immutable`) |
| `plc_Started_Date` | ISO date | |
| `plc_Closed_Date` | ISO date | Empty until status `closed` |
| `plc_Sealed_Date` | ISO date | Empty until status `e_immutable` |
| `plc_Actor_Touched` | list[link] | Every Actor referenced in this cycle |
| `plc_Slash_Constituents` | list[string] | Slash addressing strings (per D18 system 1) |
| `plc_OPC_Diagnostic_Refs` | list[string] | OPC hierarchical IDs referenced (per D18 system 2) |
| `plc_Tactic_IDs_Considered` | list[string] | Catalogue Reference IDs in the considered set (per D16) |
| `plc_Tactic_IDs_Selected` | list[string] | Catalogue Reference IDs in the selected set (per D16) |
| `plc_Strategy_Number_Selected` | integer | 1-16 if a Catalogue strategy was lifted into selection |
| `plc_Clusters_Engaged` | list[string] | C01-C84 |
| `plc_Theorists_Invoked` | list[link] | `[[theorist-<name>]]` per invoked theorist |
| `plc_Alternatives_Audit_Completed_At` | ISO datetime | Empty if gate skipped |
| `plc_Ethical_Accounting_Completed_At` | ISO datetime | Empty if gate skipped |
| `plc_Accounting_Overrides` | list[string] | Each entry: `<gate>:<justification>` per D9 |
| `AI_Instructions` | string | Default `""` |

## Required body sections

The cycle body mirrors the 14-constituent dissertation protocol with the two embedded gates between capability-gate (constituent 9) and Execution (constituent 10). Body sections fill in order as the cycle progresses.

```markdown
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
<Moves actually executed. Status flips to `engaged`. Each engaged move gets a sub-block.>

### Move <N>: <Catalogue ID> — <Tactic Name>
- Engaged: <ISO datetime>
- Slash address: <string>
- Target actors: <links>
- Intended outcome: <string>

## Phase Log
<Append-only entries as track-and-detect signals come in. Perception shifts, resource shifts, classification.>
- <date>: <event>
...

## Refinement
<What OPC sections updated; what Principal funnel sharpening occurred; reciprocal updates pushed.>

## Lessons
<What worked; what didn't; what to carry into next cycle. Status flips to `closed`.>

## Cross-References
- Sphere / Campaign / Principal: <links>
- Actors touched: <links>
- Prior cycle: <link>
```

## Relation slots

| Direction | Relation | Target Type | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 1 |
| Out | `plc_Campaign` | PLC_Campaign | 0..1 |
| Out | `plc_Principal_Owner` | PLC_Principal | 1 |
| Out | `plc_Actor_Touched` | PLC_Actor | 1..N |
| Out | `plc_Tactic_IDs_Selected` | PLC_Tactic | 0..N |
| Out | `plc_Theorists_Invoked` | PLC_Theorist | 0..N |
| Out | `plc_Strategy_Number_Selected` | PLC_Strategy | 0..1 |
| In | `plc_Last_Updated_Cycle` (from Actor) | PLC_Actor | 1..N |

## Reciprocal-update discipline

- Every Actor in `plc_Actor_Touched` has its `plc_Last_Updated_Cycle` pointed here.
- Every Tactic in `plc_Tactic_IDs_Selected` has its `plc_Cited_In_Cycles` updated to include this cycle ID.
- Every Theorist in `plc_Theorists_Invoked` has its `plc_Invoked_In_Cycles` updated.
- When status transitions to `closed`, the parent Campaign's `plc_Active_Cycles` loses this cycle.
- When status transitions to `engaged`, perception/resource detection writes back to each Actor file's `## Perception History` / `## Resource History`.

## Gate discipline (Gates 1 + 2)

Per D9 + P7:

- **Both gates MUST complete** before any move from `plc_Tactic_IDs_Considered` enters `plc_Tactic_IDs_Selected`.
- **Skipping a gate is permitted** but requires explicit operator override.
- **Override format:** `<gate-name>:<one-line justification>` appended to `plc_Accounting_Overrides`.
- **Silent skipping is F8** (per `05-WRITING-FOR-AI.md`). The session-close protocol checks for completion timestamps; if absent, prompts for override justification.

## Cycle status state machine

| From | To | Trigger |
|------|-----|---------|
| (new) | `planning` | Cycle file created at RUN-CYCLE start |
| `planning` | `active` | Agenda + Landscape + OPC + Funnel body sections populated |
| `active` | `engaged` | First move engaged (Engaged Moves body section populated) |
| `engaged` | `closed` | Cycle close — lessons captured; outcome resolved (post-Obtained-Resource reflection) |
| `closed` | `e_immutable` | Operator confirms seal after grace window (default 7 days) |

`planning` and `active` are revisable freely. `engaged` is revisable but Phase Log is append-only. `closed` is revisable for grace-window-length. `e_immutable` is sealed forever.

## Worked example (abbreviated frontmatter)

```markdown
---
type: PLC_Cycle
timestamp: "2026-06-10T00:00:00Z"
Item_ID: cycle-0007
title: "Cycle 0007 — Q2 mandate signal preservation"
Date_Added: 2026-05-22
Date_Modified: 2026-06-10
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Campaign: "[[campaign-succession-q3]]"
plc_Principal_Owner: "[[principal-sam-ceo]]"
plc_Cycle_Number: 7
plc_Cycle_Status: closed
plc_Update_Mode: D
plc_Started_Date: 2026-05-22
plc_Closed_Date: 2026-06-10
plc_Sealed_Date: ""
plc_Actor_Touched:
  - "[[actor-carol-cfo]]"
  - "[[actor-robert-board-chair]]"
  - "[[actor-elena-independent-director]]"
plc_Slash_Constituents:
  - "α.Sam/Σ.Robert/2.1.4.2"
  - "δ.Carol/budget-memo-timing"
plc_OPC_Diagnostic_Refs:
  - "1.2"
  - "13.1.1"
  - "13.3.2"
plc_Tactic_IDs_Considered: ["0029", "0044", "0112", "0301"]
plc_Tactic_IDs_Selected: ["0029", "0301"]
plc_Strategy_Number_Selected: 7
plc_Clusters_Engaged: ["C12", "C44"]
plc_Theorists_Invoked:
  - "[[theorist-schelling]]"
  - "[[theorist-lukes]]"
plc_Alternatives_Audit_Completed_At: "2026-05-25T10:30:00"
plc_Ethical_Accounting_Completed_At: "2026-05-25T11:15:00"
plc_Accounting_Overrides: []
AI_Instructions: ""
---
```

(Full body would include all 14-constituent sections — abbreviated here for the type definition.)

## Anti-patterns

- **F8 — Silent gate skip.** Treating ALTERNATIVES-AUDIT or ETHICAL-ACCOUNTING as optional without override justification. The empty timestamps must be explained.
- **F9 — Reference system conflation.** Mixing slash addressing, OPC IDs, and Catalogue IDs in the same field. Keep them in their native frontmatter fields.
- **F5 — Asymmetric writeback.** Selecting a Tactic without updating the Tactic's `plc_Cited_In_Cycles`; touching an Actor without updating its `plc_Last_Updated_Cycle`. The graph corrupts silently.
- **Premature seal.** Flipping to `e_immutable` before the 7-day grace window. The operator may need to refine lessons.
- **Editing a sealed cycle.** Once Mode E, never edit. Corrections go in a follow-up Cycle's Agenda referencing the prior cycle.
- **Skipping `## Phase Log` discipline.** During `engaged`, every material signal (perception shift, resource shift, outcome confirmation) appends an entry. Without the log, ANALYZE-CYCLE has nothing to read.
