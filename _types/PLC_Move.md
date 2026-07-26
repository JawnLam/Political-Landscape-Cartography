---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-move-type
title: "PLC_Move — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-07-24
Needs_Processing: false
type_namespace: plc
type_version: "1.2"
---

# PLC_Move

## Purpose

The **smallest unit of political action** per D20 — a granular move from the Lam 2018 dissertation Table 3 with the **PP/AA/B/C/Inc/Dec signature**. Moves are the atoms; Tactics are higher-order compositions of Moves (see `PLC_Tactic.md`). Per D14, the Move catalog (**148 rows** from dissertation Table 3) and the Tactic catalog (782 from the Political Warfare Catalogue) coexist at different grains. The row count is authoritative from `_frameworks/dissertation-table-3/Table-3-Manifest.md`; the "~100" estimate carried at v1.0 was wrong and any surviving instance of it is stale.

Resolves D14's deferred grain question: separate first-class Types connected by reciprocal `plc_Composed_Of` ↔ `plc_Appears_In_Tactics` relations.

## Cardinality and grain

- **148 rows + N operator-extended.** Shipped from `_frameworks/dissertation-table-3/`. **3 of the 148 are authored Move files** (`Move-001`–`Move-003`); the other 145 exist only as rows in `Table-3-Manifest.md` and are carried as backlog in `ROADMAP.md`. A Move file you cannot find probably was never authored — read the manifest row rather than inferring a file.
- **Lives at**: `_frameworks/dissertation-table-3/Move-<NNN>-<slug>.md` (3-digit zero-padded sequence + kebab-case slug)
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
| `plc_Move_Number` | integer | Row number within Table 3 (1-148) |
| `plc_Move_Name` | string | Short name as in Table 3 |
| `plc_Move_Source` | enum | `dissertation_table_3 \| operator_extended` |
| `plc_Move_Signature` | object | The 6-field PP/AA/B/C/Inc/Dec structure |
| `plc_Move_Signature.PP` | enum | `+ \| - \| 0` — Principal-Push direction |
| `plc_Move_Signature.AA` | enum | `+ \| - \| 0` — Actor-Acceptance direction |
| `plc_Move_Signature.B` | enum | `+ \| - \| 0` — Benefit direction |
| `plc_Move_Signature.C` | enum | `+ \| - \| 0` — Cost direction |
| `plc_Move_Signature.Inc` | enum | `+ \| - \| 0` — Incentive direction |
| `plc_Move_Signature.Dec` | enum | `+ \| - \| 0` — Decentive direction |
| `plc_Resource_Types_Required` | list[enum] | Subset of `money \| hard_assets \| credibility \| attributes \| legitimacy \| information \| access \| title \| tribe` (dissertation 9-type taxonomy) `\| other` (v1.2+) — `other` REQUIRES a `## Resources Required` line naming the actual carrier. The nine are a non-exhaustive basis for elicitation, not a closed list; see `PLC_Actor.md` § `plc_Resources_Held` |
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
<Subset of 9-type taxonomy with brief specifics — plus any `other` carrier, which MUST be named here (v1.2+).>

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
title: "Move 042 — Seeking Opportunities for Exposure to Superiors and Other Influential Individuals"
Date_Added: 2026-04-15
Date_Modified: 2026-04-15
Needs_Processing: false
plc_Move_Number: 42
plc_Move_Name: "Seeking Opportunities for Exposure to Superiors and Other Influential Individuals"
plc_Move_Source: dissertation_table_3
plc_Move_Signature:
  PP: "+"
  AA: "0"
  B: "0"
  C: "0"
  Inc: "0"
  Dec: "0"
plc_Resource_Types_Required: [access, attributes]
plc_Appears_In_Tactics:
  - "[[tactic-0078]]"
  - "[[tactic-0081]]"
  - "[[tactic-0307]]"
plc_Slash_Operators_Used: ["α", "δ"]
plc_Citing_Cycles: []
AI_Instructions: ""
---

# Move 042 — Seeking Opportunities for Exposure to Superiors and Other Influential Individuals

## Signature
PP: `+`  AA: `0`  B: `0`  C: `0`  Inc: `0`  Dec: `0`

**Dissertation Table 3 classifications (row 42):**
- **Option Affected:** Preferred Position
- **Consideration Affected:** Varied
- **Effect on Component(s):** Varied
- **LSPI component:** `varied`

The actor acts, so `PP: +`. Everything else is `0` — not because the move is inert, but because Table 3 records this row's Consideration and Effect as *Varied*, and a Varied cell has no sign to transcribe. Do not resolve a Varied cell into `+` or `-` to make the signature look complete; the ambiguity is the datum.

## Description (verbatim from the manifest row)

Seeking opportunities for exposure to superiors and other influential individuals.

## When to Use
- Long-horizon positioning where the target's read of the actor has not formed yet
- Contexts where the actor's contribution is real but is being observed only through an intermediary
- Before any move that requires the target to already know who the actor is

## When Not to Use
- The target's read is already formed and favorable — exposure adds risk, not information
- The exposure route runs through a channel the opposition controls
- The actor has nothing to be observed doing yet; premature exposure fixes a weak read

## Resources Required
- **Access**: proximity to the superiors and influential individuals in question — the scarce carrier here
- **Attributes**: whatever the exposure is meant to display, which must exist before it can be seen

## Appears In Tactics
Per `INDEX-lspi.json` `provenance.lam_table3_refs`, three corpus tactics descend from row 42:
- [[tactic-0078]] — Shadow Promotion (informal access to leadership *is* the exposure)
- [[tactic-0081]] — Proximity Mapping (maps the exposure pathways this Move exploits)
- [[tactic-0307]] — The Politics of Presence (exposure as the point of attendance)

## Slash Addressing Notes
Typically appears as `α.<actor>/δ.<observable-attribute>/<target-superior>` — actor-operator + the attribute the exposure puts on display + the observing target.

## Citing Cycles
(Auto-populated as cycles select this Move.)
```

## Anti-patterns

- Treating Moves and Tactics as the same grain. They're not. Per D20: Move is elemental; Tactic is composed. The reciprocal relation captures the composition.
- Editing a shipped Move's signature without a `## Refinement History` entry justifying the reinterpretation.
- Letting `plc_Appears_In_Tactics` drift from `PLC_Tactic.plc_Composed_Of`. Symmetric reciprocal must hold. F5 audit catches.
- Inventing Moves not in Table 3 and labeling them `dissertation_table_3`. Operator extensions go in `operator_extended` source.
