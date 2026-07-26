---
Item_ID: plc-changelog
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Political Landscape Cartography — Changelog"
Date_Added: 2026-06-13
Date_Modified: 2026-07-24
Needs_Processing: false
AI_Instructions: ""
---

# Political Landscape Cartography — Changelog

All notable changes to PLC are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/) conventions with PLC-specific section conventions added:

- **Added** — new Prototypes, Templates, scaffolding, Catalogue extensions, patterns, principles, session activities, framework references
- **Changed** — modifications to existing engine prose, framework content, scaffolding, or Catalogue entries
- **Deprecated** — features still present but slated for removal in a future major
- **Removed** — features deleted (always a major bump)
- **Fixed** — typo / clarification / formatting corrections
- **Security** — any change to redaction profiles, gate semantics, or boundary-of-disclosure discipline
- **BREAKING** — any change that breaks installed sphere cartridges (always a major bump; requires `MIGRATION-v<x>-to-v<y>.md`)
- **Migration notes** — for minor or major bumps, what existing cartridges need to do

PLC follows semantic versioning. See `CONTRIBUTING.md` § "In-scope vs major-version-bump scope" for the categorization rules.

---

## [1.2.0] — 2026-07-24 (LSPI Formal Foundation integration)

The integration of substrate authority 5 into the volume, completed in two passes. The first (2026-07-02) landed the framing, the estimation layer, the Types, and the mechanical half of the catalogue binding. The second (2026-07-24) completed the interpretive catalogue passes, closed the formal layers that had been named but not built, propagated every Type-level addition into the templates and the worked example, and reconciled the volume's internal counts. Both passes are recorded below; the correction log at the end of this entry states the defects the second pass found and fixed, per `CONTRIBUTING.md` § correction-log discipline.

### Added (second pass, 2026-07-24)

- **New engine chapter `_plc-engine/09-LSPI-RULES.md` — the rule catalogue and state machine.** All 21 transition rules across the three families plus the two non-firing disciplines, each with trigger, premises, writes, and configuration effect; the derived views their premises read (`last`, `IntentionPosition`, `PendingTheta`, live/declared/mooted intention sets, `CyclePattern`, `q_of`); the nine lifecycle positions; **the per-state admissibility table**; the σ-fork vs interpretive-guard classification with the three standing options; the WF-1…WF-6 well-formedness conditions termination is conditional on; the meta-theorem-to-practice map; the known-unsound register; and the five worked cases as ground truth. This closes the gap where `03-SESSION-PROTOCOL.md` instructed the AI to "name the admissible next steps" with no table to name them from. Engine chapters: 9 → **10**.
- **Layer 2 (type system) and Layer 3 (congruence) in `04-SCHEMA.md`.** The five-layer validation ladder previously named a type-check and a congruence-check with nothing to check against. Added: the child-class lattice (including the `intention → interest` row that licenses escalation, and the reason `a/a` needs no separate rule); the prefix-admissibility table (actor-only / target-only / systemic, and why a wrong prefix is a type error rather than a style slip); argument-sort compatibility and root anchoring; the disambiguation of the two `→` and two `=` senses; and the three congruence generators (**A2** slash associativity — previously absent entirely, **D5** set-order irrelevance, **M4** root glyph) with the normalize-then-compare procedure and the three refusals (no unfolding during comparison; never equate primed with unprimed; the perception `=` is not symmetric).
- **Relation family 13 — the defense graph** (`countered-by ↔ counters`), machine-derived from the catalogue's Resolution-Approach prose. Named relations: 25 → **27**; families: 12 → **13**.
- **`plc_Cycle_Status` gains `mooted` and `abandoned`.** Both `R-moot` and `R-abandon` were specified in the protocol and unrecordable in the schema — an abandoned cycle could only sit at `engaged` forever or be falsely closed. Since `R-abandon` is the escape hatch LSPI's termination result rests on, a cycle status that cannot express it made the volume's central liveness property unauditable. Both statuses are terminal and produce no flowback.
- **The `⟨C; M; S; R⟩` configuration** now has a defined home (`_types/PLC_Cycle.md` § LSPI Configuration, scaffolded in the Cycle template). `04-SCHEMA.md` had referenced an `lspi_configuration` construct that existed nowhere; the four slots were tracked across unconnected fields, and the active-cycle pointer C was never mapped at all. Includes the non-monotonicity note (C decreases on resume, so it is not a cycle ID).
- **The structural-marker vocabulary** — the closed 16-marker set, with the typing rule that **markers are not LSPI terms** and must not be run down the validation ladder. Without this, every marker in an operation record was a spurious F10 rejection waiting to happen.
- **Intention-terminality check before Outcome** — no cycle proceeds to selection while a live intention sits at `executed` with no recorded perceive. This is `R-select`'s universal premise given a surface.
- **Two session templates that were referenced but did not exist:** `PLC_Session_SPHERE_OPEN_TEMPLATE.md` and `PLC_Session_SPHERE_CLOSE_TEMPLATE.md`. Templates: 23 → **25**.
- **Three upstream specs mirrored** into `_frameworks/lspi/` (Mode C): `Tactic-Corpus-LSPI-Integration-Spec.md` — the binding contract the catalogue integration implements, which the volume had been satisfying without shipping; `Content-Audit-v0.3.md` — the correction-log exemplar `CONTRIBUTING.md` names; `Resource-Detection-Slot-Analysis.md`.
- **WS4 passes 3–6 complete (the interpretive catalogue binding).** All 782 tactic records now carry `required_resources` (against the nine carriers, role `enabling`/`consumed`), `detectability` (level + the observable tell), `certainty_class`, and `ethical_valence` (axes + severity). The defense graph carries 174 links across 152 records with 70 derived reciprocals. Provenance covers 606 records and **127 of the 148** Table-3 manifest rows. All values are **P10 proposals pending operator QA**, not measurements. Facet vocabularies are declared in the sidecar and validated.
- **The ε-template is now spec-conformant.** The upstream spec defines a three-place tuple ⟨Δ, θ, meta⟩; the shipped template was Δ-only, with θ structurally absent and `_types/PLC_Tactic.md` nonetheless calling the remainder "the typed ε-form." Records now emit `[a.] ε_<ID>(<addr>/e.) → { deltas } consuming { θ }`, with `epsilon_tuple` carrying Δ/θ/meta structurally. Records with no required-resources emit the delta-only variant — θ unknown, not empty.
- **Six new Section 10 regression checks** in `07-SHIPPING-CHECKLIST.md`: correction-log presence on any release carrying formal-content change; marker-typing; **claimed-writeback** (every reciprocal a session log claims to have written actually exists on the other side); abandon/moot recordability with the abandon premise unnarrowed; carrier-openness; and catalogue facet coverage with vocabulary validation.
- **`R-unfold` given a concrete discipline** in `06-STATE-PERSISTENCE.md` — bind, unfold one-way, never re-fold, later references cite the binding entry. It was the one Persistence Invariant commitment with no surface.
- **An `N_probe` rule** in `08-ESTIMATION.md`. The termination claim rested on the probe budget and nothing said how to set it; the worked example set 4 by fiat. A budget chosen by feel is termination-by-fiat, and the chapter now says so.
- **A correction-log location and shape** in `CONTRIBUTING.md`, plus an issue-template field. The discipline was defined with nowhere for logs to live.

### Changed (second pass)

- `_plc-engine/03-SESSION-PROTOCOL.md` — every constituent in the cycle walk now names the rule(s) that fire there and cites `09-LSPI-RULES.md` for their premises; the dense 21-rule paragraph is replaced by a pointer; `R-moot` and `R-abandon` routes added to the control flow with the distinction stated (moot is the world removing the question; abandon is the operator answering it); the gate returns five verdicts, `abandon` included.
- `_plc-engine/08-ESTIMATION.md` — calibration flags (e) myopic VoI, (f) risk allowance and depth-loss weights, and additivity are now flagged **at their points of use** rather than only in a closing list, per the chapter's own rule.
- `_frameworks/reflexivity-frontier.md` — depth converted from the retired symbol `k` to `ℓ`; the game object (players, actor type, target signaling strategy, payoff structure) and the oracle/σ linkage added; still `frontier: true`, still non-operational.
- `ROADMAP.md` — idea #4's status divergence from upstream recorded rather than silently resolved; #7 restated as data-landed rather than schema-landed; the ranking substitution (#3 for #4 in the next-spin-off pair) made visible; the absorbed / do-not-re-mine list carried; the provenance coverage finding and the missing-source gaps recorded.
- Volume-wide count reconciliation: 17 Types, 13 relation families / 27 named relations, 16 activities, 25 templates, 10 engine chapters, 11 failure modes (F1–F11 plus F4b), 11 shipping-checklist sections, 148 Table-3 rows, next principle P14.

### Fixed (second pass) — correction log

Per `CONTRIBUTING.md` § correction-log discipline: *(i)* the defect, *(ii)* why it is wrong, *(iii)* the fix.

1. **M3 re-installed in the coaching layer.** `_frameworks/4R.md` asserted the strategic edge is "operating one level above the opponent's actual depth" and attributed it to `08-ESTIMATION.md`. *(ii)* That is the unconditional +1 bias the upstream Content Audit repaired as finding M3; the chapter actually specifies `ℓ̂_T + b` with `b ∈ [0,1]` calibrated to OPC-measured adversarial intensity. The anti-paranoia ship test checks AI behaviour, not the framework corpus, so this contradicted the chapter while passing the gate — and 4R is the principal-facing layer, where manufactured paranoia does the most damage. *(iii)* Restated as the calibrated rule with both failure directions named.
2. **Termination overclaimed.** `08-ESTIMATION.md` said v0.4 "proves" the estimation loop terminates. *(ii)* Upstream describes that argument as a sketch at the rigor of LSPI's own measure arguments, explicitly not machine-checked — and it sat one paragraph from six genuinely machine-grade meta-theorems, so a reader would inherit the wrong warrant. *(iii)* Restated honestly, with the distinction from the six theorems made explicit.
3. **A closed enum standing in for a non-exhaustive basis.** `plc_Resources_Held` was a closed nine-value list while both the chapter and the Type's own note called the nine a non-exhaustive basis of carriers. *(ii)* The primary definition of a resource is intensional; a genuine resource outside the nine had nowhere to be recorded, so the definition could be discussed but not used. *(iii)* `other` added, requiring a note naming the carrier.
4. **Claimed writebacks that never happened, inside the regression canary.** Three files in the Acme sphere recorded reciprocal updates to the Actor and Principal files that were never applied. *(ii)* This is a live F5 (asymmetric graph) in the artifact the shipping checklist designates as the F-code regression substrate — and it was on the exact relation family v1.2 added. *(iii)* The writes were performed; a shipping check now tests for the class.
5. **The depth-bias evidence chain terminated in nothing.** The worked Detection Record justified `b = 0.5` by citing an OPC section that contained no intensity reading. *(iii)* A real political-intensity reading was added to the diagnostic and the citation re-pointed.
6. **The F10 exemplar was itself ill-typed.** The worked cycle wrote a matrix operation with the matrix in argument position and no target prefix — two violations of rules the schema chapter states correctly — in the file the AI is told to copy patterns from. *(iii)* Repaired in place with the violation cited; the sphere was swept for others.
7. **Pass numbering off by one.** `_types/PLC_Tactic.md` numbered the WS4 facet passes one lower than the runbook, labelling a facet "pending (pass 2)" while marking pass 2's own deliverables complete. *(iii)* Renumbered to the runbook/spec numbering, which `_UPGRADE-STATUS.md` and the sidecar's own status string already used.
8. **Extraction-script defects.** The lever extractor silently dropped tactic `0028` from its exception log (every lever heading marked "Not active" produced zero levers with no report), double-counted lever cells for two tactics with multiple lever blocks, consulted only the generic strategy in its fallback, and carried a status guard that would have reverted completed facet batches to "pending" on the next run. *(iii)* All four fixed; idempotency re-verified byte-for-byte across two runs.
9. **Dangling paths.** `_plc-engine/_meta/` (cited five times as a load location), `_plc-engine/redaction-profiles/` (the real path is under `_yaml/`), legacy `TEMPLATE-*.md` session-template names, and an example-sphere location at the volume root rather than under `Spheres/`. *(iii)* All re-pointed to real homes; the missing directories were **not** created, since their content already had homes.
10. **Checks that pass a human eye and fail on disk.** Section 3 of the shipping checklist required four canonical sources, sixteen strategy atom files, and the LSPI figures, none of which are present. *(iii)* Rewritten to test what the volume actually ships, with the remainder carried as named gaps in `ROADMAP.md`.

### Migration notes

Existing v1.1 sphere cartridges load unchanged. Every addition is optional: new Type fields, new body sections, the two new cycle statuses, and the `other` carrier are all additive. Pre-1.2 cycles remain valid and need no backfill. Operators may adopt the augmented gate mid-engagement by adding the gate block to open cycles only. The one thing worth doing deliberately: declare the WF-1…WF-6 bounds for the engagement (see `09-LSPI-RULES.md` § Termination) — an engagement with no declared bounds is not unbounded in practice, it is one whose termination argument has not been made.

---

### First pass — 2026-07-02

*The workstreams below landed in the first pass and are carried here as the release's full record.*

### Added
- **Fifth substrate authority: LSPI Formal Foundation.** New `_frameworks/lspi/` with Mode C mirrors of `LSPI-Foundations.md` (typed DSL + small-step operational semantics + six meta-theorems), `Matrix-Estimation-Layer-v0.4.md` (estimator / depth decoder / actuator / augmented gate / termination proof), `Reflexivity-Layer-v0.1.md` (`frontier: true` — research scaffold, non-operational), Figures 3–4, and `_lspi-README.md` (orientation: meta-theorems, Pillar 2/Pillar 4, strategic stances, worked-case ground-truth table, precedence rules, known-unsound areas incl. the §11.4.7 multi-q gate defect, external dependencies incl. the visibility/permissions model).
- **New engine chapter `_plc-engine/08-ESTIMATION.md`** — the Matrix-Estimation Layer operationalized: detection loop (differential → VoI-selected probes with pre-registered predictions → update → stop rule), probe budget, depth decoder with loss-calibrated bias `b` from OPC political-intensity, actuator (intensional resource definition primary; nine types demoted to carriers; contextual worth; convertibility; gain-cycle compounding; protection), the seam (detection = price discovery), the augmented gate, the integrated loop, defensibility capstone, calibration flags.
- **17th Type: `PLC_Detection_Record`** (`_types/PLC_Detection_Record.md` + `_plc-engine/_templates/PLC_Detection_Record_TEMPLATE.md`) — Mode D; lives at `<Sphere>/Detection/`; new reciprocal relation `estimates ↔ estimated-by` (25 named relations).
- **16th session activity: `ESTIMATE`** — forward hypothesis-design loop against one target; decision-algorithm trigger added (gate re-probe route / active record with budget + threshold-adjacent uncertainty).
- **Two failure modes: F10** (silent coercion of malformed LSPI — layer-order validation, surface rejections with rule citation; the three lexer normalizations are the only licensed auto-corrections) and **F11** (executability claim — banned formulations; administer-and-record register). Quality checklists extended.
- **Augmented gate inside RUN-CYCLE constituent 9** — sufficiency + inclusion + affordability over the intended plan, layered above the retained binary possession check; failure routes (acquire / collective-PASS / abandon-or-rescope / re-probe); gate block scaffold in the Cycle template. One-q-per-gate-test constraint (upstream LSPI §11.4.7 open defect).
- **WS4 passes 1–2 (catalogue LSPI binding, mechanical):** new sidecar `_frameworks/political-warfare-catalogue/INDEX-lspi.json` — `lspi_levers` (signed, intensity-weighted deltas) + `epsilon_template` for 779/783 tactics (775 from Active Levers sections, 4 from strategy-combination fallback; exceptions 0014/0015/0031/0037 + 1 placeholder logged); alias map corpus X→P / Y→Adv embedded; facet fields schema-reserved. Catalogue README gains the LSPI-binding section. `_types/PLC_Tactic.md` gains the eight optional LSPI facet schemas. New `_frameworks/lspi/WS4-RUNBOOK.md` (repeatable procedure for passes 3–6 + the validated 0158 four-register round-trip anchor).
- **Table 3 manifest:** new `_frameworks/dissertation-table-3/Table-3-Manifest.md` — all **148** Table 3 rows transcribed from the source PDF with Option/Consideration/Effect and LSPI component mapping (note: 148 actual rows vs the "~100" v1.0 estimate); `_README.md` updated.
- **WS6-5 worked example (v1.2 machinery end-to-end):** Acme sphere gains `Detection/detection-robert-board-chair.md` (3-hypothesis differential, two pre-registered probes with observations and updates, loss-calibrated depth bias from OPC intensity, VoI stop decision, budget 2/4), `Cycles/cycle-0009.md` (adaptive stance; Operation Record; σ/Guard Log; Intention Positions; augmented-gate PASS on collective sufficiency — the Rusty pattern, no single member sufficient; one trust⇝access conversion; both PLC gates completed incl. a considered-and-rejected 0158 boundary case), sessions `010_ESTIMATE` + `011_RUN-CYCLE`, and sphere-state Open Estimation rollup.
- **QUARTERLY-AUDIT base steps 4–5**: forecast-calibration review (projected ′ vs realized) and belief-hygiene review (stale differentials; un-re-priced worth; resource-conservation eyeball per Theorem 13.4).
- **P13 — Numbers are scaffolding, not answers** (`02-PRINCIPLES.md`; 13th principle). Estimation-layer quantities are uncalibrated until a QUARTERLY-AUDIT calibration record exists: epistemic-status register mandatory ("working credence," "uncalibrated margin read," "ordinal"); directional conclusions only; gate verdicts are proposals; operator disagreement routes into the differential, never gets outranked by arithmetic; anti-patterns codified (number worship, precision laundering, gut-override-by-arithmetic, premature graduation). Enforcement hooks: 08-ESTIMATION calibration-flags section, Detection Record type anti-pattern + template AI_Instructions, Cycle template gate-block note, Audit Mode P13 checkbox, 05-WRITING-FOR-AI quality check, 00-START-HERE principle 13 + AI-BOOTSTRAP read list. Principle counts propagated volume-wide (12 → 13; CONTRIBUTING frozen-set and next-principle references updated to P14+).

- **Weak-operator hardening (assume the running AI infers nothing):** root `_UPGRADE-STATUS.md` marker (mandatory pre-flight read while present: never bump VERSION mid-upgrade; never remove newer features to reconcile stale docs; document-precedence ranking; completion checklist — deleting the file IS the release declaration) with Tier-0 checks added to `AI-BOOTSTRAP.md` + `00-START-HERE.md`. **F10 generation half** (never invent LSPI notation: copy a validated pattern or write plain English and flag; composing unseen operator combinations forbidden) + generation-discipline pointer in 04-SCHEMA System 1. **F4b worked-example quarantine** (the Acme sphere teaches FORMAT, never FACTS — no citing its content as data, base rates, defaults, or precedent) + in-situ marker in the example manifest's `AI_Instructions`. **Document-precedence rule** under F6 (CHANGELOG > engine > types > templates > front-door docs; report staleness, never silently harmonize, never resolve by deleting the newer feature). **Sphere-folder rule** in 06-STATE-PERSISTENCE (the existing sphere's structure wins; never create parallel folders). **Extraction script saved** at `_frameworks/political-warfare-catalogue/tools/extract-lspi-levers.py` (idempotent regeneration of INDEX-lspi.json, preserves interpretive facets — the pass-2 tooling no longer lives only in a chat session).

- `OPERATOR-GUIDE.md` — new § "What changed in v1.2 (the LSPI integration)" for operators upgrading from v1.1: beat-by-beat v1.1 vs v1.2 workflow comparison; all-additions-optional migration note; the two disciplines to internalize (P13; gut-disagreement-is-probe-material); learning path (08-ESTIMATION → worked example, formats-only per F4b). Daily-operations cadence table gains the ESTIMATE row and 5-part quarterly base; symptom → cause → fix table gains six v1.2 rows (P13 number-quoting, endless probing, M1 gate misfire, depth-bias miscalibration, F10 invented notation, F4b example bleed).

### Fixed
- **Sphere-path drift normalized:** `04-SCHEMA.md` (and 00-START-HERE / AI-BOOTSTRAP / 03-SESSION-PROTOCOL writability + protocol references) said `<Sphere>/Diagnostics/` and `<Sphere>/_PRINCIPALS/` while BOOTSTRAP-NEW-SPHERE, README's tree, and the shipped example use `OPC-Diagnostics/` and `Principals/` — a parallel-folder trap for literal-minded assistants. All engine references normalized to `OPC-Diagnostics/` and `Principals/`.
- Stale ship-time counts in front-door docs: README + CONTRIBUTING "16-type" → 17; CONTRIBUTING frozen-set counts (17 Types, 16 activities, P1–P13); UPDATE-PROMPT template count 22 → 23.

### Changed
- `_plc-engine/01-WHAT-IS-PLC.md` — four → five substrate authorities; Pillar 2 (boundary of computation) paragraph — LSPI is descriptive, never "political computation"; OV-as-cognitive-hierarchy-depth-amplifier positioning.
- `README.md` — Foundations section gains substrate 5.
- `AI-BOOTSTRAP.md` + `_plc-engine/00-START-HERE.md` — Tier 2 read entries for `_frameworks/lspi/`; layer-order validation pre-flight rule.
- `_plc-engine/04-SCHEMA.md` — System 1 section rewritten as the formal front half of LSPI: full 21-constituent table with Greek/Latin duality and case discipline; the four operator families + agent-attribution prefix dispatch; the three lexer normalizations (Α/A, Θ/Φ/Λ, `t.`-insertion); per-actor uniqueness and owning-actor+path keying (Thm 13.1); five-layer validation ladder; P/Adv option-role vocabulary with the corpus X/Y alias map; precedence rules (engine wins sphere-level, treatise wins LSPI-internal). 16 → 17 Types; 24 → 25 relations; folder structure gains `Detection/`.
- `_plc-engine/03-SESSION-PROTOCOL.md` — new § "The LSPI formal spine" in RUN-CYCLE (21 rules; state-by-state one-question walk; σ-forks vs guards; standing option; three strategic stances; perceive-failure continuations; spawn/resume discipline; close with prime persistence); constituent 9 rewritten (two-layer gate); OPC-DIAGNOSE note (§4.3/§9 as estimation inputs; political intensity calibrates b); UNCOVER→ESTIMATE hand-off; 15 → 16 activities.
- `_plc-engine/05-WRITING-FOR-AI.md` — LSPI notation discipline convention (prime; P/Adv; per-actor keying); F10/F11; quality checks extended.
- `_plc-engine/06-STATE-PERSISTENCE.md` — Persistence Invariant section (M append-only; three commitments: prime-preserve / non-destructive unfold / non-destructive revision; Δ as derived fold — replay, don't store); mode table row for Detection_Record.
- `_types/PLC_Cycle.md` — optional LSPI frontmatter (`plc_Strategic_Stance`, `plc_Stance_Rationale`, `plc_Probe_Budget_Remaining`, `plc_Detection_Record_Refs`, `plc_Suspended_Parent`, `plc_Spawned_Subcycles`); new body sections `## LSPI Operation Record (M)`, `## σ / Guard Log`, `## Intention Positions`; capability-gate subsection (one-q rule; augmented gate; spawn/flowback conservation); worked example's `plc_Slash_Constituents` corrected (previous example was an F9 violation — mixed OPC ID into a slash path).
- `_types/PLC_Session.md` — 16 activities incl. `ESTIMATE`; RUN_CYCLE formal-spine note. `_types/PLC_Actor.md` — optional `plc_Estimated_By` / `plc_Depth_Estimate`; body sections for effect signatures, convertibility edges, estimated-matrix summary; nine-types-as-carriers note. `_types/PLC_Principal.md` — Current Resource Holdings multiset discipline (LSPI R; Thm 13.4). `_types/PLC_Sphere_State.md` — `## Open Estimation` rollup.
- Templates: `PLC_Cycle_TEMPLATE.md` (LSPI frontmatter + Operation Record + σ/Guard Log + Intention Positions + Augmented Gate block), `PLC_Session_RUN_CYCLE_TEMPLATE.md` (stance / σ-forks / guards / spawns / budget lines), `PLC_Sphere_State_TEMPLATE.md` (open detection records line).
- `_frameworks/ADAPT.md` — Decide and Perceive beats gain internal procedures (probe-vs-execute pricing; predicted-vs-observed); three-utilities ↔ prime mapping. `_frameworks/dissertation-substrate.md` — functional resource definition promoted to primary; Category 3 proceduralized; prime notation gains forward dynamics.
- `07-SHIPPING-CHECKLIST.md` — new Section 10 "LSPI integration regression" (layer-order spot-checks; P/Adv alias; owning-actor keying; Rusty gate test; anti-paranoia depth test; probe-budget presence; one-q rule; Persistence Invariant spot-check; frontier hygiene; 0158 round-trip; mirror integrity); ship-time counts updated (17 Types / 23 templates / 9 chapters / 5 substrates / 16 activities / F1–F11). `UPDATE-PROMPT.md` — F-code range → F1–F11.
- **WS5 (frontier intake):** new `_frameworks/reflexivity-frontier.md` (`frontier: true` — level-k, one-above principle, cheap-talk/costly-signal, ck(f) status + publicize verb Ξ, Rusty⟶Erik and Charles⟶CFO anchors, six open problems, depth-estimation delivered/frontier line); new `_frameworks/lspi/observation-model-grounding.md` (catalogue clusters as the managed-signal library; pooling moves; ck_operation frontier tags; hypothesis-not-accusation usage rule); `_frameworks/4R.md` — ladder annotated as depth scale, flywheel formalized as gain-cycles, OV-as-depth-amplifier.
- **WS6 (governance):** new `ROADMAP.md` (the ten expandable ideas with build status + LSPI-named frontiers + sequencing principle); `CONTRIBUTING.md` — LSPI-mirrors zone (no direct edits; upstream-originated re-mirrors) + the correction-log discipline (v0.3→0.4 audit as exemplar; "prose can be more correct than formulas"; "don't build tooling on flagged formalism").

## [1.1.1] — 2026-06-27

Patch — **terminology retirement: "Prototype" → "Type".** The OVE engine concept formerly called a *Prototype* (the type-definition unit) is now uniformly called a **Type**, completing the OKF `type` vocabulary adopted in 1.1.0. Infrastructure surfaces — `_plc-engine/` docs, `export-schema.yaml` (`conforms_to_prototypes` → `conforms_to_types`), front-door docs, and the `- Pattern Prototype:` schema-pointer footer in 79 `_PATTERNS/` files → `- Pattern Type:`. The political-warfare tactic and pattern **prose bodies are untouched** (the word "prototype" there is domain language); historical CHANGELOG entries below and Hugo are unchanged. No behavioral or content change.

## [1.1.0] — 2026-06-26

Google OKF v0.1 conformance (coordinated with vault Master_Schema v1.23.0 + OVE v2.4.0). Universal Core renamed to OKF field names (Item_Prototype→type, Title→title, Tags→tags; added timestamp from Date_Modified, optional description/resource). Convention-6 folder _Prototypes/ → _types/. Date_Modified kept, time-synced with timestamp. Hugo excluded.

## [1.0.0] — 2026-06-13

First shipping release. Establishes the v1.0 schema, the four substrate authorities, the 16 Prototypes, the 22 Templates, the 6 YAML scaffolding files, the operator-facing documentation set, the bootstrap protocols, and the worked-example sphere cartridge.

### Added — Foundations
- **Lam 2018 Pepperdine dissertation on political capital** integrated as the grounded-theory substrate. 19 axial-coded categories; interaction-cycle protocol (14 operational constituents per PLC's walk-through); 9-type resource taxonomy (money / hard assets / credibility / attributes / legitimacy / information / access / title / tribe); slash-addressing notation; Table 3 inventory of ~100 granular Moves. Source PDF in `_frameworks/sources/`.
- **ADAPT Loop** integrated as the commercialized 5-beat coaching frame (Agenda → Decide → Act → Perceive → Track). Source PDF in `_frameworks/sources/`. Lookup card at `_frameworks/ADAPT.md`; craft layer at `_frameworks/ADAPT-as-consulting-engine.md`.
- **OPC Assessment v3.0** integrated as the 17-section sphere diagnostic with 6-level hierarchical IDs. Includes § 11 (Harm & Ethical Evaluation — drives ETHICAL-ACCOUNTING gate), § 15 (Legitimate Alternatives — drives ALTERNATIVES-AUDIT gate), § 16 (Practitioner Self-Assessment — consultant mode), § 17 (Advisor Engagement Politics — consultant mode). Located at `_frameworks/OPC-Assessment.md`.
- **Political Warfare Catalogue** integrated: 782 tactics, 16 strategies, 84 thematic clusters, 50 scholarly theorists. Source mirror at `_frameworks/political-warfare-catalogue/`. Full INDEX.json plus by-strategy / by-cluster / by-theorist facet directories.

### Added — Engine (8 chapters)
- `AI-BOOTSTRAP.md` — AI entry point (4 engagement paths; Phase 0 pre-flight; readiness statement requirements; mode-aware path decision)
- `_plc-engine/00-START-HERE.md` — operator identification; active-sphere identification; Tier 1 + Tier 2 reads; mode-aware pre-engagement hard precedence; sandbox mode; 12 core principles overview
- `_plc-engine/01-WHAT-IS-PLC.md` — definition; 4 substrate authorities; bimodal operator model; what PLC is NOT; 6 distinguishing properties; when right form / when not
- `_plc-engine/02-PRINCIPLES.md` — P1-P12 in full with consequences and anti-patterns
- `_plc-engine/03-SESSION-PROTOCOL.md` — 9-step session lifecycle; 15 activities + 2 embedded gates; full RUN-CYCLE protocol with ALTERNATIVES-AUDIT § 15 + ETHICAL-ACCOUNTING § 11 walkthroughs; QUARTERLY-AUDIT (3-part base + 4 consultant additions); Audit Mode; quality gates checklist
- `_plc-engine/04-SCHEMA.md` — 16 Prototypes; 12 relation families with 24 reciprocal pairs; three reference systems (slash addressing / OPC hierarchical IDs / Catalogue Reference IDs); mastery scales; folder structure; frontmatter conventions
- `_plc-engine/05-WRITING-FOR-AI.md` — 4 audiences; AI-facing + operator-facing prose conventions; tone discipline with mode-aware no-false-confidence priming; F1-F9 documented failure modes; quality checks
- `_plc-engine/06-STATE-PERSISTENCE.md` — 5 durability modes (A/C/D/E/D→E); per-Prototype mode table; Current/History section discipline; cycle lifecycle state machine; reciprocal-update enforcement; sphere-backbone rollup discipline; status-flag pattern
- `_plc-engine/07-SHIPPING-CHECKLIST.md` — 10-section pre-ship gauntlet plus Major Bump Addendum; F1-F9 regression checklist; Convention 1-8 compliance signoff

### Added — Prototypes (16)
- Sphere backbone trio: `PLC_Sphere_Manifest`, `PLC_Sphere_State`, `PLC_Sphere_Decisions`
- Identity + cast: `PLC_Principal`, `PLC_Actor`
- Operational: `PLC_Campaign`, `PLC_Cycle` (the D→E status-flag-transitioning Prototype), `PLC_Session` (with 15-activity enum)
- Diagnostic + retrospective: `PLC_OPC_Diagnostic`, `PLC_Engagement_Retrospective`
- Substrate: `PLC_Move` (smallest grain), `PLC_Tactic` (composed; Catalogue Reference ID 0001-0782), `PLC_Strategy` (1-16), `PLC_Cluster` (C01-C84), `PLC_Theorist` (50 scholarly atoms per D15)
- Discovery: `PLC_Pattern` (single Prototype with 6-family enum: stakeholder_archetypes / change_initiator_postures / opposition_postures / arc_dynamics / power_dynamics_themes / ethical_dilemmas)

### Added — Templates (22)
22 blank-but-conforming starter scaffolds in `_plc-engine/_templates/`. Per-Prototype distribution: Actor 2 flavors (Full + Stub); Session 4 specialized (RUN_CYCLE + OPC_DIAGNOSE + QUARTERLY_AUDIT + Generic); OPC_Diagnostic 3 scopes (Full + Partial + Seed); other Prototypes 1 each.

### Added — YAML scaffolding (6)
1. `export-schema.yaml` — structured-export schema for D23 Layer 3 longitudinal-signals
2. `redaction-profiles/internal-leadership-summary.yaml` — internal leadership audience
3. `redaction-profiles/external-board-summary.yaml` — strictest in regular flow; board-chair-escalation protocol included
4. `redaction-profiles/peer-consultant-share.yaml` — anonymizes identity; preserves methodology
5. `redaction-profiles/principal-private.yaml` — consultant §§ 16-17 redacted; advisor-eyes-only flag honored
6. `redaction-profiles/audit-trail-full.yaml` — no redaction; source of truth for all derived profiles

### Added — Operator-facing documentation
- `README.md` — front door with one-line pitch + three quick-start paths (deploy / orient / methodology-study) + Foundations section naming all 50 theorists at ship time
- `INSTALL.md` — 5-step install with Convention 1 folder naming enforced + 11-row troubleshooting table
- `OPERATOR-GUIDE.md` — single file with partitioned mode sections per D3; 20-row universal symptom→cause→fix + 4-row consultant-specific + 3-row principal-self-specific; AI register overrides via `_USER.md`; stash-pop conflict guidance
- `CONTRIBUTING.md` — 4-zone contribution table; patch/minor/major version criteria; "what's frozen between majors" list; 3-tier contribution workflow

### Added — Bootstrap protocols
- `BOOTSTRAP-NEW-SPHERE.md` — 12-section new-sphere intake; pre-engagement hard precedence in consultant mode (OPC §§ 16-17 BEFORE CQ1); quality floor at sphere-open; CQ1-CQ8 required + CQ9-CQ10 optional
- `UPDATE-PROMPT.md` — 12-step AI-facing version-update protocol per Convention 7; sphere-preservation discipline; F1-F9 regression spot-check at every update

### Added — Pattern seeds (6 families)
- `_PATTERNS/stakeholder-archetypes/` — from OPC § 2.2.1
- `_PATTERNS/change-initiator-postures/` — 10 from OPC § 13.1.1
- `_PATTERNS/opposition-postures/` — 10 from OPC § 13.1.2
- `_PATTERNS/arc-dynamics/` — 20 from OPC § 13.2
- `_PATTERNS/power-dynamics-themes/` — 10 from OPC § 13.3.1
- `_PATTERNS/ethical-dilemmas/` — 10 from OPC § 13.3.2

### Added — Worked-example sphere
A populated example sphere cartridge demonstrating the full schema. See `Spheres/Example-Sphere-Acme-Corp/` — Acme Corp engagement (consultant mode; family-board succession scenario) materializing the worked examples used across the Prototype definitions. Serves as the F-code regression canary per `07-SHIPPING-CHECKLIST.md` § 7. Intentionally mid-engagement (not closed) — demonstrates active-state cartridge form rather than retrospective-final state.

### Added — License + version metadata
- `LICENSE.md` — proprietary, all-rights-reserved license with explicit permission grants required for consulting deployment, derivative works, redistribution, embedding, organizational deployment
- `VERSION.md` — canonical version reference; compatibility matrix
- `CHANGELOG.md` — this file
- `.gitignore` — sphere-cartridge exclusion patterns

### Security
- ALTERNATIVES-AUDIT § 15 + ETHICAL-ACCOUNTING § 11 gates established as mandatory inside RUN-CYCLE protocol; override discipline documented (per D9)
- Five redaction profiles establish baseline output-disclosure discipline (per D13 + D16)
- F1-F9 documented failure modes establish baseline AI-misbehavior discipline (per `05-WRITING-FOR-AI.md`)

### Migration notes
First shipping release; no prior cartridges to migrate. Operators installing PLC for the first time follow `INSTALL.md`.

### Acknowledgments
PLC v1.0.0 was designed using **Operating Volume Engineering v1.2** (the meta-OV for designing other OVs). The design engagement ran 2026-06-07 through 2026-06-13 across three sessions: BOOTSTRAP (CQ1-CQ10 → D1-D13), CATALOGUE-INTEGRATION (D14-D16), and SCHEMA-DESIGN (Q0-Q13 → D17-D30). The ARTIFACT-DRAFT phase materialized this v1.0 set of shipping files.

The 50 cited theorists are acknowledged in `README.md` § Foundations and individually in `_frameworks/political-warfare-catalogue/by-theorist/`. Their scholarly works remain subject to their own copyrights; PLC cites under fair-use academic conventions and does not redistribute their primary work.

---

## Format conventions for future entries

When adding a new release section:

- Place above prior releases (newest first)
- Use the format `## [<version>] — <YYYY-MM-DD>`
- Group entries under the standard headings (Added / Changed / Deprecated / Removed / Fixed / Security / BREAKING / Migration notes)
- BREAKING entries MUST be prefixed `BREAKING:` and MUST include a pointer to the migration guide
- Acknowledgment block at end of substantive releases

## Format conventions for pre-release work

Pre-release versions (alpha, beta, rc) follow semantic versioning with the convention:

- `1.0.0-alpha.1` — early development, schema unstable
- `1.0.0-beta.1` — schema stable; documentation gaps acceptable
- `1.0.0-rc.1` — release candidate; ship-checklist passing; awaiting final sign-off

Pre-release entries are documented separately under `## [Unreleased]` until they reach a numbered release.
