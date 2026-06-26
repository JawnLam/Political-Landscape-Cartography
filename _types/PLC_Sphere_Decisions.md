---
type: Prototype
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-sphere-decisions-prototype
title: "PLC_Sphere_Decisions — Prototype Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
prototype_namespace: plc
prototype_version: "1.0"
---

# PLC_Sphere_Decisions

## Purpose

Append-only log of consequential sphere-level decisions elevated from session work. The durable record of "why this sphere is shaped the way it is" — survives engagement length, principal turnover, and the AI's session memory loss.

Per D27 user pushback resolution: decisions in session logs alone risk getting lost after many sessions. This file elevates them to permanent reference.

## Cardinality and grain

- **One per sphere.**
- **Lives at sphere root**: `Spheres/<Sphere>/_sphere-decisions.md`

## Durability mode

**Mode A — Append-only.** New entries are added; existing entries are never edited, reordered, or deleted. The audit trail's value is its immutability.

If a prior decision is superseded, append a new entry citing the prior. Do not edit the original.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Sphere_Decisions` |
| `Item_ID` | string | `<sphere-slug>-decisions` |
| `Title` | string | `"<Sphere Name> — Sphere Decisions Log"` |
| `Date_Added` | ISO date | Sphere-open date |
| `Date_Modified` | ISO date | Date of most recent append |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Decision_Count` | integer | Total entries; never decreases |
| `AI_Instructions` | string | Default `""` |

## Required body sections

```markdown
# <Sphere Name> — Sphere Decisions Log

> Append-only. Never edit prior entries. To supersede a decision, append a new entry citing the prior.

## §<NNN> — <ISO date> — <One-line title>

**Decided:** <The decision in one sentence.>

**Why:** <One paragraph: the motivating context, constraint, or stakeholder ask.>

**Source:** <Session log filename and section, OR `_sphere-state.md` § ..., OR external reference.>

**Status:** active | superseded by §<NNN>

---

## §<NNN+1> — <ISO date> — <next entry>
...
```

## Elevation criterion

Not every session decision belongs here. The criterion (per D27, repeated in `06-STATE-PERSISTENCE.md`):

> *"Would a future operator — coming in cold to this sphere — need to know this to operate the sphere correctly?"*

Examples that **qualify**:

- Deciding the principal's authority threshold for unilateral action
- Deciding to bring in a co-principal (or close one out)
- Deciding to shift the engagement's ethical guardrails
- Deciding an actor is permanently out-of-scope for analysis
- Deciding to switch the redaction default
- Deciding the engagement's end-state criteria

Examples that **don't**:

- Which of two equivalent tactics to use in a single cycle (lives in the cycle log)
- Adjusting an Actor's perception based on this week's signals (lives in Actor file's perception history)
- Scheduling the next cycle (lives in working state)

## Relation slots

| Direction | Relation | Target Prototype | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 1 |
| Out (per entry) | `plc_Sourced_From` | PLC_Session OR `_sphere-state.md` | 1 per entry |
| Out (when superseded) | `plc_Superseded_By` | PLC_Sphere_Decisions entry | 0..1 per entry |

## Reciprocal-update discipline

- When a decision is elevated to this file, the corresponding bullet in `_sphere-state.md` § Decided is updated to match.
- When a decision is superseded, the new entry's frontmatter cites the old §; the old entry's `Status` is updated to `superseded by §<NNN>` — **this is the ONE exception to append-only**: status-flag flip on supersession. The decision *content* is never edited.
- When `plc_Decision_Count` increments, the manifest's `Date_Modified` is touched on the next session-end.

## Worked example

```markdown
---
type: PLC_Sphere_Decisions
timestamp: "2026-06-10T00:00:00Z"
Item_ID: acme-corp-decisions
title: "Acme Corp — Sphere Decisions Log"
Date_Added: 2026-04-22
Date_Modified: 2026-06-10
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Decision_Count: 4
AI_Instructions: ""
---

# Acme Corp — Sphere Decisions Log

> Append-only. Never edit prior entries. To supersede a decision, append a new entry citing the prior.

## §001 — 2026-04-22 — Engagement scope locked

**Decided:** Engagement closes when (a) board succession plan ratified with Sam's mandate preserved, OR (b) Sam exits the role. Family-personal dynamics beyond what shows up at the board are out of scope.

**Why:** Sam's stated reason for engagement is succession-period operating-mandate preservation. Family-personal scope expansion would change the engagement kind and the practitioner-assessment fit.

**Source:** Session 2026-04-22_000_SPHERE-OPEN.md § CQ3-CQ4 + § CQ7.

**Status:** active

---

## §002 — 2026-04-29 — Carol treated as `defensive`

**Decided:** Until further detection, treat Carol (CFO) as `defensive` posture toward the principal. Do not assume neutralizable in this engagement window without additional perception signal.

**Why:** Three cold-reading indicators present from § 13 review: budget-memo timing, finance-committee staffing, communication channel narrowing. Acting on `unaware` assumption would risk asymmetric exposure.

**Source:** Session 2026-04-29_001_OPC-DIAGNOSE.md § 13.1 + § 2.2.

**Status:** active

---

## §003 — 2026-05-15 — Sam's unilateral authority threshold raised

**Decided:** Capital allocation threshold for unilateral action raised from $2M to $5M.

**Why:** Board approved at 2026-05-15 meeting. Material change to principal authority scope — affects every subsequent cycle's "considered moves" set.

**Source:** Session 2026-05-15_004_ACTOR-UPDATE.md § Sam-funnel-refinement.

**Status:** active

---

## §004 — 2026-06-10 — Redaction default switched

**Decided:** EXPORT-SHAREABLE default switches from `internal-leadership-summary` to `external-board-summary` for the remainder of the engagement.

**Why:** External board reporting will be primary deliverable through Q4 succession-planning window. Reducing risk of accidental internal-only content leaking into external exports.

**Source:** Session 2026-06-10_006_RUN-CYCLE.md § post-cycle deliverable planning.

**Status:** active
```

## Anti-patterns

- Editing a prior decision's content because "the wording was unclear." Append a clarifying entry instead; never mutate.
- Treating every cycle's tactical pick as a sphere-level decision and elevating it here. Apply the criterion strictly.
- Forgetting to update `## Decided` in `_sphere-state.md` when appending here. Both update together.
- Flipping `Status: superseded` without an explicit superseding §NNN reference in the new entry.
- Letting `plc_Decision_Count` drift from the actual entry count. They must always match.
