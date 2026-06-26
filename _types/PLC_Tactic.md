---
type: Prototype
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-tactic-prototype
title: "PLC_Tactic — Prototype Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
prototype_namespace: plc
prototype_version: "1.0"
---

# PLC_Tactic

## Purpose

A **composed political tactic** from the Political Warfare Catalogue — 782 tactics per D14, each with Catalogue Reference IDs 0001-0782, citations to theorists, classifications by Strategy (1-16) and Cluster (C01-C84). Tactics sit one grain above Moves: a Tactic is a coherent multi-Move play; a Move is the elemental atom inside a Tactic.

Per D14 + D15 + D16 + D20. The Catalogue is the **load-bearing tactical substrate** of PLC — when the operator asks "what could we do here?", the Catalogue is the answer space (gated by ALTERNATIVES-AUDIT + ETHICAL-ACCOUNTING per D9).

## Cardinality and grain

- **782 shipped + N operator-extended.** Shipped from `_frameworks/political-warfare-catalogue/tactics/`.
- **Lives at**: `_frameworks/political-warfare-catalogue/tactics/Tactic-<NNNN>.md` (4-digit zero-padded)
- Operator extensions live in `_frameworks/political-warfare-catalogue-extensions/tactics/`

## Durability mode

**Mode E — Immutable (for shipped Tactics) / Mode D (for operator-extended Tactics).**

- Shipped tactics: shipped from the canonical Catalogue source per D14. Immutable. To extend, create a new file in the extensions folder. Reasoning: the Catalogue is sourced scholarly substrate; mutating shipped tactics breaks the canon and corrupts the audit trail across cycles citing those tactics.
- Operator-extended tactics: Mode D with `## Current` + `## Refinement History` for evidentiary append.

Per D14 + D28 (Tactic row in mode table).

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Tactic` |
| `Item_ID` | string | `tactic-<NNNN>` |
| `Title` | string | `"Tactic <NNNN> — <Name>"` |
| `Date_Added` | ISO date | Catalogue ship date or operator-extension date |
| `Date_Modified` | ISO date | (shipped: same as Date_Added; extended: most recent refinement) |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Tactic_ID` | string | 4-digit Catalogue Reference ID (e.g., `"0029"`) per D18 system 3 |
| `plc_Tactic_Name` | string | Catalogue name |
| `plc_Tactic_Source` | enum | `catalogue \| operator_extended` |
| `plc_Strategies_Belongs_To` | list[integer] | Strategy numbers 1-16 (per D14; one Tactic may belong to multiple strategies) |
| `plc_Clusters_Belongs_To` | list[string] | Cluster codes C01-C84 |
| `plc_Cites_Theorists` | list[link] | `[[theorist-<name>]]` per cited theorist |
| `plc_Composed_Of` | list[link] | `[[move-<NNN>]]` per composing Move (reciprocal of PLC_Move.plc_Appears_In_Tactics) |
| `plc_Resource_Types_Required` | list[enum] | Subset of 9-type taxonomy |
| `plc_Slash_Addressing_Pattern` | string | Common slash-addressing form when invoked |
| `plc_Cited_In_Cycles` | list[link] | Cycles that selected this Tactic (per D16 audit trail) |
| `plc_Catalogue_Source_File` | string | Path to source markdown in `_frameworks/political-warfare-catalogue/tactics/<file>` |
| `AI_Instructions` | string | Default `""` |

## Required body sections

```markdown
# Tactic <NNNN> — <Name>

## Catalogue Summary
<Sourced from the Catalogue verbatim or near-verbatim. The shipped Tactic's canonical description.>

## Composed Of Moves
<Reciprocal of Move side. Lists the Moves that compose this Tactic with brief role-in-composition for each.>

## Strategies and Clusters
<Which Catalogue strategies (1-16) and clusters (C01-C84) this Tactic belongs to, with brief connection notes.>

## Theorist Citations
<Per D15. Which of the 50 theorists this Tactic draws on; citation counts feed theorist facet pages.>

## Worked Application Pattern
<How the Tactic typically plays out when invoked. Generic — not sphere-specific (F4 prevention).>

## Slash Addressing Pattern
<Canonical slash-addressing form for this Tactic. Operator examples.>

## When the ALTERNATIVES-AUDIT § 15 Pass Surfaces This Tactic
<Which of OPC § 15's 10 constructive approaches typically surface this Tactic during gate walks.>

## Ethical Considerations (§11 cross-references)
<OPC § 11 harm categories that ETHICAL-ACCOUNTING gate should check when this Tactic is in the considered set.>

## Cited In Cycles
<Auto-populated. Cycles that selected this Tactic — feeds D16 cross-cycle searchability.>

## Refinement History (operator-extended Tactics only)
<Append-only evidentiary refinements.>
```

## Relation slots

| Direction | Relation | Target Prototype | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Composed_Of` | PLC_Move | 1..N |
| Out | `plc_Cites_Theorists` | PLC_Theorist | 0..N |
| Out | `plc_Strategies_Belongs_To` | PLC_Strategy | 1..N (every Tactic belongs to ≥1 strategy) |
| Out | `plc_Clusters_Belongs_To` | PLC_Cluster | 1..N (every Tactic belongs to ≥1 cluster) |
| In | `plc_Appears_In_Tactics` (from Move) | PLC_Move | 1..N (reciprocal of above) |
| In | `plc_Citing_Tactics` (from Theorist) | PLC_Theorist | 0..N (reciprocal of Cites_Theorists) |
| In | (cycle selection / engagement) | PLC_Cycle | 0..N |

## Reciprocal-update discipline

- `plc_Composed_Of` ↔ `PLC_Move.plc_Appears_In_Tactics`. Symmetric.
- `plc_Cites_Theorists` ↔ `PLC_Theorist.plc_Citing_Tactics`. Symmetric. Per F5 — the most-violated discipline; consistently caught at QUARTERLY-AUDIT graph-integrity pass.
- `plc_Strategies_Belongs_To` ↔ `PLC_Strategy.plc_Tactics`. Symmetric.
- `plc_Clusters_Belongs_To` ↔ `PLC_Cluster.plc_Tactics`. Symmetric.
- When a Cycle's `plc_Tactic_IDs_Selected` includes this Tactic ID, this file's `plc_Cited_In_Cycles` updates.

## Worked example (abbreviated)

```markdown
---
type: PLC_Tactic
timestamp: "2026-04-01T00:00:00Z"
Item_ID: tactic-0029
title: "Tactic 0029 — Selective Disclosure Choreography"
Date_Added: 2026-04-01
Date_Modified: 2026-04-01
Needs_Processing: false
plc_Tactic_ID: "0029"
plc_Tactic_Name: "Selective Disclosure Choreography"
plc_Tactic_Source: catalogue
plc_Strategies_Belongs_To: [7, 11]
plc_Clusters_Belongs_To: ["C12", "C44"]
plc_Cites_Theorists:
  - "[[theorist-schelling]]"
  - "[[theorist-lukes]]"
plc_Composed_Of:
  - "[[move-042]]"
  - "[[move-057]]"
  - "[[move-088]]"
plc_Resource_Types_Required: [information, access, legitimacy]
plc_Slash_Addressing_Pattern: "α.<principal>/δ.<info-bundle>/Σ.<target-coalition>"
plc_Cited_In_Cycles:
  - "[[cycle-0007]]"
plc_Catalogue_Source_File: "_frameworks/political-warfare-catalogue/tactics/0029-selective-disclosure-choreography.md"
AI_Instructions: ""
---

# Tactic 0029 — Selective Disclosure Choreography

## Catalogue Summary
A composed play in which the principal reveals specific information to specific actors in a deliberately sequenced cadence designed to shape coalition incentives without direct confrontation. The choreography matters — what is revealed, to whom, in what order, with what gap. Force vector is incentive-side; disposition shifts are second-order effects.

## Composed Of Moves
- [[move-042]] — Selective Information Exposure (the elemental disclosure act)
- [[move-057]] — Sequenced Timing Control (the cadence dimension)
- [[move-088]] — Target Audience Segmentation (the audience-choice dimension)

The three Moves together constitute the Tactic; using any one alone is a degenerate (and often weaker) form.

## Strategies and Clusters
- **Strategy #7** — Coalition Preservation. This Tactic preserves coalition by shaping incentive structure without forcing positional choices.
- **Strategy #11** — Asymmetric Data Exposure. This Tactic is a controlled-asymmetry variant where the asymmetry is choreographed rather than ambient.
- **Cluster C12** — Information-Choreography cluster
- **Cluster C44** — Coalition-Stabilization cluster

## Theorist Citations
- **Schelling** — strategic-signaling lineage; the cadence of disclosure as the signal
- **Lukes** — three-dimensional power (the disclosure shapes the agenda, not just the decision)

## Worked Application Pattern
Principal identifies an information asymmetry they control. Maps target actors into segments based on incentive sensitivity. Designs a disclosure sequence that delivers different signal weights to different segments with controlled timing gaps. The choreography produces emergent coalition behavior without direct confrontation.

## Slash Addressing Pattern
`α.<principal>/δ.<info-bundle>/Σ.<target-coalition>` — principal-operator + information-asymmetry-element + target-coalition-set.

## When the ALTERNATIVES-AUDIT § 15 Pass Surfaces This Tactic
- §15.3 — Constructive information-sharing (when the disclosure is genuinely informative, not weaponized)
- §15.7 — Coalition-strengthening constructive approach (when the choreography preserves rather than fractures)

## Ethical Considerations
ETHICAL-ACCOUNTING gate should check:
- §11 Harm Scope 1 (target actor): is the choreography deceptive, or transparent-but-strategic? Latter clears; former flags.
- §11 Harm Scope 2 (non-target actors): does the asymmetric disclosure create unfair exclusion from material information?
- §11 Harm Scope 3 (sphere-wide): does the choreography corrupt the sphere's information ecosystem long-term?

## Cited In Cycles
- [[cycle-0007]] — Q2 mandate signal preservation; engaged past the capability-gate as part of strategic-signaling play
```

## Anti-patterns

- Editing a shipped Tactic. Mode E. To revise, create an operator-extended Tactic in the extensions folder citing the shipped one.
- Treating a Tactic as decomposable into Moves only when convenient. The `plc_Composed_Of` relation is required for every shipped Tactic — the composition is the analytical handle.
- Citing a theorist in `plc_Cites_Theorists` without updating that Theorist's `plc_Citing_Tactics`. F5 violation. The Catalogue ships with the reciprocal relations populated; preservation is the operator's responsibility.
- Letting `plc_Cited_In_Cycles` drift from actual cycle selections. The audit signal depends on this list being accurate (per D16).
- Inventing a Tactic-0XXXX number in extensions. Operator extensions use a different ID space (e.g., `EXT-0001`) — never overlap with the shipped 0001-0782 range.
- Conflating Strategy and Cluster — they are different classification axes. A Tactic belongs to ≥1 of each.
