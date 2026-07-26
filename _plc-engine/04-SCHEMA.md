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

> **The structural contract every Item in PLC conforms to. 17 first-class Types + 13 relation families + state-persistence summary + reference-system specifications.**

## The 17 first-class Types

| # | Type | Cardinality | Grain | Lives at |
|---|---|---|---|---|
| 1 | `PLC_Sphere_Manifest` | 1 per sphere | sphere-identity | `<Sphere>/_sphere-manifest.md` |
| 2 | `PLC_Sphere_State` | 1 per sphere | sphere-state-rollup | `<Sphere>/_sphere-state.md` |
| 3 | `PLC_Sphere_Decisions` | 1 per sphere | sphere-decisions-log | `<Sphere>/_sphere-decisions.md` |
| 4 | `PLC_Principal` | 1..N per sphere | protagonist | `<Sphere>/Principals/<name>.md` |
| 5 | `PLC_Actor` | many per sphere | long-lived dossier | `<Sphere>/Actors/actor-<slug>.md` (optional multi-principal overlay: `<slug>/_baseline.md` + `_view-<principal>.md`) |
| 6 | `PLC_Campaign` | many per sphere | strategic arc | `<Sphere>/Campaigns/<slug>.md` |
| 7 | `PLC_Cycle` | many per sphere | operational artifact | `<Sphere>/Cycles/cycle-<NNNN>.md` (4-digit, zero-padded) |
| 8 | `PLC_Session` | many per sphere | history | `<Sphere>/Sessions/<YYYY-MM-DD>_<NNN>_<activity>.md` |
| 9 | `PLC_OPC_Diagnostic` | many per sphere | cartography output | `<Sphere>/OPC-Diagnostics/{opc\|practitioner-self-assessment\|engagement-politics}-<YYYY-MM-DD>.md` |
| 10 | `PLC_Engagement_Retrospective` | 1 per engagement (multiple per revived sphere) | engagement deliverable | `<Sphere>/OPC-Diagnostics/engagement-retrospective-<YYYY-MM-DD>.md` |
| 11 | `PLC_Move` | 148 manifest rows + operator-extensible | smallest tactical unit | `_frameworks/dissertation-table-3/<NNN>-<slug>.md` |
| 12 | `PLC_Tactic` | 782 (canonical) | composed tactical pattern | `_frameworks/political-warfare-catalogue/tactics/<range>/<NNNN>-<slug>.md` (bucketed by ID range) |
| 13 | `PLC_Strategy` | 16 (closed) | lever-combination meta-pattern | `_frameworks/political-warfare-catalogue/by-strategy/<NN>-<slug>.md` |
| 14 | `PLC_Cluster` | 84 (canonical) | thematic family of tactics | `_frameworks/political-warfare-catalogue/by-cluster/<CNN>-<slug>.md` |
| 15 | `PLC_Theorist` | 50 (canonical) + operator-extensible | intellectual lineage | `_frameworks/political-warfare-catalogue/by-theorist/<name>.md` |
| 16 | `PLC_Pattern` | 60+ (from OPC §§ 13 + 2.2) + operator-extensible | situational archetype | `_PATTERNS/<name>.md` (OV-root canonical) + `<Sphere>/_PATTERNS/<name>.md` (sphere-extensible) |
| 17 | `PLC_Detection_Record` (v1.2+) | 0..1 per (sphere, target actor) | forward-estimation audit trail | `<Sphere>/Detection/detection-<actor-slug>.md` |

Types 1-10 and 17 are *sphere-content* (live inside operator-extended sphere cartridges). Types 11-16 are *OV-content* (live at OV root; shipped canonical reference).

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
| `PLC_Principal` | `## Current` (with `### Funnel`, `### Authority Scope`, `### Active Coaching Themes`, `### Mastery Signals`, `### Current Resource Holdings` (v1.2+)); `## Engagement History`; `## Mastery History`; `## Cross-References` |
| `PLC_Actor` | `## Current` (funnel, resource state incl. effect signatures and durability, observation pattern, inferred theorist frame, tagged patterns, and — v1.2+ — `### Convertibility Edges` / `### Estimated Matrix Summary`); `## Perception History`; `## Resource History`; `## Cross-References` |
| `PLC_Actor` (optional multi-principal overlay — *not the default layout, not shipped in the example*) | `## Current Relationship Status`; `## Current Debt Ledger`; `## Perception Gap History (this principal's view)`; `## Cycle References`; `## Provenance` |
| `PLC_Campaign` | `## Root Interest`; `## Sub-Interest Tree`; `## Owning Principals`; `## Cycle References`; `## Lifecycle History` |
| `PLC_Cycle` | body sections corresponding to PLC's RUN-CYCLE protocol output (Agenda / Landscape Assessment / OPC Self-Diagnosis / Principal Funnel / ALTERNATIVES-AUDIT / ETHICAL-ACCOUNTING / Considered Moves / Selected Moves / Engaged Moves / Phase Log / Refinement / Lessons); the 14 dissertation constituents are tracked via frontmatter fields; `## Alternatives Audit`; `## Ethical Accounting`; `## Slash Constituents` reference |
| `PLC_Session` | `## Activity Recap`; `## Files Touched`; `## Decisions Made`; `## Reciprocal Updates Applied`; `## Gate Outcomes` (RUN_CYCLE only); `## Activity-Specific Block`; `## Open Threads`; `## Next Activity Recommendation`; `## Next Activity Chosen`; `## Cross-References` |
| `PLC_OPC_Diagnostic` | Walkthrough of OPC sections in scope (varies by `plc_OPC_Section_Scope`: sphere → §§ 2-13; practitioner_self → § 16; engagement_politics → § 17) |
| `PLC_Engagement_Retrospective` | `## Cycles Run + Audit Pass Rate`; `## Campaigns History`; `## Per-Actor Perception Gap Trajectory`; `## Per-Principal Resource Trajectory`; `## Forecast Accuracy`; `## Pattern Recognition Accuracy`; `## Eight Benefits at Open vs Close`; `## UNCOVER-Payoff Log`; `## Handoff Documentation` (consultant mode) |
| `PLC_Move` | `## Description`; `## Signature` (Option Affected / Consideration Affected / Effect); `## Strategy Number`; `## Cluster ID`; `## Example`; `## Counter-Moves`; `## Appears In Tactics` (reciprocal of `composed-of`) |
| `PLC_Tactic` | `## Description`; `## Type`; `## Strategy` (specific + generic); `## Cluster`; `## Theorists Cited`; `## Analysis` (influence mechanism + scenarios); `## Versatility`; `## Application Examples`; `## Composed Of Moves` (per D14) |
| `PLC_Strategy` | `## Lever Combination`; `## Name`; `## Tactics Using This Strategy`; `## Moves Using This Strategy` |
| `PLC_Cluster` | `## Description`; `## Tactics In Cluster`; `## Theme`; `## Related Clusters` |
| `PLC_Theorist` | `## Foundational Principle`; `## Key Concepts`; `## Tactics Citing` (reverse of `cites`); `## Sample Works (canonical reference list)` |
| `PLC_Pattern` | `## Definition`; `## Family` (per `plc_Pattern_Family` enum); `## Diagnostic Features`; `## Examples`; `## Counter-Patterns`; `## Tagged To Actors`; `## Tagged To Cycles` |
| `PLC_Detection_Record` (v1.2+) | `## Current` (differential + margin + depth estimates); `## Probe Log` (append-only; VoI rationale + pre-registered predictions + observations + updates); `## Stop Decision`; `## Cross-References` |

## The 13 relation families

Every relation in PLC participates in one of 13 families. Reciprocal pairs are encoded in frontmatter as YAML wiki-link arrays.

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
| 12 | Temporal/predictive | `estimates` | `estimated-by` | `PLC_Detection_Record` ↔ `PLC_Actor` (v1.2+: the forward estimation loop's record targets an actor) |
| 13 | Defense graph | `countered-by` | `counters` | `PLC_Tactic` ↔ `PLC_Tactic` (v1.2+: promoted from the catalogue's Resolution-Approach prose; stored in the sidecar as `counter_tactic_ids` / `counters_tactic_ids`) |

Plus the lateral catch-all `related-to` for non-canonical lateral references (used sparingly).

Total: 27 named relations across 13 families (estimates/estimated-by and countered-by/counters added v1.2).

**Family 13 is machine-derived, not hand-authored.** `counters_tactic_ids` is generated as the exact inverse of `counter_tactic_ids` when the catalogue sidecar is rebuilt. Do not hand-edit one side; edit the forward direction and regenerate. It is also the one relation family that lives outside the Items themselves — the catalogue's tactic bodies are Mode E and carry no frontmatter, so the graph is held in `_frameworks/political-warfare-catalogue/INDEX-lspi.json`.

### Reciprocal-update discipline (P11)

When an Item declares a relation in one direction (e.g., `plc_Cites_Theorists: ["[[Schelling]]"]` on a Tactic), the AI proposes the reverse update (`plc_Citing_Tactics: ["[[Tactic-0029]]"]` on the cited Theorist's file).

Session-end protocol enforces:
1. Scan session's touched files for new relations
2. For each new relation, locate the related Item
3. Propose appending the reverse to the related Item's appropriate `## ... Reciprocal` section
4. Make the updates or note them in session log for next-session follow-up

Asymmetric graph corruption (F5 failure mode) results when this discipline is skipped.

## The three reference systems (per D18, P8)

PLC uses three distinct reference systems coexisting by domain. Do not conflate (F9). LSPI's own statement of this separation (`LSPI-Foundations.md` §2.4) is normative: LSPI expressions never carry OPC IDs or Catalogue IDs; OPC and Catalogue IDs never appear in LSPI fields.

### System 1: Slash Addressing — formally grounded in LSPI (from dissertation, per substrate authority 5)

**Grain:** Inside one interaction cycle. Addresses cycle constituents.

**Formal status:** System 1 is no longer conventional notation. It is the surface syntax of **LSPI** — a typed DSL with a small-step operational semantics and proven meta-theory (`_frameworks/lspi/LSPI-Foundations.md`). What follows is the PLC-facing summary; the treatise carries the full statements and **wins for LSPI-internal questions** (well-formedness, typing, congruence, transition). The PLC engine wins for sphere-level discipline (gates, audit trail, F9 separation).

**The 21 typed constituents (dissertation Table 4).** Greek = operation form (predicate position, takes an argument in round brackets); Latin = set/attribute form (subject/object position, appears in paths). Both refer to the same theoretical category — the duality is load-bearing.

| Construct | Operation (Greek) | Set member (Latin) | Note |
|---|---|---|---|
| Actor | α | a | nominal-only in practice |
| Agenda | Α † | A | cycle root |
| Target | τ | t | nominal-only |
| Interest | ι | i | |
| Detection | δ | d | actor-performed; drives R-detect |
| Decision Matrix | Δ | D | appears only as path-node `D`, never `Δ(…)` |
| Objective | ω | o | projection-bearing |
| Outcome | Ω | O | systemic (no agent prefix) |
| Intention | γ | g | multi-instance (g_1 … g_K) |
| Perception | Γ | G | target-performed |
| Execution | ε | e | actor-performed; a citation into the Catalogue post-integration |
| Selection | Σ | S | target-performed |
| Preferred Position | π | P | member of D |
| Adverse Alternative | ψ | X | member of D |
| Benefit | β | b | consideration (+) |
| Cost | κ | c | consideration (−) |
| Utility | λ | u | net per option |
| Required Resources | θ | q | gate operand |
| Obtained Resources | Φ ‡ | Q | flows back at close |
| Current Resources | Θ ‡ | R | actor's multiset |
| Obtained Utility | Λ ‡ | U | target-side gain |

**Case discipline:** uppercase Greek ≈ aggregate/summary operations; lowercase ≈ single instances. Constituent-specific — Table 4 by row is canonical; do not override it with the global pattern.

**The three lexer normalizations** (adopt everywhere System 1 text is read):
- **† Α/A glyph (M4):** Greek uppercase Alpha and Latin A are visually identical and used interchangeably in source material — normalize to one token.
- **‡ Θ/Φ/Λ overload (D-21):** the worked cases write Θ for all three resource/utility operations. Table 4 is canonical; disambiguate by structural context: Θ followed by `/Q.` is Φ; followed by `/U.` is Λ; otherwise Θ. The most consequential single normalization in LSPI.
- **`t.`-insertion (D-26):** when comparison shorthand omits the target node between interest and matrix, insert `t.` (canonical form `[Α/i./t./D./P./u.] > [Α/i./t./D./X./u.]`).

**The four operator families + prefix dispatch:**
- **A — Path:** slash `/` (parent→child, left-associative, non-commutative); sole-of-type dot `.` ("the only one of this type in the parent set"); ordinal suffix (sibling discrimination, **parent-set-scoped**, per-snapshot — primed and unprimed siblings number separately).
- **B — Scope:** `[ ]` complete constituent designation; `( )` operation argument; `{ }` unordered set (member order is congruence-irrelevant).
- **C — Semantic:** prime `′` (projected vs realized — both persist, the realization never overwrites the projection); yields `→` (two type-dispatched senses: projection-clause vs effect-on-matrix); `≡` (split by layer: symmetric structural congruence at Layer 3 vs directional definition-unfolding as the non-firing R-unfold discipline); attribution `:=`; capability predicates `∋` / `∌`.
- **D — Arithmetic/comparison:** `+` `−` on matrix cells and resource quantities only; `<` `>` `≤` `≥` `=` on utilities only; comma as set separator.
- **Agent-attribution prefix (dispatch):** `[a.]·` actor operations; `[Α/i./t.]·` target operations; bare `·` systemic (Ω). The prefix determines which transition rule fires.

**Path example:** `α.1/i.1/D.1/P.1` = Actor 1's first interest's first decision matrix's preferred position.

**Uniqueness and keying (Theorem 13.1):** constituent addresses are unique **within one actor's agenda tree only** — paths do not embed actor identity. Every PLC field holding an LSPI path MUST have a sibling field naming the owning actor (key = owning-actor + path). Two actors may both legitimately hold `Α/i./t.`.

**Generation discipline (writing LSPI):** never invent notation. Copy an existing pattern from the worked example (`Spheres/Example-Sphere-Acme-Corp/Cycles/cycle-0009.md` § LSPI Operation Record) or this section's examples and substitute constituents; if no validated pattern matches, write plain English and flag it for the operator. An invented-but-plausible expression is an F10 violation (see `05-WRITING-FOR-AI.md` § F10, generation half).

**The five-layer validation ladder (mandatory processing order for AI engines):** (1) parse against the grammar → (2) type-check → (3) congruence-check against any reference term → (4) transition only if a rule licenses it → (5) invoke theorems as needed. If any layer rejects, **surface the rejection with a citation to the violated rule — never silently coerce** (F10). A stuck configuration means operator judgment must intervene — that is Pillar 2, not an error.

**The ladder applies to LSPI terms only.** Structural markers (`⟨open, C⟩`, `⟨gate-pass, q⟩`, `⟨select-staged, σ⟩`, …) are audit-trail meta-entries, **not** terms: they have no Layer-2 sort, and running one down the ladder produces a spurious rejection. The closed marker vocabulary is in `_types/PLC_Cycle.md`; the rules that write them are in `09-LSPI-RULES.md`.

#### Layer 2 — the type system (what "type-check" means at step 2)

Well-formedness (Layer 1) says an expression is *shaped* like LSPI. Typing says it is *about* something coherent. Three checks carry almost all the practical weight:

**(a) The child-class lattice — which constituent may hang below which.** A slash composition `parent/child` is well-typed only if the child's sort is admissible under the parent's. The lattice is a fixed table, not a judgment call; the rows that matter in day-to-day cycle work:

| Parent | Admissible children |
|---|---|
| agenda | interest, outcome |
| interest | detection, target, objective |
| target | decision matrix, selection |
| decision matrix | preferred position, adverse alternative, perception |
| position / alternative | benefit, cost, utility |
| objective | intention |
| **intention** | required resource, execution, **interest** ← *this row is the escalation mechanism* |
| outcome | resource obtained, utility obtained, selection |
| *leaves* | required resource, resources held, obtained resource, utility, benefit, cost, detection, execution |

Two consequences worth naming. First, `intention → interest` is why a failed gate can spawn a nested cycle at all: an unmet requirement becomes a new interest one level down. Second, **no sort appears in its own admissible-child column**, which is why `a/a` is ill-typed — a constituent cannot be its own child. You do not need a separate rule for that; the lattice already forbids it.

**(b) Prefix admissibility — who is allowed to perform an operation.** Every operation-bearing constituent admits exactly one agent class. This is not stylistic; the prefix is what selects which transition rule can fire.

| Class | Operations | Prefix form |
|---|---|---|
| actor-only | ι, δ, ω, γ, θ, ε, Φ | `[a.]·` |
| target-only | Σ, Γ, Λ | `[Α/i./t.]·` |
| systemic | Ω | **no prefix** |

`[a.]Σ(…)` (the actor performing the target's selection), `[Α/i./t.]δ(…)` (the target performing the actor's detection), and any prefixed `Ω` are type errors, not stylistic slips. They are also the most common way an AI-authored expression goes wrong, because the prose around them reads fine.

**(c) Argument-sort compatibility.** An operation's argument must terminate in the sort that operation consumes — detection takes a detection path, objective an objective path, execution an execution path, selection a matrix path, perception a perception path. And the argument must be a **fully-rooted path**: every well-formed path begins at the agenda root (`Α`) or the actor (`a.`). A bare fragment in operation-argument position is ill-formed however sensible it looks.

Also at Layer 2: the two senses of `→` are told apart by position (a projection clause inside a definitional body vs. an execution's effect on the matrix), the two senses of `=` are told apart by their left-hand side (a utility comparison vs. a perception evaluation), and **projected and realized forms are distinct sorts** — `t` and `t′` never unify. LSPI v1 has no subtyping; every well-typed term has exactly one sort.

#### Layer 3 — congruence (what "congruence-check" means at step 3)

Congruence is **thin by design**. It has exactly three generators, and there is no fourth:

| Generator | Statement | Effect |
|---|---|---|
| **A2** — slash associativity | `(a/b)/c ≡ a/(b/c)` | path grouping is syntactic only; right-associate to normalize |
| **D5** — set order irrelevance | `{d₁, d₂} ≡ {d₂, d₁}` | designation sets are unordered; sort members to normalize |
| **M4** — root glyph | `A ≡ Α` | Latin A and Greek Alpha are the same root |

**The decision procedure is normalize-then-compare:** reject ill-typed input first, then apply A2 (right-associate), D5 (sort set members), and M4 (normalize the root glyph), then test for syntactic identity. Sound and complete — the three generators do not interfere. Log which generators fired and how many times; a congruence claim with no trace is not auditable.

**Three things the congruence check must refuse to do.** Do not unfold a definition while comparing (unfolding is directional — it belongs to the `R-unfold` discipline, not here). Do not equate a primed form with its unprimed twin (four worked cases depend on the distinction). Do not assume the perception-evaluation `=` is symmetric.

Note what congruence is *not*: `a/b ≢ b/a` (paths are ordered), and a projection's direction cannot be reversed. An objective body is a forward projection precisely because the arrow does not commute.

**Option-role vocabulary:** in all PLC-authored artifacts the decision-matrix options are **`P`** (preferred position) and **`Adv`** (adverse alternative). The corpus's bare `X`/`Y` lever letters translate via the fixed alias map (corpus `X` → `P`, corpus `Y` → `Adv`) and never appear raw in integrated artifacts — LSPI's own `X` names the *adverse* alternative, so bare letters silently invert meaning across the two systems.

**Used in:** Cycle log frontmatter (`plc_Slash_Constituents` field family); Cycle `## LSPI Configuration ⟨C; M; S; R⟩` and `## Operation Record` sections (`_types/PLC_Cycle.md`); Actor file `## Current Funnel` sections; Strategy and Move signature schemas (`B(P)↑ + C(Adv)↑` lever notation binds to this system via the alias map).

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

`PLC_Cycle` carries a `plc_Cycle_Status` enum in frontmatter: `planning | active | engaged | closed | mooted | abandoned | e_immutable`.

**While `planning | active | engaged`:** the Cycle log is in Mode D (append-friendly). The 14 constituents fill progressively as planning → execution → tracking unfolds over hours-to-weeks. Frontmatter fields update; body sections append.

**At `closed`:** the closure constituent (Obtained Resource — *"this concludes one discrete interaction cycle"*) sets the status. The file stays **Mode D** through a seven-day grace window, so late realizations, flowbacks and reciprocal writebacks can still land; the AI prompts for the seal at the end of it.

**At `e_immutable`:** the file transitions to Mode E. The AI refuses further edits. This — not `closed` — is the audit-grade durable state. The D → E flip is an explicit operator election (P10), never automatic.

**At `mooted` or `abandoned` (v1.2+):** terminal, and neither produces a flowback. `mooted` records that the cycle's premise stopped holding (the world removed the question); `abandoned` records that the operator elected to stop (`R-abandon`, admissible from any state — see `09-LSPI-RULES.md`). Both follow the same grace-then-seal path as `closed`.

**Cycle revival:** closed cycles are NOT revivable. If a cycle's outcomes change post-hoc (e.g., the target reverses their selection), a NEW cycle is opened to handle the new dynamics; the original closed cycle remains as historical record. Reference the original via `precedes` / `follows` relation.

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

**Gate behavior in RUN-CYCLE:** if target Actor has completeness ≤ 1 (level 0 or 1), AI surfaces a warning at session-open (*"this Actor is at level `sketched` — cycle reasoning is thin; consider ACTOR-UPDATE before proceeding"*). Operator can override; the override is logged in the Cycle's `## σ / Guard Log` as a guard resolution naming the actor and the completeness level accepted (there is no dedicated frontmatter flag — the log is the record).

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
| `PLC_Actor` | D — append-friendly | Current overwrite + History accumulate. Flat `Actors/actor-<slug>.md` by default; the `<slug>/_baseline.md` + `_view-<principal>.md` split is an optional multi-principal overlay. |
| `PLC_Campaign` | D — append-friendly | Frontmatter overwrites; sub-Interest tree + cycle refs accumulate |
| `PLC_Cycle` | D → E via `plc_Cycle_Status` flag | Mode D through `planning`/`active`/`engaged`, and through `closed`/`mooted`/`abandoned` for the 7-day grace window. Mode E only at `e_immutable`, by operator election. |
| `PLC_Session` | A — append-only | Created at session end. The narrative is never rewritten; corrections are appended as dated blocks (this is what makes a session log an audit trail rather than a summary). |
| `PLC_OPC_Diagnostic` | E — immutable | Created at OPC-DIAGNOSE; refreshes create new timestamped files |
| `PLC_Engagement_Retrospective` | E — immutable | Created at SPHERE-CLOSE; archived even if engagement revived |
| `PLC_Move` / `PLC_Tactic` / `PLC_Strategy` / `PLC_Cluster` / `PLC_Theorist` | C — release-owned | Updated via `git pull`; not operator-edited |
| `PLC_Pattern` | D — append-friendly | Operator-curated; AI proposes updates from UNCOVER |
| `PLC_Detection_Record` (v1.2+) | D — append-friendly | `## Current` overwrite; `## Probe Log` append-only (pre-registered predictions NEVER edited post-observation) |

## Convention compliance

PLC inherits the OVE substrate conventions; their in-volume statements of record are `04-SCHEMA.md` (structure) and `05-WRITING-FOR-AI.md` (conventions and failure modes):

- **Convention 1** — Six Universal Core frontmatter fields (`type`, `Item_ID`, `Title`, `Date_Added`, `Date_Modified`, `Needs_Processing`)
- **Convention 2** — Case rules: core keys `Title_Snake_Case`; namespace prefixes `lowercase_snake_case`; acronyms fully capitalized; body after prefix `Title_Snake_Case`; enum identifiers `lowercase_snake_case`
- **Convention 3** — One namespace per OV: `plc_` (Political Landscape Cartography)
- **Convention 4** — Every Type gets its own `type` value (`PLC_<TypeName>`); non-Item files use `type: Fleeting`
- **Convention 5** — Schema-of-namespace declared in this chapter (`04-SCHEMA.md`), which is the volume's schema of schemas
- **Convention 6** — `_types/` folder at OV root with one `.md` file per Type (17 files)
- **Convention 7** — Install-and-update pattern (see `INSTALL.md`, `OPERATOR-GUIDE.md`, `UPDATE-PROMPT.md`)
- **Convention 8** — Engine vs operator-content boundary (4 zones — Engine, Operator-Private, Operator-Extension, Shipped Examples)

## Where Items live (folder structure)

Per D27 (sphere backbone) and Convention 8 (zone boundaries):

```
Political-Landscape-Cartography/                    ← OV root
├── AI-BOOTSTRAP.md, BOOTSTRAP-NEW-SPHERE.md, ...   ← engine zone (front-door)
├── _plc-engine/                                     ← engine zone
│   ├── 00-START-HERE.md ... 09-LSPI-RULES.md        ← 10 engine chapters
│   ├── _templates/                                  ← 25 markdown scaffolds
│   └── _yaml/                                       ← export-schema.yaml
│       └── redaction-profiles/                      ← 5 audience YAML profiles
├── _types/                                          ← 17 PLC_*.md definition files (Convention 6)
├── _frameworks/                                     ← engine zone (canonical reference)
│   ├── ADAPT.md, 4R.md, OPC-Assessment.md, dissertation-substrate.md
│   ├── reflexivity-frontier.md                      ← frontier: true (non-operational)
│   ├── lspi/                                        ← Mode C mirrors of the LSPI Formal Foundation
│   ├── dissertation-table-3/                        ← Table-3-Manifest (148 rows) + authored PLC_Move files
│   ├── political-warfare-catalogue/                 ← 782 tactics + 16 strategies + 83 clusters + the `ORIGINAL` sentinel + 50 theorists
│   │   └── INDEX-lspi.json                          ← the LSPI binding sidecar (levers, ε-templates, 7 facets)
│   ├── strategies/                                  ← PLC_Strategy definition files (see ROADMAP — atoms not yet authored)
│   └── sources/                                     ← canonical source pointers
├── _PATTERNS/                                       ← canonical PLC_Pattern files (6 families)
└── Spheres/
    ├── Example-Sphere-Acme-Corp/                    ← shipped examples zone
    └── <Operator-Extended-Sphere>/                  ← operator-extension zone (the operator's actual client cartridges)
    ├── _sphere-manifest.md, _sphere-state.md, _sphere-decisions.md  ← 3 backbone files
    ├── Principals/<principal>.md
    ├── Actors/actor-<slug>.md              # optional overlay: <slug>/_baseline.md + _view-<principal>.md
    ├── Campaigns/<slug>.md
    ├── Cycles/cycle-<NNNN>.md
    ├── Detection/detection-<actor-slug>.md   # v1.2+ estimation records
    ├── Sessions/<YYYY-MM-DD>_<NNN>_<activity>.md
    ├── OPC-Diagnostics/{opc|practitioner-self-assessment|engagement-politics|engagement-retrospective}-<YYYY-MM-DD>.md
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
