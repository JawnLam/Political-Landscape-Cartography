---
Item_ID: plc-pattern-family-ethical-dilemmas
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Ethical Dilemmas — Family Overview"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
plc_Pattern_Family: ethical_dilemmas
plc_Pattern_Source_OPC_Section: "13.3.2"
plc_Shipped_Atom_Count: 10
AI_Instructions: ""
---

# Ethical Dilemmas — Family Overview

## OPC Source

OPC Assessment v3.0 § 13.3.2 — Ethical Dilemmas within the broader Dynamics section.

## What this family captures

Recurring ethical-tension structures that characterize political work. Unlike § 11 (Harm & Ethical Evaluation), which is a gate against specific tactical moves, § 13.3.2 ethical-dilemma themes characterize **structural tensions** that pervade an engagement and that ETHICAL-ACCOUNTING gates encounter cycle after cycle.

When an ethical-dilemma theme is active in a sphere, the ETHICAL-ACCOUNTING gate cannot resolve it through any single cycle's evaluation — the dilemma is durable. The operator's job is to recognize the structural tension and select tactics that minimize harm under the tension's constraints, not pretend the tension can be eliminated.

The Acme Corp worked example flags "legitimate-information-asymmetry vs deceptive-information-asymmetry boundary" as the active ethical-dilemma theme — the engagement uses information asymmetry (legitimate per Sam's authority), but the boundary between legitimate cadenced disclosure and deceptive withholding has to be evaluated at each gate.

## Shipped atom count

**10 atoms per D10** sourced from OPC § 13.3.2.

## How to populate

For each of the 10 ethical-dilemma themes in OPC § 13.3.2:

1. Copy `_TEMPLATE.md` to `Pattern-<dilemma-slug>.md`
2. Set `Title` to the dilemma name as defined in OPC
3. Populate `## Pattern Description` from OPC source
4. Populate `## Detection Signals` — when this dilemma is present in an engagement
5. Populate `## What Typically Drives It` — structural conditions producing the dilemma
6. Populate `### Operating Under This Dilemma` — guidance for minimizing harm rather than eliminating tension
7. Cross-reference to § 11 (Harm & Ethical Evaluation) which provides per-tactic gate evaluation against this dilemma's frame
8. Cite ethical-framework theorists OPC associates with each dilemma (consequentialist, deontological, virtue, care-ethics, justice-as-fairness lineages)

## Examples (illustrative — not load-bearing for ship)

OPC § 13.3.2 typically distinguishes ethical-dilemma themes like:

- Legitimate vs deceptive information asymmetry
- Persuasion vs manipulation boundary
- Loyalty (to principal) vs duty (to institution)
- Confidentiality vs transparency
- Short-term tactical gain vs long-term sphere ecosystem
- Individual benefit vs collective benefit
- Means-vs-ends evaluation
- Stakeholder primacy questions
- Reversibility-vs-irreversibility of moves
- Power-asymmetry exploitation boundary

These are NOT canonical until populated from OPC source.

## Cross-references

- Family library: `../README.md`
- Template: `_TEMPLATE.md`
- Pattern Prototype: `_types/PLC_Pattern.md`
- OPC source section: `_frameworks/OPC-Assessment.md § 13.3.2`
- Related OPC section: `_frameworks/OPC-Assessment.md § 11` (Harm & Ethical Evaluation gate — operates per-tactic; themes here operate at the engagement level)
- Worked example: OPC § 13.3.2 in `Spheres/Example-Sphere-Acme-Corp/OPC-Diagnostics/opc-2026-06-01.md` notes "legitimate-information-asymmetry vs deceptive-information-asymmetry boundary" as the active theme
