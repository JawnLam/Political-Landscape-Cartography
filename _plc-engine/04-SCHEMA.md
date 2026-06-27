---
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-engine-04-schema
title: "PLC Engine — 04 Schema"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
doc_type: engine
role: schema-reference
scope: subject-agnostic-within-PLC
updated: 2026-06-13
---

# 04 — SCHEMA

> **The structural contract every Item in PLC conforms to. 16 first-class Types + 12 relation families + state-persistence summary + reference-system specifications.**

## The 16 first-class Types

| # | Type | Cardinality | Grain | Lives at |
|---|---|---|---|---|
| 1 | `PLC_Sphere_Manifest` | 1 per sphere | sphere-identity | `<Sphere>/_sphere-manifest.md` |
| 2 | `PLC_Sphere_State` | 1 per sphere | sphere-state-rollup | `<Sphere>/_sphere-state.md` |
| 3 | `PLC_Sphere_Decisions` | 1 per sphere | sphere-decisions-log | `<Sphere>/_sphere-decisions.md` |
| 4 | `PLC_Principal` | 1..N per sphere | protagonist | `<Sphere>/_PRINCIPALS/<name>.md` |
| 5 | `PLC_Actor` | many per sphere | long-lived dossier | `<Sphere>/Actors/<slug>/_baseline.md` + `_view-<principal>.md` |
| 6 | `PLC_Campaign` | many per sphere | strategic arc | `<Sphere>/Campaigns/<slug>.md` |
| 7 | `PLC_Cycle` | many per sphere | operational artifact | `<Sphere>/Cycles/<YYYY-MM-DD>_<NNN>_<slug>.md` |
| 8 | `PLC_Session` | many per sphere | history | `<Sphere>/Sessions/<YYYY-MM-DD>_<NNN>_<activity>.md` |
| 9 | `PLC_OPC_Diagnostic` | many per sphere | cartography output | `<Sphere>/Diagnostics/{opc\|practitioner-self-assessment\|engagement-politics}-<YYYY-MM-DD>.md` |
| 10 | `PLC_Engagement_Retrospective` | 1 per engagement (multiple per revived sphere) | engagement deliverable | `<Sphere>/Diagnostics/engagement-retrospective-<YYYY-MM-DD>.md` |
| 11 | `PLC_Move` | ~100 + operator-extensible | smallest tactical unit | `_frameworks/dissertation-table-3/<NNN>-<slug>.md` |
| 12 | `PLC_Tactic` | 782 (canonical) | composed tactical pattern | `_frameworks/political-warfare-catalogue/tactics/<NNNN>-<slug>.md` |
| 13 | `PLC_Strategy` | 16 (closed) | lever-combination meta-pattern | `_frameworks/political-warfare-catalogue/by-strategy/<NN>-<slug>.md` |
| 14 | `PLC_Cluster` | 84 (canonical) | thematic family of tactics | `_frameworks/political-warfare-catalogue/by-cluster/<CNN>-<slug>.md` |
| 15 | `PLC_Theorist` | 50 (canonical) + operator-extensible | intellectual lineage | `_frameworks/political-warfare-catalogue/by-theorist/<name>.md` |
| 16 | `PLC_Pattern` | 60+ (from OPC §§ 13 + 2.2) + operator-extensible | situational archetype | `_PATTERNS/<name>.md` (OV-root canonical) + `<Sphere>/_PATTERNS/<name>.md` (sphere-extensible) |

Types 1-10 are *sphere-content* (live inside operator-extended sphere cartridges). Types 11-16 are *OV-content* (live at OV root; shipped canonical reference).

### Required Universal Core fields (per Convention 1)

Every Item carries six universal fields plus its specific keys:

```yaml
---
Item_ID: <slug-or-uuid>
type: PLC_<TypeName>
title: "<Human-readable title>"
Date_Added: YYYY-MM-DD
Date_Modified: YYYY-MM-DD
Needs_Processing: false
# PLC-specific fields below
---
```

Plus `AI_Instructions: ""` per OVE_OV_Manifest pattern.

### Per-Type required body sections

| Type | Required body sections |
|---|---|
| `PLC_Sphere_Manifest` | Sphere identity; Domain validity; Operator mode; Principals declared; Engagement metadata; Sphere-close criteria; Initial cast inventory |
| `PLC_Sphere_State` | `## Decided` rollup; `## OPC Current Summary`; `## Open Threads`; `## Recent Sessions`; `## Active Campaigns`; `## Engagement State` |
| `PLC_Sphere_Decisions` | Append-only decision log entries (each: Decided / Alternatives / Rationale / Implications / Session) |
| `PLC_Principal` | `## Current Funnel`; `## Current Resource State`; `## Current Observation Pattern`; `## Eight Benefits History`; `## Resource Ledger History`; `## Cycle References`; `## Perception Gap History (vs Self)` |
| `PLC_Actor` (baseline) | `## Current Funnel`; `## Current Resource State`; `## Current Observation Pattern`; `## Inferred Theorist Frame`; `## Tagged Patterns`; `## Perception Gap History`; `## Multi-Cycle History`; `## Provenance` |
| `PLC_Actor` (overlay `_view-<principal>.md`) | `## Current Relationship Status`; `## Current Debt Ledger`; `## Perception Gap History (this principal's view)`; `## Cycle References`; `## Provenance` |
| `PLC_Campaign` | `## Root Interest`; `## Sub-Interest Tree`; `## Owning Principals`; `## Cycle References`; `## Lifecycle History` |
| `PLC_Cycle` | body sections corresponding to PLC's RUN-CYCLE protocol output (Agenda / Landscape Assessment / OPC Self-Diagnosis / Principal Funnel / ALTERNATIVES-AUDIT / ETHICAL-ACCOUNTING / Considered Moves / Selected Moves / Engaged Moves / Phase Log / Refinement / Lessons); the 14 dissertation constituents are tracked via frontmatter fields; `## Alternatives Audit`; `## Ethical Accounting`; `## Slash Constituents` reference |
| `PLC_Session` | `## Opening State Summary`; `## Activity Proposal & Rationale`; `## What Happened`; `## Decisions Locked`; `## Artifacts Touched`; `## Open Threads for Next Session`; `## Quality Gates Checklist` |
| `PLC_OPC_Diagnostic` | Walkthrough of OPC sections in scope (varies by `plc_OPC_Section_Scope`: sphere → §§ 2-13; practitioner_self → § 16; engagement_politics → § 17) |
| `PLC_Engagement_Retrospective` | `## Cycles Run + Audit Pass Rate`; `## Campaigns History`; `## Per-Actor Perception Gap Trajectory`; `## Per-Principal Resource Trajectory`; `## Forecast Accuracy`; `## Pattern Recognition Accuracy`; `## Eight Benefits at Open vs Close`; `## UNCOVER-Payoff Log`; `## Handoff Documentation` (consultant mode) |
| `PLC_Move` | `## Description`; `## Signature` (Option Affected / Consideration Affected / Effect); `## Strategy Number`; `## Cluster ID`; `## Example`; `## Counter-Moves`; `## Appears In Tactics` (reciprocal of `composed-of`) |
| `PLC_Tactic` | `## Description`; `## Type`; `## Strategy` (specific + generic); `## Cluster`; `## Theorists Cited`; `## Analysis` (influence mechanism + scenarios); `## Versatility`; `## Application Examples`; `## Composed Of Moves` (per D14) |
| `PLC_Strategy` | `## Lever Combination`; `## Name`; `## Tactics Using This Strategy`; `## Moves Using This Strategy` |
| `PLC_Cluster` | `## Description`; `## Tactics In Cluster`; `## Theme`; `## Related Clusters` |
| `PLC_Theorist` | `## Foundational Principle`; `## Key Concepts`; `## Tactics Citing` (reverse of `cites`); `## Sample Works (canonical reference list)` |
| `PLC_Pattern` | `## Definition`; `## Family` (per `plc_Pattern_Family` enum); `## Diagnostic Features`; `## Examples`; `## Counter-Patterns`; `## Tagged To Actors`; `## Tagged To Cycles` |

## The 12 relation families

Every relation in PLC participates in one of 12 families. Reciprocal pairs are encoded in frontmatter as YAML wiki-link arrays.

| # | Family | Forward | Reverse | Wires |
|---|---|---|---|---|
| 1 | Compositional | `composed-of` | `appears-in` | `PLC_Tactic` ↔ `PLC_Move` |
| 1 | Compositional | `parent-of` | `child-of` | `PLC_Campaign` ↔ sub-`PLC_Campaign` (recursive Interest tree) |
| 2 | Classification | `classified-by` | `classifies` | `PLC_Move` / `PLC_Tactic` ↔ `PLC_Strategy` |
| 2 | Classification | `clustered-in` | `contains` | `PLC_Move` / `PLC_Tactic` ↔ `PLC_Cluster` |
| 3 | Citation | `cites` | `cited-by` | `PLC_Tactic` / `PLC_Cycle` ↔ `PLC_Theorist` |
| 4 | Tagging | `tagged-with` | `tagged-by` | `PLC_Actor` / `PLC_Cycle` ↔ `PLC_Pattern` |
| 5 | Cycle↔Actor | `protagonist-of` | `protagonized-by` | `PLC_Actor` ↔ `PLC_Cycle` |
| 5 | Cycle↔Actor | `targets` | `targeted-by` | `PLC_Cycle` ↔ `PLC_Actor` (the target) |
| 6 | Cycle↔Campaign | `advances` | `advanced-by` | `PLC_Cycle` ↔ `PLC_Campaign` |
| 7 | Principal ownership | `owned-by` | `owns` | `PLC_Campaign` ↔ `PLC_Principal` (joint campaigns supported) |
| 8 | Cycle audit trail | `considered` | `considered-in` | `PLC_Cycle` → `PLC_Tactic` (alternatives audit) |
| 8 | Cycle audit trail | `selected` | `selected-in` | `PLC_Cycle` → `PLC_Tactic` (committed move) |
| 8 | Cycle audit trail | `engaged` | `engaged-by` | `PLC_Cycle` → `PLC_Cluster` / `PLC_Theorist` / `PLC_Pattern` (what surfaced) |
| 9 | Resource graph | `holds-resource` | `held-by` | `PLC_Actor` ↔ `Resource_Type` (9-type taxonomy) |
| 9 | Resource graph | `owes` | `owed-by` | `PLC_Actor` ↔ `PLC_Actor` (IOU ledger) |
| 10 | Network alignment | `allied-with` | (symmetric) | `PLC_Actor` ↔ `PLC_Actor` |
| 10 | Network alignment | `opposed-by` | (symmetric) | `PLC_Actor` ↔ `PLC_Actor` |
| 10 | Network alignment | `coalitioned-with` | (symmetric) | `PLC_Actor` ↔ `PLC_Actor` (named coalition membership) |
| 10 | Network alignment | `brokers-between` | `brokered-by` | `PLC_Actor` ↔ `PLC_Actor` (network broker role) |
| 11 | Information flow | `informs` | `informed-by` | `PLC_Actor` ↔ `PLC_Actor` |
| 11 | Information flow | `bypasses` | `bypassed-by` | `PLC_Actor` ↔ `PLC_Actor` (info flows skipping the actor) |
| 12 | Temporal/predictive | `precedes` | `follows` | `PLC_Cycle` ↔ `PLC_Cycle` (temporal sequence) |
| 12 | Temporal/predictive | `forecasts` | `forecasted-by` | `PLC_Cycle` ↔ `PLC_Cycle` (predicted next move) |

Plus the lateral catch-all `related-to` for non-canonical lateral references (used sparingly).

Total: 24 named relations across 12 families.

### Reciprocal-update discipline (P11)

When an Item declares a relation in one direction (e.g., `plc_Cites_Theorists: ["[[Schelling]]"]` on a Tactic), the AI proposes the reverse update (`plc_Citing_Tactics: ["[[Tactic-0029]]"]` on the cited Theorist's file).

Session-end protocol enforces:
1. Scan session's touched files for new relations
2. For each new relation, locate the related Item
3. Propose appending the reverse to the related Item's appropriate `## ... Reciprocal` section
4. Make the updates or note them in session log for next-session follow-up

Asymmetric graph corruption (F5 failure mode) results when this discipline is skipped.

## The three reference systems (per D18, P8)

PLC uses three distinct reference systems coexisting by domain. Do not conflate.

### System 1: Slash Addressing (from dissertation)

**Grain:** Inside one ADAPT cycle. Addresses cycle constituents.

**Syntax:** Greek operators (predicates) + Latin set-members (subjects/objects) + path syntax.

| Construct | Operator | Set member |
|---|---|---|
| Actor | α | a |
| Agenda | A | A |
| Target | τ | t |
| Interest | ι | i |
| Detection | δ | d |
| Decision Matrix | Δ | D |
| Objective | ω | o |
| Outcome | Ω | O |
| Intention | γ | g |
| Perception | Γ | G |
| Execution | ε | e |
| Selection | Σ | S |
| Preferred Position | π | P |
| Adverse Alternative | ψ | X |
| Benefit | β | b |
| Cost | κ | c |
| Utility | λ | u |
| Required Resources | θ | q |
| Obtained Resources | Φ | Q |
| Current Resources | Θ | R |
| Obtained Utility | Λ | U |

**Path example:** `α.1/i.1/D.1/P.1` = Actor 1's first interest's first decision matrix's preferred position.

**Used in:** Cycle log frontmatter (`plc_Slash_Constituents` field family); Actor file `## Current Funnel` sections; Strategy and Move signature schemas (`B(X)↑ + C(Y)↑` notation derives from this system).

**Not used in:** Sphere diagnostic state (use OPC IDs); Catalogue references (use Catalogue Reference IDs); operator-facing prose (use plain English with AI translation on request).

### System 2: OPC Hierarchical IDs

**Grain:** Sphere structural state. Addresses elements of the political landscape.

**Syntax:** 6-level decimal notation (`X.Y.Z.A.B.C`).

**Example:** `2.1.6.4.2` = Section 2 (Situational Context) > 2.1 (Organizational Structure) > 2.1.6 (Soft Power Architecture) > 2.1.6.4 (Ritual & Symbolic Politics) > 2.1.6.4.2 (Recognition Ceremonies).

**Used in:** `PLC_OPC_Diagnostic` walkthrough structure; Cycle log frontmatter (`plc_OPC_Diagnostic_Refs` field); Pattern tagging when patterns derive from OPC § 13.

**Not used in:** Cycle constituents (use slash addressing); Catalogue references (use Catalogue Reference IDs).

### System 3: Catalogue Reference IDs

**Grain:** The tactical corpus. Addresses tactics, strategies, clusters, theorists.

**Syntax (four sub-types):**
- **Tactic IDs** — zero-padded 4-digit (`0001`-`0782`)
- **Strategy Numbers** — integer (`1`-`16`)
- **Cluster IDs** — `C01`-`C84` plus `ORIGINAL`
- **Theorist names** — normalized strings (`Schelling`, `Kahneman-Tversky`, `Sun-Tzu`, etc.)

**Used in:** Cycle log frontmatter (`tactic_ids_considered`, `tactic_ids_selected`, `strategy_number_selected`, `clusters_engaged`, `theorists_invoked`); MOVE-LOOKUP and THEORIST-LOOKUP queries; Move and Tactic Item bodies.

**Not used in:** Cycle constituents (use slash addressing); Sphere diagnostic state (use OPC IDs).

### Translation discipline

In chat / UI, the AI translates between system IDs and plain English on operator request:

- `α.1/i.1/D.1/P.1` ↔ "Alice's first interest's first matrix's preferred position"
- `2.1.6.4.2` ↔ "recognition ceremonies as soft-power signals"
- `0029` ↔ "the Decoy Initiative tactic"

Translation is on-demand; the underlying schema preserves system-native IDs for searchability.

## Section discipline (Mode D files; per D28)

Items in Mode D (Principal, Actor baseline, Actor overlay, Campaign, Pattern) carry mixed-mode content:

- **`## Current ...` sections** — overwrite on update (current state)
- **`## ... History` sections** — append on update (chronological accumulation)

The AI session-end protocol enforces:

1. Rewriting `## Current` sections in place with the new current values
2. Appending new entries to `## ... History` sections without touching prior entries
3. Section headers are explicit and consistent across Items of the same Type

Operators editing manually should respect the same discipline. The convention is documented in OPERATOR-GUIDE so manual edits don't inadvertently corrupt history.

## Cycle status flag (per D28 Tension 1)

`PLC_Cycle` carries a `plc_Cycle_Status: open | closed` enum in frontmatter.

**When `open`:** Cycle log is in Mode D (append-friendly). Constituents 1-14 fill progressively as planning → execution → tracking unfolds over hours-to-weeks. Frontmatter fields update; body sections append. The AI can edit any section.

**When `closed`:** Cycle log transitions to Mode E (immutable). The AI refuses further edits. The cycle's closure constituent (Obtained Resource) (*"This concludes one discrete interaction cycle"*) sets the status to closed. Closed cycle logs are the audit-grade durable record.

**Cycle revival:** Closed cycles are NOT revivable. If a cycle's outcomes change post-hoc (e.g., the target reverses their selection), a NEW cycle is opened to handle the new dynamics; the original closed cycle remains as historical record. Reference the original via `precedes` / `follows` relation.

## Mastery scales (per D25)

PLC uses Item-level maturity scales where operationally useful. No single OV-wide "mastery scale" (the dissertation's recursive operation thesis precludes a terminal-state framing).

### `plc_Actor_Completeness` (0-5)

Primary scale on `PLC_Actor`:

| Level | Label | Diagnostic |
|---|---|---|
| 0 | `stub` | name only |
| 1 | `sketched` | role + agenda hypothesis |
| 2 | `drafted` | full ADAPT profile draft + observation pattern |
| 3 | `detailed` | + 9-type resource state estimate + perception biases + per-principal overlay |
| 4 | `comprehensive` | + multi-cycle perception-gap log + pattern tagging |
| 5 | `deeply-known` | + cross-engagement continuity + theorist frame inferred |

**Gate behavior in RUN-CYCLE:** if target Actor has completeness ≤ 1 (level 0 or 1), AI surfaces a warning at session-open (*"this Actor is at level `sketched` — cycle reasoning is thin; consider ACTOR-UPDATE before proceeding"*). Operator can override; override logged as `plc_Completeness_Override_Acknowledged: true` in Cycle frontmatter.

### `plc_Principal_Funnel_Sharpness` (0-5)

Secondary scale on `PLC_Principal`:

| Level | Label | Diagnostic |
|---|---|---|
| 0 | `agenda-only` | only the long-running agenda is named |
| 1 | `interest-named` | current Interest specified |
| 2 | `objective-specified` | concrete Objective written |
| 3 | `goal-measurable` | specific measurable Goal articulated |
| 4 | `target-named` | the Target (person/thing to move) named explicitly |
| 5 | `multi-cycle-validated` | funnel has produced multiple completed cycles |

QUARTERLY-AUDIT surfaces principals with funnel sharpness < 3 for follow-up.

### `plc_OPC_Diagnostic_Completeness`

Count field on `PLC_OPC_Diagnostic` (sphere scope): `sections_walked / total_sections`. Not a discrete scale; numeric ratio.

### Operator practice maturity (Framing A — NOT a schema field)

A subjective 0-5 scale (`not-started` / `introduced` / `recognized` / `applied` / `mastered` / `teachable`) is documented in OPERATOR-GUIDE for QUARTERLY-AUDIT self-reflection. **NOT persisted by the AI; NOT a schema field.** Per D25.

## State-persistence mode summary (per D28)

Full mode contract in `06-STATE-PERSISTENCE.md`. Quick summary per Type:

| Type | Mode | Discipline |
|---|---|---|
| `PLC_Sphere_Manifest` | C — overwrite | Identity rarely changes; rewrite on change |
| `PLC_Sphere_State` | C — overwrite | Rewritten every session end |
| `PLC_Sphere_Decisions` | A — append-only | Sphere-level decisions only (per D27 criteria) |
| `PLC_Principal` | D — append-friendly | Current overwrite + History accumulate |
| `PLC_Actor` (baseline + overlay) | D — append-friendly | Current overwrite + History accumulate |
| `PLC_Campaign` | D — append-friendly | Frontmatter overwrites; sub-Interest tree + cycle refs accumulate |
| `PLC_Cycle` | D → E via `plc_Cycle_Status` flag | Open: Mode D progressive fill. Closed: Mode E immutable. |
| `PLC_Session` | E — immutable | Created at session end; never edited |
| `PLC_OPC_Diagnostic` | E — immutable | Created at OPC-DIAGNOSE; refreshes create new timestamped files |
| `PLC_Engagement_Retrospective` | E — immutable | Created at SPHERE-CLOSE; archived even if engagement revived |
| `PLC_Move` / `PLC_Tactic` / `PLC_Strategy` / `PLC_Cluster` / `PLC_Theorist` | C — release-owned | Updated via `git pull`; not operator-edited |
| `PLC_Pattern` | D — append-friendly | Operator-curated; AI proposes updates from UNCOVER |

## Convention compliance

PLC inherits all conventions from `_meta/CONVENTIONS.md`:

- **Convention 1** — Six Universal Core frontmatter fields (`type`, `Item_ID`, `Title`, `Date_Added`, `Date_Modified`, `Needs_Processing`)
- **Convention 2** — Case rules: core keys `Title_Snake_Case`; namespace prefixes `lowercase_snake_case`; acronyms fully capitalized; body after prefix `Title_Snake_Case`; enum identifiers `lowercase_snake_case`
- **Convention 3** — One namespace per OV: `plc_` (Political Landscape Cartography)
- **Convention 4** — Every Type gets its own `type` value (`PLC_<TypeName>`); non-Item files use `type: Fleeting`
- **Convention 5** — Schema-of-namespace declared in `_plc-engine/_meta/SCHEMA-OF-SCHEMAS.md`
- **Convention 6** — `_types/` folder at OV root with one `.md` file per Type (16 files)
- **Convention 7** — Install-and-update pattern (see `INSTALL.md`, `OPERATOR-GUIDE.md`, `UPDATE-PROMPT.md`)
- **Convention 8** — Engine vs operator-content boundary (4 zones — Engine, Operator-Private, Operator-Extension, Shipped Examples)

## Where Items live (folder structure)

Per D27 (sphere backbone) and Convention 8 (zone boundaries):

```
Political-Landscape-Cartography/                    ← OV root
├── AI-BOOTSTRAP.md, BOOTSTRAP-NEW-SPHERE.md, ...   ← engine zone (front-door)
├── _plc-engine/                                     ← engine zone
│   ├── 00-START-HERE.md ... 07-SHIPPING-CHECKLIST.md
│   ├── _templates/                                  ← 22 markdown + YAML scaffolds
│   ├── redaction-profiles/                          ← 5 audience YAML profiles
│   └── _meta/                                       ← SCHEMA-OF-SCHEMAS, CONVENTIONS, FAILURE-MODES
├── _types/                                     ← 16 PLC_*.md definition files (Convention 6)
├── _frameworks/                                     ← engine zone (canonical reference)
│   ├── ADAPT.md
│   ├── OPC-Assessment.md (or split per section)
│   ├── dissertation-table-3/                        ← ~100 PLC_Move files
│   ├── political-warfare-catalogue/                 ← 782 tactics + 16 strategies + 84 clusters + 50 theorists
│   ├── strategies/                                  ← 16 PLC_Strategy definition files
│   └── sources/                                     ← canonical PDFs + JSONs
├── _PATTERNS/                                       ← canonical PLC_Pattern files (60+ from OPC §§ 13 + 2.2)
├── Example-Sphere-Acme-Corp/                        ← shipped examples zone
└── <Operator-Extended-Sphere>/                      ← operator-extension zone (e.g., the operator's actual client cartridges)
    ├── _sphere-manifest.md, _sphere-state.md, _sphere-decisions.md  ← 3 backbone files
    ├── _PRINCIPALS/<principal>.md
    ├── Actors/<actor-slug>/_baseline.md + _view-<principal>.md
    ├── Campaigns/<slug>.md
    ├── Cycles/<YYYY-MM-DD>_<NNN>_<slug>.md
    ├── Sessions/<YYYY-MM-DD>_<NNN>_<activity>.md
    ├── Diagnostics/{opc|practitioner-self-assessment|engagement-politics|engagement-retrospective}-<YYYY-MM-DD>.md
    ├── Exports/<YYYY-MM-DD>_<audience>_<slug>.md
    └── _PATTERNS/<pattern>.md                        ← sphere-extensible (operator-curated archetypes)
```

The operator's extended sphere cartridges live as top-level folders at OV root, parallel to the shipped example sphere. Per Convention 8, `git pull` updates the engine + shipped examples + `_types/` + `_frameworks/` + canonical `_PATTERNS/` without disturbing operator-extended spheres.

## Frontmatter conventions (per Convention 1 + Convention 2)

All Items declare frontmatter in this order:

```yaml
---
Item_ID: <slug>
type: PLC_<TypeName>
title: "<Human-readable title>"
plc_<...>: <PLC-specific fields per Type>
Date_Added: YYYY-MM-DD
Date_Modified: YYYY-MM-DD
Needs_Processing: false
AI_Instructions: ""
---
```

The `_extends_type: PLC_<TypeName>` header in Templates points to the canonical Type definition for validation traceability.

When in doubt about a specific Type's required fields, consult `_types/PLC_<TypeName>.md`.
