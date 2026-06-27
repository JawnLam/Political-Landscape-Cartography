---
Item_ID: plc-pattern-family-stakeholder-archetypes
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Stakeholder Archetypes — Family Overview"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
plc_Pattern_Family: stakeholder_archetypes
plc_Pattern_Source_OPC_Section: "2.2.1"
AI_Instructions: ""
---

# Stakeholder Archetypes — Family Overview

## OPC Source

OPC Assessment v3.0 § 2.2.1 — Stakeholder Archetypes within the broader Stakeholders & Actors section.

## What this family captures

Recurring archetypal positions stakeholders occupy in organizational political landscapes. Unlike change-initiator-postures (§ 13.1.1) or opposition-postures (§ 13.1.2), which characterize active disposition, stakeholder archetypes characterize **structural role-positions** that exist regardless of whether the stakeholder is actively engaged in political work.

An actor may simultaneously occupy a stakeholder archetype (e.g., "audit-committee gatekeeper") AND hold a posture (e.g., "earned-mandate change-initiator"). The archetype is durable; the posture is engagement-specific.

## Shipped atom count

Per OPC § 2.2.1 source. (Operator populates at SHIP-PREP from OPC source materials.)

## How to populate

For each archetype in OPC § 2.2.1:

1. Copy `_TEMPLATE.md` to `Pattern-<archetype-slug>.md`
2. Set `Title` to the archetype name as defined in OPC
3. Populate `## Pattern Description` from the OPC source
4. Populate `## Detection Signals` with the 3-5 cold-reading indicators OPC describes
5. Populate `## What Typically Drives It` with the OPC contextual description
6. For stakeholder archetypes, `## Typical Lifecycle` may not apply (archetypes are durable; not lifecycle-bounded) — omit or note "Not lifecycle-bounded; archetype is structural"
7. Populate `### Recommended Strategies (against)` and `### Recommended Strategies (alignment)` from OPC's strategic-response framing
8. Set `plc_Confidence_Level: seeded`
9. Leave `plc_Evidence_Cycles` and `plc_Evidence_Diagnostics` empty (these accumulate during engagements)

## Examples (illustrative — not load-bearing for ship)

OPC § 2.2.1 typically distinguishes archetypes like:

- Decision-rights holders within formal authority structures
- Gatekeepers controlling information flow
- Coalition brokers operating across factions
- Audience-of-confidence members shaping perception
- Resource controllers within specific functional domains
- (etc. — refer to OPC source for the canonical inventory)

These archetypes are NOT yet drafted as `Pattern-<slug>.md` files in this folder; populated at SHIP-PREP per the operator's OPC source.

## Cross-references

- Family library: `../README.md`
- Template: `_TEMPLATE.md`
- Pattern Type: `_types/PLC_Pattern.md`
- OPC source section: `_frameworks/OPC-Assessment.md § 2.2.1`
