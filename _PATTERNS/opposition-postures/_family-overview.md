---
Item_ID: plc-pattern-family-opposition-postures
Item_Prototype: Fleeting
Title: "Opposition Postures — Family Overview"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
plc_Pattern_Family: opposition_postures
plc_Pattern_Source_OPC_Section: "13.1.2"
plc_Shipped_Atom_Count: 10
AI_Instructions: ""
---

# Opposition Postures — Family Overview

## OPC Source

OPC Assessment v3.0 § 13.1.2 — Opposition Postures within the broader Dynamics section.

## What this family captures

Active postures that opposition actors (the actors working against the principal's agenda) take in response to the principal's change-initiator posture. Per the dialectical structure of OPC § 13.1, every change-initiator posture provokes a characteristic counter-posture set; the operator's read on which opposition posture is active determines which counter-strategies are viable.

Opposition postures evolve. Carol's "shadow-CEO consolidation" posture in the Acme Corp worked example developed from precursor signals (April-May) into confirmed posture (June, 3/3 detection signals).

## Shipped atom count

**10 atoms per D10** sourced from OPC § 13.1.2.

## How to populate

For each of the 10 opposition postures in OPC § 13.1.2:

1. Copy `_TEMPLATE.md` to `Pattern-<posture-slug>.md`
2. Set `Title` to the posture name as defined in OPC
3. Populate `## Pattern Description` from OPC source
4. Populate `## Detection Signals` — opposition postures often require 2-3 indicators present to confirm (single indicator may be coincidence; pattern requires reinforcement)
5. Populate `## What Typically Drives It` with the structural/incentive conditions OPC describes
6. Populate `## Typical Lifecycle` — opposition postures often have a 4-stage arc (precursor → emergence → consolidation → either crisis-resolution or escalation)
7. Populate `### Recommended Strategies (against)` — what Strategies work against this opposition posture
8. Cite the relevant theorists OPC associates with this posture

## Examples (illustrative — not load-bearing for ship)

OPC § 13.1.2 typically distinguishes opposition postures like:

- Defensive consolidation (the "shadow-CEO" pattern manifests here)
- Procedural obstruction
- Coalition blocking
- Resource hoarding
- Information asymmetry exploitation
- Legitimacy contesting
- Audience capture
- Delay-and-deflect
- Direct confrontation
- Strategic withdrawal

These are NOT canonical until populated from OPC source.

## Cross-references

- Family library: `../README.md`
- Template: `_TEMPLATE.md`
- Pattern Prototype: `_Prototypes/PLC_Pattern.md`
- OPC source section: `_frameworks/OPC-Assessment.md § 13.1.2`
- Worked example: Carol Reyes' "shadow-CEO consolidation" posture in `Spheres/Example-Sphere-Acme-Corp/Actors/actor-carol-cfo.md`; 3-stage observation history in `Spheres/Example-Sphere-Acme-Corp/Patterns/pattern-family-succession-pressure-loop.md`
