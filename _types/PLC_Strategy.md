---
type: Prototype
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-strategy-prototype
title: "PLC_Strategy — Prototype Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
prototype_namespace: plc
prototype_version: "1.0"
---

# PLC_Strategy

## Purpose

A **lever-combination meta-strategy** — one of the 16 strategies in the Political Warfare Catalogue (per D14). A Strategy sits one grain above Tactics: where a Tactic is a composed multi-Move play, a Strategy is a coherent family of Tactics organized around a shared political force-vector and intent. The 16 strategies are the **first-cut answer space** when an operator asks "what's the strategic shape of this cycle?"

Per D14 + D20.

## Cardinality and grain

- **Exactly 16 shipped + N operator-extended.** Shipped from `_frameworks/political-warfare-catalogue/by-strategy/` per D14.
- **Lives at**: `_frameworks/strategies/Strategy-<N>.md` (1-16, no zero-padding) AND mirror facet in `_frameworks/political-warfare-catalogue/by-strategy/Strategy-<N>-<slug>.md`
- Operator extensions live in `_frameworks/strategies-extensions/` and use a separate ID space (e.g., `EXT-S-001`)

## Durability mode

**Mode E — Immutable (shipped) / Mode D (operator-extended).**

Per D14 + D28. Same reasoning as PLC_Tactic: the 16-strategy frame is sourced scholarly substrate; mutating shipped strategies breaks the canon.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Strategy` |
| `Item_ID` | string | `strategy-<N>` (1-16) or `strategy-ext-<NNN>` for extensions |
| `Title` | string | `"Strategy <N> — <Name>"` |
| `Date_Added` | ISO date | |
| `Date_Modified` | ISO date | |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Strategy_Number` | integer | 1-16 (shipped) or null for extensions |
| `plc_Strategy_Name` | string | |
| `plc_Strategy_Source` | enum | `catalogue \| operator_extended` |
| `plc_Force_Vector` | string | One-line characterization of the strategy's political force direction |
| `plc_Tactics` | list[link] | `[[tactic-<NNNN>]]` per member Tactic (reciprocal of `PLC_Tactic.plc_Strategies_Belongs_To`) |
| `plc_Theorists_Primary` | list[link] | Theorists whose work most directly shaped this Strategy |
| `plc_Slash_Addressing_Family` | string | The slash-addressing pattern shared by Tactics in this Strategy |
| `plc_Cited_In_Cycles` | list[link] | Cycles where `plc_Strategy_Number_Selected` equals this Strategy's number |
| `plc_Catalogue_Source_File` | string | Path to canonical Catalogue facet markdown |
| `AI_Instructions` | string | Default `""` |

## Required body sections

```markdown
# Strategy <N> — <Name>

## Force Vector
<One-paragraph characterization: what political force does this Strategy apply, against what target, with what intended dynamic?>

## When This Strategy Fits
<Conditions where adopting this Strategy as the cycle's frame is appropriate.>

## When This Strategy Misfits
<Conditions where adopting this Strategy would backfire or be inert.>

## Member Tactics
<List of Tactics in this Strategy. Each entry brief — full content in the Tactic file. This is the operator's quick lookup.>

## Theoretical Lineage
<Which theorists most directly shaped this Strategy. Citations to source works (in `_frameworks/sources/`).>

## Common Slash-Addressing Family
<Shared slash-addressing pattern across member Tactics.>

## ALTERNATIVES-AUDIT § 15 Bridge
<Which of OPC § 15's 10 constructive approaches typically open the door to this Strategy.>

## ETHICAL-ACCOUNTING § 11 Profile
<§ 11 harm categories most commonly flagged when this Strategy is in the considered set. Strategy-level not Tactic-level — per-Tactic flags live in PLC_Tactic.>

## Cited In Cycles
<Auto-populated rollup.>
```

## Relation slots

| Direction | Relation | Target Prototype | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Tactics` | PLC_Tactic | 1..N |
| Out | `plc_Theorists_Primary` | PLC_Theorist | 0..N |
| In | `plc_Strategies_Belongs_To` (from Tactic) | PLC_Tactic | N (reciprocal of above) |
| In | `plc_Strategy_Number_Selected` (from Cycle) | PLC_Cycle | 0..N |

## Reciprocal-update discipline

- `plc_Tactics` ↔ `PLC_Tactic.plc_Strategies_Belongs_To`. Symmetric — required.
- `plc_Theorists_Primary` ↔ `PLC_Theorist.plc_Primary_For_Strategies`. Symmetric.
- When a Cycle's `plc_Strategy_Number_Selected` matches this Strategy, this file's `plc_Cited_In_Cycles` updates.

## Worked example (abbreviated)

```markdown
---
type: PLC_Strategy
timestamp: "2026-04-01T00:00:00Z"
Item_ID: strategy-7
title: "Strategy 7 — Coalition Preservation"
Date_Added: 2026-04-01
Date_Modified: 2026-04-01
Needs_Processing: false
plc_Strategy_Number: 7
plc_Strategy_Name: "Coalition Preservation"
plc_Strategy_Source: catalogue
plc_Force_Vector: "Apply structural-incentive force to maintain an existing coalition against fracturing pressure; avoid direct confrontation that would force positional choices."
plc_Tactics:
  - "[[tactic-0029]]"
  - "[[tactic-0301]]"
  - "[[tactic-0118]]"
plc_Theorists_Primary:
  - "[[theorist-schelling]]"
  - "[[theorist-axelrod]]"
plc_Slash_Addressing_Family: "α/Σ.<coalition>/δ.<incentive-element>"
plc_Cited_In_Cycles:
  - "[[cycle-0007]]"
plc_Catalogue_Source_File: "_frameworks/political-warfare-catalogue/by-strategy/Strategy-7-coalition-preservation.md"
AI_Instructions: ""
---

# Strategy 7 — Coalition Preservation

## Force Vector
Apply structural-incentive force to maintain an existing coalition against fracturing pressure; avoid direct confrontation that would force positional choices. The Strategy's force is preventive, not propulsive — the goal is "no one defects" rather than "everyone advances."

## When This Strategy Fits
- Existing coalition is genuinely on the principal's side and worth holding
- Fracturing pressure is incentive-driven (not value-driven; value-driven fractures require a different Strategy)
- Time horizon allows for indirect play (Coalition Preservation is slow)

## When This Strategy Misfits
- Coalition is already fracturing past the point of incentive repair
- The opposition's pressure is value-driven (members reconsidering allegiance on principle, not incentive)
- Cycle horizon is acute (urgent threats need different Strategy frames)

## Member Tactics
- [[tactic-0029]] — Selective Disclosure Choreography
- [[tactic-0301]] — Asymmetric Briefing Cascade
- [[tactic-0118]] — Reciprocity Activation
(... 4 more tactics in this Strategy in the Catalogue ...)

## Theoretical Lineage
- **Schelling** — strategic signaling; incentive-structure preservation through choreographed communication
- **Axelrod** — cooperation-stability under iterated interaction; coalition durability theory

## Common Slash-Addressing Family
`α/Σ.<coalition>/δ.<incentive-element>` — principal-operator + coalition-set + incentive-asymmetry-element

## ALTERNATIVES-AUDIT § 15 Bridge
- § 15.7 — Coalition-strengthening constructive approach (the most common bridge)
- § 15.3 — Constructive information-sharing (when the preservation play involves disclosure)
- § 15.5 — Reciprocity-based exchange (when the preservation uses obligation activation)

## ETHICAL-ACCOUNTING § 11 Profile
Strategy-7 plays typically flag:
- § 11 Harm Scope 2 (non-coalition actors): risk of unfair exclusion from coalition benefits
- § 11 Harm Scope 3 (sphere-wide): risk of sphere-wide information ecosystem corruption if disclosure-based Tactics are used carelessly
Strategy-level profile; per-Tactic flags refine these.

## Cited In Cycles
- [[cycle-0007]] — Q2 mandate signal preservation
```

## Anti-patterns

- Mutating one of the 16 shipped Strategies' Force Vector. Mode E. Extensions go in extensions folder.
- Adding a Tactic to `plc_Tactics` without updating the Tactic's `plc_Strategies_Belongs_To`. F5.
- Inventing Strategy numbers 17+. Operator extensions use `EXT-S-NNN` namespace, never extend the 1-16 numbered range.
- Treating Strategy as Cluster's synonym. Strategies are force-vector frames; Clusters are thematic groupings. Different classification axes; both apply to a Tactic.
