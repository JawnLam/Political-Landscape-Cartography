---
Item_Prototype: PLC_Move
Item_ID: move-<NNN>
Title: "Move <NNN> — <Name>"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Move_Number: <integer>
plc_Move_Name: "<Name>"
plc_Move_Source: dissertation_table_3   # dissertation_table_3 | operator_extended
plc_Move_Signature:
  PP: "0"   # + | - | 0
  AA: "0"
  B: "0"
  C: "0"
  Inc: "0"
  Dec: "0"
plc_Resource_Types_Required: []   # subset of 9-type taxonomy
plc_Appears_In_Tactics: []   # symmetric reciprocal with PLC_Tactic.plc_Composed_Of
plc_Slash_Operators_Used: []   # Greek operators from dissertation slash notation
plc_Citing_Cycles: []
AI_Instructions: ""
---

# Move <NNN> — <Name>

## Signature
PP: <+/-/0>  AA: <+/-/0>  B: <+/-/0>  C: <+/-/0>  Inc: <+/-/0>  Dec: <+/-/0>

> Signature reference:
> - **PP** (Principal Push): + applies force / - absorbs force / 0 neutral
> - **AA** (Actor Acceptance): + accepts/yields / - resists / 0 neutral
> - **B** (Benefit): + creates / - erodes / 0 neutral
> - **C** (Cost): + imposes / - reduces / 0 neutral
> - **Inc** (Incentive): + adds / - removes / 0 neutral
> - **Dec** (Decentive): + adds / - removes / 0 neutral

## Description
<One paragraph: what the Move does at the smallest grain; the elemental political action.>

## When to Use
- <condition where the signature aligns with cycle's needed force vector>

## When Not to Use
- <condition where the signature would backfire>

## Resources Required
- **<Resource type>:** <brief specifics>

## Appears In Tactics
<Reciprocal of `plc_Composed_Of` from Tactic side.>

## Slash Addressing Notes
<How this Move appears in slash notation when used. Operator examples.>

## Citing Cycles
<Auto-populated as cycles select this Move.>

## Refinement History (operator-extended Moves only)
<Append-only refinements as understanding deepens.>
