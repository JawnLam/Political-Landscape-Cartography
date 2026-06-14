---
Item_ID: plc-pattern-family-arc-dynamics
Item_Prototype: Fleeting
Title: "Arc Dynamics — Family Overview"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
plc_Pattern_Family: arc_dynamics
plc_Pattern_Source_OPC_Section: "13.2"
plc_Shipped_Atom_Count: 20
AI_Instructions: ""
---

# Arc Dynamics — Family Overview

## OPC Source

OPC Assessment v3.0 § 13.2 — Arc Dynamics within the broader Dynamics section. The largest family in the OPC pattern library (20 atoms per D10).

## What this family captures

Multi-cycle political arcs that play out across an engagement's lifetime. Arc dynamics are different from postures (§ 13.1) in that postures are point-in-time dispositions; arc dynamics are temporal patterns that develop across many cycles. The Acme Corp worked example's "family-succession-pressure-loop" pattern is an arc-dynamic instance.

Arc dynamics are the most operationally useful pattern family for **prediction**. Once an operator recognizes which arc dynamic is active in a sphere, they can predict the next inflection point and prepare counter-moves before the inflection arrives.

## Shipped atom count

**20 atoms per D10** sourced from OPC § 13.2. The 20-count reflects that arc dynamics have higher granularity than posture families — multiple variants of a "succession pressure" arc, multiple variants of a "coalition fracture" arc, etc.

## How to populate

For each of the 20 arc dynamics in OPC § 13.2:

1. Copy `_TEMPLATE.md` to `Pattern-<arc-slug>.md`
2. Set `Title` to the arc name as defined in OPC
3. Populate `## Pattern Description` from OPC source
4. Populate `## Detection Signals` — arc dynamics often have signals that emerge in temporal sequence (signal-1 typically precedes signal-2 by N months)
5. Populate `## Typical Lifecycle` — arc dynamics by definition have a temporal arc; populate with 3-5 stages
6. Populate `### Recommended Strategies` for each arc stage — which Strategies fit Stage 1 vs Stage 3 differ substantially
7. Cite relevant theorists OPC associates with each arc dynamic

## Examples (illustrative — not load-bearing for ship)

OPC § 13.2 typically distinguishes arc dynamics like:

- Succession-pressure-loop (family-board variant; founder-CEO variant; etc.)
- Coalition-fracture-and-reform
- Resource-consolidation-cascade
- Mandate-erosion arc
- Trust-rebuilding arc
- Crisis-and-recovery
- Transition-of-power
- Generational-handoff
- Reform-and-counter-reform
- (etc. — 20 total per OPC § 13.2)

The worked example's `pattern-family-succession-pressure-loop` is a sphere-specific instance of an OPC § 13.2 arc dynamic; the shipped pattern is the canonical version.

## Cross-references

- Family library: `../README.md`
- Template: `_TEMPLATE.md`
- Pattern Prototype: `_Prototypes/PLC_Pattern.md`
- OPC source section: `_frameworks/OPC-Assessment.md § 13.2`
- Worked example: `Spheres/Example-Sphere-Acme-Corp/Patterns/pattern-family-succession-pressure-loop.md` (sphere-specific instance of an arc-dynamic pattern)
