---
type: Type
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-cycle-type
title: "PLC_Cycle — Type Definition"
Date_Added: 2026-06-13
Date_Modified: 2026-07-24
Needs_Processing: false
type_namespace: plc
type_version: "1.2"
---

# PLC_Cycle

## Purpose

The interaction-cycle protocol (14 operational constituents per PLC's walk-through) from the Lam 2018 dissertation, instantiated as a first-class Item. Each Cycle is one disciplined pass through Agenda → Decide → Act → Perceive → Track (with the dissertation's interaction-cycle constituents including alternatives audit + ethical accounting gates). The **central operational Type** — RUN-CYCLE writes here; ANALYZE-CYCLE reads from here; the audit trail flows through here.

Per D20 + D24 + D28 + D9. Embeds the two mandatory gates (ALTERNATIVES-AUDIT + ETHICAL-ACCOUNTING) per D9.

## Cardinality and grain

- **N per sphere.** Open-ended count over engagement life.
- **Lives at**: `Spheres/<Sphere>/Cycles/cycle-<NNNN>.md` (4-digit sequence, zero-padded; lowercase — matches the shipped example and `04-SCHEMA.md`)

## Durability mode

**Mode D → E.** The only Type with mode transition.

- During `cycle_status: planning | active | engaged | closed | mooted | abandoned` → Mode D (revisable)
- On `cycle_status: e_immutable` → Mode E (sealed; no edits)
- 7-day grace window after `closed` (or after `mooted` / `abandoned`, v1.2+) before AI prompts for seal

Per D28.

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Cycle` |
| `Item_ID` | string | `cycle-<NNNN>` |
| `Title` | string | `"Cycle <NNNN> — <one-line agenda summary>"` |
| `Date_Added` | ISO date | Cycle-open date |
| `Date_Modified` | ISO date | Most recent material update |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Campaign` | link | `[[campaign-<slug>]]` (optional; cycle can be sphere-direct) |
| `plc_Principal_Owner` | link | `[[principal-<slug>]]` |
| `plc_Cycle_Number` | integer | Sequence within sphere |
| `plc_Cycle_Status` | enum | `planning \| active \| engaged \| closed \| mooted \| abandoned \| e_immutable` (`mooted` / `abandoned` are v1.2+ terminal states) |
| `plc_Update_Mode` | enum | `D \| E` (mirrors status; D when status ∈ {planning, active, engaged, closed, mooted, abandoned}; E when `e_immutable`) |
| `plc_Started_Date` | ISO date | |
| `plc_Closed_Date` | ISO date | Empty until status `closed` |
| `plc_Sealed_Date` | ISO date | Empty until status `e_immutable` |
| `plc_Actor_Touched` | list[link] | Every Actor referenced in this cycle |
| `plc_Slash_Constituents` | list[string] | Slash addressing strings (per D18 system 1) |
| `plc_OPC_Diagnostic_Refs` | list[string] | OPC hierarchical IDs referenced (per D18 system 2) |
| `plc_Tactic_IDs_Considered` | list[string] | Catalogue Reference IDs in the considered set (per D16) |
| `plc_Tactic_IDs_Selected` | list[string] | Catalogue Reference IDs in the selected set (per D16) |
| `plc_Strategy_Number_Selected` | integer | 1-16 if a Catalogue strategy was lifted into selection |
| `plc_Clusters_Engaged` | list[string] | Shipped cluster codes — 83 of them in `C01`-`C96`, **gapped, not contiguous** (`C28`, `C45`, `C70`, `C71`, `C77`, `C78`, `C84`, `C85`, `C88`, `C89`, `C92`, `C93`, `C94` do not exist), plus the `ORIGINAL` sentinel. Verify against `by-cluster/` — see `PLC_Cluster.md` |
| `plc_Theorists_Invoked` | list[link] | `[[theorist-<name>]]` per invoked theorist |
| `plc_Alternatives_Audit_Completed_At` | ISO datetime | Empty if gate skipped |
| `plc_Ethical_Accounting_Completed_At` | ISO datetime | Empty if gate skipped |
| `plc_Accounting_Overrides` | list[string] | Each entry: `<gate>:<justification>` per D9 |
| `AI_Instructions` | string | Default `""` |

### Optional LSPI fields (v1.2+; per substrate authority 5)

All optional — pre-1.2 cycles remain valid without them.

| Field | Type | Notes |
|-------|------|-------|
| `plc_Strategic_Stance` | enum | `adaptive \| pre_committed_resource_careful \| pre_committed_resource_batched` — the Pillar-4 stance toward multi-intention uncertainty (Rusty / Nathan / Sarah patterns). Chosen at the first multi-intention moment; revisable, revision logged |
| `plc_Stance_Rationale` | string | Why this stance for this cycle |
| `plc_Probe_Budget_Remaining` | integer | Per-cycle probe budget (termination by construction; see `08-ESTIMATION`). Decrement per probe; resets per cycle |
| `plc_Detection_Record_Refs` | list[link] | `[[detection-<actor-slug>]]` records feeding this cycle |
| `plc_Suspended_Parent` | link | Parent cycle if this cycle was spawned by a gate-fail (`∌`); empty for top-level cycles |
| `plc_Spawned_Subcycles` | list[link] | Sub-cycles this cycle spawned (reciprocal of `plc_Suspended_Parent`) |

**Keying note (Theorem 13.1):** entries in `plc_Slash_Constituents` are keyed to `plc_Principal_Owner` as the owning actor unless an entry is explicitly annotated with another actor. Uniqueness of addresses holds per-actor only.

## Required body sections

The cycle body mirrors the 14-constituent dissertation protocol with the two embedded gates between capability-gate (constituent 9) and Execution (constituent 10). Body sections fill in order as the cycle progresses.

```markdown
# Cycle <NNNN> — <one-line agenda summary>

## Agenda
<The principal's articulated agenda for this cycle. ADAPT "A" beat. One paragraph.>

## Landscape Assessment
<Current sphere read going into the cycle. Citations to OPC IDs and Actor files.>

## OPC Self-Diagnosis
<Where the principal stands across the OPC sections most material to this agenda.>

## Principal Funnel
<The funnel narrowed for this specific cycle. Decision criteria.>

## ALTERNATIVES-AUDIT § 15 Pass (Gate 1)
<Walk through OPC § 15's 10 constructive approaches. For each: relevant? considered? proposed move?>

**Completed:** <ISO datetime>  OR  **Skipped — override justification:** <text>

## ETHICAL-ACCOUNTING § 11 Pass (Gate 2)
<Walk through OPC § 11: 3 harm scopes × 10 categories + 5 ethical frameworks weighting.>

**Completed:** <ISO datetime>  OR  **Skipped — override justification:** <text>

## Considered Moves
<Full considered-moves set with Catalogue IDs, theorist invocations, slash addressing.>

## Selected Moves
<Narrowed set after gates. Why these; why not the others.>

## Engaged Moves
<Moves actually executed. Status flips to `engaged`. Each engaged move gets a sub-block.>

### Move <N>: <Catalogue ID> — <Tactic Name>
- Engaged: <ISO datetime>
- Slash address: <string>
- Target actors: <links>
- Intended outcome: <string>

## Phase Log
<Append-only entries as track-and-detect signals come in. Perception shifts, resource shifts, classification.>
- <date>: <event>
...

## LSPI Operation Record (M)
<Append-only. The cycle's formal log: declarations and structural markers in lifecycle order (open, interest, detection, objective, intentions g_k, required-resources θ_k, gate results, executions ε_k, perceptions, selection, outcome, obtained utility, close, flowback — plus spawn/resume/moot/revision markers). Projected values carry ′ and are NEVER overwritten by realizations; supersession is additive (a revised objective appends the new body alongside the old, with a revision marker). This section maps to LSPI's M; the suspended-parent link and the Principal's resource holdings are S and R; the decision matrix Δ is a DERIVED VIEW — reconstruct it by replaying this record, never store it as mutable state. Markers come from the closed vocabulary in § "LSPI Configuration ⟨C; M; S; R⟩" below — do not invent marker forms (F10).>
- <date>: <marker or declaration, slash-addressed where applicable>
...

## σ / Guard Log
<Two kinds of judgment, logged separately (Pillar 4 vs Pillar 2):>

| Date | Kind | State | Admissible options | Operator's pick | Rationale |
|------|------|-------|--------------------|-----------------|-----------|
| <date> | σ (strategic) | <e.g., γ_1 declared, θ pending> | <e.g., declare γ_2 / resource γ_1 now> | <pick> | <why> |
| <date> | guard (interpretive) | <e.g., post-execution> | <perceive-validates / perceive-fails> | <reading of the realized world> | <evidence> |

<σ entries are sequencing choices (which admissible rule fires — includes the standing option "resource any pending intention now"). Guard entries are readings of the world (possession, perception-validation, premise-attested). Per-σ confluence (Theorem 13.6): with this log, the trace is reconstructable and deterministic.>

## Intention Positions
<Per-intention lifecycle position when K > 1 — each g_k tracks separately: declared → resourced (θ_k) → gated (∋/∌) → executed (ε_k) → perceived (validated / failed) → or mooted (intention-scoped: the cycle continues on remaining live intentions; requires ≥ 1 live intention remaining) . One line per g_k, updated as it advances.>
- g_1: <position>
- g_2: <position>

## Refinement
<What OPC sections updated; what Principal funnel sharpening occurred; reciprocal updates pushed.>

## Lessons
<What worked; what didn't; what to carry into next cycle. Status flips to `closed`.>

## Cross-References
- Sphere / Campaign / Principal: <links>
- Actors touched: <links>
- Prior cycle: <link>
```

## LSPI Configuration ⟨C; M; S; R⟩ (v1.2+, optional)

Where the four LSPI configuration slots live in a PLC cycle file. Pre-1.2 cycles carry none of this and remain valid; a v1.2+ cycle running the formal spine populates all four. Rules: `_plc-engine/09-LSPI-RULES.md`; persistence discipline: `06-STATE-PERSISTENCE.md`.

| Slot | What it is | Where it lives in PLC |
|------|------------|-----------------------|
| **C** | **Active-cycle pointer.** A number identifying the cycle currently holding control. Advances on open (`R-open`) and on spawn (`R-spawn`); **decreases on resume** (`R-resume`) when control returns to a suspended parent | `plc_Cycle_Number`, read as the *active* pointer — not as a sequence index |
| **M** | **Operation record.** The append-only log of declarations and structural markers | This file's own `## LSPI Operation Record (M)` body section |
| **S** | **Suspended-parent stack.** Entries `⟨parent-C, parent-pending-q, parent-prefix⟩`, pushed by `R-spawn` at a gate-fail, popped by `R-resume` when the sub-cycle delivers the parent's `q` | `plc_Suspended_Parent` (this cycle's entry) + `plc_Spawned_Subcycles` (the reciprocal); the stack itself is reconstructed from the spawn/resume markers in M |
| **R** | **Resource multiset.** What the principal currently holds | Pointer to the Principal file's `### Current Resource Holdings` — see `PLC_Principal.md`. Never copied here; a cycle reads and deducts, it does not own R |

**C is not monotonic.** Because `R-resume` decreases it, C alone cannot identify a cycle. **Cycle identity is carried by the `⟨open, C⟩` markers** — a cycle's identity is the C-value at its own open marker, and it persists across suspension and resumption. In a chain of escalations, M's entries interleave across cycles; each cycle's event sequence is recovered by filtering M for that cycle's identity.

**Δ is a derived view (restated — this is the rule most often broken).** The decision matrix Δ is a **fold over M**, reconstructed by replay to any point in the cycle. It is **never stored** as an editable block. The same holds for S and R: they are runtime views whose triggering events (`⟨gate-fail, q⟩`, `⟨flowback-recorded, E⟩`) persist in M as the source of truth.

### Structural-marker vocabulary (M, v1.2+)

The **closed canonical set**. If an event you want to record has no marker here, it has no marker — write it as a Phase Log entry in plain English and flag it, rather than inventing a form (F10, generation half).

| Marker | Records |
|--------|---------|
| `⟨open, C⟩` | A cycle opened; **carries that cycle's identity** |
| `⟨gate-pass, q⟩` | The capability gate passed on required resource `q` |
| `⟨gate-fail, q⟩` | The gate failed on `q` (`∌`) — the escalation trigger |
| `⟨select-staged, σ⟩` | `R-select` staged the matrix selection; ends the per-intention phase |
| `⟨close, C⟩` | Cycle closed on the normal path |
| `⟨close-nested, sub-C, parent-C⟩` | A sub-cycle closed and its earnings flowed to the principal's holdings |
| `⟨flowback-recorded, E⟩` | Obtained resources `E` recorded at flowback |
| `⟨resume, parent-C, q⟩` | Control returned to the suspended parent, which now holds `q` |
| `⟨perceive, g_k⟩` | Per-intention perception validated (per-intention / Rusty pattern) |
| `⟨perceive, C⟩` | Cycle-level perception validated (cycle-shared / Nathan pattern) |
| `⟨perceive-failure, g_k⟩` | Per-intention perception failed |
| `⟨perceive-failure, C⟩` | Cycle-level perception failed |
| `⟨moot, C⟩` | Cycle-scoped moot — the whole cycle's premise went void (terminal) |
| `⟨moot, C, g_k⟩` | Intention-scoped moot — `g_k`'s purpose is void; the cycle continues on its remaining live intentions (requires ≥ 1 remaining) |
| `⟨abandon, C⟩` | The principal elected to stop (terminal) |
| `⟨objective-revised, C, ι, old ↦ new⟩` | Non-destructive objective revision; the old body is retained alongside the new |

**Typing note — do not parse markers as terms.** Markers are **audit-trail meta-entries, not LSPI terms**. They are **not subject to the Layer-2 type system** and must never be fed to the five-layer validation ladder in `04-SCHEMA.md` as if they were declarations: the ladder's parse and type-check layers would reject every one of them as an **F10 violation**. Declarations (ι, δ, ω, γ, θ, ε, Γ, Σ, Ω, Λ, Φ bodies) are validated; markers are read.

**Tagging note.** Each entry is tagged with the **cycle-identity it semantically records**, not with whatever C happened to be active when it was written. The three C-transitioning rules fix this per entry: `R-spawn` writes `⟨gate-fail, q⟩` tagged with the failing **parent** and `⟨open, C+1⟩` tagged with the new **sub-cycle**; `R-resume` writes `⟨resume, parent-C, q⟩` tagged with the resumed **parent**; `R-abandon` writes `⟨abandon, C⟩` tagged with the **abandoned** cycle. Without this discipline, filter-by-identity over M is ambiguous at every escalation boundary.

## Intention-terminality check before Outcome (v1.2+)

**No cycle may proceed to Outcome / Selection while any live intention is non-terminal.** This is `R-select`'s universal premise (`∀ live g_k`), and without a check at the operator's level it is possible to close a cycle with an unresolved intention — the audit trail then shows an execution whose effect was never read.

Terminal positions, per intention:

| Position | Terminal? | Pattern |
|----------|-----------|---------|
| `perceived` | yes | per-intention perceive fired (`⟨perceive, g_k⟩`) |
| `executed` **with** a cycle-level perceive present (`⟨perceive, C⟩` ∈ M) | yes | cycle-shared perceive (Nathan pattern) |
| `mooted` | yes | `⟨moot, C, g_k⟩` written; the intention is retired, not resolved |
| `executed` **without** any recorded perceive | **no — blocks** | the common failure: the move was made, the world was never read |
| `declared` / `resourced` / `gated` | no | the intention never reached execution |

**The check.** Before the cycle's outcome handoff — the `⟨select-staged, σ⟩` entry in the Operation Record, and the `## Refinement` / `## Lessons` sections that follow it — walk `## Intention Positions` and confirm every live `g_k` sits at one of the three terminal positions. (LSPI's Σ selection is this close-phase handoff, not the earlier gate-driven `## Selected Moves` narrowing; the two are different steps and this check keys off the former.) If any sits at `executed` with no `⟨perceive, g_k⟩` and no cycle-level `⟨perceive, C⟩`, the cycle **blocks**: fire the perceive (validating or failing), or moot the intention, before proceeding. A blocked cycle is not an error — it is the operator's judgment being required (Pillar 2).

## Relation slots

| Direction | Relation | Target Type | Cardinality |
|-----------|----------|------------------|-------------|
| Out | `plc_Sphere` | PLC_Sphere_Manifest | 1 |
| Out | `plc_Campaign` | PLC_Campaign | 0..1 |
| Out | `plc_Principal_Owner` | PLC_Principal | 1 |
| Out | `plc_Actor_Touched` | PLC_Actor | 1..N |
| Out | `plc_Tactic_IDs_Selected` | PLC_Tactic | 0..N |
| Out | `plc_Theorists_Invoked` | PLC_Theorist | 0..N |
| Out | `plc_Strategy_Number_Selected` | PLC_Strategy | 0..1 |
| In | `plc_Last_Updated_Cycle` (from Actor) | PLC_Actor | 1..N |

## Reciprocal-update discipline

- Every Actor in `plc_Actor_Touched` has its `plc_Last_Updated_Cycle` pointed here.
- Every Tactic in `plc_Tactic_IDs_Selected` has its `plc_Cited_In_Cycles` updated to include this cycle ID.
- Every Theorist in `plc_Theorists_Invoked` has its `plc_Invoked_In_Cycles` updated.
- When status transitions to `closed`, the parent Campaign's `plc_Active_Cycles` loses this cycle.
- When status transitions to `engaged`, perception/resource detection writes back to each Actor file's `## Perception History` / `## Resource History`.

## Gate discipline (Gates 1 + 2)

Per D9 + P7:

- **Both gates MUST complete** before any move from `plc_Tactic_IDs_Considered` enters `plc_Tactic_IDs_Selected`.
- **Skipping a gate is permitted** but requires explicit operator override.
- **Override format:** `<gate-name>:<one-line justification>` appended to `plc_Accounting_Overrides`.
- **Silent skipping is F8** (per `05-WRITING-FOR-AI.md`). The session-close protocol checks for completion timestamps; if absent, prompts for override justification.

### Capability gate (LSPI, v1.2+)

- **One q per gate test.** Do not declare a single gate test over multiple required resources — multi-q conjunction gate semantics are an open defect upstream (LSPI §11.4.7, Axis 6). An intention needing several resources declares separate gate tests, one per q.
- The binary possession check (`∋`/`∌`) is retained; the **augmented gate** (sufficiency + inclusion + affordability over the intended plan) layers above it — see `03-SESSION-PROTOCOL.md` RUN-CYCLE and `08-ESTIMATION.md`.
- Gate-fail (`∌`) spawns a sub-cycle targeting the missing q: set the sub-cycle's `plc_Suspended_Parent`, append to this cycle's `plc_Spawned_Subcycles`, and record spawn/resume markers in the Operation Record. On sub-cycle close, obtained resources flow back to the Principal's holdings (resource conservation, Theorem 13.4 — no leaks, no duplications). Sibling sub-cycles do not run simultaneously; spawn order is a σ-choice (log it).

## Cycle status state machine

| From | To | Trigger |
|------|-----|---------|
| (new) | `planning` | Cycle file created at RUN-CYCLE start |
| `planning` | `active` | Agenda + Landscape + OPC + Funnel body sections populated |
| `active` | `engaged` | First move engaged (Engaged Moves body section populated) |
| `engaged` | `closed` | Cycle close — lessons captured; outcome resolved (post-Obtained-Resource reflection) |
| `planning \| active \| engaged` | `mooted` (v1.2+) | **`R-moot` fires** — the cycle's premise went void (the preferred position became unreachable, the target left the matrix), or a perceive-failure was resolved by mooting rather than by a new intention. The cycle gained no resources; R unchanged. Record `⟨moot, C⟩` in the Operation Record |
| **any state** | `abandoned` (v1.2+) | **`R-abandon` fires** — the principal elects to stop. Admissible from **any** state; do not narrow this premise (see note below). Record `⟨abandon, C⟩` in the Operation Record |
| `closed \| mooted \| abandoned` | `e_immutable` | Operator confirms seal after grace window (default 7 days) |

`planning` and `active` are revisable freely. `engaged` is revisable but Phase Log is append-only. `closed` is revisable for grace-window-length. `e_immutable` is sealed forever.

**`mooted` and `abandoned` (v1.2+).** Both are **terminal** — no lifecycle transition leaves them; the only onward move is the durability seal to `e_immutable`. **Neither produces a flowback**: no `Φ` obtained-resources body, no `⟨flowback-recorded, E⟩`, no addition to the Principal's holdings. A mooted or abandoned *sub-cycle* therefore does not satisfy its parent's pending `q` — the parent must escalate again against a **fresh** intention, moot, or abandon in turn; it may not re-spawn against the same `g_k`.

**The "any state" premise on `R-abandon` is load-bearing.** It is the universal escape hatch and the progress mechanism underwriting LSPI's termination theorem (13.5). Narrowing it here — restricting abandonment to, say, post-gate or post-perceive states — would re-open that proof. Leave it universal. Rule statements: `_plc-engine/09-LSPI-RULES.md` (`R-moot`, `R-moot-intention`, `R-abandon`).

## Worked example (abbreviated frontmatter)

```markdown
---
type: PLC_Cycle
timestamp: "2026-06-10T00:00:00Z"
Item_ID: cycle-0007
title: "Cycle 0007 — Q2 mandate signal preservation"
Date_Added: 2026-05-22
Date_Modified: 2026-06-10
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Campaign: "[[campaign-succession-q3]]"
plc_Principal_Owner: "[[principal-sam-ceo]]"
plc_Cycle_Number: 7
plc_Cycle_Status: closed
plc_Update_Mode: D
plc_Started_Date: 2026-05-22
plc_Closed_Date: 2026-06-10
plc_Sealed_Date: ""
plc_Actor_Touched:
  - "[[actor-carol-cfo]]"
  - "[[actor-robert-board-chair]]"
  - "[[actor-elena-independent-director]]"
plc_Slash_Constituents:
  # keyed by owning actor (Theorem 13.1); paths are pure System 1 — no OPC or Catalogue IDs (F9)
  - "Sam: [Α/i.1/t./D./P.]"
  - "Sam: [Α/i.1/d.]"
plc_OPC_Diagnostic_Refs:
  - "1.2"
  - "13.1.1"
  - "13.3.2"
plc_Tactic_IDs_Considered: ["0210", "0380", "0392", "0393"]
plc_Tactic_IDs_Selected: ["0210", "0392"]
plc_Strategy_Number_Selected: 15
plc_Clusters_Engaged: ["C03", "C09"]
plc_Theorists_Invoked:
  - "[[theorist-schelling]]"
  - "[[theorist-goffman]]"
plc_Alternatives_Audit_Completed_At: "2026-05-25T10:30:00"
plc_Ethical_Accounting_Completed_At: "2026-05-25T11:15:00"
plc_Accounting_Overrides: []
AI_Instructions: ""
---
```

(Full body would include all 14-constituent sections — abbreviated here for the type definition.)

## Anti-patterns

- **F8 — Silent gate skip.** Treating ALTERNATIVES-AUDIT or ETHICAL-ACCOUNTING as optional without override justification. The empty timestamps must be explained.
- **F9 — Reference system conflation.** Mixing slash addressing, OPC IDs, and Catalogue IDs in the same field. Keep them in their native frontmatter fields.
- **F5 — Asymmetric writeback.** Selecting a Tactic without updating the Tactic's `plc_Cited_In_Cycles`; touching an Actor without updating its `plc_Last_Updated_Cycle`. The graph corrupts silently.
- **Closing over an unresolved intention (v1.2+).** Proceeding to Outcome while a live `g_k` sits at `executed` with no recorded perceive. Terminal is `perceived | executed-with-cycle-level-perceive | mooted` — nothing else. See § Intention-terminality check.
- **Inventing a marker (v1.2+).** Writing a plausible-looking `⟨…⟩` form that is not in the closed vocabulary, or feeding a marker to the type checker as if it were a term. Both are F10.
- **Premature seal.** Flipping to `e_immutable` before the 7-day grace window. The operator may need to refine lessons.
- **Editing a sealed cycle.** Once Mode E, never edit. Corrections go in a follow-up Cycle's Agenda referencing the prior cycle.
- **Skipping `## Phase Log` discipline.** During `engaged`, every material signal (perception shift, resource shift, outcome confirmation) appends an entry. Without the log, ANALYZE-CYCLE has nothing to read.
