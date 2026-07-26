---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-principal-type
title: "PLC_Principal — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-07-24
Needs_Processing: false
type_namespace: plc
type_version: "1.2"
---

# PLC_Principal

## Purpose

The actor at the center of the sphere — whose Agenda the principal-funnel narrows and whose moves the cycle protocol orchestrates. In consultant mode, this is the client; in principal-self mode, this is the operator themselves.

PLC supports 1..N principals per sphere (D1). Each principal has their own Principal Item file.

## Cardinality and grain

- **1..N per sphere.**
- **Lives at**: `Spheres/<Sphere>/Principals/<Principal-Name-Or-Placeholder>.md`

## Durability mode

**Mode D — Append-friendly current+history.**

- **`## Current` block** — overwrite zone for current funnel + authority scope + mastery signals
- **`## Engagement History` block** — append-only chronological log of material role / scope shifts
- **`## Mastery History` block** — append-only chronological log of mastery-scale (`plc_Principal_Funnel_Sharpness`) changes

Per D27 + D28.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Principal` |
| `Item_ID` | string | `principal-<slug>` |
| `Title` | string | `"<Principal Name> — Principal"` (or `[PRINCIPAL]` placeholder) |
| `Date_Added` | ISO date | Date this Principal was added to the sphere |
| `Date_Modified` | ISO date | Most recent material update |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Principal_Name` | string | Name as used in writing (placeholder permitted) |
| `plc_Principal_Role` | string | Position/title in the sphere |
| `plc_Authority_Scope_Unilateral` | string | What the principal can decide alone |
| `plc_Authority_Scope_Coalition` | string | What requires alliance |
| `plc_Authority_Scope_Forbidden` | string | What the principal cannot touch |
| `plc_Current_Agenda` | string | One-paragraph current Agenda summary |
| `plc_Principal_Funnel_Sharpness` | integer | 0-5 mastery scale (per D25) |
| `plc_Funnel_Last_Refined_Date` | ISO date | Most recent funnel-refinement session |
| `plc_Engagement_Status` | enum | `active \| coaching_paused \| closed_out` (per principal, not per sphere) |
| `plc_Active_Campaigns` | list[link] | Campaigns this principal is currently driving |
| `AI_Instructions` | string | Default `""` |

### `plc_Principal_Funnel_Sharpness` levels (per D25)

| Level | Label | Meaning |
|-------|-------|---------|
| 0 | Unstated | No funnel articulated yet |
| 1 | Vague | High-level goal, no decision criteria |
| 2 | Drafted | Decision criteria proposed; not pressure-tested |
| 3 | Operational | Funnel survived 1+ cycles |
| 4 | Sharp | Operator can derive considered-move set directly from funnel |
| 5 | Deeply held | Funnel is the principal's working frame, not a coached scaffold |

## Required body sections

```markdown
# <Principal Name> — Principal

## Current

### Funnel
<The current Agenda narrowed into decision criteria. ADAPT-Loop "A" beat. Operator's working theory of what the principal is trying to accomplish and what counts as success.>

### Authority Scope
<Unilateral / coalition / forbidden — sourced from frontmatter, summarized prose.>

### Active Coaching Themes
<What the operator is currently working with the principal on. Mode-aware: in consultant mode, this is the coaching agenda; in principal-self mode, this is self-development focus.>

### Mastery Signals
<Evidence of the current `plc_Principal_Funnel_Sharpness` level. What earned this score; what would justify moving up.>

### Current Resource Holdings (v1.2+, optional)
<This is LSPI's R — the principal's resource MULTISET (quantities matter: two banked favors ≠ one). One line per holding, quantity FIRST and explicit — never "has favors," always "×2 banked favors (Robert, Elena)." Per resource: quantity, type (carrier), effect signature, durability, and any convertibility edges / gain-cycle positions. Protection note: which durable low-yield resources defend which fragile high-yield ones. Full discipline in § Resource-holdings discipline below.>
- ×<n> <carrier> — <specifics; whose, since when> · moves <cells> · <durable|fragile> · <as-of date, cycle ref>

## Engagement History
<Append-only. Material role / scope / status shifts. Dated.>
- <date>: <event>
...

## Mastery History
<Append-only. Funnel-sharpness changes with reason. Dated.>
- <date>: Sharpness <prev> → <new>. Reason: <brief>.
...

## Cross-References
- Sphere: <link>
- Active campaigns: <links>
- Most recent cycle: <link>
```

## Resource-holdings discipline (R) (v1.2+, optional)

`### Current Resource Holdings` is LSPI's **R** slot. Pre-1.2 Principal files carry no such section and stay valid; once it exists, it is auditable, and these are the rules an audit checks.

1. **Quantities are explicit.** R is a multiset, not a set. Every line carries a count (`×1`, `×2`, …). "Holds credibility with the board" is not an entry; "×2 unredeemed commitments (Robert, Elena)" is. Holding two units and spending one leaves one — set notation cannot say that, which is precisely why the multiset framing is load-bearing.
2. **Executions deduct exactly once.** When a cycle's ε fires, the resources in its θ are decremented once each, at execution, in the cycle that executed. Not at selection, not again at close. Decrement by writing the new count with the cycle reference — never by deleting the line unless the count reaches zero.
3. **Flowbacks append exactly once.** When a sub-cycle closes and flows back, its obtained resources are added once, tagged with the flowing-back cycle. A resource is never credited twice because it appears in both the sub-cycle's `Φ` and the parent's resumed gate — those are one event recorded from two sides.
4. **Mooted and abandoned cycles flow back nothing.** They produce no `Φ` and no `⟨flowback-recorded, E⟩`; R is unchanged. If a holdings line grew out of a mooted cycle, that is a bug.
5. **The quarterly conservation eyeball counts multiplicities (Theorem 13.4).** At QUARTERLY-AUDIT's belief-hygiene review, walk the quarter's cycles: every deduction has a matching execution, every addition a matching flowback, and the arithmetic runs **over counts, not over kinds**. "Credibility in, credibility out" is not conservation if two units went in and one came back.

**Pinning note — conservation of totals is not conservation of identity.** What flows back on a resume must be **the resource that failed the gate**. A sub-cycle spawned because the principal lacked `q` and returning some *other* resource of equal notional worth has not resolved the escalation: the parent's gate re-test reads the specific `q` it failed on, and `R-resume` will not fire without it. The audit checks the pin, not just the balance — match each flowback to the `⟨gate-fail, q⟩` that caused the spawn. (See `PLC_Cycle.md` § Capability gate and § LSPI Configuration.)

## Relation slots

| Direction | Relation | Target Type | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 1 |
| Out | `plc_Active_Campaigns` | PLC_Campaign | 0..N |
| In | `plc_Principal_Owner` (from Campaign) | PLC_Campaign | 0..N |
| In | `plc_Principal_Owner` (from Cycle) | PLC_Cycle | 0..N |

## Reciprocal-update discipline

- When `plc_Active_Campaigns` changes here, the Campaign file's `plc_Principal_Owner` is updated to match. Both directions enforced.
- When the Principal's `plc_Authority_Scope_Unilateral` changes (e.g., capital threshold raised — see Sphere_Decisions worked example §003), the corresponding sphere-level decision is appended to `_sphere-decisions.md`.
- When `plc_Principal_Funnel_Sharpness` changes, an entry is appended to `## Mastery History` AND the sphere state's `## Decided` is reviewed for any contingent positions.

## Worked example

```markdown
---
type: PLC_Principal
timestamp: "2026-06-10T00:00:00Z"
Item_ID: principal-sam-ceo
title: "Sam — Principal"
Date_Added: 2026-04-15
Date_Modified: 2026-06-10
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Principal_Name: "Sam"
plc_Principal_Role: "CEO, 4 years tenure"
plc_Authority_Scope_Unilateral: "Full P&L; capital allocation up to $5M; board-relations lead; org-design within existing structure"
plc_Authority_Scope_Coalition: "Capital allocation > $5M (board); board composition (board); succession planning (board + family)"
plc_Authority_Scope_Forbidden: "Unilateral board restructure; family ownership structure; bypass of independent directors on audit"
plc_Current_Agenda: "Through 2026-Q4: preserve operating mandate through succession-planning cycle. Specifically — keep the family voting bloc 3-1 in his favor and prevent Carol's shadow-CEO consolidation."
plc_Principal_Funnel_Sharpness: 4
plc_Funnel_Last_Refined_Date: 2026-06-10
plc_Engagement_Status: active
plc_Active_Campaigns:
  - "[[Campaign-Succession-Q3]]"
AI_Instructions: ""
---

# Sam — Principal

## Current

### Funnel
**Agenda:** Preserve operating mandate through succession-planning cycle (through 2026-Q4).

**Decision criteria** (sharpness 4 — Sam can derive considered-move set directly from these):
1. Does this move preserve or strengthen the 3-1 family voting bloc?
2. Does this move avoid handing Carol additional unilateral resource control?
3. Does this move maintain Sam's standing with the 3 independent directors?
4. Can this move be reversed if the political read turns out wrong?

Anything failing #1 or #2 is out. Anything passing all four is in.

### Authority Scope
- Unilateral: P&L, $5M capital, board-relations lead, org-design
- Coalition: capital > $5M, board composition, succession plan
- Forbidden: board restructure, family ownership, audit bypass

### Active Coaching Themes
- Detection discipline: Sam runs on relationship intuition; we're building structured perception-gap checks at every cycle close.
- Coalition asymmetry: Sam underweights Robert (board chair) as a swing — explicit coalition-mapping at Cycle close.

### Mastery Signals
Sharpness 4 earned 2026-06-10: Sam independently derived the considered-move set for Cycle-0008 before the AI surfaced one. Funnel is operational AND can drive move-generation. Sharpness 5 would require Sam using the funnel without scaffolding — currently he still works from the written criteria.

## Engagement History
- 2026-05-15: Unilateral capital threshold raised from $2M to $5M (board ratified). Authority scope updated.
- 2026-04-15: Engagement opened; principal added.

## Mastery History
- 2026-06-10: Sharpness 3 → 4. Reason: Cycle-0007 close — Sam derived considered moves before AI prompted.
- 2026-05-08: Sharpness 2 → 3. Reason: Funnel survived Cycle-0006 against Carol's budget-memo escalation.
- 2026-04-22: Sharpness 1 → 2. Reason: Initial funnel drafted from CQ3-CQ7 at sphere-open.
- 2026-04-15: Sharpness 0 (baseline at engagement start).

## Cross-References
- Sphere: [[acme-corp-manifest]]
- Active campaigns: [[Campaign-Succession-Q3]]
- Most recent cycle: [[Cycle-0008]]
```

## Anti-patterns

- Inferring `plc_Principal_Name` from any indirect signal (email handle, file path, git config). Always use the operator's explicit answer. Per P5 / F3.
- Letting `## Current ### Funnel` drift from the active coaching agenda. Refresh at the end of every cycle that affected the funnel.
- Editing `## Engagement History` or `## Mastery History` entries. Both are append-only.
- Inflating `plc_Principal_Funnel_Sharpness` without evidence. Each level has explicit mastery signals; the History block records the earning event.
- Forgetting reciprocal updates to Campaign files when `plc_Active_Campaigns` changes. The graph corruption is silent until QUARTERLY-AUDIT surfaces it.
