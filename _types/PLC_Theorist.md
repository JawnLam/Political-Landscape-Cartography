---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-theorist-type
title: "PLC_Theorist — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
type_namespace: plc
type_version: "1.0"
---

# PLC_Theorist

## Purpose

A **scholarly source-of-authority** — one of the 50 theorists in the Political Warfare Catalogue (per D15). Each Theorist is a first-class entity carrying citation counts, intellectual lineage notes, and links to the Tactics that cite them. Per D15, the Theorist canon is the **defensible scholarly substrate** that grounds PLC's recommendations — the published methodology README's "Foundations" section names all 50 with citation counts.

Per D15 + D19 + D20. The only Authority Type shipped as a first-class Item (per D19 Q2 lock — `PLC_Source` deferred).

## Cardinality and grain

- **Exactly 50 shipped + N operator-extended.** Shipped from `_frameworks/political-warfare-catalogue/by-theorist/`.
- **Lives at**: `_frameworks/political-warfare-catalogue/by-theorist/<theorist-slug>.md`
- Operator extensions live in `_frameworks/political-warfare-catalogue-extensions/by-theorist/` and use `<theorist-slug>` with `plc_Theorist_Source: operator_extended`

## Durability mode

**Mode E — Immutable (shipped) / Mode D (operator-extended).**

Per D15 + D28.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Theorist` |
| `Item_ID` | string | `theorist-<slug>` |
| `Title` | string | `"<Theorist Name> — Theorist"` |
| `Date_Added` | ISO date | |
| `Date_Modified` | ISO date | |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Theorist_Name` | string | Surname or full canonical name |
| `plc_Theorist_Full_Name` | string | Full given+family name |
| `plc_Theorist_Lifespan` | string | e.g., `"1921-2016"` or `"b. 1939"` |
| `plc_Theorist_Tradition` | string | Disciplinary lineage (e.g., "game theory / strategic behavior") |
| `plc_Theorist_Source` | enum | `catalogue \| operator_extended` |
| `plc_Citing_Tactics` | list[link] | Tactics that cite this Theorist (reciprocal of `PLC_Tactic.plc_Cites_Theorists`) |
| `plc_Citation_Count` | integer | Auto: `len(plc_Citing_Tactics)`. Material for the README "Foundations" section per D15. |
| `plc_Primary_For_Strategies` | list[link] | Strategies where this Theorist is a primary lineage source |
| `plc_Primary_For_Clusters` | list[link] | Clusters where this Theorist is most-cited |
| `plc_Invoked_In_Cycles` | list[link] | Cycles where `plc_Theorists_Invoked` includes this Theorist |
| `plc_Canonical_Works` | list[string] | Key publications that ground the Theorist's contribution |
| `plc_Catalogue_Source_File` | string | Path to canonical facet markdown |
| `AI_Instructions` | string | Default `""` |

## Required body sections

```markdown
# <Theorist Name> — Theorist

## Contribution Summary
<One paragraph: the Theorist's core contribution to political-action thinking. Why their work matters to PLC.>

## Tradition and Lineage
<Disciplinary tradition (game theory / sociology of power / organizational behavior / etc.). Who they extend; who extends them.>

## Canonical Works
<Key publications the Catalogue cites. Brief annotation per work.>

## Citation Profile
<Citation count + which Tactics, Strategies, Clusters most rely on this Theorist's thinking.>

## When To Invoke
<Conditions where pulling this Theorist's frame into a cycle's reasoning is appropriate.>

## When Not To Invoke
<Conditions where this Theorist's frame would mislead (e.g., applying Schelling's two-player game theory to a multi-coalition sphere).>

## Citing Tactics
<Auto-populated. Reciprocal of Tactic's `plc_Cites_Theorists`.>

## Invoked In Cycles
<Auto-populated.>
```

## Relation slots

| Direction | Relation | Target Type | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Citing_Tactics` | PLC_Tactic | 0..N (reciprocal of `plc_Cites_Theorists`) |
| Out | `plc_Primary_For_Strategies` | PLC_Strategy | 0..N |
| Out | `plc_Primary_For_Clusters` | PLC_Cluster | 0..N |
| Out | `plc_Invoked_In_Cycles` | PLC_Cycle | 0..N |
| In | `plc_Cites_Theorists` (from Tactic) | PLC_Tactic | 0..N (reciprocal of above) |
| In | `plc_Theorists_Invoked` (from Cycle) | PLC_Cycle | 0..N |

## Reciprocal-update discipline

- `plc_Citing_Tactics` ↔ `PLC_Tactic.plc_Cites_Theorists`. Symmetric. **Most-violated reciprocal in PLC** per F5 — caught at QUARTERLY-AUDIT graph-integrity pass.
- `plc_Citation_Count` is derived from `len(plc_Citing_Tactics)`. Drift between the count and the list signals graph corruption.
- `plc_Primary_For_Strategies` ↔ `PLC_Strategy.plc_Theorists_Primary`. Symmetric.
- `plc_Primary_For_Clusters` ↔ `PLC_Cluster.plc_Theorists_Primary`. Symmetric.

## Worked example (abbreviated)

```markdown
---
type: PLC_Theorist
timestamp: "2026-04-01T00:00:00Z"
Item_ID: theorist-schelling
title: "Schelling — Theorist"
Date_Added: 2026-04-01
Date_Modified: 2026-04-01
Needs_Processing: false
plc_Theorist_Name: "Schelling"
plc_Theorist_Full_Name: "Thomas C. Schelling"
plc_Theorist_Lifespan: "1921-2016"
plc_Theorist_Tradition: "game theory / strategic behavior"
plc_Theorist_Source: catalogue
plc_Citing_Tactics:
  - "[[tactic-0029]]"
  - "[[tactic-0301]]"
  - "[[tactic-0445]]"
  - "[[tactic-0118]]"
  # ... 126 more Tactic citations
plc_Citation_Count: 130
plc_Primary_For_Strategies:
  - "[[strategy-7]]"
  - "[[strategy-11]]"
plc_Primary_For_Clusters:
  - "[[cluster-C12]]"
  - "[[cluster-C17]]"
plc_Invoked_In_Cycles:
  - "[[cycle-0007]]"
plc_Canonical_Works:
  - "The Strategy of Conflict (1960)"
  - "Arms and Influence (1966)"
  - "Micromotives and Macrobehavior (1978)"
plc_Catalogue_Source_File: "_frameworks/political-warfare-catalogue/by-theorist/schelling.md"
AI_Instructions: ""
---

# Schelling — Theorist

## Contribution Summary
Foundational work on strategic signaling, commitment, and the structure of bargaining under interdependence. Reframed political action as a problem of how decisions interact rather than how decisions are made in isolation. The intellectual root for most of PLC's information-choreography and coalition-preservation Tactics.

## Tradition and Lineage
- **Tradition:** Game theory, with sociological extensions into organizational and political behavior.
- **Extends:** von Neumann–Morgenstern foundations; adds the asymmetric-information and commitment dimensions absent from classical game theory.
- **Extended by:** Axelrod (cooperation iteration); contemporary signaling-mechanism design; behavioral game theory applied to organizational politics.

## Canonical Works
- **The Strategy of Conflict (1960)** — the foundational text. Strategic signaling, commitment, focal points.
- **Arms and Influence (1966)** — coercion, deterrence, the structure of escalation.
- **Micromotives and Macrobehavior (1978)** — how individual incentive structures aggregate to system-level outcomes (the structural-incentive lens that grounds Coalition Preservation strategy).

## Citation Profile
- **130 Tactics** cite Schelling — the highest citation count in the Catalogue.
- **Primary for Strategies:** #7 (Coalition Preservation), #11 (Asymmetric Data Exposure).
- **Primary for Clusters:** C12 (Information-Choreography), C17 (Timing-Asymmetry).

## When To Invoke
- Cycle involves strategic signaling or commitment problems
- Information asymmetry is the primary lever
- Two-actor or small-coalition reasoning (Schelling's primary frame)
- Cycle horizon allows for sequential play (the commitment dimension needs time to unfold)

## When Not To Invoke
- Sphere is dominated by multi-party brokering with no clear principal-vs-counterparty axis (Schelling's two-player frame degrades)
- Cycle horizon is single-shot (commitment-based plays need iteration to bite)
- The political action is fundamentally about legitimacy or identity, not information or incentive (other theorists fit better — e.g., Lukes for legitimacy, Tilly for identity-mobilization)

## Citing Tactics
(... 130 Tactic links — abbreviated in this type example ...)

## Invoked In Cycles
- [[cycle-0007]] — Q2 mandate signal preservation
```

## Anti-patterns

- Editing a shipped Theorist file. Mode E. Operator's commentary or extensions go in extension files.
- Letting `plc_Citation_Count` drift from `len(plc_Citing_Tactics)`. The count is derived; mismatches signal F5 graph corruption.
- Reciprocal-pointer asymmetry. Tactic cites Schelling but Schelling's `plc_Citing_Tactics` doesn't include the Tactic — the most-common F5 violation in the Catalogue. Caught at QUARTERLY-AUDIT.
- Inventing theorist citations not in the Catalogue's source files. Operator can ADD theorist files (operator-extended), but cannot retroactively add citations from shipped Tactics to shipped Theorists.
- Truncating the citation profile in the README "Foundations" section — per D15, all 50 theorists with citation counts are named publicly.
