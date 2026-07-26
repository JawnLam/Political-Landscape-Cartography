---
type: PLC_Sphere_Manifest
timestamp: "2026-06-10T00:00:00Z"
Item_ID: acme-corp-manifest
title: "Acme Corp — Sphere Manifest"
Date_Added: 2026-04-15
Date_Modified: 2026-06-10
Needs_Processing: false
plc_Sphere_Name: "Acme Corp"
plc_Sphere_Slug: acme-corp
plc_Sphere_Description: "Mid-market industrial supplier, ~2000 employees, family-board with professional CEO. Current political pressure: family board factionalizing around succession-planning cycle through 2026-Q4."
plc_Operator_Mode: consultant
plc_Engagement_Kind: campaign
plc_Engagement_Status: routine
plc_Engagement_Horizon: "9 months through 2026-Q4"
plc_Domain_Validity: in_scope
plc_Principals:
  - "[[principal-sam-ceo]]"
plc_Coprincipal_Conflict_Discipline: ""
plc_Redaction_Default: external-board-summary
plc_Pre_Engagement_Status: complete
plc_Sphere_Opened_Date: 2026-04-15
AI_Instructions: "FICTIONAL WORKED EXAMPLE (F4b quarantine, 05-WRITING-FOR-AI). Everything in this sphere is fabricated pedagogy. Copy its FORMATS (file structures, section shapes, notation patterns) freely; NEVER cite its content as facts, base rates, defaults, precedent, or priors in any live sphere. Its credences and estimates illustrate mechanics only. This sphere ships a SUBSET of its own narrative history — see the 'What ships here' section; a link to an artifact that is not on disk is a deliberate elision, not a broken volume."
---

# Acme Corp

> **Worked example sphere shipped with PLC v1.0.** This cartridge demonstrates the populated form of every Type and is referenced from the Type definitions in `_types/`. It also serves as the F-code regression canary per `_plc-engine/07-SHIPPING-CHECKLIST.md` § 7. The sphere is consultant-mode (the discipline floor); the principal is fictional; the engagement is illustrative.

## Charter
Help Sam (CEO) navigate the family-board succession politics through 2026 without losing operating mandate. PLC applied as the political-landscape backbone; ADAPT applied at the principal coaching layer. Engagement runs through 2026-Q4 with possible extension contingent on Q4 board action.

## Principals
- **Sam — CEO (4 years tenure).** Authority scope: full P&L; capital allocation up to $5M unilateral; board-relations lead; org-design within existing structure. Cannot unilaterally restructure the board; cannot touch family ownership structure; cannot bypass independent directors on audit.

## Engagement Scope
**Closes when:** (a) board succession plan ratified with Sam's operating mandate preserved (3-1 family voting bloc maintained), OR (b) Sam exits the role.

**Out of scope:** Family-personal succession dynamics that don't manifest at the board (this scope boundary surfaced in CQ7 at sphere bootstrap and is held throughout — see `_sphere-decisions.md` § 001).

## Operating Conventions
See `_USER.md` for any sphere-local register overrides. Defaults otherwise (peer / direct / minimal-hedging / no-filler / no-emojis). Consultant-mode adds standard §§ 16-17 quarterly refresh discipline.

## Cross-References
- `_sphere-state.md` — current state with OPC rollup
- `_sphere-decisions.md` — append-only sphere-level decisions log
- `Practitioner-Assessment.md` — § 16-17 outcomes from sphere-open
- `Principals/principal-sam-ceo.md` — Sam's funnel + authority + coaching themes
- Active campaign: `Campaigns/campaign-succession-q3.md`
- Latest OPC diagnostic: `OPC-Diagnostics/opc-2026-06-01.md`

## What ships here (and what is referenced but elided)

This example is a **teaching subset of a longer fictional engagement**, not a complete cartridge. The narrative runs from 2026-04 and refers to work that predates what is on disk. That is deliberate: shipping every session and cycle of a nine-month engagement would bury the mechanisms the example exists to demonstrate.

**On disk:** sessions `000`, `007`, `009`–`015`; cycles `0007`–`0010`; one OPC diagnostic (`opc-2026-06-01.md`); one Detection Record; one campaign; four actors; one principal.

**Referenced in prose but intentionally not shipped:** sessions `001`–`006` and `008` (the sphere's early diagnostic and actor-build sequence), cycles `0001`–`0006`, and the partial diagnostic `opc-2026-04-29-partial.md`. Their absence is why some wiki-links in this sphere do not resolve.

**What this means for an AI reading the sphere.** A dangling link here is not a defect to repair, and it is emphatically not an invitation to reconstruct the missing artifact — inventing `cycle-0003.md` to satisfy a link would be F2 (fabricated specificity) inside the volume's own regression canary, which is the worst place in the repository for it to happen. Read the elision as what it is: the engagement had a history; you are being shown the part that teaches.

The mechanisms the shipped subset does demonstrate end-to-end: a Detection Record with pre-registered predictions and a VoI stop; an augmented gate passing on collective sufficiency where no single resource suffices; a nested acquisition (gate fail → spawn → close-nested → resume → re-gate) with resource conservation visible; a non-destructive mid-cycle objective revision; projected and realized values coexisting through close; and a five-part quarterly audit reading the calibration off both.
