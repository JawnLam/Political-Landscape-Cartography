---
type: PLC_Sphere_Manifest
Item_ID: <sphere-slug>-manifest
title: "<Sphere Name> — Sphere Manifest"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere_Name: "<Sphere Name>"
plc_Sphere_Slug: <sphere-slug>
plc_Sphere_Description: "<One paragraph: organization + sector + scale + current political pressure>"
plc_Operator_Mode: consultant   # consultant | principal_self
plc_Engagement_Kind: campaign   # campaign | advisory | self_coaching | other
plc_Engagement_Status: pre_engagement   # pre_engagement | routine | close_out | closed
plc_Engagement_Horizon: "<e.g., '6 months', 'open-ended'>"
plc_Domain_Validity: in_scope   # in_scope | adjacent | out_of_scope
plc_Principals:
  - "[[principal-<slug>]]"
plc_Coprincipal_Conflict_Discipline: ""   # Required when len(plc_Principals) > 1
plc_Redaction_Default: <profile-name>
plc_Pre_Engagement_Status: complete   # complete | deferred | not_applicable
plc_Sphere_Opened_Date: <YYYY-MM-DD>
AI_Instructions: ""
---

# <Sphere Name>

## Charter
<One paragraph: what this sphere is for; why PLC is being applied to it.>

## Principals
- **<Principal Name> — <Role> (<tenure>).** Authority scope: <unilateral>. Cannot: <forbidden>.

## Engagement Scope
**Closes when:** <end-state criteria>. **Out of scope:** <explicit boundaries>.

## Operating Conventions
<Sphere-local overrides to default communication preferences. Pointer to `_USER.md` if one exists.>

## Cross-References
- `_sphere-state.md` — current state
- `_sphere-decisions.md` — append-only decisions log
- `Practitioner-Assessment.md` — § 16-17 (consultant mode only)
