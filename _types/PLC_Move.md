---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-move-type
title: "PLC_Move — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
type_namespace: plc
type_version: "1.0"
---

# PLC_Move

## Purpose

The **smallest unit of political action** per D20 — a granular move from the Lam 2018 dissertation Table 3 with the **PP/AA/B/C/Inc/Dec signature**. Moves are the atoms; Tactics are higher-order compositions of Moves (see `PLC_Tactic.md`). Per D14, the Move catalog (~100 entries from dissertation Table 3) and the Tactic catalog (782 from the Political Warfare Catalogue) coexist at different grains.

Resolves D14's deferred grain question: separate first-class Types connected by reciprocal `plc_Composed_Of` ↔ `plc_Appears_In_Tactics` relations.

## Cardinality and grain

- **~100 ship-shipped + N operator-extended.** Shipped from `_frameworks/dissertation-table-3/`.
- **Lives at**: `_frameworks/dissertation-table-3/Move-<NNN>.md` (3-digit sequence)
- Operator extensions live in `_frameworks/dissertation-table-3-extensions/`

## Durability mode

**Mode C — Current overwrite (for shipped Moves) / Mode D (for operator-extended Moves).**

- Shipped moves: revisable reference data per D28 Move-row in the mode table. Reasoning: the dissertation Move set is the canonical substrate, but operators may refine wording, examples, or signature interpretation as their understanding deepens. Unlike Catalogue Tactics (Mode E shipped immutable), Moves are derived from a single source the operator may legitimately reinterpret.
- Operator-extended moves: Mode D with `## Current` + `## Refinement History` for evidentiary append.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Move` |
| `Item_ID` | string | `move-<NNN>` |
| `Title` | string | `"Move <NNN> — <Name>"` |
| `Date_Added` | ISO date | |
| `Date_Modified` | ISO date | |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Move_Number` | integer | Sequence within Table 3 (1-100ish) |
| `plc_Move_Name` | string | Short name as in Table 3 |
| `plc_Move_Source` | enum | `dissertation_table_3 \| operator_extended` |
| `plc_Move_Signature` | object | The 6-field PP/AA/B/C/Inc/Dec structure |
| `plc_Move_Signature.PP` | enum | `+ \| - \| 0` — Principal-Push direction |
| `plc_Move_Signature.AA` | enum | `+ \| - \| 0` — Actor-Acceptance direction |
| `plc_Move_Signature.B` | enum | `+ \| - \| 0` — Benefit direction |
| `plc_Move_Signature.C` | enum | `+ \| - \| 0` — Cost direction |
| `plc_Move_Signature.Inc` | enum | `+ \| - \| 0` — Incentive direction |
| `plc_Move_Signature.Dec` | enum | `+ \| - \| 0` — Decentive direction |
| `plc_Resource_Types_Required` | list[enum] | Subset of 9-type taxonomy needed to execute this Move |
| `plc_Appears_In_Tactics` | list[link] | `[[tactic-<NNNN>]]` per Tactic that composes this Move (reciprocal of PLC_Tactic.plc_Composed_Of) |
| `plc_Slash_Operators_Used` | list[string] | Greek operators from dissertation slash notation that this Move invokes (e.g., `α`, `δ`, `Σ`) |
| `plc_Citing_Cycles` | list[link] | Cycles that selected this Move |
| `AI_Instructions` | string | Default `""` |

### PP/AA/B/C/Inc/Dec signature semantics

From dissertation Table 3:

| Field | Stands for | Direction meaning |
|-------|------------|-------------------|
| PP | Principal Push | `+` Principal applies force; `-` Principal absorbs force; `0` Principal neutral |
| AA | Actor Acceptance | `+` Actor accepts/yields; `-` Actor resists; `0` Actor neutral |
| B | Benefit | `+` Move creates benefit; `-` Move erodes benefit; `0` Move benefit-neutral |
| C | Cost | `+` Move imposes cost; `-` Move reduces cost; `0` Move cost-neutral |
| Inc | Incentive | `+` Move adds incentive; `-` Move removes incentive; `0` Move incentive-neutral |
| Dec | Decentive | `+` Move adds disincentive; `-` Move removes disincentive; `0` Move decentive-neutral |

The signature is the diagnostic — two Moves with the same signature have similar political force regardless of surface description.

## Required body sections

```markdown
# Move <NNN> — <Name>

## Signature
PP: <+/-/0>  AA: <+/-/0>  B: <+/-/0>  C: <+/-/0>  Inc: <+/-/0>  Dec: <+/-/0>

## Description
<One paragraph: what the Move does at the smallest grain; the elemental political action.>

## When to Use
<Conditions where the Move's signature aligns with the cycle's needed force vector.>

## When Not to Use
<Conditions where the Move's signature would backfire or be wasted.>

## Resources Required
<Subset of 9-type taxonomy with brief specifics.>

## Appears In Tactics
<Reciprocal of `plc_Composed_Of` from Tactic side. Auto-populated/maintained.>

## Slash Addressing Notes
<How this Move appears in slash notation when used. Operator examples.>

## Citing Cycles
<Cycles that selected this Move. Auto-populated.>

## Refinement History (operator-extended Moves only)
<Append-only refinements as understanding deepens.>
```

## Relation slots

| Direction | Relation | Target Type | Cardinality |
|-----------|----------|------------------|-------------|
| In | `plc_Composed_Of` (from Tactic) | PLC_Tactic | 0..N |
| In | (cycle selection) | PLC_Cycle | 0..N |
| Out | `plc_Appears_In_Tactics` | PLC_Tactic | 0..N (reciprocal of above) |
| Out | `plc_Citing_Cycles` | PLC_Cycle | 0..N (rollup of cycle selections) |

## Reciprocal-update discipline

- `plc_Appears_In_Tactics` ↔ `PLC_Tactic.plc_Composed_Of`. Symmetric — if Tactic X cites Move 042, Move 042's appearance list includes X.
- When a Cycle selects a Move, this file's `plc_Citing_Cycles` updates.
- For operator-extended Moves: refinement to the signature requires a `## Refinement History` entry with reasoning.

## Worked example

```markdown
---
type: PLC_Move
timestamp: "2026-04-15T00:00:00Z"
Item_ID: move-042
title: "Move 042 — Selective Information Exposure"
Date_Added: 2026-04-15
Date_Modified: 2026-04-15
Needs_Processing: false
plc_Move_Number: 42
plc_Move_Name: "Selective Information Exposure"
plc_Move_Source: dissertation_table_3
plc_Move_Signature:
  PP: "+"
  AA: "0"
  B: "0"
  C: "0"
  Inc: "+"
  Dec: "0"
plc_Resource_Types_Required: [information, access]
plc_Appears_In_Tactics:
  - "[[tactic-0029]]"
  - "[[tactic-0301]]"
plc_Slash_Operators_Used: ["α", "δ"]
plc_Citing_Cycles:
  - "[[cycle-0007]]"
AI_Instructions: ""
---

# Move 042 — Selective Information Exposure

## Signature
PP: `+`  AA: `0`  C: `0`  B: `0`  Inc: `+`  Dec: `0`

## Description
Principal pushes by revealing specific information to specific actors at specific times. Actor-acceptance is neutral (the actor's posture toward the principal does not need to shift for this move to work). Adds incentive structure (information asymmetry creates new actor positioning). No direct cost or benefit; the move's force is incentive-side.

## When to Use
- Cycle needs `PP: +` force vector
- Information asymmetry exists that the principal controls
- Actor's incentive structure is the lever, not their disposition
- Two-step plays where information exposure now enables a follow-up move

## When Not to Use
- Cycle needs disposition shift (use a `AA: +` move instead)
- Information is symmetric (no asymmetry to exploit)
- Risk of information backfire (target actor may weaponize the exposure)

## Resources Required
- **Information**: the asymmetric signal itself
- **Access**: the channel to deliver to the target

## Appears In Tactics
- [[tactic-0029]] — Selective Disclosure Choreography
- [[tactic-0301]] — Asymmetric Briefing Cascade

## Slash Addressing Notes
Typically appears as `α.<principal>/δ.<info-signal>/<target-actor>` — principal-operator + information-asymmetry-element + target.

## Citing Cycles
- [[cycle-0007]] — Q2 mandate signal preservation (selected as part of Tactic 0301)
```

## Anti-patterns

- Treating Moves and Tactics as the same grain. They're not. Per D20: Move is elemental; Tactic is composed. The reciprocal relation captures the composition.
- Editing a shipped Move's signature without a `## Refinement History` entry justifying the reinterpretation.
- Letting `plc_Appears_In_Tactics` drift from `PLC_Tactic.plc_Composed_Of`. Symmetric reciprocal must hold. F5 audit catches.
- Inventing Moves not in Table 3 and labeling them `dissertation_table_3`. Operator extensions go in `operator_extended` source.
