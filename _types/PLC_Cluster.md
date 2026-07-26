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

A **thematic grouping** of Tactics — one of the 83 clusters in the Political Warfare Catalogue (per D14), plus the `ORIGINAL` sentinel that carries the pre-existing analyses. Where Strategy is a force-vector frame (16 frames), Cluster is a thematic grouping (83 themes). The two are orthogonal classification axes: every Tactic belongs to ≥1 Strategy AND ≥1 Cluster. Clusters answer "what's this Tactic *about* (substantively)" while Strategy answers "what political force does it apply."

Per D14 + D20.

## Cardinality and grain

- **Exactly 84 facet files shipped + N operator-extended** — 83 cluster codes plus the `ORIGINAL` sentinel. Shipped from `_frameworks/political-warfare-catalogue/by-cluster/`.
- **Lives at**: `_frameworks/political-warfare-catalogue/by-cluster/<CNN>-<slug>.md` (no `Cluster-` prefix; slug truncated to a fixed filename width)
- Codes: `C01`-`C96`, 2-digit zero-padded, **with gaps — the range is not contiguous.** 83 codes are in use; `C28`, `C45`, `C70`, `C71`, `C77`, `C78`, `C84`, `C85`, `C88`, `C89`, `C92`, `C93`, `C94` do not exist. Plus the literal sentinel `ORIGINAL` (`ORIGINAL-original-(pre-existing-analyses).md`), which is a cluster value in `INDEX.json` but not a `C`-code. Never infer a file from the range — check `by-cluster/` or `INDEX.json`.
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
| `plc_Cluster_Code` | string | One of the 83 shipped codes in `C01`-`C96` (gapped — see Cardinality) or the `ORIGINAL` sentinel; `EXT-C-NNN` for extensions |
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
- `plc_Adjacent_Clusters` is symmetric: C12 lists C11 as adjacent ⇒ C11 lists C12.
- When a Cycle's `plc_Clusters_Engaged` includes this Cluster, `plc_Engaged_In_Cycles` updates here.

## Worked example (abbreviated)

```markdown
---
type: PLC_Cluster
timestamp: "2026-04-01T00:00:00Z"
Item_ID: cluster-C12
title: "Cluster C12 — Internal Compliance, Audit & HR Weaponization"
Date_Added: 2026-04-01
Date_Modified: 2026-04-01
Needs_Processing: false
plc_Cluster_Code: "C12"
plc_Cluster_Name: "Internal Compliance, Audit & HR Weaponization"
plc_Cluster_Source: catalogue
plc_Cluster_Theme: "Tactics that turn HR, Audit, Legal and Compliance functions into political weapons — selective enforcement, weaponized investigations, anonymous complaints, targeted audits, due-diligence diversions."
plc_Tactics:
  - "[[tactic-0053]]"
  - "[[tactic-0265]]"
  - "[[tactic-0419]]"
plc_Adjacent_Clusters:
  - "[[cluster-C11]]"
  - "[[cluster-C13]]"
plc_Theorists_Primary:
  - "[[theorist-williamson]]"
  - "[[theorist-goffman]]"
plc_Engaged_In_Cycles: []
plc_Catalogue_Source_File: "_frameworks/political-warfare-catalogue/by-cluster/C12-internal-compliance-audit-and-hr-weaponization.md"
AI_Instructions: ""
---

# Cluster C12 — Internal Compliance, Audit & HR Weaponization

## Thematic Characterization
Tactics that turn the organization's control functions against its own people. HR, Audit, Legal and Compliance exist to apply a rule uniformly; every Tactic here works by applying it selectively — the investigation that is opened on one person, the audit that lands on one department, the policy read strictly for one team and waived for another. The weapon is the legitimacy of the function, which is why these plays are so hard to name out loud.

## Member Tactics
- [[tactic-0053]] — Internal Regulatory Capture
- [[tactic-0265]] — The HR Hit Job
- [[tactic-0419]] — Targeted Auditing
(... 12 more Tactics in this Cluster — 15 total; see the facet file ...)

## Adjacent Clusters
- [[cluster-C11]] — Bureaucratic Friction & Red-Tape Weaponization (process as the instrument; C12 adds the enforcement function's authority)
- [[cluster-C13]] — Policy Weaponization, Workaround Reclassification & Catch-22 Engineering (the rule itself as the instrument)

## Theorist Concentration
- Williamson (8 of the 15 Tactics) — transaction-cost and governance-opportunism lineage
- Goffman, Akerlof, Kahneman and Pfeffer (4 each) — impression management, information asymmetry, framing, resource dependence

## When This Cluster Is Worth Surfacing
- An actor with control-function authority (CFO, GC, CHRO, audit chair) is the opposition
- UNCOVER work on selective enforcement — the same rule landing differently on different people
- Detection work: several C12 signatures are visible only as a pattern across cases, not in any single one

## Engaged In Cycles
(None yet — auto-populated as Cycles engage this Cluster.)
```

## Anti-patterns

- Treating Cluster as Strategy's synonym. Different classification axes. Strategy = force-vector frame; Cluster = thematic grouping.
- Mutating a shipped Cluster's theme. Mode E. Extensions go in extensions folder.
- Adjacent-Cluster asymmetry. If C12 lists C11 as adjacent, C11 must list C12. F5 violation otherwise.
- Adding a Tactic to `plc_Tactics` without updating the Tactic's `plc_Clusters_Belongs_To`. F5.
- Inventing codes. Only the 83 shipped codes and `ORIGINAL` exist; the gaps in `C01`-`C96` (`C28`, `C45`, `C70`, `C71`, `C77`, `C78`, `C84`, `C85`, `C88`, `C89`, `C92`, `C93`, `C94`) are not free slots and `C97+` is not a range. Operator extensions use `EXT-C-NNN` namespace.
