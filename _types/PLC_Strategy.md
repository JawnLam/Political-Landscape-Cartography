---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-strategy-type
title: "PLC_Strategy — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
type_namespace: plc
type_version: "1.0"
---

# PLC_Strategy

## Purpose

A **lever-combination meta-strategy** — one of the 16 strategies in the Political Warfare Catalogue (per D14). A Strategy sits one grain above Tactics: where a Tactic is a composed multi-Move play, a Strategy is a coherent family of Tactics organized around a shared political force-vector and intent. The 16 strategies are the **first-cut answer space** when an operator asks "what's the strategic shape of this cycle?"

Per D14 + D20.

## Cardinality and grain

- **Exactly 16 shipped + N operator-extended.** Shipped from `_frameworks/political-warfare-catalogue/by-strategy/` per D14.
- **Lives at**: `_frameworks/political-warfare-catalogue/by-strategy/<NN>-<slug>.md` — **2-digit zero-padded** (`07-benefit-contrast.md`), no `Strategy-` prefix. `_frameworks/strategies/` holds operator notes only; the 16 atoms ship as facet files in the Catalogue mirror and nowhere else.
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

| Direction | Relation | Target Type | Cardinality |
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
title: "Strategy 7 — Benefit Contrast"
Date_Added: 2026-04-01
Date_Modified: 2026-04-01
Needs_Processing: false
plc_Strategy_Number: 7
plc_Strategy_Name: "Benefit Contrast"
plc_Strategy_Source: catalogue
plc_Force_Vector: "B(X)↑ + B(Y)↓ — raise the perceived benefit of the preferred position while lowering the perceived benefit of the adverse alternative. Both benefit levers, neither cost lever: the target is moved by what the two options are worth, never by what they cost."
plc_Tactics:
  - "[[tactic-0313]]"
  - "[[tactic-0507]]"
  - "[[tactic-0689]]"
plc_Theorists_Primary:
  - "[[theorist-kahneman]]"
  - "[[theorist-goffman]]"
plc_Slash_Addressing_Family: "[a.] ε_<NNNN>(<addr>/e.) → { [<addr>/t/D/P/b] +, [<addr>/t/D/Adv/b] − }"
plc_Cited_In_Cycles: []
plc_Catalogue_Source_File: "_frameworks/political-warfare-catalogue/by-strategy/07-benefit-contrast.md"
AI_Instructions: ""
---

# Strategy 7 — Benefit Contrast

## Force Vector
`B(X)↑ + B(Y)↓`. Raise the perceived benefit of the preferred position; lower the perceived benefit of the adverse alternative. Neither cost lever is touched — nothing is made harder for anyone, which is what distinguishes this from the triples. The target is left free to choose and simply finds one column worth more than it was.

## When This Strategy Fits
- The target's margin is a benefit judgment, not a friction judgment — they are weighing what the options are worth, not what they cost to take
- The principal can genuinely raise the preferred option's value, or can show the alternative is worth less than the target believes
- Cost levers are unavailable or would be read as coercion

## When This Strategy Misfits
- The blocker is cost, not value (the target already prefers the position and cannot afford it) — that is Cost Contrast, Strategy 8
- The benefit claim would have to be manufactured; two of this Strategy's three Tactics carry the deception axis for exactly this reason (0313 at severity 3, 0507 at severity 2)
- The margin is wide enough that a benefit-only pair cannot close it

## Member Tactics
Three, each carried in the facet file as both a specific and a generic entry (6 rows):
- [[tactic-0313]] — The Cosmetic KPI Push (C66)
- [[tactic-0507]] — The 'Voice of the Customer' Ventriloquism (C36)
- [[tactic-0689]] — The Hierarchy Signal / The Pecking Order Display (C59)

## Theoretical Lineage
- **Kahneman** (with Tversky) — prospect theory; the benefit judgment is reference-dependent, which is what makes B(X)↑ achievable without changing anything material
- **Goffman** — impression management; the presented value of an option, not its audited value, is what the target weighs

## Common Slash-Addressing Family
`[a.] ε_<NNNN>(<addr>/e.) → { [<addr>/t/D/P/b] +, [<addr>/t/D/Adv/b] − }` — both effect cells are `/b` (benefit); the absence of any `/c` cell is the Strategy's signature.

## ALTERNATIVES-AUDIT § 15 Bridge
- § 15.10 — Mutual-gain reframing (the most common bridge; a genuine mutual-gain case is a truthful B(X)↑)
- § 15.3 — Constructive information-sharing (when the alternative's benefit is overestimated and correcting the record is the whole move)

## ETHICAL-ACCOUNTING § 11 Profile
Strategy-7 plays typically flag:
- **Deception** — the dominant axis. 0313 (severity 3) and 0507 (severity 2) both manufacture the benefit signal rather than the benefit; 0689 (severity 1) does not carry the axis at all
- § 11 Harm Scope 3 (sphere-wide): metric and consultation channels degrade when they are used to carry benefit claims they cannot support
Strategy-level profile; per-Tactic flags in `INDEX-lspi.json` `ethical_valence` refine these.

## Cited In Cycles
(None yet — auto-populated rollup.)
```

## Anti-patterns

- Mutating one of the 16 shipped Strategies' Force Vector. Mode E. Extensions go in extensions folder.
- Adding a Tactic to `plc_Tactics` without updating the Tactic's `plc_Strategies_Belongs_To`. F5.
- Inventing Strategy numbers 17+. Operator extensions use `EXT-S-NNN` namespace, never extend the 1-16 numbered range.
- Treating Strategy as Cluster's synonym. Strategies are force-vector frames; Clusters are thematic groupings. Different classification axes; both apply to a Tactic.
