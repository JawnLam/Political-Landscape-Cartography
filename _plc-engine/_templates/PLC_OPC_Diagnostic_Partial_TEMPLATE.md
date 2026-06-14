---
Item_Prototype: PLC_OPC_Diagnostic
Item_ID: opc-<YYYY-MM-DD>
Title: "<Sphere Name> — OPC Partial Diagnostic <YYYY-MM-DD>"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Diagnostic_State: active
plc_Diagnostic_Scope: partial
plc_Sections_Covered: []   # list specific section numbers covered, e.g., ["1", "13.1.1", "14"]
plc_Performed_By: consultant_led
plc_Performed_In_Session: "[[session-<sphere-slug>-<NNN>]]"
plc_Supersedes: ""   # Partial diagnostics typically don't supersede full ones — they refine specific sections; only set this if the partial scope fully replaces the prior diagnostic's coverage for that scope.
plc_Superseded_By: ""
AI_Instructions: ""
---

# <Sphere Name> — OPC Partial Diagnostic <YYYY-MM-DD>

> **Partial scope.** Refines specific sections without full re-walk. Used when a material shift demands updated read on a subset of OPC sections but the full diagnostic was recent. Cycles citing OPC IDs from the prior full diagnostic remain authoritative for sections NOT covered here.

## Diagnostic Context
<One paragraph: what triggered the partial diagnostic; why this scope; what full diagnostic this refines on top of.>

## Section Scores

<Only sections listed in `plc_Sections_Covered`. For each section, include hierarchical structure as in full template.>

### §<N> — <Section Name>
- §<N>.<sub> — <leaf>
- §<N>.<sub> — <leaf>

## Headline Reads (delta vs prior diagnostic)
<3-5 bullets: what changed in the covered sections since the prior diagnostic.>

## Trajectory Signals (if §14 covered)
<Otherwise omit this section.>

## Score History
<Append-only — refinements within window.>

## Cross-References
- Sphere: [[<sphere-slug>-manifest]]
- Session: <link>
- **Prior full diagnostic (authoritative for non-covered sections):** <link>
- Cycles citing this partial diagnostic: <links>
