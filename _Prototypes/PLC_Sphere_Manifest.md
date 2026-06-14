---
Item_Prototype: Prototype
Item_ID: plc-sphere-manifest-prototype
Title: "PLC_Sphere_Manifest — Prototype Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
prototype_namespace: plc
prototype_version: "1.0"
---

# PLC_Sphere_Manifest

## Purpose

The identity card and charter of a sphere (one political landscape, typically one organization). Created at sphere-open; rarely changes mid-engagement. Operator's first read when context-switching between spheres.

## Cardinality and grain

- **One per sphere.** A PLC cartridge has exactly one `_sphere-manifest.md`.
- **Lives at sphere root**: `Spheres/<Sphere>/_sphere-manifest.md`

## Durability mode

**Mode C — Current overwrite.** Whole file replaced as state changes; no history kept in-file. State history lives in `_sphere-state.md`. Manifest changes are rare and structural (e.g., sphere renamed, principal swapped, mode flipped).

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `Item_Prototype` | string | Must be `PLC_Sphere_Manifest` |
| `Item_ID` | string | `<sphere-slug>-manifest` (kebab-case) |
| `Title` | string | `"<Sphere Name> — Sphere Manifest"` |
| `Date_Added` | ISO date | Sphere-open date |
| `Date_Modified` | ISO date | Most recent material change |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere_Name` | string | The sphere's canonical name (typically organization name) |
| `plc_Sphere_Slug` | string | kebab-case identifier used in file paths and IDs |
| `plc_Sphere_Description` | string | One-paragraph description of what the sphere is |
| `plc_Operator_Mode` | enum | `consultant \| principal_self` (per D3) |
| `plc_Engagement_Kind` | enum | `campaign \| advisory \| self_coaching \| other` |
| `plc_Engagement_Status` | enum | `pre_engagement \| routine \| close_out \| closed` (per D22) |
| `plc_Engagement_Horizon` | string | Free-text time horizon (e.g., "6 months", "open-ended") |
| `plc_Domain_Validity` | enum | `in_scope \| adjacent \| out_of_scope` (per D5) |
| `plc_Principals` | list[link] | `[[Principal-Name]]` per principal; supports 1..N |
| `plc_Coprincipal_Conflict_Discipline` | string | How conflicting principal agendas are handled; required when `len(plc_Principals) > 1` |
| `plc_Redaction_Default` | string | Default EXPORT-SHAREABLE redaction profile name |
| `plc_Pre_Engagement_Status` | enum | `complete \| deferred \| not_applicable` (deferred only valid for short window; per D11 consultant mode) |
| `plc_Sphere_Opened_Date` | ISO date | Date of bootstrap session |
| `AI_Instructions` | string | Default `""` per Convention 2 |

## Body sections

```markdown
# <Sphere Name>

## Charter
<One paragraph: what this sphere is for, why PLC is being applied to it.>

## Principals
<List of principals with role + authority scope. One bullet per principal pointing to the Principal Item file.>

## Engagement Scope
<End-state criteria; what closes this engagement; what's explicitly out of scope.>

## Operating Conventions
<Sphere-local overrides to default communication preferences. Points to `_USER.md` if one exists.>

## Cross-References
<Pointers to `_sphere-state.md`, `_sphere-decisions.md`, and any sphere-local frameworks.>
```

## Relation slots

| Direction | Relation | Target Prototype | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Principals` | PLC_Principal | 1..N |
| Out | `plc_Active_Campaigns` | PLC_Campaign | 0..N (rollup of currently-active campaigns) |
| In (implicit) | `plc_Sphere` from every other Prototype in the sphere | All | N |

## Reciprocal-update discipline

- When `plc_Principals` is edited, every referenced Principal file must have its `plc_Sphere` pointer updated.
- When `plc_Active_Campaigns` shifts, every Campaign's `plc_Lifecycle_Stage` must align.

## Worked example

```markdown
---
Item_Prototype: PLC_Sphere_Manifest
Item_ID: acme-corp-manifest
Title: "Acme Corp — Sphere Manifest"
Date_Added: 2026-04-15
Date_Modified: 2026-06-10
Needs_Processing: false
plc_Sphere_Name: "Acme Corp"
plc_Sphere_Slug: acme-corp
plc_Sphere_Description: "Mid-market industrial supplier, ~2000 employees, family-board with professional CEO. Current political pressure: family board factionalizing around succession."
plc_Operator_Mode: consultant
plc_Engagement_Kind: campaign
plc_Engagement_Status: routine
plc_Engagement_Horizon: "9 months through 2026-Q4"
plc_Domain_Validity: in_scope
plc_Principals:
  - "[[Principal-Sam-CEO]]"
plc_Coprincipal_Conflict_Discipline: ""
plc_Redaction_Default: external-board-summary
plc_Pre_Engagement_Status: complete
plc_Sphere_Opened_Date: 2026-04-15
AI_Instructions: ""
---

# Acme Corp

## Charter
Help Sam (CEO) navigate the family-board succession politics through 2026 without losing operating mandate. PLC applied as the political-landscape backbone; ADAPT applied at the principal coaching layer.

## Principals
- **Sam — CEO (4 years tenure).** Authority scope: full P&L, capital allocation up to $5M unilateral, board-relations leads. Cannot unilaterally restructure the board.

## Engagement Scope
**Closes when:** (a) board succession plan ratified with Sam's mandate preserved, OR (b) Sam exits the role. **Out of scope:** family-personal dynamics beyond what shows up at the board.

## Operating Conventions
See `_USER.md` for register overrides. Defaults otherwise.

## Cross-References
- `_sphere-state.md` — current state
- `_sphere-decisions.md` — append-only decisions log
- `Practitioner-Assessment.md` — § 16-17 from sphere-open
```

## Anti-patterns

- Storing state history in the manifest. State history lives in `_sphere-state.md` § State History.
- Inferring `plc_Sphere_Name` from the folder name. Always confirm with the operator at CQ1.
- Leaving `plc_Coprincipal_Conflict_Discipline` empty when multiple principals are declared.
