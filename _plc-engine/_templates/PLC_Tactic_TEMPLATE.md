---
type: PLC_Tactic
Item_ID: tactic-<NNNN>
title: "Tactic <NNNN> — <Name>"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Tactic_ID: "<NNNN>"   # 4-digit Catalogue Reference ID; operator extensions use EXT-<NNNN>
plc_Tactic_Name: "<Name>"
plc_Tactic_Source: catalogue   # catalogue | operator_extended
plc_Strategies_Belongs_To: []   # subset of 1-16
plc_Clusters_Belongs_To: []   # subset of C01–C96 (83 codes, gapped) + `ORIGINAL`
plc_Cites_Theorists: []   # symmetric reciprocal with PLC_Theorist.plc_Citing_Tactics
plc_Composed_Of: []   # symmetric reciprocal with PLC_Move.plc_Appears_In_Tactics
plc_Resource_Types_Required: []
plc_Slash_Addressing_Pattern: ""
plc_Cited_In_Cycles: []
plc_Catalogue_Source_File: ""
AI_Instructions: ""
---

# Tactic <NNNN> — <Name>

> **Mode E (shipped) — DO NOT EDIT.** To revise, create an operator-extended Tactic in `_frameworks/political-warfare-catalogue-extensions/tactics/` citing this one. Operator-extended Tactics are Mode D.

## Catalogue Summary
<Sourced from the Catalogue verbatim or near-verbatim. The shipped Tactic's canonical description.>

## Composed Of Moves
<Reciprocal of Move side. Brief role-in-composition for each.>

- [[move-<NNN>]] — <role in composition>

## Strategies and Clusters
- **Strategy #<N>** — <connection note>
- **Cluster <CNN>** — <connection note>

## Theorist Citations
- **<Theorist>** — <lineage note>

## Worked Application Pattern
<How the Tactic typically plays out. Generic — not sphere-specific (F4 prevention).>

## Slash Addressing Pattern
<Canonical slash-addressing form. Operator examples.>

## When the ALTERNATIVES-AUDIT § 15 Pass Surfaces This Tactic
<Which of OPC § 15's 10 constructive approaches typically open the door.>

## Ethical Considerations (§11 cross-references)
<OPC § 11 harm categories that ETHICAL-ACCOUNTING gate should check.>

- Harm Scope 1 (target actor): <check>
- Harm Scope 2 (non-target actors): <check>
- Harm Scope 3 (sphere-wide): <check>

## LSPI Facets (v1.2+, optional)

> **Sidecar-resident — do NOT fill these in a shipped Tactic body (Mode E).** Source of truth is `_frameworks/political-warfare-catalogue/INDEX-lspi.json`, keyed by tactic ID (alongside `lspi_levers` and `epsilon_template`). Operator-extended Tactics (Mode D) may carry the same facets in frontmatter, using these vocabularies verbatim. Interpretive facets are P10 proposals pending operator QA.

- **`required_resources`:** `[{type, role, note}]` — type ∈ money | hard_asset | credibility | attribute | legitimacy | information | access | title | tribe; role ∈ enabling | consumed
- **`detectability`:** `{level: low | med | high, signature: "<the tell>"}` — feeds MOVE-LOOKUP output and the estimation loop's observation model
- **`certainty_class`:** certain | probable | extra_conditional | spurious
- **`ethical_valence`:** `{axes: [...], severity: 1-3}` — axes ⊆ deception | coercion | fairness | transparency | dignity | loyalty_exploitation | harm_to_third_parties | institutional_damage; pre-populates the § 11 checks above
- **`counter_tactic_ids`:** `["<NNNN>", …]` — tactics that counter this one (this one is *countered-by* them)
- **`counters_tactic_ids`:** `["<NNNN>", …]` — tactics this one counters (derived reciprocal: counters ↔ countered-by)
- **`provenance`:** `{lam_table3_refs: [<row numbers per Table-3-Manifest.md>], vignette_refs: [Charles | Jim | Nathan | Sarah | Rusty]}`

## Cited In Cycles
<Auto-populated. Feeds D16 cross-cycle searchability.>

## Refinement History (operator-extended Tactics only)
<Append-only evidentiary refinements.>
