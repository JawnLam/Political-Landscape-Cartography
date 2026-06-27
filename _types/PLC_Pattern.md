---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-pattern-type
title: "PLC_Pattern — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
type_namespace: plc
type_version: "1.0"
---

# PLC_Pattern

## Purpose

An **operator-discovered or seeded political pattern** — a recurring archetype, posture, arc, or dynamic in the sphere's political landscape. Per D10, six pattern families seed at ship from OPC sections; the family enum makes a single Type carry all six. Operators extend during engagements via UNCOVER work and quarterly audits.

Per D10 + D20 (Q3 lock — single Type with `plc_Pattern_Family` enum).

## Cardinality and grain

- **N per OV (shipped seeds) + N per sphere (operator-discovered).** Shipped seeds live in `_PATTERNS/<family>/`; sphere-specific extensions live in `Spheres/<Sphere>/Patterns/`.
- **Lives at**: `_PATTERNS/<family>/Pattern-<slug>.md` (shipped) OR `Spheres/<Sphere>/Patterns/Pattern-<slug>.md` (sphere-specific)

## Durability mode

**Mode D — Append-friendly current+history.**

- **`## Current` block** — overwrite zone for pattern description, current evidentiary basis, related theorists
- **`## Evidence History` block** — append-only log of each cycle/diagnostic that surfaced supporting (or contradicting) evidence

Per D28.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Pattern` |
| `Item_ID` | string | `pattern-<slug>` |
| `Title` | string | `"<Pattern Name> — Pattern"` |
| `Date_Added` | ISO date | |
| `Date_Modified` | ISO date | |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Pattern_Family` | enum | One of: `stakeholder_archetypes \| change_initiator_postures \| opposition_postures \| arc_dynamics \| power_dynamics_themes \| ethical_dilemmas` (per D10) |
| `plc_Pattern_Scope` | enum | `shipped_seed \| sphere_specific \| ov_wide_operator_extended` |
| `plc_Pattern_Source_OPC_Section` | string | OPC section that seeded this pattern (e.g., `13.1.1` for change-initiator-postures) |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` (empty for shipped seeds and OV-wide extensions) |
| `plc_Related_Theorists` | list[link] | Theorists whose frame illuminates this pattern |
| `plc_Related_Strategies` | list[link] | Strategies typically deployed against (or aligned with) this pattern |
| `plc_Confidence_Level` | enum | `seeded \| 1_observation \| 2_observations \| 3+_observations_confirmed` |
| `plc_Evidence_Cycles` | list[link] | Cycles whose phase logs provide evidentiary basis |
| `plc_Evidence_Diagnostics` | list[link] | OPC diagnostics that surfaced this pattern |
| `AI_Instructions` | string | Default `""` |

### Pattern family enum (per D10)

| Family | OPC source | Shipped count |
|--------|------------|---------------|
| `stakeholder_archetypes` | § 2.2.1 | per OPC |
| `change_initiator_postures` | § 13.1.1 | 10 |
| `opposition_postures` | § 13.1.2 | 10 |
| `arc_dynamics` | § 13.2 | 20 |
| `power_dynamics_themes` | § 13.3.1 | 10 |
| `ethical_dilemmas` | § 13.3.2 | 10 |

## Required body sections

```markdown
# <Pattern Name> — Pattern

## Family
**Family:** <family enum> (per OPC § <section>)

## Current

### Pattern Description
<One paragraph: what this pattern looks like in the wild. Distinguishing features. What makes it recognizable.>

### Detection Signals
<Cold-reading indicators an operator can use to detect this pattern.>

### What Typically Drives It
<Underlying conditions or incentive structures that produce this pattern.>

### Typical Lifecycle
<How this pattern usually develops, peaks, and resolves (or fails to). Especially material for `arc_dynamics`.>

### Recommended Strategies (against)
<For postures and dynamics: which Strategies typically respond well to this pattern.>

### Recommended Strategies (alignment)
<For supportive/allied patterns: which Strategies leverage this pattern.>

### Related Theorists
<Which theorists' frames illuminate this pattern. Citations.>

## Evidence History
<Append-only. Each entry: date + cycle/diagnostic source + what the evidence was + whether it confirms or contradicts.>
- <date>: <source>. Evidence: <brief>. <confirms | contradicts | partial>.
...

## Cross-References
- Sphere (if sphere-specific): <link>
- Cycles providing evidence: <links>
- Diagnostics surfacing: <links>
- Related patterns (often co-occur or contrast): <links>
```

## Relation slots

| Direction | Relation | Target Type | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 0..1 (only sphere-specific) |
| Out | `plc_Related_Theorists` | PLC_Theorist | 0..N |
| Out | `plc_Related_Strategies` | PLC_Strategy | 0..N |
| Out | `plc_Evidence_Cycles` | PLC_Cycle | 0..N |
| Out | `plc_Evidence_Diagnostics` | PLC_OPC_Diagnostic | 0..N |

## Reciprocal-update discipline

- Patterns are referenced *from* Cycles and Diagnostics; they don't enforce back-pointer Items on those (since a Cycle citing a Pattern in prose doesn't create a graph edge requiring symmetric update).
- However, `plc_Evidence_Cycles` should match the Cycles that have prose references to this Pattern in their bodies. QUARTERLY-AUDIT spot-checks.
- When `plc_Confidence_Level` advances (e.g., `1_observation` → `2_observations`), the supporting evidence cycle is appended to `## Evidence History` AND `plc_Evidence_Cycles` updates.

## Worked example (abbreviated)

```markdown
---
type: PLC_Pattern
timestamp: "2026-11-22T00:00:00Z"
Item_ID: pattern-family-succession-pressure-loop
title: "Family-Succession-Pressure-Loop — Pattern"
Date_Added: 2026-06-09
Date_Modified: 2026-11-22
Needs_Processing: false
plc_Pattern_Family: arc_dynamics
plc_Pattern_Scope: sphere_specific
plc_Pattern_Source_OPC_Section: "13.2"
plc_Sphere: "[[acme-corp-manifest]]"
plc_Related_Theorists:
  - "[[theorist-pfeffer]]"
  - "[[theorist-tilly]]"
plc_Related_Strategies:
  - "[[strategy-7]]"
  - "[[strategy-13]]"
plc_Confidence_Level: 3+_observations_confirmed
plc_Evidence_Cycles:
  - "[[cycle-0006]]"
  - "[[cycle-0009]]"
  - "[[cycle-0012]]"
plc_Evidence_Diagnostics:
  - "[[opc-2026-06-01]]"
  - "[[opc-2026-09-01]]"
AI_Instructions: ""
---

# Family-Succession-Pressure-Loop — Pattern

## Family
**Family:** `arc_dynamics` (per OPC § 13.2)

## Current

### Pattern Description
In family-board organizations facing succession-planning pressure, opposition actors (typically CFO or COO archetype) consolidate resource control through finance-committee or operating-committee staffing in the 12-18 months preceding succession ratification, generating a feedback loop where consolidated resources create perception-of-shadow-CEO authority, which in turn legitimizes further consolidation, which compresses the principal's mandate window.

### Detection Signals
1. Finance- or operating-committee composition changes that move authority away from principal's allies
2. Independent reporting lines being expanded or formalized
3. Communication channels with principal narrowing (1:1s replaced with email-only or committee-mediated)
4. External press citations of the opposition actor increasing in frequency or substance

### What Typically Drives It
- Family-board structures where succession is treated as institutional event rather than continuous process
- Opposition actor's existing functional authority (CFO/COO) is genuinely high-leverage
- Family voting bloc's attention is on family-personal dynamics, not operational politics

### Typical Lifecycle
1. **Initiation (12-18 months pre-succession):** First committee restructure
2. **Acceleration (6-12 months pre):** Resource consolidation visible to independents
3. **Crisis (3-6 months pre):** Either principal mounts coalition-preservation response, OR opposition's shadow-CEO position becomes self-legitimizing
4. **Resolution (succession event):** Pattern terminates with either principal's mandate preservation or principal's exit

### Recommended Strategies (against)
- **Strategy 7 (Coalition Preservation)** — preserve the family voting bloc against pressure
- **Strategy 13 (Counter-Consolidation)** — directly contest specific committee staffing decisions

### Recommended Strategies (alignment)
N/A — this is an opposition pattern; alignment isn't operative.

### Related Theorists
- **Pfeffer** — resource-dependence theory; the consolidation move is classic resource-dependence play
- **Tilly** — political-opportunity structure; the succession window is the opportunity structure

## Evidence History
- 2026-11-22: Cycle-0012 evidence. Carol's third committee staffing move; principal's coalition-preservation response held. CONFIRMS pattern (3rd observation).
- 2026-08-30: Cycle-0009 evidence. Independent director Elena cited as inflection point; supports detection signal #4. CONFIRMS.
- 2026-06-09: Cycle-0006 evidence. First observation. Carol's budget-memo timing + finance-committee staffing matched signals #1 + #3. PARTIAL (1 observation).

## Cross-References
- Sphere: [[acme-corp-manifest]]
- Evidence cycles: [[cycle-0006]], [[cycle-0009]], [[cycle-0012]]
- Diagnostics: [[opc-2026-06-01]], [[opc-2026-09-01]]
- Related patterns: [[Pattern-Shadow-CEO-Consolidation]] (opposition-posture family; same Acme sphere)
```

## Anti-patterns

- Assigning a `plc_Confidence_Level` higher than the evidence supports. Each level has explicit observation-count criteria.
- Editing `## Evidence History` entries. Append-only — even if the original interpretation turned out wrong, append a corrective entry rather than mutating.
- Promoting a sphere-specific Pattern to OV-wide before it has 3+ confirmations across multiple spheres. Pattern abstraction without evidentiary basis is theory-leakage.
- Conflating Pattern families. A pattern is in exactly one family; if it spans two, the framing is wrong and the operator should split into two Patterns or refine the description.
- Treating shipped seeds as immutable. Shipped seeds are Mode D — refinable via `## Evidence History` as operators add observations. Only the OV namespace itself (PLC) is Mode E.
