---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-cluster-type
title: "PLC_Cluster — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
type_namespace: plc
type_version: "1.0"
---

# PLC_Cluster

## Purpose

A **thematic grouping** of Tactics — one of the 84 clusters in the Political Warfare Catalogue (per D14). Where Strategy is a force-vector frame (16 frames), Cluster is a thematic grouping (84 themes). The two are orthogonal classification axes: every Tactic belongs to ≥1 Strategy AND ≥1 Cluster. Clusters answer "what's this Tactic *about* (substantively)" while Strategy answers "what political force does it apply."

Per D14 + D20.

## Cardinality and grain

- **Exactly 84 shipped + N operator-extended.** Shipped from `_frameworks/political-warfare-catalogue/by-cluster/`.
- **Lives at**: `_frameworks/political-warfare-catalogue/by-cluster/Cluster-<CNN>-<slug>.md`
- Codes: `C01` through `C84` (2-digit zero-padded)
- Operator extensions: separate ID space (e.g., `EXT-C-NNN`)

## Durability mode

**Mode E — Immutable (shipped) / Mode D (operator-extended).**

Per D14 + D28.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Cluster` |
| `Item_ID` | string | `cluster-<CNN>` (e.g., `cluster-C12`) |
| `Title` | string | `"Cluster <CNN> — <Name>"` |
| `Date_Added` | ISO date | |
| `Date_Modified` | ISO date | |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Cluster_Code` | string | `C01`-`C84` for shipped; `EXT-C-NNN` for extensions |
| `plc_Cluster_Name` | string | Short name |
| `plc_Cluster_Source` | enum | `catalogue \| operator_extended` |
| `plc_Cluster_Theme` | string | One-line thematic characterization |
| `plc_Tactics` | list[link] | Member Tactics (reciprocal of `PLC_Tactic.plc_Clusters_Belongs_To`) |
| `plc_Adjacent_Clusters` | list[link] | Clusters with thematic overlap (often co-cited in operator's UNCOVER work) |
| `plc_Theorists_Primary` | list[link] | Theorists most-cited across this Cluster's Tactics |
| `plc_Engaged_In_Cycles` | list[link] | Cycles whose `plc_Clusters_Engaged` includes this Cluster code |
| `plc_Catalogue_Source_File` | string | Path to canonical facet markdown |
| `AI_Instructions` | string | Default `""` |

## Required body sections

```markdown
# Cluster <CNN> — <Name>

## Thematic Characterization
<One paragraph: what substantive theme does this Cluster organize Tactics around?>

## Member Tactics
<List of Tactics in this Cluster. Brief; full content in Tactic files.>

## Adjacent Clusters
<Other Clusters with thematic overlap. Useful during UNCOVER work — when this Cluster surfaces, adjacent ones often do too.>

## Theorist Concentration
<Theorists most-cited across this Cluster's Tactics. Often signals the Cluster's intellectual provenance.>

## When This Cluster Is Worth Surfacing
<Conditions where pulling all Tactics in this Cluster into consideration is appropriate (typically during MOVE-LOOKUP or UNCOVER work).>

## Engaged In Cycles
<Auto-populated.>
```

## Relation slots

| Direction | Relation | Target Type | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Tactics` | PLC_Tactic | 1..N |
| Out | `plc_Adjacent_Clusters` | PLC_Cluster | 0..N (symmetric) |
| Out | `plc_Theorists_Primary` | PLC_Theorist | 0..N |
| In | `plc_Clusters_Belongs_To` (from Tactic) | PLC_Tactic | N (reciprocal of above) |
| In | `plc_Clusters_Engaged` (from Cycle, as Cluster code) | PLC_Cycle | 0..N |

## Reciprocal-update discipline

- `plc_Tactics` ↔ `PLC_Tactic.plc_Clusters_Belongs_To`. Symmetric — required.
- `plc_Adjacent_Clusters` is symmetric: C12 lists C44 as adjacent ⇒ C44 lists C12.
- When a Cycle's `plc_Clusters_Engaged` includes this Cluster, `plc_Engaged_In_Cycles` updates here.

## Worked example (abbreviated)

```markdown
---
type: PLC_Cluster
timestamp: "2026-04-01T00:00:00Z"
Item_ID: cluster-C12
title: "Cluster C12 — Information-Choreography"
Date_Added: 2026-04-01
Date_Modified: 2026-04-01
Needs_Processing: false
plc_Cluster_Code: "C12"
plc_Cluster_Name: "Information-Choreography"
plc_Cluster_Source: catalogue
plc_Cluster_Theme: "Tactics organized around the deliberate sequencing and audience-segmentation of information disclosure as the primary political instrument."
plc_Tactics:
  - "[[tactic-0029]]"
  - "[[tactic-0301]]"
  - "[[tactic-0445]]"
plc_Adjacent_Clusters:
  - "[[cluster-C44]]"
  - "[[cluster-C17]]"
plc_Theorists_Primary:
  - "[[theorist-schelling]]"
  - "[[theorist-lukes]]"
plc_Engaged_In_Cycles:
  - "[[cycle-0007]]"
plc_Catalogue_Source_File: "_frameworks/political-warfare-catalogue/by-cluster/Cluster-C12-information-choreography.md"
AI_Instructions: ""
---

# Cluster C12 — Information-Choreography

## Thematic Characterization
Tactics organized around the deliberate sequencing and audience-segmentation of information disclosure as the primary political instrument. What gets revealed matters less than the cadence and the audience map. Choreography is the lever.

## Member Tactics
- [[tactic-0029]] — Selective Disclosure Choreography
- [[tactic-0301]] — Asymmetric Briefing Cascade
- [[tactic-0445]] — Information-Gap Mapping
(... ~6 more Tactics in this Cluster ...)

## Adjacent Clusters
- [[cluster-C44]] — Coalition-Stabilization (Information-Choreography often serves coalition-stabilization plays)
- [[cluster-C17]] — Timing-Asymmetry (sequencing is the shared dimension)

## Theorist Concentration
- Schelling (most-cited across this Cluster) — strategic-signaling lineage
- Lukes (second-most) — three-dimensional power's information-control axis

## When This Cluster Is Worth Surfacing
- Cycle agenda involves information asymmetry the principal controls
- UNCOVER work on information-flow gaps in the sphere
- MOVE-LOOKUP for "how do we use what we know without making it public?"

## Engaged In Cycles
- [[cycle-0007]] — Q2 mandate signal preservation
```

## Anti-patterns

- Treating Cluster as Strategy's synonym. Different classification axes. Strategy = force-vector frame; Cluster = thematic grouping.
- Mutating a shipped Cluster's theme. Mode E. Extensions go in extensions folder.
- Adjacent-Cluster asymmetry. If C12 lists C44 as adjacent, C44 must list C12. F5 violation otherwise.
- Adding a Tactic to `plc_Tactics` without updating the Tactic's `plc_Clusters_Belongs_To`. F5.
- Inventing C85+ codes. Operator extensions use `EXT-C-NNN` namespace.
