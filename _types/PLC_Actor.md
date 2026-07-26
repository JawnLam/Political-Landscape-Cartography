---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-actor-type
title: "PLC_Actor — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-07-24
Needs_Processing: false
type_namespace: plc
type_version: "1.2"
---

# PLC_Actor

## Purpose

A person (or institutional role) in the sphere's political landscape whose disposition materially affects what the principal can accomplish. The central strategic Type — the cast that every cycle reasons against. Per D6, vocabulary is "Actor" (not "cast member" or "stakeholder"); D26 forbids cross-sphere sharing (same human at two organizations = two Actor files).

## Cardinality and grain

- **N per sphere.** Typically 5-30 actively-tracked.
- **Lives at**: `Spheres/<Sphere>/Actors/actor-<slug>.md` — **one flat file per Actor.** This is the default and the only layout the shipped example sphere uses.

### Layout: flat by default; the per-principal overlay is optional

The flat file above holds everything: `## Current`, `## Perception History`, `## Resource History`. Unless the sphere needs the overlay below, there is exactly one file per Actor and no directory.

The alternative — a directory per Actor holding `<slug>/_baseline.md` plus one `_view-<principal>.md` per principal — is an **optional multi-principal overlay pattern**, not the default. Adopt it only when a single sphere carries several principals whose reads of the same Actor genuinely diverge and must be kept separately auditable (typically consultant mode). It is not exercised in the shipped example sphere; a single-principal sphere that splits an Actor into baseline + one view has added a directory and gained nothing.

When the overlay is in use: the `_baseline.md` holds the principal-independent record (profile, resources, network position, and their histories) and each `_view-<principal>.md` holds only that principal's relationship status, debt ledger, and perception-gap history. Both halves are Mode D and both obey the section discipline in `_plc-engine/04-SCHEMA.md` § *Section discipline* — `## Current ...` overwrites, `## ... History` appends. Migrating flat → overlay is a split, never a copy: no fact should end up asserted in two files.

## Durability mode

**Mode D — Append-friendly current+history.**

- **`## Current` block** — overwrite zone for profile, current perception, current resource set, current network position
- **`## Perception History` block** — append-only chronological log of perception-toward-principal shifts
- **`## Resource History` block** — append-only log of resource gains/losses

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Actor` |
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
| `plc_Resources_Held` | list[enum] | Subset of `money \| hard_assets \| credibility \| attributes \| legitimacy \| information \| access \| title \| tribe` (dissertation 9-type taxonomy) `\| other` (v1.2+) — `other` REQUIRES a note in `### Resources Held` naming the actual carrier |
| `plc_Coalitions` | list[link] | `[[<Actor-Name>]]` per allied actor |
| `plc_Opposed_By` | list[link] | `[[<Actor-Name>]]` per opposing actor (reciprocal of opposition) |
| `plc_Actor_Completeness` | integer | 0-5 mastery scale (per D25) |
| `plc_Last_Updated_Cycle` | link | Most recent Cycle that touched this actor |
| `AI_Instructions` | string | Default `""` |

### Optional LSPI fields (v1.2+; per substrate authority 5)

| Field | Type | Notes |
|-------|------|-------|
| `plc_Estimated_By` | list[link] | `[[detection-<slug>]]` records targeting this actor (reciprocal: **estimates / estimated-by**) |
| `plc_Depth_Estimate` | string | Current signaling-depth read (ℓ̂_T + credence + as-of date); full trail in the Detection Record |

Note on `plc_Resources_Held`: the nine types are a **non-exhaustive basis of carriers for elicitation** — the primary definition of a resource is intensional (a costly, target-conditional capacity to shift a decision-matrix cell; see `08-ESTIMATION.md`). The body's `### Resources Held` records per-resource effect signatures and durability.

**Why `other` exists (v1.2+).** A closed nine-value enum silently contradicts the intensional definition: a genuine resource that is not one of the nine — it costs something, it is target-conditional, it moves a matrix cell — would have nowhere to live, and the elicitation would quietly drop it. `other` is that home. It is **not** a shrug: every `other` entry MUST be accompanied by a `### Resources Held` line naming the actual carrier in the operator's own words, alongside its effect signature and durability like any other resource. Recurring `other` carriers are a QUARTERLY-AUDIT signal — either the sphere has a carrier the basis misses, or the entry belongs under one of the nine after all.

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
<Subset of 9-type taxonomy with specifics — plus any `other` carrier, which MUST be named here (v1.2+). Material amounts where relevant. Per resource (v1.2+, optional): effect signature — which matrix cells it can move ({P/b, P/c, Adv/b, Adv/c}), sign, target-conditionality note, rough cost — and durability (durable vs fragile).>

### Convertibility Edges (v1.2+, optional)
<Conversion paths this actor's resources participate in: r₁ ⇝ r₂, edge type (transfer / transform / earn-sanction / non-transferable), rough sphere-indexed rate. Note any gain-cycle (rate-product > 1 loop) — that's a compounding position — and what protects it (durable low-yield spent defending fragile high-yield).>

### Estimated Matrix Summary (v1.2+, optional)
<Prose: current best read of how this actor loads keep-vs-relinquish on live questions; margin direction. Pointer to [[detection-<slug>]] for the full differential and probe trail. This is a summary, not the record.>

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

| Direction | Relation | Target Type | Cardinality |
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
type: PLC_Actor
timestamp: "2026-06-13T00:00:00Z"
Item_ID: actor-carol-cfo
title: "Carol Reyes — CFO"
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
