---
Item_Prototype: Prototype
Item_ID: plc-actor-prototype
Title: "PLC_Actor — Prototype Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
prototype_namespace: plc
prototype_version: "1.0"
---

# PLC_Actor

## Purpose

A person (or institutional role) in the sphere's political landscape whose disposition materially affects what the principal can accomplish. The central strategic Prototype — the cast that every cycle reasons against. Per D6, vocabulary is "Actor" (not "cast member" or "stakeholder"); D26 forbids cross-sphere sharing (same human at two organizations = two Actor files).

## Cardinality and grain

- **N per sphere.** Typically 5-30 actively-tracked.
- **Lives at**: `Spheres/<Sphere>/Actors/<Actor-Name>.md`

## Durability mode

**Mode D — Append-friendly current+history.**

- **`## Current` block** — overwrite zone for profile, current perception, current resource set, current network position
- **`## Perception History` block** — append-only chronological log of perception-toward-principal shifts
- **`## Resource History` block** — append-only log of resource gains/losses

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `Item_Prototype` | string | Must be `PLC_Actor` |
| `Item_ID` | string | `actor-<slug>` |
| `Title` | string | `"<Actor Name> — <Role>"` (or `[ACTOR-N]` placeholder) |
| `Date_Added` | ISO date | Date added to sphere |
| `Date_Modified` | ISO date | Most recent material update |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Actor_Name` | string | Name as used in writing (placeholder permitted) |
| `plc_Actor_Role` | string | Position/title in the sphere |
| `plc_Hierarchical_Position` | enum | `executive \| director \| manager \| ic \| board \| external \| other` |
| `plc_Current_Perception_Toward_Principal` | enum | `allied \| neutral \| ambivalent \| defensive \| opposed \| unknown` |
| `plc_Network_Distance_From_Principal` | integer | Hop count; 1 = direct peer / report / boss; 2 = one degree of separation; etc. |
| `plc_Resources_Held` | list[enum] | Subset of `money \| hard_assets \| credibility \| attributes \| legitimacy \| information \| access \| title \| tribe` (dissertation 9-type taxonomy) |
| `plc_Coalitions` | list[link] | `[[<Actor-Name>]]` per allied actor |
| `plc_Opposed_By` | list[link] | `[[<Actor-Name>]]` per opposing actor (reciprocal of opposition) |
| `plc_Actor_Completeness` | integer | 0-5 mastery scale (per D25) |
| `plc_Last_Updated_Cycle` | link | Most recent Cycle that touched this actor |
| `AI_Instructions` | string | Default `""` |

### `plc_Actor_Completeness` levels (per D25)

| Level | Label | Meaning |
|-------|-------|---------|
| 0 | Stub | Name + role only |
| 1 | Sketched | Stub + apparent disposition |
| 2 | Drafted | Sketched + resources held + 1+ coalition mapped |
| 3 | Detailed | Drafted + perception history + network position |
| 4 | Comprehensive | Detailed + multi-cycle resource trajectory + opposition mapping |
| 5 | Deeply known | Comprehensive + behavioral patterns + predictive read survives 3+ cycles |

## Required body sections

```markdown
# <Actor Name> — <Role>

## Current

### Profile
<One paragraph: position, tenure, professional context, anything material to political reasoning.>

### Perception Toward Principal
<Current perception with as-of date. Evidence summary (1-3 cold-reading indicators).>

### Resources Held
<Subset of 9-type taxonomy with specifics. Material amounts where relevant.>

### Network Position
<Coalitions / opposition / brokering relationships. Distance from principal.>

### Behavioral Notes
<Observed patterns. Communication style. What triggers shifts.>

## Perception History
<Append-only. Date prefix. Brief reason + cite.>
- <date>: <prev> → <new>. Reason: <brief>. (Source: <cycle/session>)
...

## Resource History
<Append-only. Date prefix. Gain/loss + reason + cite.>
- <date>: <gain|loss>: <resource type + specifics>. (Source: <cycle/session>)
...

## Cross-References
- Sphere: <link>
- Most recent cycle: <link>
- Coalitions: <links>
- Opposition: <links>
```

## Relation slots

| Direction | Relation | Target Prototype | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 1 |
| Out | `plc_Coalitions` | PLC_Actor | 0..N (symmetric) |
| Out | `plc_Opposed_By` | PLC_Actor | 0..N (symmetric inverse) |
| Out | `plc_Last_Updated_Cycle` | PLC_Cycle | 0..1 |
| In | `plc_Actor_Touched` (from Cycle) | PLC_Cycle | 0..N |
| In | `plc_Member_Of` (from Campaign) | PLC_Campaign | 0..N |
| In | `plc_Holds_Resource` (graph) | PLC_Resource (implicit) | N |

## Reciprocal-update discipline

- `plc_Coalitions` is symmetric: A → B requires B → A. F5 audit catches asymmetries.
- `plc_Opposed_By` is inversely symmetric: A.opposed-by B requires B's `plc_Opposed_By` ⊇ {A}.
- When a Cycle log references this Actor in `plc_Engaged_Moves` or perception-shift detection, this file's `plc_Last_Updated_Cycle` and history blocks update.
- When `plc_Current_Perception_Toward_Principal` changes, append to `## Perception History` and surface to the latest OPC diagnostic for cross-check.

## Worked example

```markdown
---
Item_Prototype: PLC_Actor
Item_ID: actor-carol-cfo
Title: "Carol Reyes — CFO"
Date_Added: 2026-04-22
Date_Modified: 2026-06-13
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Actor_Name: "Carol Reyes"
plc_Actor_Role: "CFO"
plc_Hierarchical_Position: executive
plc_Current_Perception_Toward_Principal: defensive
plc_Network_Distance_From_Principal: 1
plc_Resources_Held: [money, information, legitimacy, access]
plc_Coalitions:
  - "[[actor-david-coo]]"
plc_Opposed_By:
  - "[[principal-sam-ceo]]"
plc_Actor_Completeness: 3
plc_Last_Updated_Cycle: "[[Cycle-0008]]"
AI_Instructions: ""
---

# Carol Reyes — CFO

## Current

### Profile
CFO, 6 years tenure, joined under prior CEO. Background public-company controller. Reports to Sam but has independent reporting line to audit committee. Reputation: rigorous, risk-averse, politically careful.

### Perception Toward Principal
**Defensive** since 2026-06-10. Indicators:
1. Budget memo timing (delivered Friday EOD before quarterly board meeting — pressure tactic)
2. Finance-committee staffing (replaced Sam's ally with own deputy)
3. Communication channel narrowing (1:1s replaced with email-only)

Three of three cold-reading indicators present.

### Resources Held
- **Money:** Budget authority over OpEx + capital projects (since 2026-05-15)
- **Information:** Audit committee independent reporting line; sees financial signal before Sam does
- **Legitimacy:** Finance committee chair; quoted in industry press
- **Access:** Family-board direct line (one independent director is former colleague)

### Network Position
- **Coalitioned with:** David (COO) — aligned on cost-discipline platform
- **Opposed by:** Sam (principal); 1-hop direct opposition
- **Brokers between:** Independent directors and family voting bloc

### Behavioral Notes
Acts on data, not relationships. Will shift if shown asymmetric financial risk in her current posture. Will not respond to relationship-rebuilding overtures alone.

## Perception History
- 2026-06-13: Confirmed `defensive` after Cycle-0008 cold-reading (3/3 indicators present)
- 2026-06-10: Shifted `unaware` → `defensive` per budget memo episode. (Source: Cycle-0007)
- 2026-04-22: Baseline at sphere-open — `unaware`

## Resource History
- 2026-05-15: Gained budget authority over capital projects (org restructure)
- 2026-04-22: Baseline — finance committee chair, OpEx budget authority

## Cross-References
- Sphere: [[acme-corp-manifest]]
- Most recent cycle: [[Cycle-0008]]
- Coalitions: [[actor-david-coo]]
- Opposition: [[principal-sam-ceo]]
```

## Anti-patterns

- Inferring `plc_Actor_Name` from email handles, file paths, or any indirect signal. Use the operator's explicit answer. Per P5 / F3.
- Letting `plc_Current_Perception_Toward_Principal` drift from `## Perception History` — the current and the latest history entry must match.
- Adding a coalition reference without the reciprocal update on the partner Actor file. Symmetric relations require both-sides edits.
- Inflating `plc_Actor_Completeness` without the corresponding evidence. Each level has explicit criteria; over-claiming hides intelligence gaps.
- Reusing an Actor file across spheres. Same human at two organizations = two Actor files (D26).
