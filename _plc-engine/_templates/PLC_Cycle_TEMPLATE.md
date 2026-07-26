---
type: PLC_Cycle
Item_ID: cycle-<NNNN>
title: "Cycle <NNNN> — <one-line agenda summary>"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Campaign: ""   # "[[campaign-<slug>]]" or empty for sphere-direct cycle
plc_Principal_Owner: "[[principal-<slug>]]"
plc_Cycle_Number: <integer>
plc_Cycle_Status: planning   # planning | active | engaged | closed | mooted | abandoned | e_immutable  (mooted, abandoned: v1.2+; see 09-LSPI-RULES.md)
plc_Update_Mode: D   # D | E — flips to E only when status: e_immutable
plc_Started_Date: <YYYY-MM-DD>
plc_Closed_Date: ""
plc_Sealed_Date: ""
plc_Actor_Touched: []
plc_Slash_Constituents: []   # System 1 — "<owning-actor>: [<path>]"; pure LSPI, no OPC/Catalogue IDs (F9); keyed per-actor (Thm 13.1)
plc_OPC_Diagnostic_Refs: []   # System 2: OPC hierarchical IDs (e.g., "13.1.1")
plc_Tactic_IDs_Considered: []   # System 3: Catalogue IDs (e.g., "0029")
plc_Tactic_IDs_Selected: []
plc_Strategy_Number_Selected: 0   # 1-16 or 0 if none
plc_Clusters_Engaged: []   # e.g., ["C12", "C44"]
plc_Theorists_Invoked: []
plc_Alternatives_Audit_Completed_At: ""   # ISO datetime or empty if skipped (then log override)
plc_Ethical_Accounting_Completed_At: ""   # ISO datetime or empty if skipped
plc_Accounting_Overrides: []   # ["<gate>:<justification>"]
# --- Optional LSPI fields (v1.2+; all optional, pre-1.2 cycles valid without them) ---
plc_Strategic_Stance: ""   # adaptive | pre_committed_resource_careful | pre_committed_resource_batched (choose at first multi-intention moment)
plc_Stance_Rationale: ""
plc_Probe_Budget_Remaining: 0   # per-cycle probe budget; decrement per probe (see 08-ESTIMATION)
plc_Detection_Record_Refs: []   # [[detection-<actor-slug>]]
plc_Suspended_Parent: ""   # parent cycle link if spawned by a gate-fail (∌)
plc_Spawned_Subcycles: []
AI_Instructions: ""
---

# Cycle <NNNN> — <one-line agenda summary>

## Agenda
<The principal's articulated agenda for this cycle. ADAPT "A" beat. One paragraph.>

## Landscape Assessment
<Current sphere read going into the cycle. Citations to OPC IDs and Actor files.>

## OPC Self-Diagnosis
<Where the principal stands across the OPC sections most material to this agenda.>

## Principal Funnel
<The funnel narrowed for this specific cycle. Decision criteria.>

## Augmented Gate (v1.2+; over the intended plan Π — see 08-ESTIMATION)
<Plan members with per-member worth-vs-cost (inclusion), plan-level sufficiency judgment against the estimated margin (with risk allowance), affordability judgment against the interest's value. One q per possession test. Chosen route if not passing: acquire / abandon / rescope / re-probe.>

- **Possession (∋/∌):** <the retained binary capability gate, beneath the augmented tests. One line per required resource, one q per test (LSPI §11.4.7): `[a./R.] ∋ <q>`? y/n. Any ∌ spawns a sub-cycle for that q.>

| Plan member (resource) | Effect (cells, sign) | Cost | Worth given rest of plan | Clears inclusion? |
|------------------------|----------------------|------|--------------------------|-------------------|
| <r1> | <e.g., Adv/c ↑> | <cost> | <marginal contribution> | <y/n> |

- **Sufficiency:** <expected to close margin? evidence + risk note>
- **Affordability:** <Σ cost vs prize>
- **Verdict:** PASS / acquire <q> / rescope / re-probe (VoI rationale, budget remaining: <n>) / abandon <the route that ends the cycle; admissible from any state>
- **P13 note:** the sufficiency/worth judgments above are uncalibrated scaffolding — verdict is a proposal under the operator's stated reads; if the operator's gut disagrees with the margin estimate, that disagreement is probe material, not noise>

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
<Status flips to `engaged` when first move executes.>

### Move 1: <Catalogue ID> — <Tactic Name>
- Engaged: <ISO datetime>
- Slash address: <string>
- Target actors: <links>
- Intended outcome: <string>

## LSPI Configuration ⟨C; M; S; R⟩ (v1.2+, optional)
<The cycle's formal configuration (see `09-LSPI-RULES.md`). Pointers only — nothing here is a second source of truth.>

- **C — active cycle:** <this cycle, or the running sub-cycle if one is open>. **Not monotonic** — C decreases on resume (sub-cycle closes, parent resumes at its gate).
- **M — operation record:** `## LSPI Operation Record (M)` below (append-only; projections primed, never overwritten).
- **S — suspended-parent stack:** <`plc_Suspended_Parent` chain, outermost first — or "empty (top-level cycle)">.
- **R — resource holdings:** [[principal-<slug>]] → `### Current Resource Holdings` (the multiset; executions deduct once, flowbacks append once — Thm 13.4).

<Δ (the decision matrix) is a DERIVED fold over M — replay the record to reconstruct it; never store it as state.>

## LSPI Operation Record (M)
<Append-only formal log: declarations and markers in lifecycle order (open, interest, detection, objective, γ_k, θ_k, gate results, ε_k, perceptions, selection, outcome, obtained utility, close, flowback; plus spawn/resume/moot/revision markers). Projected values carry ′ and are never overwritten. Δ is a derived view — replay this record, never store a mutable matrix. One q per gate test (LSPI §11.4.7 constraint).>
- <date>: <marker or declaration>

## σ / Guard Log
| Date | Kind | State | Admissible options | Pick | Rationale |
|------|------|-------|--------------------|------|-----------|
| <date> | σ | <state> | <options> | <pick> | <why> |
<σ = strategic sequencing choice (Pillar 4, incl. the standing "resource a pending intention now" option). guard = interpretive world-reading (Pillar 2: possession, perception-validation, premise-attested).>

## Intention Positions
<Per-intention position when K > 1: declared → resourced → gated → executed → perceived / mooted (intention-scoped moot requires ≥ 1 live intention remaining).>
- g_1: <position>

## Phase Log
<Append-only entries as track-and-detect signals come in.>

- <date>: <event>

## Refinement
<What OPC sections updated; what Principal funnel sharpening occurred; reciprocal updates pushed.>

## Lessons
<What worked; what didn't; what to carry into next cycle. Status flips to `closed`.>

## Cross-References
- Sphere: <link>
- Campaign: <link>
- Principal: <link>
- Actors touched: <links>
- Prior cycle: <link>
