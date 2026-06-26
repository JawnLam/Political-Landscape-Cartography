---
Item_ID: plc-pattern-family-power-dynamics-themes
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Power-Dynamics Themes — Family Overview"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
plc_Pattern_Family: power_dynamics_themes
plc_Pattern_Source_OPC_Section: "13.3.1"
plc_Shipped_Atom_Count: 10
AI_Instructions: ""
---

# Power-Dynamics Themes — Family Overview

## OPC Source

OPC Assessment v3.0 § 13.3.1 — Power-Dynamics Themes within the broader Dynamics section.

## What this family captures

Recurring thematic structures in how power operates within an organization. Unlike postures (§ 13.1) which are actor-bound and arcs (§ 13.2) which are temporal, power-dynamics themes are **system-level patterns** that characterize the entire sphere's political economy regardless of which specific actors are in play.

Themes are diagnostic at the sphere level. An operator identifies which themes are active in the sphere as part of OPC diagnostic § 13.3; the themes shape which strategies are viable in the sphere overall. The Acme Corp worked example currently shows "agenda-control-vs-execution-discipline" as the active power-dynamics theme (Lukes' three-dimensional power frame).

## Shipped atom count

**10 atoms per D10** sourced from OPC § 13.3.1.

## How to populate

For each of the 10 themes in OPC § 13.3.1:

1. Copy `_TEMPLATE.md` to `Pattern-<theme-slug>.md`
2. Set `Title` to the theme name as defined in OPC
3. Populate `## Pattern Description` from OPC source
4. Populate `## Detection Signals` — themes are system-level, so signals often surface as observed patterns across multiple actors simultaneously
5. Populate `### Related Theorists` — power-dynamics themes have deep theoretical lineage (Lukes, Foucault, Pfeffer, Bourdieu, etc.); cite OPC's associations
6. Populate `### Recommended Strategies` — themes shape which Strategy families are viable at the sphere level, not just at the cycle level

## Examples (illustrative — not load-bearing for ship)

OPC § 13.3.1 typically distinguishes power-dynamics themes like:

- Agenda-control vs execution-discipline (the three-dimensional power frame; Lukes)
- Visible-vs-hidden authority structures
- Formal-vs-informal influence networks
- Centralized-vs-distributed decision rights
- Resource-dependence dynamics (Pfeffer)
- Symbolic-vs-material power
- Position-vs-personal power
- Legitimate-vs-coercive authority
- Disciplinary-vs-sovereign power (Foucault)
- Habitus-and-field dynamics (Bourdieu)

These are NOT canonical until populated from OPC source.

## Cross-references

- Family library: `../README.md`
- Template: `_TEMPLATE.md`
- Pattern Prototype: `_types/PLC_Pattern.md`
- OPC source section: `_frameworks/OPC-Assessment.md § 13.3.1`
- Worked example: OPC § 13.3.1 in `Spheres/Example-Sphere-Acme-Corp/OPC-Diagnostics/opc-2026-06-01.md` notes "agenda-control-vs-execution-discipline (Lukes' three-dimensional power frame)" as the active theme
