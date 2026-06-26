---
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-engine-06-state-persistence
title: "PLC Engine — 06 State Persistence"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
doc_type: engine
role: state-persistence-contract
scope: subject-agnostic-within-PLC
updated: 2026-06-13
---

# 06 — STATE PERSISTENCE

> **PLC has no database. The filesystem is the database. The rules in this file are the schema constraints. If state goes wrong, it's because one of these rules was violated.**

## The five durability modes

Every file in a PLC sphere falls into one of five durability modes. The mode determines what edits are allowed and what edits would corrupt the audit trail.

| Mode | Name | Rule | Where used |
|------|------|------|------------|
| **A** | Append-only | New lines added; existing lines never edited, reordered, or deleted | Decision logs, session logs, retrospective archives |
| **C** | Current overwrite | Whole file replaced as state changes; no history kept in-file | Current state files where history is captured elsewhere |
| **D** | Append-friendly current+history | Single file with a `## Current` section (overwriteable) and a `## ... History` section (append-only) | Sphere state, Principal funnels, Actor profiles, OPC diagnostic ledgers |
| **E** | Immutable | Created once; never edited after creation | Closed cycle logs, archived OPC diagnostics, session retrospectives once shipped |
| **D → E** | Append-friendly that locks on event | Lives as Mode D during one phase; flips to Mode E on a status flag transition | Cycle logs (D during `cycle_status: active`; E once `cycle_status: closed`) |

Modes A and E preserve audit integrity. Mode C is the only mode that *replaces* state — and it's only used where history is captured in a sibling file. Mode D is the workhorse — it gives operators current state at the top and history below, in one file.

## Mode discipline by Prototype

Every Prototype has a documented mode. Violating it corrupts the audit trail.

| Prototype | Mode | Notes |
|-----------|------|-------|
| PLC_Sphere_Manifest | C | Identity & charter; rarely changes; no history kept |
| PLC_Sphere_State | D | `## Decided` section + `## OPC Current Summary` section rollup; `## State History` for material shifts |
| PLC_Sphere_Decisions | A | Append-only decision log, elevated from session logs |
| PLC_Principal | D | Funnel + identity current; engagement-period and mastery history appended |
| PLC_Actor | D | Profile current; perception-history and resource-shift history appended |
| PLC_Campaign | D | Cohort + scope current; member-add/remove history appended |
| PLC_Cycle | **D → E** | Current cycle logs are Mode D (revisable); on `cycle_status: closed`, flip to Mode E and never edit |
| PLC_Session | A | Session logs are append-only after the session closes |
| PLC_OPC_Diagnostic | D | Active diagnostic ledger Mode D; archived diagnostic Mode E |
| PLC_Engagement_Retrospective | E | One-shot artifact at engagement end; never edited after publication |
| PLC_Move | C | Move catalog entries are reference data; revisable as the operator learns |
| PLC_Tactic | E | Catalogue tactics are sourced from the dissertation/sources and shipped immutable |
| PLC_Strategy | E | 16 strategies shipped immutable |
| PLC_Cluster | E | 84 clusters shipped immutable |
| PLC_Theorist | E | 50 theorists shipped immutable; operator may add adjacent theorists in a separate file |
| PLC_Pattern | D | Patterns are operator-discovered; revisable as evidence accumulates |

The shipped Catalogue (Tactic / Strategy / Cluster / Theorist) is Mode E because it's reference substrate, not sphere state. If the operator wants to extend the canon, they create new files in `Catalogue-Extensions/` rather than editing the shipped immutables. This preserves the scholarly canon per D15.

## The `## Current` and `## ... History` section discipline

Mode D files are the workhorse — they hold revisable state and append-only history in the same file. The two zones must be kept separate.

### Standard structure

Every Mode D file has at least these two sections:

```
## Current
<everything here is overwriteable; reflects state right now>

## ... History
<everything here is append-only; chronological log of material shifts>
```

The history section's exact name depends on the Prototype:

| Prototype | History section name |
|-----------|---------------------|
| PLC_Sphere_State | `## State History` |
| PLC_Principal | `## Engagement History` + `## Mastery History` |
| PLC_Actor | `## Perception History` + `## Resource History` |
| PLC_Campaign | `## Membership History` |
| PLC_OPC_Diagnostic | `## Score History` |
| PLC_Pattern | `## Evidence History` |
| PLC_Cycle | `## Phase Log` (during `cycle_status: active`) |

### Update rules

When updating a Mode D file:

1. **Edit `## Current` in place.** This is overwrite zone. Read, modify, write.
2. **Append to `## ... History`.** Never edit, reorder, or delete prior history entries. Each entry is timestamped (ISO 8601 date or datetime).
3. **History entries are dated facts**, not narrative. *"2026-06-13: Carol moved from `unaware` to `defensive` after the budget memo."* Not *"Carol seems to be reacting to recent events."*

If you find yourself wanting to edit a history entry: **stop.** The correct move is to append a correction entry, not to mutate the original. The audit trail's value is its immutability.

### Worked example: Actor file under Mode D

```
---
type: PLC_Actor
plc_Actor_ID: A-Carol-CFO
plc_Sphere: [[_sphere-manifest]]
plc_Current_Perception_Toward_Principal: defensive
plc_Update_Mode: D
---

# Carol Reyes — CFO

## Current
- **Position:** CFO, reports to CEO
- **Perception toward Principal:** defensive (since 2026-06-10)
- **Material resources:** budget authority over capital projects; appoints finance committee
- **Coalitions:** aligned with COO on cost-discipline platform; ambivalent toward Principal
- **Network distance:** 1 hop (direct peer)

## Perception History
- 2026-06-13: Confirmed `defensive` after Cycle-0008 cold-reading (3/3 indicators present)
- 2026-06-10: Shifted from `unaware` → `defensive` per the budget memo episode (Cycle-0007)
- 2026-04-22: Baseline at Practitioner Assessment — `unaware`

## Resource History
- 2026-05-15: Acquired budget authority over capital projects (org restructure)
- 2026-04-22: Baseline — finance committee chair, budget authority over OpEx
```

The `## Current` block is overwritten as state changes. The history blocks grow monotonically.

## The Cycle lifecycle — Mode D → E

PLC_Cycle is the only Prototype that changes modes. This is by design — the dissertation's 14-constituent cycle is recursive and revisable during execution; closed cycles are immutable audit records.

### State machine

```
planning → active → engaged → closed → e_immutable
```

| State | Mode | Edit semantics |
|-------|------|----------------|
| `planning` | D | Considered moves and decision rationale revisable |
| `active` | D | Phase log appendable; current step updatable |
| `engaged` | D | Move-in-flight phase log appendable; perception/outcome blocks fillable |
| `closed` | D | Final outcome and lessons editable for ~7 days post-close (grace window) |
| `e_immutable` | E | Sealed; no further edits permitted |

The grace window (closed → e_immutable) gives the operator time to refine the post-cycle lessons block without losing the audit guarantee. The flip is operator-explicit: on the next session opening, the AI asks "*Cycle-NNNN closed 7+ days ago. Seal as immutable?*" Once flipped, the file is Mode E forever.

Cycles still in `active` or `engaged` past their planned timeframe should surface in QUARTERLY-AUDIT as anomalies — open cycles aging is a workflow drift signal.

### What gets written when

| Step in 14-constituent cycle | Cycle file section updated |
|----------------------|---------------------------|
| Agenda body section | `## Agenda` |
| Landscape + OPC Self-Diagnosis + Principal Funnel body sections | `## Considered Moves` (initial set) + `## OPC Reference` |
| Gates + Considered Moves + Selected Moves body sections | `## Considered Moves` (full audit) + `## ALTERNATIVES-AUDIT § 15 Pass` + `## ETHICAL-ACCOUNTING § 11 Pass` + `## Selected Moves` |
| Engaged Moves body section (status flip to `engaged`) | `## Engaged Moves` (one entry per move executed) + status flips to `engaged` |
| Phase Log body section (Execution / Perception / Outcome tracking) | `## Phase Log` entries + reciprocal Actor file updates |
| Refinement body section (OPC + Funnel updates) | reciprocal updates to `_sphere-state.md` and Principal file |
| Cycle close (lessons + status flip) | `## Lessons` + status flips to `closed` |

## Reciprocal-update enforcement

The 24-relation reciprocal contract (per `04-SCHEMA.md` § Relation families) is the most-violated discipline in PLC. State persistence depends on enforcement.

### The protocol

After every Item-mutating session activity, before committing:

1. **Scan touched files** for added/removed relation references.
2. **For each new reference**, locate the target Item and verify the reverse pointer exists.
3. **If reverse pointer missing**, propose the reverse update to the operator and apply on confirmation.
4. **For each removed reference**, the reverse pointer must also be removed (relations are symmetric — half-removal is corruption).
5. **Log the reciprocal-update count** in the session log's `## Files Touched` block.

This protocol is repeated in `03-SESSION-PROTOCOL.md` step 8 and in every Mode D / Mode E template that participates in relations. Redundancy is by design — F5 is documented as a recurring failure mode.

### What to do when reciprocity breaks

If a QUARTERLY-AUDIT pass surfaces asymmetric graph state (Item X cites Y, but Y doesn't list X as citing it):

1. Determine which side is canonical (usually the side with richer context — the Tactic citing the Theorist is canonical over a bare backlink).
2. Repair the missing reverse pointer.
3. Log the repair in the audit session log as an F5 incident.
4. If the incident count exceeds 3 in a single audit, surface a workflow review — the operator's session-end discipline may need tightening.

## Sphere-state and sphere-decisions roll-up discipline

The sphere root has three backbone files: `_sphere-manifest.md`, `_sphere-state.md`, `_sphere-decisions.md`. Per D24 these are the operator's quick-reference layer.

| File | Mode | What it holds | Updated when |
|------|------|---------------|-------------|
| `_sphere-manifest.md` | C | Sphere identity, charter, principals, scope, mode | SPHERE-OPEN; rare mid-engagement updates |
| `_sphere-state.md` | D | `## Decided` (committed sphere-level decisions) + `## OPC Current Summary` (rollup of current OPC diagnostic scores) + `## State History` | End of any session that materially shifts sphere-level state; QUARTERLY-AUDIT |
| `_sphere-decisions.md` | A | Append-only log of consequential decisions elevated from sessions (per D24 user pushback resolution) | When a session log surfaces a sphere-level decision worth elevating |

The OPC Current Summary in `_sphere-state.md` is a *rollup view*, not the canonical diagnostic. The canonical is in `Spheres/<Sphere>/OPC-Diagnostics/<latest>.md`. If the two diverge, the diagnostic file wins; the state file is regenerated from it.

The elevation discipline for `_sphere-decisions.md`: not every session decision belongs here. The criterion is *"would a future operator need to know this to operate the sphere correctly?"* Examples that qualify: deciding the Principal's authority threshold; deciding to bring in a co-principal; deciding to shift the engagement's ethical guardrails. Examples that don't: which of two equivalent tactics to use in a single cycle.

## The status-flag pattern (for D → E transitions)

The D → E transition is operator-explicit and frontmatter-mediated. The pattern:

```yaml
---
type: PLC_Cycle
plc_Cycle_ID: C-0012
plc_Cycle_Status: closed         # planning | active | engaged | closed | e_immutable
plc_Update_Mode: D               # flips to E when plc_Cycle_Status: e_immutable
plc_Closed_Date: 2026-06-10
plc_Sealed_Date: ""              # populated at D → E flip
---
```

When `plc_Cycle_Status: e_immutable` and `plc_Sealed_Date` is populated, the AI treats the file as Mode E for the remainder of the engagement. Any edit attempt surfaces a refusal: *"Cycle C-0012 is sealed (2026-06-17). Edits not permitted. Create a follow-up note in `_sphere-state.md` if context changed."*

## Anti-patterns

- **F5 violation**: Adding a `plc_Cites_Theorists` reference without updating the reverse `plc_Citing_Tactics`. Run reciprocal-update protocol every session.
- **Mode A violation**: Editing a past decision log entry. The append-only contract means correcting via append, not via mutation.
- **Mode E violation**: Editing a closed cycle log or a shipped Catalogue Tactic. Shipped Catalogue extensions go in `Catalogue-Extensions/`; cycle corrections go in a follow-up cycle's `## Agenda` section referencing the prior cycle.
- **Mode D `## Current` corruption**: Letting history entries leak into the `## Current` block, or letting `## Current` content drift to a stale snapshot. Update both blocks every session that touches the file.
- **Cycle seal premature**: Flipping `plc_Cycle_Status: e_immutable` before the operator has had the grace window to refine lessons. Default to a 7-day grace; surface the flip prompt only after that window.
- **Sphere-decisions inflation**: Elevating every session decision to `_sphere-decisions.md`. Apply the criterion — *future-operator-needs-to-know* — strictly, or the file becomes noise and the operator stops reading it.

## Quality checks before closing a session

- [ ] Every Mode D file touched this session has its `## Current` block updated and a fresh history entry.
- [ ] Every new relation reference has its reciprocal counterpart in place (F5 protocol passed).
- [ ] No edits were made to Mode A history entries or Mode E files.
- [ ] If a cycle status flipped (planning → active, active → engaged, engaged → closed), the cycle file frontmatter reflects it and downstream state files (state, decisions, Principal funnel) reflect any sphere-level implications.
- [ ] Session log lists every file touched and includes the reciprocal-update count.
- [ ] If any sphere-level decision was made, evaluate against the elevation criterion and append to `_sphere-decisions.md` if it qualifies.

If any check fails, fix before closing.
