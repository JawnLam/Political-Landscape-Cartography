---
Item_ID: plc-pattern-family-change-initiator-postures
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Change-Initiator Postures — Family Overview"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
plc_Pattern_Family: change_initiator_postures
plc_Pattern_Source_OPC_Section: "13.1.1"
plc_Shipped_Atom_Count: 10
AI_Instructions: ""
---

# Change-Initiator Postures — Family Overview

## OPC Source

OPC Assessment v3.0 § 13.1.1 — Change-Initiator Postures within the broader Dynamics section.

## What this family captures

Active postures that change-initiating actors (typically the principal in PLC engagements) take when driving political work. These are engagement-specific dispositions, not structural archetypes. The principal's change-initiator posture shapes how their political work reads to other actors and which counter-postures it provokes.

Postures evolve during engagements. A principal might begin with one posture and stabilize at another as the engagement matures (see e.g., the Acme Corp worked example where Sam's "earned-mandate" posture stabilizes at sharpness 4 by Cycle-0007).

## Shipped atom count

**10 atoms per D10** sourced from OPC § 13.1.1.

## How to populate

For each of the 10 postures in OPC § 13.1.1:

1. Copy `_TEMPLATE.md` to `Pattern-<posture-slug>.md` (e.g., `Pattern-Earned-Mandate.md`)
2. Set `Title` to the posture name as defined in OPC
3. Populate the body sections from the OPC source
4. The `## Recommended Strategies (alignment)` block should name which Strategies amplify this posture
5. The `## Recommended Strategies (against)` block should name Strategies that work AGAINST this posture if the principal is on the opposition side

## Examples (illustrative — not load-bearing for ship)

OPC § 13.1.1 typically distinguishes change-initiator postures like:

- Earned-mandate (legitimacy-grounded; demonstrated track record)
- Crisis-mandate (urgency-grounded; external pressure forcing change)
- Visionary-mandate (future-grounded; articulated alternative state)
- Coalition-mandate (collective-grounded; broad stakeholder backing)
- Technical-mandate (expertise-grounded; specialist authority)
- Restorative-mandate (recovery-grounded; addressing prior failure)
- Reform-mandate (improvement-grounded; incremental progress)
- Strategic-mandate (competitive-grounded; market positioning)
- Innovation-mandate (novelty-grounded; new capability)
- Stewardship-mandate (institutional-grounded; preservation framing)

These are NOT canonical until populated from OPC source. The 10 actual postures come from OPC § 13.1.1.

## Cross-references

- Family library: `../README.md`
- Template: `_TEMPLATE.md`
- Pattern Prototype: `_types/PLC_Pattern.md`
- OPC source section: `_frameworks/OPC-Assessment.md § 13.1.1`
- Worked example: Sam's "earned-mandate" posture sharpened across cycles in `Spheres/Example-Sphere-Acme-Corp/` (Cycle-0007 close evidence)
