---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-tactic-type
title: "PLC_Tactic — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-07-24
Needs_Processing: false
type_namespace: plc
type_version: "1.2"
---

# PLC_Tactic

## Purpose

A **composed political tactic** from the Political Warfare Catalogue — 782 tactics per D14, each with Catalogue Reference IDs 0001-0782, citations to theorists, classifications by Strategy (1-16) and Cluster (83 numbered codes in `C01`-`C96`, plus the `ORIGINAL` sentinel). Tactics sit one grain above Moves: a Tactic is a coherent multi-Move play; a Move is the elemental atom inside a Tactic.

Per D14 + D15 + D16 + D20. The Catalogue is the **load-bearing tactical substrate** of PLC — when the operator asks "what could we do here?", the Catalogue is the answer space (gated by ALTERNATIVES-AUDIT + ETHICAL-ACCOUNTING per D9).

## Cardinality and grain

- **782 shipped + N operator-extended.** Shipped from `_frameworks/political-warfare-catalogue/tactics/`.
- **Lives at**: `_frameworks/political-warfare-catalogue/tactics/<range>/<NNNN>-<slug>.md` — bucketed by hundred (`0000-0100/`, `0101-0200/`, … `0701-0800/`); 4-digit zero-padded ID + kebab-case slug
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
| `plc_Clusters_Belongs_To` | list[string] | Cluster codes as the catalogue writes them: 83 numbered facets in `C01`-`C96` (the range has gaps — 13 codes are unused) **plus** the `ORIGINAL` sentinel for the 34 pre-existing analyses. 84 cluster facet files in `by-cluster/`. `ORIGINAL` is a legal value here; do not coerce it to a number |
| `plc_Cites_Theorists` | list[link] | `[[theorist-<name>]]` per cited theorist |
| `plc_Composed_Of` | list[link] | `[[move-<NNN>]]` per composing Move (reciprocal of PLC_Move.plc_Appears_In_Tactics) |
| `plc_Resource_Types_Required` | list[enum] | Subset of 9-type taxonomy |
| `plc_Slash_Addressing_Pattern` | string | Common slash-addressing form when invoked |
| `plc_Cited_In_Cycles` | list[link] | Cycles that selected this Tactic (per D16 audit trail) |
| `plc_Catalogue_Source_File` | string | Path to source markdown — `_frameworks/political-warfare-catalogue/tactics/<range>/<NNNN>-<slug>.md`. Include the bucket directory; a path without it does not resolve |
| `AI_Instructions` | string | Default `""` |

### Optional LSPI facets (v1.2+; per substrate authority 5 and the Tactic-Corpus Integration Spec)

Shipped tactic files are Mode E — these facets live in the sidecar `_frameworks/political-warfare-catalogue/INDEX-lspi.json`, keyed by tactic ID. Operator-extended tactics may carry them in frontmatter directly.

| Facet | Schema | Pass | Status |
|-------|--------|------|--------|
| `lspi_levers` | `[{component: P/b\|P/c\|Adv/b\|Adv/c, sign: +\|-, intensity: 1-3, corpus_lever}]` — the tactic's signed, intensity-weighted deltas. Alias map: corpus `X`→`P`, corpus `Y`→`Adv` (mandatory; F9/F10 discipline) | 2 | **populated (WS4 complete, 2026-07-24)** — 779/783; 4 empty-lever exceptions (`0015`, `0028`, `0031`, `0037`) logged in the runbook |
| `epsilon_template` | The display string of the three-place ε-form (below). ε is a citation into the Catalogue, not a primitive | 2 | **populated (WS4 complete, 2026-07-24)** — derived from levers + θ |
| `epsilon_tuple` | `{delta, theta, meta}` — the same content **structurally**: `delta` = the signed, intensity-weighted component list; `theta` = typed resources with `enabling`/`consumed` roles; `meta` = `detectability` + `certainty_class` + `ethical_valence`. **Consumers read this; the string is display** | 2 | **populated (WS4 complete, 2026-07-24)** |
| `required_resources` | `[{type: <9-carrier enum>, role: enabling\|consumed, note}]` — θ; what the capability gate tests | 3 | **populated (WS4 complete, 2026-07-24)** — 782/783 |
| `detectability` | `{level: low\|med\|high, signature: "<the tell>"}` — feeds MOVE-LOOKUP output and the estimation loop's observation model (the signature is a probe target; see `_frameworks/lspi/observation-model-grounding.md`) | 4 | **populated (WS4 complete, 2026-07-24)** — 782/783 |
| `certainty_class` | `certain \| probable \| extra_conditional \| spurious` | 4 | **populated (WS4 complete, 2026-07-24)** — 782/783 |
| `ethical_valence` | `{axes: [<8-axis enum>], severity: 1-3}` — pre-populates ETHICAL-ACCOUNTING prompts | 4 | **populated (WS4 complete, 2026-07-24)** — 782/783 |
| `counter_tactic_ids` | `[tactic_id, …]` — promoted from Resolution Approach prose; the defense graph (**countered-by** half of `counters ↔ countered-by`) | 5 | **populated (WS4 complete, 2026-07-24)** — 152 records, 174 links |
| `counters_tactic_ids` | `[tactic_id, …]` — the **derived reciprocal**: if A lists B in `counter_tactic_ids`, B's record lists A here. Generated from `counter_tactic_ids`, never hand-authored; regeneration is the only supported way to change it | 5 | **populated (WS4 complete, 2026-07-24)** — 70 reciprocals |
| `provenance` | `{lam_table3_refs: [row numbers per Table-3-Manifest.md], vignette_refs: [Charles\|Jim\|Nathan\|Sarah\|Rusty]}` — the citable bridge back to the 25 interviews | 6 | **populated (WS4 complete, 2026-07-24)** — 606 records; anchor 0158 validated |

**Pass numbering (authoritative).** 1 = P/Adv alias adoption · 2 = `lspi_levers` + `epsilon_template` · 3 = `required_resources` · 4 = `detectability` + `certainty_class` + `ethical_valence` · 5 = `counter_tactic_ids` · 6 = `provenance`. This matches `_frameworks/lspi/WS4-RUNBOOK.md`, the sidecar `INDEX-lspi.json`, and the upstream integration spec. (Earlier revisions of this file numbered passes 3–6 one lower; that numbering is retired — cite the runbook's, not the old one.)

#### The ε-template (three-place form)

The upstream spec defines the template as a three-place tuple `ε_T := ⟨ Δ_T , θ_T , meta_T ⟩`, emitting an execution line of the form `[a.] ε(<addr>/e.) → { deltas } consuming { θ }`. The shipped string was Δ-only for one release — the dropped `consuming { θ }` place is load-bearing, because θ is exactly what the capability gate tests. It is now spec-conformant:

```
[a.] ε_<ID>(<addr>/e.) → { [<addr>/t/D/<component>] <sign> ·i<intensity>, … } consuming { <carrier> (<role>), … }
```

Instantiating binds the slash-address prefix and the concrete resource instances, yielding a normal LSPI execution line. Records with **no `required_resources`** emit the **delta-only variant** (no `consuming` clause): that means θ is **unknown, not empty** — read it as "the resource requirement was not derivable from this record's prose," never as "this tactic is free."

Worked (0158 — The Favor Bank Run):

```
[a.] ε_0158(<addr>/e.) → { [<addr>/t/D/P/c] - ·i3, [<addr>/t/D/Adv/c] + ·i3 } consuming { credibility (consumed), tribe (enabling) }
```

#### Facet vocabularies (as the sidecar enforces them)

| Facet | Vocabulary |
|-------|------------|
| `required_resources.type` | `money \| hard_asset \| credibility \| attribute \| legitimacy \| information \| access \| title \| tribe` |
| `required_resources.role` | `enabling` (needed to act) \| `consumed` (spent by acting) |
| `detectability.level` | `low \| med \| high` — a prior on how hard the tell is to see, **not** evidence the tactic is in play |
| `detectability.signature` | free text — the observable tell |
| `certainty_class` | `certain \| probable \| extra_conditional \| spurious` |
| `ethical_valence.axes` | subset of `deception \| coercion \| fairness \| transparency \| dignity \| loyalty_exploitation \| harm_to_third_parties \| institutional_damage` |
| `ethical_valence.severity` | `1 \| 2 \| 3` |

Note the singular carrier spellings (`hard_asset`, `attribute`) — the sidecar's vocabulary, not the Actor file's plural enum. Do not silently coerce between them.

#### Measured coverage (2026-07-24)

- **782 of 783** records carry all four interpretive facets (`required_resources`, `detectability`, `certainty_class`, `ethical_valence`). The 783rd is the corpus placeholder `0037` — not a tactic; its `facet_status` records facets as *not applicable*, not missing.
- **152** records carry counter links, **174** links total, **70** reciprocals in `counters_tactic_ids`. Sparse by design: prose counters that are postures rather than catalogue tactics were left as prose.
- **606** records carry Table-3 provenance, covering **127 of the 148** manifest rows. The 21 uncovered rows are a corpus-coverage gap, not a manifest error (runbook § pass-6 finding).
- **All facet values are P10 proposals pending operator QA — not facts.** They are interpretive derivations from prose. Quote them with their epistemic status; a `certainty_class` of `probable` is a reading, and `detectability.signature` is a candidate tell, not an observation.

## Required body sections

```markdown
# Tactic <NNNN> — <Name>

## Catalogue Summary
<Sourced from the Catalogue verbatim or near-verbatim. The shipped Tactic's canonical description.>

## Composed Of Moves
<Reciprocal of Move side. Lists the Moves that compose this Tactic with brief role-in-composition for each.>

## Strategies and Clusters
<Which Catalogue strategies (1-16) and clusters (`C01`-`C96` codes, or `ORIGINAL`) this Tactic belongs to, with brief connection notes.>

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

| Direction | Relation | Target Type | Cardinality |
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
- `counter_tactic_ids` ↔ `counters_tactic_ids` (**counters / countered-by**, v1.2+, sidecar-only). Symmetric **by generation, not by hand**: the reciprocal is regenerated from the forward links. Hand-editing `counters_tactic_ids` is the one way to corrupt the defense graph silently.

## Worked example (abbreviated)

```markdown
---
type: PLC_Tactic
timestamp: "2026-04-01T00:00:00Z"
Item_ID: tactic-0029
title: "Tactic 0029 — The 'Decoy' Initiative"
Date_Added: 2026-04-01
Date_Modified: 2026-04-01
Needs_Processing: false
plc_Tactic_ID: "0029"
plc_Tactic_Name: "The 'Decoy' Initiative"
plc_Tactic_Source: catalogue
plc_Strategies_Belongs_To: [8, 13]
plc_Clusters_Belongs_To: ["ORIGINAL"]
plc_Cites_Theorists:
  - "[[theorist-kahneman]]"
  - "[[theorist-tversky]]"
  - "[[theorist-schelling]]"
plc_Composed_Of:
  - "[[move-001]]"
  - "[[move-002]]"
  - "[[move-042]]"
plc_Resource_Types_Required: [money, hard_assets, access]
plc_Slash_Addressing_Pattern: "[a.] ε_0029(<addr>/e.) → { [<addr>/t/D/P/c] - ·i3, [<addr>/t/D/Adv/c] + ·i3 } consuming { money (consumed), hard_asset (consumed), access (enabling) }"
plc_Cited_In_Cycles:
  - "[[cycle-0007]]"
plc_Catalogue_Source_File: "_frameworks/political-warfare-catalogue/tactics/0000-0100/0029-the-decoy-initiative.md"
AI_Instructions: ""
---

# Tactic 0029 — The 'Decoy' Initiative

## Catalogue Summary
Launching a high-profile, resource-intensive project that is ultimately expendable, designed specifically to draw attention and resistance away from the actual, more critical transformation efforts. Type `hybrid`. The distinctive signature is that the tactic never engages the real change on its merits — it manipulates the geometry of what gets scrutinized rather than what gets argued.

## Composed Of Moves
- [[move-001]] — Perception Management (the root move: controlling what the opposition concludes is the live threat)
- [[move-002]] — Inflating the Significance or Magnitude of the Actor's Duties and Responsibilities (the decoy must be inflated enough to hold the opposition's full attention)
- [[move-042]] — Selective Information Exposure (manufacturing the decoy's salience through the channels the actor controls)

Using any one alone is a degenerate form: an inflated project nobody was steered toward is just an expensive project.

## Strategies and Clusters
- **Strategy #8 — Cost Contrast** · `C(X)↓ + C(Y)↑` (primary classification). The real change advances cheaply because opposition attention is absorbed elsewhere; effective resistance becomes prohibitively expensive because the opposition's finite capacity is spent on the wrong fight.
- **Strategy #13 — Y-Focused Triple** · `B(X)↑ + B(Y)↓ + C(Y)↑` (the source file's alternative analysis, read from the target's choice architecture rather than the deployer's). Both are recorded rather than one silently dropped — this is exactly the multi-strategy case `list[integer]` exists for.
- **Cluster ORIGINAL** — the catalogue's sentinel for the 34 pre-existing analyses, **not** a themed C-code. `plc_Clusters_Belongs_To` here holds `"ORIGINAL"`; do not coerce it into the `C01`-`C96` range.

## Theorist Citations
- **Kahneman** — the finite attentional pool (System 1 / System 2 capacity limits): opponents cannot scrutinize everything at once
- **Tversky** — salience bias out of the availability research: scrutiny flows to what is cognitively prominent, not to what is strategically important
- **Schelling** — focal-point coordination in adversarial form: manufacturing a focal point of conflict coordinates the opposition onto a battleground of the actor's choosing

## Worked Application Pattern
The actor identifies a real change that would draw organized resistance if it were the most salient thing moving. They launch a second initiative — genuinely expensive, highly visible, with named executives and committed budget — that they can afford to lose. Opposition capacity routes to the decoy; the real change proceeds through routine governance channels. Effectiveness turns on three structural conditions: the decoy must be credible enough not to be dismissed as a feint; real resources must be visibly committed to sustain that credibility; and the real change must land at peak decoy distraction. It fails when opposition leadership has the discipline to ask "what else is moving right now?", or when an outside observer names the real change publicly before the decoy fight resolves.

## Slash Addressing Pattern
The validated ε-form from the sidecar — copied, never composed (F10):

`[a.] ε_0029(<addr>/e.) → { [<addr>/t/D/P/c] - ·i3, [<addr>/t/D/Adv/c] + ·i3 } consuming { money (consumed), hard_asset (consumed), access (enabling) }`

θ spelling note: the sidecar writes the carrier `hard_asset` (singular); `plc_Resource_Types_Required` above uses the 9-type taxonomy's `hard_assets`. Both are correct in their own vocabulary — do not silently coerce between them (see § *Facet vocabularies*).

## When the ALTERNATIVES-AUDIT § 15 Pass Surfaces This Tactic
Against OPC § 15.1's 10 constructive approaches, the gate walk typically surfaces this Tactic at:
- `honest_dialogue` — would naming the real change directly cost less than the decoy's budget?
- `problem_solving` — is the anticipated resistance tracking a genuine defect in the change, which dissolving would remove?

## Ethical Considerations (§11 cross-references)
The sidecar's `ethical_valence` flags axes `deception`, `transparency`, `institutional_damage` at severity 2 of 3. ETHICAL-ACCOUNTING should check:
- **§ 11.1.1 individual_impact** — `reputation_annihilation` for opposition leaders who spend a quarter's credibility on a fight the actor always intended to lose. That is the mechanism, not a side effect.
- **§ 11.1.2 organizational_damage** — `trust_annihilation` if the decoy is later recognized as one; the detectability signature below *is* that recognition event.
- **§ 11.1.3 systemic_effects** — `institutional_rot` and `legitimacy_loss`: a governance process that can be routed around by manufacturing salience has been taught that it can be.

Detectability is `low`, signature *"a loudly launched initiative is quietly defunded once a quieter change completes"*; `certainty_class` is `extra_conditional`. Both are P10 proposals pending operator QA, not observations.

## Cited In Cycles
- [[cycle-0007]] — selected into the engaged set; realized values against these projections live in that cycle's LSPI Operation Record
```

## Anti-patterns

- Editing a shipped Tactic. Mode E. To revise, create an operator-extended Tactic in the extensions folder citing the shipped one.
- Treating a Tactic as decomposable into Moves only when convenient. The `plc_Composed_Of` relation is required for every shipped Tactic — the composition is the analytical handle.
- Citing a theorist in `plc_Cites_Theorists` without updating that Theorist's `plc_Citing_Tactics`. F5 violation. The Catalogue ships with the reciprocal relations populated; preservation is the operator's responsibility.
- Letting `plc_Cited_In_Cycles` drift from actual cycle selections. The audit signal depends on this list being accurate (per D16).
- Inventing a Tactic-0XXXX number in extensions. Operator extensions use a different ID space (e.g., `EXT-0001`) — never overlap with the shipped 0001-0782 range.
- Conflating Strategy and Cluster — they are different classification axes. A Tactic belongs to ≥1 of each.
