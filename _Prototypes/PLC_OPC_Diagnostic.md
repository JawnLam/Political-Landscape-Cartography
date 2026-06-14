---
Item_Prototype: Prototype
Item_ID: plc-opc-diagnostic-prototype
Title: "PLC_OPC_Diagnostic — Prototype Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
prototype_namespace: plc
prototype_version: "1.0"
---

# PLC_OPC_Diagnostic

## Purpose

A structured sphere-diagnostic instance using the **OPC Assessment v3.0** framework — 17 sections with 6-level hierarchical IDs. Each diagnostic is a point-in-time snapshot of the sphere's political-capital state. The Sphere_State file rolls up the latest diagnostic's headline reads; the diagnostic file itself carries the full structured scoring.

Per D7 + D27. Distinct from the `plc_OPC_Diagnostic_Seed` block in `_sphere-state.md` (which is a thin seed captured at sphere-open) — this Prototype is the **full ~90-minute structured assessment**.

## Cardinality and grain

- **N per sphere.** Typically 1 baseline at sphere-open + 1 per quarter + ad-hoc when material shifts occur.
- **Lives at**: `Spheres/<Sphere>/OPC-Diagnostics/OPC-<YYYY-MM-DD>.md`

## Durability mode

**Mode D while active; Mode E once archived.**

- **`Active`** (default — most recent diagnostic in the sphere): Mode D. `## Section Scores` editable for refinement within ~14 days; `## Score History` append-only.
- **`Archived`** (any diagnostic superseded by a newer one): Mode E. Sealed; never edited.

Per D28. Note: this is a softer D→E than the Cycle status flag — archival is automatic when a newer diagnostic publishes; no 7-day grace window.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `Item_Prototype` | string | Must be `PLC_OPC_Diagnostic` |
| `Item_ID` | string | `opc-<YYYY-MM-DD>` (or `opc-<YYYY-MM-DD>-<seq>` if multiple same-day) |
| `Title` | string | `"<Sphere Name> — OPC Diagnostic <date>"` |
| `Date_Added` | ISO date | Diagnostic performed date |
| `Date_Modified` | ISO date | Most recent refinement |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Diagnostic_State` | enum | `active \| archived` |
| `plc_Diagnostic_Scope` | enum | `full \| partial \| seed` (full = all 17 sections; partial = targeted subset; seed = CQ5 sphere-open) |
| `plc_Sections_Covered` | list[string] | OPC section numbers (e.g., `["1", "2", "13", "14"]` for a partial; `["1"-"17"]` for full) |
| `plc_Performed_By` | enum | `consultant_led \| principal_self \| co_facilitated` |
| `plc_Performed_In_Session` | link | `[[session-...]]` — the session this diagnostic ran in |
| `plc_Supersedes` | link | `[[opc-...]]` — prior diagnostic this replaces (empty for first) |
| `plc_Superseded_By` | link | `[[opc-...]]` — populated when a newer diagnostic publishes |
| `AI_Instructions` | string | Default `""` |

## Required body sections

```markdown
# <Sphere Name> — OPC Diagnostic <date>

## Diagnostic Context
<One paragraph: what triggered this diagnostic; what scope (full/partial/seed); what changed since prior.>

## Section Scores

<For each OPC section covered (1-17), one subsection. Each subsection includes the section's hierarchical-ID structure with operator's read for each leaf.>

### §1 — Power Structure
- §1.1 — <leaf>
- §1.2 — <leaf>
- ...

### §2 — Stakeholders & Actors
- §2.1 — <leaf>
- §2.2 — <leaf>
- ...

(... 17 sections total for a full diagnostic; selective for partial.)

## Headline Reads
<3-5 bullets summarizing what the diagnostic surfaced. This is the block that feeds `_sphere-state.md` § OPC Current Summary.>

## Trajectory Signals
<§14-specific: where the sphere is heading; over what horizon; with what confidence.>

## Score History
<Append-only log of within-window refinements. After archival, no further entries.>
- <date>: refined §<N>.<sub>: <prior> → <new>. Reason: <brief>.
...

## Cross-References
- Sphere: <link>
- Session: <link>
- Prior diagnostic: <link>
- Cycles citing this diagnostic: <links>
```

## The 17 OPC sections (reference)

For full diagnostics, all 17 sections must be covered. The sections (from OPC Assessment v3.0):

1. Power Structure
2. Stakeholders & Actors (incl. §2.2.1 stakeholder archetypes)
3. Resources
4. Relationships & Coalitions
5. Information & Communication
6. Decision Rights
7. Legitimacy & Mandate
8. Conflict & Tension
9. History & Precedent
10. Cultural Dynamics
11. **Harm & Ethical Evaluation** — used by ETHICAL-ACCOUNTING gate
12. Reciprocity & Obligation
13. Dynamics — Postures + Arcs + Themes (§13.1.1 / §13.1.2 / §13.2 / §13.3.1 / §13.3.2)
14. Trajectory
15. **Legitimate Alternatives** — used by ALTERNATIVES-AUDIT gate (10 constructive approaches)
16. **Practitioner Self-Assessment** — consultant-mode mandatory (D11)
17. **Advisor Engagement Politics** — consultant-mode mandatory (D11)

Sections 11, 15, 16, 17 carry special operational weight (gates + consultant pre-engagement).

## Relation slots

| Direction | Relation | Target Prototype | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 1 |
| Out | `plc_Performed_In_Session` | PLC_Session | 1 |
| Out | `plc_Supersedes` | PLC_OPC_Diagnostic | 0..1 |
| Out | `plc_Superseded_By` | PLC_OPC_Diagnostic | 0..1 |
| In | `plc_Latest_OPC_Diagnostic` (from Sphere_State) | PLC_Sphere_State | 0..1 (only the active one) |
| In | `plc_OPC_Diagnostic_Refs` (from Cycle) | PLC_Cycle | 0..N (cycles cite specific OPC IDs) |

## Reciprocal-update discipline

- When this diagnostic publishes as `active`, the prior `active` diagnostic flips to `archived` AND `plc_Superseded_By` populates.
- `_sphere-state.md`'s `plc_Latest_OPC_Diagnostic` updates to point here AND `## OPC Current Summary` regenerates from this diagnostic's `## Headline Reads`.
- Per D11, consultant-mode diagnostics MUST include §§ 16 + 17 — verify before publishing.
- Cycles that cited the prior diagnostic's OPC IDs do not auto-migrate; their references remain pointing at the now-archived diagnostic (audit-correct).

## Worked example (abbreviated)

```markdown
---
Item_Prototype: PLC_OPC_Diagnostic
Item_ID: opc-2026-06-01
Title: "Acme Corp — OPC Diagnostic 2026-06-01"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Diagnostic_State: active
plc_Diagnostic_Scope: full
plc_Sections_Covered: ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"]
plc_Performed_By: consultant_led
plc_Performed_In_Session: "[[session-acme-corp-005]]"
plc_Supersedes: "[[opc-2026-04-22]]"
plc_Superseded_By: ""
AI_Instructions: ""
---

# Acme Corp — OPC Diagnostic 2026-06-01

## Diagnostic Context
Quarterly full diagnostic. Triggered by family voting bloc shift (Robert wavering on succession-plan timing) — material enough to refresh the full sphere read, not just the affected sections.

## Section Scores

### §1 — Power Structure
- §1.1 — Formal authority structure: CEO + 7-director board (4 family / 3 independent)
- §1.2 — Voting bloc composition: family 3-1 in Sam's favor; Robert (board chair) is the swing
- §1.3 — ...

### §2 — Stakeholders & Actors
- §2.1 — 12 actors mapped (full cast)
- §2.2.1 — Stakeholder archetypes: Sam = "earned-mandate change-initiator" (§13.1.1.4); Carol = "shadow-CEO consolidator" (§13.1.2.7); Robert = "preservationist swing" (operator-extended)
- §2.3 — ...

(... 15 more sections ...)

### §16 — Practitioner Self-Assessment
- §16.1 through §16.14 — operator self-assessed; one item flagged below threshold (§16.7 — schedule-flexibility for client crisis response) — discussed with operator; mitigation plan in place.

### §17 — Advisor Engagement Politics
- §17.1 through §17.11 — engagement environment assessed; no contraindications.

## Headline Reads
- Power: family voting bloc 3-1 holds; Robert is the swing; loss of Robert → 2-2 deadlock
- Stakeholders: Carol's shadow-CEO consolidation accelerating; David coalitioned
- Trajectory: 6-month horizon to succession ratification; Q3 mandate-signal preservation is the cycle pressure
- Harm/ethical: no current §11 flags; gate-clear for cycle execution
- Practitioner readiness: green except §16.7 (mitigated)

## Trajectory Signals
6-month horizon (through 2026-Q4). Confidence: moderate. Key uncertainty: Robert's swing — needs direct signal in next 2-4 weeks.

## Score History
- (no within-window refinements yet)

## Cross-References
- Sphere: [[acme-corp-manifest]]
- Session: [[session-acme-corp-005]]
- Prior diagnostic: [[opc-2026-04-22]]
- Cycles citing this diagnostic: [[Cycle-0007]], [[Cycle-0008]]
```

## Anti-patterns

- Publishing a `full` diagnostic in consultant mode without §§ 16 + 17 covered. Per D11, this is a protocol violation.
- Letting two diagnostics carry `plc_Diagnostic_State: active` simultaneously. There is exactly one active per sphere at any time.
- Editing an archived diagnostic. Once superseded, sealed. Corrections live in the new active diagnostic.
- Confusing `seed` scope with `full` scope. The seed is the CQ5 sphere-open thumbnail; the full is the ~90-minute structured walk. Conflation degrades the audit signal.
- Letting `_sphere-state.md` § OPC Current Summary drift from this diagnostic's `## Headline Reads`. The state file is the rollup; this is the canonical.
