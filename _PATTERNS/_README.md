---
Item_ID: plc-patterns-readme
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "PLC Pattern Library — README"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
AI_Instructions: ""
---

# PLC Pattern Library

> **Six shipped pattern families seeded from OPC Assessment v3.0 sections per D10.** Each family is a folder; each pattern atom inside a family is a `PLC_Pattern` Item with `plc_Pattern_Scope: shipped_seed`. Operators extend the library during engagements by adding sphere-specific patterns (`plc_Pattern_Scope: sphere_specific`) in their own `Spheres/<Sphere>/Patterns/` folder, OR by adding OV-wide operator-extended patterns (`plc_Pattern_Scope: ov_wide_operator_extended`) here in `_PATTERNS/` when a pattern has been confirmed across 3+ engagements.

## The six families

| Family | OPC source | Shipped atom count | Folder |
|--------|------------|--------------------|--------|
| Stakeholder archetypes | § 2.2.1 | (per OPC) | `stakeholder-archetypes/` |
| Change-initiator postures | § 13.1.1 | 10 | `change-initiator-postures/` |
| Opposition postures | § 13.1.2 | 10 | `opposition-postures/` |
| Arc dynamics | § 13.2 | 20 | `arc-dynamics/` |
| Power-dynamics themes | § 13.3.1 | 10 | `power-dynamics-themes/` |
| Ethical-dilemmas themes | § 13.3.2 | 10 | `ethical-dilemmas/` |

The families are NOT orthogonal — a single political situation often manifests multiple patterns simultaneously (e.g., a "shadow-CEO consolidation" opposition posture inside a "succession-pressure-loop" arc dynamic with "agenda-control-vs-execution" as the power-dynamics theme). Operators identify which patterns are active for a sphere via OPC § 13 walkthrough during diagnostics.

## File structure

Each family folder contains:

- `_family-overview.md` — explains the family + lists the shipped atoms expected at full population
- `_TEMPLATE.md` — blank PLC_Pattern scaffold demonstrating the expected pattern atom shape
- `Pattern-<slug>.md` — one file per shipped pattern atom

## Ship-time population status (as of PLC v1.0.0 draft)

**Substrate-pending.** The shipped pattern atom files have not been drafted at ARTIFACT-DRAFT. Each pattern atom requires content sourced from the operator's OPC Assessment v3.0 source materials (the operator's proprietary diagnostic instrument — not on disk during ARTIFACT-DRAFT). At SHIP-PREP, the operator populates each family's `Pattern-<slug>.md` files from the corresponding OPC source section.

The `_family-overview.md` and `_TEMPLATE.md` files in each family ARE shipped at v1.0.0 and provide the structural scaffold operators populate against.

## How to use shipped patterns

During an active engagement:

1. **OPC diagnostic** (`OPC-DIAGNOSE` activity) walks the relevant § 13 subsection; if any pattern atom matches the sphere's current state, surface it
2. The cycle log references the pattern by `[[Pattern-<slug>]]` link
3. The pattern's `## Evidence History` accumulates each cycle's observation per the Mode D append-only history discipline
4. Cross-engagement: if the same pattern surfaces in 3+ engagements, consider promoting to `ov_wide_operator_extended`

## How to extend the library

For sphere-specific patterns surfaced during a single engagement:

- Create `Spheres/<Sphere>/Patterns/Pattern-<slug>.md` with `plc_Pattern_Scope: sphere_specific`
- Set `plc_Pattern_Family` to one of the 6 enum values matching the best-fit family
- Accumulate evidence per Mode D discipline

For OV-wide operator-extended patterns (3+ engagements confirmed):

- Create `_PATTERNS/<family>/Pattern-<slug>.md` with `plc_Pattern_Scope: ov_wide_operator_extended`
- Document the cross-engagement evidence in `## Evidence History`
- Propose for inclusion in next minor version bump via `CONTRIBUTING.md`'s framework-extension path

## Cross-references

- Pattern Prototype definition: `_types/PLC_Pattern.md`
- Pattern Template: `_plc-engine/_templates/PLC_Pattern_TEMPLATE.md`
- D10 lock decision: `_design-decisions.md` § D10
- OPC Assessment v3.0 (canonical source): `_frameworks/OPC-Assessment.md`
