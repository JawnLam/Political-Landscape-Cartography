---
Item_Prototype: Fleeting
Item_ID: lpic-foundations
Title: "The Lam System for Political Interaction (LSPI): a typed, oracle-driven domain-specific language with a small-step operational semantics and proven meta-theory — Foundations"
Date_Added: 2026-06-18
Date_Modified: 2026-06-22
Needs_Processing: false
plc_Doc_Type: treatise
plc_Doc_Status: draft-parts-I-through-IV-in-progress
plc_Doc_Scope: "The foundations treatise for the Lam System for Political Interaction (LSPI). Six parts: (I) Foundations, (II) The System by Layer, (III) Theorems & Properties, (IV) Validation against worked cases, (V) Operational guidance for AI engines, (VI) Open questions and extensions. This file accumulates parts as they are drafted; signed-off architecture lives in LPIC-Treatise-Architecture.md (r5)."
plc_Architecture_Source: "LPIC-Treatise-Architecture.md (r5, signed off)"
plc_Substrate_Authority: "Lam 2018 Pepperdine dissertation; PLC v1.0; five worked case studies (Charles, Jim, Nathan, Sarah, Rusty — dissertation Tables 5–22)"
AI_Instructions: "This is the treatise that the LSPI architecture (r5) plans. Parts I–VI build out as drafted. Hard guardrails from architecture §1 govern every part: not an algebra; not a process calculus (LSPI is a typed DSL with a small-step structural operational semantics forming an oracle-parameterized state-transition system, per §1.1 / §2.2); descriptive, not computation; axioms = Layer 3 only; theorems out of catalog; no frame-mixing; Persistence Invariant governs the operation record M; the dissertation's derived decision matrix Δ is a fold over M, not a configuration slot, and is ungoverned (the discipline is in M, the source-of-truth). The treatise serves two audiences in parallel: human readers evaluating the methodology, and AI engines using LSPI during live PLC engagements. Where audiences diverge, prose serves the human; `## For AI engines` subsections serve the AI."
---

# The Lam System for Political Interaction (LSPI) — Foundations

### A typed, oracle-driven domain-specific language with a small-step operational semantics and proven meta-theory

## Abstract

The **Lam System for Political Interaction (LSPI)** is a typed domain-specific language (the slash-addressing notation) with a small-step structural operational semantics, forming an oracle-parameterized state-transition system, with proven meta-theory (§13.1–§13.6): subject reduction, congruence decidability, resource conservation, strong normalization, and oracle-relative confluence.

<!-- ALT opening for org-science venues: This treatise formalizes the move-by-move dynamics of organizational political interaction — how an actor declares interest, detects who controls a desired resource, sets an objective, declares intentions, escalates when held resources fall short, perceives whether realized outcomes validate projected ones, and accumulates political capital across compound cycles — as the **Lam System for Political Interaction (LSPI)**: a typed domain-specific language (the slash-addressing notation) with a small-step structural operational semantics, forming an oracle-parameterized state-transition system, with proven meta-theory (§13.1–§13.6): subject reduction, congruence decidability, resource conservation, strong normalization, and oracle-relative confluence. -->

The transition relation is **oracle-parameterized**: the irreducibly interpretive guards — perception-validation (did the realized comparison validate the projected one?), σ-discretion at irreversible operator elections, and operator-attested premises — are lifted into an explicit oracle `O` that resolves them. The meta-theorems hold *oracle-relative*: once the oracle's judgments are fixed, the system's per-σ confluence (§13.6) is exactly oracle-relative determinism. This is the central selling point and the central honesty: the system describes a process a human drives; the machine guarantees what the machine can guarantee; the boundary between the two is **Pillar 2** of the treatise (the boundary of computation), made formally precise.

The constituent vocabulary, the typed grammar, the structural congruence and its decidability, the twenty-one transition rules organized into lifecycle, failure, and non-destructive families, and the meta-theorems (§13.1–§13.6) are all validated against the dissertation's five worked engagements (Charles, Jim, Nathan, Sarah, Rusty — Lam 2018, Tables 5–22). The name reflects the object — a state-transition system, not a calculus or an algebra; §2.1 records the naming history and §2.2 gives the three structural reasons those technical terms do not apply.

# Part I — Foundations

## §1 Introduction & Purpose

### §1.1 What LSPI is

LSPI is a typed domain-specific language (the slash-addressing notation) with a small-step structural operational semantics, forming an oracle-parameterized state-transition system, with proven meta-theory (§13.1–§13.6): subject reduction, congruence decidability, resource conservation, strong normalization, and oracle-relative confluence. It formalizes the notation system introduced in the Lam 2018 Pepperdine dissertation on political capital — the system the dissertation calls "slash addressing notation" — and equips it with the typed grammar, the structural congruence, the transition relation, and the meta-theorems needed to support cross-cycle reasoning at engagement scale.

The name **Lam System for Political Interaction (LSPI)** is literal — the object is the state-transition system the name describes. §2.1 records the naming history (an earlier compositional-algebra framing and a process-calculus framing, both rejected for technical reasons); §2.2 gives the three structural reasons the system is deliberately not a calculus or algebra. The identity matches the name.

What LSPI formalizes is **organizational political interaction** — the move-by-move accumulation, deployment, and protection of political capital that Lam's 2018 dissertation grounds in twenty-five executive interviews. The transition rules model what political reasoning produces: detections, executions, perceptions, selections, gate-failure-triggered nested cycles, obtained resources flowing back, projected positions reconciled against realized ones, and the audit trail of every step preserved. The oracle parameter `O` resolves the irreducibly interpretive guards — perception-validation, σ-discretion at Bucket-1 forks, operator-attested premises — so the meta-theorems hold *relative to the oracle's choices* and the per-σ confluence (§13.6) IS oracle-relative determinism. This is **Pillar 2** of the treatise: the boundary of computation, made formally precise.

### §1.2 Why this treatise exists

The dissertation introduced its notation as part of a grounded-theory methodology — to "track each relevant fact from the unique observation and how it mapped onto the conditional matrix." The notation served its scholarly purpose admirably. But the dissertation neither axiomatized the system nor specified its dynamics formally. The grammar was implicit in worked examples; the type system was implicit in operator conventions; the structural congruence was undefined; the transition relation was narrated in prose rather than given as inference rules.

For LSPI to function as the operational substrate for an AI-driven political-reasoning system — which is what the Political Landscape Cartography (PLC) Operating Volume needs it to be — these omissions must be filled. An AI parsing LSPI expressions cannot reason "what the dissertation probably meant." It needs:

1. A **grammar** that precisely specifies which strings are well-formed terms.
2. A **type system** that determines which terms are well-typed.
3. A **structural congruence** that says which terms denote the same constituent.
4. A **transition relation** that says how a configuration evolves.
5. **Theorems** that prove the system has the properties it claims (uniqueness, closure, decidability, conservation).

This treatise supplies all five. Six parts:

- **Part I (this part) — Foundations.** What LSPI is; how it relates to its sources; the metalanguage; the constituent vocabulary; the operator families; the five-layer architecture; the Persistence Invariant.
- **Part II — The System by Layer.** The grammar (Layer 1), type system (Layer 2), structural congruence (Layer 3), transition relation (Layer 4 — 21 transition rules plus 2 non-firing disciplines), and the complete operator-layer catalog (§12).
- **Part III — Theorems & Properties.** Uniqueness, closure under transitions, preservation of typing, decidability of well-formedness, resource conservation across nested cycles, termination bounds, and explicit non-claims.
- **Part IV — Validation against worked cases.** Each of the dissertation's five worked case studies (Charles, Jim, Nathan, Sarah, Rusty) walked through LSPI's rules to confirm that LSPI reproduces what the dissertation depicts.
- **Part V — Operational guidance for AI engines.** How an AI parses, validates, reduces, and hands off LSPI state during live PLC engagements.
- **Part VI — Open questions, extensions, appendices.** Design-decisions log; v2 candidates (behavioral equivalence, name binding, concurrent composition, multi-level abandonment cascade); relationship to other formal systems; glossary; cross-reference index; complete rule catalog.

### §1.3 What counts as success

This treatise succeeds when an AI engine reading it (and the architecture document that supplies its skeleton) can:

1. **Parse** an LSPI expression deterministically.
2. **Validate** the expression's well-formedness against the grammar (Layer 1) and type system (Layer 2).
3. **Decide** equality of two expressions against the structural congruence (Layer 3).
4. **Apply** a transition rule (Layer 4) to a configuration and produce the resulting configuration, with the agent-dispatch, the path-extension family, the persistence discipline, and the failure-family branches all honored.
5. **Reproduce** the dissertation's five worked case studies as traces through the transition relation.
6. **Surface** the design decisions LSPI made where the dissertation was silent — neither smuggling them in as if they were dissertation-derived, nor hiding them in implementation.

This treatise does NOT succeed if any of:

- The treatise presents LSPI as autonomously executable, or its guards as mechanically evaluable. The guards are interpretive *by design* (see §1.5); the AI's job is to *administer* the system, not to *execute* it autonomously. Treating the system as executable would corrupt both the system and the engagement it supports.
- The axioms forbid moves that the worked cases demonstrate.
- The Persistence Invariant is violated by any rule (with the scope clarified in §7.5).
- Any term written in the worked cases is rejected by LSPI's grammar after the Θ/Φ/Λ source-reconciliation normalization is applied.

### §1.4 The maneuver lifecycle — what the system is about (Pillar 4)

§1.1 introduces the interaction cycle as "a transaction opened by an actor with an interest for a desired resource, closed when the target selects from a decision matrix and an outcome resolves." That seed is enough for a single-intention cycle. The corpus also exhibits multi-intention cycles, where an actor pursues one interest through several distinct levers aimed at the same target. This subsection develops the seed into the full lifecycle — including the multi-intention case — and states what the lifecycle commits LSPI to and what it leaves to operator judgment. The transition rules of §11.4 are the formal realization of what is said here.

#### §1.4.1 The maneuver

A **maneuver** is one actor's intervention into one target's selection. The actor opens an interest in a desired resource Q held by the target's decision; commits to one or more **intentions** — projected utility comparisons through which the actor expects the target's preferred position to become the selected outcome; executes each intention against an identified resource the actor must possess to act through that lever; perceives whether the realized comparison validates the projection; and either advances toward outcome or revises. The maneuver closes when the target selects from a decision matrix and an outcome resolves; the actor's obtained utility and obtained resource flow back into the actor's resource set.

This is field theory, not rule list. The constituents (interest, detection, objective, intention, required-resource, gate, execute, perceive, select, outcome, obtained-utility, close, flowback) are not arbitrary phases; each names a specific epistemic act in the actor's intervention. **Detection** records what the actor sees about the target's decision space. **Objective** fixes the selection-yields-position projection the actor wants. **Intention** specifies the lever — the projected utility comparison through which a chosen resource (Q) is expected to shift the target's preferred-position calculus. **Required-resources / gate** ask whether the actor possesses what the lever needs. **Execute** applies the lever. **Perceive** realizes the projected comparison against what the target actually does. **Select / outcome / obtained-utility** close the cycle. The phases sequence because each writes to the operation record `M` what the next phase reads.

#### §1.4.2 Single-intention case (Charles): the canonical lifecycle

Charles T5 walks the single-intention lifecycle from open to flowback in linear sequence: open → interest → detect → objective → intention → required-resources → gate (passes) → execute → perceive → select → outcome → obtained-utility → close → flowback. K=1 (one intention), gate passes, no escalation. This is the baseline; every phase fires exactly once; there is no question about sequencing because there is only one of each phase to fire.

The corpus's other four cases all exhibit either K>1 (multiple intentions, where the actor identifies multiple levers for the same interest) or gate-failure-driven nesting (where missing a required resource triggers a sub-cycle to obtain it), or both. The lifecycle as field theory must answer: when the actor has identified multiple levers, what determines the ordering, batching, and adaptation pattern?

#### §1.4.3 The strategic stance — multi-intention sequencing as Oracle judgment

When an actor has identified multiple levers for the same interest, the **ordering, batching, and adaptation of those levers is a strategic stance the actor takes toward uncertainty about whether the levers will be sufficient**. The corpus exhibits three legitimately distinct stances. They are not three competing readings of one phenomenon; they are three different ways an actor can intervene through K>1 levers, each appropriate to different judgments about how to manage the uncertainty.

- **Adaptive (Rusty)**. The actor declares each lever only after perceiving the previous one's effect. γ_2 is declared after R-perceive-failure(γ_1); γ_3 after R-perceive-failure(γ_2). Both intention-additions ride the `⟨perceive-failure, C⟩` premise that §11.4.5 line 1841 admits. Only γ_3 (T22) ultimately validates; γ_1 (T18) and γ_2 (T20) both fail their projections (Todd voices displeasure but does not yet prefer leaving at T18; the organizational restructure does not yet shift the system at T20). The maneuver evolves with realized utility. Stance: "I will only commit to the next lever after I see what the previous one did, especially when the previous one failed." Source-verified at Rusty T16 → T18 → T20 → T22.

- **Pre-committed, resource-careful (Nathan)**. The actor declares all levers upfront, then executes each through its full θ / gate / execute before declaring the next gate test. Stance: "I know the lever set early, but I'll secure each resource and apply it before committing effort to the next." Source-verified at Nathan T7 (γ_1, γ_2 declared in adjacent rows; then θ_1 → gate_1 ∋ → ε_1 → θ_2 → gate_2 ∌ → spawn Wanda).

- **Pre-committed, resource-batched (Sarah)**. The actor declares all levers AND all gate tests upfront, then spawns for whatever's missing. Stance: "I'll lay out the complete plan, identify everything I lack, then pursue all the missing pieces." Source-verified at Sarah T12 (γ_1, γ_2, θ_1, θ_2 all declared upfront; both gates fail before either sub-cycle runs).

The system's job is to **receive** whichever stance the actor adopts — not to choose between them. §11.4's transition rules should be permissive where the choice belongs to the actor.

#### §1.4.4 The Pillar-2 ∩ Pillar-4 boundary

§1.5 (Hard disclaimers, immediately below) names the **interpretive surface** in LSPI: the guards — does the actor possess q, does the target perceive P.u > X.u — are resolved by human judgment, not mechanical evaluation. That is Pillar 2.

The maneuver lifecycle (this section, Pillar 4) names the **strategic surface**: which lever to declare first, whether to batch or adapt, when to evaluate perception versus commit to the next intention, whether to moot a lever whose substantive purpose another sub-cycle's outcome has met. These are judgment calls, not gaps in the spec. They are where the Oracle inhabits the lifecycle from the strategic-sequencing side, the same way it inhabits the guard-firing side from the interpretive side.

**The two pillars are the same boundary seen from two sides.** Pillar 2 names what fills the guards; Pillar 4 names what shapes the sequence the guards fire in. LSPI's transition relation is permissive on both because that's where the system *receives* the actor's intervention; the determinism §13.6 establishes is determinism **per fixed σ** (the operator's choice sequence), not determinism in the rule set. σ is the formalization of "the Oracle made these choices." Where §11.4 has a fork that admits multiple firings, that fork is the surface Pillar 2 ∩ Pillar 4 inhabits — not a defect.

#### §1.4.5 The discretion-vs-defect cut — derived from lifecycle states

The earlier framings of this cut started from a catalog of named "axes" surfaced during §14 verification and tried to classify each. That approach produced four re-classification passes in succession, each surfacing a different way the inherited axis taxonomy didn't map to real forks (phantoms, mis-grained rules, conflated sub-modes). The structurally cleaner derivation — and the one Pillar 4 requires — builds the forks natively from the lifecycle: enumerate each `last(M-cycle-C)`-state the lifecycle can reach, list which rules' premises match at that state, check which firings each corpus case witnesses, and classify the state on its own evidence. Forks appear where multiple admissible rules contest with witnessed picks; phantoms are absent (no entry); mis-grained rules surface as "rule operates at wrong grain for this state's witness"; the inherited axes become parenthetical legacy pointers for §14 cross-references.

**Strict test (carried unchanged from earlier framings):**

- **A state is licensed-σ-discretion iff the rule admits all source-witnessed behaviors at the state regardless of σ.** Different cases may pick differently; what makes the state licensed is that every case's source-verified behavior is reachable under some operator choice.
- **A state hosts a defect iff some source behavior is unreachable regardless of σ.** The rule's premise structure or contractum mechanically forbids what at least one case actually does. The Rule 2 reproduction-failure signal.
- **A state is guard-determined (Pillar 2) iff there is no σ-fork — the firing is selected by the operator's interpretive judgment of the realized world (does the actor possess q, does the realized comparison validate the projected one), not by sequencing choice.**

The state table below derives from these three dispositions, with each state row-walked against the source. "Witnessed by ∅" means the corpus does not exercise the admissible rule at that state — recorded as "no fork" rather than as a licensed claim that would require witnesses to validate. Inherited axis labels appear in parentheticals so §14 worked-case sections that cite "Axis N" still resolve.

**Standing-option principle (R-rr admissibility, post-2026-06-23 §11.4.6 revision).** §11.4.6's pending-θ-set premise makes **R-required-resources a standing option, not a localized fork**: R-rr is admissible at **every** state where `PendingTheta(M-cycle-C) ≠ ∅` — i.e., the entire window from any γ's declaration until its θ is written. At each such state R-rr forms a σ-fork with whatever rule is otherwise admissible at that `last`-position: R-intention at γ-body, R-gate at θ-body, R-execute at ⟨gate-pass⟩, R-perceive / R-perceive-failure at ε-body, R-spawn at ⟨gate-fail⟩, R-intention/moot/abandon at ⟨perceive-failure⟩. The operator's σ chooses at each: **resource a pending intention now vs proceed with the current lifecycle activity**. This is a pervasive Pillar-4 interleaving-discretion surface introduced by the set-based premise — the operator may resource any declared intention at any point before its gate, with σ at §13.6 carrying the choice. The per-state rows below record witnessed picks at each state where the standing option applies; the rule's admissibility is not localized to those rows, only the witnesses are. (The 2026-06-23 propagation pass under-counted the standing-option surface twice by treating it as three localized forks; this principle states it once, correctly.)

| `last`-state | Admissible rules | Witnessed picks | Classification | Axis legacy |
|--------------|------------------|-----------------|----------------|-------------|
| `ω-body` | R-intention(γ_1) | all cases | no fork (single admissible rule) | — |
| `γ_1-body`, single γ in scope | R-intention(γ_2); R-required-resources(θ_1) | Sarah, Nathan → R-intention; Rusty → R-required-resources | **licensed-σ-discretion** — both admissible rules witnessed | Axis 1a + Axis 3a (same state, same fork) |
| `γ_2-body`, both γ_1 and γ_2 declared | R-required-resources (per §11.4.6's 2026-06-23 pending-θ-set premise) writes θ for `earliest-declared γ ∈ PendingTheta` = γ_1 | Sarah T12 row 12, Nathan T7 row 11 → θ for γ_1 (reproduced) | **RESOLVED 2026-06-23 via §11.4.6 set-based premise** (was: defect — Site (i)) | Axis 1b Site (i) — resolved |
| `ε_1-body`, γ_2 still owes θ | R-perceive, R-perceive-failure (per validation premise), AND R-required-resources (per §11.4.6's 2026-06-23 pending-θ-set premise, since PendingTheta = {γ_2}) | Nathan T7 row 13 → row 14 fires θ_2 (R-rr writes θ_2 from PendingTheta = {γ_2}, reproduced); σ disambiguates among R-perceive / R-perceive-failure / R-rr at this state | **RESOLVED 2026-06-23 via §11.4.6 set-based premise; now licensed σ-discretion at this state** (was: defect — Site (ii)) | Axis 1b Site (ii) — resolved; Axis 7 terminal mode also resolved (Nathan's "terminal perceive" is now licensed σ-choice, not defect artifact) |
| `ε-body`, no γ pending θ | R-perceive (if realized validates γ-body); R-perceive-failure (if not) | all cases at this state; firing determined by the realized comparison | **guard-determined (Pillar 2)** — not a σ-sequencing fork; the operator's judgment of the realized world selects the firing | Axis 7 per-intention mode (perceiving at ε-body is guard-determined, not σ) |
| `⟨perceive-failure, C⟩` | R-intention(new γ); R-moot; R-abandon | Rusty T18 → R-intention(γ_2); Rusty T20 → R-intention(γ_3); R-moot and R-abandon not witnessed at this state | **licensed-σ-discretion** for R-intention (Rusty witnesses cleanly under §11.4.5 line 1841's `⟨perceive-failure, C⟩` premise — this is the fix the §14.5.1 perception correction established); R-moot and R-abandon admissible-but-unwitnessed-here | Axis 2 (re-located: intention-addition discretion lives here; the ε-body framing was the phantom — this is §14.5's "Rusty's dynamic intention-addition") |
| post-resume / operator-attested premise-void | R-moot-intention (per-intention; §11.6.6.3) at K ≥ 2 cycles; R-moot (cycle-scoped) at K=1 | Sarah T15-area: parent post-Srini-resume, operator attests g_2 substantively achieved → **R-moot-intention(g_2)** writes intention-scoped `⟨moot, C, g_2⟩`; cycle continues on g_1 and reaches R-close via R-execute(g_1)/R-perceive(g_1)/R-select/R-outcome/R-obtained-utility/R-close/R-flowback | ~~defect — §11.6.6's contractum writes `⟨moot, C⟩` (cycle-scoped) but source needs intention-scoped moot of g_2 while cycle continues to close on g_1 (T15 fires Ω/Λ/Φ); no σ-choice reproduces the source's intention-scoped moot under cycle-scoped contractum~~ **Axis 4 RESOLVED 2026-06-24** by the implemented Phase 2 / Phase 3 reframe (intention-scoped R-moot-intention rule at §11.6.6.3 supplies the marker granularity; IntentionPosition per-K fold at §11.1 makes R-execute(g_1) admissible past the buried `⟨resume, q_2⟩` marker; Sarah-T15 mechanically reduces to R-close — full transition trace verified at source 2026-06-24). The licensed σ-discretion at this state is now: σ picks R-moot-intention(g_k) vs proceed-with-g_k (Bucket 1 per §13.6's classification) | Axis 4 (resolved 2026-06-24) |
| `θ-body` (PendingTheta = ∅) | R-gate | Charles, Jim, Rusty (no pending γ at θ-body) | no fork | — |
| `θ-body` (PendingTheta ≠ ∅) | R-gate AND R-rr (standing-option principle) | Nathan T7: after θ_1 written (row 11), at `last = θ_1-body` with PendingTheta = {γ_2}, Nathan picks R-gate (row 12) over R-rr. Strategic stance: gate-now over resource-next. | **licensed-σ-discretion** (witnessed pick: R-gate). The σ-fork at this state was previously unreachable under §11.4.6's `last`-keyed premise (R-rr couldn't fire from θ-body); post-2026-06-23 the fork is admissible per the standing-option principle. | (no inherited axis — surface emerged from §11.4.6's broadening; recorded with the standing-option principle citation) |
| `⟨gate-pass, q⟩` (PendingTheta = ∅) | R-execute, body specifies q to deduct | Charles, Jim, Rusty | non-defect (body specifies; rule resolves) | — |
| `⟨gate-pass, q⟩` (PendingTheta ≠ ∅) | R-execute AND R-rr (standing-option principle) | Nathan T7: at gate_1 ∋ (row 12), with PendingTheta = {γ_2}, Nathan picks R-execute(ε_1) (row 13) over R-rr(θ_2). Strategic stance: execute-now over resource-next. ~~Sarah T15 reaches this state at K=2 with uniform-sole-dot body — Axis 8-Sarah defect at the R-execute leg of the fork.~~ **Axis 8-Sarah RESOLVED 2026-06-24** via full g_k-scoped path discipline (see §11.4.8): Sarah's full θ-bodies are `θ(Α/i./o./g1) := {[Α/i./o./g1/q.]}` and `θ(Α/i./o./g2) := {[Α/i./o./g2/q.]}` — distinct full designations differing at the g_k segment. Sole-dot under each g_k means "unique q under this g_k" per the dissertation's nomenclature; "no constituents will ever share the same designation." `R ⊖ cost([Α/i./o./g_k/q.])` reads the full g_k-scoped path, not bare `[q.]`. | **licensed-σ-discretion at the fork** (witnessed pick: R-execute, Nathan); ~~defect at R-execute leg for Sarah~~ — **defect RESOLVED 2026-06-24 (faithful-and-unique-when-fully-addressed)**. The state hosts only the licensed σ-discretion now. | ~~Axis 8-Sarah~~ **(resolved 2026-06-24)**; standing-option σ-discretion at the fork itself |
| `⟨gate-fail, q⟩`, single-q θ, PendingTheta = ∅ | R-spawn (targets q) | Charles (gate ∋, no gate-fail at all), Jim (gate ∋), Nathan (Wanda escalation at gate_2 ∌ after γ_2 resourced — PendingTheta empty), Rusty (each γ_k's escalation is at its own gate-fail with PendingTheta empty per interleaving) | no fork | — |
| `⟨gate-fail, q⟩`, single-q θ, PendingTheta ≠ ∅ | R-spawn AND R-rr (standing-option principle) | Sarah T12: after gate_1 ∌ (`R ∌ q_1`), with PendingTheta = {γ_2}, Sarah picks R-rr — writes θ_2 (defers spawn, resources γ_2 first). Strategic stance: resource-next over escalate-now. | **licensed-σ-discretion** (witnessed pick: R-rr, Sarah) — **Axis 3b θ-reachability half resolved** by §11.4.6's standing-option surface. Axis 3b's remaining needs-inspection narrows to the §11.6 active-C question (double R-spawn stacking on S after both θ written and both gates failed). | Axis 3b θ-reachability half — resolved; double-spawn-on-S half — needs-inspection |
| `⟨gate-fail, ...⟩`, multi-q θ under conjunction reading of R-gate | R-spawn (no licensed target — no rule names which q broke the conjunction) | Rusty T16 escalates for q_2 specifically — relies on per-θ inference §11.4.6 / §11.4.7 don't license | **defect** — R-spawn's target identification is unlicensed inference under conjunction reading; the per-θ reading that licenses Rusty's escalation is itself unlicensed by §11.4.7's singular-q premise | Axis 6 Layer C |
| `Γ-body`, validating | R-select | all cases at this state | no fork | — |
| `Σ-body` | R-outcome | all cases | no fork | — |
| `Ω-body` | R-obtained-utility | all cases | no fork | — |

**Two needs-inspection states (located by state, not yet row-walked to a defect/discretion classification)**:

- `⟨gate-fail, q_1⟩` with parent's lifecycle continuing to fire θ_2 before R-resume (Sarah T12 batched-θ pattern). Does §11.6 admit a second R-spawn while a parent is already suspended on S — i.e., can the parent continue firing rules in its own cycle after R-spawn has transferred active C to the first sub-cycle? §11.6.2's active-C-transfer discipline and §11.6.1's S-stack structure need state-by-state inspection. Leaning defect (the active-C-transfer reading suggests the parent's lifecycle is suspended when R-spawn fires), but the row-walk of §11.6's rules at this configuration hasn't been completed. **Axis 3b legacy**.
- `ε_1-body`, same γ, ε_2 must fire (Sarah T14's Srini sub-cycle with two ε firings for one γ). R-execute's premise is `last = ⟨gate-pass, q⟩`; ε_1's contractum writes `ε_1-body` to last, not a fresh `⟨gate-pass, q⟩` marker. Re-firing R-execute from `ε_1-body` matches neither R-execute's premise nor any other admissible rule's premise. Looks structurally forbidden under the current rule. Leaning defect. **Axis 5 legacy**.

**Summary (post-2026-06-24 Phase 2/3 Thread A reframe; standing-option principle preserved; two fix-targets resolved at source, one remains)**: §11.4.6's pending-θ-set premise establishes R-rr as a **standing option** at every state with `PendingTheta(M-cycle-C) ≠ ∅` — this is a pervasive Pillar-4 interleaving-discretion surface, not three localized forks. Per-state witnesses recorded above: **Sarah picks R-rr at γ_2-body** (writes θ_1), **Nathan picks R-rr at γ_2-body** (writes θ_1) and **at ε_1-body** (writes θ_2), **Nathan picks R-gate at θ-body with pending γ_2** (gate-now over resource-next), **Nathan picks R-execute at ⟨gate-pass⟩ with pending γ_2** (execute-now over resource-next), **Sarah picks R-rr at ⟨gate-fail, q_1⟩ with pending γ_2** (resource-next over escalate-now). Six witnessed picks at five distinct states (γ_2-body shared by Sarah and Nathan; ε_1-body, θ-body, ⟨gate-pass⟩, ⟨gate-fail⟩ each witnessed once), all part of the same standing-option surface. **One state remains guard-determined** (`ε-body` no-γ-pending — the Pillar-2 surface, independent of PendingTheta). **Three states previously hosted defects** (post-resume operator-attested R-moot, `⟨gate-pass, q⟩` R-execute leg for Sarah-K=2-sole-dot, `⟨gate-fail⟩` R-spawn target-id under multi-q-conjunction); **two are now resolved** (post-resume R-moot → **Axis 4 RESOLVED 2026-06-24** by Phase 2/3 reframe — R-moot-intention §11.6.6.3 + IntentionPosition §11.1 + full Sarah-T15 transition trace; `⟨gate-pass⟩` Sarah-K=2-sole-dot → **Axis 8-Sarah RESOLVED 2026-06-24** by §11.4.8's full g_k-scoped path discipline via the dissertation's nomenclature uniqueness guarantee), and **one fix-target remains: §11.4.7 multi-q gate (Axis 6)**. **One needs-inspection narrowed**: Axis 3b — the θ-reachability half is resolved by the standing-option surface (Sarah's "θ_2 before spawn" at gate-fail-with-pending-γ is licensed σ-discretion); the remaining question is the §11.6 active-C admissibility of double R-spawn stacking on S after both θ written and both gates failed — and per the design note §5.6 split, the stacking question dissolves by active-C (sibling sub-cycles cannot stack on S simultaneously), with the spawn-ORDER becoming licensed σ-discretion via (R-spawn, g_k) σ-pick reading IntentionPosition. **One needs-inspection resolved by §13.6 Bucket-2 classification (Sarah per-intention multi-execute)**: the Phase 3 confluence proof's Embrace diamonds for distinct-g_k R-execute pairs commute, making the question structurally answered. The rest are no-fork single-admissible-rule transitions when PendingTheta = ∅.

**The two judgment surfaces are visible at different states.** Pillar 2's guard-determined surface lives at `ε-body` (R-perceive vs R-perceive-failure is selected by the operator's reading of the realized world, not by σ). Pillar 4's σ-sequencing surface lives at `γ_1-body single-γ` (R-intention vs R-required-resources) and at `⟨perceive-failure, C⟩` (R-intention vs R-moot vs R-abandon). Both surfaces are Oracle judgment, but they operate at different lifecycle states and resolve different kinds of question — interpretive (does the world look as projected) vs strategic (which lever next given the world as it is). The state table makes this two-surface structure visible where the inherited axis taxonomy buried it.

**Discipline note (carried from the prior framings, sharpened).** The state-fork structure surfaces mis-locations as "wrong state" (Sarah's R-moot was mis-co-located with Rusty's R-intention at `⟨perceive-failure, C⟩` in an earlier sketch and the row-walk caught it; the corrected location is post-resume operator-attested) rather than hiding them as "phantom axis under closer look." But the structure does not auto-correct. Every state row must still be row-walked against the source independently. The cleaner organization eliminates one class of failure mode (inherited-axes-don't-map-to-real-forks); it does not eliminate row-walking. Future state additions or re-classifications must each cite the source rows they rest on.

**Fix targets by state** (the actionable summary):

- **`γ_2-body` (Axis 1b Site (i)) + `ε_1-body` γ-pending (Axis 1b Site (ii))**: **RESOLVED 2026-06-23** — §11.4.6's `last`-keyed premise has been replaced by a pending-θ-set premise, with declaration-order firing at K=2 (K-coverage caveat preserved: K≥3 batched data would refine further but no such case exists in the corpus). The single set-based premise covers both sites and additionally resolves the θ-reachability half of Axis 3b (Sarah's "θ_2 before spawn" at `⟨gate-fail, q_1⟩` with `PendingTheta = {γ_2}` is now licensed σ-discretion). §13.6's pre-Thread-A coarse-reading empty-independence argument was repaired (old §13.6.2/§13.6.3 of the pre-Thread-A draft): the symmetric-write half of the last-dependency clause catches R-required-resources's `LastEffect = θ-body` write, preserving the empty-independence conclusion. (Under Thread A the empty-independence claim is superseded by the three-bucket partition; the same literal-`last` accounting is now in §13.6.3's congruence lemma enumeration.) The per-cycle firing-count bound (inline in §13.5.2's `rem_budget`, formerly old §13.5.4's Reading B / old §13.5.6's bound) holds by construction (PendingTheta excludes γ_k once θ_k ∈ M; per-cycle θ-firings = K_C as before). See §11.4.6's revised rule for the full reproduction analysis and §13.6.2 for the lemma repair.
- ~~**post-resume operator-attested R-moot (Axis 4)**: either an intention-scoped moot rule (contractum `⟨moot, C, g_k⟩` with a side condition that the cycle's remaining intentions can still progress), or a structural reframe in §11.4 that treats a cycle's K intentions as separately closable sub-units so the cycle's outcome can close on g_1 with g_2 dropped without cycle-level moot firing.~~ **Axis 4 RESOLVED 2026-06-24** by the implemented Phase 2 / Phase 3 reframe — BOTH options identified above have landed jointly: §11.6.6.3 R-moot-intention provides the intention-scoped contractum `⟨moot, C, g_k⟩` with the `|LiveIntentions \ {g_k}| ≥ 1` side condition (marker granularity), AND the §11.1 IntentionPosition substrate + §11.6.6.2 transparent-`last` convention + the §11.4 per-intention rule rewrites (R-execute, R-perceive, R-rr, R-gate, etc.) implement the structural reframe (per-intention lifecycle-position tracking) that lets the cycle continue on g_1 past g_2's mooting. Sarah-T15 mechanically reduces to R-close via R-moot-intention(g_2) → R-execute(g_1) [admissible via per-K IntentionPosition fold past `⟨resume, q_2⟩` and `⟨moot, C, g_2⟩`] → R-perceive(g_1) → R-select [F4 satisfied: g_1 perceived, g_2 mooted, both terminal] → R-outcome → R-obtained-utility → R-close → R-flowback. Full transition trace verified at source 2026-06-24. **No fix-target remains here.**
- ~~**`⟨gate-pass, q⟩` for Sarah-K=2-uniform-sole-dot (Axis 8-Sarah)**: either §11.4.8 specifies a body-resolution side condition (e.g., "if body's path uses sole-dot, `R ⊖ [.../q.]` resolves against the most-recently-flowed-back q"), or Sarah's representation is corrected to use the ordinal at the body, or the case is filed as a fidelity divergence at the system's literal level (parallel to Gap-§11.7.2).~~ **Axis 8-Sarah RESOLVED 2026-06-24** via §11.4.8's full g_k-scoped path discipline. The "ambiguity" was a false alarm from address truncation — the dissertation's full θ-bodies are distinct designations (`[Α/i./o./g_k/q.]` for each g_k); bare `[q.]` is typographic abbreviation per the dissertation's nomenclature subsection ("the dot denotes the only element of its type… no constituents will ever share the same designation"). R-execute reads `R ⊖ cost([Α/i./o./g_k/q.])` with the full path via `q_of(g_k)`. Resolution required no new mechanism — just the correct reading of the dissertation's address semantics. No fix-target remains here.
- **`⟨gate-fail⟩` multi-q-θ-conjunction (Axis 6 Layer C)**: either §11.4.6 admits multi-θ-per-γ declaration (Layer A) or §11.4.7 specifies multi-q gate semantics (Layer B — conjunction-with-failure-witness vs per-θ); either way, R-spawn's target identification becomes rule-licensed rather than inferred.

**Cross-reference for §14 worked-case sections**: the inherited axis labels survive in the table's rightmost column as legacy pointers. §14.3.2 / §14.4.2 / §14.5.2 references to "Axis 1b" still resolve (state: γ_2-body Site (i) AND ε_1-body Site (ii)); "Axis 4" still resolves (state: post-resume operator-attested); "Axis 6" / "Axis 8-Sarah" still resolve. **Axis 2 re-locates to `⟨perceive-failure, C⟩` — its ε-body framing was the phantom, but its content (intention-addition) is real licensed discretion at that state, which is what §14.5 validates. Axis 7 dissolves as a σ-discretion**: per-intention perceiving is the guard-determined `ε-body` state (Pillar 2, not σ), and terminal-only was the Axis-1b Site-(ii) defect artifact, not a cardinality choice. "Axis 3a" merges into the `γ_1-body` single-γ state with Axis 1a (same state, same fork). The §14 sections retain their numbered references for traceability; the catalog now indexes by state.

**Tracked Step-2 action — §14 reconciliation (load-bearing, do not let ride on cross-ref implication)**: §14.5.2 and §14.3.4 currently characterize "Axis 2" as "the ε-body fork — R-perceive precedes R-intention." That characterization is **falsified by this state table** (Axis 2's ε-body framing was the phantom; the real Axis 2 content is intention-addition at `⟨perceive-failure, C⟩`). **Action, executed in the same pass as Step 2's thinning of §13.5.9**: rewrite §14.5.2's "Axis 2 = ε-body fork" sentences to "Axis 2 = intention-addition at `⟨perceive-failure, C⟩` per §1.4.5"; same change in §14.3.4. Without this rewrite, those §14 cross-references dangle against the state table they cite — exactly the contradiction the discipline exists to surface. Tracked here as a concrete action item, not as an implication of the cross-reference paragraph.

#### §1.4.6 What this commits LSPI to

This section says four things the rest of the treatise honors:

1. **LSPI is the formal realization of the maneuver lifecycle, not a free-standing rule system.** Each transition rule realizes a specific epistemic act in the actor's intervention; the rule set's job is to receive the maneuver, not to compute it.
2. **The lifecycle is permissive at the strategic-sequencing surface, just as it is permissive at the guard-firing surface.** Both surfaces are Oracle judgment. Pillar 2 and Pillar 4 are the same boundary from two sides.
3. **An ordering or sequencing question §11.4 leaves open is classified by the strict test of §1.4.5, not by default presumption.** Licensed discretion is an active finding — it requires checking every corpus case's source-verified behavior at that fork against §11.4's admissible firings, and the licensed claim holds only if every case's behavior is reachable under some σ. A defect is the passive observation that at least one case's behavior is unreachable regardless of σ. The "Pillar 2 ∩ Pillar 4 surface" framing is real but must not become a bucket that absorbs genuine defects — the discipline that produced the cut rejects any licensed claim it cannot verify against the rows. The treatise's specification gaps are precisely the forks where the strict test surfaces unreachable source behavior.
4. **The σ at §13.6 carries the Oracle's choices.** Determinism in LSPI is per-σ determinism (≡ oracle-relative determinism, per §2.2 / §13.6: σ = the oracle's choices); the system's permissiveness at the strategic-sequencing surface is what σ measures, **not a hole the formalization should close**. Mechanically closing it would falsify Pillar 2 by making the operator's interpretive judgment something the machine pretends to compute. Per-σ confluence (§13.6) is the precise formal statement: once the oracle's judgments are fixed, the system is deterministic.

The transition rules in §11.4 are written under these commitments. The §11.6 failure family and §11.7 non-destructive family inherit them. The Part IV worked-case validations apply the discretion-vs-defect cut per case. The working register at LPIC-Part-IV-prep.md holds the full editorial history of how the cut was developed across the §14 walks; this section is the resolved statement.

### §1.5 Hard disclaimers

These bear repeating before anything in the treatise can be misread.

**LSPI is not a model of computation.** The transition relation will be well-defined, but its **guards** — does the actor possess `q`? does the target perceive `P.u > X.u`? — are resolved by human interpretive judgment. The dissertation's own words on utility appraisal: "fuzzy," "qualitative," "not replicable." LSPI supplies the structural scaffolding; the operator (consultant or principal) supplies the judgment that fires the guards. The transition steps are not mechanically effective.

This is the boundary between LSPI and λ-calculus / π-calculus / CCS: those calculi reduce mechanically — their reduction relation is decidable by a machine; you can write a normalizer. LSPI does not. An operator advances the configuration based on what they observe in the political environment, and the AI engine records and administers the advance against the system's transition rules. **LSPI is descriptive** of the process it formalizes; it is **not executable**. (Per Pillar 2 / §2.2: the oracle parameter `O` resolves the interpretive guards; the machine guarantees what the machine can guarantee.)

**Never claim "political computation."** Never claim LSPI is "executable" or "effective." The system's rigor is earned — through subject reduction, congruence decidability, resource conservation, strong normalization, and oracle-relative confluence (§13.1–§13.6); mechanical computation is not claimed and is not on offer.

### §1.6 Structure of this treatise

Part I is foundational orientation — vocabulary, families, layered architecture, the global Persistence Invariant. It does not yet specify any rule. Rules appear in Part II.

Part II is the longest part. Each layer gets its own section: Layer 1 grammar (formation rules), Layer 2 type system, Layer 3 structural congruence (the actual axioms), Layer 4 transition relation (the 21 transition rules plus 2 non-firing disciplines), and a complete operator-layer catalog (§12) that cross-indexes rules by operator (primary) and by layer (secondary).

Part III proves what the architecture promised: that the system has the properties it claims. The uniqueness theorem (every constituent has a unique address within an actor's agenda tree) is the load-bearing result; the rest follow.

Part IV grounds the abstract system in the dissertation's actual data. Each of the five worked cases — Charles, Jim, Nathan, Sarah, Rusty — is walked through LSPI's transition relation step by step. Any place LSPI and the dissertation diverge is surfaced explicitly.

Part V hands off to AI engines: how to actually use the system during live PLC engagements.

Part VI closes the audit trail and points at v2.

### For AI engines

This treatise is the operational ground truth for LSPI. When this treatise conflicts with the LPIC-Treatise-Architecture.md (r5) planning document, **this treatise wins** for layer-internal specification (grammar, typing, congruence, transition rules, theorems). The architecture wins for cross-layer choices, design-decision logging, and the operator × layer matrix indexing. When this treatise conflicts with the PLC engine documentation, the PLC engine wins for sphere-level discipline (gates, audit trail, reference-system separation per F9); this treatise wins for LSPI-internal questions (well-formedness, transition, type checking).

---

## §2 Naming and lineage

### §2.1 Origin of the name

The name **Lam System for Political Interaction (LSPI)** is literal: the formal object is an oracle-parameterized state-transition system, and the name says so. §2.2 sets out why the system is deliberately not a calculus and not an algebra; this section records the naming history that landed there.

The system reached its current identity through three architectural revisions, each abandoned for technical reasons:

- **r1 — a compositional-algebra framing.** An earlier framing treated the notation as a typed compositional algebra over cycle constituents. Abandoned: no operator composes two cycles into a larger cycle whose behavior derives from the parts; what appeared compositional was set-membership and path-extension, so the framing was dropped cleanly.
- **r2 — a process-calculus framing.** The next framing inherited π-calculus / Actor-model presentation — structural-congruence-plus-reduction-relation, configurations and small-step transitions, guarded recursion. Abandoned as an identity claim: LSPI's transitions act on a state ⟨C ; M ; S ; R⟩ rather than rewriting terms, and the key guards (perception-validation, σ-discretion, operator-attested premises) are interpretive, not mechanically decidable. The presentation borrows from structural operational semantics (Plotkin) and process-calculus notation; it does not place the system inside the process-calculus family.
- **r3 — *Oracle-parameterized state-transition system* (current; the name follows the object).** The precise object: a typed domain-specific language (the slash-addressing notation) with a small-step structural operational semantics, forming an oracle-parameterized state-transition system, with proven meta-theory (§13.1–§13.6): subject reduction, congruence decidability, resource conservation, strong normalization, and oracle-relative confluence. The oracle `O` resolves the interpretive guards; the meta-theorems hold oracle-relative. Per-σ confluence (§13.6) IS oracle-relative determinism — σ = the oracle's choices. The name **Lam System for Political Interaction** is the literal description of what r3 is.

Documenting these revisions in the open is the command demonstration: a reviewer cannot say the author doesn't know what a calculus or an algebra is when the author rejected both for the correct technical reasons.

Two terms used throughout this treatise should not be conflated:

- **Slash addressing** refers to the path-composition operator family within the system — the slash, the sole-of-type dot, the ordinal suffix, and the scope brackets that delimit paths. The most visible substructure, not the whole.
- **Lam System for Political Interaction (LSPI)** is the name of the whole system as a brand: the typed grammar (§§8–9), the structural congruence (§10), the transition relation (§11), the meta-theorems (§13), and the worked-case validations (§14).

The qualifier *Political Interaction* mirrors the dissertation's central construct, the *interaction cycle*. The eponymous *Lam* credits the methodology author whose 2018 work supplies the load-bearing substrate.

### §2.2 Why it's a System, not a calculus or algebra

The name is **Lam System for Political Interaction** because the formal object is a state-transition system. It is not a calculus and not an algebra, and the choice is deliberate. Three structural grounds rule out those terms:

**1. No compositional term algebra.** A process calculus is built on composition: `P | Q` is a term whose behavior is determined by `P`, `Q`, and the composition operator, and reduction is defined over the term algebra. LSPI has no operator that composes two interactions into a larger interaction whose behavior derives from the parts. The per-intention parallelism §13.6 proves is *interleaving of independent rule-firings on one configuration*, not algebraic composition: configurations don't compose into larger configurations, and cycles don't compose into larger cycles. The system has structure, but it is not a term algebra.

**2. Transitions are state-machine steps on ⟨C ; M ; S ; R⟩, not term-rewriting.** The configuration is an abstract-machine state: `C` is the active-cycle pointer (program counter); `M` is the append-only operation record (log / tape); `S` is the suspended-parent stack (call stack); `R` is the resource multiset (resource store). The twenty-one transition rules step that state forward. They don't rewrite a term into a smaller term whose behavior is the residue of the original; they advance an abstract machine through its phases. There is no compositional calculus *underneath* the machine that the machine reduces — the machine *is* the system.

**3. Guards are oracle-supplied (Pillar 2 — the boundary of computation).** Key transitions gate on judgments only a human can supply: perception-validation (does the realized comparison validate the projected one?), σ-discretion at Bucket-1 forks (which irreversible operator election does the actor make?), operator-attested premises (does the cycle's premise still hold?). These are not decidable from the configuration. A calculus *computes* — its reduction relation is mechanically defined and Church–Rosser is a theorem about that mechanical relation. LSPI describes a process an oracle drives: an explicit oracle `O` parameterizes the transition relation, and the meta-theorems hold *oracle-relative*. This is **Pillar 2** of the treatise — the boundary of computation. Calling LSPI a calculus in the technical sense would actively contradict the central thesis.

**What the system legitimately has** — and what stays under its correct name — is the structural-congruence-plus-transition-relation **presentation** borrowed from structural operational semantics (Plotkin) and process-calculus notation; the typed grammar (§§8–9); the structural congruence over well-typed terms (§10, verified — see §10.2 / §10.5 / the universal-algebra construction of the least equivalence relation closed under congruence containing the three generators A2 / D5 / M4); the constituent vocabulary specialized to political interaction (twenty-one Greek/Latin pairs); the decision-matrix substrate (`M` as a first-class object the rules operate on); the explicit prime modality (`σ′`) distinguishing projected from realized values; the Persistence Invariant governing the audit trail; and the meta-theorems (§13.1–§13.6): subject reduction, congruence decidability, resource conservation, strong normalization, and oracle-relative confluence, all validated against the dissertation's five worked engagements. Borrowing the apparatus does not make the system a calculus; the apparatus is real and correctly applied.

**Prepared answer: "Is your reduction modulo congruence — is your transition relation defined on `≡`-equivalence classes of terms?"** No. The transition relation `⟶` acts on configurations ⟨C ; M ; S ; R⟩, not on terms. Where `⟶` *reads* embedded data terms (paths inside markers, sets in body slots), it reads them up-to the equational identities `≡` provides — paths up-to bracketing (A2), sets up-to member order (D5), root glyph up-to normalization (M4) — exactly as any reasonable system reads its data. This data-respecting behavior is universal (a Turing machine that reads strings up-to a defined string-equivalence is the same case) and confers no calculus-hood. Congruence-quotiented *term-rewriting* is a different shape entirely; LSPI does not have it, because LSPI does not rewrite terms.

**The boundary, stated precisely.** At Layer 3, equational/algebraic vocabulary is honest in full: `≡` is a genuine structural congruence on well-typed LSPI terms in the standard universal-algebra sense (verified by enumeration against §8's BNF — closure holds under every term-forming context by the definitional clause); normalize-then-compare is the proper decision procedure (§13.3); A2 / D5 / M4 are legitimate equational axioms. **This Layer-3 honesty does not cross the layer boundary.** It does not license a system-identity "is a calculus" claim, because reasons (1)–(3) above hold at the system level regardless of what happens inside Layer 3. Equational vocabulary describes how terms relate; the system-identity claim is about how transitions, configurations, and oracle-supplied guards relate. The two stay separate, and that separation is the discipline that keeps the document defensible.

### §2.3 Relationship to the dissertation

The Lam 2018 dissertation is LSPI's **primary source authority**. Every formal claim in this treatise is either derived from explicit dissertation text or logged as a design decision where the dissertation is silent. The architecture document maintains a Design Decisions log (§8 in r5) — twenty-five entries at sign-off, each pointing to its motivation.

The dissertation does not name a calculus. It introduces the notation as a tool for testing theoretical saturation of its grounded-theory model. The notation's purpose, in the dissertation's own words, was "to differentiate between constituents of separate interaction cycles." That purpose is honored throughout LSPI: the uniqueness theorem (Part III §13) is exactly the formal statement of the dissertation's p.164 claim — quoted with its scope intact — that "if done properly by using the correct slash addressing and correct ordinal designation when mapping all elements of all agendas of a single actor, no constituents will ever share the same designation." The scope is **single-actor**, not global; paths are rooted at the agenda (`Α/i./t./...`) and the actor does not appear in the address, so two different actors can both hold `Α/i./t.` without LSPI's grammar contradiction. Cross-actor uniqueness is not claimed and Part III §13 does not attempt to prove it.

The dissertation's five worked case studies (Charles, Jim, Nathan, Sarah, Rusty — Tables 5–22) serve as LSPI's **ground truth**. Part IV walks each case through LSPI's transition relation. If any LSPI rule fails to reproduce a worked-case step, the rule is wrong, not the dissertation.

One known source inconsistency is reconciled at the lexer level: the dissertation's Table 4 assigns Θ to Current Resources, Φ to Obtained Resources, Λ to Obtained Utility, but the worked cases write Θ for all three uses. LSPI adopts Table 4 as canonical and normalizes the worked cases' Θ-overload at the lexer (design decision D-21 in the architecture). The normalization is mechanical from structural context: when Θ is followed by a `/Q.` path it is Φ; when followed by `/U.` it is Λ; otherwise it is Θ.

### §2.4 Relationship to PLC

LSPI is not the same thing as the Political Landscape Cartography (PLC) Operating Volume. PLC is the engagement-level system — the sphere cartridge, the 17-section OPC diagnostic, the 782-tactic catalogue, the principal funnel, the actor cast cartography, the session protocol, the principles, the failure modes. PLC operates at the *engagement* grain; LSPI operates at the *cycle constituent* grain.

LSPI is one of three coexisting reference systems within PLC (per PLC engine ch. 04 §8):

- **LSPI** — for cycle constituents (this treatise).
- **OPC hierarchical IDs** (e.g., `2.1.6.4.2`) — for sphere structural state.
- **Catalogue Reference IDs** (e.g., `0029`, `#8`, `C24`, `Schelling`) — for the tactical corpus.

Mixing them is failure mode F9. LSPI expressions never carry OPC IDs or Catalogue IDs; OPC IDs and Catalogue IDs never appear in LSPI fields.

When PLC's engine documentation conflicts with this treatise, PLC's engine wins for sphere-level concerns (gates, audit trail, reference-system separation). This treatise wins for LSPI-internal questions (well-formedness, transition, type checking).

---

## §3 Methodology — how the system was derived

LSPI was not invented; it was reconstructed. The dissertation contains a notation system; this treatise extracts the formal structure that notation implicitly already had, names what was implicit, and supplies what was missing.

The reconstruction followed a disciplined evidentiary process. Three rules governed:

**Rule 1 — Every formal claim has a source.** A rule, an axiom, or a typing constraint is either:
- Directly quoted from the dissertation,
- Inferred from the dissertation's worked cases by structural analysis (e.g., "no worked case uses ψ with an argument — so ψ is nominal, not an operation"),
- Or logged as a **design decision** where the dissertation is silent.

Twenty-five design decisions accumulated during the architectural process (r1 through r5). Each is logged with its reasoning in the architecture document §8. No design decision is smuggled in unmarked.

**Rule 2 — Worked cases are ground truth.** Each of the dissertation's five interview-derived case studies (Charles/CFO, Jim/John, Nathan/Wanda/Mike/Randy, Sarah/Beth/Srini/Margaret, Rusty/Erik/Gerry/Todd) anchors LSPI's transition relation. If a rule fails to reproduce a worked-case step, the rule is wrong. Part IV §§14.1–14.9 walks each case through LSPI's rules systematically.

**Rule 3 — Surface contradictions, do not paper over them.** Where the dissertation's Table 4 and its worked cases conflict (the Θ/Φ/Λ overload), LSPI declares Table 4 canonical and normalizes the worked cases. Where the dissertation calls `≡` both "definition-by-expansion" (directional) and assumes it's a symmetric equivalence (which contradicts directionality), LSPI splits them into two layers: symmetric `≡` is the structural congruence at Layer 3; directional unfolding is the rule **R-unfold** (a non-firing discipline at Layer 4, reserved for `≡_named` reasoning, not counted among the 21 transition rules — see §13.5.9 Gap-§11.7-non-firing). These reconciliations are logged.

The architectural process produced five revisions (r1 algebra → r2 process calculus → r3 operator-layer matrix → r4 failure family + Persistence Invariant → r5 six content corrections). Each revision was driven by a specific review finding; the cumulative result is the signed-off architecture in `LPIC-Treatise-Architecture.md (r5)`.

This treatise begins from that signed-off architecture. Where this treatise specifies more than the architecture (operational-semantics prose for the transition rules, theorem proofs, worked-case traces), the treatise is the operational ground truth. The architecture remains the skeleton.

---

## §4 The notational metalanguage

LSPI is a formal system, but this treatise is prose about that system. To talk about LSPI we need a metalanguage. The conventions are minimal and unsurprising; they are listed here so they are not improvised case-by-case throughout the treatise.

### §4.1 Metavariables and sorts

- `t`, `t′`, `t1`, `t2`, ... — metavariables ranging over LSPI terms (any well-formed expression).
- `τ`, `σ` — metavariables ranging over sorts (types). The constituent vocabulary in §5 names twenty-one sorts; the structural operators have their own sorts (path-of(σ), set-of(σ), etc.).
- `Σ` — a typing environment: a partial function from free names to sorts. Used in typing judgments of the form `Σ ⊢ t : τ` ("under typing environment Σ, term t has sort τ").

### §4.2 Configurations

A **configuration** is a runtime state — the snapshot that transition rules transform. LSPI's configuration shape is:

```
⟨ C ; M ; S ; R ⟩
```

where:

- `C` is the **active-cycle pointer** — a natural number identifying the currently active cycle. C advances via R-open and R-spawn (new cycle pushed), decreases via R-resume (return to suspended parent); the cycle's constituents themselves live in the operation record `M`, addressed by the cycle's paths, **not** in C. Per-cycle filtering of M by cycle-identity recovers each cycle's full state. Cycle identity is monotonic and recorded structurally by `⟨open, C⟩` markers; the active-pointer C is not (it can return to a parent on resume). See §11.1 for the full pointer/identity discipline; §11.6.11 holds a depth-2 constructed-example trace whose empirical match is now row-verified in §14.3.4 (Nathan's Randy → Wanda → Mike chain, pinning literal at both depths) — the prior attribution to Rusty Tables 16–19 was ruled out by §14.5 (Rusty is depth-1 at every sub-cycle).
- `M` is the **operation record** — an append-only log of declarations and structural markers the cycle produces. Each entry is tagged with the cycle-identity it semantically records (per §11.1's per-rule tagging clause). The Persistence Invariant (§7.5) governs M: no rule rewrites or removes a prior entry; supersession is additive. The dissertation's **decision matrix `Δ`** is a *derived view* folded from M (the current decision-matrix state computed from the history of declarations and ε-modifications), not a configuration slot in its own right — `Δ = fold(M, current-cycle)`. Δ is reconstructible at any point in the past by replaying M up to that point.
- `S` is the **suspended-parent stack** — a LIFO stack of parent cycles that were suspended when their capability-gate failed and they spawned a child. Empty when the current cycle is the root.
- `R` is the actor's **current resource set** — a multiset of resources the actor holds. Read at the capability-gate; written when nested cycles flow obtained resources back.

The decomposition was decided in the architectural process and committed during r4 in response to Q5: without explicit M, the perceive/select rules have nothing to operate on. Sphere-level information and cross-actor graph state remain out of LSPI's scope (deferred to v2).

### §4.3 Transition notation

A single-step transition is written:

```
⟨ C ; M ; S ; R ⟩ ⟶ ⟨ C′ ; M′ ; S′ ; R′ ⟩
```

The reflexive-transitive closure (multi-step transition) is written `⟶*`.

Transition rules are presented in standard inference-rule notation:

```
   premise1     premise2     ...
   ────────────────────────────
              conclusion
```

The premises name the side conditions under which the rule fires; the conclusion gives the configuration transition. Names of rules are prefixed `R-` (e.g., `R-spawn`, `R-perceive-success`). The complete catalog appears in §11 of Part II.

### §4.4 Structural congruence

`t ≡ t′` denotes structural congruence between terms — *not* between configurations. Two terms are congruent if Layer 3's congruence (Part II §10) identifies them. Transition rules treat congruent terms interchangeably; the congruence handles the surface-syntactic variation that does not affect semantic identity.

### §4.5 Auxiliary notation

- `p ⊑ q` — the subpath relation on path terms: `p` is a (possibly improper) prefix of `q`. Used in the uniqueness proof (Part III §13). Defined inductively in Part II §8.
- `o ↦ body` — a `let`-style binding introduced by `R-unfold`. The named operation symbol `ω.k` (the operation being unfolded) is **retained** in the operation record per the Persistence Invariant; `body` is the bound expression that subsequent transitions consult on demand.
- `[a.]·`, `[Α/i./t.]·`, bare `·` — the three agent-attribution dispatch classes (actor-prefixed, target-prefixed, systemic-unprefixed) from architecture §5C.

### §4.6 Character set and encoding

LSPI uses Greek letters (lowercase and uppercase) and Latin letters for its constituent vocabulary, plus standard set-theoretic and mathematical symbols (`∋`, `∌`, `→`, `≡`, `:=`, `′`, `+`, `-`, `<`, `>`, `≤`, `≥`, `=`) for its operators. All symbols use their canonical Unicode codepoints.

**One normalization at the lexer:** the Greek uppercase Alpha (`Α`, U+0391) and the Latin uppercase A (`A`, U+0041) are identified — both refer to Agenda. The two codepoints render identically in most fonts, and the dissertation's worked cases use them interchangeably. After lexer normalization, the LSPI parser sees one symbol.

### For AI engines

When reading or writing LSPI expressions, use the canonical Unicode codepoints (do not substitute ASCII equivalents). When parsing input that may have been hand-typed by a human, accept the documented codepoint variants and normalize. When parsing the dissertation's worked cases, also apply the Θ/Φ/Λ normalization (§5B footnote in the architecture, D-21): `Θ` followed by `/Q.` normalizes to `Φ`; `Θ` followed by `/U.` normalizes to `Λ`; `Θ` in `[a./R.]` context retains as `Θ`.

---

## §5 The 21 typed constituents

LSPI's vocabulary is the twenty-one constituents enumerated in dissertation Table 4. Each constituent has a Greek operator symbol (predicate form) and a Latin set/attribute symbol (subject/object form). The duality is load-bearing: when a theoretical category functions as a predicate, it is rendered in Greek; when it functions as a subject or object, it is rendered in Latin. The dissertation states this explicitly (p. 163).

### §5.1 The vocabulary table

| #  |     Constituent     |   Operation (Greek)    | Set / Attribute (Latin) |                       Sort                      |                  Definition (per dissertation)                   |
|----|---------------------|------------------------|-------------------------|-------------------------------------------------|------------------------------------------------------------------|
|  1 | Actor               | α (lowercase alpha)    | a                       | actor                                           | The individual who initiates the interaction cycle               |
|  2 | Agenda              | Α (uppercase Alpha) †  | A                       | agenda (cycle root)                             | The actor's long-running aim across cycles                       |
|  3 | Target              | τ (lowercase tau)      | t                       | target                                          | The individual who completes the interaction cycle               |
|  4 | Interest            | ι (lowercase iota)     | i                       | interest                                        | What the actor stands to gain from the cycle                     |
|  5 | Detection           | δ (lowercase delta)    | d                       | detection (actor-performed operation)           | Actor's discovery of who controls the desired resource           |
|  6 | Decision Matrix     | Δ (uppercase Delta)    | D                       | matrix structure                                | The target's option × consideration grid                         |
|  7 | Objective           | ω (lowercase omega)    | o                       | objective (actor-performed; projection-bearing) | The actor's target-selection direction                           |
|  8 | Outcome             | Ω (uppercase Omega)    | O                       | outcome (systemic; cycle-bound)                 | The cycle's closure state; one of several possible future states |
|  9 | Intention           | γ (lowercase gamma)    | g                       | intention (actor-performed; multi-instance)     | The specific action chosen to move the target's matrix           |
| 10 | Perception          | Γ (uppercase Gamma)    | G                       | perception (target-performed)                   | How the target views comparative utility before selecting        |
| 11 | Execution           | ε (lowercase epsilon)  | e                       | execution (actor-performed)                     | The actor's action entering the world                            |
| 12 | Selection           | Σ (uppercase Sigma)    | S                       | selection (target-performed)                    | The target's choice from the matrix                              |
| 13 | Preferred Position  | π (lowercase pi)       | P                       | position; member of D                           | The option leading to the actor's desired outcome                |
| 14 | Adverse Alternative | ψ (lowercase psi)      | X                       | alternative; member of D                        | The option leading away from the actor's desired outcome         |
| 15 | Benefit             | β (lowercase beta)     | b                       | consideration (positive)                        | Favorable conditions in the matrix                               |
| 16 | Cost                | κ (lowercase kappa)    | c                       | consideration (negative)                        | Requisite expenditures in the matrix                             |
| 17 | Utility             | λ (lowercase lambda)   | u                       | net consideration                               | Net benefit minus cost per option                                |
| 18 | Required Resources  | θ (lowercase theta)    | q                       | resource designator (actor-performed)           | The resources the actor needs to execute the intention           |
| 19 | Obtained Resources  | Φ (uppercase Phi) ‡    | Q                       | resource gain (actor-side)                      | What the actor obtained from a closed cycle                      |
| 20 | Current Resources   | Θ (uppercase Theta) ‡  | R                       | actor's resource set (a multiset; see §11.1)    | The actor's currently-held resources                             |
| 21 | Obtained Utility    | Λ (uppercase Lambda) ‡ | U                       | utility gain (target-side)                      | Utility realized by the target as a result of the outcome        |

**† Α/A glyph normalization.** The Greek uppercase Alpha (Α, U+0391) and the Latin uppercase A (U+0041) are visually identical in most fonts. The dissertation's worked cases use both interchangeably for Agenda. LSPI normalizes them at the lexer to a single internal token.

**‡ Θ/Φ/Λ source reconciliation.** Table 4 assigns Θ to Current Resources, Φ to Obtained Resources, Λ to Obtained Utility — three distinct operations. The dissertation's worked cases (Tables 5–22) use Θ for all three. The dissertation contradicts itself. LSPI adopts Table 4 as canonical and normalizes the worked cases' Θ-overload at the lexer: when Θ is followed by `/Q.` it is Φ; when followed by `/U.` it is Λ; otherwise it is Θ. This is the most consequential single normalization in LSPI.

### §5.2 Greek/Latin duality

The Greek symbol is the **operation form**; the Latin symbol is the **subject/object form**. Both refer to the same theoretical category. The distinction matters because LSPI's grammar admits each form in different positions:

- An operation form (Greek) takes an argument in round brackets: `δ(Α/i./d.)`, `ω(Α/i./o.)`, `ε(Α/i./o./g./e.)`.
- A subject/object form (Latin) appears in path expressions: `Α/i./t.`, `Α/i./o./g.`, `Α/i./t./D./P.`.

For some constituents the Greek form drives a Layer-4 transition rule (δ → R-detect, ε → R-execute, etc.); for others (α, Α, τ, Δ, π, ψ, β, κ, λ — see footnote in architecture §5B, D-25) the worked cases never use the Greek operation form (Δ in particular appears only as the path-node `D`, never as `Δ(…)`), and LSPI treats those as nominal-only. This partition is exact at the time of writing; if a future revision finds a worked-case operation form for any of these constituents, the partition will be revised before Part II §9 typing is finalized.

### §5.3 Case discipline

Within the Greek family, **uppercase** versus **lowercase** carries information about structural role. The pattern, per dissertation Table 4 and the worked cases:

- **Uppercase Greek** typically denotes aggregate or summary operations: Α (whole Agenda containing interests), Δ (whole Decision Matrix containing positions), Ω (the cycle's systemic Outcome), Γ (the target's holistic Perception of the matrix), Σ (the act of Selection across the matrix), Φ (Obtained Resources flowing back), Θ (the Current Resources set), Λ (Obtained Utility).
- **Lowercase Greek** typically denotes single-instance operations or single-instance constituents: α (a specific actor), ι (a specific interest), δ (a specific Detection event), ω (a specific Objective for one cycle), γ (a specific Intention), ε (a specific Execution), π (a specific Preferred Position within a matrix), ψ (a specific Adverse Alternative), and so on.

The pattern is constituent-specific rather than a strict global aggregate-vs-instance rule. Reading Table 4 by row is the canonical reference; the global pattern is a useful guide but should not be invoked to override what Table 4 specifies for a given constituent.

### §5.4 Domain definitions

The dissertation's full prose definitions of each of the twenty-one constituents (its pp. 151–158) are LSPI's domain semantics. This treatise does not reproduce those definitions in full — they are the substrate, not the system. LSPI's grammar, typing, and transition rules respect the dissertation's domain definitions but do not encode them as formal predicates. Domain definitions live where they originated.

What LSPI encodes formally is **structural** — which terms are well-formed, which are well-typed, which are congruent, which transitions are licensed. The domain-level question "is this Detection sound?" is for the operator; LSPI ensures only that the Detection is *expressible* and *type-correct*.

---

## §6 The structural operators by family

LSPI's structural connectives — the symbols that compose constituents into expressions and govern how those expressions interact — fall into four families. Each family is detailed in Part II §§8–11 (grammar / typing / congruence / transition); this section gives the overview.

### §6.1 Family A — Path operators

Three symbols: the slash `/`, the sole-of-type dot `.`, and the ordinal suffix.

**The slash** is the parent-to-child path separator. A path like `Α/i./t./D./P.` reads "the agenda's only interest's only target's only decision matrix's only preferred position." The slash composes a path by stacking constituents in a parent-child relation. It is left-associative by convention; non-commutative by definition (`a/b ≢ b/a`); non-idempotent in general (`a/a` requires the type system to permit self-containment, which the constituent vocabulary does not).

**The sole-of-type dot** denotes "the only one of this type within the parent set." `P.` reads "the only Preferred Position." When more than one constituent of the same type exists in a parent set, ordinal suffixes disambiguate.

**The ordinal suffix** is a positive integer immediately following a constituent symbol, used to discriminate siblings within a parent set. `X1` and `X2` are the first and second Adverse Alternatives within their common parent Decision Matrix. **Numbering is parent-set-scoped**, not global: `ι.1` in cycle 7 and `ι.1` in cycle 8 are distinct interests in distinct cycles, disambiguated by their full paths. Numbering is **per snapshot**: projected (primed) siblings and realized (unprimed) siblings are completeness-checked separately.

Family A is what the dissertation called "slash addressing." It is the most visible structural family and the one that the uniqueness theorem (Part III §13) primarily depends on.

### §6.2 Family B — Scope operators

Three symbols: square brackets `[ ]`, round brackets `( )`, and curly brackets `{ }`.

**Square brackets** enclose a complete constituent designation: `[Α/i./t.]` is "the target of the agenda's interest." Square-bracketed forms appear wherever a constituent reference is needed in a position that would otherwise be ambiguous.

**Round brackets** enclose an operation's argument: `δ(Α/i./d.)` is "the Detection operation applied to the agenda's interest's detection-target." When a Greek operator is followed by `( ... )`, the contents are the operation's argument.

**Curly brackets** denote sets — either sets of constituents or sets of operations. The members of a curly-bracketed set are unordered (this is the D5 generator of the Layer-3 congruence): `{ A, B } ≡ { B, A }`.

The three bracket types are not interchangeable. Every opening bracket has exactly one matching closing bracket of the same type. Different types can nest (e.g., `{ [A], [B] }`); same types can nest with normalization (`[[t]]` flattens to `[t]` per the B8 nesting-normalization grammar rule in Part II §8).

### §6.3 Family C — Semantic operators

Six symbols, each carrying its own semantic role: the prime `′`, the yields arrow `→`, the equivalence `≡`, the attribution assignment `:=`, and the membership / non-membership pair `∋` / `∌`.

**The prime** distinguishes projected from realized values: `P.1′` is "the projected first Preferred Position" (a forecast); `P.1` is "the realized first Preferred Position" (the observed outcome). Both persist in the record at cycle close per the Persistence Invariant; the forecast is never overwritten by the realization.

**The yields arrow** has two type-dispatched senses. In the projection sense, it yields a projected constituent from an operation: `Σ(M)′ → [Α/i./t./S./P.]′`. In the effect-on-matrix sense, it yields a matrix modification from an Execution: `ε(...) → { [Α/i./t./D./P./b.] + [Α/i./o./g./q.] }`. The two senses are dispatched by type (Part II §9).

**The equivalence** carries two distinct roles that LSPI explicitly splits across layers. As the **structural congruence symbol** (Layer 3 at Part II §10), `≡` denotes the least congruence generated by three LSPI-specific axioms (slash associativity, set-member order-irrelevance, Α/A normalization); symmetry, transitivity, substitution, and reflexivity come for free as properties of being a congruence. As the **definitional-expansion symbol** (used throughout the dissertation's worked cases for Objectives, Intentions, and Outcomes — e.g., `ω.k ≡ { body }`), `≡` is directional: the left-hand side is being defined by the right. LSPI resolves the apparent conflict between symmetric-congruence and directional-definition by handling the latter as the non-destructive **R-unfold** transition rule at Layer 4 (Part II §11), not as a congruence axiom. See §3 Rule 3.

**The attribution assignment** binds a set of constituents to an evaluation by an operation: `[a.]δ(Α/i./d.) := { [Α/i./t.], [Α/i./t./D./P.], [Α/i./t./D./X1], [Α/i./t./D./X2] }` reads "the actor's Detection has been applied to (and produces as its attributes) the target, the preferred position, and the adverse alternative." The right-hand side must be in curly brackets.

**Membership and non-membership** are the capability-gate predicates. `[a./R.] ∋ θ.q` is true when the actor's current resource set contains the required resource; the capability-gate clears. `[a./R.] ∌ θ.q` is true when it does not; the capability-gate fails and a nested cycle spawns. The two are mutually exclusive; both are decidable in constant time.

### §6.4 Family D — Arithmetic and comparison

Several symbols: addition `+`, subtraction `-`, the strict and non-strict inequalities `<` `>` `≤` `≥`, the evaluation equality `=`, and the comma `,` as a set-member separator.

Addition and subtraction modify decision-matrix component values: `[Α/i./t./D./P./b.] + [Α/i./o./g./q.]` is "add the required resource quantity to the preferred position's benefit cell." Subtraction subtracts a quantity from a cell, analogously to addition, and is not commutative (`a - b ≠ b - a`). These operators are restricted to matrix-component types and resource quantities — the type system enforces.

The comparison operators are used in Perception lines to express utility comparisons: `[Α/i./t./D./P./u.] > [Α/i./t./D./X./u.]` is "the preferred position's utility exceeds the adverse alternative's utility" (canonical form, with the target node `t.` between interest and matrix, per the D-26 lexer normalization in §8.2.2 which inserts `t.` when the dissertation's shorthand omits it). Comparisons are restricted to utility values.

The evaluation equality `=` is used in Perception lines to denote a realized comparison.

The comma separates members within `{ }` sets. The set itself is order-irrelevant per D5 (a generator of the Layer-3 congruence).

### §6.5 Agent-attribution prefix (cross-cutting dispatch mechanism)

Distinct from the four structural-connective families is the **agent-attribution prefix** — a cross-cutting dispatch mechanism that precedes operation forms and determines which Layer-4 transition rule fires. It is not a fifth family of structural connectives; it is a mechanism that operates across all four. Three dispatch classes:

- `[a.]·` — actor-prefixed, for operations the actor performs (Detection, Objective-setting, Intention-setting, Execution, Required-Resources designation, Obtained-Resources acquisition).
- `[Α/i./t.]·` — target-prefixed (with the target's full path), for operations the target performs (Perception, Selection, Obtained-Utility realization).
- bare `·` — systemic / unprefixed, for operations that stand alone "as a matter of course for the interaction cycle" (the dissertation's words at p. 164). The Outcome `Ω(Α/i./O.)` is the canonical systemic operation; the worked cases all write Ω without an agent prefix.

The agent-attribution prefix is not a structural connective in the same sense as Families A–D, but it serves a parallel role: it dispatches transition rules. R-detect operates on actor-prefixed δ; R-perceive operates on target-prefixed Γ; R-close operates on systemic Ω. The architecture document treats agent-attribution in its own subsection (§5C of r5); the transition-rule definitions in Part II §11 honor the dispatch.

---

## §7 The five-layer architecture

LSPI's specification has **five interlocking layers** that together define the system. None of the layers is optional. None subsumes another. (LSPI is not a process calculus in the technical sense — see §2.2 for the three structural reasons; the five-layer architecture is borrowed from the process-calculus presentation tradition but does not import the family membership.)

### §7.1 The five layers

**Layer 1 — Grammar (formation rules).** Specifies which strings are well-formed LSPI terms. This is the abstract syntax — the BNF-style production rules that say "an LSPI term is one of: a constituent reference, a slash-composition of terms, a bracketed sub-term, an operation applied to a constituent, ..." Without a grammar, parsing is improvisation.

**Layer 2 — Type system (typing rules).** Specifies which terms are well-typed. The constituent vocabulary in §5 names twenty-one sorts; the operators have their own sorts. A typing rule says, for example: "if `t1 : path-of(τ)` and `t2 : path-of(σ)` are well-typed and `σ` is a valid child of `τ`, then `t1/t2 : path-of(σ)` is well-typed." Type-correct terms are the proper input to transition rules; type-incorrect terms are rejected before transition begins.

**Layer 3 — Structural congruence (axioms).** Specifies when two terms denote the same constituent — that is, when surface-syntactic differences are semantically irrelevant. LSPI's structural congruence is "the least congruence generated by {A2 slash associativity, D5 set-member order-irrelevance, M4 Α/A normalization}." Reflexivity, symmetry, transitivity, and Leibniz substitution come for free as properties of being a congruence. This is the *only* layer where "axiom" is the right word.

**Layer 4 — Transition relation (transition rules).** Specifies how a configuration evolves: how the actor opens a cycle, performs Detection, sets an Objective, runs an Execution, the target Perceives, Selects, the cycle closes, resources flow back. **Twenty-one transition rules in LSPI v1, plus two non-firing disciplines** (R-unfold as the directional substitution device the metatheory invokes; R-prime-preserve as an invariant clause the C-transitioning rules satisfy), presented in standard inference-rule notation. This is the **dynamic** layer of the system — the layer that distinguishes a state-transition system from a mere notation.

**Layer 5 — Theorems (metatheory).** Properties proved *from* the previous four layers. Uniqueness of constituent addresses, closure of well-formedness under transitions, decidability of well-formedness, preservation of typing under transitions, conservation of resources across nested cycles. Theorems are not asserted as part of the system; they are derived.

### §7.2 How the layers compose

A term, in LSPI, passes through the layers as follows:

1. A string is parsed against the **grammar** (Layer 1). If it's not well-formed, parsing fails.
2. The parsed term is **type-checked** against the type system (Layer 2). If it's not well-typed, type-checking fails.
3. Two well-typed terms can be compared for **structural congruence** (Layer 3). Congruent terms are treated as equal by all subsequent layers.
4. A well-typed term that appears in a configuration can undergo **transition** (Layer 4). Transition produces a new configuration containing new (or modified) terms, which themselves must be well-formed and well-typed.
5. **Theorems** (Layer 5) guarantee that this process is well-behaved: parsing terminates, type-checking is decidable, congruence is decidable, transition preserves well-formedness and typing, the resource set conserves correctly across nested cycles, and so on.

The layered architecture means that errors are caught at the right layer. A syntactically malformed term is rejected at parsing without further analysis. A well-formed but ill-typed term is rejected at type-checking. A well-typed term that participates in an attempted transition step that no rule licenses produces no transition (the configuration is stuck — which, for an interpretive system like LSPI, means the operator's interpretive judgment must intervene).

### §7.3 What lives where

This is the cross-reference index for the rest of the treatise.

- **Layer 1** lives in Part II §8. Formation rules for constituents, slash composition, brackets, prime suffixing, operation forms, agent-attribution prefixes, ordinal numbering, vocabulary closure.
- **Layer 2** lives in Part II §9. Typing rules for each operator and operation; sort signatures; agent-prefix dispatch typing; the lexer-level normalizations (M4 Α/A, D-21 Θ/Φ/Λ).
- **Layer 3** lives in Part II §10. The least congruence generated by {A2, D5, M4}, with the explicit statement that A3, A4, C11 are *consequences* of the congruence's thinness rather than separate axioms.
- **Layer 4** lives in Part II §11. The twenty-one transition rules plus the two non-firing disciplines (R-unfold, R-prime-preserve), presented in inference-rule notation with worked-case validation pointers.
- **Layer 5** lives in Part III §§13–19. Proofs of uniqueness, closure, preservation, decidability, conservation, termination bounds, and explicit non-claims.

### For AI engines

When given an LSPI expression to process, run the layers in order: (1) parse, (2) type-check, (3) check for congruence with any reference term being compared, (4) apply transition if the expression appears in a configuration that licenses a transition, (5) invoke theorem-supported properties (e.g., the uniqueness guarantee) as needed. If any layer rejects the input, do not silently coerce — surface the rejection to the operator with a citation to the rule that was violated.

---

## §7.5 The Persistence Invariant (global meta-principle)

LSPI commits to a single global discipline that cuts across every layer: **nothing in LSPI's operation record is destructively overwritten. Supersession is additive.**

This is hard guardrail 6 in the architecture document; it is the discipline that distinguishes LSPI from a system that would discard old states as it advances. LSPI retains everything: every projection, every realization, every body bound by R-unfold, every revised objective, every spawn-trigger event. The audit trail of the cycle is the cycle.

### §7.5.1 Three instances

The Persistence Invariant manifests as three specific supersession-additive commitments across the transition relation:

**R-prime-preserve (Part II §11.7.3).** At cycle close, both the projected constituent (`σ.k′`) and the realized constituent (`σ.k`) are preserved in the cycle's record. The projection is never destroyed by the realization. This is what makes forecast-vs-realized calibration possible: comparing P.n′ to P.n requires both to exist.

**R-unfold non-destructive (Part II §11.7.1).** When an Objective, Intention, or Outcome definition is unfolded for evaluation (`ω.k ≡ { body }`), the operation symbol `ω.k` is *retained* in the operation record; the body is bound additively as `o ↦ body`. The name remains addressable. The body is available on demand. Subsequent transitions use the binding without destroying the name.

**R-objective-revise non-destructive (Part II §11.7.2).** When an Objective is revised mid-cycle (Sarah Table 14: Sarah's read of Srini changes; she revises her objective from "convince him to lose" to "convince him to step out"), the revision rebinds `o ↦ body′`. The old `body` is **retained as superseded**, not deleted. The historical record contains both bodies and the revision event.

**Related but distinct: Theorem 13.1 (Part III §13.1).** The dissertation's p.164 uniqueness claim — every constituent in an actor's agenda tree has a unique slash-addressed designation — is a Layer-5 theorem **proved from** the addressing scheme plus the per-rule freshness premises (§11.4.2's iN, §11.4.3's Xk/Pk, §11.4.5's g_k). It is **guaranteed by §13.1 but is not itself a non-destructive supersession commitment** — it is a uniqueness property of the addressing, not an additive-supersession property of the operation record. Earlier drafts listed it as the fourth instance of the Persistence Invariant; it is properly classified as a downstream theorem, not a manifestation.

### §7.5.2 What the Invariant does and does not govern

**The Invariant governs `M`.** Under the configuration `⟨ C ; M ; S ; R ⟩` settled in §4.2, `M` is the **operation record** — the append-only log of declarations and structural markers the cycle produces. The Persistence Invariant fully governs M: every transition rule's contractum is `M ⊎ (new entry)`; no rule rewrites or removes a prior entry; supersession is additive (R-objective-revise appends the revised body alongside the original; R-unfold appends the unfold marker alongside the named declaration). This is what makes M's monotonicity load-bearing across §11's twenty-one transition rules.

**The dissertation's decision matrix `Δ` is a derived view, not a governed slot.** Δ — the current state of the options/considerations/components — is a **fold over M**: `Δ = fold(M, current-cycle)`. Recomputing Δ as the cycle's ε-Executions and matrix-modifications land in M is not destructive overwriting; it is the matrix being re-derived from its audit-traced history. Every ε-modification that contributed to Δ persists as an ε-declaration in M (per R-execute, §11.4.8), so any past state of Δ is reconstructible by replaying M up to that point. The Invariant governs the source-of-truth (M); Δ inherits its persistence by being a fold over a governed source.

**`S` and `R` follow the same discipline.** The suspended-parent stack and the resource set are runtime structures mutated by R-spawn, R-close-nested, R-resume, R-execute, R-flowback. Those mutations are not Persistence Invariant violations because the operation events that triggered them — the `∌` non-membership at the gate (recorded by `⟨gate-fail, q⟩` per §11.6.2), the `Φ.q` obtained resource at flowback (recorded by Φ + `⟨flowback-recorded, E⟩` per §11.4.14) — persist in M as the source-of-truth. S and R are derived state; M is the record.

**Architectural note.** Earlier drafts of §7.5.2 stated that the Invariant did *not* govern M (treating M as the derived matrix Δ and citing three rules — R-execute-modify, R-execute-restructure, R-matrix-restructure — that "legitimately mutated" it). Those three rules were holdovers from an earlier mutable-matrix design that §11 does not adopt; the present §11 has one R-execute (§11.4.8) that *appends* an ε-declaration to M rather than mutating a matrix grid in place. The reconciliation puts Δ outside the configuration slot list (as a derived fold) and assigns the slot M to the operation record, restoring consistency between §4.2's configuration definition and §11's transition-rule discipline. The architecture's guardrail 6 reads (verbatim from r5 line 42): "Nothing in LSPI's **constituent/operation record** is destructively overwritten; supersession is additive." — that discipline is exactly the discipline M satisfies under this reconciliation: every transition-rule contractum is `M ⊎ (new entry)` (append-only), and supersession is additive (R-objective-revise appends the revised body alongside the original; R-unfold appends the unfold marker alongside the named declaration). The architecture also needs the M-redefinition propagated into its own r5 references to "the derived running matrix M" — those refer to what is now called Δ (the derived view) under this reconciliation; see the propagation note at the architecture doc.

### §7.5.3 Operational rationale

Why this discipline? Two reasons.

**Forecast calibration requires both projected and realized values to persist.** The dissertation's perception-gap discipline operationalized as forecast calibration depends on being able to compare `P.n′` to `P.n` at any point in the engagement. If the realization overwrote the projection, the comparison would be impossible. The Persistence Invariant is what makes calibration tractable.

**The audit trail is the consultant's durable practice capital.** Across many cycles, across many engagements, the consultant accumulates patterns of what actually happens versus what was projected. Those patterns require a substrate that does not lose history. The Persistence Invariant is the architectural commitment that the substrate keeps what it produces.

### §7.5.4 Implication for future LSPI extensions

Any future transition rule proposed for LSPI v2 or beyond must be designed to supersede additively. A rule that destructively overwrites a constituent or a binding is a hard violation of guardrail 6 and is rejected on architectural grounds. v2 candidates (behavioral equivalence, name binding, parallel composition, multi-level abandonment cascade) will be evaluated against this constraint when they enter the design process.

### For AI engines

When an operator asks "what was the matrix before Sarah's third move?" — replay the operation log; do not query a separately-stored historical M. When an operator asks "what was Bob's projected read of Sasha at cycle 4?" — read `[Α/i./t./D./P.]′` from cycle 4's record; the projection persists. When the operator asks "what did Sarah's objective look like before she revised it?" — read the superseded `body₁` binding; it is in the record. The log is the source of truth.

---

# End of Part I — signed off

Part I is signed off. One carry-forward concern logged in the architecture document (§11.1): Part V (operational guidance) must specify how an AI engine keys constituents by *owning-actor + path*, since LSPI paths do not embed the actor and cross-actor uniqueness requires both keys. Part V §§27–31 will address.

---

# Part II — The System by Layer

Part II is the longest part of the treatise. It specifies LSPI layer by layer, in the order an expression travels through the system: first the grammar that says which strings are well-formed terms (§8), then the type system that says which terms are well-typed (§9), then the structural congruence that says which terms are interchangeable (§10), then the transition relation that says how a configuration evolves (§11), and finally a complete catalog cross-indexed by operator and by layer (§12).

The architecture's primary view of the system is the operator × layer matrix (architecture §5A–§5C). Part II follows the dual indexing: by layer here (each section is one layer), with operators woven through. §12 closes Part II with the matrix-style catalog.

---

## §8 Layer 1 — Grammar (Formation Rules)

### §8.1 What Layer 1 specifies

Layer 1 specifies *which strings of LSPI characters are well-formed terms*. It is the grammar of the system — the precise statement of which symbols can appear, in which positions, in which combinations, to produce something the rest of the system is prepared to reason about. A string that satisfies Layer 1 is a **well-formed term** and is eligible for the type checking of Layer 2. A string that does not is rejected at parsing; type-checking, congruence-checking, and transitions never see it.

This section presents the grammar in two complementary forms:

1. **BNF productions** for the context-free skeleton — the parts of LSPI's syntax that depend only on local structure.
2. **Inference rules and side conditions** for the context-sensitive parts — the parts of LSPI's syntax that depend on the surrounding term (sibling completeness, parent-set-scoped numbering, vocabulary closure).

Both forms are equally normative. Where a BNF production and an inference rule appear to specify the same thing, the inference rule takes priority — it carries the side conditions that the BNF cannot express.

**The well-formedness judgment** is written:

```
⊢ t : term
```

read "term `t` is well-formed." When the context matters (typically because a side condition references a parent or a sibling set), the judgment expands to `Γ ⊢ t : term` where `Γ` is a context recording the relevant surrounding structure.

### §8.2 The lexical layer

Before parsing produces terms, the **lexer** produces tokens from the input character stream. LSPI's lexical layer is small but carries two consequential normalizations.

#### §8.2.1 Character set

LSPI source text uses Unicode. Three character classes:

- **Greek letters**: α β γ δ ε ζ η θ ι κ λ μ ξ ο π ρ ς σ τ υ φ χ ψ ω (lowercase); Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Σ Τ Υ Φ Χ Ψ Ω (uppercase). LSPI uses only the subset listed in Part I §5.1: α, Α, τ, ι, δ, Δ, ω, Ω, γ, Γ, ε, Σ, π, ψ, β, κ, λ, θ, Φ, Θ, Λ. Other Greek letters are not in LSPI's vocabulary and will be rejected by M5 (constituent vocabulary closure, §8.7).
- **Latin letters**: a, A, t, i, d, D, o, O, g, G, e, S, P, X, b, c, u, q, Q, R, U. As with Greek, only the subset in Table 4.
- **Symbols and punctuation**: `/`, `.`, `[`, `]`, `(`, `)`, `{`, `}`, `:`, `=`, `→`, `≡`, `∋`, `∌`, `′` (prime), `+`, `-`, `<`, `>`, `≤`, `≥`, `,` (comma), plus numerals 0–9 for ordinal suffixes.

Whitespace is non-significant between tokens. Whitespace inside an operation form's argument (`δ(...)`) and inside a bracketed designation (`[...]`) is also non-significant. Whitespace inside a numeric ordinal suffix is forbidden — `X 1` is two tokens, not the ordinal `X1`.

#### §8.2.2 Lexer normalizations

The lexer applies five normalizations before yielding tokens to the parser. The normalizations are **confluent** — they may be applied in any order and produce the same canonical result. Pattern targets: M4 fires on the Α/A character; D-21 fires on Greek Θ followed by `/Q.` or `/U.`; D-26 fires on `/i?./D./` (where `?` is empty for sole-dot or any numeric ordinal — the generalization that handles both pre- and post-D-28 interest-segments, restoring D-26/D-28 commutativity); D-27 fires on `/t./G.`; D-28 fires on the **agenda-root sole-dot interest, glyph-agnostic** — it matches both `A/i.` (Latin A) and `Α/i.` (Greek Α), so D-28 and M4 commute regardless of which order fires first (without glyph-agnosticism, D-28-first on `A/i./...` would no-op and leave the sole-dot in place after M4 normalizes the glyph; with glyph-agnosticism, D-28 sees the agenda root in either rendering and fires). D-28 applies **only at the agenda root** — sub-cycle sole-dot interests are not affected. Two pairwise commutativity-restoring generalizations together make the five-rule set genuinely confluent: D-26's `/i?./D./` (handles D-26/D-28) and D-28's glyph-agnostic root-match (handles M4/D-28). An implementer may apply the five as a single ordered pass (M4 → D-21 → D-26 → D-27 → D-28 is conventional and what the worked-case validation in Part IV assumes) or interleave them without affecting the result. The convergence is verified against the worked cases on three representative pairs: (a) **D-26/D-27** on the two Perception forms — the realized Perception `/i./D./G.` canonicalizes via D-26 alone (D-27's `/t./G.` pattern never matches this input since no `t` node exists yet), and the projected Perception `/i./t./G.` canonicalizes via D-27 alone (D-26's `/i./D./` pattern never matches this input since no matrix node appears immediately under interest) — **neither input triggers both rules**, so the pair commutes trivially regardless of order; (b) **D-26/D-28** on agenda-root sole-dot `Α/i./D./P./u.` reaches canonical `Α/i1/t./D./P./u.` regardless of order (D-26 then D-28: `Α/i./D./P./u.` → `Α/i./t./D./P./u.` → `Α/i1/t./D./P./u.`; D-28 then D-26: `Α/i./D./P./u.` → `Α/i1/D./P./u.` → `Α/i1/t./D./P./u.`); (c) **M4/D-28** on Latin-rendered agenda root `A/i./...` reaches canonical `Α/i1/...` regardless of order (M4 then D-28: `A/i./...` → `Α/i./...` → `Α/i1/...`; D-28 then M4: `A/i./...` → `A/i1/...` via glyph-agnostic D-28 → `Α/i1/...` via M4). The remaining seven pairs of the ten total are trivially disjoint (D-21 shares no node with the other four; D-27's `/t./G.` shares no node with the root or D-26's `/i./D./` pattern).

**M4 — Α/A glyph normalization.** The Greek uppercase Alpha (`Α`, U+0391) and the Latin uppercase A (`A`, U+0041) render identically in most fonts and the dissertation's worked cases use both interchangeably for the Agenda constituent. The lexer maps both to a single internal token (denoted in this treatise as `Α` for clarity, but neither rendering is preferred or required in source text).

**D-21 — Θ/Φ/Λ source-reconciliation normalization.** Per Part I §5.1 footnote ‡: the dissertation's Table 4 assigns Θ to Current Resources, Φ to Obtained Resources, Λ to Obtained Utility, but the worked cases write Θ for all three. The lexer disambiguates structurally:

- `Θ` followed by an argument path ending in `/Q.` → tokenize as **Φ** (Obtained Resources).
- `Θ` followed by an argument path ending in `/U.` → tokenize as **Λ** (Obtained Utility).
- `Θ` in any other position (notably `[a./R.]` membership contexts, where it denotes Current Resources) → tokenize as **Θ**.

The disambiguation is mechanical from the structural context and applies to source-text input that follows the dissertation's overload convention; LSPI's own canonical output uses Φ/Λ/Θ correctly per Table 4 and does not need re-normalization.

**D-26 — Matrix-path shorthand normalization.** A sweep of Tables 5–22 shows two patterns for the Decision Matrix in path expressions:

- The **canonical form** `Α/i./t./D./...` — interest → target → matrix → ... (60 occurrences across the worked cases).
- The **shorthand** `Α/i./D./...` — interest → matrix → ... with the target node implicit (21 occurrences, primarily in realized Perception lines like `[Α/i./D./P./u.] > [Α/i./D./X./u.]`).

Both forms refer to the same semantic constituent (the target's decision matrix); Table 4 defines the matrix as "the target's option × consideration grid," which makes `Α/i./t./D./...` the structurally canonical address. The lexer normalizes the shorthand to canonical:

- `/i?./D./` → `/i?./t./D./` where `?` is either empty (sole-dot `/i./`, the dissertation's pre-D-28 surface form) or a numeric ordinal (`/iN./`, the post-D-28 canonical form). Insert the target node when matrix appears immediately under any interest, sole-dot or numbered, with no intervening target.
- The rule applies at every interest depth: `/i?./o./gN/i./D./` → `/i?./o./gN/i./t./D./` for nested-cycle paths (the inner `/i./` is sub-cycle sole-dot per A6, unaffected by D-28; the outer interest-segment may be either sole-dot or numbered).
- **D-26 covers both sole-dot and numbered interest-segments** so that D-26 and D-28 are commutative on `Α/i./D./...` paths and the lexer's confluence property is preserved (see the confluence note in §8.2.2). Under the original sole-dot-only D-26, applying D-28 first would rewrite `Α/i./D./...` to `Α/iN/D./...` and the original D-26 pattern `/i./D./` would no longer match — breaking confluence on the D-26 / D-28 pair. The generalized form fires on both surface and post-D-28 patterns, restoring genuine order-independence.

After D-26 normalization, every matrix-bearing path in the post-lexer corpus is in canonical form. The child-class lattice (§9.3.1) admits matrix as a child of `target` only; the D-26 normalization is what makes the lattice's tightness consistent with the dissertation's surface shorthand.

**Soundness precondition for D-26.** D-26 inserts the sole-form `t.` (not an ordinal-bearing `tN`). This is sound iff every interest in the dissertation's worked cases has exactly one target — which is the dissertation's actor → single-target structure of the interaction cycle (Tables 4–22 are uniformly single-target per cycle; multi-target interactions are modeled as separate interest cycles in a parent's nested-interest tree). The normalization is therefore deterministic; if a future LSPI extension admits multi-target cycles per interest, D-26 would need to be revised to use ordinal-bearing `tN` and the insertion rule would no longer be unique.

**D-27 — Perception-path canonicalization.** A sweep of Γ-argument occurrences in Tables 5–22 shows two patterns terminating at the perception node `G.`:

- The **realized Perception form** `Γ(Α/[path]/i./D./G.)` — perception under matrix, target node implicit (14 occurrences across realized Perception rows). After D-26 normalization: `Γ(Α/[path]/i./t./D./G.)`.
- The **projected Perception form** `Γ(Α/[path]/i./t./G.)′` — perception directly under target, matrix node implicit (17 occurrences across Intention-body projection forms).

Both refer to the same semantic constituent: "the target's perception of the matrix" (Table 4 #10 — "how the target views the comparative utility between the options"). The matrix-bearing form is canonical because Perception is *of* the matrix. The lexer normalizes the projected shorthand to canonical:

- `/t./G.` (target followed directly by perception) → `/t./D./G.` (insert matrix node between target and perception)
- The rule applies at every cycle depth; the `/t./G.` pattern only ever occurs in Γ arguments (G is exclusively a Perception path node, and Perception arguments are the only context where `/t./G.` appears), so the normalization is unambiguous.

After D-27 normalization, every Γ argument in the post-lexer corpus terminates at `/t./D./G.` (canonical form). The child-class lattice (§9.3.1) admits `perception` as a child of `matrix` only; `target` does not admit `perception` directly. D-27 makes the lattice's tightness consistent with the dissertation's projection-shorthand convention.

**Soundness precondition for D-27.** Same as D-26's: single target per interest. Additionally, D-27 assumes that wherever the dissertation writes `Γ(.../t./G.)` projectively, it semantically refers to the perception of the matrix that target holds — which is consistent with every Intention-body usage in Tables 5–22 (Charles T5, Jim T6, Nathan T7–T11, Sarah T12–T15, Rusty T16–T20).

**D-28 — Agenda-root interest normalization.** A sweep of top-level interest declarations across Tables 5–22 shows the dissertation writes `Α/i.` (sole-of-type) for the agenda-root interest of every documented worked case, because every documented engagement runs a single top-level cycle per actor. This surface form is correct under A6 (sole-of-type valid when no siblings) at N=1, but is **ill-formed for any multi-cycle agenda**: a second top-level cycle would need to introduce `Α/i2` per A7's ordinal designator discipline, which would violate A9 (sibling completeness — `i2` requires `i1` to exist in the same parent set) and contradict A6 (the original `i.` would no longer be sole-of-type once `i2` appeared). And append-only M (§7.5) forbids retroactively rewriting cycle 1's `i.` to `i1` when the second cycle opens — so the "first sole-dot, later numbered" encoding is structurally unavailable.

The lexer normalizes the agenda-root sole-dot to its ordinal-numbered form:

- `[A|Α]/i.` at the agenda root → `[A|Α]/i1` (the sole-dot is reinterpreted as the surface form of the N=1 ordinal-numbered interest). **D-28 is glyph-agnostic at the root** — it pattern-matches the agenda root regardless of whether the dissertation writes Latin `A` or Greek `Α` for the agenda constituent. This is what makes M4 and D-28 commute on agenda-root paths (see the confluence note above): M4 then D-28 normalizes the glyph first then the sole-dot; D-28 then M4 normalizes the sole-dot first then the glyph; both reach the same canonical `Α/i1/...`.

The rule applies **only at the agenda root** — sub-cycle interests at `parent-prefix/i.` retain sole-dot under A6, because the parent-prefix already discriminates sub-cycles from siblings and only one interest exists per sub-cycle's scope (§11.4.2's sub-cycle branch). Charles T5's `[a.]ι(Α/i.) := { [Α/i./Q.] }` is read post-D-28 as `[a.]ι(Α/i1) := { [Α/i1/Q.] }`, and a hypothetical second cycle of Charles's actor would write `Α/i2` from the start — A9 and A6 both satisfied uniformly.

**Soundness precondition for D-28.** D-28 is sound iff the agenda-root sole-dot always refers to the actor's first top-level cycle (N=1) — which is the dissertation's convention (every worked-case actor runs one top-level cycle and uses sole-dot for that one cycle's interest). The post-lexer form is uniformly ordinal-numbered across top-level interests, which is what Theorem 13.1's (W) layer 1 reasons over. Sub-cycle interests are not affected — sole-dot inside a parent-prefix remains sole-dot, and (W) at the sub-cycle layer is enforced by the parent-prefix's own discriminator.

### §8.3 Sorts

Layer 1's formation rules are organized around **sorts** — the type universe Layer 2 will reason over. Layer 1 declares the sorts; Layer 2 uses them.

#### §8.3.1 Constituent sorts

Each of the 21 constituents in Part I §5.1 declares a sort. The sort name is the lowercase form of the constituent's English name:

|     Constituent     |         Sort        |
|---------------------|---------------------|
| Actor               | `actor`             |
| Agenda              | `agenda`            |
| Target              | `target`            |
| Interest            | `interest`          |
| Detection           | `detection`         |
| Decision Matrix     | `matrix`            |
| Objective           | `objective`         |
| Outcome             | `outcome`           |
| Intention           | `intention`         |
| Perception          | `perception`        |
| Execution           | `execution`         |
| Selection           | `selection`         |
| Preferred Position  | `position`          |
| Adverse Alternative | `alternative`       |
| Benefit             | `benefit`           |
| Cost                | `cost`              |
| Utility             | `utility`           |
| Required Resources  | `resource-required` |
| Obtained Resources  | `resource-obtained` |
| Current Resources   | `resource-set`      |
| Obtained Utility    | `utility-obtained`  |

#### §8.3.2 Compound sort constructors

Layer 1 introduces three compound sort constructors used in formation:

- `path-of(σ)` — a path designating a constituent of sort `σ`. A path-of(`position`) is a path that resolves to a Preferred Position; the slash composition rule produces values of `path-of(σ)`.
- `op-form(σ)` — an operation form applied to an argument of sort `σ`. `δ(Α/i./d.)` has sort `op-form(detection)`.
- `set-of(σ)` — a curly-bracketed set whose members all have sort `σ`. `{ [Α/i./t.], [Α/i./t./D./P.] }` has sort `set-of(constituent-ref)`.

The full sort universe includes these compound sorts plus the 21 constituent sorts plus a small number of auxiliary sorts (`ordinal`, `actor-prefix`, `target-prefix`, `boolean` — used in the predicate forms). Section §8.7 enumerates the closure.

### §8.4 Formation rules by family

#### §8.4.1 Family A — Path operators

**A1 — Slash composition (binary).**

```
   ⊢ t1 : path-of(τ)       ⊢ t2 : constituent-of-τ-child-class
   ────────────────────────────────────────────────────────────
                ⊢ t1/t2 : path-of(sort-of(t2))
```

The slash composes a parent path `t1` with a child constituent `t2` to yield a longer path. The premise "constituent-of-τ-child-class" expresses that `t2` must be a legal child constituent under `τ` (Layer 2 specifies the child-class lattice; Layer 1 only requires that the relation exist). Left-associativity is a parser convention; semantically the slash is associative (Layer 3 axiom A2).

**A5 — Sole-of-type dot suffix (unary).**

```
   ⊢ σ : constituent-symbol
   ────────────────────────
       ⊢ σ. : constituent-ref
```

The dot suffix produces a constituent-reference asserting "the only constituent of this type in the current parent set." Examples: `P.`, `i.`, `o.`.

**A6 — Dot / ordinal exclusion.** The dot suffix and the numeric ordinal suffix are mutually exclusive on the same symbol at the same path position. The grammar admits exactly one or the other:

```
   ⟨constituent-ref⟩ ::= ⟨symbol⟩ "." | ⟨symbol⟩ ⟨ordinal⟩
```

`P.1` is a parse error; either `P.` (sole) or `P1` (the first of multiple) is permitted but not both.

**A7 — Ordinal range.** The ordinal suffix is a positive integer:

```
   ⟨ordinal⟩ ::= "1" | "2" | "3" | ... | n ∈ ℕ⁺
```

Zero, negatives, and decimals are rejected.

**A8 — Parent-set-scoped numbering (side condition on path resolution).**

```
   ⊢ p : path-of(parent-sort)       σN appears within p's child-set position
   ──────────────────────────────────────────────────────────────────────────
   the ordinal N is scoped to p's child-set, not to any larger context
```

In particular, `ι.1` within cycle 7 and `ι.1` within cycle 8 denote different interests when their full paths differ; the ordinal alone does not disambiguate across cycles. This is the side condition that makes the per-actor uniqueness theorem (Part III §13) provable.

**A9 — Sibling completeness per snapshot (side condition).**

```
   if σN appears in a parent set, and N > 1,
   then σ1, σ2, ..., σ(N-1) must all appear in the same parent set
   ── checked separately for the projected (primed) and realized snapshots ──
```

The check is **per snapshot**: the projected siblings (`σ1′, σ2′, ...`) and the realized siblings (`σ1, σ2, ...`) are completeness-checked independently. A configuration that holds a projected `X2′` without `X1′` is malformed; the same configuration may legitimately have not yet realized any `Xn`.

**A13 — Path depth (definitional).** The depth of a path `t1/t2/.../tk` is `k`. Depth is well-defined by induction on the slash-composition.

**A14 — Root anchoring.**

```
   ⟨path⟩ ::= ⟨root-anchor⟩                                -- single-segment path
           |  ⟨root-anchor⟩ "/" ⟨constituent-ref-chain⟩     -- multi-segment path
   ⟨root-anchor⟩ ::= "Α" | "a."
```

Every well-formed path begins with either the Agenda symbol `Α` (when the path is rooted in the agenda tree, the typical case) or the actor symbol `a.` (when the path is rooted in the actor's resource set or other actor-bound structure, as in `[a./R.]` membership tests). Paths that lack a root anchor are malformed.

**Single-segment paths admit `[a.]` and `[Α]` as designations.** A path that is just its root-anchor is well-formed. This is what makes the dissertation's `[a.]` actor prefix a legitimate designation: `a.` is the path, and `[a.]` is the bracketed designation enclosing that path. Without the single-segment alternative, `[a.]` would parse as a bracketed constituent-ref — but `a.` is a root-anchor, not a constituent-ref, so that path is closed. The single-segment alternative is the resolution.

**A4 (rejected at Layer 2 — noted here for locality).** Slash composition is non-idempotent: `a/a` is not well-formed because no constituent in LSPI's vocabulary is its own legal child. **The enforcement happens at Layer 2** via the child-class typing premise of A1 (the constituent-of-τ-child-class requirement), not at Layer 1 — Layer 1 admits the syntactic form `t1/t2` for any t1, t2 of compatible bracket structure and pushes the child-class compatibility check to typing (§9). A4 is recorded here for locality, since the consequence is most readable alongside A1, but the rejecting layer is §9.

#### §8.4.2 Family B — Scope operators

**B1 — Square brackets enclose a constituent designation (rooted-path content).**

```
   ⊢ t : path
   ──────────────────────────────────
   ⊢ [t] : constituent-designation
```

A square-bracketed term is a complete constituent reference, usable in any position that calls for a constituent-designation. **The content must be a fully-rooted path** — including the single-segment-path case where the path is just the root-anchor (`[a.]`, `[Α]`). Examples: `[Α/i./t.]`, `[a.]` (single-segment), `[a./R.]`. Bare constituent-refs without a root anchor are not bracketed as designations; the worked cases never use such forms.

**B2 — Round brackets enclose an operation's argument (rooted-path content).**

```
   ⊢ op : op-symbol       ⊢ t : path
   ─────────────────────────────────
        ⊢ op(t) : op-form(sort-of(t))
```

Round brackets immediately follow a Greek operator and contain the operation's argument. **The argument must be a fully-rooted path** (the A8 parent-set-scoping side condition requires a parent context, which a rootless constituent-ref does not supply). Examples: `δ(Α/i./d.)`, `ω(Α/i./o.)`.

**B3 — Curly brackets denote sets.**

```
   ⊢ t1 : σ       ⊢ t2 : σ       ...
   ─────────────────────────────────
   ⊢ { t1, t2, ... } : set-of(σ)
```

Curly brackets enclose a comma-separated list of terms of a common sort. Singleton sets are well-formed (`{ t }` is set-of(sort-of(t))).

**B4 — Bracket types are non-interchangeable.** `[`, `(`, `{` are three distinct opening brackets; `]`, `)`, `}` are the three corresponding closers. A bracket pair must match in type. `[t)` is a parse error.

**B5 — Bracket pairs balance.** Every opening bracket has exactly one matching closing bracket of the same type, in the correct nesting order.

**B6 — Brackets nest without type-mixing of openers and closers in a single pair.** `[ ( ] )` is a parse error. `[ ( ) ]` is well-formed.

**B7 — The semantic role of a bracket pair is dispositive at parse time from the preceding operator context.** A round-bracket pair following a Greek operator is the operation's argument (per B2); a round-bracket pair appearing elsewhere is malformed at Layer 1 (LSPI does not use parentheses for grouping outside operation forms).

**B8 — Nesting normalization (grammar-level).** Adjacent nestings of the *same* bracket type are flattened during parsing:

```
   [[t]] → [t]
   (( t )) → ( t )
   {{ t }} → { t }
```

Different bracket types remain non-interchangeable per B4: `[ ( t ) ]` is well-formed and does not collapse to `[ t ]` or `( t )`. B8 is purely lexical/parsing — it does not affect semantic identity (and does not collide with B4's type-distinction, as the original wording in r2 of the architecture mistakenly suggested).

#### §8.4.3 Family C — Semantic operators (formation only)

Layer 1 specifies the *form* of expressions using these operators. Their semantics — what congruence laws they obey at Layer 3, what transitions they trigger at Layer 4 — are deferred to those layers.

**C1 — Prime suffix (unary projection marker — applies to projectables).**

```
   ⊢ t : projectable
   ─────────────────────────
   ⊢ t′ : projected-form(t)

where ⟨projectable⟩ ::= ⟨constituent-symbol⟩
                     |  ⟨constituent-ref⟩
                     |  ⟨designation⟩
                     |  ⟨op-form⟩
                     |  ⟨prefixed-op-form⟩
```

Prime suffixes any projectable term to produce its projected (anticipated, pre-execution) form. Examples from the worked cases:

- `P.1′` — primed constituent-ref
- `Σ(Α/i./t./D.)′` — primed op-form (Charles Table 5 Objective body; every Objective definition in Tables 5–22)
- `[Α/i./t./S./P.]′` — primed designation (every Objective definition)
- `[Α/i./t.]Σ(Α/i./t./D.)′` — primed prefixed-op-form (target-prefixed Selection in projection-clause position)

**Prime composition.** Prime composes additively with the sole-of-type dot (A5) and with the ordinal suffix (A7) on a constituent-symbol: `P.′`, `P.1′`, and `P1′` are all well-formed. A6's dot-vs-ordinal exclusion forbids only those two suffixes against each other; prime is permitted alongside either. On op-forms, prefixed-op-forms, and designations, the prime trails the entire form (write `Σ(...)′`, never `Σ(...′)`; write `[Α/i./t./S./P.]′`, never `[Α/i./t./S./P.′]`).

**C5 — Realized and projected forms are syntactically distinct.** For any projectable term `t`, `t` and `t′` are distinct terms at the grammar level. Layer 3's congruence does not identify them (the congruence's thinness guarantees no implicit equation between them — see §10).

**C7 — Yields arrow `→` (binary, restricted to two contexts).** The yields arrow is **not** a general term-former. It appears in exactly two grammatical positions, distinguished by surrounding context, and **does not chain** (`a → b → c` is malformed; exactly one `→` per form).

**C7a — Effect form (top-level execution).**

```
   ⊢ t1 : prefixed-op-form (typically [a.]ε(...))       ⊢ t2 : set
   ──────────────────────────────────────────────────────────────
                  ⊢ t1 → t2 : effect-form
```

The effect-form connects an Execution operation to the set of matrix modifications it produces. The LHS is an actor-prefixed Execution; the RHS is a curly-bracketed set whose members are typically arithmetic forms (Family D). Example: `[a.]ε(Α/i./o./g./e.) → { [Α/i./t./D./X./c.] + [Α/i./o./g./q.] }` (Charles Table 5).

**C7b — Projection clause (inside an equivalence body or as a set member).**

```
   ⊢ t1 : projection-operand       ⊢ t2 : projection-operand
   ─────────────────────────────────────────────────────────
              ⊢ t1 → t2 : projection-clause

where ⟨projection-operand⟩ ::= ⟨op-form⟩
                            |  ⟨prefixed-op-form⟩
                            |  ⟨designation⟩
                            |  ⟨primed-form⟩
```

The projection-clause appears as the body of an Objective, Intention, or Outcome equivalence (introduced by `≡`) or as a member inside a curly-bracketed set. Example: `Σ(Α/i./t./D.)′ → [Α/i./t./S./P.]′` (every Objective body in the worked cases).

**Precedence and parse-time disambiguation.** `→` has **no defined precedence with `:=`, `≡`, `+`, `-`** because it does not appear at top level outside an effect-form, and inside an effect-form or projection-clause the surrounding `{ }` or `≡` boundaries prevent interleaving. At parse time, the next-token after a `prefixed-op-form` is the disambiguator: `≡` → equivalence-form, `:=` → attribution-form, `→` followed by `{` → effect-form, `′` → primed-form. Each is uniquely identified by lookahead-1.

**C17 — Attribution assignment (binary, with curly RHS).**

```
   ⊢ lhs : op-form(σ)       ⊢ { t1, t2, ... } : set-of(constituent-ref)
   ───────────────────────────────────────────────────────────────────
              ⊢ lhs := { t1, t2, ... } : attribution-form
```

The right-hand side of `:=` **must** be a curly-bracketed set. `lhs := t` (with a bare term on the right) is a parse error per C19.

**C19 — Curly RHS required.** `:=` followed by anything other than `{ ... }` is malformed.

**C21 — Singleton RHS permitted.** `lhs := { t }` is well-formed.

**C22 — Membership predicate (binary).**

```
   ⊢ t1 : constituent-designation (typically a resource set)
   ⊢ t2 : constituent-ref (typically a required-resource designator)
   ────────────────────────────────────────────────────────────────
              ⊢ t1 ∋ t2 : predicate-form(boolean)
```

**C23 — Non-membership is the syntactic negation of ∋.** `∌` is admitted by the grammar in the same positions as `∋`. Their semantic dual relationship is a Layer 2 typing concern (C26) and a Layer 4 transition concern (∋ guards R-gate-clear; ∌ guards R-spawn).

**`≡` — definitional introducer (grammar-level form).**

```
   ⊢ lhs : op-form(σ)       ⊢ rhs : term
   ─────────────────────────────────────
       ⊢ lhs ≡ rhs : equivalence-form
```

The grammar admits `≡` between an operation form on the left and an arbitrary term on the right. The form's two roles — symmetric structural congruence at Layer 3, directional definitional expansion handled by R-unfold at Layer 4 — are split across those layers and not visible here.

**Perception-evaluation form (grammar-level).**

```
   ⊢ lhs : prefixed-op-form | primed-form (underlying op-form is Γ)
   ⊢ rhs : set
   ──────────────────────────────────────────────────────────────
                ⊢ lhs = rhs : perception-evaluation
```

The Perception lines in the worked cases use a distinct form, `[Α/i./t.]Γ(...) = { ... }` (realized) or `[Α/i./t.]Γ(...)′ = { ... }` (projected, inside an Intention body). The outer `=` here is not the inner utility-comparison `=` from D4; it is a Perception-specific evaluation form that relates a target's Perception (op or primed-op) to the set of comparisons that realize/project it. Charles T5 realized form: `[Α/i./t.]Γ(Α/i./t./D./G.) = { [Α/i./t./D./P./u.] > [Α/i./t./D./X./u.] }` (after D-26 normalization). The same shape with primed LHS appears as the body of Intention equivalences. Layer 2 (§9.7) restricts the underlying op-form to Γ (Perception). The set's members are comparison-forms (`<`, `>`, `≤`, `≥`) over utility-typed designations, optionally primed.

**Note on glyph collision (added for reader disambiguation).** The `≡` in `⟨op-form⟩ ≡ ⟨equiv-body⟩` is the Layer-1 **binding-form** constructor — a syntactic device binding an op-form to its body. The Layer-3 **structural-congruence relation** `≡` defined in §10 shares the same glyph but is a distinct construct (an equivalence relation on well-typed terms). The parse-level disambiguation is unambiguous (Layer-1 binding requires an op-form on the left; Layer-3 relation relates any two well-typed terms); the shared glyph is a notational artifact preserved from the dissertation. See §10's opening note for the symmetric breadcrumb at the Layer-3 site.

#### §8.4.4 Family D — Arithmetic and comparison

**D1, D2 — Addition and subtraction (binary).**

```
   ⊢ t1 : path-of(matrix-component | resource)
   ⊢ t2 : path-of(matrix-component | resource)
   ───────────────────────────────────────────
        ⊢ t1 + t2 : arithmetic-form
        ⊢ t1 - t2 : arithmetic-form
```

**D3 — Comparison operators (binary).**

```
   ⊢ t1 : path-of(utility)       ⊢ t2 : path-of(utility)
   ─────────────────────────────────────────────────────
           ⊢ t1 < t2 : comparison-form(boolean)
           (similarly for >, ≤, ≥)
```

**D4 — Evaluation equality (binary).** `t1 = t2` is admitted by the grammar in Perception lines; its typing and transition roles are at Layer 2 (typing at perception time) and Layer 4 (R-perceive uses it for realized comparisons).

**D5 — Comma separator.** Within `{ ... }`, the comma separates members of the set. Set order-irrelevance is a Layer 3 generator (D5 in the congruence); at Layer 1, the comma is purely a separator.

### §8.5 Constituent-operation forms

Eleven of the twenty-one constituents have operation forms — Greek operators that take an argument in round brackets. Ten do not appear in operation form in any worked case **after the D-21 lexer normalization**; LSPI treats them as nominal-only. The partition (per Part I §5.2 with Δ added, and with Θ reclassified per the D-21 normalization):

#### §8.5.1 Operation-bearing constituents (11)

```
δ(arg)   — Detection
ω(arg)   — Objective
γ(arg)   — Intention
ε(arg)   — Execution
θ(arg)   — Required Resources
Φ(arg)   — Obtained Resources
Γ(arg)   — Perception (target-prefixed)
Σ(arg)   — Selection (target-prefixed)
Ω(arg)   — Outcome (systemic, unprefixed)
Λ(arg)   — Obtained Utility (target-prefixed)
ι(arg)   — Interest (in attribution forms like `[a.]ι(Α/i.) := { ... }`)
```

#### §8.5.2 Nominal-only constituents (10)

```
α, Α, τ, Δ, π, ψ, β, κ, λ, Θ
```

These appear in paths and as constituent references but never in the form `Greek-symbol(argument)`. **Θ is included as nominal-only because, after the D-21 lexer normalization (§8.2.2), the Greek symbol Θ does not appear as a surface operation form at all.** Every operation-form occurrence of Θ in the source worked cases (`[a.]Θ(Α/i./O./Q.)`, `[Α/i./t.]Θ(Α/i./O./U.)`) is retokenized as Φ or Λ before the parser sees it; the Current Resources constituent is referenced in the post-lexer corpus exclusively through its Latin set/attribute form `R` (as in `[a./R.]`), not through the Greek operation form Θ. Θ is filed under nominal-only **because it bears no operation form in the post-lexer corpus**, not because a nominal Θ token appears in any specific position. The 11 + 10 = 21 partition is therefore exact and disjoint after lexer normalization.

The partition is exact at the time of writing — and was determined by **the same test applied to each constituent**: does the symbol appear in `Greek-symbol(argument)` form anywhere in the post-lexer corpus of Tables 5–22? Each of the 11 operation-bearing constituents in §8.5.1 has at least one direct citation in the worked cases (representative examples: δ as `[a.]δ(Α/i./d.) := { ... }` in Charles T5; θ as `[a.]θ(Α/i./o./g1) := { [Α/i./o./g1/q.] }` in Charles T5 with parallel occurrences in Jim T6, Nathan T7–T11, Sarah T12–T15, Rusty T16–T20 — 15+ rows across the worked cases; ι as `[a.]ι(Α/i.) := { [Α/i./Q.] }` in Charles T5; ε as `[a.]ε(Α/i./o./g./e.) → { ... }` in Charles T5; etc.). Each of the 10 nominal-only constituents in §8.5.2 lacks any such occurrence after the D-21 normalization (Θ is the test case worked through above; the others — α, Α, τ, Δ, π, ψ, β, κ, λ — appear only as path-nodes or constituent-refs, never as `Greek-symbol(arg)`). If a future worked case is discovered using one of the nominal-only constituents in operation form, the partition is revised (architecture D-25).

### §8.6 Agent-attribution prefixes

The grammar admits three dispatch classes for operation forms (per Part I §6.5):

```
⟨prefixed-op-form⟩ ::= "[a.]" ⟨op-form⟩                  -- actor-prefixed (a.-rooted only)
                    |  "[" ⟨Α-rooted-path⟩ "]" ⟨op-form⟩   -- target-prefixed (Α-rooted only)
                    |  ⟨op-form⟩                            -- systemic, unprefixed
```

**The actor-prefix and target-prefix productions are disjoint by construction.** Every actor prefix in the worked cases is the literal `[a.]` (a single-segment `a.`-rooted designation). Every target prefix in the worked cases is `[Α/i./t.]` or a longer Α-rooted path. Restricting the target-prefix alternative to `⟨Α-rooted-path⟩` makes the dispatch class **unambiguous at parse time**: an `a.`-rooted bracketed form is necessarily the actor prefix; an `Α`-rooted bracketed form is necessarily the target prefix. Without this restriction, `[a.]δ(...)` would derive two ways (actor literal, or target with single-segment `a.` path), and §9's typing dispatch would have nothing to read off the parse tree.

**The systemic (unprefixed) alternative and the bare `⟨op-form⟩` term are intentionally redundant.** A bare `δ(...)` matches both `⟨op-form⟩` (as a top-level term) and the systemic `⟨prefixed-op-form⟩` alternative; both classify it as the same dispatch class (systemic). The redundancy is harmless and intended — the systemic alternative makes the three-way dispatch structure explicit in the prefixed-op-form production, while the bare `⟨op-form⟩` admits the operation as a component term in larger expressions.

Layer 1 admits all three dispatch classes; Layer 2 typing constrains which operations admit which prefix class (e.g., δ admits only actor-prefix; Γ admits only target-prefix; Ω admits only systemic).

### §8.7 Vocabulary closure

**M5 — Constituent vocabulary closure.** The 21 constituent symbols in Part I §5.1 (after the Α/A normalization at M4 and the Θ/Φ/Λ normalization at D-21) constitute LSPI's complete constituent vocabulary. Any other Greek letter or Latin symbol that appears in operation-form position or constituent-reference position is rejected at Layer 1. Extension requires a future LSPI version, not silent admission.

**M6 — Operator vocabulary closure.** The structural operators enumerated in §8.4 (Families A–D) plus the agent-attribution prefix mechanism constitute LSPI's complete operator vocabulary. Any other punctuation, mathematical symbol, or operator-like glyph that appears in operator position is rejected. Like M5, extension requires a future LSPI version.

The two closure rules together mean that **the LSPI grammar is decidable**: a finite-state lexer plus a context-sensitive parser can mechanically determine whether any input string is well-formed.

### §8.8 The subpath relation (auxiliary definition)

A frequently-used auxiliary relation on path terms is **subpath** `⊑`. It is defined inductively:

```
   ε ⊑ p                                (the empty path is a subpath of every path)

   t ⊑ p
   ───────────                          (any subpath extends by a child)
   t/c ⊑ p/c

   p ⊑ p                                (every path is a subpath of itself)
```

Equivalent characterization: `t ⊑ p` iff `t` is a (possibly improper) prefix of `p`, considering paths as sequences of constituent-ref segments separated by slashes.

`⊑` is not a typing rule, a congruence axiom, or a transition rule. It is a definition used by the uniqueness theorem in Part III §13 and by the path-extension rules in Layer 4 (notably R-spawn and R-resume, which extend or restore paths along subpath relations).

### §8.9 The full grammar in BNF (consolidated, corrected)

For reference, the complete context-free skeleton of LSPI's grammar:

```
⟨term⟩ ::= ⟨designation⟩
        |  ⟨op-form⟩
        |  ⟨prefixed-op-form⟩
        |  ⟨primed-form⟩
        |  ⟨attribution-form⟩
        |  ⟨equivalence-form⟩
        |  ⟨effect-form⟩
        |  ⟨perception-evaluation⟩
        |  ⟨arithmetic-form⟩
        |  ⟨predicate-form⟩
        |  ⟨comparison-form⟩
        |  ⟨set⟩
       -- note: ⟨projection-clause⟩ is NOT a top-level ⟨term⟩; it appears only
       -- inside ⟨set⟩ or as the body of an ⟨equivalence-form⟩

⟨designation⟩      ::= "[" ⟨path⟩ "]"

⟨path⟩             ::= ⟨root-anchor⟩                                    -- single-segment
                    |  ⟨path⟩ "/" ⟨constituent-ref⟩                      -- multi-segment

⟨root-anchor⟩      ::= "Α" | "a."

⟨constituent-ref⟩  ::= ⟨constituent-symbol⟩ "."
                    |  ⟨constituent-symbol⟩ ⟨ordinal⟩
                    |  ⟨constituent-symbol⟩ "." "′"
                    |  ⟨constituent-symbol⟩ ⟨ordinal⟩ "′"

⟨constituent-symbol⟩ ::= "α" | "Α" | "τ" | "ι" | "Δ" | "π" | "ψ" | "β" | "κ" | "λ" | "Θ"
                       | "δ" | "ω" | "γ" | "ε" | "θ" | "Φ" | "Γ" | "Σ" | "Ω" | "Λ"
                       -- (the 21 vocabulary symbols from Table 4 — see Part I §5.1)

⟨ordinal⟩          ::= "1" | "2" | "3" | ... (positive integer)

⟨op-form⟩          ::= ⟨op-symbol⟩ "(" ⟨path⟩ ")"              -- argument MUST be fully-rooted

⟨op-symbol⟩        ::= "δ" | "ω" | "γ" | "ε" | "θ" | "Φ" | "Γ" | "Σ" | "Ω" | "Λ" | "ι"
                       -- (11 symbols post-D-21 normalization; Θ does NOT appear in op-form
                       --  after lexer normalization — it has been rewritten to Φ or Λ)

⟨Α-rooted-path⟩    ::= "Α"
                    |  ⟨Α-rooted-path⟩ "/" ⟨constituent-ref⟩

⟨prefixed-op-form⟩ ::= "[a.]" ⟨op-form⟩                         -- actor-prefixed (a.-rooted)
                    |  "[" ⟨Α-rooted-path⟩ "]" ⟨op-form⟩          -- target-prefixed (Α-rooted)
                    |  ⟨op-form⟩                                  -- systemic, unprefixed

⟨primed-form⟩      ::= ⟨designation⟩ "′"                        -- primed designation
                    |  ⟨op-form⟩ "′"                              -- primed op-form
                    |  ⟨prefixed-op-form⟩ "′"                     -- primed prefixed-op-form
                    -- (primed constituent-refs and primed constituent-symbols are
                    --  already covered by the prime alternatives in ⟨constituent-ref⟩;
                    --  see C1)

⟨attribution-form⟩ ::= ⟨op-form⟩ ":=" ⟨set⟩
                    |  ⟨prefixed-op-form⟩ ":=" ⟨set⟩

⟨equivalence-form⟩ ::= ⟨op-form⟩ "≡" ⟨equiv-body⟩
                    |  ⟨prefixed-op-form⟩ "≡" ⟨equiv-body⟩

⟨equiv-body⟩       ::= ⟨set⟩
                    |  ⟨projection-clause⟩                       -- e.g., Objective body

⟨effect-form⟩      ::= ⟨prefixed-op-form⟩ "→" ⟨set⟩            -- top-level Execution effect
                    -- LHS is typically [a.]ε(...); the typing (§9) restricts further

⟨projection-clause⟩ ::= ⟨projection-operand⟩ "→" ⟨projection-operand⟩
                    -- non-associative; exactly one "→"; no chaining

⟨projection-operand⟩ ::= ⟨op-form⟩
                      |  ⟨prefixed-op-form⟩
                      |  ⟨designation⟩
                      |  ⟨primed-form⟩

⟨perception-evaluation⟩ ::= ⟨perception-lhs⟩ "=" ⟨set⟩         -- Perception line / Intention body
                          -- underlying op-form must be Γ (Layer 2 restriction)
                          -- set members are ⟨comparison-form⟩ over utility-typed designations

⟨perception-lhs⟩   ::= ⟨prefixed-op-form⟩                       -- realized Perception
                    |  ⟨prefixed-op-form⟩ "′"                    -- projected Perception (in Intention body)
                    -- NB: a primed designation is NOT a valid perception-lhs; this restriction
                    -- is what disambiguates inner `=` (⟨cmp-operand⟩ "=" ⟨cmp-operand⟩) from
                    -- outer `=` (⟨perception-lhs⟩ "=" ⟨set⟩) at parse time. The two `=` senses
                    -- never collide because their LHS productions are disjoint by construction.

⟨arithmetic-form⟩  ::= ⟨designation⟩ "+" ⟨designation⟩
                    |  ⟨designation⟩ "-" ⟨designation⟩

⟨predicate-form⟩   ::= ⟨designation⟩ "∋" ⟨designation⟩
                    |  ⟨designation⟩ "∌" ⟨designation⟩

⟨comparison-form⟩  ::= ⟨cmp-operand⟩ ⟨cmp-op⟩ ⟨cmp-operand⟩
                    |  ⟨cmp-operand⟩ "=" ⟨cmp-operand⟩          -- realized-comparison `=`
                    -- distinct from the outer `=` in ⟨perception-evaluation⟩;
                    -- disambiguated at parse time by LHS shape (designation vs prefixed-op-form)

⟨cmp-operand⟩      ::= ⟨designation⟩
                    |  ⟨designation⟩ "′"                         -- primed designation (utility value)

⟨cmp-op⟩           ::= "<" | ">" | "≤" | "≥"

⟨set⟩              ::= "{" ⟨set-content⟩ "}"

⟨set-content⟩      ::= ⟨set-member⟩
                    |  ⟨set-member⟩ "," ⟨set-content⟩

⟨set-member⟩       ::= ⟨term⟩                                   -- ⟨term⟩ already produces ⟨arithmetic-form⟩, etc.
                    |  ⟨projection-clause⟩                       -- e.g., Σ(...)′ → P.′
                                                                  -- (projection-clause is the ONLY non-term form
                                                                  --  that legitimately appears as a set member)
```

**Notable corrections in this BNF vs the r1 draft:**

1. `⟨primed-form⟩` is a new top-level term-former — it admits prime on designations, op-forms, and prefixed-op-forms (the case Example 3 requires). The r1 BNF restricted prime to constituent-refs only; this corrects that.
2. `⟨path⟩` now admits a single-segment form (just the root-anchor). This is what makes `[a.]` parse as `[ ⟨path⟩ ]` legitimately.
3. `⟨designation⟩` is restricted to bracketed paths only (the r1 alternative `[ ⟨constituent-ref⟩ ]` is removed — a sweep of all bracketed-reference occurrences in Tables 5–22 confirms every bracket-enclosed reference is a fully-rooted path beginning with `Α` or `a.`; no `[P.]`, `[X.]`, `[d.]`, or other bare-ref form appears anywhere in the worked cases).
4. `⟨arg⟩` of an op-form is restricted to fully-rooted paths only. The r1 alternative `⟨arg⟩ ::= ... | ⟨constituent-ref⟩` is removed because A8's parent-set-scoping side condition cannot bind to a rootless constituent-ref.
5. `⟨yields-form⟩` is split into `⟨effect-form⟩` (top-level, LHS is prefixed-op-form, RHS is set) and `⟨projection-clause⟩` (appears only inside `⟨set⟩` or as `⟨equiv-body⟩`). Neither is a general term-former. `→` does not chain.
6. `⟨op-symbol⟩` no longer includes Θ — after D-21 lexer normalization, Θ never appears as an operation symbol (it has been retokenized as Φ or Λ).

The BNF specifies the **context-free skeleton**. The context-sensitive constraints — A8 parent-set-scoped numbering, A9 sibling completeness per snapshot, A14 root anchoring, M5/M6 vocabulary closure, A1 type-aware child-class on slash composition — are the inference-rule premises in §8.4 and §8.7. A complete Layer 1 well-formedness check requires both the BNF skeleton and the side conditions.

### §8.10 Worked examples through Layer 1

To ground the grammar, three expressions from the dissertation's worked cases are parsed through Layer 1.

**Example 1 — Charles Table 5, Interest line:**

```
[a.]ι(Α/i.) := { [Α/i./Q.] }
```

Parse:
- `[a.]` is a `⟨prefixed-op-form⟩` opener with the actor-prefix class.
- `ι(Α/i.)` is an `⟨op-form⟩`: `ι` is in the operation-symbol set; `(Α/i.)` is the argument; `Α/i.` is a `⟨path⟩` (root `Α`, child `i.`).
- `:=` opens an `⟨attribution-form⟩`.
- `{ [Α/i./Q.] }` is a `⟨set⟩` with one member, the `⟨designation⟩` `[Α/i./Q.]`.

Well-formed at Layer 1.

**Example 2 — Charles Table 5, Resource check:**

```
[a./R.] ∋ [Α/i./o./g1/q.]
```

Parse:
- `[a./R.]` is a `⟨designation⟩` enclosing the path `a./R.` (root `a.`, child `R.`).
- `∋` opens a `⟨predicate-form⟩`.
- `[Α/i./o./g1/q.]` is a `⟨designation⟩` enclosing the path `Α/i./o./g1/q.` (root `Α`, children `i.`, `o.`, `g1`, `q.`).

The ordinal `g1` in the right-hand designation invokes A8: it is scoped to the parent set under `o.`, not globally; A9 sibling completeness requires that `g1` is the first of however many intentions exist; if a later signal references `g2`, then `g1` and `g2` must both appear in the realized snapshot's parent set.

Well-formed at Layer 1.

**Example 3 — Sarah Table 14, Objective definition:**

```
[a.]ω(Α/i./o./g2/i./o.) ≡ { [Α/i./o./g2/i./t.]Σ(Α/i./o./g2/i./t./D.)′ → [Α/i./o./g2/i./t./S./P.]′ }
```

Parse:
- `[a.]ω(Α/i./o./g2/i./o.)` is a `⟨prefixed-op-form⟩` — actor-prefixed Objective applied to a long path.
- `≡` opens an `⟨equivalence-form⟩` whose right-hand side is the curly-bracketed set.
- Inside the set: a primed prefixed-op-form `[Α/i./o./g2/i./t.]Σ(Α/i./o./g2/i./t./D.)′` (target-prefixed Selection, prime marks projection), then `→`, then a primed designation `[Α/i./o./g2/i./t./S./P.]′` — the whole `primed-prefixed-op-form → primed-designation` is a single `⟨projection-clause⟩` per C7b.

The nested path depth (six segments under `Α`) is admitted by A1's recursive structure. The target-prefixed `Σ` operation is admitted by §8.6's three dispatch classes. The prime on `Σ(Α/i./o./g2/i./t./D.)′` (a primed prefixed-op-form within a `[Α/i./...]Σ(...)` form) is admitted by C1's projectable-form rule and is realized in the BNF as `⟨primed-form⟩` (§8.9). The prime on `[Α/i./o./g2/i./t./S./P.]′` (a primed designation) is admitted by the same rule. The `→` between the primed prefixed-op-form and the primed designation is admitted as a `⟨projection-clause⟩` (C7b, §8.9) — appearing here as the body of the `≡` equivalence-form per `⟨equiv-body⟩`. No `→` chaining occurs.

Well-formed at Layer 1.

### §8.11 What Layer 1 does NOT do

Layer 1 says which strings are well-formed terms. It does not say:

- Which terms are **well-typed** (Layer 2). A term that is syntactically well-formed may still be ill-typed: writing `[a.]Σ(...)` (actor-prefixed Selection) is well-formed at Layer 1, but Layer 2 rejects it because Selection is target-performed.
- Which terms are **congruent** (Layer 3). The grammar treats `a/(b/c)` and `(a/b)/c` as distinct parse trees; Layer 3's congruence identifies them.
- How configurations **evolve** (Layer 4). The grammar admits the syntactic form of a transition's redex, but only Layer 4's rules can fire a transition.
- What constituents **mean** in the political domain. The dissertation supplies the semantics; LSPI's grammar is structural.

Layer 1 is the gate. Everything downstream depends on it. Everything downstream is constrained by it.

### For AI engines

The mechanical procedure for parsing an LSPI expression:

1. **Lex.** Tokenize the input, applying all four normalizations: M4 (Α/A glyph), D-21 (Θ→Φ/Λ contextually), D-26 (matrix-path shorthand `/i./D./` → `/i./t./D./`), and D-27 (perception-path canonicalization `/t./G.` → `/t./D./G.`). An engine that skips D-26 or D-27 will fail to canonicalize the 21 shorthand matrix paths and the 17 shorthand projected-Perception paths respectively, and the resulting non-canonical paths will then mis-type against the tight child-class lattice in §9.3.1.
2. **Parse against the BNF.** Use the context-free grammar in §8.9 to construct a parse tree. Reject any input that fails to parse — do not attempt to coerce or guess.
3. **Check the context-sensitive side conditions.** A1's type-aware child-class premise, A8's parent-set-scoped numbering, A9's per-snapshot sibling completeness, M5/M6 vocabulary closure. Reject any input that fails any side condition; surface the specific failing rule to the operator.
4. **Yield a well-formed term.** Pass it to Layer 2 (typing) for further checking.

At no point does Layer 1 reason about meaning, intent, or political-domain plausibility. It is purely structural. An expression that parses at Layer 1 is the input to type-checking; an expression that fails at Layer 1 is rejected immediately with a citation to the failing rule.

When given an expression that fails Layer 1, do not silently propose a correction. Surface the failure with the rule reference (e.g., "rejected: A6 — dot suffix and ordinal suffix appear together on `P.1`") and ask the operator. Silent coercion would corrupt the audit trail.

---

## §9 Layer 2 — Type System (Typing Rules)

### §9.1 What Layer 2 specifies

Layer 2 specifies *which well-formed terms are well-typed*. It builds directly on Layer 1: only well-formed terms (those that pass §8's grammar) are eligible for type-checking. A term that is syntactically well-formed at Layer 1 but ill-typed at Layer 2 is rejected — typing is a strictly downstream gate.

This section discharges the four explicit deferrals from §8:

1. **The child-class lattice** that A1's premise "constituent-of-τ-child-class" refers to (§9.3) — the partial order over constituent sorts that determines which sorts may appear as children of which. A4's non-idempotence falls out as an immediate consequence.
2. **The prefix-dispatch typing** (§9.4) — which operations admit which agent-attribution prefix class (δ actor-only, Γ / Σ / Λ target-only, Ω systemic-only, etc.). With the actor/target prefix productions now disjoint at Layer 1 (§8.6 r5 correction), the parse tree carries the dispatch class unambiguously and Layer 2 reads it off directly.
3. **The two senses of `→`** (§9.5) — C7a effect-form and C7b projection-clause typed apart by the LHS sort.
4. **The RHS typing of `≡` and `:=`** (§9.6) — what kinds of expressions are admissible as the body of an equivalence or the right-hand side of an attribution.

Plus the typing of predicates (`∋`, `∌`), comparisons (`<`, `>`, `≤`, `≥`, `=`), and the typing-level statement of the M4 and D-21 lexer normalizations.

**The typing judgment.** Written:

```
   Σ ⊢ t : τ
```

read "under typing environment Σ, term t has sort τ." When Σ is irrelevant (most typing rules are context-free at the typing level because the context-sensitive premises were already discharged at Layer 1), the judgment abbreviates to `⊢ t : τ`. When Σ matters — typically because a typing rule references a previously-declared agent-prefix or a parent constituent sort — Σ is shown explicitly.

The typing rules below are presented in standard inference-rule notation. Where useful, tables consolidate the dispatch decisions (especially §9.4's prefix dispatch).

### §9.2 Sorts and the typing universe

The sort universe at Layer 2 is the union of three categories, all declared in §8.3:

1. **The 21 constituent sorts.** One per Table 4 entry: `actor`, `agenda`, `target`, `interest`, `detection`, `matrix`, `objective`, `outcome`, `intention`, `perception`, `execution`, `selection`, `position`, `alternative`, `benefit`, `cost`, `utility`, `resource-required`, `resource-obtained`, `resource-set`, `utility-obtained`.
2. **Compound sort constructors.** `path-of(σ)`, `op-form(σ)`, `set-of(σ)`, and the new ones Layer 2 introduces: `projection-clause(σ₁, σ₂)`, `effect-form`, `perception-evaluation`, `attribution-form(σ)`, `equivalence-form(σ)`, `predicate-form` (carrying the `boolean` result), `comparison-form`, `primed-form(σ)` (the projected variant of a projectable sort `σ`).
3. **Auxiliary sorts.** `ordinal`, `agent` (the dispatch class — actor / target / systemic), `boolean`, `dispatch-class`.

Layer 2 reasons over this universe. A well-typed term is one whose sort can be derived by the inference rules below. Type-checking is decidable (proved in Part III §16, depending on the rules below and the child-class lattice's finite breadth).

### §9.3 The child-class lattice — A1's deferred premise resolved

A1's formation rule from Layer 1 contained the premise:

```
   ⊢ t1 : path-of(τ)       ⊢ t2 : constituent-of-τ-child-class
   ────────────────────────────────────────────────────────────
                ⊢ t1/t2 : path-of(sort-of(t2))
```

The "constituent-of-τ-child-class" premise was deferred to Layer 2. **This section discharges it.** The child-class lattice is the partial order over constituent sorts that says: for each sort τ, what set of sorts may legitimately appear as τ's children in a slash composition.

#### §9.3.1 The lattice (defined by inspection of Tables 5–22)

The lattice was extracted by enumerating every parent/child pair that appears in any slash path in the worked cases and consolidating. The result:

|                 Parent sort                 |                                            Admissible child sorts                                            |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| `agenda` (Α)                                | `interest`, `outcome`                                                                                        |
| `actor` (a.)                                | `resource-set` (R), and acts as anchor for actor-performed operations                                        |
| `interest` (ι)                              | `detection`, `target`, `objective`, `outcome`, `resource-obtained`                                            |
| `target` (τ)                                | `matrix` (D as path node), `selection` (S as path node, post R-select)                                       |
| `matrix` (D as path node)                   | `position`, `alternative`, `perception` (G as path node, after D-27 normalization makes all Γ arguments terminate at `/t./D./G.`) |
| `position` (π)                              | `benefit`, `cost`, `utility`                                                                                 |
| `alternative` (ψ)                           | `benefit`, `cost`, `utility`                                                                                 |
| `objective` (ω)                             | `intention`, `resource-obtained` (as shorthand on close), `outcome`                                          |
| `intention` (γ)                             | `resource-required`, `execution`, `interest` (when capability-gate fails and a nested interest spawns)       |
| `outcome` (Ω)                               | `resource-obtained` (Q), `utility-obtained` (U), `selection`                                                 |
| `selection` (S as path node, post R-select) | `position` (the position selected)                                                                           |
| `resource-required` (θ as q)                | (leaf — no children)                                                                                         |
| `resource-obtained` (Φ as Q)                | (leaf)                                                                                                       |
| `resource-set` (R)                          | (leaf — but the set may contain resource designations as members)                                            |
| `utility-obtained` (Λ as U)                 | (leaf)                                                                                                       |
| `benefit`, `cost`, `utility`                | (leaves)                                                                                                     |
| `detection` (δ as d)                        | (leaf — the Detection's output is constructed via `:=`, not via slash children)                              |
| `execution` (ε as e)                        | (leaf — Execution's effect is constructed via the effect-form C7a, not via slash children)                   |
| `perception` (Γ as G in path-extension form)| (leaf — Perception's content is constructed via the perception-evaluation form, not via slash children)      |

**Reading the table.** Each row says: "if `t1` has the parent sort named in the row, then `t1/t2` is well-typed iff `t2` has one of the child sorts listed in the row." The slash composition `t1/t2` rejects any `t2` whose sort is not in the parent's admissible-child set.

#### §9.3.2 The typing rule for slash composition (A1 with the premise discharged)

```
   ⊢ t1 : path-of(τ)       ⊢ t2 : σ       σ ∈ child-class(τ)
   ─────────────────────────────────────────────────────────
                       ⊢ t1/t2 : path-of(σ)
```

where `child-class(τ)` is the set in the right-hand column of the lattice table above.

#### §9.3.3 A4 (non-idempotence) as a direct consequence

A4 says `a/a` is not well-formed. In the lattice, no constituent sort appears in its own admissible-child set: `child-class(agenda)` does not contain `agenda`, `child-class(target)` does not contain `target`, and so on. A4 is therefore a corollary of the lattice rather than a separately asserted formation rule; the proof is the single observation that the lattice's reflexive entries are all empty.

#### §9.3.4 Recursion via nested-interest spawn

One row of the lattice is structurally important: `intention` admits `interest` as a child. This is the lattice-level statement of the capability-gate-failure spawn mechanism (Layer 4 rule R-spawn). When `[a./R.] ∌ θ.q` fires at the gate, a new Interest is opened at a deeper slash path under the failing Intention. The lattice admits this because `interest` is a legal child of `intention`. The recursion is bounded only by the engagement's stack depth, not by the lattice.

#### For AI engines

The child-class lattice is the central data structure Layer 2 reads when typing a slash composition. Encode it as a lookup table or a partial-function map. When a parse tree presents a slash composition `t1/t2`:

1. Determine `t1`'s sort (recursively typing `t1`).
2. Look up `child-class(sort-of(t1))`.
3. Determine `t2`'s sort.
4. If `sort-of(t2) ∈ child-class(sort-of(t1))`, the slash composition is well-typed with sort `path-of(sort-of(t2))`. Otherwise, reject with citation to the specific child-class failure.

This is mechanical. Surface failures by naming the parent and child sorts and the lattice entry that excluded the combination.

### §9.4 Prefix-dispatch typing — which operations admit which prefix class

Layer 1 (§8.6) defined three dispatch classes for `⟨prefixed-op-form⟩`: actor-prefixed (`[a.]·`), target-prefixed (`[Α-rooted-path]·`), and systemic (unprefixed). The Layer 1 productions are disjoint by construction (since the actor literal is `a.`-rooted and the target alternative is Α-rooted), so the parse tree carries the dispatch class unambiguously. **Layer 2 reads off the parse tree's dispatch class and rejects any operation that admits a different class.**

#### §9.4.1 The prefix-admissibility table

Each of the 11 operation-bearing constituents admits exactly one prefix class. The table is determined by direct enumeration of the worked cases:

|       Operation        |       Admits      |                                                  Cases                                                   |
|------------------------|-------------------|----------------------------------------------------------------------------------------------------------|
| δ (Detection)          | **actor-only**    | `[a.]δ(...)` in every cycle's Detection line (Charles T5, Jim T6, Nathan T7, Sarah T12, Rusty T16, etc.) |
| ω (Objective)          | **actor-only**    | `[a.]ω(...)` in every Objective line                                                                     |
| γ (Intention)          | **actor-only**    | `[a.]γ(...)` in every Intention line                                                                     |
| ε (Execution)          | **actor-only**    | `[a.]ε(...)` in every Execution line                                                                     |
| θ (Required Resources) | **actor-only**    | `[a.]θ(...)` in every Required-Resources line                                                            |
| Φ (Obtained Resources) | **actor-only**    | `[a.]Φ(...) := { ... }` after Resource flow-back                                                         |
| ι (Interest)           | **actor-only**    | `[a.]ι(...) := { ... }` in every Interest line                                                           |
| Γ (Perception)         | **target-only**   | `[Α/i./t.]Γ(...)` in every Perception line                                                               |
| Σ (Selection)          | **target-only**   | `[Α/i./t.]Σ(...)` in every Selection line                                                                |
| Λ (Obtained Utility)   | **target-only**   | `[Α/i./t.]Λ(...) := { ... }` in every Obtained-Utility line                                              |
| Ω (Outcome)            | **systemic-only** | `Ω(Α/i./O.) ≡ { ... }` in every Outcome line, no prefix                                                  |

#### §9.4.2 The prefix-dispatch typing rules

For each operation symbol, exactly one typing rule fires:

**Actor-prefix typing rule (instantiated for each of δ, ω, γ, ε, θ, Φ, ι):**

```
   op ∈ { δ, ω, γ, ε, θ, Φ, ι }       ⊢ t : path-of(σ)       σ is op-compatible
   ──────────────────────────────────────────────────────────────────────────
                  ⊢ [a.]op(t) : prefixed-op-form(op, actor)
```

**Target-prefix typing rule (instantiated for each of Γ, Σ, Λ):**

```
   op ∈ { Γ, Σ, Λ }       ⊢ tp : Α-rooted-path-of(target)
                          ⊢ t : path-of(σ)       σ is op-compatible
   ─────────────────────────────────────────────────────────────────
              ⊢ [tp]op(t) : prefixed-op-form(op, target)
```

**Systemic typing rule (for Ω only):**

```
   ⊢ t : path-of(outcome)
   ──────────────────────────────────
   ⊢ Ω(t) : prefixed-op-form(Ω, systemic)
```

**Rejection clauses:**

- Writing `[a.]Σ(...)` (actor-prefixed Selection) is rejected: Σ is target-only.
- Writing `[Α/i./t.]δ(...)` (target-prefixed Detection) is rejected: δ is actor-only.
- Writing `[a.]Ω(...)` or `[Α/i./t.]Ω(...)` is rejected: Ω is systemic-only.

Rejections cite the specific operation and the prefix-admissibility row that excluded the combination.

#### §9.4.3 "Op-compatible" — the argument-sort constraint

The premise "σ is op-compatible" in the typing rules above means the operation's argument sort must match the sort the operation is defined to act upon. For example:

- δ (Detection) takes a path-of(detection): the argument must resolve to a sort that ends in `detection` — i.e., `Α/i./d.` for the only detection within an interest.
- ω (Objective) takes a path-of(objective): the argument must resolve to a sort ending in `objective`.
- ε (Execution) takes a path-of(execution): argument ends in `execution`.
- Σ (Selection) takes a path-of(matrix): argument ends in `matrix` (the selection is *over* the decision matrix).
- Γ (Perception) takes a path-of(perception): argument ends in `perception`.

The full op-compatibility map is determined by inspection of the worked cases, in parallel to the child-class lattice. For each operation, the argument's terminal sort must match the operation's expected input sort.

### §9.5 The two senses of `→` typed apart

§8 split `→` into two grammatical positions: C7a effect-form (top-level execution) and C7b projection-clause (inside an equivalence body or as a set member). Layer 2 types them differently.

#### §9.5.1 C7a effect-form typing

```
   ⊢ t1 : prefixed-op-form(ε, actor)       ⊢ t2 : set-of(arithmetic-form | resource-designation)
   ───────────────────────────────────────────────────────────────────────────────────────────
                                  ⊢ t1 → t2 : effect-form
```

The effect-form's LHS must be an **actor-prefixed Execution** specifically. No other operation in actor-prefix position licenses an effect-form. The RHS must be a set whose members are arithmetic-forms (matrix-component modifications) or resource designations (the resources consumed by the Execution).

Rejection: `[a.]δ(...) → { ... }` is rejected. Detection is actor-prefixed but is not ε; the effect-form typing rule does not license non-Execution LHSs.

#### §9.5.2 C7b projection-clause typing

```
   ⊢ t1 : projection-operand        ⊢ t2 : projection-operand
   ──────────────────────────────────────────────────────────
            ⊢ t1 → t2 : projection-clause
```

where `projection-operand` is the union of:

- `op-form`
- `prefixed-op-form`
- `designation`
- `primed-form` (of any of the above)

Both sides of a projection-clause must be projection-operands. Projection-clauses appear inside `⟨set⟩` or as the body of an `≡` equivalence (per §8.9's `⟨equiv-body⟩`).

#### §9.5.3 Disambiguating between the two at typing

Layer 1's BNF already routes `→` into one of two grammatical forms based on context (effect-form is top-level with a set RHS; projection-clause is inside a set or equiv-body). At typing time, the dispatch is fixed by the parse tree: an `effect-form` parse tree is typed by §9.5.1; a `projection-clause` parse tree is typed by §9.5.2. The two are never ambiguous because their grammatical contexts are mutually exclusive.

### §9.6 `≡` and `:=` RHS typing

Both `≡` (equivalence) and `:=` (attribution) are LHS-RHS forms. Layer 1 specified the syntactic shape (`⟨op-form⟩ "≡" ⟨equiv-body⟩` and `⟨op-form⟩ ":=" ⟨set⟩`). Layer 2 constrains what the RHS may type as.

#### §9.6.1 `≡` (equivalence) RHS typing

```
   ⊢ lhs : op-form(σ) | prefixed-op-form(op, dispatch)
   ⊢ rhs : equiv-body-of(σ)
   ─────────────────────────────────────────────────────
        ⊢ lhs ≡ rhs : equivalence-form(σ)
```

where `equiv-body-of(σ)` is:

- For σ = `objective` : a `⟨set⟩` whose sole member is a `projection-clause` of the form `[target]Σ(...)′ → [...]′` — both LHS and RHS primed; the LHS is a target-prefixed Selection in projection-operand position, and the RHS is a primed designation. Per Charles T5: `[a.]ω(Α/i./o.) ≡ { [Α/i./t.]Σ(Α/i./t./D.)′ → [Α/i./t./S./P.]′ }`.
- For σ = `intention` : a `⟨set⟩` whose sole member is a `perception-evaluation` of the form `[target]Γ(...)′ = { [P./u.]′ > [X./u.]′ }` — the LHS is a primed target-prefixed Perception; the RHS is a set containing a `⟨comparison-form⟩` over primed utility-designations. The outer `=` is the perception-evaluation `=` (not the inner utility-comparison `=`); the parse tree distinguishes by LHS shape. Per Charles T5 (after D-27 canonicalization inserts the matrix node in Γ's argument): `[a.]γ(Α/i./o./g.) ≡ { [Α/i./t.]Γ(Α/i./t./D./G.)′ = { [Α/i./t./D./P./u.]′ > [Α/i./t./D./X./u.]′ } }`. The dissertation's source-text version of this expression uses the projected shorthand `Γ(Α/i./t./G.)′`; the lexer's D-27 rule inserts the matrix node `D./` between `t./` and `G.` to produce the canonical form shown.
- For σ = `outcome` : a `⟨set⟩` whose sole member is a `projection-clause` of the form `[target]Σ(...) → [...]` (no prime — Outcome is post-execution and bodies are realized, not projected). Per Charles T5: `Ω(Α/i./O.) ≡ { [Α/i./t.]Σ(Α/i./t./D.) → [Α/i./t./S./P.] }`.
- For any other σ : not licensed at the time of writing (no worked case uses `≡` with a non-{objective, intention, outcome} LHS).

#### §9.6.2 `:=` (attribution) RHS typing

```
   ⊢ lhs : op-form(σ) | prefixed-op-form(op, dispatch)
   ⊢ rhs : set-of(constituent-designation)
   ─────────────────────────────────────────────────────
        ⊢ lhs := rhs : attribution-form(σ)
```

The RHS of `:=` is always a curly-bracketed set whose members are constituent-designations (rooted-path designations like `[Α/i./t.]`, `[Α/i./t./D./P.]`, `[Α/i./Q.]`). Per the dissertation's p.164 semantic intent, the members of the set are the constituents that share the attribute of having been evaluated upon by the operation on the LHS.

Rejection: `[a.]δ(...) := { [Α/i./t.], Σ(...)′ → P.′ }` is rejected — the set member `Σ(...)′ → P.′` is a projection-clause, not a constituent-designation, and projection-clauses are not licensed as `:=` RHS set members.

### §9.7 Predicates and comparisons

#### §9.7.1 Membership predicates (∋, ∌)

```
   ⊢ t1 : designation       ⊢ t2 : designation
   t1's terminal-sort is a resource-set    t2's terminal-sort is a resource-designation
   ─────────────────────────────────────────────────────────────────────────────────
                            ⊢ t1 ∋ t2 : predicate-form(boolean)
                            ⊢ t1 ∌ t2 : predicate-form(boolean)
```

The membership predicates type to boolean. The typing constraint is sort-asymmetric: the LHS must designate a resource-set (typically `[a./R.]` — the actor's current-resource set), and the RHS must designate a resource (typically a `[Α/i./o./g./q.]` path ending at a required-resource designator). The typing enforces the capability-gate's intended structure.

**Sort-name versus runtime.** The sort name `resource-set` is a Layer-2 syntactic-category label — designations that name an actor's resource holdings — and does not commit to set-vs-multiset multiplicity. Runtime instances in the R-component operate under multiset semantics (multiplicities admitted; deduction via `⊖`, accrual via `⊎`); see §11.1 and §13.4. The sort name predates D-1's multiset reconciliation and is retained as a stable Layer-2 label; the multiplicity discipline lives at the runtime layer, not the sort name. Membership (`∋`/`∌`) under multiset semantics is still boolean — "present with any positive multiplicity" vs "absent" — so §9.7.1's typing rule is unaffected by the runtime distinction.

#### §9.7.2 Comparison operators (<, >, ≤, ≥)

```
   ⊢ t1 : cmp-operand       ⊢ t2 : cmp-operand
   t1's terminal-sort is utility       t2's terminal-sort is utility
   ────────────────────────────────────────────────────────────────
              ⊢ t1 ⟨cmp-op⟩ t2 : comparison-form(boolean)
```

The four comparison operators all take two utility-typed operands and produce a boolean. **Operands are `⟨cmp-operand⟩` (designation or primed designation), not bare designations** — this matches the §8.9 grammar production for `⟨comparison-form⟩` and is what makes projected utility comparisons (Intention bodies, where both sides are primed) typeable alongside realized utility comparisons (Perception lines, where both sides are unprimed). Without this, every Intention body in Tables 5–22 would fail at the comparison step. Per Charles T5 Intention: the inner `{ [Α/i./t./D./P./u.]′ > [Α/i./t./D./X./u.]′ }` types because `>` takes two primed-designation `⟨cmp-operand⟩`s, each with terminal sort `utility`. Per Charles T5 Perception: the inner `{ [Α/i./t./D./P./u.] > [Α/i./t./D./X./u.] }` types because `>` takes two unprimed designations, same terminal sort. The same typing rule covers both.

#### §9.7.3 Evaluation equality `=` (inner utility-comparison sense)

```
   ⊢ t1 : cmp-operand       ⊢ t2 : cmp-operand
   t1's terminal-sort is utility       t2's terminal-sort is utility
   ────────────────────────────────────────────────────────────────
                ⊢ t1 = t2 : comparison-form(boolean)
```

The inner `=` operator types to boolean and requires both operands to be utility-valued designations (optionally primed via the `⟨cmp-operand⟩` production). It is **not** the same operator as the outer `=` in `⟨perception-evaluation⟩`; the two are syntactically distinguished at parse time (inner `=` has designation LHS; outer `=` has prefixed-op-form or primed-form LHS). Layer 4 R-perceive uses this inner `=` for realized utility comparisons.

#### §9.7.4 Perception-evaluation form (outer `=`)

```
   ⊢ lhs : prefixed-op-form(Γ, target) | primed-form(prefixed-op-form(Γ, target))
   ⊢ rhs : set-of(comparison-form)
   ──────────────────────────────────────────────────────────────────────────
                  ⊢ lhs = rhs : perception-evaluation
```

The outer `=` types a Perception (or primed Perception) against the set of utility comparisons it realizes (or projects). This is the form Charles T5 writes as `[Α/i./t.]Γ(...) = { ... > ... }` (realized) or as the body of an Intention equivalence `[Α/i./t.]Γ(...)′ = { ... > ... }` (projected). The LHS must be a target-prefixed Perception specifically; the RHS must be a singleton set whose member is a comparison-form. Layer 4 R-perceive-success and R-perceive-failure dispatch on which inner comparison-form is realized; the perception-evaluation form is the typing-level witness that the dispatch is well-formed.

The two senses of `=` (§9.7.3 inner, §9.7.4 outer) are mutually exclusive at parse time — `⟨comparison-form⟩` admits only designation/primed-designation operands (per the `⟨cmp-operand⟩` production); `⟨perception-evaluation⟩` admits only an unprimed or primed prefixed-op-form on its LHS (per the tightened `⟨perception-lhs⟩` production in §8.9, which deliberately excludes primed designations to keep the LHS productions disjoint). Type-checking selects one rule per parse tree position with no ambiguity, and the RHS shapes (cmp-operand vs set) provide belt-and-suspenders disambiguation.

### §9.8 Lexer normalizations at the typing level

Four normalizations from Layer 1 (M4, D-21, D-26, D-27) have been applied before typing begins. Layer 2 sees the normalized vocabulary, and its typing rules use the normalized sorts.

**M4 (Α/A normalization).** Greek Α and Latin A are identified at the lexer. By the time Layer 2 sees a term, both have been retokenized to a single internal `Α`. The typing rules use `agenda` as the sort name and never need to distinguish source-text Α from A.

**D-21 (Θ/Φ/Λ source reconciliation).** Operation-form occurrences of Θ in the source corpus have been rewritten to Φ (when followed by `/Q.`) or Λ (when followed by `/U.`) before parsing. Layer 2's prefix-dispatch table (§9.4) lists Φ and Λ separately from Θ, and the Θ that survives post-lexer is only the nominal form (no `Θ(...)` operation form remains in any case). The typing rules treat the three sorts (`resource-obtained` Φ, `utility-obtained` Λ, `resource-set` Θ) as distinct.

**D-26 (matrix-path shorthand normalization).** Source-text occurrences of `Α/i./D./...` (interest directly followed by matrix, target node implicit) have been rewritten to `Α/i./t./D./...` (canonical form, target node explicit) before parsing. Layer 2's child-class lattice (§9.3.1) admits `matrix` as a child of `target` only — never of `interest` directly — so any path that reached Layer 2 with `i./D./` would fail the A1 child-class typing premise. D-26 ensures every matrix-bearing path arrives at typing in canonical form, making the lattice's tightness consistent with the dissertation's surface shorthand.

**D-27 (perception-path canonicalization).** Source-text occurrences of `Γ(.../t./G.)` (target directly followed by perception node, matrix node implicit — used in projected Perception forms inside Intention bodies) have been rewritten to `Γ(.../t./D./G.)` (canonical form, matrix node explicit) before parsing. Layer 2's child-class lattice admits `perception` as a child of `matrix` only — never of `target` directly — so any Γ argument that reached Layer 2 with `t./G.` would fail the A1 child-class typing premise on the perception terminal. D-27 ensures every Γ argument arrives at typing with the canonical `.../t./D./G.` terminal pattern, making Γ's op-compatibility (§9.4.3 — argument's terminal sort must be `perception`) uniform across realized and projected Perception forms.

### §9.9 The complete typing judgment (consolidated)

The Layer 2 typing relation `Σ ⊢ t : τ` is the smallest relation closed under the inference rules above plus the following uncontroversial closure conditions:

1. **Variable lookup:** if `Σ(x) = τ` then `Σ ⊢ x : τ` (this rule rarely fires in LSPI; the system has few free variables).
2. **Sub-term typing:** every immediate sub-term of a typed term is itself typed by some rule.
3. **Sort uniqueness:** if `Σ ⊢ t : τ1` and `Σ ⊢ t : τ2`, then `τ1 = τ2`. Each well-typed term has a unique sort.

The full set of inference rules:

|                      Rule                      |                Sort produced                |                                  Discharged in                                  |
|------------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------|
| Slash composition (A1 with discharged premise) | `path-of(σ)`                                | §9.3                                                                            |
| Sole-of-type dot (A5)                          | `constituent-ref`                           | §9.3 (trivially typed via constituent-symbol → constituent-ref)                 |
| Ordinal-suffixed constituent (A6, A7)          | `constituent-ref`                           | §9.3 (trivially)                                                                |
| Prime (C1)                                     | `primed-form(t)`                            | §9.5 / §9.6 (where projectables appear)                                         |
| Designation (B1)                               | `constituent-designation`                   | §9.3, §9.7                                                                      |
| Op-form (B2)                                   | `op-form(σ)`                                | §9.4.3 (op-compatibility)                                                       |
| Actor-prefixed op-form                         | `prefixed-op-form(op, actor)`               | §9.4                                                                            |
| Target-prefixed op-form                        | `prefixed-op-form(op, target)`              | §9.4                                                                            |
| Systemic op-form                               | `prefixed-op-form(op, systemic)`            | §9.4                                                                            |
| Effect-form (C7a)                              | `effect-form`                               | §9.5.1                                                                          |
| Projection-clause (C7b)                        | `projection-clause`                         | §9.5.2                                                                          |
| Equivalence-form                               | `equivalence-form(σ)`                       | §9.6.1                                                                          |
| Attribution-form                               | `attribution-form(σ)`                       | §9.6.2                                                                          |
| Predicate-form (∋, ∌)                          | `predicate-form(boolean)`                   | §9.7.1                                                                          |
| Comparison-form (<, >, ≤, ≥)                   | `comparison-form(boolean)`                  | §9.7.2                                                                          |
| Evaluation-form (=)                            | `comparison-form(boolean)`                  | §9.7.3                                                                          |
| Set (B3, D5)                                   | `set-of(σ)` (homogeneous over member sorts) | §9.6, §9.7                                                                      |
| Arithmetic-form (D1, D2)                       | `arithmetic-form`                           | (typed by Layer 1 form; restricted to matrix-component / resource paths per D6) |

### §9.10 Worked examples through Layer 2

To ground the typing rules, three expressions from the dissertation's worked cases are typed.

**Example 1 — Charles Table 5 Interest line:**

```
[a.]ι(Α/i.) := { [Α/i./Q.] }
```

Typing:
- `Α/i.` is a path: by A1 (with child-class), Α is `path-of(agenda)`; `i.` is `interest`; `child-class(agenda)` admits `interest`; so `Α/i. : path-of(interest)`.
- `ι(Α/i.)` is an op-form by B2: ι expects an argument with terminal sort `interest`; this matches; so `ι(Α/i.) : op-form(interest)`.
- `[a.]ι(Α/i.)` is a prefixed-op-form by §9.4: ι admits actor-prefix; `[a.]` is the actor literal; so `[a.]ι(Α/i.) : prefixed-op-form(ι, actor)`.
- `[Α/i./Q.]` is a designation by B1: `Α/i./Q.` is a path (with `Q.` representing `resource-obtained` per D-21's shorthand); so `[Α/i./Q.] : constituent-designation`.
- `{ [Α/i./Q.] }` is a set by B3: a singleton set of constituent-designations; sort `set-of(constituent-designation)`.
- `[a.]ι(Α/i.) := { [Α/i./Q.] }` is an attribution-form by §9.6.2: LHS is a prefixed-op-form, RHS is a set of constituent-designations; sort `attribution-form(interest)`.

Well-typed.

**Example 2 — Charles Table 5 Resource check:**

```
[a./R.] ∋ [Α/i./o./g1/q.]
```

Typing:
- `a./R.` is a path: `a.` is the actor root-anchor; `R.` is `resource-set`; `child-class(actor)` admits `resource-set`; so `a./R. : path-of(resource-set)`.
- `[a./R.]` is a designation: sort `constituent-designation` with terminal-sort `resource-set`.
- `Α/i./o./g1/q.` is a path of depth 4 under Α: each child-class check passes (`agenda → interest`, `interest → objective`, `objective → intention` (`g1` is an ordinal-bearing intention), `intention → resource-required`).
- `[Α/i./o./g1/q.]` is a designation with terminal-sort `resource-required`.
- `[a./R.] ∋ [Α/i./o./g1/q.]` is a predicate-form by §9.7.1: LHS is a designation with terminal-sort `resource-set`, RHS is a designation with terminal-sort `resource-required` (a resource-designation); types as `predicate-form(boolean)`.

Well-typed.

**Example 3 — Sarah Table 14 Objective definition (the case that drove the §8 r2 fix):**

```
[a.]ω(Α/i./o./g2/i./o.) ≡ { [Α/i./o./g2/i./t.]Σ(Α/i./o./g2/i./t./D.)′ → [Α/i./o./g2/i./t./S./P.]′ }
```

Typing:
- `[a.]ω(Α/i./o./g2/i./o.)` is a prefixed-op-form by §9.4: ω is actor-only; LHS types as `prefixed-op-form(ω, actor)`. The argument's terminal sort is `objective` (since the path ends in `o.` at depth 6).
- The RHS body: `[Α/i./o./g2/i./t.]Σ(Α/i./o./g2/i./t./D.)′ → [Α/i./o./g2/i./t./S./P.]′` is a projection-clause by C7b:
  - LHS of `→`: `[Α/i./o./g2/i./t.]Σ(Α/i./o./g2/i./t./D.)′` — a primed prefixed-op-form. Σ is target-only; the prefix path `Α/i./o./g2/i./t.` types as `Α-rooted-path-of(target)`; the argument types as `path-of(matrix)`; the unprimed form types as `prefixed-op-form(Σ, target)`; prime promotes it to `primed-form(prefixed-op-form(Σ, target))`.
  - RHS of `→`: `[Α/i./o./g2/i./t./S./P.]′` — a primed designation. The path's terminal sort is `position` (via the selection-extension through `S`); the unprimed designation types as `constituent-designation`; prime promotes to `primed-form(constituent-designation)`.
  - Both sides are `projection-operand` (primed-form alternative); types as `projection-clause`.
- The whole equivalence: by §9.6.1, ω's equiv-body-of(objective) admits a projection-clause; the LHS sort matches; types as `equivalence-form(objective)`.

Well-typed.

### §9.11 What Layer 2 does NOT do

Layer 2 says which terms are well-typed. It does not say:

- Which terms are **congruent** (Layer 3). Layer 3's structural congruence treats `(a/b)/c` and `a/(b/c)` as equal (per A2 associativity), but Layer 2 types them identically without invoking the congruence.
- How configurations **evolve** (Layer 4). Type-correct terms are eligible for transition, but typing alone does not fire any transition.
- Whether a well-typed expression **makes political-domain sense**. A well-typed `[a.]δ(Α/i./d.) := { [Α/i./Q.] }` is structurally and type-wise valid; whether the actor's Detection actually identifies the Obtained-Resource attribute is a substantive question Layer 2 does not address.
- **Subtype relations between operation sorts.** LSPI v1 has no subtyping; each operation has a single sort. Future extensions may add subtyping (e.g., "Required-Resources is a subtype of Resource"), but the v1 typing system is sort-monomorphic.

Layer 2 is the gate that ensures the parse tree's structural skeleton corresponds to a politically-meaningful relation. Everything past that gate trusts the typing.

### For AI engines

The mechanical procedure for typing an LSPI term:

1. **Verify Layer 1 first.** Type-checking only applies to well-formed terms. If the term has not passed Layer 1, surface the Layer 1 failure and stop.
2. **Recursively type sub-terms.** Apply the typing rules above to each sub-term. The order is bottom-up: leaf constituents type first (constituent-symbol → constituent-ref by A5/A6/A7), then paths (by A1 with child-class lookup), then op-forms (by B2), then prefixed-op-forms, primed-forms, sets, predicates, and finally the top-level form (attribution, equivalence, effect, projection-clause).
3. **Consult the child-class lattice (§9.3.1)** for every slash composition. Reject any composition whose child sort is not in the parent's admissible-child set, citing the parent and child sorts and the missing lattice entry.
4. **Consult the prefix-admissibility table (§9.4.1)** for every prefixed-op-form. Reject any prefix-op combination not in the table.
5. **Consult the op-compatibility map (§9.4.3)** for every op-form. Reject any operation whose argument's terminal sort does not match the operation's expected input sort.
6. **For `→` forms, dispatch by parse-tree position:** effect-form or projection-clause. Apply the corresponding typing rule.
7. **Yield the term's sort.** Pass the typed term to Layer 3 (congruence) for further reasoning, or to Layer 4 (transition) when the term appears in a configuration.

When type-checking fails, surface the rejection with citation to the specific rule (e.g., "rejected at §9.4: Σ admits only target-prefix, but the parse tree shows actor-prefix `[a.]Σ(...)`"). Do not coerce; do not silently re-type. Failures are part of the audit trail.

---

## §10 Layer 3 — Structural Congruence (Equational Axioms)

Layer 3 specifies *when two well-typed LSPI terms denote the same thing*. It does not specify how terms transform under execution — that is Layer 4 (transitions), and the distinction is the load-bearing one for this section. Equational reasoning runs in both directions: if `s ≡ t`, then `t ≡ s`. Computational reasoning runs in one direction: if `s ⟶ t`, then `t` is what `s` becomes, and the reverse step is not licensed. This section is the **only** layer of the system where the word *axiom* is the right word. Every rule in §11 (transitions) is directional and is therefore a rule, not an axiom; every rule in §9 (typing) is a judgment derivation rule, not an axiom. Confusing the three has been the historical source of nearly every published process-calculus error in the political-science adaptations the dissertation reviewed, so Layer 3 is policed strictly.

The substantive claim of §10, picking up the credit §7.3 took: the structural congruence over LSPI terms is generated by **three** equational axioms, and only three. Every other equational property — slash non-commutativity, slash non-idempotence, yields-arrow direction-preservation, primed-vs-unprimed distinctness, reflexivity, symmetry, transitivity, congruence-under-substitution — is either a consequence of those three generators (combined with what Layers 1 and 2 already constrain) or a free property of congruence-hood itself. §10 retires the credit by proving each consequence below.

### §10.1 The three generators

The structural congruence `≡` on well-typed LSPI terms is defined as the **least equivalence relation closed under congruence** (substitution into any context) that satisfies the following three equational axioms:

**Axiom A2 (slash associativity).** For any three constituents `a`, `b`, `c` whose pairwise slash compositions are admitted by the child-class lattice (§9.3.1),

```
   (a / b) / c   ≡   a / (b / c)
```

The slash operator is left-binding by convention (§8.5.1), but A2 makes that convention purely syntactic — the underlying address denotes the same path regardless of bracketing. Witness: the realized-perception path `Α/i./t./D./G.` and the projected-perception path `Α/i./t./D./G.′` parse left-binding, but every Layer 4 rule that pattern-matches on a sub-path may rebracket freely. Source: Lam 2018 §3.4.2 (path equivalence under address composition); validation: every multi-segment slash path in Tables 5–22 admits both bracketings without changing its referent.

**Axiom D5 (set order irrelevance).** For any two designations `d_1, d_2` of the same terminal sort, appearing as members of a designation-set,

```
   { d_1, d_2 }   ≡   { d_2, d_1 }
```

By induction, any permutation of a finite designation-set is congruent to the original. The set braces `{ … }` are an unordered collection, not a sequence, and this axiom is what makes them so. Witness: Charles T5's operation record at C=14 lists `θ` candidates in the order Charles considered them, but no Layer 4 rule may depend on that order — the candidate set `{ [Α/i./o./g1] , [Α/i./o./g2] , [Α/i./o./g3] }` is congruent to any permutation. Source: Lam 2018 §3.5.1 (operation-record sets as unordered membership); validation: Tables 8, 13, 16, 19 each list candidate sets in a presentation order that differs across worked cases for the same constituent sort, with no semantic consequence.

**Axiom M4 (Latin-A / Greek-Alpha normalization).** For any path-root character occurrence,

```
   A   ≡   Α
```

where `A` is the Latin capital A (U+0041) and `Α` is the Greek capital Alpha (U+0391). The lexer normalizes one to the other before yielding tokens to the parser (§8.2.2), so M4 records the equational fact that justifies the normalization rather than introducing it. Witness: dissertation Tables 5–22 use `Α` consistently; analyst notes recovered from the Pepperdine archive use `A`; the lexer treats them as the same root. Source: Lam 2018 §3.2 footnote 7 (typographic note on the actor root); validation: M4 is the only one of the three generators that is purely typographic — A2 and D5 capture genuine semantic structure, M4 captures a glyph collision.

These three are the generators. No fourth.

**Note on glyph collision (added for reader disambiguation).** The Layer-3 structural-congruence relation `≡` defined in this section shares its glyph with the Layer-1 **binding-form** `≡` used inside operation bodies (e.g., `[a.]ω(...) ≡ { ... }` per §8.4.3 / §8.9). The two are distinct constructs: the Layer-3 `≡` is an equivalence relation on well-typed terms (this section's subject); the Layer-1 `≡` is a syntactic constructor binding an op-form to a body. There is no parse-level ambiguity (the Layer-1 binding has an op-form on its left and an equiv-body on its right; the Layer-3 relation relates any two well-typed terms), but the shared glyph is a notational artifact preserved from the dissertation and warrants the explicit flag for readers approaching §10 fresh. See §8.4.3's symmetric note at the constructor site.

### §10.2 What congruence-hood gives for free

The phrase **least equivalence relation closed under congruence** in §10.1 is doing substantial work. Unpacking it:

1. **Reflexivity:** for every well-typed term `t`, `t ≡ t`. *Free from equivalence-hood.* Not asserted as an axiom in §10.
2. **Symmetry:** for all well-typed terms `s, t`, if `s ≡ t` then `t ≡ s`. *Free from equivalence-hood.* Not asserted.
3. **Transitivity:** for all well-typed `s, t, u`, if `s ≡ t` and `t ≡ u` then `s ≡ u`. *Free from equivalence-hood.* Not asserted.
4. **Substitution-under-context (congruence proper):** for any context `C[·]` and any well-typed terms `s, t`, if `s ≡ t` then `C[s] ≡ C[t]`. *Free from the phrase "closed under congruence."* Not asserted as an axiom.

Property 4 is what makes `≡` a congruence (not merely an equivalence). It says: equivalence propagates through every syntactic constructor — slash composition, set braces, prefix brackets, operation argument positions, primed marks, comparison operators, and the yields arrow. A term and any congruent substitution into any well-typed position denote the same thing. Layer 4 (transition) and Layer 5 (theorems) both rely on this property without restating it.

The reason these four come free, not as axioms, is that they are properties of the *least equivalence relation closed under congruence* — the moment you commit to defining `≡` as that object, all four hold by construction. Treating reflexivity or symmetry as a separate axiom would be the system-design equivalent of writing `0 = 0` as an axiom of arithmetic: it is true, it is asserted by the definition of equality, and asserting it separately is a tell that the author did not understand what an equivalence relation is. §10 names the four properties so that proofs in §13 may invoke them; it does not list them in the same status as A2, D5, M4.

### §10.3 Thinness — what falls out as consequence

The structural congruence with generators {A2, D5, M4} is **thin**: a large family of claims that political-process notations from the prior literature (Granovetter 1973, Pfeffer 1981, Lukes 1974, and the precursor notations the dissertation reviewed in §2) asserted as separate axioms turn out to be theorems of LSPI's three generators plus the Layer 1 grammar and Layer 2 type system. §7.3 promised three retirements in particular: A3, A4, and C11. §10.3 pays.

**Consequence A3 (slash non-commutativity).** For distinct constituents `a ≠ b` admitting a slash composition in at least one order, `a / b ≢ b / a`.

*Proof sketch.* Suppose `a / b ≡ b / a`. Since `≡` is the *least* equivalence relation closed under congruence satisfying {A2, D5, M4}, every congruence pair must be derivable from those three generators by some finite sequence of: (i) reflexive base steps, (ii) symmetric and transitive closure, (iii) substitution into a context, (iv) instances of A2, D5, or M4. None of A2, D5, M4 equates `a / b` to `b / a` for distinct `a, b`. A2 rebrackets but does not permute. D5 permutes set members, but `a / b` is a slash composition, not a set. M4 normalizes a glyph, not a structural position. No finite derivation reaches `a / b ≡ b / a`, so the supposition fails. ∎ Validation: Charles T5's path `Α/i./t./D./G.` is the perception sub-tree of his interest in the matrix's reading of the goal; `Α/G./t./D./i.` is a malformed token sequence the Layer 1 grammar rejects outright. Where both orderings are well-typed (rare, and only when the parent sort admits both child sorts), the two paths address distinct constituents in the principal's agenda.

**Consequence A4 (slash non-idempotence).** For any constituent `a`, `a / a` is not a well-typed term, so the question `a / a ≡ a` does not arise inside the congruence relation.

*Proof sketch.* The child-class lattice (§9.3.1) admits a slash composition `a / b` only if `b`'s sort appears in `a`'s admissible-child column. Inspection of §9.3.1 confirms that no sort appears in its own admissible-child column — for a concrete witness, the `target` row's admissible-child column is `{matrix (D), selection (S)}`, neither of which is `target`. The same exclusion holds for every other row of the lattice. Therefore `a / a` is rejected by Layer 2 before Layer 3 sees it, and §10 reasons only over well-typed terms. ∎ This is a stronger result than A4 as conventionally stated in process-calculus textbooks (which usually assert `a / a ≢ a` as a separate axiom in untyped settings): in LSPI the question never reaches Layer 3 because Layer 2 has already eliminated it. A4 retires by becoming a Layer 2 lattice fact, not a Layer 3 axiom. Validation: no row of any worked case in Tables 5–22 contains a path with two adjacent identical sort segments.

**Consequence C11 (yields-arrow direction preservation).** For terms `σ, τ` of compatible perception-yield sorts (§9.6) with `σ ≠ τ`, `σ → τ ≢ τ → σ`.

*Proof sketch.* The same uniqueness-of-derivation argument as A3. No generator equates `σ → τ` to `τ → σ`. A2 is about the slash operator, not the yields arrow. D5 is about set membership, not directional yielding. M4 is about a glyph in the actor root, not the arrow. No derivation from {A2, D5, M4} reaches the swap, so the swap is not in `≡`. ∎ Validation: `→` lives in Objective/Outcome bodies and effect-forms (§9.6), never in Perception lines (those use `=` over comparisons, §9.7.4), so C11's validation is drawn from where `→` actually occurs. Charles T5's Objective body `[Α/i./t.]Σ(Α/i./t./D.)′ → [Α/i./t./S./P.]′` reads as *the projected selection over the matrix yields the projected preferred position*; reversing the arrow reads as *the position yields the selection*, which no worked case ever holds. The arrow's direction is what makes the body a forward projection rather than a backward inference, and that asymmetry is preserved by `≡` because no generator equates the two orderings.

Three retirements complete. §7.3 is paid.

### §10.4 What §10 deliberately does not contain

Two families of rules are tempting at this point in the system and both are excluded by design.

**The first temptation: R-unfold.** A system designer may notice that the operation record holds names for designations whose bodies appear elsewhere in the same record, and may want to write an *unfold* axiom — replace the name by the body — as an equational property. This temptation must be refused. Unfolding is *directional*: the operation record's audit value depends on which form is on the page when, and folding an unfolded body back into a name would erase the unfolding step from the record. The unfold operation is therefore Rule **R-unfold** in §11.x (Layer 4 transition), where directionality is the whole point. If R-unfold were placed in §10 as an axiom, equational reasoning would let proofs in §13 silently re-fold expanded definitions, and the persistence invariant (§7.5) — which depends on the operation record being a directional log — would fail. Layer 3 is symmetric. Anything directional belongs in Layer 4.

**The second temptation: structural-congruence-as-typing.** A system designer may notice that the M4 generator (`A ≡ Α`) blurs the line between lexer normalization and typing, and may want to import other typing-flavored facts into §10 — for example, asserting `[Α/i./o./g_k] ≡ [Α/i./o./g_k]′` to capture some notion of "structural sameness modulo time-indexing." This is rejected. The prime mark is a Layer 1 grammar constituent introduced as axiom C5 (§8) with its own well-formed forms (§8.4.2), and Layer 2 carries the distinction by giving the primed form its own `primed-form(σ)` sort (§9.2). The primed form denotes a *future-projected* expectation; the unprimed form denotes a *realized* observation. They are not equationally the same and equating them would collapse the realized-vs-projected distinction that the Charles T5 worked case, the Jim/John T8 case, the Sarah T16 case, and the Rusty T19 case all depend on. M4 is the only typographic generator; no other typographic or typing flavored equation enters §10.

Both temptations have the same structure: a property that looks equational on first read turns out to be directional or sort-distinguishing on second read. The guardrail is to test every candidate rule against the directional and sort questions before allowing it into §10.

### §10.5 The complete congruence — consolidated statement

Putting §10.1 and §10.2 together, the structural congruence `≡` on well-typed LSPI terms is **defined** as the smallest binary relation on the set of well-typed terms such that:

1. `≡` is reflexive, symmetric, and transitive.
2. `≡` is closed under substitution into any well-typed context (the congruence-proper property).
3. For all well-typed terms `a, b, c`: `(a / b) / c ≡ a / (b / c)`. [A2]
4. For all designations `d_1, d_2` of the same terminal sort and any designation-set membership context: `{ d_1, d_2 } ≡ { d_2, d_1 }`. [D5]
5. For every path-root occurrence: `A ≡ Α`. [M4]

Nothing else. The five-clause statement above is the complete definition of `≡`. Any equational property of LSPI terms that proofs in §13 invoke either appears in this list, is a consequence of this list combined with the Layer 1 grammar and Layer 2 type system (as shown in §10.3), or is a property of equivalence relations / congruence relations in general (as identified in §10.2).

### §10.6 Worked examples — what is and is not congruent

The dissertation tables make every congruence claim below either explicitly or by implication. The examples here are selected to show the boundary between congruence (Layer 3) and transition (Layer 4) — the line that §10.4 spent its budget protecting.

| # |                                  Term pair                                  | Congruent? |                                                                                                                                                                                     Justification                                                                                                                                                                                     |
|---|-----------------------------------------------------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | `(Α/i.)/t.` vs. `Α/(i./t.)`                                                 | Yes        | A2, single application                                                                                                                                                                                                                                                                                                                                                                |
| 2 | `Α/i./t./D./G.` vs. `Α/(i./(t./(D./G.)))`                                   | Yes        | A2, applied right-associatively four times; the path's referent is invariant under rebracketing                                                                                                                                                                                                                                                                                       |
| 3 | `{ [Α/i./o./g1] , [Α/i./o./g2] }` vs. `{ [Α/i./o./g2] , [Α/i./o./g1] }`     | Yes        | D5, single swap                                                                                                                                                                                                                                                                                                                                                                       |
| 4 | `A/i./o./g1` vs. `Α/i./o./g1`                                               | Yes        | M4 applied to the root character                                                                                                                                                                                                                                                                                                                                                      |
| 5 | `[Α/i./o./g1]` vs. `[Α/i./o./g2]` for distinct sub-indices                  | No         | Distinct goal sub-indices denote distinct goal designations; no generator equates them                                                                                                                                                                                                                                                                                                |
| 6 | `[Α/i./o./g1]` vs. `[Α/i./o./g1]′`                                          | No         | The prime mark is a Layer 1 distinguishing constituent (§8.4.2); §10.4 guardrail; realized and projected forms are sort-distinct via C5 (§8) and the `primed-form(σ)` sort (§9.2)                                                                                                                                                                                                     |
| 7 | `θ(Α/i./o./g1)` vs. `[Α/i./o./g1/q.]` (the body θ would unfold to)          | No         | This is an R-unfold equality, directional, belongs in §11.x; treating it as `≡` would erase the unfolding step from the operation record                                                                                                                                                                                                                                              |
| 8 | `σ → τ` vs. `τ → σ` for distinct σ, τ                                       | No         | C11 consequence (§10.3)                                                                                                                                                                                                                                                                                                                                                               |
| 9 | `[Α/i./t.]Γ(Α/i./t./D./G.) = { … }` vs. `{ … } = [Α/i./t.]Γ(Α/i./t./D./G.)` | No         | The outer `=` is the perception-evaluation operator (§9.7.4), which is *not* symmetric — the LHS is the perceiver's prefixed-op-form, the RHS is the perceived utility yield. The inner `=` is symmetric (§9.7.3), but the outer is not. §10 does not introduce any equational property of `=` — symmetry of the inner sense follows from `=`'s typing rule, not from a Layer 3 axiom |

Pair 7 is the most instructive. The pull to call it a congruence is strong — the body is *the same thing* the name resolves to, after all. But that "after all" is doing the work of a transition step. R-unfold is a Layer 4 rule precisely because the operation record needs to log the unfolding moment as a distinct event in the audit trail; if pair 7 were a Layer 3 congruence, proofs could silently swap names for bodies and the trail would be irrecoverable. The dissertation's commitment to operation-record integrity (§7.5, §8 of the dissertation) is what forces this design choice, and §10's tight three-generator presentation is what protects it.

### §10.7 What Layer 3 does not do

Layer 3 does not transform terms — that is Layer 4 (transitions). Layer 3 does not type terms — that is Layer 2. Layer 3 does not parse terms — that is Layer 1. Layer 3 does not prove theorems — that is Layer 5 (which uses Layer 3 as one of its premises). Layer 3 says only: *which well-typed terms denote the same thing, by virtue of three equational axioms and the free properties of being a congruence relation.* Everything else about how LSPI terms behave is the work of another layer.

In particular, Layer 3 is silent on:

- **Order of operation-record entries.** The operation record is a directional log; D5 covers unordered designation-sets *within* a record entry, not the sequence of entries across cycles. The cycle counter `C` of the configuration `⟨C ; M ; S ; R⟩` (Part I §4.2) orders the entries, and reordering them would violate the persistence invariant (§7.5).
- **The transition relation `⟶`.** Layer 4 introduces `⟶` and the 21 transition rules (plus two non-firing disciplines). Layer 3 does not anticipate them.
- **Confluence of transition.** Whether `s ⟶ t_1` and `s ⟶ t_2` implies `t_1 ⟶* u` and `t_2 ⟶* u` for some `u` is a theorem about Layer 4 (proved or refuted in §13), not a Layer 3 property.
- **Bisimulation.** The classical π-calculus notion of bisimulation as a finer-grained equivalence than structural congruence is not introduced in LSPI. The political-engagement use case does not call for distinguishing between bisimilar but structurally-non-congruent processes; the operation record provides the relevant level of behavioral identity directly.

### For AI engines

When deciding whether two LSPI terms `s` and `t` are congruent, the procedure is:

1. **Reject ill-typed inputs immediately.** Layer 3 reasons only over well-typed terms (§9). If either `s` or `t` fails type-checking, do not invoke `≡`; report the type error.
2. **Normalize both terms** by applying A2 (right-associate every slash composition for canonical form), D5 (sort every designation-set by a fixed total order on its members — e.g., lexicographic on the terminal designation strings), and M4 (map every root `A` to `Α`). Call the results `s°` and `t°`.
3. **Compare `s°` and `t°` for syntactic identity.** If identical, `s ≡ t`. If not, `s ≢ t`.

The normalize-then-compare procedure decides `≡` in time linear in term size, and is sound and complete relative to the three-generator definition because A2, D5, and M4 are all *confluent* equational rules with disjoint pattern targets (A2 acts on slash, D5 acts on set braces, M4 acts on the root glyph, and no pattern overlaps another).

Three things to refuse:

- **Do not unfold definitions during congruence-checking.** If a name appears in `s` and its body appears in `t`, that is an R-unfold relationship, decided at Layer 4, not Layer 3. Report `s ≢ t` from the congruence engine and let the caller decide whether to invoke R-unfold.
- **Do not equate primed and unprimed forms.** `[…]` and `[…]′` are distinct under `≡` by §10.4. Realized and projected utilities do not collapse.
- **Do not assume symmetry of the outer `=`.** The perception-evaluation operator's typing rule (§9.7.4) is asymmetric in role (LHS perceiver address, RHS perceived yield set). Even though `≡` is symmetric as a relation, that symmetry does not extend to making `=` a symmetric operator on its arguments.

When the procedure returns `s ≡ t`, the result is logged in the audit trail with citation of which generators (A2, D5, M4) the normalization invoked, and how many applications of each. This is overhead for short terms but indispensable for the longer paths and sets in Tables 16, 19, and 22, where the chain of equational reasoning is long enough that a human reviewer needs to be able to retrace it.

---

## §11 Layer 4 — Transition Relation (Operational Semantics)

Layer 4 specifies *how LSPI terms transform under execution*. Where Layer 3 said when two terms denote the same thing — equationally, in both directions — Layer 4 says how a configuration of LSPI terms steps forward through the principal's agenda, directionally, one cycle at a time, with every step logged. The relation is `⟶` (single-step transition); `⟶*` is its reflexive-transitive closure (multi-step). The transition relation `⟶` is defined by rules organized into three families: **fourteen lifecycle rules** walking the principal through a single normal-path cycle (open → interest → detect → objective → intention → required-resources → gate → execute → perceive → select → outcome → obtained-utility → close → flowback); the **failure family** handling guard failures, escalations, mooting, and abandonment (R-spawn, R-resume, R-close-nested, R-perceive-failure, R-moot, R-abandon); and the **non-destructive family** — one transition rule (R-objective-revise) plus two non-firing disciplines (R-unfold and R-prime-preserve) that the persistence invariant governs. Totals: **twenty-one transition rules** (14 + 6 + 1) plus **two non-firing disciplines**, matching the count consolidated at §7.1, §10.7, and §11.7.

The directionality of `⟶` is the load-bearing semantic change crossing the §10/§11 boundary. In §10 the relation `≡` was symmetric: `s ≡ t` implies `t ≡ s`. In §11 the relation `⟶` is one-way: `s ⟶ t` does **not** imply `t ⟶ s`, and any rule that attempted to assert the reverse step would erase the just-logged operation-record entry, violating the persistence invariant (§7.5). The whole layer is built around this asymmetry. Every rule has a redex (the term-shape it pattern-matches), a contractum (what the redex becomes), and side conditions; no rule has a reverse companion. When you want both directions, you want equational reasoning, and that belongs in Layer 3.

This sub-section drafts the fourteen lifecycle rules and validates them end-to-end against Charles T5 (dissertation Table 5). The failure family is drafted in §11.6 in a separate review batch — its configuration plumbing (S-stack push/pop, R-set flowback under suspended-parent state) is subtle enough that it deserves isolated review against Rusty T19 (escalation case) and Sarah T16 (revise-and-moot case). The non-destructive three are drafted in §11.7 in the third batch, against the persistence invariant.

### §11.1 The configuration ⟨C ; M ; S ; R⟩

Part I §4.2 defined the configuration. This sub-section recaps the four slots that the transition rules pattern-match on:

- **C — active-cycle pointer.** A natural number identifying the currently active cycle. Advances via R-open (top-level new cycle) and R-spawn (nested sub-cycle, both push a new cycle onto the principal's agenda); **decreases via R-resume** when control returns to a suspended parent (§11.6.4). C is therefore **not monotonic** in the presence of escalation — it tracks the *active* cycle's identifier, not a sequence index. **Cycle identity is monotonic** and is recorded structurally: a cycle's identity is the C-value at its `⟨open, C⟩` marker, and that identity persists across suspensions and resumes. Each rule tags its M-entries with the active C; downstream readers (audit, theorem-proving) can recover any cycle's full event sequence by filtering M for entries tagged with that cycle's identity. In a chain of escalations the M-tags interleave across cycles, but each cycle's entries remain coherent under filter-by-identity.
- **M — operation record / running matrix.** A sequence of audit-trail entries, each tagged with the cycle in which it was written. **M is append-only** — no rule removes or rewrites a prior entry. The persistence invariant (§7.5) is what makes M's monotonicity load-bearing. Entries are well-formed LSPI declarations — interest bodies (ι-body), detection bodies (δ-body), objective bodies (ω-body), intention bodies (γ-body), required-resources bodies (θ-body), execution bodies (ε-body), perception bodies (Γ-body), selection bodies (Σ-body), outcome bodies (Ω-body), obtained-utility bodies (Λ-body), obtained-resources bodies (Φ-body) — plus a family of structural markers (`⟨open, C⟩`, `⟨gate-pass, [Α/i./o./g_k/q.]⟩`, `⟨select-staged, σ⟩`, `⟨close, C⟩`, `⟨flowback-recorded, E⟩`) that record phase-transition events the surface-syntax declarations alone would not capture.
- **S — suspended-parent stack.** A stack of cycle records preserved when an inner cycle is spawned to handle a gate failure (covered in §11.6). Empty in the normal-path lifecycle; this batch's rules touch S only in the trivial sense of "S unchanged."
- **R — resource multiset.** A multiset of resource designations the principal currently holds (matching §4.2's "multiset of resources" — corrected from earlier set-notation prose). The multiset framing is load-bearing for conservation: holding two units of a resource and spending one leaves one (not zero), which set-difference cannot express. The gate (R-gate) reads R to test whether the **required-resource** designation `[Α/i./o./g_k/q.]` is present (multiset membership: any positive multiplicity counts as "present"); R-execute removes one occurrence of `cost(·)`'s designations via multiset difference `⊖`; R-flowback and R-close-nested add `earnings(·)`'s designations via multiset sum `⊎`. R is the only slot that both grows and shrinks within the normal lifecycle path.

Notation conventions used throughout §11:

- `last(M-cycle-C)` denotes the most recent entry in M whose cycle tag equals C. Most lifecycle rules' premises read this projection to enforce phase ordering.
- `M ⊎ e` denotes M appended with new entry `e`, **tagged with the cycle-identity the entry semantically records** — *not* mechanically with the active-cycle pointer C at the moment of writing. For lifecycle rules that do not transition C (the eleven substantive rules R-interest through R-obtained-utility, plus R-close and R-flowback), the two coincide: the entry is tagged with the active C. For the **three C-transitioning rules** (R-spawn, R-resume, R-abandon), the tag is specified per-entry by the rule's contractum:
   - **R-spawn** writes two entries with different tags: `⟨gate-fail, q⟩` tagged with the **failing parent** cycle (pre-transition C, since the gate-fail records the parent's failed attempt), and `⟨open, C+1⟩` tagged with the **new sub-cycle** (post-transition C+1, since the open marker creates that cycle's identity).
   - **R-resume** writes `⟨resume, parent-C, q⟩` tagged with the **resumed parent** cycle (post-transition C = parent-C, since the resume marker records control returning to that cycle).
   - **R-abandon** writes `⟨abandon, C⟩` tagged with the **abandoned** cycle (pre-transition C; the entry records the closing of the cycle being abandoned, even when control transitions to the parent on the same step).

The per-rule tagging is what makes `last(M-cycle-X)` mechanically well-defined across C-transitions — without this clause, R-gate's post-resume trigger (which reads `last(M-cycle-parent-C) = ⟨resume, parent-C, q⟩`) would be ambiguous because the resume marker could be read as tagged either with the sub-cycle's C (pre-transition) or with parent-C (post-transition). The tag is fixed by the rule, not by the transition. The operator `⊎` is associative but emphatically non-commutative — order of entries within M is part of the audit trail's semantics.
- `R ⊖ X` denotes **multiset-difference** — R minus one occurrence of each designation in X (R-execute uses this for resource consumption: a held multiplicity of two becomes one, not zero); `R ⊎ X` denotes **multiset-sum** — R with one occurrence of each designation in X added (R-flowback and R-close-nested use this for resource accrual). The set-difference operator `\` and set-union `∪` are **not** used on R; they were the earlier-draft framing that D-1 reconciled away because set-arithmetic cannot express "hold two, spend one, leaves one" — see §11.1 R-multiset description above and §13.4.1's conservation invariant.
- **⊎ operand-typing.** The `⊎` glyph is operand-typed and carries two distinct semantics: `M ⊎ e` (defined above) is **sequence-append** — non-commutative, because entry order in M is audit-trail-load-bearing; `R ⊎ X` (defined just above) is **multiset-sum** — commutative, because multiset accumulation discards order. Same glyph, opposite commutativity, disambiguated by operand sort (M is the operation record; R is the resource multiset). The overload is deliberate (both operations are "extend the structure by adding") but a reader scanning the two definitions in isolation should track which operand each `⊎` is acting on.
- `cost(·)` and `earnings(·)` are deterministic functions the rules invoke for resource bookkeeping. `cost(·)` reads a **required-resource** designation of the form `[Α/i./o./g_k/q.]` (lowercase q, per #18 Required Resources — declared by θ in cycle C, tested by R-gate, deducted by R-execute) and returns the resource-designation set R-execute removes from R. `earnings(·)` returns the **obtained-resource designation set E** the cycle's outcome records: in the worked-case treatment, E is the obtained-Q designations Table 5's flowback row attests to for cycle C (Charles T5 line 192: `[a.]Θ(Α/i./O./Q.) := { [Α/i./Q.] }`, post-D-21 → Φ) — the declared-direct reading is canonical, settled by the row-by-row pass against Table 5. In a live engagement, E is the analyst's recorded observation of obtained resources for that cycle. R-flowback writes E as the body of the **Φ operation** (uppercase Q / Φ, per #19 Obtained Resources), making the declaration explicit in the audit trail. §13 (theorems) will state determinism formally; for §11 both functions are taken as given. **Normal-path ι↔Φ property:** on the normal path, Φ's body is identical to ι's declared `[Α/i./Q.]` — the cycle obtained the resource it set out for, and the want/get loop is structurally traceable from the cycle's ι row to its Φ row (Charles T5: row 179 declares `{ [Α/i./Q.] }`, row 192 obtains `{ [Α/i./Q.] }`). This identity is a **property of the normal path, not a construction rule**: the failure family (§11.6) breaks it deliberately — mooted and abandoned cycles obtain nothing (Φ body is the empty set, or Φ doesn't fire), and escalation cycles may obtain a different resource than the parent's ι declared. R-flowback always reads what was *actually* obtained via `earnings(·)`; it does not synthesize Φ's body from the ι-body. The ι↔Φ match is a theorem of the normal path, not a precondition of the rule.

**`IntentionPosition` derived view (added 2026-06-23 per Thread A IntentionPosition reframe; design at `LPIC-Thread-A-IntentionPosition-Design.md`, Phase 1 audit at `LPIC-Thread-A-Rule-Edit-Phase1-Audit.md`; recognizer tightened to position-bearing 2026-06-23 post-Batch-5-review per the Sarah-Table-14 catch).** For per-intention rules in steps 4–9, the positional `last(M-cycle-C)` enumeration is replaced by a per-K-filtered fold over append-only M-cycle-C:

```
   IntentionPosition(M-cycle-C, g_k) =
       the most-recent *position-bearing* entry e ∈ M-cycle-C such that e is "about g_k"
       (in g_k's position-defining role for that shape),
       interpreted as the LifecyclePosition encoded by e's shape.

       If no position-bearing entry about g_k exists in M-cycle-C, IntentionPosition(g_k) = undeclared.
```

Where the **position-bearing shapes** are exactly the nine that encode a LifecyclePosition value (the shape ↔ LifecyclePosition map):

| Shape | Position-defining g_k role | Encodes LifecyclePosition |
|---|---|---|
| `γ(Α/.../g_k) ≡ {...}` | g_k as **argument terminal** of γ | `declared` |
| `θ(Α/.../g_k) := {...}` | g_k as **argument terminal** of θ | `θ-written` |
| `⟨gate-pass, q⟩` | q ∈ `q_of(g_k)` (q is gate's q-argument; under disjoint q-sets q identifies g_k uniquely) | `gate-passed q` |
| `⟨gate-fail, q⟩` | q ∈ `q_of(g_k)` (the specific failed q ∈ q_of(g_k) \ R) | `gate-failed q` |
| `⟨resume, parent-C, q⟩` | q ∈ `q_of(g_k)` (q delivered by sub-cycle) | `resumed q` |
| `[a.]ε(Α/.../g_k/e.) → {...}` | g_k as **next-to-last argument-path segment** before `/e.` | `executed` |
| `⟨perceive, g_k⟩` | g_k as **direct second argument** | `perceived` (validating; Rusty pattern) |
| `⟨perceive-failure, g_k⟩` | g_k as **direct second argument** | `perceived` (failing; Rusty pattern) |
| `⟨moot, C, g_k⟩` | g_k as **direct third argument** | `mooted` |

**Crucial distinction (refined post-Batch-5 review): "about g_k" requires both shape AND role.** The first-draft recognizer ("tagged with g_k in the entry's path") was structurally under-specified: it would match an ι/ω/δ-body whose path carries g_k as **provenance only** (e.g., a sub-cycle's ι at `Α/i./o./g2/i.` carries `g2` as the parent's intention sub-index — provenance, not position-defining), and then try to interpret that ι-shape as a LifecyclePosition, which is undefined (ι is not in the shape ↔ position table above). **Sarah Table 14's sub-cycle ι revision exposes this**: the revised ι at `[a.]ι(Α/i./o./g2/i.) := { [Α/i./o./g2/i./Q.] }` has both path AND body carrying `g2`, but ι is not a position-bearing shape and the `g2` is provenance, not g_k-as-LifecyclePosition-argument. **The tightened recognizer skips it.**

**Non-position-bearing entries that may carry g_k provenance (excluded from the fold).** Cycle-prologue bodies (ι, ω, δ), cycle-shared Γ-bodies (the target-prefixed `[Α/i./t.]Γ(...)` written by R-perceive / R-perceive-failure / R-perceive-cycle / R-perceive-failure-cycle — the marker companions are what carry IntentionPosition advancement; the Γ-body itself is non-position-bearing), and structural cycle-scoped markers (⟨open, C+1⟩, ⟨close, C⟩, ⟨moot, C⟩ at cycle scope, ⟨abandon, C⟩, **⟨perceive, C⟩ at cycle scope (Nathan validating cycle-perceive)**, **⟨perceive-failure, C⟩ at cycle scope (Nathan failing cycle-perceive)**, ⟨objective-revised, ...⟩, ⟨select-staged, σ⟩, ⟨flowback-recorded, E⟩, ⟨close-nested, sub-C, parent-C⟩) — these may carry g_k provenance in path-segments at sub-cycle scope (the `parent-prefix = base-prefix/o./g_k/` discipline of §11.6.2 propagates parent's g_k into every sub-cycle path), but they are not in the position-bearing shape set above. **IntentionPosition's fold skips all of them**, regardless of whether their path-form carries g_k as provenance.

**Note on the cycle-scoped perceive markers** (added post-Batch-5 review for tracing clarity): `⟨perceive, C⟩` and `⟨perceive-failure, C⟩` differ from their per-K cousins `⟨perceive, g_k⟩` and `⟨perceive-failure, g_k⟩` by exactly one character — but the role distinction is structural: C is the second argument in the cycle-scoped variants, and C is never any g_k (C is a cycle identifier, g_k is an intention sub-index — different sorts). So the role-spec "g_k as direct second argument" never matches `⟨perceive, C⟩` for any g_k, and the cycle-scoped marker is correctly excluded from per-K reads while still serving as R-select's conjunct (iii) cycle-shared producer. **Nathan-pattern cycles advance their live g_k's to `executed` per-K (via R-execute) and then write a single cycle-shared `⟨perceive, C⟩` (via R-perceive-cycle) — no per-K perceive-marker write happens; individual g_k's remain at `executed` throughout the Nathan path's terminal phase.** This is by design and is what makes R-select's executed-existential implication (§11.4.10 conjunct (iii)) fire correctly in Nathan-pattern cycles.

The companion derived view `q_of(M-cycle-C, g_k)` reads g_k's θ-declarations for its bound q-set: `q_of(g_k) = { q : θ(.../g_k) := { [.../g_k/q] } ∈ M-cycle-C }`. Relational under WF-6 (Axis 6 resolved 2026-06-24); single-valued under the functional-q_of specialization (Charles, Jim, Nathan, Sarah have |q_of(g_k)| = 1 for every g_k); multi-valued for Rusty (γ_1 has q_of = {q_1, q_2}). Bounded by Q_max per WF-6. The standing recognizer's `q ∈ q_of(g_k)` clause reads against this set.

**Companion derived view `CyclePattern(M-cycle-C)` (added 2026-06-24 to close Gate (4) perceive-pattern mechanical commitment + Axis 8-Sarah as one cut; peer of `q_of`; fold refined post-review to read over *declared* γ_k rather than *live* γ_k, see Stability paragraph below for the rationale).** A cycle-level derived view, computed at read-time by folding over the projected Γ-comparison bodies of every γ_k declared in M-cycle-C (i.e., `g_k ∈ DeclaredIntentions(M-cycle-C)`):

```
   CyclePattern(M-cycle-C) =
       per-intention   if ∃ declared γ_k whose projected Γ-comparison body
                         references an ordinally-indexed decision-matrix position
                         (P_n or X_n at the matrix-position level, n ≥ 1)
       cycle           otherwise (all declared γ_k's projected Γ-comparisons use
                         sole-dot P. and sole-dot X. at the matrix-position level)
```

**Discriminator scope (corpus-verified across all five cases).** The fold reads matrix-position designations (preferred-position P, adverse-alternative X) at the **decision-matrix layer** of the projected Γ-comparison body. **Cost/benefit sub-indices** (c, b — children of P or X via further `/c./` or `/b./` extensions) **do NOT count** — Nathan's K=2 cycle is `cycle` despite his γ-bodies carrying `c1`/`c2` cost-indices, because both intentions reference the same sole-dot P. (the cost-sub-index discriminates tactics, not the matrix position). Verified across:

- **Charles** (K=1, Table 5): γ-comparison uses sole-dot `P.` vs sole-dot `X.` → `cycle` (vacuous at K=1; one perceive)
- **Jim** (K=2, Table 6): both γ-comparisons reference sole-dot `P./c`, `P./b` (cost/benefit tactics on the unique P) → `cycle` → one cycle-level perceive
- **Nathan** (K=2, Table 7): both γ-comparisons reference `P./c1`, `P./c2` (cost sub-indices on the shared sole-dot P) → `cycle` → one interest-level realized Γ at Table 11
- **Sarah** (K=2, Table 12): γ₁ references `X1`, γ₂ references `X2` (ordinally-indexed adverse alternatives) → `per-intention` → "Perception of Intention 1" / "Perception of Intention 2"
- **Rusty** (K=3, Table 16): γ-comparisons reference ordinally-indexed `P1`/`P2` preferred positions → `per-intention` → per-intention realized Γs

The δ-body (R-detect's contractum) **over-lists** matrix-position alternatives — Charles's δ enumerates `X1, X2` even though his γ-comparison uses sole-dot `X.`; Jim's same. Detection *enumerates the matrix* (which positions exist); intentions *target* positions (which positions the cycle pursues). **CyclePattern reads γ-comparison bodies (what the cycle's intentions target), NOT δ-bodies (the over-listed matrix enumeration).**

**Sole-dot semantics (resolved 2026-06-24 — faithful, not representation-gap).** Per the dissertation's nomenclature subsection: "If the constituent contains no siblings, then the dot '.' is used to denote that it is the only element of its type in its parent set… 'A./i./P.' refers to the only preferred position in this whereas X1 refers to the first adverse alternative and X2 refers to the second" + "no constituents will ever share the same designation." Sole-dot is a **deliberate uniqueness marker** meaning "the unique instance of its type within its parent scope," NOT shorthand and NOT a representation gap. Ordinals (P1/P2, X1/X2) are used precisely when and only when siblings exist. This resolves both:
- **Gate (4)**: CyclePattern reads the dissertation's intentional ordinal vs sole-dot distinction at the matrix-position level — exactly what the corpus exhibits.
- **Axis 8-Sarah**: the alleged `R ⊖ [sole-dot-q]` ambiguity was a false alarm from address truncation — the dissertation's full θ-bodies are `θ(Α/i./o./g_k) := {[Α/i./o./g_k/q.]}`, distinct *full* designations differing at the g_k segment; "no constituents will ever share the same designation" guarantees uniqueness. Resolution: §11.4.8 R-execute's body-resolution side condition rewrites to the full g_k-scoped `R ⊖ [Α/i./o./g_k/q.]` (via `q_of(g_k)`). Bare `[q.]` in dissertation source rows is typographic abbreviation of the full address, not a semantic ambiguity.

**Persistence Invariant compliance.** `CyclePattern` is a derived view over append-only M-cycle-C — a fold over the existing γ-declaration bodies, no new state stored, no marker introduced. Same status as `q_of`, `IntentionPosition`, `PendingTheta`, `LiveIntentions`, `MootedIntentions`, `DeclaredIntentions`. §7.5 satisfied.

**Stability under WF-5 (see §13.5.2).** WF-5 (perceive-pattern cycle-conformance, added 2026-06-24) requires all declared γ_k in a cycle to conform to one CyclePattern value — either all references sole-dot at the matrix-position level (cycle), or each references its own ordinal index at the matrix-position level (per-intention). The conformance is a Layer-2 well-formedness condition that rides on R-intention's existing "well-typed at Layer 2" premise: R-intention(g_k) at k ≥ 2 fails the typing check if g_k's projected Γ-comparison body would violate the cycle's CyclePattern (e.g., introducing an ordinal `P_n` into a sole-dot cycle, or sole-dot `P.` into an ordinal cycle). Under WF-5 — combined with §7.5's append-only M — **CyclePattern is set by R-intention(g_1)'s firing and stable thereafter** — there is no second writer, no further evolution.

**Why `declared` and not `live` (post-review correction 2026-06-24).** An earlier draft of this definition folded over *live* γ_k. That formulation made the "no second writer" claim technically false: R-moot-intention(g_k) is a domain-writer for the `live` formulation because its `⟨moot, C, g_k⟩` contractum shrinks `LiveIntentions`, which is the fold's domain. The *value* happens to be invariant under mooting (existential-monotone: if any remaining live γ_k was per-intention before mooting, it still is after), so the conclusion held — but the justification had a hole §13.6's perceive-determinism step would have hit: citing "CyclePattern is constant" would have triggered a separate value-invariance lemma to discharge the R-moot-intention domain-write. The post-review fix folds over `declared` γ_k instead. Since γ-declarations are append-only (§7.5; no rule removes a γ-entry; the `DeclaredIntentions` view is monotone-growing), R-moot-intention is no longer a domain-writer, and "set-once / no further evolution" becomes literally true. All five corpus classifications survive the change (a mooted γ_k's γ-declaration still carries its ordinal-or-sole-dot in M; the discriminator's read is unchanged); WF-5 conformance is checked at γ-declaration time anyway, so it's naturally a property of the declared set, not the live set.

This is what makes CyclePattern a stable derived view, **NOT** a coupling surface (NOT a global fold F6); §13.6's confluence proof reads CyclePattern as a constant, not a write-coupled value. (See Phase 1 audit §A3 catalog note for the explicit non-coupling classification.)

**LifecyclePosition values**: `undeclared | declared | θ-written | gate-passed q | gate-failed q | resumed q | executed | perceived | mooted`.

**Ontology note (refined 2026-06-23 post-Batch-3-review, trace-don't-inventory catch).** The first draft of this section listed `⟨spawn, sub-C, q_k⟩` as a recognized "about g_k" marker shape and `spawn-pending q` as a distinct LifecyclePosition value. Both were vestigial residue from a draft where gate-failure and sub-cycle-spawn were separate steps. The actual spec consolidates them: **R-spawn (§11.6.2) atomically writes `⟨gate-fail, q_k⟩` (parent-tagged) + `⟨open, C+1⟩` (sub-cycle-tagged) in one firing, then pushes S and transitions C to the sub-cycle.** No rule writes a `⟨spawn, sub-C, q_k⟩` marker — that marker is a phantom — and `spawn-pending q` is a dead LifecyclePosition value (unreachable by any rule). The realized escalation walk for g_k is:

```
θ-written  →  [R-spawn fires]  →  gate-failed q_k  →  [sub-cycle runs; parent IntentionPosition(g_k) unchanged] 
            →  [R-close-nested writes parent-R ⊎ E]  →  [R-resume writes ⟨resume, parent-C, q_k⟩]  
            →  resumed q_k  →  [R-gate re-fires]  →  gate-passed q_k  →  executed
```

`gate-failed q_k` is the position from R-spawn's firing through R-resume's firing — covering both "gate just failed in the parent" and "sub-cycle in flight under it" in a single LifecyclePosition value. The **suspended-waiting semantics is carried by the S-stack entry** (parent-C, parent-pending-q, parent-prefix) and the **C-transition** (active C is sub-cycle during the escalation), NOT by the IntentionPosition value. Adding a redundant `spawn-pending` value would violate the minimal-mechanism design and let §13.5 / §13.6 enumerations stumble on an unreachable value. Removed for soundness; the consolidated `gate-failed q_k` is internally complete.

**Persistence Invariant compliance.** Both `IntentionPosition` and `q_of` are derived views — folds over append-only M-cycle-C — per §7.5. Nothing is stored; the filter computes at read-time. The convention coexists with `last(M-cycle-C)` (still used by cycle-shared close rules, steps 10–14) and with §11.6.6.2's operative-`last` (the intention-moot skip convention, a localized first hint of this per-K-filtered structure).

**Per-K-filtered reads vs global-fold reads (three-category meta-principle, per Phase 1 audit §A1).** Per-intention rule premises read two distinct kinds:
- **Per-K-filtered** (filtered by the rule's own g_k): `IntentionPosition(g_k)`, `g_k fresh in M-cycle-C`, `g_k ∈ DeclaredIntentions`, `g_k ∈ MootedIntentions`. Writes about g_a do NOT change reads about g_b.
- **Global-fold** (three categories): **cardinality** (`|DeclaredIntentions| < K_C`, `|LiveIntentions \ {g_k}| ≥ 1`, `PendingTheta = ∅`); **earliest-of-set** (R-rr's `earliest g ∈ PendingTheta`); **all-of universal** (R-select's `∀ live g_k: PerIntentionTerminal`). Writes that change the fold couple to every rule reading it.

Per-K-filtered existentials (e.g., g_k freshness) are NOT global folds even when they look existential — they filter by the rule's own g_k.

**Cycle-shared phase boundaries (used by per-intention rule premises to gate admissibility).** Per-intention rules read whether the cycle is currently in its per-intention phase (steps 4–9 active):

```
   per-intention phase active  ↔  ω-body ∈ M-cycle-C
                                  ∧  ⟨select-staged, σ⟩ ∉ M-cycle-C
                                  ∧  {⟨close, C⟩, ⟨moot, C⟩, ⟨abandon, C⟩} ∩ M-cycle-C = ∅
```

(objective has been declared; R-select has NOT fired the handoff to cycle-shared close; no cycle-shared terminal marker yet). **The `⟨select-staged, σ⟩` exclusion is load-bearing** (refined 2026-06-23 post-Batch-1-review): R-select writes the handoff marker that ends the per-intention phase one phase earlier than R-close. Without this clause, R-intention (and any other per-intention rule keyed off the boundary) would remain admissible during steps 10–13 (R-outcome → R-obtained-utility → R-close → R-flowback), letting a new γ_k declare into a cycle that has already committed its selection — incoherent, and it would manufacture a spurious R-intention vs cycle-shared-close σ-fork that §13.6 would have to carry in I. The per-intention phase ends at R-select's `⟨select-staged, σ⟩`, not at R-close. No worked case is affected (every R-intention firing in the corpus is pre-select, including Rusty's post-perceive-failure γ_3 declaration); the clause only closes the soundness gap.

The cycle-shared close phase (steps 10–14, starting at `⟨select-staged, σ⟩`) reads literal-`last` over cycle-scope entries as today; IntentionPosition applies only to the per-intention phase (steps 4–9).

**Independence relation `I` (governs §13.6 confluence, per Phase 1 audit §A4).** Pairs of rules are **I-independent** iff (a) neither's writes change the other's reads AND (b) their non-M side-effects (R, S, C) commute. Per-intention rules at distinct g_k under WF-6 with **disjoint q-sets** (`q_of(g_a) ∩ q_of(g_b) = ∅` whenever a ≠ b) are I-independent on per-K reads; couplings arise through (i) the four global folds F1 (DeclaredIntentions cardinality), F2 (PendingTheta), F3 (LiveIntentions cardinality), F4 (PerIntentionTerminal universal), (ii) cycle-shared scalars R / S / C, and (iii) same-g_k IntentionPosition reads. The full I-classification catalog is in the Phase 1 audit §A4; per-rule prose below cites the relevant coupling(s) at the point they matter.

### §11.2 The inference-rule form

Every transition rule below is presented in the standard SOS form (Plotkin):

```
   premise_1     premise_2     ...     premise_n
   ─────────────────────────────────────────  [R-name]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C' ; M' ; S' ; R'⟩
```

Below each rule appears a **redex form** specification (the §8 grammar shape the rule keys off, or a configuration-state predicate when the rule is structurally triggered rather than surface-syntax triggered), **side conditions** (constraints on free variables, well-typedness of the redex, phase preconditions), and a **worked-case validation** pointer to the specific row of Charles T5 (Table 5) the rule fires at. Every rule's redex is a form §8 admits and §9 types; no rule introduces new syntax.

### §11.3 The lifecycle invariant — phase progression

A single normal-path cycle progresses through fourteen phases in fixed order, each licensed by exactly one rule:

```
   open  →  interest  →  detect  →  objective  →  intention  →
   required-resources  →  gate  →  execute  →  perceive  →
   select  →  outcome  →  obtained-utility  →  close  →  flowback
```

The actor-half of the cycle (steps 2–6) is declared by five operation-bearing constituents from §8.5.1: **ι** (Interest, #4), **δ** (Detection, #5), **ω** (Objective, #7), **γ** (Intention, #9), **θ** (Required Resources, #18). The gate (step 7) is a Boolean test, not an operation declaration. Execute (step 8) writes **ε**. The matrix-half (steps 9–10) is declared by two target-prefixed operations — **Γ** (Perception) and **Σ** (Selection) — both **target-only** per §9.4.1. The systemic Outcome (step 11) is declared by **Ω** (#8), which is **systemic-only** (no prefix) per §9.4.1. **Obtained Utility** (step 12) is declared by **Λ** (target-prefixed), the target's utility gain — post-D-21 retokenization of the dissertation's target-prefixed `Θ` form (§8.5.2). The flowback (step 14) is declared by **Φ** (Obtained Resources, #19, actor-prefixed), which records the obtained-resource designation set the cycle yields; with Λ at step 12 and Φ at step 14, every one of the eleven operation-bearing constituents in §8.5.1 has a defined firing point in the lifecycle. Structural markers (`⟨open, C⟩`, `⟨gate-pass, q⟩`, `⟨select-staged, σ⟩`, `⟨close, C⟩`, `⟨flowback-recorded, E⟩`) handle phase transitions between the operation declarations and carry inter-rule context (the staged Σ projection-clause, the recorded earnings) that no surface-syntax form is allowed to carry at top-level per §8.9.

**Row-correspondence note (lifecycle rules vs. Table 5 rows).** The lifecycle has fourteen rules, of which **eleven correspond directly to dissertation Table 5 rows**: R-interest (row 179), R-detect (180), R-objective (184), R-intention (185), R-required-resources (186), R-gate (187), R-execute (188), R-perceive (189), R-outcome (190), R-obtained-utility (191), R-flowback (192). **Three rules are system-internal artifacts** without dissertation rows: R-open and R-close are structural markers for audit-trail discipline (the dissertation doesn't write structural meta-data); R-select stages the Σ → P projection-clause as marker data because §8.9 forbids that clause at top-level, with R-outcome later folding it into Ω's body where §8.9 admits it (the dissertation just embeds the Σ → P clause inside Ω at row 190 directly, which is what the staging+folding sequence produces in M). So "every Table 5 row has a corresponding lifecycle rule" is correct; "every lifecycle rule has a corresponding Table 5 row" is correct *modulo* the three structural rules (R-open, R-select, R-close).

The order is a partial function — each phase enables the next, and the next-phase rule's preconditions encode "previous phase has completed." The lifecycle is the **normal path**; deviations branch off at gate, perceive, or select into the failure family (§11.6), which either resumes the lifecycle from where it left off (R-resume) or aborts the cycle (R-moot, R-abandon).

**The fourteen-phase order is the single-intention skeleton, not an invariant step count.** R-intention's expanded premise (§11.4.5) admits one or more γ entries per cycle (one per intention sub-index `g_k`), so a multi-intention cycle **iterates the objective-through-perceive segment (steps 4–9) once per `g_k`**: each intention gets its own γ → θ → gate → execute → perceive pass before the cycle converges on a single select → outcome → obtained-utility → close → flowback (steps 10–14). Sarah Table 12 declares γ₁ and γ₂ upfront and runs the iteration twice; Rusty Table 16 → 18 → 20 declares γ₁, γ₂, γ₃ incrementally across resumes and runs the iteration three times. The §11.5 trace (one intention, `g.`) is the linear base case — N=1 iteration. The phase order is fixed *within* a single intention's pass; the number of passes is determined by how many γ entries the cycle declares.

Charles T5 (dissertation Table 5) is the validation case for every rule below. Each rule's worked-case pointer names the operation symbol of the row the rule fires at; precise row-by-row alignment against Table 5 has been validated (the §11.5 trace walks Charles T5 cycle 1 row by row, and the eleven substantive rules align with eleven Table 5 operation-rows — 179 ι, 180 δ, 184 ω, 185 γ, 186 θ, 187 gate, 188 ε, 189 Γ, 190 Ω, 191 Λ, 192 Φ — in fixed order, modulo the three structural rules R-open / R-select / R-close that have no dissertation row per §11.3's row-correspondence note). **Rows 181–183 are representative single-designation rows** in dissertation Table 5 that print the path-form of one instance per kind — target (181: `[Α/i./t.]`), preferred position (182: `[Α/i./t./D./P.]`), and adverse alternative (183: `[Α/i./t./D./X.]`). They are not separate operation-row declarations and have no rule mapping; they are descriptive accompaniment to R-detect's δ-body at row 180, which is the operational source of truth for what designations the cycle declares.

**Dissertation-internal inconsistency at row 183 (flagged so the LSPI trace does not silently adopt the wrong form).** Row 180's δ-body enumerates four members including **two indexed adverse alternatives** `[Α/i./t./D./X1]` and `[Α/i./t./D./X2]`, while row 183's standalone Adverse-alternative row describes one alternative in prose ("Harry is not transferred or demoted") with the sole-dot designation `[Α/i./t./D./X.]`. The dissertation does not explain what the second `X` refers to. **LSPI adopts the δ-body's enumeration as the source of truth** — R-detect's body (§11.4.3) declares two indexed adverse alternatives matching row 180 exactly; the §11.5 trace step 3 shows four members. Row 183's sole-dot `X.` is treated as a representative class-marker for the adverse-alternative *sort*, not a definitive count. This is the only dissertation-internal inconsistency Charles T5 exhibits at the row level; every other §11.5 trace step matches its corresponding Table 5 row exactly.

**Verification provenance.** The dissertation-content claims in the paragraph above — that row 180's δ-body enumerates four members with `X1` and `X2`, that row 183's standalone row uses prose "Harry is not transferred or demoted" with sole-dot `[Α/i./t./D./X.]`, and that the conflict is internal to Table 5 — were verified against the dissertation extract at `Lam-2018-Pepperdine (just the important bits).md` lines 180 and 183 during the §13.1 row-by-row pass. The claims are mine to stand behind; readers without the dissertation in front of them are not relied on for certification.

### §11.4 The fourteen lifecycle rules

#### §11.4.1 R-open — open a new cycle (cycle-prologue; literal-`last` read on whole-M confirmed correct per §11.1 cycle-shared convention 2026-06-23 per Thread A reframe — R-open is the rule that CREATES a cycle's identity, so no IntentionPosition substrate applies pre-firing; the new cycle's M-cycle-C is empty until R-open writes ⟨open, C+1⟩)

```
   (M = ∅ ∧ C = 0)  ∨  ((last(M) = ⟨flowback-recorded, _⟩)  ∧  S = [])
   ─────────────────────────────────────────  [R-open]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C+1 ; M ⊎ ⟨open, C+1⟩ ; S ; R⟩
```

**Redex form.** No surface-syntax redex — R-open is structurally triggered (initial state, or the previous cycle just completed flowback). The rule writes the structural marker `⟨open, C+1⟩` to M and advances C.

**Side conditions.** S unchanged. R unchanged. R-open is the only rule that advances C; every other lifecycle rule operates within a fixed cycle. The "previous cycle just completed flowback" trigger (rather than "just closed") reflects that R-flowback is the *last* lifecycle rule of a cycle, after R-close — so R-open at C+1 must wait for R-flowback at C. The `S = []` premise distinguishes R-open from **R-resume** (§11.6.4), which fires from the same post-flowback state but only when S is non-empty (a suspended parent exists). The two rules are mutually exclusive on the S-emptiness condition.

**Worked-case validation.** Charles T5, Table 5, the row tagged C=1 (initial cycle open) and every subsequent row tagged C=k+1 immediately after `⟨flowback-recorded, _⟩` at cycle k.

#### §11.4.2 R-interest — declare the interest (cycle-prologue step 2; literal-`last(M-cycle-C) = ⟨open, C⟩` read confirmed correct per §11.1 cycle-shared convention 2026-06-23 per Thread A reframe — no IntentionPosition substrate change; pre-objective phase, so the §11.1 per-intention boundary's `ω-body ∈ M-cycle-C` condition is not yet satisfied — per-intention rules cannot fire here)

```
   last(M-cycle-C) = ⟨open, C⟩
   if S = []  (top-level cycle):
     N is a fresh interest-ordinal in M — no prior  [a.]ι(Α/iM) := …  in M for any M = N
     interest-path = Α/iN
     interest-body = { [interest-path/Q.] }   (actor's interest-level obtained-Q reference)
   if S ≠ []  (sub-cycle):
     interest-path = parent-prefix/i.   (sole-of-type within the inherited prefix, per A6)
     interest-body = { parent-pending-q }   (the parent's required-q literally — read from top
                                              S-entry, so the sub-cycle's want IS the parent's
                                              need; closes the want/get loop by design and is
                                              what makes R-resume's `R ∋ parent-pending-q`
                                              premise satisfiable via literal membership)
   [a.]ι(interest-path) := interest-body  is well-typed at Layer 2
   ─────────────────────────────────────────  [R-interest]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ([a.]ι(interest-path) := interest-body) ; S ; R⟩
```

**Redex form (top-level cycle, S = []).** `[a.]ι(interest-path) := { [interest-path/Q.] }` per §8.5.1 (ι in operation-bearing list, **#4 Interest**), §9.4.3 (ι typing rule), and **§8.10 Example 1** (labeled "Charles Table 5, Interest line"). The argument terminates at sort `interest`, matching the scheme every other operation rule follows (δ at `…/d.`, ω at `…/o.`, ε at `…/e.`). The body's `[interest-path/Q.]` is the actor's interest-level obtained-Q reference; the cycle is *opened by an actor with an interest*, and the body shape per §8.10 Example 1 is the form ι records that interest in.

**Redex form (sub-cycle, S ≠ []).** For sub-cycles, the body is `{ parent-pending-q }` instead — the parent's literal required-q designation read from the top S-entry, not the sub-cycle's own obtained-Q reference. The two forms differ because escalation exists precisely to fetch the parent's needed q, so the sub-cycle's ι must equal what the parent's gate will re-test.

**No downstream type ripple.** The sub-cycle's R-detect/R-objective/R-intention read the ι *interest-path*, not the ι *body*, so the body change is invisible to them. The only place the body surfaces is at R-flowback, where on the normal path the sub-cycle's Φ-body equals its ι-body via the ι↔Φ identity (§11.4.14) — Φ is built from `earnings(·)`, not read off ι, so a mooted/abandoned sub-cycle yields Φ-body ≠ `parent-pending-q` and R-resume correctly does not fire. That equality on the success path is what makes E = `parent-pending-q` = what R-resume tests.

**The interest-path is uniformly ordinal-numbered at top level and sole-dot at sub-cycle level.** This is the **iN discipline** for top-level cycles, required because top-level cycles all share the same agenda root `Α` and must therefore differentiate at the interest-node to avoid (W)-collision (Theorem 13.1's no-collision claim, §13.1.3.1):

- **Top-level cycles** (S = []): each top-level cycle's interest declaration uses an ordinal-numbered form `Α/iN` per A7's ordinal designator discipline, with N fresh in M. **The dissertation's surface form `Α/i.`** (used in every worked case because every documented engagement runs a single top-level cycle) **is normalized by D-28 (§8.2.2) to `Α/i1` post-lexer**, so the rule's redex is uniformly `Α/iN` for all N including N=1. Charles T5's `[a.]ι(Α/i.) := { [Α/i./Q.] }` reads post-D-28 as `[a.]ι(Α/i1) := { [Α/i1/Q.] }`. The "first sole-dot, subsequent numbered" mixed encoding that an earlier draft considered is rejected because it would violate A6 and A9 (the original `i.` is no longer sole-of-type once `i2` appears, and `i2` requires `i1` to exist for sibling completeness); the D-28 normalization handles this uniformly by reading sole-dot as the surface form of N=1.
- **Sub-cycles** (S ≠ []): each sub-cycle's interest is at `parent-prefix/i.` (sole-of-type within the inherited prefix, per A6). The `parent-prefix` (from the S-entry per §11.6.2) already discriminates the sub-cycle from sibling sub-cycles via the parent's gated `g_k`, so sole-dot suffices at the sub-cycle's interest. Sub-cycle re-spawn against the same parent g_k is forbidden by §11.6.7's tightened rule (any re-spawn from a failed sub-cycle must target a fresh g_k via R-intention's freshness), so two sub-cycles never share a `parent-prefix/i.` address. Sarah Table 13 line 338 demonstrates: `[a.]ι(Α/i./o./g1/i.) := { [Α/i./o./g1/q.] }` — sole-dot inside the parent-prefix `Α/i./o./g1/` (D-28 does not normalize sub-cycle sole-dot, only agenda-root sole-dot).

**Side conditions.** C unchanged (R-interest advances phase within the cycle, not the cycle pointer). S, R unchanged. Exactly one ι per cycle. **Top-level freshness premise**: when S = [], N must be distinct from every prior interest-ordinal in M (actor-scoped, not cycle-scoped). The freshness is the basis for Theorem 13.1's (W) no-collision at the interest-node layer.

**Worked-case validation.** Charles T5, Table 5, the ι row immediately following `⟨open, C⟩` — surface `Α/i.`, post-D-28 `Α/i1` (Charles has one top-level cycle, N=1). Sarah Table 13 line 338 — sub-cycle sole-dot under parent-prefix (unaffected by D-28). **No worked case directly exhibits a multi-top-level-cycle agenda** (every dissertation engagement runs a single top-level cycle that may have sub-cycles); the `Α/iN` form for N ≥ 2 is the natural extension by A7's ordinal discipline at the agenda-root level, applied uniformly to all top-level interests via D-28, and is what Theorem 13.1's (W) proof argues from.

#### §11.4.3 R-detect — detect the target, preferred position, and adverse alternative (cycle-prologue step 3; literal-`last(M-cycle-C) = ι-body` read confirmed correct per §11.1 cycle-shared convention 2026-06-23 per Thread A reframe — no IntentionPosition substrate change; **R-detect is the rule that re-fires after R-objective-revise** per §11.7.2 lifecycle-reset semantics — the revised ι-body becomes the new `last`, matching R-detect's premise — see §11.7.2 IntentionPosition preservation note for the interaction)

```
   last(M-cycle-C) = ι-body
   [a.]δ(Α/i./d.) := { [Α/i./t.], [Α/i./t./D./P.], [Α/i./t./D./X1], [Α/i./t./D./X2] }  is well-typed at Layer 2
   ─────────────────────────────────────────  [R-detect]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ([a.]δ(Α/i./d.) := { [Α/i./t.], [Α/i./t./D./P.], [Α/i./t./D./X1], [Α/i./t./D./X2] }) ; S ; R⟩
```

**Redex form.** `[a.]δ(Α/i./d.) := { … }` per §8.5.1 (δ in operation-bearing list, **#5 Detection**) and §9.4.3 (δ typing rule). The body's members are **constituent-designations of varying terminal sort** — the target `[Α/i./t.]`, the matrix-preferred-position `[Α/i./t./D./P.]`, and one or more matrix-adverse-alternatives `[Α/i./t./D./Xk]` (indexed per A7 — Charles T5 line 180 cites two: `[Α/i./t./D./X1]` and `[Α/i./t./D./X2]`) — unified at the `constituent-designation` level per §9.6.2 and Part I §6.3. The members are *not* all of sort `detection`.

**Side conditions.** C unchanged; S, R unchanged. The detection set is non-empty. **Ordinal-freshness for adverse-alternative sub-indices**: the Xk indices within the body are pairwise distinct (X1 ≠ X2 etc.), and are fresh within the parent matrix's adverse-alternative set in M (no prior δ entry's body in M-cycle-C declares the same Xk under the same parent matrix). This freshness is the basis for Theorem 13.1's (W) no-collision at the adverse-alternative sibling layer; without it, two adverse alternatives could share the address `[Α/i./t./D./X1]` and collapse into one constituent. The same freshness discipline applies to **preferred-position sub-indices** Pk when multiple preferred positions exist (e.g., Rusty Table 16 line 402 cites `[Α/i./t./D./P2]` — a second preferred position alongside the default P), with the analogous pairwise-distinct and parent-scoped freshness obligations on R-detect's body.

**Worked-case validation.** Charles T5, Table 5, the δ row immediately following ι. Charles's body cites his target plus the matrix's two key children (P, X) that will appear in the subsequent γ comparison.

#### §11.4.4 R-objective — declare the objective (projected selection-yields-position; cycle-prologue step 4; literal-`last(M-cycle-C) = δ-body` read confirmed correct per §11.1 cycle-shared convention 2026-06-23 per Thread A reframe — no IntentionPosition substrate change; **R-objective's ω-body write activates the §11.1 per-intention phase boundary** — once `ω-body ∈ M-cycle-C` holds and no terminal markers exist, the per-intention rules become admissible; this is the step-4/5 transition from cycle-prologue to per-intention phase)

```
   last(M-cycle-C) = δ-body
   [a.]ω(Α/i./o.) ≡ { [Α/i./t.]Σ(Α/i./t./D.)′ → [Α/i./t./S./P.]′ }  is well-typed at Layer 2
   ─────────────────────────────────────────  [R-objective]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ([a.]ω(Α/i./o.) ≡ { [Α/i./t.]Σ(Α/i./t./D.)′ → [Α/i./t./S./P.]′ }) ; S ; R⟩
```

**Redex form.** `[a.]ω(Α/i./o.) ≡ { [Α/i./t.]Σ(Α/i./t./D.)′ → [Α/i./t./S./P.]′ }` per §8.5.1 (ω in operation-bearing list, **#7 Objective**) and §9.6.1 (Objective equivalence body). The ω body holds a **projected** (primed) selection-yields-position projection-clause — the actor's planned matrix-mediated outcome. The Σ inside ω's body is target-prefixed and primed; the position is primed. The realized counterpart appears later inside Ω's body at R-outcome (same Σ form, unprimed).

**Side conditions.** C unchanged; S, R unchanged. Exactly one ω per cycle. The clause is **legally placed** because §8.9 admits projection-clauses inside equivalence bodies, which `≡` introduces.

**Worked-case validation.** Charles T5, Table 5, the ω row immediately following δ.

#### §11.4.5 R-intention — declare the intention (projected perception, premise revised 2026-06-23 per Thread A IntentionPosition reframe)

```
   per-intention phase active in M-cycle-C                  (per §11.1: ω-body present ∧ ⟨select-staged⟩ absent ∧ no terminal markers)
   IntentionPosition(M-cycle-C, g_k) = undeclared           (per-K freshness: ∄ prior γ-entry for g_k in M-cycle-C)
   |DeclaredIntentions(M-cycle-C)| < K_C                    (WF-1 cap: budget for fresh intentions remains)
   [a.]γ(Α/i./o./g_k) ≡ { [Α/i./t.]Γ(Α/i./t./D./G.)′ = { [Α/i./t./D./P./u.]′ > [Α/i./t./D./X./u.]′ } }  is well-typed at Layer 2
   ─────────────────────────────────────────  [R-intention]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ([a.]γ(Α/i./o./g_k) ≡ { [Α/i./t.]Γ(Α/i./t./D./G.)′ = { [Α/i./t./D./P./u.]′ > [Α/i./t./D./X./u.]′ } }) ; S ; R⟩
```

**Premise-shape note (revision rationale).** The pre-reframe premise enumerated positional `last`-states: `last(M-cycle-C) ∈ { ω-body, γ-body, ε-body, ⟨perceive-failure, C⟩ }`. This was the positional approximation of the standing-option surface — every enumerated `last`-state is a configuration where (cycle's per-intention phase is active) ∧ (some g_k is fresh) ∧ (K_C budget has room). Empirically the enumeration was correct (Sarah, Rusty traces fit), but it conflated three structurally distinct conditions and bound them to specific positions. The IntentionPosition reframe states the surface directly: (a) cycle-shared phase boundaries (ω-body present, no terminal markers), (b) per-K freshness as `IntentionPosition(g_k) = undeclared`, (c) global cardinality as explicit `|DeclaredIntentions| < K_C` (WF-1's cap, previously implicit). The new shape exposes the K_C cardinality coupling that the pre-reframe `last`-enumeration hid (per Phase 1 audit §A5.2 finding: R-intention pairs at distinct g_k couple through F1 cardinality, NOT through freshness).

**Redex form.** `[a.]γ(Α/i./o./g_k) ≡ { [Α/i./t.]Γ(Α/i./t./D./G.)′ = { comparison } }` per §8.5.1 (γ in operation-bearing list, **#9 Intention**) and **§9.6.1 Intention equivalence body** (`[a.]γ(Α/i./o./g.) ≡ { [Α/i./t.]Γ(…)′ = { … } }`). The argument terminates at sort `intention` (path `Α/i./o./g_k`), per the §9.3.1 lattice where intention is a child of objective. The γ body holds a **projected** (primed) perception equivalence whose inner comparison set asserts that the projected utility of the preferred position exceeds that of the adverse alternative. The Γ inside γ's body is target-prefixed and primed; the comparison's operands are primed utilities. This is the form the §9.7.2 review pass admits as `⟨cmp-operand⟩` (designation or primed designation). The `g_k` index in γ's argument threads the rest of the cycle: R-required-resources declares `[a.]θ(Α/i./o./g_k) := { [Α/i./o./g_k/q.] }` for the same `g_k`, R-gate tests that `g_k`'s q, and R-execute consumes that `g_k`'s cost — so γ is where the index originates that the gate-and-execute chain binds to.

**Standing-option principle (R-intention admissibility, per Thread A reframe).** R-intention is a **standing option** at every reachable cycle-state where (a) the cycle's per-intention phase is active (cycle-shared phase boundaries hold), (b) at least one fresh g_k is available (`IntentionPosition(g_k) = undeclared` for some g_k the operator can supply), AND (c) the WF-1 K_C budget has room (`|DeclaredIntentions| < K_C`). Like R-rr (§11.4.6) and R-moot-intention (§11.6.6.3), R-intention's admissibility is determined by derived views over M-cycle-C, not by literal-`last`. This is a third pervasive Pillar-4 interleaving-discretion surface alongside R-rr and R-moot-intention — the operator may declare a fresh intention at any point during the per-intention phase, subject only to the K_C budget and freshness.

**Coupling structure (per Phase 1 audit §A4).** R-intention's writes change three derived views:
- `|DeclaredIntentions|` increments by 1 — **couples to F1 (K_C cap)**: at `|DeclaredIntentions| = K_C - 1`, firing R-intention(g_a) disables R-intention(g_b) for any g_b (cap reached). **R-intention(g_a) ↔ R-intention(g_b) for distinct g_a, g_b is the I-coupling**, through F1 cardinality, NOT through per-K freshness (Phase 1 §A5.2 finding).
- PendingTheta gains g_k (new declared, θ not yet written) — **couples to F2 (R-rr earliest-pick)**: R-intention(g_a) ↔ R-rr coupled through PendingTheta membership.
- `|LiveIntentions|` increments — **couples to F3 (R-moot-intention's `|LiveIntentions \ {g_k}| ≥ 1`)**: state-conditional at the K-boundary.
- PerIntentionTerminal universal can be broken (new live g_k that hasn't terminaled) — **couples to F4 (R-select handoff)**: R-intention(g_a) firing late can delay R-select if another g_b had reached PerIntentionTerminal.

**I-independent** (per Phase 1 §A4.2): R-intention(g_a) ↔ R-execute(g_b), R-perceive(g_b), R-gate(g_b), R-moot-intention(g_b) for distinct g_b under WF-6 with disjoint q-sets — the per-K-filtered freshness and the per-K writes don't overlap.

**Side conditions.** C unchanged; S, R unchanged. **One or more γ entries per cycle, one per intention sub-index `g_k`.** R-intention may fire after R-objective (initial intention declaration), after another γ-body (sequential intentions declared upfront — Sarah Table 12 lines 325–326 declare γ₁ and γ₂ in sequence), after R-execute (dynamic intention addition — Rusty Table 18 line 440 declares γ₂ after ε₁), or after R-perceive-failure (post-failure intention addition — Rusty Table 20 line 473 declares γ₃ after Intention 2's perception fails). The fresh-`g_k` premise (now expressed as `IntentionPosition(g_k) = undeclared`) ensures each γ entry carries a distinct intention identifier within the cycle; the same g_k cannot be re-declared (use R-objective-revise — §11.7.2 — for body revision of an *existing* declaration at the same path).

**Worked-case validation.** Charles T5, Table 5, the γ row immediately following ω. The projected Γ comparison inside γ's body is the expectation that R-perceive's realized comparison must validate.

#### §11.4.6 R-required-resources — declare the required resources (PendingTheta premise, revised 2026-06-23 per §1.4.5 Axis 1b; re-stated under Thread A IntentionPosition substrate 2026-06-23)

```
   per-intention phase active in M-cycle-C                  (per §11.1: defense-in-depth — PendingTheta self-empties post-select, but uniform boundary held cheap)
   PendingTheta(M-cycle-C) ≠ ∅
   g_k = earliest-declared γ in PendingTheta(M-cycle-C)
   [a.]θ(Α/i./o./g_k) := { [Α/i./o./g_k/q.] }  is well-typed at Layer 2
   ─────────────────────────────────────────  [R-required-resources]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ([a.]θ(Α/i./o./g_k) := { [Α/i./o./g_k/q.] }) ; S ; R⟩
```

Where the **derived view** `PendingTheta(M-cycle-C)`, re-stated under IntentionPosition per design `LPIC-Thread-A-IntentionPosition-Design.md` §3.1, is:

```
   PendingTheta(M-cycle-C) = { g_k : IntentionPosition(M-cycle-C, g_k) ∈ { declared, θ-written } }
```

— the set of intention-goals `g_k` whose IntentionPosition has not yet advanced past `θ-written`. Under the functional-q_of specialization (|q_of(g_k)| = 1), g_k transitions from `declared` to `θ-written` on the first R-rr firing and immediately becomes σ-electable for R-gate (which closes coverage); under relational q_of (Axis 6, Rusty), g_k stays in PendingTheta at `θ-written` until σ elects to close coverage by firing R-gate — admitting Layer A's standing-option re-firing of R-rr to add additional θ's for distinct q's. The IntentionPosition framing automatically excludes mooted intentions (when `⟨moot, C, g_k⟩` is written, IntentionPosition(g_k) advances to `mooted`, removing g_k from PendingTheta) AND automatically excludes g_k post-R-gate (IntentionPosition advances to `gate-passed q` or `gate-failed q`, removing g_k from PendingTheta). The explicit moot-exclusion clause §11.6.6.3 flagged as needed is satisfied structurally by the IntentionPosition substrate; no separate clause is required. **"Earliest-declared"** reads entry-order over M-cycle-C: among the elements of PendingTheta, the rule picks the `g_k` whose γ-declaration entry has the lowest position in M-cycle-C's append-order.

**Redex form.** `[a.]θ(Α/i./o./g_k) := { [Α/i./o./g_k/q.] }` per §8.5.1 (θ in operation-bearing list, **#18 Required Resources**) and §9.4.3 (θ typing rule). The body declares the **required-resource** designation (lowercase **q**) for goal `g_k`. The path `[Α/i./o./g_k/q.]` reads as: the actor's interest's outcome's goal-`g_k`'s required-resource. In concrete worked-case terms `g_k` is written `g1`, `g2`, … per A6/A7.

**Persistence Invariant compliance (§7.5).** `PendingTheta` is a **derived view over M-cycle-C**, not a configuration slot. It is computed as a fold over M (γ-declarations minus θ-declarations) at the moment the rule's premise is checked; nothing is stored anywhere persistent. This is the same discipline §7.5 establishes for the dissertation's decision matrix Δ (`Δ = fold(M, current-cycle)`) and for the precedent that R-objective-revise's downstream readers use (filtered views of M rather than absolute `last(M-cycle-C)`, per the architectural note at §7.5.2 and the side-condition pattern at §11.7.2). M itself remains append-only; the contractum is `M ⊎ (one new θ entry)`, no rewrite, no removal. **§7.5 is satisfied without modification.**

**Side conditions.**

- C unchanged; S, R unchanged. The contractum writes one new θ entry per firing.
- The rule may fire from **any state where `PendingTheta(M-cycle-C) ≠ ∅`**, not only from `last(M-cycle-C) = γ-body`. This is the structural change from the prior `last`-keyed version, which could not reach Sarah T12 row 12 (fires θ_1 at `last = γ_2-body`) or Nathan T7 rows 11 and 14 (fires θ_1 at `last = γ_2-body`, then θ_2 at `last = ε_1-body`) — the §14.3.4 Sarah 1b re-walk and §14.3 Nathan walk together established that the source's θ firings are unreachable under the prior premise regardless of σ (Rule 2 reproduction-failure signal, formerly the Axis 1b defect at §1.4.5 row 122 Site (i) and row 122 Site (ii)).
- **Firing-order discipline (K-coverage caveat preserved)**: at K=2, "earliest-declared" coincides with "oldest-first" — the two are indistinguishable on the K=2 data the corpus supplies (Sarah T12 and Nathan T7 both fire θ_1 first at `last = γ_2-body`; both fit declaration-order, both fit oldest-first). "Earliest-declared" is pinned as the conservative framing: declaration-order is the more general specification; oldest-first is its K=2 specialization. K≥3 batched data, if it surfaces in a future case study, would test whether the rule should fire θ for the *oldest* pending-γ vs the γ in *declaration order* vs some other discipline; until then, declaration-order via entry-order in M-cycle-C is the strongest pin the data licenses.
- The rule may fire multiple times in a single cycle as PendingTheta is re-populated by subsequent R-intention firings — each θ entry is appended; the order across firings is determined by the earliest-declared discipline applied to each successive PendingTheta state.

**Worked-case validation across the corpus.**

- **Charles T5 (K=1, single γ)**: PendingTheta = {γ_1} at all γ-declaration / θ-pre-declaration states; rule fires once for γ_1. Identical behavior to the prior `last`-keyed version.
- **Jim T6 (K=2, interleaved θ/gate-pass per intention)**: PendingTheta is a singleton at each θ-firing position (γ_1 declared → θ_1 fires → gate passes → ε_1 → γ_2 declared → θ_2 fires); rule fires twice, each from a singleton PendingTheta. Identical behavior to the prior rule.
- **Sarah T12 (K=2, batched declarations)**: γ_1 declared (row 10), γ_2 declared (row 11), so at `last = γ_2-body` PendingTheta = {γ_1, γ_2}; earliest-declared = γ_1; rule writes θ_1 (row 12). After gate_1 fails and θ_1 is in M, PendingTheta = {γ_2}; rule writes θ_2 (row 14). **Sarah reproduced**; Site (i) defect resolved.
- **Nathan T7 (K=2, batched declarations then sequential firing)**: γ_1 declared (row 9), γ_2 declared (row 10), at `last = γ_2-body` PendingTheta = {γ_1, γ_2}; earliest-declared = γ_1; rule writes θ_1 (row 11). After gate_1 ∋ and ε_1 fires (row 13), PendingTheta = {γ_2} still (γ_2 declared but θ_2 not yet written; ε_1 doesn't add a θ); at `last = ε_1-body`, rule fires from non-empty PendingTheta, earliest-declared = γ_2 (the only element); writes θ_2 (row 14). **Nathan T7 reproduced**; Site (i) AND Site (ii) defects both resolved by the single set-based premise.
- **Rusty T16/T18/T20 (K=3 interleaved per §11.4.5 line 1850)**: γ_k declared, θ_k written, gate tested, ε_k or spawn, then γ_{k+1} declared only after R-perceive(γ_k) or R-perceive-failure(γ_k). PendingTheta is a singleton at each θ-firing position. Identical behavior to the prior rule.

The set-based premise admits both defect sites without breaking the cases the prior rule already reproduced.

**§13 re-check obligations (this revision touches cleared theorems; flagged here for the propagation pass that follows review of this rule).**

- **§13.5.2 (depth-weighted termination measure, inline per-cycle bound; formerly old §13.5.6's arbitrary-depth termination / firing-count bound)**: the inline bound `5·(1+J_C) + 6·K_C + J_C + 5` assumes at most one θ per γ_k and bounds θ-firings by K_C. The set-based premise preserves "at most one θ per γ_k" — the PendingTheta definition explicitly excludes γ_k once a θ_k is in M — so the per-cycle θ-firing count remains K_C. **Bound structure preserved; explicit re-derivation needed to confirm no other interaction.**
- **§13.6 (uniqueness of derivation / determinism)**: §13.6's per-step `last`-determined applicable-rule argument rests on every lifecycle rule's premise reading absolute `last(M-cycle-C)` and writing a new `last` that breaks subsequent rules' patterns. The set-based premise does NOT read `last`; it reads a derived view (PendingTheta) over the cycle-filtered M. **This changes the independence relation**: R-required-resources now admits firing from multiple states (any state where PendingTheta ≠ ∅), competing with rules whose premises do read `last`. At licensed σ-discretion states per §1.4.5 (e.g., `γ_1-body single-γ` where R-required-resources and R-intention both match; `⟨perceive-failure, C⟩` where R-required-resources, R-intention, R-moot, R-abandon all potentially match if PendingTheta is non-empty), σ at §13.6 carries the operator's choice. **§13.6's empty-independence claim needs re-verification under the set-based premise; the per-σ determinism claim should still hold but via "σ disambiguates among admissible rules at each state" rather than via "only one rule's premise matches at each state."** The re-verification is the load-bearing §13 work this revision creates.

**Migration note (prior `last`-keyed version, retracted).** The prior premise `last(M-cycle-C) = γ-body` structurally couldn't reach Sites (i) and (ii) regardless of σ — Sarah T12 row 12 and Nathan T7 rows 11 / 14 were unreachable under it. The Rule 2 reproduction-failure signal was established via the §14.3.4 Sarah 1b re-walk and §14.3 Nathan walk. The prior rule's side-condition note "The rule may fire multiple times in a single cycle when multiple `g_k` carry distinct required-resource designations" was technically true under interleaving (Rusty's K=3) but mechanically excluded the batched-declaration patterns (Sarah, Nathan). The revised rule preserves all interleaved behavior and additionally admits the batched-declaration behavior.

**Propagation discipline (flagged for the post-review sweep, NOT executed in this revision).** Per the dissolution/relocation-keyed sweep rule established 2026-06-23, the propagation needs to key on every surface form of the now-resolved defect concept — not just the literal label "Axis 1b" or "Site (i)/Site (ii)" but also "γ_2-body unreachable," "ε_1-body unreachable," "Nathan's θ_1 cannot be reached," "Sarah's θ_1 cannot be reached," "the `last`-pointer cannot represent multi-element pending-θ obligations," "Rule 2 reproduction-failure on §11.4.6's `last`-keyed premise," and similar paraphrases. Sites identified pre-sweep: §1.4.5 state-fork table (Site (i)/(ii) rows move from defect to resolved; "five defects / four fix-targets" → "four defects / three fix-targets"); §13.5.2 inline per-cycle bound paragraph (formerly old §13.5.6's bound discussion; re-derive with new premise, note the K_C ceiling holds); §13.6 determinism (re-verify independence relation under set-based premise); §14.3.2 §13.2 contingency (drop the Site (i)/(ii) contingency); §14.3.2 §13.6 trace (the corrected 3786 site moves from "defect blocking determinacy" to "resolved by §11.4.6"); §14.3.4 outcomes (Nathan's grounds-Axis-1b-Site-(i)-and-(ii) re-framed as "now resolved by §11.4.6"); §14.4 Sarah's same; §13.5.9 thin pointer (the four fix-targets list drops to three: §11.6.6, §11.4.8, §11.4.7); prep-doc Section I (close out Axis 1b with the resolution citation; the axis-to-state-fork mapping updates with "resolved" status for both sites). Concept-keyed sweep, not label-keyed.

#### §11.4.7 R-gate — gate-test passes (premise re-keyed to IntentionPosition 2026-06-23 per Thread A reframe; Axis 6 multi-q gate semantics NOT addressed here — see "Axis 6 still-open" note below)

```
   per-intention phase active in M-cycle-C                  (per §11.1)
   IntentionPosition(M-cycle-C, g_k) ∈ { θ-written, resumed q }
   q_set = q_of(M-cycle-C, g_k)                             (g_k's bound q-set from θ-declarations; relational under WF-6, |q_set| ≤ Q_max)
   ∀ q ∈ q_set: [a./R.] ∋ [Α/i./o./g_k/q]                  (conjunctive gate test passes: R ⊇ q_set)
   q_* ∈ q_set                                              (σ-picks canonical representative for the gate-pass marker; under disjoint q-sets q_* identifies g_k)
   ─────────────────────────────────────────  [R-gate-pass]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ⟨gate-pass, [Α/i./o./g_k/q_*]⟩ ; S ; R⟩
```

**Failure variant (Layer C — specific-q identification):**

```
   per-intention phase active in M-cycle-C
   IntentionPosition(M-cycle-C, g_k) ∈ { θ-written, resumed q }
   q_set = q_of(M-cycle-C, g_k)
   q_failed ∈ q_set ∧ [a./R.] ∌ [Α/i./o./g_k/q_failed]      (some q ∈ q_set is missing; σ-picks q_failed when |q_set \ R| > 1)
   ─────────────────────────────────────────  [R-gate-fail]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ⟨gate-fail, [Α/i./o./g_k/q_failed]⟩ ; S ; R⟩
```

**Premise-shape note (revision rationale).** The pre-reframe premise enumerated two positional `last`-states: (a) `last(M-cycle-C) = θ-body` (normal-path trigger) and (b) `last(M-cycle-C) = ⟨resume, C, q⟩` (post-resume trigger). Under the IntentionPosition reframe, both reduce to a single per-K read: `IntentionPosition(M-cycle-C, g_k) ∈ { θ-written, resumed q_k }`. The two pre-reframe `last`-cases are the two LifecyclePosition values the IntentionPosition fold can return when g_k has reached the gate-eligible state — the disjunction is now over IntentionPosition values, not over literal positional reads. This unifies the rule's behavior across normal-path and post-resume firings and (per Phase 1 audit §A6.1) carries the §11.6.4 correction that R-resume's `⟨resume, parent-C, q_k⟩` marker is IntentionPosition-tagged for g_k, NOT R-effected — R is unchanged at resume; the q_k gain happened earlier at R-close-nested. R-gate's R-test reads parent-R's post-close-nested state via cycle-shared S1, not via R-resume's nonexistent R-effect.

**Redex form.** The gate test `[a./R.] ∋ [Α/i./o./g_k/q.]` per §8 (∋ guard form) and §9.7.1 (∋ types as a Boolean over resource-set membership; the RHS is a path ending at a **lowercase-q** required-resource designator). The q-designation in the gate's RHS is bound by the IntentionPosition fold: g_k from `IntentionPosition(M-cycle-C, g_k)`'s scope and q_k from `q_of(M-cycle-C, g_k)`'s read of g_k's γ-declaration body. Read literally: "the actor's resource bag contains the lowercase-q required-resource that g_k's declared body binds via q_of."

**Standing-option principle (R-gate admissibility, per Thread A reframe + Axis 6 multi-q extension).** R-gate(g_k) is admissible per-g_k whenever (a) the cycle's per-intention phase is active (per §11.1), (b) `IntentionPosition(g_k) ∈ {θ-written, resumed q}`, AND (c) R ⊇ q_of(g_k) (conjunctive gate-pass) OR R ⊉ q_of(g_k) with σ-picked q_failed ∈ q_of(g_k) \ R (gate-fail with specific-q identification per Layer C). The rule is parameterized by g_k; the operator's σ chooses among admissible (R-gate, g_k) pairs at states where multiple g_k's are gate-eligible, and additionally σ-picks the closing of θ-coverage (electing R-gate over R-rr re-firing) and q_failed when multiple q's are missing. R-gate(g_a) and R-gate(g_b) for distinct g_a, g_b at compatible positions are I-independent under WF-6 with disjoint q-sets (q_of(g_a) ∩ q_of(g_b) = ∅; disjoint IntentionPosition reads, disjoint q-component R-tests, disjoint contractum markers) — per Phase 1 audit §A4.2.

**Coupling structure (per Phase 1 audit §A4).** R-gate's coupling sources:
- **R-coupling at same q_of**: R-gate(g_a) and R-gate(g_b) (or R-execute(g_b), R-spawn(g_b)) sharing q_of(g_a) ∩ q_of(g_b) ≠ ∅ read/test the same R-multiset components. **Resolved under WF-6 with disjoint q-sets**: the dissertation corpus exhibits disjoint q-sets across γ_k (Rusty's q_of(g_1)={q_1, q_2}, q_of(g_2)={q_γ2}, q_of(g_3)={q_γ3} are pairwise disjoint, source-verified at §14.5.1). Distinct-g_k pairs are R-independent under disjoint-q-sets WF-6 instances. **Contention** (shared q across γ_k) remains a deliberate general-case extension, scoped out for the corpus; opens as a Bucket-1 fork only if exhibited.
- **R-close-nested cross-cycle R-coupling**: per §A6.1, R-close-nested writes parent-R `R ⊎ E` at sub-cycle close. R-gate's R-test on parent-R sees the post-close-nested R-state. Cross-cycle coupling (R-close-nested fires in sub-cycle, writes parent-R that R-gate reads).
- **Same-g_k coupling**: R-gate(g_k) ↔ R-execute(g_k) ↔ R-perceive(g_k) ↔ R-moot-intention(g_k) all touch g_k's IntentionPosition; sequence-forced.

**Axis 6 RESOLVED 2026-06-24 (multi-q gate semantics, Layer B + Layer C).** R-gate's contractum now reads `R ⊇ q_of(g_k)` (conjunctive gate-pass) with the failure variant identifying q_failed ∈ q_of(g_k) \ R as the specific missing q. The pass-variant writes ⟨gate-pass, q_*⟩ for σ-picked q_* ∈ q_of(g_k) (canonical representative; under WF-6 with disjoint q-sets q_* identifies g_k uniquely via q_of's inverse). The fail-variant writes ⟨gate-fail, q_failed⟩, and R-spawn (§11.6.2) targets q_failed cleanly — Layer C resolved. **Layer A (multi-θ-per-g_k declaration)** resolved via §11.4.6's PendingTheta admitting `IntentionPosition(g_k) ∈ {declared, θ-written}` (standing-option re-firing of R-rr). **WF-6 (bounded q-per-intention)** added to §13.5.1 to bound PerIntentionBound. The Axis-6 resolution is corpus-verified: Rusty's source σ runs cleanly (§14.5 walk; the trace doesn't change since the source σ exercises the same firing sequence the resolved rules license); the batched σ over Rusty exercises §13.6.7's R-execute Embrace diamond under disjoint q-sets (q_of's pairwise disjoint across γ_k). **Resource contention** (q-sets share a q across γ_k) is the deliberate general-case extension, scoped out as a new-Bucket-1 fork opened only if an engagement exhibits it.

**Side conditions.** R unchanged — R-gate is a *test*, not a deduction. Resource consumption happens at R-execute. The contractum writes a `⟨gate-pass, [Α/i./o./g_k/q.]⟩` structural marker so R-execute can pattern-match on it. C, S unchanged. The gate tests **required** resources (lowercase q, #18); **obtained** resources (uppercase Q / Φ, #19) accrue at R-flowback, not here.

**Failure case.** When `[a./R.] ∌ [Α/i./o./g_k/q.]` (the actor's resources do not include the required q), R-gate does **not** fire and the lifecycle does not advance to R-execute. Control transfers to R-spawn (failure family, §11.6), which suspends the current cycle onto S and opens a sub-cycle whose objective is to acquire the missing q.

**Worked-case validation.** Charles T5, Table 5, the row immediately following θ where Charles's R holds the required q. For a row where the gate fails and R-spawn fires instead, see Rusty T19 (escalation case), reviewed in §11.6.

#### §11.4.8 R-execute — execute the intention, consume required resources (premise re-keyed to IntentionPosition 2026-06-23 per Thread A reframe; Axis 8-Sarah RESOLVED 2026-06-24 via the full g_k-scoped path discipline — see "Axis 8-Sarah resolution" note below)

```
   per-intention phase active in M-cycle-C                  (per §11.1)
   IntentionPosition(M-cycle-C, g_k) = gate-passed q_k
   q_k = q_of(M-cycle-C, g_k)
   [a.]ε(Α/i./o./g_k/e.) → { … }  is well-typed at Layer 2
   ─────────────────────────────────────────  [R-execute]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ([a.]ε(Α/i./o./g_k/e.) → { … }) ; S ; R ⊖ cost([Α/i./o./g_k/q.])⟩
```

**Premise-shape note (revision rationale).** The pre-reframe premise was `last(M-cycle-C) = ⟨gate-pass, [Α/i./o./g_k/q.]⟩` — positional. Under the IntentionPosition reframe, this becomes the per-K read `IntentionPosition(M-cycle-C, g_k) = gate-passed q_k`, which is the LifecyclePosition the `⟨gate-pass, q_k⟩` marker encodes for g_k. Functionally identical at K=1 (Charles); structurally distinct at K ≥ 2 because the positional read of `last` would fail at states where another g_b's lifecycle entry is more recent (the post-resume R-execute(γ_1) continuation case the design note §5 surfaced). The IntentionPosition filter recovers g_k's gate-pass position regardless of intervening g_b-tagged entries — this is the load-bearing post-Batch-1 unblock for Sarah T15's R-execute(γ_1) firing past the g_2 moot+resume markers.

**Redex form.** `[a.]ε(Α/i./o./g_k/e.) → { … }` per §8.5.1 (ε in operation-bearing list, Execute) and §9.4.3 (ε typing rule). The right-hand side `{ … }` is the effect's payload, typed per §9.6 — in Charles T5 line 188 the concrete body is `{ [Α/i./t./D./X./c.] + [Α/i./o./g./q.] }` (an arithmetic-form set per §9.6 family D); the rule's `{ … }` is the abstract form.

**Standing-option principle (R-execute admissibility, per Thread A reframe).** R-execute(g_k) is admissible per-g_k whenever (a) cycle's per-intention phase is active, (b) `IntentionPosition(g_k) = gate-passed q` (with q ∈ q_of(g_k) post-Axis-6), AND (c) ε-body for g_k is well-typed. The rule is parameterized by g_k; σ chooses among admissible (R-execute, g_k) pairs at states where multiple g_k's are simultaneously at gate-passed. R-execute(g_a) ↔ R-execute(g_b) for distinct g_a, g_b under WF-6 with disjoint q-sets is **I-independent**: disjoint IntentionPosition reads, disjoint ε-tagged writes, disjoint R-multiset components (multiset difference over disjoint operands commutes — `(R ⊖ cost(q_of(g_a))) ⊖ cost(q_of(g_b)) = (R ⊖ cost(q_of(g_b))) ⊖ cost(q_of(g_a))` when q_of(g_a) ∩ q_of(g_b) = ∅; the multiset-difference commutation step works at any |q_of(g_k)| ≤ Q_max).

**Coupling structure (per Phase 1 audit §A4).** R-execute's coupling sources:
- **R-coupling at overlapping q_of**: R-execute(g_a) and R-execute(g_b) sharing a q (i.e., q_of(g_a) ∩ q_of(g_b) ≠ ∅) read/consume the same R-multiset component; contention pairs are R-coupled. **Resolved under WF-6 with disjoint q-sets** (corpus-verified): the dissertation corpus exhibits pairwise-disjoint q-sets across γ_k (Charles K=1 vacuous; Jim/Nathan/Sarah |q_of|=1 with distinct paths; Rusty K=3 disjoint), so distinct-g_k R-execute pairs are R-independent. Contention is a deliberate general-case extension, scoped out.
- **F4 coupling to R-select**: R-execute(g_k)'s write of ε_k-body advances `IntentionPosition(g_k) = executed`; under Nathan pattern this is PerIntentionTerminal, but per the §A6.2 atomic-conjunction-read R-select reads `∀ live g_k: PerIntentionTerminal` as one snapshot, so R-execute(g_a) ↔ R-select couples via F4.
- **R-close-nested cross-cycle R-coupling** (per §A6.1): R-execute reads R; R-close-nested writes parent-R. Cross-cycle.
- **Same-g_k coupling**: standard.

**Side conditions.** R updated: `R' = R ⊖ cost([Α/i./o./g_k/q.])` — the **multiset-difference** of R with the lowercase-q **required** resources execution consumes (one occurrence of each designation in `cost(·)`'s return removed; a held multiplicity of two becomes one, not zero, matching §11.1's R-multiset framing and §13.4.1's conservation invariant). `cost(·)` is a deterministic structural read of the q designation declared by θ (§11.1) — the q-designation is a single resource-token per θ-declaration in the worked cases (no per-θ multiplicity), so `cost(·)`'s return is effectively a singleton (or small set of distinct designations) without internal multiplicity, and `R ⊖ cost(·)` is unambiguous: each designation in cost's return is removed once from R. It does **not** read a Σ-body, since Σ yields a position, not a resource multiset. C, S unchanged.

**Axis 8-Sarah RESOLVED 2026-06-24 (via the full g_k-scoped path discipline; the alleged ambiguity was a false alarm from address truncation).** The body-resolution side condition `R ⊖ cost([Α/i./o./g_k/q.])` reads the **full g_k-scoped designation** — not the bare `[q.]` tail. Sarah's own θ-bodies are `θ(Α/i./o./g1) := {[Α/i./o./g1/q.]}` and `θ(Α/i./o./g2) := {[Α/i./o./g2/q.]}` — two distinct **full** designations differing at the g_k segment. The "ambiguity" appears only when the address is truncated to `[q.]`, which the dissertation's nomenclature subsection explicitly forbids: "no constituents will ever share the same designation… if done properly by using the correct slash addressing and correct ordinal designation… 'A./i./P.' refers to the only preferred position in this whereas X1 refers to the first adverse alternative and X2 refers to the second." Sole-dot is a deliberate uniqueness marker meaning "the unique instance of its type within its parent scope" — `q.` under `g1` is the unique q under g1, and `q.` under `g2` is the unique q under g2. They are not the same designation. R-execute's body-resolution reads the full g_k-scoped path via `q_of(g_k)` (per §11.1's q_of derived view), which carries the full address. **Bare `[q.]` appearances in dissertation source rows are typographic abbreviation of the full address, not a semantic ambiguity.** The classification call ("error vs ambiguity") was a false dichotomy — the answer is a third option: **faithful and unambiguous when fully addressed**, as the dissertation's own designation-uniqueness guarantee specifies. The §11.4.8 body-resolution side condition is `R ⊖ cost([Α/i./o./g_k/q.])` with the full g_k segment included — exactly the rule above. **Axis 8-Sarah is no longer an open fix-target at §1.4.5**; the row is updated to "resolved 2026-06-24 (faithful-and-unique-when-fully-addressed)."

**Worked-case validation.** Charles T5, Table 5, the ε row immediately following each `⟨gate-pass, …⟩` marker. Charles's R shrinks at each R-execute step by the cost of the q declared at R-required-resources.

#### §11.4.9 R-perceive — realized perception of utility yields (premise re-keyed to IntentionPosition 2026-06-23 per Thread A reframe; Rusty per-intention variant — Nathan cycle-shared variant at R-perceive-cycle SUB-SECTION BELOW, landed 2026-06-23 post-Batch-5 to close Phase 3 gate (2); paired with R-perceive-failure at §11.6.5 per Phase 1 §A6.3 symmetry, both inheriting cardinality from §1.4.5 rows 122/123)

```
   per-intention phase active in M-cycle-C                  (per §11.1)
   CyclePattern(M-cycle-C) = per-intention                  (per §11.1 + WF-5; Gate (4) commitment — makes R-perceive admissible at per-intention cycles only)
   IntentionPosition(M-cycle-C, g_k) = executed             (Rusty pattern: per-intention)
   [Α/i./t.]Γ(Α/i./t./D./G.) = { [Α/i./t./D./P./u.] > [Α/i./t./D./X./u.] }  is well-typed at Layer 2
   the realized comparison validates the projected γ-body declared at R-intention for g_k
   ─────────────────────────────────────────  [R-perceive]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ([Α/i./t.]Γ(Α/i./t./D./G.) = { [Α/i./t./D./P./u.] > [Α/i./t./D./X./u.] }) ⊎ ⟨perceive, g_k⟩ ; S ; R⟩
```

**Premise-shape note (revision rationale).** The pre-reframe premise `last(M-cycle-C) = ε-body` was positional. Under the IntentionPosition reframe, it becomes `IntentionPosition(M-cycle-C, g_k) = executed` — the LifecyclePosition g_k's ε_k-body entry encodes. Functionally identical at K=1; structurally distinct at K ≥ 2 by the same mechanism R-execute uses (the IntentionPosition filter recovers g_k's executed position past intervening sibling-intention markers).

**Contractum addition (system-internal IntentionPosition tagging).** The contractum now appends **two** entries: (i) the Γ-body — the dissertation-faithful realized perception (Table 5 row 189), and (ii) a `⟨perceive, g_k⟩` structural marker — a system-internal addition that advances `IntentionPosition(g_k) = perceived` for the per-K read by downstream rules. The marker is an audit-trail meta-entry per §11.3's structural-marker convention (no dissertation row, similar to `⟨select-staged, σ⟩`). Without the marker, IntentionPosition(g_k) would remain at `executed` after R-perceive fires (the Γ-body is target-prefixed without g_k in its path), and the rule would be re-firable — incoherent. The two-append contractum has precedent: R-spawn (§11.6.2) writes both `⟨gate-fail, q⟩` and `⟨open, C+1⟩` in one firing.

**Redex form.** The realized Perception form `[Α/i./t.]Γ(Α/i./t./D./G.) = { comparison }` per §8.4.3 (perception-evaluation as top-level term) and §9.7.4 (outer `=` typing). The Γ is **target-prefixed** per §9.4.1 (Γ target-only; actor-prefixed Γ is rejected at Layer 2). The comparison set's members are comparison-forms over realized (unprimed) utility designations.

**Standing-option principle (R-perceive admissibility, per Thread A reframe).** R-perceive(g_k) is admissible per-g_k whenever (a) cycle's per-intention phase is active, (b) `IntentionPosition(g_k) = executed`, AND (c) the realized comparison validates the projected γ-body. The rule is parameterized by g_k; σ chooses among admissible (R-perceive, g_k) pairs at states where multiple g_k's are simultaneously at executed (multi-intention Rusty-pattern interleaving). R-perceive(g_a) ↔ R-perceive(g_b) for distinct g_a, g_b is **I-independent** (disjoint IntentionPosition reads, disjoint per-K marker writes, no R/S/C side-effects).

**Coupling structure (per Phase 1 audit §A4).** R-perceive's coupling sources:
- **F4 coupling to R-select**: R-perceive(g_k)'s contractum advances IntentionPosition(g_k) to `perceived`, which satisfies PerIntentionTerminal under Rusty pattern. R-select reads `∀ live g_k: PerIntentionTerminal` atomically per §A6.2; R-perceive(g_a) ↔ R-select couples via F4.
- **Symmetric pairing with R-perceive-failure (§11.6.5)**: per §A6.3, R-perceive and R-perceive-failure are two outcomes of the same perception event at the same lifecycle position; their cardinality mirrors (Rusty per-intention vs Nathan cycle-shared). Coupling is structural: at any state with `IntentionPosition(g_k) = executed`, exactly one of R-perceive(g_k) (validation succeeds) and R-perceive-failure(g_k) (validation fails) is admissible — they form a guard-determined Pillar-2 fork on the comparison's realized value.
- **Same-g_k coupling**: standard.

**Side conditions.** This is the *lifecycle* R-perceive (Rusty per-intention variant) — only fires when the realized comparison validates the projected γ-body. "Validates" is semantic, not a syntactic form-match: the realized utility ordering (`[Α/i./t./D./P./u.] > [Α/i./t./D./X./u.]` — preferred-utility-realized > adverse-utility-realized; the dissertation-canonical realized form across the corpus, source-verified at Charles T5, Nathan T11, Sarah/Rusty parallel Γ rows) confirms the projected comparison's *intent*, whether the projection is a direct preferred-vs-adverse ordering (Charles T5, Sarah T12 — `[.../t./D./P./u.]′ > [.../t./D./X./u.]′`) OR a cost-differential ordering (Nathan T7 — `[.../t./D./P./c2]′ > [.../t./D./P./c2]′` preferred-cost-with-support vs without-support; Rusty T16 — `[.../t./D./X./c.]′ > [.../t./D./X./c.]` adverse-cost-differential). The premise's "validates" wording is form-agnostic by design: the realized outcome confirms the projection's directional intent, which the corpus exhibits at three distinct projected-comparison shapes (direct utility, preferred-cost-differential, adverse-cost-differential) all converging on the same realized `P./u > X./u` form via the dissertation's comparison semantics. If the realized comparison fails to validate the projected one, R-perceive-failure (§11.6.5.1) fires instead per the §A6.3 symmetric pairing, which triggers R-moot, R-abandon, or R-intention (Rusty γ_3 path). Nathan pattern uses the cycle-shared R-perceive-cycle in the sub-section immediately below (landed 2026-06-23 post-Batch-5 to close Phase 3 gate (2)). C, S, R unchanged.

**Worked-case validation.** Charles T5, Table 5, the Γ row immediately following ε. The prefix `[Α/i./t.]` reflects target-attribution: the perception is the target's own perception of the matrix's goal-yield.

##### R-perceive-cycle — Nathan cycle-shared variant of R-perceive (added 2026-06-23 post-Batch-5 to close Phase 3 gate (2); symmetric pair to R-perceive-failure-cycle at §11.6.5.2)

This sub-section adds the Nathan cycle-shared validating-perceive rule, mirroring §11.6.5.2 R-perceive-failure-cycle's structure exactly (same premise shape; same simultaneity guard per §A6.2; cycle-level Γ-body; cycle-scoped marker only). R-perceive-cycle is the **validating** variant; R-perceive-failure-cycle (§11.6.5.2) is its symmetric **failing** dual. Both inherit cardinality from §1.4.5 rows 122/123 (Nathan terminal interest-level perceive).

```
   per-intention phase active in M-cycle-C                                       (per §11.1)
   CyclePattern(M-cycle-C) = cycle                                              (per §11.1 + WF-5; Gate (4) commitment — makes R-perceive-cycle admissible at cycle-pattern cycles only)
   ∀ g_k ∈ LiveIntentions(M-cycle-C): IntentionPosition(g_k) = executed          (Nathan simultaneity guard per §A6.2, identical to §11.6.5.2's premise)
   [Α/i./t.]Γ(Α/i./t./D./G.) = { cycle-level comparison }  is well-typed at Layer 2
   the realized cycle-level comparison VALIDATES the cycle's terminal perceive
   ─────────────────────────────────────────  [R-perceive-cycle (Nathan)]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; 
                          M ⊎ ([Α/i./t.]Γ(Α/i./t./D./G.) = { validating-cycle-comparison }) 
                            ⊎ ⟨perceive, C⟩                                       (cycle-scoped marker — C as second arg, NOT per-K)
                          ; S ; R⟩
```

**Critical contractum property — NO per-K marker write (the load-bearing property the user-review pre-flagged).** R-perceive-cycle writes only the cycle-shared Γ-body and the cycle-scoped `⟨perceive, C⟩` marker. **No `⟨perceive, g_k⟩` per-K marker is written for any g_k.** Under §11.1's tightened recognizer, the cycle-scoped `⟨perceive, C⟩` marker's role-spec is "C as direct second argument" — C is a cycle identifier, never any g_k (different sorts), so this marker never matches "about g_k" for any g_k. Therefore: **individual live g_k's remain at `IntentionPosition(g_k) = executed` throughout and after R-perceive-cycle fires.** This is precisely what makes R-select's executed-existential implication (§11.4.10 conjunct (iii)) fire correctly in Nathan-pattern cycles: every live g_k is at executed (conjunct (ii) satisfied — executed ∈ PerIntentionTerminal); `∃ executed` is true; the implication then requires `⟨perceive, C⟩ ∈ M-cycle-C`, and R-perceive-cycle's contractum supplies exactly that. R-select then fires, transitioning the cycle to cycle-shared close.

**Premise-shape note (mirrors §11.6.5.2 R-perceive-failure-cycle).** Identical structure to the failing dual: per-intention phase active + Nathan all-executed simultaneity guard + cycle-level Γ-form well-typed. The only difference between R-perceive-cycle and §11.6.5.2 is the validation guard — R-perceive-cycle fires on **validates**, R-perceive-failure-cycle fires on **does NOT validate**. These are a guard-determined Pillar-2 fork at the Nathan terminal-perceive position; exactly one fires per cycle-level Γ-evaluation outcome.

**Standing-option principle.** R-perceive-cycle is **structurally triggered** once all live g_k's reach `IntentionPosition = executed` simultaneously (the Nathan simultaneity guard, per §A6.2). No σ-discretion at the firing itself; the σ-fork lives upstream at the per-intention rules' (rule, g_k) σ-picks that drive the cycle into the all-executed state. The validate-or-not choice between R-perceive-cycle and R-perceive-failure-cycle is Pillar-2 guard-determined by the realized cycle-level Γ-comparison.

**Coupling structure (per Phase 1 audit §A4).**
- **F4 coupling to R-select via the cycle-shared perceive marker**: R-perceive-cycle writes `⟨perceive, C⟩`, which satisfies R-select's conjunct (iii) executed-existential implication. R-select then becomes admissible. R-perceive-cycle ↔ R-select coupled through the cycle-shared marker read.
- **Symmetric pair with R-perceive-failure-cycle (§11.6.5.2)**: at the all-executed state, exactly one of R-perceive-cycle (validating) and R-perceive-failure-cycle (failing) fires based on the realized cycle-level comparison. Pillar-2 guard-determined fork, NOT σ-discretion at the rule-pair level.
- **No per-K coupling** (load-bearing for the §13.6 confluence proof): R-perceive-cycle writes nothing g_k-tagged, so no per-K IntentionPosition is changed. Per-K rules at distinct g_k that fired earlier in the cycle (R-execute(g_a), R-execute(g_b)) remain I-independent of R-perceive-cycle's firing — the cycle-shared marker write doesn't introduce any new per-K coupling.

**Worked-case validation — source-anchored to Table 11 (Nathan-Randy Part 2; per the 2026-06-23 post-Batch-5 dissertation trace that closed Phase 3 gate (2)'s open fidelity check).** Nathan's K=2 top cycle (Intention 1 + Intention 2) resolves with a **single realized Perception at the interest level**: `[Α/i./t.]Γ(Α/i./D./G.) = { [Α/i./D./P./u.] > [Α/i./D./X./u.] }` — path carries no g_k segment, and the realized perception fires once at cycle scope after both intentions have executed, NOT one perception per intention. This is the structural form R-perceive-cycle formalizes: target-prefixed cycle-scoped Γ-body, written once at the end of the per-intention pass after all live γ_k's reach `executed` simultaneously. The validating guard (`>` in the realized comparison) is attested directly in Table 11; the failing guard (`≤`) is attested at Sarah's perceive (Sarah Table 14-15 perceive line, where Sarah's cycle terminates via R-perceive-failure rather than reaching select). **The Rusty-vs-Nathan cardinality distinction (§1.4.5 rows 122/123) is source-grounded**: Rusty perceptions carry g_k in the path (`Α/i./o./g1/i./t.`) per the per-intention pattern; Nathan's doesn't, per Table 11's cycle-scope path. **The Phase 3 gate-2 fidelity check is closed at source, not deferred.**

**Lexer-normalization reconciliation (D-26 / D-27, lines 939 and 1467).** The rule's canonical Γ-form `Γ(Α/i./t./D./G.)` carries an extra `/t.` and `/D.` compared to the dissertation's source shorthand `Γ(Α/i./D./G.)` (realized) and `Γ(Α/i./t./G.)′` (projected). This is **not a deviation** — it's the D-26 (realized) and D-27 (projected) lexer-normalization rules at §8.2.2, which insert the matrix node `D./` and the target node to canonicalize the dissertation's source shorthand. The rule operates on the post-lexer form; the dissertation's source shorthand normalizes to it. Cross-referenced here so future readers tracing Table 11 against the rule's premise don't mistake the canonicalization for a discrepancy.

**Phase 4 follow-up (member-by-member trace, not blocking)**: §14.3's per-theorem trace will exercise R-perceive-cycle and R-perceive-failure-cycle against the full set of Nathan's Γ-form member-by-member designations (which specific utility-comparison operands appear in the source, the projected-comparison structure inside the antecedent γ-bodies). That detail-level walk-through rides along in §14.3 Phase 4 propagation. The **load-bearing claim** (cycle-level vs per-intention cardinality, single terminal Γ at interest scope) **is source-anchored to Table 11 as of this revision — no longer provisional**.

**Side conditions.** This is the *lifecycle* R-perceive-cycle (Nathan cycle-shared variant) — only fires when the realized cycle-level comparison validates the cycle's terminal perceive. If validation fails, R-perceive-failure-cycle (§11.6.5.2) fires instead. The two are mutually exclusive at the all-executed state; one and only one fires. C, S, R unchanged.

**Symmetric pairing with R-perceive (Rusty variant above) and R-perceive-failure-cycle (Nathan failing variant at §11.6.5.2).** Together the four rules cover the perceive lifecycle's cardinality matrix per §1.4.5 rows 122/123:
- **Rusty validating**: §11.4.9 R-perceive (per-K, writes `⟨perceive, g_k⟩`)
- **Rusty failing**: §11.6.5.1 R-perceive-failure (per-K, writes `⟨perceive-failure, g_k⟩`)
- **Nathan validating**: §11.4.9 R-perceive-cycle (cycle-shared, writes `⟨perceive, C⟩`) — **this rule**
- **Nathan failing**: §11.6.5.2 R-perceive-failure-cycle (cycle-shared, writes `⟨perceive-failure, C⟩`)

The Pillar-2 guard-determined cardinality choice (Rusty per-intention vs Nathan cycle-shared) is made at the cycle level per §1.4.5 rows 122/123. The Pillar-2 guard-determined validate-or-not choice within a cardinality pattern is made at the firing-time level per the realized Γ-comparison. Both choices are guard-determined, not σ-discretionary.

#### §11.4.10 R-select — stage the matrix selection (premise re-keyed to atomic F4 conjunction-read 2026-06-23 per Thread A reframe; per §A6.2 atomicity FORCED by §7.5 derived-view semantics)

```
   per-intention phase active in M-cycle-C                          (per §11.1; pre-R-select — about to transition to cycle-shared close)
   ∀ g_k ∈ LiveIntentions(M-cycle-C): 
       PerIntentionTerminal(IntentionPosition(M-cycle-C, g_k))       (F4 all-of-universal — Phase 1 audit §A3)
   (∃ g_k ∈ LiveIntentions(M-cycle-C): IntentionPosition(g_k) = executed)
       →  ⟨perceive, C⟩ ∈ M-cycle-C                                  (executed-existential implication — SOUNDNESS GUARD against premature select; refined post-Batch-4-review)
   [Α/i./t.]Σ(Α/i./t./D.) → [Α/i./t./S./P.]  is a well-typed projection-clause at Layer 2
   ─────────────────────────────────────────  [R-select]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ⟨select-staged, [Α/i./t.]Σ(Α/i./t./D.) → [Α/i./t./S./P.]⟩ ; S ; R⟩
```

Where the predicate `PerIntentionTerminal` admits three terminal positions per g_k:

```
   PerIntentionTerminal(IntentionPosition(g_k))  ::=
       IntentionPosition(g_k) ∈ { perceived, executed, mooted }
                                 ^^^^^^^^^   ^^^^^^^^   ^^^^^^
                                 Rusty       Nathan     either
                                 pattern     pattern    pattern
```

**The conjunction is read atomically — one snapshot from M-cycle-C — per §A6.2, forced by §7.5.** Derived-view semantics require a fold over M-cycle-C to be computed at one read-time (a derived view IS a snapshot, not a sequence of independent reads). The four premise conjuncts — per-intention phase boundary; the F4 universal over LiveIntentions; the executed-existential implication; the σ-clause well-typedness — are evaluated together against a single M-cycle-C state. Sequential reading (each conjunct independently at its own time) would let R-select fire on a snapshot where one conjunct held a moment ago but not now — incoherent under §7.5. **This is not a design recommendation; it is determined by §7.5's derived-view semantics.**

**Conjunct (iii) refinement (post-Batch-4 review — required fix).** The first-draft conjunct (iii) was `(Nathan-pattern → ⟨perceive, C⟩ ∈ M-cycle-C)` with the gloss "vacuous if Rusty." This was **wrong on two counts and exactly the kind of hazard the atomicity claim is meant to forbid**: (1) "Nathan-pattern" is an informal pattern-label, NOT a fold over M-cycle-C, so the atomicity claim doesn't actually hold for that conjunct — every conjunct in an atomic-conjunction-read MUST be a derived-view fold over M-cycle-C; (2) the gloss was incorrect about when the conjunct is vacuous (vacuous-when-Rusty vs vacuous-when-no-live-intention-is-at-executed are different conditions). The corrected formalization, an existential-implication that IS a fold over M-cycle-C: **if any live g_k sits at `IntentionPosition(g_k) = executed`, then `⟨perceive, C⟩` must be present in M-cycle-C**. This is THE soundness guard against premature select.

**Soundness trace across worked cases:**
- **Charles K=1, R-perceive fires, IntentionPosition(g_1) = perceived**: ∃ executed = false → implication vacuous → conjunct (ii) satisfied (perceived ∈ PerIntentionTerminal) → R-select fires ✓
- **Rusty K=3 mid-perceive (g_1 perceived, g_2 still at `executed`)**: conjunct (ii) holds (executed is in PerIntentionTerminal), but `∃ executed = true` → implication requires `⟨perceive, C⟩ ∈ M-cycle-C`. **A Rusty-pattern cycle never writes `⟨perceive, C⟩`** (it writes per-K `⟨perceive, g_k⟩` markers). The implication FAILS → R-select BLOCKS until g_2's R-perceive fires and advances IntentionPosition(g_2) = perceived. **This is the soundness guard firing exactly when it should** — premature R-select is prevented while a live intention has executed-but-not-perceived. The first-draft "vacuous if Rusty" gloss got this exactly backwards: the implication is NOT vacuous in mid-Rusty-perceive states; it is the load-bearing block.
- **Nathan, all live g_k's at `executed` simultaneously (Nathan simultaneity guard)**: `∃ executed = true` → requires `⟨perceive, C⟩`. R-perceive-cycle (the Nathan-pattern cycle-shared perceive rule) fires from this state, writing `⟨perceive, C⟩`; then R-select's conjunct (iii) is satisfied → R-select fires ✓
- **Sarah K=2 post-T15 (g_1 perceived, g_2 mooted)**: `∃ executed = false` (g_1 is perceived, g_2 is mooted, neither at executed) → implication vacuous → conjunct (ii) satisfied (both terminals) → R-select fires ✓

**Correct gloss**: vacuous when every live intention is `perceived` or `mooted`; **blocks R-select while any live intention sits at `executed` without a cycle-perceive present**. The implication is what tightens the otherwise-too-loose `executed ∈ PerIntentionTerminal` admission in conjunct (ii): conjunct (ii) admits executed as terminal because Nathan-pattern needs it to be; conjunct (iii) then requires that admission to be backed by the cycle-shared perceive marker, preventing the Rusty-pattern abuse (where executed alone is NOT a terminal state — the cycle still needs per-K R-perceive).

**Premise-shape note (revision rationale — the K_C-aware shape).** The pre-reframe premise was `last(M-cycle-C) = Γ-body validating γ's projected comparison` — positional, K=1-shaped. At K=1 (Charles) the cycle has one γ, R-perceive fires once writing the validating Γ, and R-select reads literal-`last` as that Γ. **At K ≥ 2 this is structurally broken**: multiple Γ-bodies are written (one per g_k under Rusty pattern; or zero per-K under Nathan with one cycle-shared Γ); positional `last` cannot encode "the cycle is done with all its per-intention passes." The reframe replaces the positional read with the F4 universal over LiveIntentions, which is the correct K_C-aware shape: R-select fires when every live g_k has reached its per-intention terminal (perceived, executed, or mooted). Per §6 of the design (perceive-cardinality consistency with §1.4.5 rows 122/123), both Rusty and Nathan patterns are admitted via the three-value PerIntentionTerminal predicate without forcing a cardinality choice.

**Standing-option principle (R-select admissibility).** R-select is **structurally triggered** (no σ-discretion): when all four premise conjuncts hold simultaneously, R-select is the only admissible rule from that state, transitioning the cycle from per-intention phase to cycle-shared close. **The σ-fork lives upstream** at the per-intention rules (which g_k advances next, whether to fire R-moot-intention vs proceed, etc.) — σ's choices upstream determine WHEN all live g_k's reach PerIntentionTerminal simultaneously; R-select's firing is the deterministic consequence.

**Coupling structure (per Phase 1 audit §A4; R-select is THE handoff hinge — user-flagged hardest-review item).**
- **F4 all-of-universal coupling** (the structurally most-coupled rule in the per-intention layer): R-select ↔ {R-execute(g_b), R-perceive(g_b), R-moot-intention(g_b), R-intention(g_b)} for every g_b. Each per-intention advancing rule's write changes `IntentionPosition(g_b)`, which changes the F4 universal's value. R-intention(g_b) firing LATE breaks the universal by adding a non-terminal live g_b — R-select must wait. R-execute(g_b) / R-perceive(g_b) / R-moot-intention(g_b) firing satisfies the universal for g_b.
- **Atomic-conjunction-read coupling**: R-select couples to R-perceive-cycle (Nathan variant — when it fires, writes ⟨perceive, C⟩ which satisfies the Nathan-pattern conditional). The atomic snapshot means R-select reads ⟨perceive, C⟩'s presence as part of the same fold as F4 — they're not sequential.
- **Cycle-shared handoff coupling**: R-select ↔ R-outcome (R-outcome's premise reads `last = ⟨select-staged, σ⟩` which R-select writes; sequential).
- **No same-K coupling at the per-intention layer**: R-select is cycle-shared; it doesn't touch any g_k's IntentionPosition. After R-select fires, `⟨select-staged, σ⟩ ∈ M-cycle-C` → per-intention phase becomes inactive per §11.1 boundary → R-intention / R-rr / R-gate / R-execute / R-perceive / R-moot-intention all become inadmissible. The handoff is unidirectional.

**Cycle-shared transition.** R-select's contractum writes `⟨select-staged, σ⟩` which is THE handoff marker: the §11.1 per-intention phase boundary excludes M-cycle-C states containing this marker, so R-select's firing transitions the cycle from per-intention phase (steps 4–9) to cycle-shared close (steps 10–14). Downstream cycle-shared rules (R-outcome → R-obtained-utility → R-close → R-flowback) read literal-`last` over cycle-scope entries per the §11.1 convention. **This is the §11.3 step-9/10 boundary the design note §2 specified — instantiated here as the actual rule that fires it.**

**Redex form.** `[Α/i./t.]Σ(Α/i./t./D.) → [Α/i./t./S./P.]` per §8.5.1 (Σ in operation-bearing list, Selection) and §9.4 prefix-admissibility (Σ **target-prefixed only** per §9.4.1; actor-prefixed Σ is rejected at Layer 2). The clause is a **projection-clause**, which §8.9 explicitly excludes from top-level term position — projection-clauses appear only inside `⟨set⟩` or as the body of an `⟨equivalence-form⟩`, never standalone.

**Side conditions.** Because the Σ → P projection-clause **cannot stand at top-level in M**, R-select does *not* write it as a top-level M-entry. It writes the structural marker `⟨select-staged, σ⟩` where σ is the staged projection-clause held as marker data (markers are audit-trail meta-entries, not LSPI top-level terms, and are not subject to the §8.9 top-level restriction). R-outcome reads this marker to construct the Ω-body, where σ is placed legally inside an equivalence body's set. C, S, R unchanged.

**Worked-case validation.** Charles T5, Table 5, the selection moment immediately following Γ. In the dissertation presentation the selection appears as part of the Outcome structure; the staging step captures the moment the selection is decided, before R-outcome folds it into Ω.

**Phase 3 prerequisites (forward note — split status: three items LANDED + Gate (4) ADDED post-catalog-reconciliation surfaced a real perceive σ-fork; §13.5 authorized to proceed, §13.6 HELD on Gate (4)).** R-select's conjunct (iii) reads `⟨perceive, C⟩` (the cycle-shared perceive marker). Under the corrected formalization above, this marker requires a producer: R-perceive-cycle (the Nathan-pattern cycle-shared perceive rule). **Four items gate §13.5 / §13.6 (Phase 3); the first three have landed, the fourth is new:**

1. **R-select conjunct (iii) executed-existential formalization** — **LANDED** (post-Batch-4 review; the soundness guard is now a genuine derived-view fold over M-cycle-C, atomicity holds for all four conjuncts).
2. **R-perceive-cycle written so `⟨perceive, C⟩` has a producer** — **LANDED** (post-Batch-5; new R-perceive sub-section at §11.4.9 — the Nathan validating cycle-perceive variant. With it, §13.5's progress proof can show R-select reachable in Nathan-pattern cycles; conjunct (iii)'s `⟨perceive, C⟩ ∈ M-cycle-C` is satisfied by R-perceive-cycle's contractum. The dissertation-row fidelity check for the specific Nathan T7–T11 Γ-form is queued for §14.3 Phase 4 walk-through validation; structural shape mirrors R-perceive-failure-cycle (§11.6.5.2, landed Batch 4).
3. **§11.1 IntentionPosition recognizer tightened to "most-recent position-bearing entry about g_k" + R-objective-revise preservation rewritten on shape-grounds** — **LANDED** (this revision; the user-flagged hardest-trace of R-objective-revise's preservation surfaced that the first-draft "no g_k in path" argument was factually contradicted by Sarah Table 14's sub-cycle ι-revision, which carries `g2` in both path and body as provenance. The right fix is to make IntentionPosition's fold shape-sensitive: only the nine position-bearing shapes encode a LifecyclePosition value, and cycle-prologue ι/ω/δ bodies and structural cycle-scoped markers are explicitly excluded even when their path carries g_k provenance via the sub-cycle parent-prefix discipline. This uniformly fixes R-interest, R-detect, R-objective, R-objective-revise, R-open, R-close, R-flowback, R-outcome, R-obtained-utility, R-moot, R-abandon, R-perceive-failure-cycle, and R-select — every rule whose contractum entries carry g_k path provenance via the sub-cycle prefix discipline but don't encode a LifecyclePosition. §13.6 re-derives the independence relation by folding over IntentionPosition; without the tightening, the fold would be ill-defined on any state where a non-position-bearing g_k-path-bearing entry is the most-recent in M-cycle-C, and the confluence argument would have no ground to stand on.)
4. **Perceive-pattern mechanical commitment** (Gate (4)) — **LANDED 2026-06-24 as one combined cut with Axis 8-Sarah.** The dissertation trace (Table 11 Nathan + Table 6 Jim + Table 12 Sarah + Table 16 Rusty + Table 5 Charles) confirmed the discriminator: γ-comparison-body's matrix-position references (P_n / X_n ordinal indices → per-intention; sole-dot P. / X. → cycle). The δ-body's over-listing (Charles and Jim list X1/X2 in δ but their γ-comparisons use sole-dot X.) made γ-comparisons the principled locus, not δ. The dissertation's nomenclature subsection settled sole-dot semantics as **faithful and unambiguous** ("the dot denotes the only element of its type… no constituents will ever share the same designation"), which collapsed both Gate (4) AND Axis 8-Sarah into one cut: **Gate (4) closes** via a derived view `CyclePattern(M-cycle-C)` (peer of `q_of`, added at §11.1) folded over the γ-comparison bodies of every γ_k in `DeclaredIntentions` (the fold reads declared γ_k, not live γ_k — see §11.1 Stability paragraph for why this matters for the "set-once" claim under R-moot-intention), plus WF-5 conformance (all declared γ_k agree on pattern, rides on R-intention's existing Layer-2 well-typedness premise — see §13.5.2). Each perceive rule gains one premise conjunct: R-perceive (§11.4.9) and R-perceive-failure (§11.6.5.1) gate on `CyclePattern = per-intention`; R-perceive-cycle (§11.4.9 sub-section) and R-perceive-failure-cycle (§11.6.5.2) gate on `CyclePattern = cycle`. From any all-executed state, exactly one CyclePattern value holds → exactly one perceive family admissible. **The non-confluent σ-fork doesn't get commuted in §13.6 — it's inadmissible by premise**, so it disappears. **Axis 8-Sarah closes** at §11.4.8 via the full g_k-scoped path discipline (`R ⊖ cost([Α/i./o./g_k/q.])`) — the alleged ambiguity was a false alarm from address truncation. **Zero new markers, zero new folds, zero new couplings.** CyclePattern is set at the first R-intention firing and WF-5-locked thereafter; it is a stable derived view, **NOT** an F6 (the coupling-surface category does not apply because there is one writer and the value never evolves). §13.6's confluence proof reads CyclePattern as a constant, not a write-coupled value. See Phase 1 audit §A3 non-coupling note for the explicit classification.

**Phase 3 gate is now CLEAR — all four gates landed.** §13.6 opens on a perceive layer deterministic by construction, with the F5 dual-polarity still first on the confluence checklist.

#### §11.4.11 R-outcome — fold the staged selection into the Outcome equivalence (cycle-shared close; literal-`last` read confirmed correct per §11.1 cycle-shared close convention 2026-06-23 per Thread A reframe — no IntentionPosition substrate change)

```
   last(M-cycle-C) = ⟨select-staged, σ⟩    where σ = [Α/i./t.]Σ(Α/i./t./D.) → [Α/i./t./S./P.]
   Ω(Α/i./O.) ≡ { σ }  is well-typed at Layer 2
   ─────────────────────────────────────────  [R-outcome]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ (Ω(Α/i./O.) ≡ { σ }) ; S ; R⟩
```

**Redex form.** `Ω(Α/i./O.) ≡ { σ }` per §8.5.1 (Ω in operation-bearing list, **#8 Outcome**) and §9.4.1 (Ω is **systemic-only** — **no actor prefix, no target prefix**). The Ω body holds the realized projection-clause σ (the staged Σ → P from the previous step), now legally placed inside an equivalence-form's set per §8.9.

**Side conditions.** Ω has **no prefix** per §9.4.1 — it is a systemic operation, attributed to the cycle as a whole rather than to any actor or target. C, S, R unchanged. Exactly one Ω per cycle. The realized Σ → P clause inside Ω's body is the **unprimed** mirror of the **primed** Σ → P clause inside ω's body at R-objective.

**Worked-case validation.** Charles T5, Table 5, the Ω row at the position immediately following the staged selection. The realized Σ → P inside Ω matches Charles's ω-projection from earlier in the cycle (modulo the prime), confirming the cycle delivered the planned outcome.

#### §11.4.12 R-obtained-utility — declare the target's obtained utility (cycle-shared close; literal-`last` read confirmed correct per §11.1 cycle-shared close convention 2026-06-23 per Thread A reframe — no IntentionPosition substrate change)

```
   last(M-cycle-C) = Ω-body
   [Α/i./t.]Λ(Α/i./O./U.) := { [Α/i./t./D./P./u.] }  is well-typed at Layer 2
   ─────────────────────────────────────────  [R-obtained-utility]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ([Α/i./t.]Λ(Α/i./O./U.) := { [Α/i./t./D./P./u.] }) ; S ; R⟩
```

**Redex form.** `[Α/i./t.]Λ(Α/i./O./U.) := { [Α/i./t./D./P./u.] }` per §8.5.1 (Λ in operation-bearing list, **Obtained Utility**) and §9.4.1 (Λ is **target-only** — actor-prefixed Λ is rejected at Layer 2). Λ's argument terminates at sort `obtained-utility` (path `Α/i./O./U.` — actor's interest's outcome's obtained-U), paralleling Φ's `Α/i./O./Q.` (obtained-Q under outcome): argument terminates at the sort marker, declared data lives in the body. The body holds the realized utility designation the target gained — typically `[Α/i./t./D./P./u.]` (the preferred-position's utility, when the cycle delivered the preferred outcome). Λ is the post-D-21 retokenization of the dissertation's target-prefixed `Θ` form per §8.5.2: pre-lexer `[Α/i./t.]Θ(Α/i./O./U.) := { [Α/i./t./D./P./u.] }` → post-lexer `[Α/i./t.]Λ(...) := {...}`.

**Side conditions.** C unchanged; S, R unchanged. Λ is **target-prefixed** (the target — not the actor — records its utility gain), **target-only** per §9.4.1. Λ is the **target-side complement to Φ** (actor-side): the two together record the **bilateral** gain from the cycle — the target's utility (Λ), then the actor's resources (Φ at R-flowback). R is *not* updated here; utility is not a resource the actor's R-set tracks. Λ fires immediately after Ω because the target's utility gain is part of the cycle's substantive audit trail; R-close (the structural seal) fires next, after both Ω and Λ are written.

**Worked-case validation.** Charles T5, Table 5, row 191 (Obtained utility): the CFO (target) gained the utility of protecting his own political credibility, declared as `[Α/i./t./D./P./u.]` — the realized utility of the preferred position (Harry's removal). The row immediately follows Ω (row 190) and precedes the Φ declaration (row 192). The lifecycle's R-close marker (structural, no dissertation row) fires between Λ and Φ in M, sealing the substantive audit trail before R-flowback applies the R-set update.

#### §11.4.13 R-close — close the cycle (cycle-shared close; literal-`last` read confirmed correct per §11.1 cycle-shared close convention 2026-06-23 per Thread A reframe — no IntentionPosition substrate change)

```
   last(M-cycle-C) = Λ-body
   ─────────────────────────────────────────  [R-close]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ⟨close, C⟩ ; S ; R⟩
```

**Redex form.** No surface-syntax redex — R-close is structurally triggered (the Obtained Utility declaration has just been written, completing the cycle's substantive declarations). The rule writes the structural marker `⟨close, C⟩` to M, sealing the cycle for everything except R-flowback.

**Side conditions.** C unchanged (R-open advances; R-close just seals). S, R unchanged. R-close enables R-flowback; R-flowback enables R-open at index C+1 via the `⟨flowback-recorded, E⟩` marker.

**Worked-case validation.** Charles T5, Table 5, no dissertation row — R-close is a system-internal artifact for audit-trail discipline (the dissertation doesn't record structural meta-data; the close is implicit between substantive rows). In M, the close marker fires between row 191's Λ-body and row 192's Φ-body.

#### §11.4.14 R-flowback — emit Φ and flow obtained resources into R (cycle-shared close; literal-`last` read confirmed correct per §11.1 cycle-shared close convention 2026-06-23 per Thread A reframe — no IntentionPosition substrate change; top-level R-flowback writes parent-R `R ⊎ E` analogous to §11.6.3 R-close-nested's escalation R-write but at cycle-top scope)

```
   last(M-cycle-C) = ⟨close, C⟩
   earnings(cycle C) = E
   ─────────────────────────────────────────  [R-flowback]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ([a.]Φ(Α/i./O./Q.) := E) ⊎ ⟨flowback-recorded, E⟩ ; S ; R ⊎ E⟩
```

**Redex form.** Two contractum entries are appended in one step:

1. **The operation declaration** `[a.]Φ(Α/i./O./Q.) := E` per §8.5.1 (Φ in operation-bearing list, **#19 Obtained Resources**) and §9.4.1. Φ's argument terminates at sort `obtained-resources` (path `Α/i./O./Q.` — actor's interest's outcome's obtained-Q), with the obtained-resource designation set E in the body. **The argument-in-body pairing parallels Λ (Obtained Utility)** — both obtained-side operations write the result at the deeper node: `/O./Q.` for Φ, `/O./U.` for Λ, with the obtained designations in the body. **The ι/θ parallel does not extend** to Φ/Λ: ι's argument is `Α/i.` (the interest sort, with no result-node included) and θ's argument is `Α/i./o./g_k` (the intention sort, with no result-node included), but Φ's and Λ's arguments *include* the result-sort marker (`/O./Q.` and `/O./U.` respectively). The obtained-side operations sit one path-node deeper than the actor-side operations; this is the dissertation's convention, demonstrated at nested-cycle scale in Table 17 line 429: `[Α/i./o./g1/i./t.]Θ(Α/i./o./g1/i./O./U.) := { [Α/i./o./g1/i./t./D./P./u.] }` — Λ terminating at the nested cycle's `/O./U.`, exactly the same depth-pattern Φ uses at top level. Φ's specific form here is the post-D-21 retokenization of Charles T5 line 192: pre-lexer `[a.]Θ(Α/i./O./Q.) := { [Α/i./Q.] }` → post-lexer `[a.]Φ(Α/i./O./Q.) := { [Α/i./Q.] }`.
2. **The structural marker** `⟨flowback-recorded, E⟩`, which records the phase-transition event so R-open at C+1 can pattern-match on the completion of flowback. The marker is kept distinct from the Φ declaration to separate operation-as-substance (what was obtained) from phase-as-event (when the flowback happened).

**Side conditions.** `earnings(·)` returns the obtained-resource designation set E the cycle's outcome records (§11.1) — the obtained-Q designations Table 5 attests to for cycle C in the worked case (Charles T5: row 192 declares `{ [Α/i./Q.] }`), or the analyst's recorded observation in a live engagement. The reading is **declared-direct**: Table 5's flowback row writes the obtained-Q designation explicitly, so `earnings(·)` is a structural read of the dissertation-attested data, paralleling `cost(·)` reading θ's declared q. C unchanged. S unchanged. R grows by E. The Φ-declaration and the marker are appended in order (Φ first, then the marker), so the audit trail reads "Φ obtained these resources, then the flowback event was recorded." R-open at C+1 keys off the marker, not the Φ declaration. **Normal-path ι↔Φ property** (per §11.1): on the normal path, Φ's body equals ι's declared `[Α/i./Q.]` — the cycle delivered the wanted resource (Charles T5: row 179 declares `{ [Α/i./Q.] }`, row 192 obtains the same `{ [Α/i./Q.] }`). R-flowback does **not** construct Φ's body from ι; it reads what was *actually* obtained. The failure family (§11.6) breaks this identity by design — mooted/abandoned cycles obtain nothing, and escalation cycles may obtain a different resource than the parent's ι declared. The identity is a theorem of the normal path, not a precondition of the rule.

**Worked-case validation.** Charles T5, Table 5, row 192 (Obtained resource): `[a.]Θ(Α/i./O./Q.) := { [Α/i./Q.] }` (post-D-21 → Φ). Charles's Φ-body declares the obtained Q designation he earned from cycle C; R grows by that designation; the cumulative R supports gate-passes in later cycles. The Φ row matches the cycle's ι row (179) in its declared `[Α/i./Q.]` — the normal-path ι↔Φ identity is observable in the dissertation.

### §11.5 End-to-end trace through Charles T5 (validated row-by-row against Table 5)

To validate that the fourteen lifecycle rules compose into a complete normal-path cycle, the following trace walks Charles T5's first full cycle from initial state through flowback. Each row shows the rule that fired, the resulting cycle index, the entry appended to M, the state of S, and the change to R. **Path-form convention:** the trace prints paths in **dissertation surface form** (`Α/i.` sole-dot) to match Charles T5's row text directly; the post-lexer canonical form (per D-28, §8.2.2) is `Α/i1` — readers may render the trace in either form, with the surface form chosen here for one-to-one comparison against the dissertation rows. The trace presents the rules in the corrected sequence — ι at step 2 (interest declaration, Table 5 row 179); δ at step 3 with the four-member body Table 5 row 180 attests; ω at step 4 (row 184); γ at step 5 (row 185); θ at step 6 introducing the lowercase-q required-resource (row 186); Ω at step 11 wrapping the realized Σ projection-clause (row 190); **Λ at step 12** declaring the target's obtained utility (row 191); **Φ at step 14** declaring the actor's obtained resources (row 192) with the body matching ι's row-179 declaration (the normal-path ι↔Φ identity). The trace has been validated row-by-row against dissertation Table 5; modulo the three structural rules (R-open, R-select, R-close) without dissertation rows, the eleven substantive rules align with eleven Table 5 rows in fixed order.

| Step |      Rule fired      | C after |                                   M's new entry (this step)                                    |    S    |          R change         |
|------|----------------------|---------|------------------------------------------------------------------------------------------------|---------|---------------------------|
|    0 | (initial)            |       0 | (empty M)                                                                                      | (empty) | R = initial endowment     |
|    1 | R-open               |       1 | `⟨open, 1⟩`                                                                                    | (empty) | unchanged                 |
|    2 | R-interest           |       1 | `[a.]ι(Α/i.) := { [Α/i./Q.] }`                                                                       | (empty) | unchanged                 |
|    3 | R-detect             |       1 | `[a.]δ(Α/i./d.) := { [Α/i./t.], [Α/i./t./D./P.], [Α/i./t./D./X1], [Α/i./t./D./X2] }`                            | (empty) | unchanged                 |
|    4 | R-objective          |       1 | `[a.]ω(Α/i./o.) ≡ { [Α/i./t.]Σ(Α/i./t./D.)′ → [Α/i./t./S./P.]′ }`                              | (empty) | unchanged                 |
|    5 | R-intention          |       1 | `[a.]γ(Α/i./o./g.) ≡ { [Α/i./t.]Γ(Α/i./t./D./G.)′ = { [Α/i./t./D./P./u.]′ > [Α/i./t./D./X./u.]′ } }`   | (empty) | unchanged                 |
|    6 | R-required-resources |       1 | `[a.]θ(Α/i./o./g.) := { [Α/i./o./g./q.] }`                                                     | (empty) | unchanged                 |
|    7 | R-gate               |       1 | `⟨gate-pass, [Α/i./o./g./q.]⟩`                                                                 | (empty) | unchanged (R ∋ q)         |
|    8 | R-execute            |       1 | `[a.]ε(Α/i./o./g./e.) → { … }`                                                                  | (empty) | R ⊖ cost([Α/i./o./g./q.])  |
|    9 | R-perceive           |       1 | `[Α/i./t.]Γ(Α/i./t./D./G.) = { [Α/i./t./D./P./u.] > [Α/i./t./D./X./u.] }`                      | (empty) | unchanged                 |
|   10 | R-select             |       1 | `⟨select-staged, [Α/i./t.]Σ(Α/i./t./D.) → [Α/i./t./S./P.]⟩`                                    | (empty) | unchanged                 |
|   11 | R-outcome            |       1 | `Ω(Α/i./O.) ≡ { [Α/i./t.]Σ(Α/i./t./D.) → [Α/i./t./S./P.] }`                                    | (empty) | unchanged                 |
|   12 | R-obtained-utility   |       1 | `[Α/i./t.]Λ(Α/i./O./U.) := { [Α/i./t./D./P./u.] }`                                              | (empty) | unchanged                 |
|   13 | R-close              |       1 | `⟨close, 1⟩`                                                                                   | (empty) | unchanged                 |
|   14 | R-flowback           |       1 | `[a.]Φ(Α/i./O./Q.) := { [Α/i./Q.] }`  +  `⟨flowback-recorded, { [Α/i./Q.] }⟩`                   | (empty) | R ⊎ { [Α/i./Q.] }         |

At step 14's end, M contains **fifteen** cycle-1 entries (thirteen rules write one entry each at steps 1–13; R-flowback writes two at step 14 — the Φ declaration and the flowback-recorded marker); S is empty (no failures, no suspensions); R has been depleted by `cost([Α/i./o./g./q.])` at step 8 and replenished by `E_1 = earnings(cycle 1) = { [Α/i./Q.] }` at step 14, where `earnings(·)` reads Table 5 row 192's declared-direct obtained-Q (the canonical reading per §11.1, settled by the row-by-row pass). R-flowback writes E_1 into Φ's body and into the marker simultaneously. The configuration is now in the state R-open requires to fire again at C=2 (the trigger keys off the `⟨flowback-recorded, _⟩` marker).

Three properties to call out:

1. **Audit-trail completeness.** Every phase transition writes a distinct, named entry to M. A reviewer can reconstruct the cycle's lifecycle entirely from M without external state — including the staged Σ projection-clause, which is preserved as marker data because §8.9 forbids it at top-level.
2. **Persistence-invariant preservation.** No step rewrites or removes a prior entry. Each rule's M' is `M ⊎ (something new)`, never `M with some entry replaced`. The R-select marker preserves the projection-clause without violating §8.9's top-level restriction; R-outcome then folds it legally inside Ω's equivalence body.
3. **Prefix-discipline observance.** The actor-prefixed operations (ι, δ, ω, γ, θ, ε) carry `[a.]`; the target-only operations (Γ, Σ) carry `[Α/i./t.]`; the systemic operation (Ω) carries no prefix at all. The trace honors §9.4.1's prefix-admissibility table at every step.

The same fourteen-step pattern repeats for cycle 2 onward, with C advancing at R-open and the M-entries of prior cycles preserved in place. The dissertation's full Charles T5 table is the multi-cycle iteration of this pattern, modulo cycles where the failure family (§11.6) or non-destructive rules (§11.7) also fire — the failure-family interruptions (R-spawn, R-close-nested, R-resume, R-perceive-failure, R-moot, R-abandon) are documented in §11.6 with validation against Rusty Tables 16–19; the non-destructive three remain a §11.7 stub pending the third review batch.

### §11.6 Failure family

The failure family handles deviations from the normal-path lifecycle. Three rules form the **escalation core** (gate-fail spawning sub-cycles and resuming after their completion): **R-spawn**, **R-close-nested**, **R-resume**. Three rules form the **abort core** (cycles that cannot complete and must be wound down): **R-perceive-failure**, **R-moot**, **R-abandon**. All six maintain the persistence invariant (§7.5) — every contractum is M ⊎ new, no rewrites — and all six obey the prefix-admissibility table of §9.4.1.

The escalation core is the load-bearing part. The dissertation case is Rusty Tables 16–19: Rusty's parent cycle with Todd hits a gate failure at `[a./R.] ∌ [Α/i./o./g1/q.]` (Table 16 line 407, Rusty lacks the authority his Intention 1 requires), which spawns a sub-cycle with Erik whose path is **nested inside the parent's path** (Table 17 line 422: `[a.]ω(Α/i./o./g1/i./o.) ≡ { … }` — observe the `/g1/i./` segment, where the parent's required-resource node `g1` is now followed by the sub-cycle's interest node `i.`). The S-stack carries this nesting structurally: each push records the parent's pending q-designation and the parent's cycle counter, and the sub-cycle's path inherits the parent's path-prefix up to the gated `g_k`.

#### §11.6.1 The S-stack — discipline and entry structure

Part I §4.2 defined the configuration's S-slot as a stack. This section makes the stack's discipline explicit for the failure-family rules that touch it.

**Entry structure.** Each S-entry is a tuple `⟨parent-C, parent-pending-q, parent-prefix⟩`:

- **`parent-C`** — the parent cycle's identifier, so R-resume can restore C when the sub-cycle completes.
- **`parent-pending-q`** — the required-resource designation the parent's gate was testing when it failed (e.g., `[Α/i./o./g1/q.]` in Rusty T16). R-resume's premise checks that the parent's pending q is now in R before popping.
- **`parent-prefix`** — the **path-prefix the spawned sub-cycle uses** for its own operation paths (e.g., `Α/i./o./g1/` for Rusty's Table 17 sub-cycle). The sub-cycle prepends this prefix to its own operations (Table 17 line 422 shows the sub-cycle's ω as `ω(Α/i./o./g1/i./o.)` — the `Α/i./o./g1/` prefix followed by the sub-cycle's own `i./o.` interest-and-outcome path). The S-entry's `parent-prefix` is constructed by R-spawn as `base-prefix/o./g_k/` where `base-prefix` is the *parent's* own interest-prefix (`Α/i.` at top level) and `g_k` is the parent's gated intention. So `parent-prefix` describes the parent's *suspended position* in the address tree, not the parent's own prefix.

**Discipline.** R-spawn pushes; R-resume pops. R-close-nested does not modify S (it operates on the sub-cycle's M and R, leaving S for R-resume). The stack grows on each escalation level and contracts on each resumption, so a chain of N escalations (Rusty T19 documents at least one such re-escalation against Erik) produces S-depths that rise and fall as the chain progresses.

**Composition guarantee.** The same fourteen-rule lifecycle (§11.4) runs at every level of the stack. A sub-cycle is just a cycle whose configuration happens to have S non-empty; it runs R-interest through R-flowback the same way a top-level cycle does. The only differences are: (i) the sub-cycle's path is prefixed by `parent-prefix`, (ii) R-close fires only when S is empty (top-level close), so sub-cycles use **R-close-nested** instead, and (iii) R-open at C+1 fires only when S is empty (so a fresh top-level cycle), while R-resume fires when S is non-empty (so a suspended parent's resumption). These three differences are what the failure family encodes.

#### §11.6.2 R-spawn — gate fails, spawn sub-cycle, push parent (premise re-keyed to IntentionPosition 2026-06-23 per Thread A reframe; **parent-R unchanged — confirmed per §A6.1**)

```
   per-intention phase active in M-cycle-C                                   (per §11.1; "C" = parent cycle here)
   IntentionPosition(M-cycle-C, g_k) ∈ { θ-written, resumed q_k }            (g_k is gate-eligible)
   q_k = q_of(M-cycle-C, g_k)
   [a./R.] ∌ [base-prefix/o./g_k/q.]                                         (R-test fails — gate cannot pass)
   ─────────────────────────────────────────  [R-spawn]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C+1 ; 
                              M ⊎ ⟨gate-fail, [base-prefix/o./g_k/q.]⟩ 
                                ⊎ ⟨open, C+1⟩ 
                          ; ⟨C, [base-prefix/o./g_k/q.], base-prefix/o./g_k/⟩ :: S 
                          ; R⟩
```

**Premise-shape note (revision rationale).** The pre-reframe premise was containment-keyed: `M-cycle-C contains θ-body for g_k` ∧ `R ∌ q`. Under IntentionPosition, the containment read becomes the per-K gate-eligibility read `IntentionPosition(M-cycle-C, g_k) ∈ { θ-written, resumed q_k }` — **identical to R-gate's gate-eligibility position**. R-spawn and R-gate are now **dual rules at the gate-eligibility position**: same IntentionPosition premise, inverted R-test (R-gate fires on `R ∋ q_k`; R-spawn fires on `R ∌ q_k`). This is a **guard-determined Pillar-2 fork** based on R's contents, NOT σ-discretion — at any given gate-eligible state, exactly one of the two fires. (Distinct from R-spawn(g_a) vs R-spawn(g_b) at different g_k's both gate-failed, which IS σ-discretion via the (R-spawn, g_k) σ-pick per design §5.6 — Axis 3b second-half's order question.)

**Parent-R UNCHANGED — confirmed per §A6.1 watch-point.** R-spawn's contractum touches three slots and leaves R untouched:
- **M (parent-tagged)**: `⟨gate-fail, q_k⟩` — q_of(g_k)-tagged for IntentionPosition tagging, advances `IntentionPosition(M-cycle-parent-C, g_k) = gate-failed q_k`
- **M (sub-cycle-tagged)**: `⟨open, C+1⟩` — establishes the new sub-cycle's identity
- **S**: push one entry (parent-C, parent-pending-q, parent-prefix)
- **C**: parent-C → C+1 (sub-cycle activated)
- **R**: **UNCHANGED.** The parent's q_k is NOT committed-to-sub-cycle as a deduction; the sub-cycle inherits visibility to the actor's R-multiset via the actor's identity, and any consumption is by the sub-cycle's R-execute. **The escalation R-effect is at §11.6.3 R-close-nested (`R ⊎ E`), not at R-spawn or R-resume** per the §A6.1 placement: R-close-nested is the escalation R-writer; R-spawn and R-resume are parent-R-unchanged. Any rewrite that gives R-spawn an R-write would be the §A6.1 inversion the user-review explicitly warned against.

**IntentionPosition tagging for the escalation round-trip** (per design note §5 Sarah trace, the load-bearing demonstration). R-spawn's `⟨gate-fail, q_k⟩` marker is q_of(g_k)-tagged → parent's IntentionPosition(g_k) = gate-failed q_k. During sub-cycle execution, parent's M-cycle-parent-C is untouched (sub-cycle's entries are sub-cycle-tagged, not parent-tagged), so parent's IntentionPosition(g_k) stays at `gate-failed q_k`. After §11.6.3 R-close-nested adds parent's q_k to R, and §11.6.4 R-resume writes `⟨resume, parent-C, q_k⟩` (parent-tagged, q_of(g_k)-tagged), parent's IntentionPosition(g_k) advances to `resumed q_k`. Then R-gate's premise `IntentionPosition(g_k) ∈ {θ-written, resumed q_k}` matches and the gate re-tests with R now containing q_k — the re-test succeeds, R-gate fires, IntentionPosition(g_k) = gate-passed q_k. **This round-trip is exactly the Sarah-T15-R-execute(γ_1) past-sibling-markers reproduction the design note §5 walks; the marker-tagging makes it mechanical.**

**Standing-option principle (R-spawn admissibility).** R-spawn(g_k) is per-g_k admissible whenever (a) cycle's per-intention phase active, (b) IntentionPosition(g_k) ∈ {θ-written, resumed q_k}, AND (c) R ∌ q_k. At distinct g_a, g_b both gate-failed at the same cycle-state, σ picks which g_k to spawn first — but active-C forces sequential resolution (the chosen g_k spawns → sub-cycle runs → R-resume pops S → parent active again → THEN the other g_k can spawn). Sibling sub-cycles cannot stack on S simultaneously per design §5.6.

**Coupling structure (per Phase 1 audit §A4).**
- **C/S coupling**: R-spawn writes C and S. R-spawn ↔ R-resume coupled through C/S (R-spawn pushes; R-resume pops, in matched pairs). R-spawn(g_a) ↔ R-spawn(g_b) for distinct g_k coupled through C (active-C forces sequential — sibling stacking impossible per design §5.6).
- **Dual-with-R-gate at gate-eligibility position**: R-spawn ↔ R-gate at the same IntentionPosition(g_k) ∈ {θ-written, resumed q_k} state is guard-determined by R's contents — Pillar-2 fork, NOT σ-discretion.
- **R-coupling at same q_of**: state-conditional under §8.1 functional-q_of-v1 (distinct g_k → distinct q_of → distinct R-components → R-pair-independent).
- **No direct F4 coupling**: R-spawn doesn't change PerIntentionTerminal directly (g_k goes from θ-written or resumed to gate-failed — still in the per-intention pass, not terminal).

**Redex form.** The gate-fail premise `[a./R.] ∌ [base-prefix/o./g_k/q.]` is the failure complement to R-gate's pass premise. When the parent's R-set does *not* contain the required q-designation, R-gate cannot fire and R-spawn fires instead. The two-rule symmetry (R-gate fires on pass, R-spawn fires on fail) is the **lifecycle/failure-family handoff point**; one and only one of the two fires from any given gate-eligible position. **Variable naming**: `base-prefix` is the *current cycle's own interest-prefix* — for the actor's only top-level cycle that is `Α/i.` (sole-of-type per A6), for an additional top-level cycle that is `Α/iN` with N the cycle's fresh interest-ordinal per §11.4.2's iN discipline, and for a nested cycle it is `parent-prefix/i.` (sole-of-type within the inherited prefix). The *S-entry field* that the rule pushes is named `parent-prefix` because it describes the parent's suspended position in the address tree — but it is *constructed from* the current cycle's `base-prefix` as `base-prefix/o./g_k/`. So `base-prefix` (rule input) and `parent-prefix` (S-entry field) differ by `/o./g_k/`. The iN discipline on `base-prefix` is what propagates the per-cycle interest-ordinal into every nested cycle's prefix: a sub-cycle of the actor's second top-level cycle has prefix `Α/i2/o./g_k/`, distinguishing it from sub-cycles of the actor's first top-level cycle (prefix `Α/i1/o./g_k/`) — the cycle-discriminator the dissertation built slash addressing for.

**Side conditions.** C advances by 1 (the sub-cycle's identifier). S grows by one entry. M gains two markers with **different cycle-tags** (per the §11.1 per-rule tagging clause): `⟨gate-fail, q⟩` is tagged with the **failing parent** cycle (the pre-transition C, since the failed attempt belongs to the parent's audit trail), and `⟨open, C+1⟩` is tagged with the **new sub-cycle** (the post-transition C+1, since the open marker is what gives that cycle its identity). The two markers are written in the same step but live in different cycle-filtered views of M. **R is unchanged** — R-spawn does not deduct from R, because the parent's resources are still the actor's; they will be available to the sub-cycle and, if anything is consumed, the deduction will be by the sub-cycle's R-execute. The new S-entry's `parent-prefix` (= `base-prefix/o./g_k/`) is what the spawned sub-cycle prepends to its own operation paths (the Rusty Table 17 nesting `Α/i./o./g1/i./...` is constructed by prepending the S-entry's `parent-prefix = Α/i./o./g1/` to the sub-cycle's own `i./...` operations).

**Worked-case validation.** Rusty Table 16, line 407: `[a./R.] ∋ [Α/i./o./g1/q1.]` — Rusty's R does *not* satisfy the required q1, R-gate cannot fire. R-spawn fires instead. S now holds `⟨16's parent-C, [Α/i./o./g1/q1.], Α/i./o./g1/⟩`. The sub-cycle that opens is Table 17's Rusty/Erik cycle, whose operations (lines 418–429) all carry the `Α/i./o./g1/i./...` prefix.

#### §11.6.3 R-close-nested — sub-cycle close + flowback, one atomic step (premise unchanged 2026-06-23 per Thread A reframe; **`R ⊎ E` preserved — this rule IS the escalation R-writer per §A6.1**)

```
   last(M-cycle-C) = Λ-body                                  (sub-cycle reached Λ — cycle-shared at sub-cycle scope)
   S = ⟨parent-C, parent-pending-q, parent-prefix⟩ :: S'    (S non-empty: sub-cycle is nested under parent)
   earnings(cycle C) = E
   ─────────────────────────────────────────  [R-close-nested]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; 
                          M ⊎ ⟨close-nested, C, parent-C⟩ 
                            ⊎ ([a.]Φ(parent-prefix/i./O./Q.) := E) 
                            ⊎ ⟨flowback-recorded, E⟩ 
                          ; S ; R ⊎ E⟩
```

**Premise-shape note (Thread A IntentionPosition scope — no premise change).** R-close-nested is a **sub-cycle-scoped rule**, not per-intention. Its premise reads sub-cycle's `last(M-cycle-C)` for Λ-body presence (cycle-shared at sub-cycle scope) plus S non-empty (cycle-shared cross-cycle structure). **No IntentionPosition substrate is needed in the premise** — the rule fires from sub-cycle Λ regardless of any g_k's per-intention position. The Thread A reframe does NOT modify R-close-nested's premise; it confirms the rule's **R-effect placement** as the escalation R-writer (the §A6.1 correction's load-bearing finding).

**Escalation R-writer — confirmed per §A6.1 (the load-bearing watch-point).** R-close-nested's contractum's `R ⊎ E` is **THE escalation R-writer** — the cross-cycle update that grows parent-R by the sub-cycle's earnings E. This is the spec-correct behavior cited verbatim by the user-review of the Phase 1 audit: "*R is unchanged at the resume step itself — R already gained the parent's needed q via R-close-nested's earlier `R ⊎ E`.*" The Phase 1 audit's first-draft mis-attribution (which had R-resume as the R-writer) has been corrected throughout — R-close-nested is the writer; R-resume is C/S-only. **`R ⊎ E` is preserved unchanged** in this rewrite; any edit that strips it or moves the R-effect to R-spawn or R-resume would be the §A6.1 inversion the user explicitly warned against.

**Cross-cycle write characterization (per Phase 1 audit §A3 S1 + §A4).** R-close-nested writes:
- **Sub-cycle M (sub-cycle-tagged)**: `⟨close-nested, C, parent-C⟩`, Φ-body, `⟨flowback-recorded, E⟩`
- **Parent-R (cycle-shared scalar, cross-cycle effect)**: `R ⊎ E` — **the rule fires in the sub-cycle but writes parent-R**

The cross-cycle R-write is what makes R-close-nested ↔ any parent-cycle R-reader (R-gate(g_b), R-execute(g_b), R-flowback at parent) I-coupled per Phase 1 §A4 — structurally important for §13.6's per-σ confluence proof over the explicit independence relation `I`. **R-close-nested does NOT write any g_k-tagged entry** at parent — the marker-tagging that advances parent's IntentionPosition(g_k) to `resumed q_k` is done by R-resume's `⟨resume, parent-C, q_k⟩` marker, NOT by R-close-nested. R-close-nested's only parent-side effect is the R-multiset update.

**Standing-option principle.** R-close-nested is structurally triggered (no σ-discretion): when sub-cycle reaches Λ-body AND S is non-empty, R-close-nested is the only admissible next rule (it must fire before R-resume can read the `⟨flowback-recorded, E⟩` marker). Sequential by construction.

**Coupling structure (per Phase 1 audit §A4).**
- **Cross-cycle R-coupling (S1)**: R-close-nested ↔ {R-gate(g_b), R-execute(g_b), R-flowback}_parent — the parent-R reader rules read the post-R-close-nested R-state. This is the load-bearing coupling for the escalation boundary's §13.6 verification.
- **Sub-cycle sequential**: R-close-nested → R-resume (R-resume's premise reads sub-cycle's `last = ⟨flowback-recorded, E⟩`, which R-close-nested wrote).
- **No per-intention coupling at parent**: R-close-nested writes no g_k-tagged entry to parent-M; it doesn't advance any parent g_k's IntentionPosition.

**Side conditions.** R-close-nested is the **sub-cycle's R-close + R-flowback fused**. It exists because the audit-trail clarity benefit of a single named "this is a nested close" event outweighs the small redundancy of fusing two normally-separate rules. The Φ argument's path uses `parent-prefix/i./O./Q.` rather than `Α/i./O./Q.` — Rusty Table 17 line 429 (Obtained utility) shows the nested form `[Α/i./o./g1/i./t.]Θ(Α/i./o./g1/i./O./U.)`, confirming that sub-cycles write their post-D-21 Φ at the nested path. C, S unchanged (S is popped by R-resume, not by R-close-nested). The `[a.]` prefix is the actor's, same as the top-level R-flowback — the obtained resources are still the *actor's* gains, just earned through the sub-cycle.

**Redex form.** No surface-syntax redex — R-close-nested is structurally triggered (sub-cycle has reached its Λ-body and S is non-empty). The rule writes three M-entries (sub-cycle-tagged: close-nested marker, Φ declaration, flowback-recorded marker) plus the cross-cycle parent-R update — one atomic step.

**Side conditions.** R-close-nested is the **sub-cycle's R-close + R-flowback fused**. It exists because the audit-trail clarity benefit of a single named "this is a nested close" event outweighs the small redundancy of fusing two normally-separate rules. The Φ argument's path uses `parent-prefix/i./O./Q.` rather than `Α/i./O./Q.` — Rusty Table 17 line 429 (Obtained utility) shows the nested form `[Α/i./o./g1/i./t.]Θ(Α/i./o./g1/i./O./U.)`, confirming that sub-cycles write their post-D-21 Φ at the nested path. C, S unchanged (S is popped by R-resume, not by R-close-nested). The `[a.]` prefix is the actor's, same as the top-level R-flowback — the obtained resources are still the *actor's* gains, just earned through the sub-cycle.

**Worked-case validation.** Rusty Table 17, the sub-cycle Rusty ran with Erik to acquire authority. The sub-cycle's Λ row (line 429: `[Α/i./o./g1/i./t.]Θ(Α/i./o./g1/i./O./U.) := { [Α/i./o./g1/i./t./D./P./u.] }`) is followed by the sub-cycle's obtained-resource declaration (the form `[a.]Θ(Α/i./o./g1/i./O./Q.) := { ... }` post-D-21 → Φ), which is what R-close-nested writes atomically with the close-nested marker and flowback-recorded marker.

#### §11.6.4 R-resume — pop S, parent resumes at gate (premise unchanged 2026-06-23 per Thread A reframe; **R-effect = NONE confirmed C/S-only per §A6.1**; resume marker is q_of(g_k)-tagged for parent's IntentionPosition advancement)

```
   last(M-cycle-C) = ⟨flowback-recorded, E⟩
   S = ⟨parent-C, parent-pending-q, parent-prefix⟩ :: S'
   R ∋ parent-pending-q    (the sub-cycle obtained what the parent needed)
   ─────────────────────────────────────────  [R-resume]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨parent-C ; 
                              M ⊎ ⟨resume, parent-C, parent-pending-q⟩ 
                          ; S' ; R⟩
```

**Premise-shape note (Thread A IntentionPosition scope — no premise change).** R-resume is a **sub-cycle-scoped rule** with cycle-shared premises (sub-cycle's `last` = ⟨flowback-recorded, E⟩; S non-empty; parent's R-test `R ∋ parent-pending-q`). **No IntentionPosition substrate change** — the rule fires from sub-cycle flowback regardless of any g_k's per-intention state at sub-cycle scope. The Thread A reframe DOES NOT add an R-effect to R-resume; it confirms the spec's existing "R unchanged" semantics and emphasizes the contractum's marker as the IntentionPosition-advancement mechanism for parent's g_k.

**R-effect = NONE — confirmed C/S-only per §A6.1 (the load-bearing watch-point).** §11.6.4's existing Side conditions state verbatim: "*R is unchanged at the resume step itself — R already gained the parent's needed q via R-close-nested's earlier `R ⊎ E`.*" This is the spec-correct C/S-only behavior. The Phase 1 audit's first draft mis-attributed R's gain to R-resume; user-review caught it (citing this verbatim §11.6.4 text); Phase 1 §A6.1 corrected the catalog. **This rule's contractum: pop S, transition C ← parent-C, write the resume marker. NO R-write.** Any rewrite that adds an R-effect here would be the §A6.1 inversion the user explicitly warned against. The R-effect at the escalation boundary lives at §11.6.3 R-close-nested's `R ⊎ E`, NOT here.

**IntentionPosition tagging of the resume marker (per design §5 round-trip).** R-resume writes `⟨resume, parent-C, parent-pending-q⟩` to M (parent-tagged via the §11.1 tagging clause — see "Tagging clause" paragraph below). The marker's `parent-pending-q` field is exactly q_of(g_k) for the specific g_k whose gate failed and triggered the escalation — so the marker is **q_of(g_k)-tagged**, and `IntentionPosition(M-cycle-parent-C, g_k) = resumed q_k` after R-resume fires. This is what enables R-gate's premise `IntentionPosition(g_k) ∈ {θ-written, resumed q_k}` to match at the parent (alongside `R ∋ q_k` which R-close-nested's earlier `R ⊎ E` made true) — the gate re-test fires R-gate, IntentionPosition(g_k) advances to `gate-passed q_k`, and the parent continues toward R-execute(γ_k). **This is the round-trip the design note §5 Sarah trace relies on**; the marker-tagging is what makes IntentionPosition(g_1) readable past sibling-intention g_2 markers in Sarah's interleaved escalation (the e10-read-past-e11/e12/e13 demonstration).

**Standing-option principle (R-resume admissibility).** R-resume itself is **structurally triggered** (no σ-discretion at the resume step) — when sub-cycle's `last = ⟨flowback-recorded, E⟩` AND S is non-empty AND R ∋ parent-pending-q, R-resume fires as the only admissible sub-cycle→parent transition rule. The σ-fork is created at the parent AFTER R-resume fires: parent's gate re-test admits R-gate (R now has q_k → gate passes) OR R-spawn (deeper escalation if R-close-nested's E didn't include q_k — which the R ∋ parent-pending-q premise of R-resume actually forbids, so this branch is structurally excluded by the safety check) OR §11.6.6 R-moot / §11.6.7 R-abandon (operator-elected exit). The safety check is what guarantees R-resume is the **successful** resumption rule — if the sub-cycle's E didn't satisfy parent-pending-q, R-resume cannot fire and the cycle stays at sub-cycle layer until R-moot or R-abandon fires.

**Coupling structure (per Phase 1 audit §A4).**
- **C/S coupling**: R-resume writes C and S (pops one S-entry, transitions C to parent). R-resume ↔ R-spawn coupled through C/S (matched push/pop). R-resume ↔ R-abandon coupled through S (both pop in nested case).
- **NO R-coupling at R-resume** (per §A6.1): R-resume is C/S-only. The escalation R-coupling lives at R-close-nested.
- **Parent-IntentionPosition coupling (per-K, cross-cycle effect at the marker level)**: R-resume's `⟨resume, parent-C, q_k⟩` write advances parent's IntentionPosition(g_k) to `resumed q_k`, which couples to subsequent parent-cycle per-intention rules (R-gate, R-spawn at parent) reading IntentionPosition(g_k) ∈ {θ-written, resumed q_k}.
- **Sub-cycle → parent sequential**: R-close-nested's `⟨flowback-recorded, E⟩` is read by R-resume's premise; sequential.

**Redex form.** No surface-syntax redex — R-resume is structurally triggered (sub-cycle just flowed back AND S is non-empty AND R now contains the parent's pending q). The rule writes the `⟨resume, parent-C, q⟩` marker and **transitions C back to parent-C**; S is popped.

**Side conditions.** R is unchanged at the resume step itself — R already gained the parent's needed q via R-close-nested's earlier `R ⊎ E`. The premise `R ∋ parent-pending-q` is the safety check the user flagged in the failure-family review brief: **the obtained-q must land in R before the gate re-test, or R-resume re-fails and the chain spawns again indefinitely**. The premise enforces this by refusing to pop until R contains the q. If the sub-cycle's earnings E do not include parent-pending-q, R-resume cannot fire; the cycle is stuck and either R-spawn (a deeper escalation), R-moot (the parent's premise no longer holds), or R-abandon (give up) must fire instead. This is by design — R-resume is the *successful* resumption rule, not the only post-flowback rule.

**Tagging clause** (per §11.1). The `⟨resume, parent-C, parent-pending-q⟩` marker is tagged with the **resumed parent** cycle (post-transition C = parent-C), **not** with the sub-cycle's pre-transition C. This is what makes R-gate's post-resume trigger work mechanically: R-gate's premise reads `last(M-cycle-parent-C) = ⟨resume, parent-C, q⟩`, and the resume marker is in M's parent-C-filtered view, so the trigger matches. **Belt-and-suspenders ordering claim**: after R-resume fires, the resume marker IS the most-recent parent-C-tagged entry in M, not merely *one of* them, because between the parent's `⟨gate-fail, q⟩` (its previous most-recent parent-C entry) and `⟨resume, parent-C, q⟩` (the current step) every intervening entry — the sub-cycle's open, ι, δ, ω, γ, θ, gate-pass, ε, Γ, select-staged, Ω, Λ, close-nested, Φ, flowback-recorded — was tagged with the sub-cycle's C, not parent-C. So `last(M-cycle-parent-C)` lands on `⟨resume, parent-C, q⟩` and R-gate's `last = resume marker` premise matches exactly. That ordering claim is what the `last(...)` (not `contains(...)`) form of R-gate's premise requires; the tagging discipline makes it hold.

After R-resume fires, the parent's M-cycle-parent-C state is: `..., θ-body, ⟨gate-fail, q⟩, ⟨resume, parent-C, q⟩`. The parent's θ-body is still in M (M is append-only), so R-gate's premise `M-cycle-C contains θ-body` still holds. R-gate re-fires on the parent, this time passing because `R ∋ q`. The audit trail records both the original `⟨gate-fail, q⟩` and the subsequent `⟨gate-pass, q⟩` — the full escalation event is reconstructable from M alone.

**Worked-case validation.** Rusty Table 18, the parent cycle's resumption. After the sub-cycle (Table 17) flowed back the authority Rusty needed, R-resume sets C back to the parent cycle's index. Table 18 begins with Rusty's execution of Intention 1 (line 438: `[a.]ε(Α/i./o./g1/e.) → { [Α/i./t./D./X./c.] + [Α/i./o./g1/q1] + [Α/i./o./g1/q2] }`), which is the parent's R-execute firing after the gate re-passed — confirming the parent resumed at the gate-and-execute juncture, not at some earlier or later point.

#### §11.6.5 R-perceive-failure — realized comparison fails projected γ-body (split into Rusty per-intention + Nathan cycle-shared variants 2026-06-23 per Thread A reframe + §A6.3 symmetric pairing with R-perceive)

Two rules sit at this section, mirroring R-perceive's variant structure (§11.4.9 Rusty per-intention + the deferred Nathan R-perceive-cycle variant). Per Phase 1 §A6.3, R-perceive and R-perceive-failure are **two outcomes of the same perception event at the same lifecycle position**; their cardinality cannot diverge, and both inherit their cardinality from §1.4.5 rows 122/123. The Rusty variant writes a per-K `⟨perceive-failure, g_k⟩` marker (system-internal, for IntentionPosition tagging); the Nathan variant writes the cycle-scoped `⟨perceive-failure, C⟩` marker. **The two markers MUST be kept separate** — shipping a single unified rule would mis-tag one of the two cases.

##### §11.6.5.1 R-perceive-failure (Rusty per-intention variant) — comparison for g_k fails

```
   per-intention phase active in M-cycle-C                          (per §11.1)
   CyclePattern(M-cycle-C) = per-intention                          (per §11.1 + WF-5; Gate (4) commitment — makes R-perceive-failure (Rusty) admissible at per-intention cycles only)
   IntentionPosition(M-cycle-C, g_k) = executed                    (Rusty pattern: per-intention)
   [Α/i./t.]Γ(Α/i./t./D./G.) = { comparison }  is well-typed at Layer 2
   the realized comparison for g_k does NOT validate γ_k's projected comparison declared at R-intention
   ─────────────────────────────────────────  [R-perceive-failure (Rusty)]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; 
                          M ⊎ ([Α/i./t.]Γ(Α/i./t./D./G.) = { failing-comparison }) 
                            ⊎ ⟨perceive-failure, g_k⟩ 
                          ; S ; R⟩
```

**Contractum addition (system-internal IntentionPosition tagging, parallel to R-perceive's Batch 2 addition).** The Γ-body is target-prefixed with no g_k in its path, so without the `⟨perceive-failure, g_k⟩` marker IntentionPosition(g_k) would remain at `executed` after firing and the rule would be re-firable — incoherent. The marker is a per-K-tagged audit-trail meta-entry per §11.3, mirroring §11.4.9 R-perceive's `⟨perceive, g_k⟩` addition.

**Premise-shape note.** Pre-reframe premise was `last(M-cycle-C) = ε-body` (positional). Under reframe, becomes `IntentionPosition(g_k) = executed` (per-K) — the same shift as R-perceive's Batch 2 rewrite. R-perceive-failure (Rusty) and R-perceive (Rusty) are **a symmetric Pillar-2 guard-determined fork at the same lifecycle position**: at any state with `IntentionPosition(g_k) = executed`, exactly one of the two fires based on whether the realized comparison validates γ_k's projection. Not σ-discretion — guard-determined per §1.4.5 perceive-cardinality.

**Standing-option principle.** Like R-perceive (Rusty), R-perceive-failure (Rusty) is admissible per-g_k whenever (a) per-intention phase active, (b) `IntentionPosition(g_k) = executed`, AND (c) the realized comparison fails to validate. The (rule, g_k) σ-pick layer is the σ-discretion surface (which g_k to perceive next at multi-intention Rusty interleaving); the validate-or-not choice between R-perceive and R-perceive-failure is Pillar-2 guard-determined.

**Coupling structure (per Phase 1 §A4 + §A6.3 symmetric pairing).**
- **Symmetric guard-determined fork** with R-perceive(g_k): exactly one fires per `IntentionPosition(g_k) = executed` state based on comparison's realized value
- **F4 coupling to R-select**: R-perceive-failure(g_k) advances IntentionPosition(g_k) to `perceived` (the Γ-body and failure marker together record perception's outcome; the position reached is still terminal per the PerIntentionTerminal predicate at R-select's atomic conjunction read — `perceived` covers both validating and failing perceptions)
- **Downstream three-way fork**: post-`⟨perceive-failure, g_k⟩`, the operator chooses R-intention (new g_k), R-moot / R-moot-intention, or R-abandon — these read the marker to know perception failed; same downstream structure as the pre-reframe rule, just per-K-tagged now.

##### §11.6.5.2 R-perceive-failure-cycle (Nathan cycle-shared variant) — cycle-level comparison fails

```
   per-intention phase active in M-cycle-C                          (per §11.1)
   CyclePattern(M-cycle-C) = cycle                                          (per §11.1 + WF-5; Gate (4) commitment — makes R-perceive-failure-cycle admissible at cycle-pattern cycles only)
   ∀ g_k ∈ LiveIntentions(M-cycle-C): IntentionPosition(g_k) = executed     (Nathan simultaneity guard per §A6.2)
   [Α/i./t.]Γ(Α/i./t./D./G.) = { cycle-level comparison }  is well-typed at Layer 2
   the realized cycle-level comparison does NOT validate the cycle's terminal perceive
   ─────────────────────────────────────────  [R-perceive-failure-cycle (Nathan)]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; 
                          M ⊎ ([Α/i./t.]Γ(Α/i./t./D./G.) = { failing-cycle-comparison }) 
                            ⊎ ⟨perceive-failure, C⟩                       (cycle-scoped, NOT per-K)
                          ; S ; R⟩
```

**Contractum: cycle-scoped marker only — NO per-K marker.** The Nathan-pattern terminal perceive is cycle-shared, not per-intention; the `⟨perceive-failure, C⟩` marker is cycle-scoped (tagged with C, no g_k argument). The Rusty per-K `⟨perceive-failure, g_k⟩` marker is INAPPROPRIATE for the Nathan variant — using it would create a phantom per-g_k position when Nathan-pattern intentions don't have per-K perceive marker writes. **This is the split the user-review pre-flagged**: shipping a single unified rule that writes one of the two markers based on a guard would mis-tag the other case.

**Premise-shape note.** Nathan-pattern uses the same `∀ live g_k: IntentionPosition(g_k) = executed` simultaneity guard as R-perceive-cycle's premise per §A6.2 (corresponding R-perceive-cycle rule landed 2026-06-23 post-Batch-5 as an R-perceive sub-section at §11.4.9 — Phase 3 gate (2) closed; this rule §11.6.5.2 is its failing-case dual). The cycle-level Γ-body is a single comparison evaluated at cycle scope, not per-intention.

**Standing-option principle and coupling structure.** Mirror R-perceive-cycle's structure (landed at §11.4.9 sub-section): structurally triggered post all-live-g_k = executed; symmetric guard-determined Pillar-2 fork with R-perceive-cycle (validate vs not); F4 coupling via the universal; downstream three-way fork same as Rusty variant but reads cycle-scoped marker.

**Worked-case validation — source-anchored (2026-06-23 post-Batch-5 dissertation trace).** The Nathan cardinality (cycle-level terminal perceive, NOT per-intention) is source-grounded at Table 11 (Nathan-Randy Part 2) per the R-perceive-cycle worked-case validation at §11.4.9. R-perceive-failure-cycle's specific failing-guard (`≤` in the realized comparison) is attested at Sarah's perceive (Sarah Table 14-15), where the realized cycle-perception fails to validate the projected. Together the two anchors close Phase 3 gate (2)'s previously-deferred fidelity check at the cardinality level. Member-by-member Γ-form trace queued for §14.3 Phase 4 propagation; the load-bearing cardinality claim is no longer provisional.

#### §11.6.5 R-perceive-failure shared prose (applies to both variants)

**Redex form.** Same surface form as R-perceive (`[Α/i./t.]Γ(...) = { comparison }`) — the rule difference is in the **validation premise**, not in the redex. R-perceive fires when the realized comparison validates γ's projected comparison; R-perceive-failure fires when it does not. The two are mutually exclusive at any given perceive position; one and only one fires.

**Side conditions.** C, S, R unchanged. The audit-trail entries record both the realized perception (for reconstruction of what the actor observed) and the structural `⟨perceive-failure, C⟩` marker (signals to downstream rules that this cycle cannot proceed to select/outcome on the failed intention's path). Downstream of R-perceive-failure, **one of three rules** fires — the perceive-failure marker doesn't force a wind-down; it forces a decision among continue-differently, give-up-premise, or give-up-choice:

1. **R-intention** (§11.4.5) — the principal adds a *new* intention at a fresh `g_k` and pursues the objective via a different intention. R-intention's expanded premise (`last(M-cycle-C) ∈ { ω-body, γ-body, ε-body, ⟨perceive-failure, C⟩ }`) admits this trigger directly. **Rusty Table 20 line 473** is the canonical worked case: after Intention 2's perception fails (`Γ(...) = { ≤ }` at line 472), Rusty declares a new γ₃ on line 473 (a new intention to add to Todd's incentive), then R-required-resources, R-gate (fails), R-spawn for the sub-cycle to Gerry, and so on. The original Intention-2 γ-body persists in M; the new γ₃ is appended. The cycle continues.
2. **R-moot** (§11.6.6) — the cycle's premise no longer holds (e.g., the preferred position became unreachable between R-detect and R-perceive; the target left the matrix). The cycle stops short of close/flowback.
3. **R-abandon** (§11.6.7) — the principal *chooses* to stop pursuing this cycle, regardless of premise. Single-level S-pop discipline (§11.6.7); the parent then decides its own next move.

**Worked-case validation.** **Two canonical cascades from R-perceive-failure are documented:** (a) **Sarah → moot** — Sarah's perception of her cycle's realized utilities does not validate her intention's projected comparison, R-perceive-failure fires, and the cycle becomes moot (R-moot below); (b) **Rusty → new intention** — Rusty T20 line 472's perception (`Γ(...) = { ≤ }`) does not validate Intention 2's projected comparison, R-perceive-failure fires, and Rusty then declares a new γ₃ at line 473 (R-intention firing under its expanded premise §11.4.5 with `last(M-cycle-C) = ⟨perceive-failure, C⟩`), continuing the cycle with a different intention. **R-abandon** is the unvalidated third branch (no dissertation engagement formally abandons; see §11.6.7's worked-case note). The pair R-perceive-failure → R-moot is **one** canonical cascade; R-perceive-failure → R-intention is the **other**; both are exhibited in the dissertation.

#### §11.6.6 R-moot — cycle becomes moot (cycle-scoped) AND R-moot-intention — single intention becomes moot (intention-scoped, added 2026-06-23 as a *partial* contribution toward Axis 4; see scope note below)

Two rules sit at this section, sharing the moot-attestation discipline but operating at different scopes. **R-moot** (existing, retained) writes a cycle-scoped `⟨moot, C⟩` marker — fires when the cycle's premise has become void as a whole. **R-moot-intention** (new, added 2026-06-23) writes an intention-scoped `⟨moot, C, g_k⟩` marker — fires when one specific intention's substantive premise has vanished while the cycle's remaining intentions can still progress. The two coexist with mutually exclusive applicability at K=1 (R-moot only; R-moot-intention's `LiveIntentions \ {g_k} ≠ ∅` side condition fails structurally) and form a licensed σ-fork at K ≥ 2.

**Scope note (Axis 4 status, post-review 2026-06-23, RESOLVED 2026-06-24 by the implemented Phase 2/3 reframe).** The 2026-06-23 user-review of this revision identified that R-moot-intention alone did not close Axis 4 — it provided the correct marker granularity (intention-scoped vs cycle-scoped) and the transparent-`last` convention (§11.6.6.2) that lets the marker coexist with the live intention's continuation, but at that point the Sarah T14/T15 reproduction could not run mechanically to R-close because **the then-current rule set still read positional `last`** (even operative-`last`), which couldn't represent two intentions at different lifecycle positions simultaneously. Sarah's escalation suspends both γ_1 at `⟨gate-pass, q_1⟩` and γ_2 at `⟨resume, q_2⟩`-then-mooted; under positional `last`, R-execute(γ_1) could not fire because γ_1's `⟨gate-pass, q_1⟩` was buried earlier in M under γ_2's resume marker, which transparent-`last` does not skip. The deeper finding from the review: **Axis 4 (intention-scoped moot), Axis 3b second half (double-spawn-on-S sequencing), and the post-resume R-execute continuation are three surface forms of one underlying gap — the multi-intention lifecycle's implicit assumption that intentions are processed sequentially via positional `last`, which escalation breaks**. The consolidated resolution identified was the structural reframe (per-intention lifecycle-position tracking), which dissolves all three together. **That reframe has now landed in full** — the Phase 2 rule premise rewrites (Batches 1–5) replaced positional `last` reads in every per-intention rule with IntentionPosition (per-K-filtered fold per §11.1) + global folds (F1–F5 per Phase 1 audit §A3 + §A5.4); the Phase 3 prerequisites all landed (R-select's executed-existential, R-perceive-cycle, §11.1 shape-based recognizer, CyclePattern + WF-5). **Sarah-T15 now mechanically reduces to R-close** under the implemented rules: at the post-Srini-resume state, R-moot-intention(g_2) writes `⟨moot, C, g_2⟩`; R-execute(g_1) reads `IntentionPosition(g_1) = gate-passed q_1` (per-K fold immune to the buried `⟨resume, q_2⟩` and `⟨moot, C, g_2⟩` markers, both g_2-tagged); R-perceive(g_1) advances g_1 to `perceived`; R-select fires (F4 universal satisfied: g_1 perceived, g_2 mooted); R-outcome → R-obtained-utility → R-close → R-flowback completes the cycle. Transition trace verified at source 2026-06-24. **Axis 4 is closed.** The full attribution and the joint-closure pattern (this revision delivered the marker-granularity contribution; Phase 2/3 reframe delivered the structural rewrite; the two combined dissolve the gap) are recorded in §11.6.6.3's "Scope and consolidated-gap finding" subsection below.

##### §11.6.6.1 R-moot — cycle becomes moot (existing rule, retained 2026-06-23 per Thread A reframe — premise unchanged; cycle-scoped contractum `⟨moot, C⟩` is the cycle-shared terminal marker, not per-K-tagged; intention-scoped granularity is handled by §11.6.6.3 R-moot-intention separately)

```
   last(M-cycle-C) = ⟨perceive-failure, C⟩
       OR  (operator-attested side condition: the cycle's premise has become void —
            e.g., the target has left the matrix, or the matrix's position-set has
            changed such that the preferred position is no longer reachable; the
            operator judges this from external state and elects to moot the cycle)
   ─────────────────────────────────────────  [R-moot]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ⟨moot, C⟩ ; S ; R⟩
```

**Redex form.** No surface-syntax redex — R-moot is structurally triggered when the cycle's premise no longer supports continuation. The most common triggers are R-perceive-failure's marker (perception did not validate) and any condition under which the target's preferred position has become unreachable between R-detect and R-perceive (e.g., the target left the matrix, or the matrix's position-set changed). The rule writes the `⟨moot, C⟩` marker and stops the cycle short of close/flowback.

**Side conditions.** R unchanged; the cycle gained no resources. S unchanged at this step (R-resume or R-abandon may pop S subsequently, depending on whether the moot cycle is top-level or nested). If the moot cycle is a sub-cycle (S non-empty), the parent's pending q was *not* obtained; R-resume cannot fire; the parent must escalate further (R-spawn **against a fresh g_k** per R-intention's freshness, §11.4.5 — same-g_k re-spawn after moot is forbidden for the same reason as after abandon: two sub-cycles spawned from the same parent g_k would share the `parent-prefix/i.` address and collide at Theorem 13.1's (W) layer) or abandon (R-abandon). If the moot cycle is top-level (S empty), R-open at C+1 fires next.

**When to use R-moot vs R-moot-intention.** R-moot applies when the cycle as a whole loses its premise — every intention's substantive purpose is jointly void, or the cycle's structural premise has vanished externally (target left the matrix). R-moot-intention (below) applies when one intention's substantive purpose is void while at least one other intention in the cycle remains live. **Heuristic**: if firing R-moot would prevent the cycle from reaching any close/flowback (because all intentions are mooted with it), use R-moot; if firing R-moot would terminate intentions that the source shows progressing, use R-moot-intention for the specific g_k.

##### §11.6.6.2 Transparent-`last` semantics for intention-moot markers (lifecycle-wide convention, added 2026-06-23)

**This is a lifecycle-wide semantics change, not a localized rule addition.** It is stated here because R-moot-intention (§11.6.6.3 below) introduces the only marker the convention applies to, but the convention governs every lifecycle rule's `last`-read. The first review draft of R-moot-intention attempted to write its marker as opaque-to-`last` (catching it via §13.6's symmetric-write mechanism, same as R-required-resources), but that opacity blocked the live intention's continuation: R-execute(γ_1) reads `last = ⟨gate-pass, q⟩`; if `last = ⟨moot, C, g_2⟩` after the moot fires, R-execute cannot fire — the live intention's lifecycle is broken. There is no firing order that escapes this: wherever R-moot-intention fires in g_1's chain, the moot marker becomes `last` and breaks g_1's next positional-`last` step. The transparent-`last` convention fixes this by defining:

**Convention (operative-`last`).** For every lifecycle rule whose premise reads `last(M-cycle-C)`, the read returns the **most-recent M-cycle-C entry that is NOT an intention-scoped moot marker `⟨moot, C, g_k⟩`** (with a g_k argument). Cycle-scoped markers (`⟨moot, C⟩`, `⟨abandon, C⟩`) are NOT skipped — they remain terminal markers that stop the cycle.

Notationally: when §11.4 / §11.6 / §11.7 rules write "`last(M-cycle-C) = X`" in a premise, the read is the operative-`last`, which transparently skips intention-scoped moot markers. The change is uniform across the lifecycle.

**Watch-point verifications (interaction with existing positional-`last` readings, performed during draft per the standing-option lesson)**:

| Marker | Written by | Read by | Affected by skip? |
|--------|-----------|---------|-------------------|
| `⟨moot, C, g_k⟩` (intention-scoped, NEW) | R-moot-intention (§11.6.6.3) | nothing — skipped | YES — defined to be skipped |
| `⟨moot, C⟩` (cycle-scoped) | R-moot (§11.6.6.1) | terminal — cycle stops | NO — not skipped |
| `⟨abandon, C⟩` | R-abandon (§11.6.7) | terminal | NO |
| `⟨resume, parent-C, q⟩` | R-resume (§11.6.4) | R-gate (post-resume) | NO |
| `⟨perceive-failure, C⟩` | R-perceive-failure (§11.6.5) | R-intention, R-moot, R-abandon | NO |
| `⟨gate-pass, q⟩` | R-gate (§11.4.7) | R-execute | NO |
| `⟨gate-fail, q⟩` | R-gate | R-spawn | NO |
| `⟨open, C⟩`, `⟨close-nested, ...⟩`, lifecycle bodies | various | various | NO |

The skip rule is narrow: only `⟨moot, C, g_k⟩` (with the g_k argument) is skipped. Every other marker (including cycle-scoped moot/abandon) reads as before.

**Persistence Invariant compliance.** The operative-`last` read is a derived view over M-cycle-C — a filtered projection over an append-only sequence, the same status as PendingTheta (§11.4.6), Δ (§7.5), and the R-objective-revise downstream readers' filtered views (§7.5.2 / §11.7.2 precedent). M itself remains append-only; no rule overwrites or removes any entry. The skip happens at read-time, on a fresh filter computation; nothing is stored. **§7.5 is satisfied without modification.**

**Why this is a lifecycle-wide convention, not "just a rule property of R-moot-intention".** Every lifecycle rule whose premise reads `last` is affected. A future reader of R-execute (§11.4.8) seeing "premise: `last = ⟨gate-pass, q⟩`" would be confused if they encountered R-moot-intention's intention-moot marker as `last` and thought R-execute should be blocked. The convention is explicit at the level where `last` is read — uniform, narrow, and cross-referenced from §11.1 / §11.4 / §11.6 prelude in the propagation pass.

**Propagation flag**: §11.1's discussion of `last(M-cycle-C)` (and §11.4 / §11.6 prelude paragraphs) should be updated to define operative-`last` and cross-reference §11.6.6.2. This is part of the post-review sweep; not done in this revision.

##### §11.6.6.3 R-moot-intention — single intention becomes moot (new rule, added 2026-06-23, under §11.6.6.2's transparent-`last` convention)

```
   (operator-attested side condition: g_k's substantive premise has become void —
        e.g., a sub-cycle's outcome substantively achieves g_k's purpose at the
        parent's interest level, or external state has rendered g_k's lever
        unnecessary; the operator judges this from the cycle's situation)
   g_k ∈ DeclaredIntentions(M-cycle-C)
   g_k ∉ MootedIntentions(M-cycle-C)        [g_k is declared and not already mooted]
   LiveIntentions(M-cycle-C) \ {g_k} ≠ ∅   [at least one other intention remains live]
   ─────────────────────────────────────────  [R-moot-intention]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ⟨moot, C, g_k⟩ ; S ; R⟩
```

Where the **derived views** over M-cycle-C are:

```
   DeclaredIntentions(M-cycle-C) = { g_k : ∃ [a.]γ(Α/i./o./g_k) ≡ {...} ∈ M-cycle-C }
   MootedIntentions(M-cycle-C)   = { g_k : ⟨moot, C, g_k⟩ ∈ M-cycle-C }
   LiveIntentions(M-cycle-C)     = DeclaredIntentions(M-cycle-C) \ MootedIntentions(M-cycle-C)
```

— three views, all folds over M-cycle-C per §7.5 Persistence Invariant; nothing is stored. (An earlier draft attempted a fourth view ClosedIntentions = `{ g_k : ∃ [a.]Ω(...g_k...) }`; the form is malformed because Ω is cycle-scoped (`Ω(Α/i./o.)`, no g_k argument), so the set is always ∅. Intention-level "closure" is not a primitive concept at the M-trace level — the cycle's lifecycle moves through intention chains and reaches Ω at cycle scope; per-intention completion is recorded as θ-write and ⟨gate-pass⟩/⟨perceive, ...⟩ entries, not as a marker tagged with g_k. LiveIntentions = Declared \ Mooted is the correct fold; the side condition `LiveIntentions \ {g_k} ≠ ∅` then reads "at least one other intention remains undeclared-as-moot," which is the structural property the rule needs.)

**Structural separation from R-moot (not a heuristic).** The side condition `LiveIntentions(M-cycle-C) \ {g_k} ≠ ∅` makes R-moot and R-moot-intention **structurally disjoint at K=1 cycles**: when the cycle has exactly one declared intention, `LiveIntentions \ {g_k} = ∅` and R-moot-intention's premise fails — only R-moot is admissible (cycle-scoped moot, the existing rule retained at §11.6.6.1). When the cycle has K ≥ 2 declared intentions and at most K-1 are already mooted, R-moot-intention is admissible (intention-scoped moot, new rule) and R-moot remains separately admissible (operator may still elect to moot the whole cycle). The two rules cover disjoint structural cases at K=1 and form a licensed σ-fork at K ≥ 2 (operator chooses moot-this-intention vs moot-the-whole-cycle). This is hard structural separation enforced by the side condition, not a heuristic preference between two interchangeable rules. The earlier draft framed the separation as a "heuristic" — that framing is withdrawn: R-moot-intention cannot fire at K=1, full stop.

**Standing-option principle (R-moot-intention admissibility, stated upfront per §1.4.5 standing-option discipline).** R-moot-intention is admissible at **any reachable state of a K ≥ 2 cycle** where the operator attests g_k's substantive premise has vanished AND the structural side conditions are satisfied (g_k declared, not already mooted, at least one other live intention remains). This is **not** localized to a specific `last`-position — like R-required-resources (§11.4.6), R-moot-intention is a standing option whose admissibility is determined by a derived view over M-cycle-C plus operator attestation. At each such state R-moot-intention forms a σ-fork with whatever rule is otherwise admissible at that operative-`last`-position (R-execute, R-rr, R-perceive, R-intention, etc.). The operator's σ chooses **moot g_k now vs proceed with the current lifecycle activity**. This is a second pervasive Pillar-4 interleaving-discretion surface (parallel to R-rr's, established by §11.4.6's revision) — the operator may moot any non-sole live intention at any point after its declaration.

**Redex form.** No surface-syntax redex — R-moot-intention is operator-triggered, similar to R-moot but with intention-level scope. The most common trigger (Sarah T14/T15 worked case) is a sub-cycle's outcome substantively achieving an intention's purpose at the parent's interest level: the actor no longer needs to pursue g_k because the goal it targets has been substantively reached via a side path. Other triggers: external state renders g_k's lever unnecessary; the actor judges g_k's pursuit no longer worth the cost.

**Side conditions.** C unchanged; S unchanged; R unchanged (no resource flow at moot). The cycle continues to progress on its remaining live intentions; R-execute / R-perceive / etc. fire for the remaining γ_j's per the operative-`last` convention defined at §11.6.6.2 (the intention-moot marker is skipped by all `last`-readers), and the cycle eventually closes via R-close / R-flowback when at least one remaining intention reaches outcome. **Important interaction with §11.4.6's PendingTheta**: R-moot-intention's contractum appends `⟨moot, C, g_k⟩`, and the updated PendingTheta definition (see §11.4.6 cross-reference below) excludes mooted intentions — so R-rr will not fire for a mooted g_k, even if g_k's θ has not been written. This prevents the dangling-pending-θ case where R-rr would attempt to resource a mooted intention.

**Cross-reference update to §11.4.6's PendingTheta definition.** The PendingTheta derived view at §11.4.6 must be updated to exclude mooted intentions:

```
   PendingTheta(M-cycle-C) = { g_k : ∃ [a.]γ(Α/i./o./g_k) ≡ {...} ∈ M-cycle-C
                                     ∧ ∄ [a.]θ(Α/i./o./g_k) := {...} ∈ M-cycle-C
                                     ∧ ⟨moot, C, g_k⟩ ∉ M-cycle-C }
```

This is a one-clause addition to the original definition; it preserves the Persistence Invariant (still a derived fold over M-cycle-C, no slot). The clause prevents R-rr from firing for mooted intentions — closing the standing-option interaction the §1.4.5 row-walk identified as a concern.

**Worked-case validation: Sarah T14/T15, traced under operative-`last` to R-close.**

The trace below uses **operative-`last`** per §11.6.6.2: every `last(M-cycle-parent-C)` read skips `⟨moot, C, g_2⟩`. The literal-last entry after R-moot-intention(g_2) is `⟨moot, C, g_2⟩`; operative-`last` returns the most-recent non-intention-moot entry.

- **T12** declares γ_1 (row 10), γ_2 (row 11), θ_1 (row 12, fires from PendingTheta = {γ_1, γ_2}), gate_1 ∌ (R-gate-fail-q_1), θ_2 (row 14, fires from PendingTheta = {γ_2} after θ_1 written), gate_2 ∌ (R-gate-fail-q_2).
- **R-spawn** for Beth (sub-cycle 1) at `⟨gate-fail, q_1⟩` — pushes S, C ← Beth-C. Beth's sub-cycle runs to R-close-nested, writing q_1 to parent's R-credit. **R-resume(q_1)** pops S, parent active again, operative-`last(M-cycle-parent-C) = ⟨resume, parent-C, q_1⟩` (no intention-moot markers yet). The parent's q_1-pending need is now satisfied; **R-gate-retry** (or equivalent post-resume gate continuation per §11.4.7 + §11.6.4) fires for gate_1, producing `⟨gate-pass, q_1⟩`. Sarah's γ_1 is now in execute-position.
- **R-spawn** for Srini (sub-cycle 2) at `⟨gate-fail, q_2⟩` — but operator-σ may interleave Beth's full chain before Srini's spawn, or spawn Srini before Beth resumes, per the standing-option-on-spawn discretion of Axis 3b's second half (still open). For trace continuity assume R-spawn for Srini fires at the appropriate point per the source's T12-T14 sequence; what matters here is the state immediately before R-moot-intention.
- **T13** Beth's sub-cycle runs to flowback (covered above for the trace's logical ordering; the source presents T13 as Beth's sub-cycle table).
- **T14** Srini's sub-cycle runs to R-close-nested; Srini's outcome (Srini agrees not to enter the competition) substantively achieves g_2's purpose at the parent's interest level (fewer competitors → Sarah's preferred position more reachable without needing γ_2's specific lever). **R-resume(q_2)** pops S, parent active again, operative-`last(M-cycle-parent-C) = ⟨resume, parent-C, q_2⟩`.
- **Operator attests g_2's substantive premise has become void** (Srini's withdrawal made γ_2's lever unnecessary). **R-moot-intention** fires for g_2: g_2 declared (T12 row 11 ✓); g_2 not previously mooted ✓; LiveIntentions = {g_1, g_2} \ {g_2} = {g_1} ≠ ∅ ✓ (γ_1 is still live — its θ_1 is written and gate_1 passed via Beth's resume; γ_1 has not been mooted). Contractum appends `⟨moot, C, g_2⟩`. **Literal-last = `⟨moot, C, g_2⟩`; operative-`last` STILL = `⟨resume, parent-C, q_2⟩`** — the intention-moot marker is skipped (per §11.6.6.2).
- **T15 row 1 — and here the trace stops.** With operative-`last = ⟨resume, parent-C, q_2⟩` (the most-recent non-intention-moot entry), the post-resume continuation for q_2 would normally feed gate_2-retry → execute(γ_2) → perceive(γ_2). But γ_2 has been mooted; R-rr is excluded (PendingTheta excludes mooted g_k); the q_2-credit on R is preserved but γ_2 no longer claims it. **The cycle needs to continue on γ_1, whose `⟨gate-pass, q_1⟩` was written earlier in M (before the Srini-spawn, Srini-resume, and g_2-moot).** Transparent-`last` skips the intention-moot marker but does NOT skip Srini's resume marker (cycle-scoped, not in §11.6.6.2's skip set), so operative-`last` still returns `⟨resume, parent-C, q_2⟩`, not γ_1's `⟨gate-pass, q_1⟩`. **R-execute(γ_1)'s premise `last = ⟨gate-pass, q⟩` does not match, and R-execute cannot fire.** The cycle is stuck after R-moot-intention. **Sarah T15 does not mechanically reproduce on this revision alone.**

**Scope and consolidated-gap finding (per user-review of this revision, added 2026-06-23).** The blocker above is **not** §11.4.8's body-resolution fix-target — that one concerns R-execute's *body* (which q to deduct from R, `R ⊖ [sole-dot-q]`), not its *premise*. The actual blocker is that **positional `last`, even under the operative-`last` convention, cannot track two intentions sitting at different lifecycle positions simultaneously**. Sarah's escalation suspends γ_1 at `⟨gate-pass, q_1⟩` and γ_2 at `⟨gate-fail, q_2⟩` (then resume-then-moot). The §11.3 multi-intention lifecycle was specified under an implicit sequential-processing assumption — each γ completes its declare → θ → gate → execute → perceive pass before the next γ's pass — so positional `last` always tracks the currently-active intention. **Escalation breaks that assumption.** Two intentions are simultaneously suspended on S; both resume; the cycle must continue both; positional `last` is structurally inadequate to represent the post-resume state.

The phrase in an earlier draft of this trace — "the most-recent gate-pass for any live intention" — was already covertly describing a **per-intention, fold-keyed premise**, i.e., a derived view over M-cycle-C indexed by live g_k. That is the structural reframe of multi-intention lifecycle tracking, not a §11.4.8 thing.

**Consolidation across cataloged items.** Three §1.4.5 open items are surface forms of one underlying gap:

1. **Axis 4** (intention-scoped moot vs cycle-scoped contractum) — what this revision addresses at the marker layer.
2. **Axis 3b second half** (double-R-spawn-on-S sequencing under two-gate-failure with both γ's θ written) — the same multi-intention escalation surface from the spawn side.
3. **The post-resume R-execute(γ_1) continuation** (above) — the same multi-intention escalation surface from the resume side.

All three reduce to: **the multi-intention lifecycle needs per-intention lifecycle-position state**, so the cycle can hold γ_1 at gate-pass while γ_2 is mooted (or while γ_2 sits at a different position). With per-intention state, R-execute(γ_1)'s premise reads "γ_1's most-recent lifecycle entry = ⟨gate-pass, q_1⟩" (a fold over M-cycle-C filtered by g_1), not "literal positional `last`." This is the same lesson as the standing-option principle one level up: **derive from the lifecycle, don't chase individual instances.**

**Two honest paths forward (recorded for the project's next-thread decision, not executed here):**

- **(A) Structural reframe (consolidated fix).** Specify per-intention lifecycle-position state (e.g., `IntentionPosition(M-cycle-C, g_k) = (most-recent lifecycle entry tagged with g_k)`, a fold over M-cycle-C). Rewrite R-execute, R-perceive, R-select, R-outcome to read `IntentionPosition(g_k) = ⟨gate-pass, q⟩` etc. instead of literal-`last`. This dissolves Axis 4, Axis 3b second half, and the post-resume continuation as a single change. **High-value consolidation**; the right fix; bigger scope than one section.
- **(B) Scope this revision to building blocks** (the chosen path for this revision). R-moot-intention provides the correct marker granularity; §11.6.6.2 transparent-`last` provides the lifecycle-wide convention that lets the marker coexist with downstream readers; §13.6 re-base is correct. These are *building blocks toward* (A), not a closure of Axis 4. **Axis 4 status: marker-granularity contribution provided; full reproduction still blocked.** Mark Axis 4 as *partially addressed*, not closed. **Do not** drop the §1.4.5 fix-target count from three to two; instead, expand the §1.4.5 thin pointer to list the consolidated underlying gap with three cataloged surface forms.

**This revision implements (B).** (A) is flagged as the consolidated next-thread direction and is the change that resolves Axis 4 + Axis 3b second half + the continuation gap together.

**(A) has now landed in full — closure recorded 2026-06-24.** The Thread A IntentionPosition reframe (design + Phase 1 audit + Phase 2 rule premise rewrites + Phase 3 prerequisites) implemented the structural reframe described in option (A). Per-intention rules read IntentionPosition (per-K-filtered) instead of literal-`last`; cycle-shared close rules read literal-`last` on cycle-scoped markers per §11.1's distinction; the σ-fork at the perceive layer is closed by CyclePattern + WF-5 (§11.4.9 / §11.6.5 perceive rules + Gate 4 closure). **Sarah-T15 transition verified at source 2026-06-24**: R-moot-intention(g_2) → R-execute(g_1) → R-perceive(g_1) → R-select → R-outcome → R-obtained-utility → R-close → R-flowback. All three consolidated surface forms — Axis 4, Axis 3b second-half, post-resume R-execute continuation — closed jointly by the reframe as predicted. **The "building blocks" delivered by this revision plus the structural reframe delivered by Phase 2/3 jointly resolve Axis 4.** This subsection's framing of "(B) now, (A) later" is preserved as the historical decision record; the present status is "(A)+(B) both landed."

**§13 re-check obligations (this revision touches §13.5 termination + §13.6 determinism; flagged here for the propagation pass).**

- **§13.5 (termination + well-foundedness)**: R-moot-intention fires at most K_C - 1 times per cycle (the side condition `LiveIntentions \ {g_k} ≠ ∅` prevents mooting the last live intention; the cycle must retain at least one live intention to reach close). Per-cycle firing count remains bounded by a finite constant in K_C. **Well-foundedness**: M still append-only; intention-scoped moot is one more append. **Terminal-state question**: can a partially-mooted cycle still reach a terminal configuration? **In the sequential (no-escalation) case, yes** — at least one live intention remains; that intention progresses through R-execute → R-perceive → R-select → R-outcome → R-close → R-flowback per the lifecycle (under operative-`last`); the cycle reaches its standard terminal phases. **In the post-escalation case (Sarah T14/T15), termination is gated by the consolidated multi-intention escalation gap** identified in the Scope subsection above — the live intention's positional-`last` is occluded by sibling intentions' resume markers, so the lifecycle cannot advance under the current premise structure. Once the structural reframe (per-intention lifecycle-position tracking) lands, termination follows from each live intention's local lifecycle bound; until then, post-escalation partial-moot termination is the gap, not a guarantee. **Per-cycle bound**: stays finite under WF-1; R-moot-intention adds at most K_C - 1 firings to the bound (charge against K_C — each mootable intention is also charged against K_C as a declared γ).
- **§13.6 (determinism)**: R-moot-intention adds to σ's discretionary surface — operator chooses whether and when to fire it, and for which g_k. **Coverage via coarse-reading M-append-order (re-based from the earlier symmetric-write claim).** The earlier draft argued §13.6.3 clause-3 symmetric-write coverage: R-moot-intention writes `⟨moot, C, g_k⟩`, breaking every downstream `last`-reader, so any same-cycle pair with R-moot-intention is last-dependent on R-moot-intention. **That argument fails under the transparent-`last` convention (§11.6.6.2): the intention-moot marker is defined to NOT break downstream `last`-readers — they skip it.** The correct coverage is via §13.6.2's coarse-reading distinctness baseline: M-cycle-C is single-threaded (one cycle's M is a single append-only sequence), so any same-cycle rule-pair is intrinsically dependent on M-append-order — reordering the pair produces a different M-cycle-C sequence, and the resulting derived views (PendingTheta, MootedIntentions, LiveIntentions, DeclaredIntentions) are sequence-sensitive at their points of read. R-moot-intention is covered the same way R-rr is covered post-2026-06-23: by the coarse single-threaded reading at §13.6.2, not by the fine `last`-coupling reading at §13.6.3 clause 3. **§13.6 verification list (§13.6.2) needs an R-moot-intention entry with `LastEffect = ⟨moot, C, g_k⟩` (literal, not operative — for distinctness-baseline accounting); §13.6.3 clause 3 is NOT invoked for R-moot-intention.** Empty-independence preserved by the coarse single-threading.

**Migration note (no prior R-moot-intention; clean addition; partial Axis 4 contribution, not closure).** This is a new rule, not a revision of an existing one. R-moot remains in place for whole-cycle moots (§11.6.6.1). The transparent-`last` convention (§11.6.6.2) is the lifecycle-wide semantics change that makes R-moot-intention's contractum non-blocking for live intentions' continuations *at the marker layer*. R-moot-intention itself (this §11.6.6.3) is a **marker-granularity contribution toward Axis 4** (Sarah T14/T15 intention-scoped moot), surfaced during the §1.4.5 state-fork derivation as a defect at the post-resume operator-attested R-moot state (row 126 of the state-fork table). It is **not** the Axis 4 closure — per the "Scope and consolidated-gap finding" subsection above, Axis 4's full closure requires the structural reframe (per-intention lifecycle-position tracking, option A) that also closes Axis 3b's second half and the post-resume R-execute continuation gap. This revision delivers the building blocks; the consolidated reframe is the project's next-thread direction.

**Propagation discipline (flagged for the post-review sweep, NOT executed in this revision; significantly re-scoped after user-review 2026-06-23)**. Per the standing-option principle established 2026-06-23 (memory: feedback-trace-claim-to-every-site refinement on premise-shape changes and standing-option pattern), R-moot-intention's admissibility is class-wide (at K ≥ 2 cycles), not localized — propagation should NOT enumerate "the new states where R-moot-intention can fire" but should state the standing-option principle once at §1.4.5 and let per-state rows record witnessed picks. Per the dissolution/relocation-keyed sweep rule (same memory), key the propagation on every surface form, including the post-review consolidation: "intention-scoped moot marker," "Axis 4 partially addressed via marker granularity," "Sarah T14 mooting Intention 2 while cycle closes on Intention 1 — blocked at T15 R-execute(γ_1) on positional-`last` inadequacy," "post-resume R-execute continuation gap," "multi-intention escalation positional-`last` inadequacy," "consolidated per-intention lifecycle-position-tracking gap." Sites identified pre-sweep, **revised post-user-review to remove overclaims**:

- **§1.4.5 state-fork table row 126** (post-resume operator-attested R-moot): was-defect → **still defect at the lifecycle-continuation layer**, but with marker-granularity contribution noted. Do NOT mark as "resolved." Add a cross-reference to §11.6.6.3's Scope subsection identifying this as one of three surface forms of the consolidated multi-intention escalation gap.
- **§1.4.5 standing-option principle paragraph**: add R-moot-intention as the second standing option alongside R-rr (at K ≥ 2 cycles); flag the K=1 structural exclusion.
- **§1.4.5 Summary**: **DO NOT recount fix-targets to two**. Retain three (Axis 4 still open), and add a new entry naming the consolidated underlying gap with Axis 4, Axis 3b second half, and post-resume R-execute continuation as its three surface forms. The §1.4.5 narrative gains structure (consolidation under one underlying gap), not a count transition.
- **§11.1 / §11.4 / §11.6 prelude**: cross-reference §11.6.6.2 operative-`last` convention at every `last`-read definition. (This building-block lands cleanly.)
- **§11.4.6 PendingTheta definition**: add moot-exclusion clause. (Building-block lands cleanly.)
- **§13.5.2 inline per-cycle bound** (formerly old §13.5.6's bound): note R-moot-intention's K_C-1 contribution; bound remains finite.
- **§13.6.1 σ definition**: broaden to include R-moot-intention vs proceed (at K ≥ 2 cycles).
- **§13.6.2 verification list**: add R-moot-intention entry with `LastEffect = ⟨moot, C, g_k⟩` literal (NOT in §13.6.3 clause 3 — the symmetric-write argument fails under transparent-`last`).
- **§13.6.3 same-cycle-pairs proof**: re-verify the coarse-reading single-threaded-M argument extends to cover R-moot-intention; symmetric-write clause is NOT load-bearing for this rule. (Building-block lands cleanly.)
- **§13.5.9 thin pointer**: retain three fix-targets (Axis 4 not closed), AND add a new "consolidated underlying gap" entry naming per-intention lifecycle-position tracking as the next-thread direction with three cataloged surface forms.
- **§14.4 Sarah outcomes**: Axis 4 marker-granularity contribution noted; Sarah's §13.6 reproduction remains blocked at T15 R-execute(γ_1) pending the multi-intention escalation continuation gap's resolution (the consolidated reframe), not pending §11.4.8 body-resolution. **Correct the prior attribution.**
- **§14.1 Charles §13.6**: Sarah list — Axis 4 not closed; consolidated gap noted.
- **Prep-doc Section I axis-to-state mapping**: Axis 4 partially-addressed (marker granularity) + entry for the consolidated underlying gap.

Concept-keyed sweep with the standing-option principle stated once per the prior lesson, AND the consolidated-gap framing carried explicitly so a future reader cannot misattribute the remaining blocker to §11.4.8 body-resolution.

#### §11.6.7 R-abandon — principal abandons the cycle (**"any state" premise HELD per §13.5.9 forward-guard 2026-06-23 per Thread A reframe — do NOT tighten**; the universal premise is the load-bearing progress mechanism for the entire §13.5 termination theorem; tightening it to state-restrict R-abandon would re-open §13.5.5's progress proof (renumbered from old §13.5.3 under Thread A))

```
   last(M-cycle-C) = (any state from which the principal elects not to continue)
   ─────────────────────────────────────────  [R-abandon]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨parent-C-if-nested-else-C ; M ⊎ ⟨abandon, C⟩ ; S' ; R⟩
                          where:
                            (a) if S = []: S' = []; C is unchanged (the abandoned cycle was top-level; no parent to return to)
                            (b) if S = ⟨parent-C, _, _⟩ :: S'': S' = S''; C ← parent-C
                                (the abandoned cycle was a sub-cycle; pop *exactly one* S-entry,
                                 return control to the immediate parent, which may then itself
                                 R-spawn against a different target, R-moot, or R-abandon)
```

**Redex form.** No surface-syntax redex — R-abandon is the principal's deliberate exit from a cycle. Unlike R-moot (which fires when premise fails), R-abandon fires when the principal *chooses* to stop, regardless of premise. The most common reasons in the worked cases: the cost of continuing escalation exceeds the cycle's value (Rusty's escalation chain has a natural depth limit), or the principal's interest itself changes.

**Side conditions.** R unchanged; abandoned cycles produce no obtained resources. **S is popped *one* level when the abandoned cycle is nested**: a single S-entry is removed, control returns to the immediate parent, and the parent then decides its own next move (R-spawn against a different target — **a fresh g_k** (a new intention sub-index per R-intention's freshness, §11.4.5; same-g_k re-spawn is forbidden because two sub-cycles spawned from the same parent g_k would share the `parent-prefix/i.` address and collide at Theorem 13.1's (W) layer, so any "another attempt" is necessarily a new intention via R-intention rather than a same-g_k retry); R-moot — the parent's premise no longer holds; R-abandon — abandon the parent too, propagating the chain failure one level higher). The chain may then unwind level by level if each parent in turn elects to abandon, but each abandon is a separate decision, not an automatic cascade. If the abandoned cycle is top-level (S = []), no pop happens; the cycle is simply marked abandoned. **Tagging clause** (per §11.1): the `⟨abandon, C⟩` marker is tagged with the **abandoned** cycle (the pre-transition C, the cycle being abandoned — *not* the parent the active pointer transitions to). This makes the abandon event recoverable from the cycle's own filtered view of M (a future audit reads `last(M-cycle-C-abandoned)` and finds the abandon marker as the cycle's final entry, distinguishing it from a stuck configuration). The audit-trail entry is what makes the choice traceable.

**Worked-case validation.** **None of the dissertation's documented engagements formally abandon — Charles T5, Jim T6, Nathan T7–T11, Sarah T12–T15, Rusty T16–T22 all either complete (R-flowback) or moot (R-perceive-failure → R-moot).** R-abandon's specification is therefore *unvalidated by worked case*, and the single-level-pop discipline above is the specified behavior, not an empirically observed one. R-abandon exists so that the failure family is **total** — every cycle that does not flow back (success) or moot (premise fails) abandons (principal exits). Totality is a *coverage* property of the transition rules (every reachable non-terminal state in the failure family has an admissible exit rule; see §13.5.5's progress proof), not an algebraic-closure property. R-abandon's S-semantics should be treated as the spec's commitment, not a dissertation finding. A future worked case demonstrating R-abandon would validate or revise the single-level rule.

#### §11.6.8 End-to-end trace through Rusty Tables 16 → 17 → 18 (escalation case)

The Rusty escalation chain is the simplest two-level example. The parent cycle (Table 16) spawns one sub-cycle (Table 17) and then resumes (Table 18). S grows to depth 1, then contracts to 0.

| Step |                                                                                         Rule fired                                                                                         |           C            |                  S after                   |                                         M's new entry                                         |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|--------------------------------------------|-----------------------------------------------------------------------------------------------|
| 1–6  | Lifecycle rules 1–6 (R-open through R-required-resources)                                                                                                                                  | 1 (parent)             | []                                         | parent-cycle's open, ι, δ, ω, γ, θ entries (Table 16 lines 397–406)                           |
| 7    | **R-spawn** (gate fails)                                                                                                                                                                   | **2** (sub)            | `⟨1, [Α/i./o./g1/q1.], Α/i./o./g1/⟩ :: []` | `⟨gate-fail, [Α/i./o./g1/q1.]⟩` + `⟨open, 2⟩`                                                 |
| 8–18 | Lifecycle rules in sub-cycle (R-interest, R-detect, R-objective, R-intention, R-required-resources, R-gate, R-execute, R-perceive, R-select, R-outcome, R-obtained-utility — eleven rules) | 2                      | unchanged                                  | sub-cycle's substantive entries (Table 17 lines 418–429, all prefixed `Α/i./o./g1/i./...`)    |
| 19   | **R-close-nested**                                                                                                                                                                         | 2                      | unchanged                                  | `⟨close-nested, 2, 1⟩` + `[a.]Φ(Α/i./o./g1/i./O./Q.) := E_sub` + `⟨flowback-recorded, E_sub⟩` |
| 20   | **R-resume**                                                                                                                                                                               | **1** (back to parent) | `[]` (popped)                              | `⟨resume, 1, [Α/i./o./g1/q1.]⟩`                                                               |
| 21   | R-gate (re-fires on parent — post-resume trigger per §11.4.7 — now passes)                                                                                                                 | 1                      | []                                         | `⟨gate-pass, [Α/i./o./g1/q1.]⟩`                                                               |
| 22+  | Parent continues lifecycle R-execute → R-flowback (Table 18 onward)                                                                                                                        | 1                      | []                                         | parent's ε, Γ, Σ, Ω, Λ, close, Φ, flowback-recorded entries                                   |

The trace honors three properties:

1. **Persistence-invariant preservation throughout the escalation.** Every M' is M ⊎ new. The parent's θ-body from step 6 is still in M at step 21 when R-gate re-tests; no entry was rewritten. C transitions from 1 (parent) → 2 (sub-cycle) → 1 (back to parent) — the **active-cycle pointer** moves, but cycle identity 1 and cycle identity 2 are each preserved as the C-values at their open markers (§11.1).
2. **S-stack composes one level.** Push at step 7, pop at step 20. The parent's full configuration slice (parent-C=1, parent-pending-q, parent-prefix) is preserved exactly so R-resume restores the configuration as if the gate had never failed.
3. **R lands the q before the gate re-test.** R-close-nested writes `R ⊎ E_sub` at step 19 (before the resume at 20), and R-resume's premise `R ∋ parent-pending-q` is what guarantees the re-test can pass. If the sub-cycle had failed to obtain q (E_sub ∌ q), R-resume couldn't fire; the chain would either escalate further (R-spawn at step 20 against some deeper target) or abandon.

For deeper escalation chains, the same pattern composes: each R-spawn pushes one S-entry, each R-close-nested + R-resume pair pops one. A chain of N spawns produces an S-depth that rises to N and contracts back to 0 as the chain resolves. Rusty's full chain (Tables 16 → 17 → 18 → 19 → 20 → ... → 22) tests this composition over multiple re-escalations against Erik.

#### §11.6.9 What the failure family does not do

- **It does not retry top-level cycles.** A top-level cycle that moots or abandons is not re-opened automatically; the principal must initiate a new cycle (which becomes a fresh top-level cycle with its own C and own ι). The dissertation's "revise" pattern (Sarah T16 → revised objective in next cycle) is the analyst's choice across cycles, not a Layer-4 transition.
- **It does not handle non-deterministic escalation.** R-spawn always opens *one* sub-cycle per gate failure, with the missing q as the sub-cycle's interest. If the parent's gate fails because multiple required resources are missing, the principal must structure the parent's θ-body as one g_k per resource, and each gate failure spawns its own sub-cycle in sequence (or the principal abandons and re-plans). The system does not parallelize spawns.
- **It does not change the lifecycle's rule shapes for nested cycles.** R-interest through R-flowback (with R-close replaced by R-close-nested for sub-cycles) run identically at every stack depth. The only difference is the path-prefix carried by the S-entry, which sub-cycle operations prepend to their argument paths.

#### §11.6.10 R-open premise update (§11.4.1)

For the escalation logic to be unambiguous, R-open's trigger must now require `S = []` (otherwise R-open and R-resume could both fire from the post-flowback state of a sub-cycle, which would be a nondeterminism the failure family must avoid). R-open's premise becomes:

```
   (M = ∅ ∧ C = 0)  ∨  ((last(M) = ⟨flowback-recorded, _⟩)  ∧  S = [])
   ─────────────────────────────────────────  [R-open, updated]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C+1 ; M ⊎ ⟨open, C+1⟩ ; S ; R⟩
```

R-resume's premise `S = ⟨…⟩ :: S'` makes it complementary to R-open's `S = []`. One and only one fires from the post-flowback state, determined by S's emptiness.

#### §11.6.11 Depth-2 stress test (constructed example; empirical depth-2 match row-verified in §14.3.4 — Nathan T7–9)

**Correction record (Part IV Phase 0 finding F-1, confirmed by §14.5 Rusty walk).** A prior version of this section asserted that the depth-2 trace below was "validated against Rusty Tables 16–19." **That attribution is confirmed false by the completed §14.5 Rusty walk.** Rusty is depth-1 at every sub-cycle: g1/i./o./g., g2/i./o./g., g3/i./o./g. — three siblings under one parent, no second nesting level anywhere in T16–T22. Sarah Tables 13–14 are also depth-1 multi-spawn (Beth and Srini as siblings under one parent), not depth-2. **The Rusty-as-depth-2 framing was an inventory-style attribution carried since early drafting** ("Rusty is the deep escalation case") that survived because Rusty was traced first under that label and the depth question was not re-checked against the actual table structures. Part IV §14.5's row-by-row walk eliminated it directly. **Positive re-attribution to Nathan T7–9 as the empirical depth-2 case is now row-verified by the completed §14.3 Nathan walk (§14.3.4).** Nathan's Randy → Wanda → Mike chain is a genuine depth-2 nesting with pinning holding **literally** at both delivery points: Mike's Φ delivers `[Α/i./o./g2/i./o./g./q.]` = Wanda's parent-pending-q (Table 9), and Wanda's Φ delivers `[Α/i./o./g2/q.]` = Randy's parent-pending-q (Table 10) — both literal multiset matches, source-verified against Tables 7–11 (PDF pp.83–94). **The dissertation therefore has a source-verified depth-2 worked case**; the depth-induction in §13.5.4/§13.5.6 (well-foundedness + conclusion; formerly old §13.5.6's arbitrary-depth induction) / §13.4.3 now has an empirical base case at depth 2, not only theoretical grounding. (Depth-≥3 remains constructed-only — Nathan bottoms out at depth 2 when Mike's gate passes; see the depth-≥3 paragraph below.)

**Status of the trace below.** The constructed-example trace remains in this section as a stress-test of the tagging discipline at depth 2 (active-pointer/identity split, three live cycle-tags interleaved in M, two suspended S-entries, two resume markers each landing as `last` in the right per-cycle view). **The empirical depth-2 match is now provided by the §14.3 Nathan walk (§14.3.4)** — Nathan's Randy → Wanda → Mike chain is the source-verified depth-2 case, with pinning literal at both depths. The constructed trace is retained because its abstract tagging stress-test (three interleaved cycle-tags, two suspended S-entries, two resume markers each landing as `last` in the right per-cycle view) exercises the discipline independently of the Nathan rows. The character names below (Rusty / Erik / hypothetical Erik-CFO) are decorative carryover from the constructed example's original framing, predating the Nathan tracing; the structural pattern is what matters, and the row-verified instance lives in §14.3.

**Depth-≥3 remains empirically unvalidated.** Nathan's chain bottoms out at depth 2 (Mike succeeds; no depth-3 spawn). The depth-induction (now §13.5.2's depth-weighted μ + §13.5.4's lex well-foundedness; formerly old §13.5.6's arbitrary-depth induction) and §13.4.3 carry the discipline to arbitrary depth, but no worked case nests beyond depth 2.

**Scenario (constructed; structurally identical to the now-row-verified Nathan T7–9 depth-2 chain per §14.3.4).** Extend Rusty Table 17 hypothetically: suppose Erik, when Rusty approaches him for the requisition-policy authorization (T17's interest), does not have the authority alone — Erik would need to consult his own CFO. Erik's sub-cycle then itself hits a gate-failure on the missing authority, and Erik spawns *his* sub-cycle to recruit the CFO. Call the parent (Rusty-Todd) cycle 1, the Rusty-Erik sub-cycle cycle 2, and the hypothetical Erik-CFO sub-sub-cycle cycle 3. (This is structurally identical to Nathan T7–9's Randy → Wanda → Mike chain, which §14.3.4 has now walked row-by-row and confirmed as a genuine depth-2 nesting with literal pinning at both depths. The Rusty-framed character names are decorative carryover from the constructed example's original framing, kept here so the trace below reads continuously; nothing in the system-mechanical detail depends on the names, and the source-verified instance is Nathan's, not Rusty's.)

|  Step |                                         Rule fired                                         | Active C |                            S after                            |                             M's new entry (this step)                             | Cycle-tag |
|-------|--------------------------------------------------------------------------------------------|----------|---------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------|
| 1–6   | Parent lifecycle through θ                                                                 | 1        | []                                                            | parent's open, ι, δ, ω, γ, θ entries                                              | 1         |
| 7     | **R-spawn** (parent gate fails on q₁)                                                      | **2**    | `⟨1, q₁, Α/i./o./g1/⟩ :: []`                                  | `⟨gate-fail, q₁⟩` (tag: 1) + `⟨open, 2⟩` (tag: 2)                                 | 1 / 2     |
| 8–13  | Sub-cycle 1 lifecycle through θ (operations prefixed `Α/i./o./g1/i./...`)                  | 2        | `[⟨1, q₁, Α/i./o./g1/⟩]`                                      | sub-1's ι, δ, ω, γ, θ entries                                                     | 2         |
| 14    | **R-spawn** (sub-1 gate fails on q₂)                                                       | **3**    | `⟨2, q₂, Α/i./o./g1/i./o./g./⟩ :: ⟨1, q₁, Α/i./o./g1/⟩ :: []` | `⟨gate-fail, q₂⟩` (tag: 2) + `⟨open, 3⟩` (tag: 3)                                 | 2 / 3     |
| 15–25 | Sub-sub-cycle lifecycle (operations doubly prefixed `Α/i./o./g1/i./o./g./i./...`)          | 3        | unchanged (depth 2)                                           | sub-2's full eleven-rule substantive sequence                                     | 3         |
| 26    | **R-close-nested** (sub-2 close + flowback)                                                | 3        | unchanged                                                     | `⟨close-nested, 3, 2⟩` + Φ + flowback-recorded for sub-2                          | 3         |
| 27    | **R-resume** (pop one S-entry, back to sub-1)                                              | **2**    | `[⟨1, q₁, Α/i./o./g1/⟩]`                                      | `⟨resume, 2, q₂⟩` (tag: 2 — the **resumed parent** at this level, which is sub-1) | 2         |
| 28    | R-gate re-fires on sub-1 (post-resume trigger; now passes because R ∋ q₂)                  | 2        | unchanged                                                     | `⟨gate-pass, q₂⟩` (tag: 2)                                                        | 2         |
| 29–34 | Sub-1 continues lifecycle (R-execute, R-perceive, R-select, R-outcome, R-obtained-utility) | 2        | unchanged                                                     | sub-1's ε, Γ, select-staged, Ω, Λ entries                                         | 2         |
| 35    | **R-close-nested** (sub-1 close + flowback)                                                | 2        | unchanged                                                     | `⟨close-nested, 2, 1⟩` + Φ + flowback-recorded for sub-1                          | 2         |
| 36    | **R-resume** (pop second S-entry, back to parent)                                          | **1**    | `[]`                                                          | `⟨resume, 1, q₁⟩` (tag: 1 — the parent)                                           | 1         |
| 37    | R-gate re-fires on parent (post-resume trigger; passes because R ∋ q₁)                     | 1        | []                                                            | `⟨gate-pass, q₁⟩` (tag: 1)                                                        | 1         |
| 38+   | Parent continues lifecycle (R-execute → R-flowback)                                        | 1        | []                                                            | parent's ε, Γ, Σ, Ω, Λ, close, Φ, flowback-recorded entries                       | 1         |

**What the trace demonstrates at depth 2:**

1. **Three live cycle-tags interleave in M.** Between step 7 and step 36, M holds entries tagged 1, 2, and 3 in interleaved order. After step 36, cycles 2 and 3 are closed but their entries persist in M (append-only); cycle 1's entries continue accumulating. Each cycle's complete event history is recoverable by filtering M by tag.
2. **Two suspended S-entries hold simultaneously.** Between steps 14 and 26 (the sub-sub-cycle's full lifecycle), S has depth 2: the top entry is sub-1's suspension, the bottom is the parent's. They unwind in LIFO order (sub-1's entry pops at step 27, parent's at step 36).
3. **Two resume markers, each `last` in the right view.** Step 27 writes `⟨resume, 2, q₂⟩` tagged with cycle 2. At that moment, `last(M-cycle-2)` is exactly this resume marker — every entry written between sub-1's `⟨gate-fail, q₂⟩` (step 14, tag 2) and step 27 was tagged with 3 (the sub-sub-cycle's entries, steps 15–26), so cycle-2's filtered view skips them all and lands on the resume marker. Step 28's R-gate then matches its post-resume trigger. Step 36 writes `⟨resume, 1, q₁⟩` tagged with cycle 1; `last(M-cycle-1)` skips every cycle-2 and cycle-3 entry from steps 8 through 35 and lands on the resume marker (the parent's last own-tagged entry before resume was `⟨gate-fail, q₁⟩` at step 7). Step 37's R-gate matches.
4. **Active-pointer trajectory: 1 → 2 → 3 → 2 → 1.** The pointer descends twice and climbs back twice; cycle identities 1, 2, 3 are each preserved as the C-values at their respective open markers and don't get confused with the pointer's transitions. The C-pointer/identity split (§11.1) is what makes this distinction recoverable.

**No corrupted parent return.** Each resume lands `last(M-cycle-X)` on the right marker because the tagging clauses on R-spawn, R-resume, and R-abandon (§11.1, plus the per-rule statements at §11.6.2 / §11.6.4 / §11.6.7) ensure entries are tagged by semantic cycle-identity rather than by active-pointer-at-write-time. The composition at depth 2 is therefore a direct corollary of the tagging discipline holding at depth 1; no additional spec is needed to extend further. By induction on stack depth: if the discipline composes at depth N, it composes at depth N+1, since each additional R-spawn / R-resume pair adds one S-entry and one resume marker without introducing any new tagging case.

---

### §11.7 Non-destructive family — one transition rule plus two non-firing disciplines

The non-destructive family completes Layer 4 with **one transition rule** (R-objective-revise, the within-cycle same-path body revision validated against Sarah T14) and **two non-firing disciplines** (R-unfold, the directional substitution device §13's metatheory invokes when expanding a named body in a proof; R-prime-preserve, the prime-discipline invariant the three C-transitioning rules must satisfy). All three obey the persistence invariant (§7.5) by construction: every transition contractum is `M ⊎ (new entry)`, never a rewriting of prior entries; the two non-firing disciplines never modify M at all. The original ι declaration whose body is revised (R-objective-revise), the named declaration whose body is substituted in a proof (R-unfold), and the prime-sort of every designation in M (R-prime-preserve) are all preserved across the rule's firing or invocation. The non-destructive family is what makes the operation record's audit value mechanically immune to "improvement after the fact" — every revision is appended as its own event, dateable and reversible only in view (never in M).

The four sub-sections below specify each item; the closing sub-section names what the non-destructive family does not do. **Rule count after the §11.7 specifications: 14 lifecycle transitions (§11.4) + 6 failure-family transitions (§11.6) + 1 non-destructive transition (R-objective-revise) = 21 transition rules; plus R-unfold and R-prime-preserve as the two non-firing disciplines that the metatheory invokes.**

#### §11.7.1 R-unfold — directional substitution device (proof-level, not a transition)

```
   For a designation declared by some entry  [a.]X(p) := { body }  in M:
     name-form  [a.]X(p)  ↦  body-form  { body }     (directional)
   ─────────────────────────────────────────  [R-unfold (proof-level)]
   (no transition; this is the substitution discipline §13 invokes when expanding a named body in a proof)
```

**Form of the rule.** R-unfold is **not a separate transition rule**. The lifecycle and failure-family rules in §11.4 and §11.6 all read declared bodies **directly** through their `last(M-cycle-C) = X-body` premises — no rule substitutes a name for its body in a configuration. R-gate reads the q-designation straight out of θ's body's RHS; R-execute reads the cost from the same q in M; R-resume reads the parent-pending-q from the S-entry. None of these is an unfold. There is therefore no firing site in the operational semantics for R-unfold as a configuration-transitioning rule, and §11 does not provide one.

**Why R-unfold is named at Layer 4 anyway.** §10.6 pair 7's discussion specifically protected Layer 3's equational congruence from silent name-to-body substitution — equational reasoning cannot swap `θ(name)` for `{body}` without a directional record. The discussion deferred the substitution to Layer 4 with the proviso that if such a substitution is ever introduced, it lives here and is one-way. The lifecycle as drafted never invokes it, but §13 proofs that expand a named ≡-defined body for evaluation cite the substitution discipline as R-unfold. The directional property (no fold-back) is what makes the discipline compatible with the persistence invariant; that property is what gets named here.

**Side conditions on the substitution discipline.** When §13 invokes R-unfold in a proof: (i) the substitution is one-way — proofs cannot fold an unfolded body back into the name without re-introducing the directional record; (ii) the original `[a.]X(p) := { body }` entry persists in M; the proof's substitution does not modify M, only the proof's local view of a designation; (iii) proofs that cite R-unfold must reference the entry-in-M that establishes the name-to-body binding, so the proof's substitution is grounded in an actual M-entry rather than asserted.

**No worked-case validation; no §13 invocation either (correction).** R-unfold has no dissertation row because it is not a transition; the dissertation's worked cases all run transitions, not metatheory proofs. The prior expectation that R-unfold's substitution discipline would first be invoked in a uniqueness-of-derivation proof at §13 has been **retracted** — §13.6's correction-round per-discipline check verified that none of §13's six theorems reasons over `≡_named` (see §13.5.9 Gap-§11.7-non-firing-disciplines and §13.6.5's retraction). R-unfold is **reserved for future `≡_named` work** (LSPI extensions with named sub-procedures, applications that decide cycle-description equivalence modulo named-unfolding, etc.). The present section names it and fixes its directional property as a standing discipline; no §13 theorem currently invokes it.

#### §11.7.2 R-objective-revise — within-cycle same-path body revision (cycle-shared; IntentionPosition preserved across the revision 2026-06-23 per Thread A reframe — §A6.4 preservation FORCED by §7.5 append-only + WF-1 global K_C cap; no IntentionPosition substrate change to the rule's premise; the preservation claim is what soundness rests on, written out explicitly below)

```
   M-cycle-C contains ([a.]ι(Α/i.) := { original-body })  (the original ι entry)
   (operator-attested side condition: a detection update warrants revising ι's body)
   [a.]ι(Α/i.) := { new-body }  is well-typed at Layer 2, with the **same** argument path as the original
   ─────────────────────────────────────────  [R-objective-revise]
   ⟨C ; M ; S ; R⟩  ⟶  ⟨C ; M ⊎ ⟨objective-revised, C, ι, original-body ↦ new-body⟩ ⊎ ([a.]ι(Α/i.) := { new-body }) ; S ; R⟩
```

**Redex form.** R-objective-revise is **scoped to same-path body revision**: the rule revises the body of an existing declaration at the same argument path `p`. The contractum is two entries in one step: a structural marker `⟨objective-revised, C, ι, original ↦ new⟩` that records what was revised and how, followed by the revised ι declaration. Both are tagged with the current cycle C (per §11.1's per-rule tagging — no C-transition here). The original ι entry is preserved in M; both versions coexist in M-cycle-C's filtered view, distinguishable by their position relative to the `objective-revised` marker.

**Scope: ι-body revision only.** The rule covers same-path revision of the **interest** declaration ι, which is the within-cycle revision pattern the dissertation actually exhibits (Sarah Table 14). The rule does **not** cover:

- **Intention addition** (adding a new γ at a fresh g_k after R-execute or R-perceive-failure): this is **R-intention firing again** with its expanded premise (§11.4.5), not R-objective-revise. The Rusty Table 20 line 473 case (adding γ₃ after Intention 2's perception fails) is R-intention's normal firing under the relaxed "one or more γ per cycle" discipline — there is no original γ-body being revised, just a new γ being added at a fresh path.
- **Cross-cycle revision** (analyst initiates a fresh top-level cycle after a moot): per §11.6.9, this is R-open at a new C with a new ι, not R-objective-revise. R-objective-revise covers the *within-cycle* case only.
- **ω-body or γ-body revision at the same path**: not exhibited in the dissertation, so not specified here. If a future worked case shows ω or γ being revised at the same path, the rule's `ι` can be generalized to `X ∈ {ι, ω, γ}` and the rule re-validated.

**Side conditions.** C, S, R unchanged. R-objective-revise is **non-destructive by construction**: M is append-only, so the original ι declaration cannot be removed. Downstream rules that read the cycle's "current" ι must use the **most recent** ι entry that precedes their own firing position — typically `last(M-cycle-C filtered to ι-bodies)` rather than the absolute `last(M-cycle-C)`. This is a small but real burden on downstream rule designers; the alternative (allowing M-overwrite) would break the persistence invariant, which §7.5 and §10's R-unfold guardrail both forbid.

**Worked-case validation.** Sarah Table 14, lines 359 → 361. Sarah's sub-cycle starts with `[a.]ι(Α/i./o./g2/i.) := { [Α/i./o./g2/q.] }` (interest: "obtain information about Srini"), then after detection (line 360 reframes the situation) writes `[a.]ι(Α/i./o./g2/i.) := { [Α/i./o./g2/i./Q.] }` (revised interest: "obtain Srini's agreement not to compete"). Both ι entries share the argument path `Α/i./o./g2/i.`; the body designation changes. R-objective-revise fires between these two rows, writing the `⟨objective-revised, C, ι, [Α/i./o./g2/q.] ↦ [Α/i./o./g2/i./Q.]⟩` marker and the new ι declaration. Both ι entries persist in M; a reviewer can see Sarah's mid-cycle reinterpretation explicitly in the audit trail. The sub-cycle then proceeds with the revised interest as its operative ι.

**IntentionPosition preservation across the revision (per Thread A reframe + §A6.4; the soundness surface — argument revised post-Batch-5-review to use shape-based mechanism per §11.1's tightened recognizer).** R-objective-revise's contractum appends exactly two entries: the `⟨objective-revised, C, ι, original-body ↦ new-body⟩` structural marker and the new ι declaration `[a.]ι(p) := { new-body }` at the same argument path `p` as the original. **Neither entry's shape is in the position-bearing set defined at §11.1** (the nine shapes are γ-decl, θ-decl, ⟨gate-pass⟩, ⟨gate-fail⟩, ⟨resume⟩, ε_k-body, ⟨perceive, g_k⟩, ⟨perceive-failure, g_k⟩, ⟨moot, C, g_k⟩); `⟨objective-revised, ...⟩` is a cycle-scoped structural marker, and ι-body is a cycle-prologue declaration. **Both are explicitly excluded from IntentionPosition's fold** per the §11.1 "non-position-bearing entries" enumeration. Therefore, for every previously-declared g_k in M-cycle-C:

```
   IntentionPosition(M-cycle-C, g_k)  is unchanged by R-objective-revise's firing
```

**Why the previous "no g_k anywhere in the contractum" argument was wrong (post-review correction).** A prior draft of this preservation claim grounded it on path/argument/body containment: "paths contain no g_k segment; arguments contain no g_k literal; bodies contain no g_k-tagged designations." This was **factually contradicted by the rule's own Sarah Table 14 validation directly above** — Sarah's revised sub-cycle ι at `[a.]ι(Α/i./o./g2/i.) := { [Α/i./o./g2/i./Q.] }` has both path AND body carrying `g2`. The argument needs to ground on **shape**, not path-content: ι-body (and ω-body, δ-body) may carry g_k path provenance at sub-cycle scope (the parent-prefix discipline of §11.6.2 propagates parent's g_k into every sub-cycle's path-prefix), but **shape determines whether IntentionPosition's fold reads the entry as position-bearing**, not path containment. The §11.1 recognizer tightening makes this explicit.

**Preservation is mechanical, given the §11.1 shape-based fold.** M is append-only (§7.5 — no prior position-bearing entry about g_k is rewritten or removed); the new entries' shapes are not in the position-bearing set (the fold skips them — they're invisible to IntentionPosition); therefore the "most-recent position-bearing entry about g_k" — and the LifecyclePosition the fold returns — is unchanged. **The preservation claim is not "preserved by design intent"; it is "preserved by mechanism — the rule cannot break it given §7.5 + §11.1's shape-based recognizer."**

**Soundness consequences (the user-flagged hardest-trace items):**

1. **No g_k is stranded by the revision.** Every previously-declared g_k continues its per-intention pass under the IntentionPosition it had at revision-time: a g_k at `gate-passed q_k` can still fire R-execute; a g_k at `executed` can still fire R-perceive or R-perceive-failure; a g_k at `θ-written` can still fire R-gate or R-spawn against parent-R's current state. The revision does NOT advance any g_k forward or roll any g_k back.

2. **Per-intention phase boundary holds through and after the revision** (per §11.1: `ω-body ∈ M-cycle-C ∧ ⟨select-staged⟩ ∉ M-cycle-C ∧ no terminal markers`). At revision-time, the pre-revision ω-body is in M (append-only — it persists); after R-detect re-fires on the new ι and R-objective re-fires on the new δ, an ADDITIONAL ω-body lands in M. Both ω-bodies persist (append-only). The boundary condition `ω-body ∈ M-cycle-C` reads "some ω-body present"; multiple ω-bodies don't break it. **The per-intention rules remain admissible throughout the revision.**

3. **K_C budget enforcement straddles passes correctly** (per §13.5.2's inline per-cycle bound under Reading B's global-cap interpretation; formerly old §13.5.4 Reading B). DeclaredIntentions cardinality is `|{g_k : γ(g_k) ∈ M-cycle-C}|` — a count over all γ entries in M-cycle-C, regardless of which lifecycle pass they were declared in. Previously-declared g_k's count against K_C; fresh g_k's declared post-revision via R-intention draw from the REMAINING budget (`K_C - |previously-declared|`). R-intention's freshness check `IntentionPosition(g_k) = undeclared` continues to forbid re-declaring previously-used g_k's (their IntentionPosition is something other than `undeclared`). **Budget exhaustion** (cap reached during a revision-induced new pass) forces R-moot or R-abandon per §11.6.6 / §11.6.7's standing admissibility — both available from any state.

4. **R-detect re-fires on the new ι via positional `last` match** (the lifecycle-reset semantics, per §13.5.2's per-cycle bound discussion of `(1+J_C)·PerCycleSkeleton`; formerly old §13.5.4). R-detect's premise reads `last(M-cycle-C) = ι-body`. R-objective-revise's contractum makes the new ι-body the new `last`. R-detect fires, writes a new δ-body. R-objective then fires on the new δ. R-intention then can declare fresh g_k's under the revised ι. **The cycle-prologue rules (R-detect, R-objective) re-firing is what processes the revision into a new per-intention pass**; the per-intention rules for previously-declared g_k's continue independently in parallel.

5. **Downstream "current ι" readers use most-recent-ι via filtered `last`**: any downstream rule that needs to know "what is the cycle's currently-operative interest?" reads `last(M-cycle-C filtered to ι-bodies)`, which after revision returns the new ι. This is the small-burden discipline noted in the Side conditions paragraph above; it persists unchanged under the reframe.

**What the preservation claim does NOT cover (out of scope for this rule).** The interaction of post-revision per-intention rules with pre-revision per-intention rules at distinct g_k's is governed by the I-classification (Phase 1 audit §A4) like any other multi-g_k interleaving — distinct-g_k pairs are I-independent under WF-6 with disjoint q-sets; same-g_k pairs are I-coupled; cardinality couplings still apply through F1/F3. R-objective-revise itself is **cycle-shared, not per-K**; it does not enter the I-classification's per-K independence relation directly — its couplings live at the cycle-shared layer (R-detect via positional `last`; PendingTheta indirectly via subsequent R-intention firings; no direct couplings to any specific g_k).

**Coupling structure (per Phase 1 audit §A4).**
- **Cycle-shared C/S/R unchanged**: R-objective-revise touches M only (two appends).
- **Sequential to R-detect**: R-detect's premise reads the new ι as `last(M-cycle-C)` immediately after R-objective-revise fires; the lifecycle-reset chain is R-objective-revise → R-detect → R-objective → R-intention(fresh g_k).
- **No per-K coupling**: R-objective-revise writes nothing g_k-tagged for any g_k; previously-declared g_k's IntentionPosition is preserved by mechanism (preservation paragraph above).
- **Indirect F1 coupling**: post-revision R-intention firings increment DeclaredIntentions cardinality, which couples to other R-intention firings at the K_C cap (per Phase 1 §A5.2). R-objective-revise itself doesn't touch F1; its downstream R-intention re-firing does.

#### §11.7.3 R-prime-preserve — prime-discipline invariant on C-transitioning rules

```
   On any C-transition (R-spawn, R-resume, R-abandon — §11.6.2 / §11.6.4 / §11.6.7):
     ∀ designation σ ∈ M tagged with any cycle X:
       prime-sort(σ) is preserved across the transition
   ─────────────────────────────────────────  [R-prime-preserve (invariant)]
   (no separate transition; this is an obligation the three C-transitioning rules satisfy)
```

**Form of the rule.** R-prime-preserve is **not a separate transition rule** in the sense that R-spawn or R-unfold are. It is a **persistence-invariant clause** the system asserts on R-spawn, R-resume, and R-abandon — the three rules that transition the active-cycle pointer. The clause states: for every designation σ stored in any M-entry, σ's prime-sort (whether σ is a primed `…′` form or an unprimed form, per C5 and §9.2's `primed-form(σ)` sort distinction) is preserved across the transition. Specifically: a designation that was primed in cycle X's view of M is still primed there after the transition; a designation that was unprimed in cycle X's view is still unprimed. The C-transition does not silently flip the prime-sort of any designation in M.

**Why this needs saying.** Sub-cycles inherit the parent's path-prefix at R-spawn (§11.6.2's `parent-prefix = base-prefix/o./g_k/`), and the parent's primed forms (in ω and γ bodies, which are *projected*) coexist in M with the sub-cycle's eventual realized forms (in Ω and Γ, which are *unprimed*). A careless implementation might "normalize" primed and unprimed forms together when interleaving cycle-tags, or might use the same designation symbol in primed and unprimed positions in different cycle-filtered views and conclude that "the same designation" is both primed and unprimed (a contradiction with §10's pair 6). R-prime-preserve forbids this: the C-transitioning rules treat prime-sort as data carried by each designation, not as a property of the active C. Charles T5 row 184's ω-body has `[Α/i./t./S./P.]′` (primed, projected); Charles T5 row 190's Ω-body has `[Α/i./t./S./P.]` (unprimed, realized). They coexist in M's cycle-1 view; neither flips into the other across any C-transition.

**Worked-case validation.** Rusty Tables 17–18 transition: the parent's ω (Table 16, projected, primed) and γ (Table 16, projected, primed) are present in M at the moment of R-resume from T17. The resume does not modify the prime-sort of these designations. When the parent then runs R-execute and writes ε (Table 18 line 438, realized, unprimed), the parent's M has both primed forms (from before suspension) and unprimed forms (after resumption) — both correctly prime-typed. No spec is needed beyond R-prime-preserve's invariant clause to make this work, because R-resume writes the resume marker without touching any earlier M-entry.

**The invariant in proof form.** §13 (theorems) will prove R-prime-preserve as a corollary of the persistence invariant: since no C-transitioning rule's contractum rewrites a prior M-entry, and since each entry's prime-sort is determined by its content (not by external state), prime-sort cannot change. R-prime-preserve is the named version of this corollary, called out because the prime-sort distinction is one of the system's two most important sort discriminations (the other is the agent-attribution prefix discipline of §9.4.1).

#### §11.7.4 What the non-destructive family does not do

- **It does not amend or replace earlier M-entries.** R-objective-revise *appends* a new declaration; the original is still in M. R-unfold *appends* an unfold marker; the named declaration is still in M. R-prime-preserve *prohibits* prime-sort flips; no rule it applies to writes a modified version of any earlier entry. Every non-destructive rule's contractum is `M ⊎ (new entry)` — the same shape as the lifecycle and failure-family rules.
- **It does not re-open closed cycles.** A closed cycle (whose last entry in its filtered view is `⟨close, C⟩` or `⟨close-nested, C, parent-C⟩`) cannot be revised, unfolded into, or re-entered. R-objective-revise fires only on open cycles. R-unfold's marker can reference designations from closed cycles for *reasoning purposes*, but no transition modifies a closed cycle's state.
- **It does not provide retry.** A moot or abandoned cycle stays moot or abandoned. The analyst's choice to "try again" with a revised plan is a fresh top-level R-open with new C and new ι, not a non-destructive operation on the old cycle.
- **It does not normalize across cycles.** Each cycle's filtered view of M is independent; non-destructive rules operating on cycle X do not affect cycle Y's filtered view (other than through the shared M-entries that pre-date the operation). The constructed depth-2 stress test (§11.6.11) shows three cycle-filtered views remaining coherent through stack unwind; the non-destructive family does not introduce any new cross-cycle interactions.

The non-destructive family completes Layer 4. The full operational semantics totals **twenty-one transition rules** (lifecycle: §11.4, fourteen rules; failure family: §11.6, six rules; non-destructive: §11.7, one rule — R-objective-revise) **plus two non-firing disciplines** (R-unfold and R-prime-preserve), all sharing the same configuration `⟨C ; M ; S ; R⟩`, the same prefix-admissibility discipline of §9.4.1, and the same persistence invariant of §7.5. Layer 4 closes here; Layer 5 (theorems, §13) is where the meta-properties — confluence of the equational congruence, subject reduction (type preservation under transitions), R-set monotonicity within a cycle, S-stack composition at arbitrary depth, and the uniqueness-of-derivation theorem (R-unfold's directional substitution discipline is reserved for `≡_named` reasoning and is not invoked by the uniqueness theorem — see §13.5.9 Gap-§11.7-non-firing) — are proved.

---

## §13 Layer 5 — Theorems (Meta-Properties of LSPI)

Layer 5 proves the meta-properties of LSPI: the structural guarantees that hold *about* the system rather than *within* it. Layers 1–4 specify what LSPI terms are and how they transform; Layer 5 proves that those specifications cohere — that the system does what its rule shapes claim it does. Six theorems are scheduled, each addressing one of the spec's load-bearing commitments. They are listed below in order; each is then drafted in its own sub-section. §13 is structured to be readable as either a sequential proof set (the order below is the order in which later theorems lean on earlier ones) or as a reference catalog (each sub-section is self-contained, citing earlier theorems by reference rather than re-proving them).

**Theorem inventory** (drafted in order; the first is the load-bearing one and is drafted here):

1. **Theorem 13.1 (Uniqueness within an actor's agenda tree).** For any actor A and any two well-formed paths in A's agenda, syntactic distinctness (modulo Layer 3 congruence) implies referent distinctness. Per-actor scope — the dissertation's Lam 2018 p.164 framing — is preserved exactly; uniqueness does **not** extend across actors, because paths in LSPI do not embed the actor identifier. **Drafted in §13.1.**
2. **Theorem 13.2 (Subject reduction — type preservation under transitions).** If a redex is well-typed at Layer 2 and a transition rule fires, the contractum is well-typed. **Drafted in §13.2; independent of Theorem 13.1** (the proof reasons about syntactic shape of M-entries, not constituents they reference).
3. **Theorem 13.3 (Congruence decidability).** The normalize-then-compare procedure of §10's For-AI-engines section decides Layer-3 congruence `≡` in time linear-expected (randomized hash-multiset representation) or O(n log n)-deterministic (sorted canonical-order representation) in term size — see §13.3.1's asymptotic statement. **Drafted in §13.3; independent of Theorems 13.1 and 13.2** (the proof reasons over syntactic congruence on §10's three generators alone).
4. **Theorem 13.4 (Resource conservation across nested cycles).** R deductions and accruals balance under R-execute's `cost(·)` and R-flowback / R-close-nested's `earnings(·)`; the R ∋ q resume guard plus the close-nested flowback discipline of §11.6.3 ensure no resource leaks or duplications across the escalation stack. **Drafted in §13.4; independent of Theorems 13.1 and 13.2** (the proof stays on the syntactic side of R-multiset arithmetic; both theorems' composites — actor-holdings-conservation via §13.1, well-typed-resource-conservation via §13.2 — are available but not consumed).
5. **Theorem 13.5 (Termination and S-stack composition).** Every well-formed LSPI transition sequence reaches a terminal configuration in finite steps (well-foundedness) and every reachable non-terminal configuration has an applicable rule (progress). Conditional on **four** well-formedness preconditions (bounded intentions/cycle, bounded revisions/cycle, bounded escalation depth/engagement, bounded top-level cycles/engagement) per the Layer-1 check that no mechanism caps operator discretion on these parameters. **Drafted in §13.5; independent of Theorems 13.1, 13.2, 13.3, and 13.4** (the proof reasons about transition-sequence length, rule applicability, and **integer** cycle identity — none of which requires constituent-identity bridging, type inspection, congruence decision, or resource arithmetic). Progress in the nested-moot case is supported by an **R-abandon-up branch always available**; a separate retry branch depends on a **§11.4.5 specification extension** the proof flags.
6. **Theorem 13.6 (Uniqueness of derivation).** Every well-formed transition sequence from a well-formed initial configuration, under a fixed operator-discretionary choice sequence σ, produces a terminal configuration that is **uniquely determined** — the "modulo permutation of independent steps" clause that traditionally accompanies uniqueness theorems is **vacuous in LSPI**: under correct accounting of the `last(M-cycle-C)` coupling (every lifecycle premise reads absolute `last`, every step writes a new `last`), the independence relation between same-cycle steps is empty, and cross-cycle steps are sequentially ordered by single-threaded C. **Drafted in §13.6; CONSUMES Theorem 13.5 only (termination is what gives the terminal configuration's existence; determinism — fixed σ + `last`-determined dispatch at every step — gives its uniqueness; together they give "deterministic transition terminates uniquely," without invoking Newman's lemma since empty independence means there are no local-confluence diamonds to promote); independent of Theorems 13.1, 13.2, 13.3, 13.4 (all composable; §13.1's bijection is invokable as a denotational gloss on the syntactic check but is mechanically removable).** This is the **corrected disposition** — the initial fine-reading draft constructed §13.1 consumption by phrasing independence denotationally; the trace-don't-inventory discipline applied to the draft's own proof body found the §13.1 invocation removable and the independence relation empty once `last`-coupling was accounted for. The series outcome: **§13.1 is composable across all six theorems**, the denotational anchor consumed mechanically by none; the **one** genuine cross-theorem consumption is §13.5 by §13.6 (termination → uniqueness). The alternative-readings analysis and the discipline's self-application that produced this correction are recorded in §13.6.2.

### §13.1 Uniqueness within an actor's agenda tree

This is the load-bearing theorem. Every subsequent theorem in §13 implicitly assumes path-to-constituent uniqueness within an actor's agenda; without it, those theorems would have to redo the path-disambiguation work each time they reasoned about constituents. The scope of the theorem — **per-actor, not global** — is also load-bearing: it is the scope the dissertation establishes (Lam 2018 p.164 frames uniqueness as "all agendas of a single actor"), and it is the scope LSPI's path notation actually supports (paths start with the agenda root `Α`, which is a per-actor symbol that does not carry an explicit actor index).

The earlier review rounds (§1.6 and §7.5.1) corrected an earlier over-claim of "globally unique" to "unique within an actor's agenda tree." §13.1 makes that scope formally precise and proves the corresponding theorem.

#### §13.1.1 Statement

**Theorem 13.1 (Uniqueness within an actor's agenda tree — bijection).** Let A be any actor. Let `Path(A)` denote the set of well-formed paths in A's agenda (paths constructed by §8.5 slash composition, well-typed at Layer 2 under §9.3.1's child-class lattice, rooted at A's agenda root `Α`), and let `Path(A)/≡` denote `Path(A)` quotiented by Layer 3 congruence. Let `Constituents(A)` denote the set of constituents in A's agenda tree. Define the address map `denote_A : Path(A)/≡ → Constituents(A)`.

The theorem asserts that `denote_A` is a **bijection**. Equivalently — and these are the three named halves the proof discharges:

- **(W) No-collision** (the dissertation's p.164 claim): distinct constituents have distinct addresses. Formally: `addr(c₁) ≡ addr(c₂)  ⟹  c₁ = c₂`. **This is the substantive half** — it asserts that the addressing scheme (slash composition + A7 ordinal discipline + cycle-prefix discipline) never assigns the same address to two genuinely distinct constituents.
- **(I) No-aliasing** (the injective direction): non-congruent addresses denote distinct constituents. Formally: `p₁ ≢ p₂  ⟹  denote_A(p₁) ≠ denote_A(p₂)`. Contrapositive: `denote_A(p₁) = denote_A(p₂)  ⟹  p₁ ≡ p₂`. **This is the near-definitional half** from tree structure: each constituent has exactly one root-path in its agenda tree, so two non-congruent paths reach different constituents.
- **Surjectivity**: every constituent in A's agenda tree is reachable by some path in `Path(A)`. Formally: `∀ c ∈ Constituents(A), ∃ p ∈ Path(A). denote_A(p) = c`. **This is the bridge** from (I) to (W): together with (I), surjectivity makes `denote_A` a bijection; together with (W), surjectivity makes `addr : Constituents(A) → Path(A)/≡` well-defined.

The three halves jointly establish the bijection. **The dissertation's "no constituents will ever share the same designation" (Lam 2018 p.164) is the (W) half explicitly**; (I) and surjectivity are the formal completion of the bijection. Earlier drafts of this theorem stated and proved only (I) while tacitly assuming (W) by writing `denote_A` as a function — the present version makes all three halves explicit and proves each.

#### §13.1.2 Why the scope is per-actor (paths do not embed actor identity)

The theorem holds *within* a single actor's agenda. For two actors A and A', a path p ∈ Path(A) and a path p' ∈ Path(A') that are syntactically identical (e.g., both literally `Α/i./t.`) do **not** denote the same constituent — they denote A's target and A''s target respectively. The agenda root `Α` is per-actor: it is a symbol that means "this actor's agenda" in context, but the symbol does not carry an explicit actor index. The actor context that disambiguates `Α` is **external to the path**.

This is why uniqueness cannot be lifted to global: there is no syntactic feature of the path that identifies the actor. The agent-attribution prefix on *operations* (§9.4.1's `[a.]δ(...)`, `[Α/i./t.]Γ(...)`, etc.) does carry actor context, but the prefix is on the operation form, not on the path inside the operation's argument. The path `Α/i./t./D./G.` inside any operation's parens is per-actor. Lifting the path to global uniqueness would require one of:

- **Per-actor agenda roots** like `Α_A`, `Α_A'`, ... (LSPI does not adopt this — it would multiply the root symbols across the dissertation corpus and break the equational congruence M4, which assumes a single `Α`).
- **Actor-prefixed paths** like `actor-A/Α/i./t.` (LSPI does not adopt this — actor prefixes apply to operations, not to paths).
- **External actor tagging** at the engagement level (a multi-actor LSPI analysis would tag each path's actor context outside the path notation; this is a use-case extension, not part of LSPI v1).

The dissertation's p.164 framing pre-dates any of these multi-actor extensions and is correctly scoped to a single actor. §13.1's theorem inherits that scope exactly.

#### §13.1.3 Proof

The proof discharges the three named halves of §13.1.1 separately. (I) and surjectivity together establish `denote_A` as a function with the right domain; (W) is the substantive content proved from the address-construction discipline.

##### §13.1.3.1 (W) No-collision — distinct constituents have distinct addresses

This is the dissertation's p.164 claim and the substantive half of the bijection. The proof argues from the **address-construction discipline** that the slash composition (§8.5) plus the ordinal designator (A7 from Part I §5; see also Lam 2018 p.164's "correct slash addressing and correct ordinal designation") enforces, with explicit ordinal-freshness premises at every sibling-generating rule.

**Claim.** Let c₁, c₂ ∈ Constituents(A) with c₁ ≠ c₂. Then `addr(c₁) ≢ addr(c₂)` (their addresses are non-congruent).

**The three discipline layers that force distinctness:**

**Layer 1 — Cycle-level discriminator (the iN discipline at the agenda root).** Every constituent in A's agenda tree belongs to some cycle of A's transition sequence. Each cycle's path-prefix is established at its R-interest or via its R-spawn-derived parent-prefix:

- **Top-level cycles** (S = [] at the cycle's R-interest firing): R-interest writes `[a.]ι(Α/iN) := { ... }` with fresh N per §11.4.2's iN discipline. The dissertation's surface form `Α/i.` is normalized by D-28 (§8.2.2) to `Α/i1` post-lexer, so every top-level interest is uniformly `Α/iN` after the lexer regardless of whether the source wrote sole-dot or numbered form. The actor-scoped freshness premise on R-interest (§11.4.2 side conditions) ensures different top-level cycles have **different interest-ordinals at the agenda root**: `Α/i1, Α/i2, …` per cycle. There is **no "first cycle sole-dot, subsequent numbered" mixed encoding** to special-case — A6/A9 forbid it and D-28 removes it before parsing.
- **Sub-cycles** (S ≠ [] at the cycle's R-interest firing): R-spawn pushes `parent-prefix = base-prefix/o./g_k/` per §11.6.2, and the sub-cycle's R-interest writes at `parent-prefix/i.` (sole-of-type within the inherited prefix, per A6). Distinct sub-cycles have distinct parent-prefixes because they were spawned from distinct parent `g_k`s (per layer 3's freshness for g_k); D-28 does not normalize sub-cycle sole-dot. Charles T5's interest reads post-D-28 as `Α/i1`; Rusty Table 17's sub-cycle inherits the parent's `Α/i1` (post-D-28) with `/o./g1/` appended, yielding the sub-cycle's path-prefix `Α/i1/o./g1/i./...`.

**Layer 2 — Sort-level discriminator (the §9.3.1 child-class lattice).** Within any parent constituent's admissible-child set, sort labels (`t.` target, `D.` matrix, `P.` preferred position, `X.` adverse alternative, `o.` objective, `g.` intention, `q.` required resource, `O.` outcome, `Q.` obtained resource, `U.` obtained utility, ...) are distinct. Two siblings of different sorts have distinct sort-segments in their addresses, hence distinct addresses at the divergence step.

**Layer 3 — Sibling-level discriminator (the A7 ordinal designator with per-rule freshness).** Where multiple siblings of the same sort exist under one parent, A7's ordinal designators (`X1`, `X2`, ..., `g1`, `g2`, ..., `P1`, `P2`, ..., `iN`) discriminate them. The ordinal is fresh per parent's same-sort sibling set — every sibling-generating transition rule carries an explicit freshness premise:

- **R-intention (§11.4.5)**: "g_k is a fresh intention sub-index in cycle C (no prior γ-entry in M-cycle-C uses this g_k)" — covers within-cycle g_k freshness.
- **R-detect (§11.4.3)**: "Xk indices within the body are pairwise distinct and fresh within the parent matrix's adverse-alternative set in M" — covers Xk freshness, and analogously Pk for multi-preferred-position cases (e.g., Rusty Table 16 line 402's `[Α/i./t./D./P2]`).
- **R-interest top-level (§11.4.2)**: "N is a fresh interest-ordinal in M (actor-scoped)" — covers iN at the agenda root.

These three freshness premises together cover **every sibling-generating sort in the lifecycle**. The remaining ordinal-bearing constituents (terminal-sort nodes like `q.`, `e.`, `Q.`, `U.`) either occur at most once per parent (no siblings to disambiguate) or inherit their parent's discriminator (e.g., g_k's q is at the parent g_k's path, so distinct g_k means distinct q-paths).

**Proof (positive case analysis).** Let c₁, c₂ ∈ Constituents(A) with c₁ ≠ c₂. Both have lineages from A's agenda root `Α` down to themselves. Since c₁ ≠ c₂, their lineages must diverge at some depth: let pₖ be the deepest common ancestor in the lineage (possibly the agenda root itself), and let x₁, x₂ be the next-level nodes (the (k+1)th path-segments) in c₁'s and c₂'s lineages respectively. The two are distinct (x₁ ≠ x₂) by the choice of pₖ as the *deepest* common ancestor. Three cases on the divergence:

- **Case W-1 (cycle-level divergence at the agenda root).** pₖ = Α (the divergence is at depth 0; c₁ and c₂ belong to different top-level cycles). Post-D-28 normalization (§8.2.2), every top-level interest is uniformly ordinal-numbered as `Α/iN`, so x₁ = `iN₁` and x₂ = `iN₂` with N₁ ≠ N₂ by layer 1's iN discipline plus R-interest's freshness premise. The address segments differ. (The dissertation's surface form `Α/i.` reads post-lexer as `Α/i1`, so the case W-1 reasons over uniformly-numbered interests with no sole-dot/numbered coexistence to special-case — the mixed encoding the previous draft considered is rejected by A6/A9 and removed by D-28.)
- **Case W-2 (sort-level divergence at any depth).** pₖ is some interior constituent; x₁ and x₂ are children of pₖ of different sorts. By layer 2's lattice, distinct sort-labels denote distinct child constituents of pₖ — the address segments differ at the sort.
- **Case W-3 (sibling-level divergence at any depth).** pₖ is some interior constituent; x₁ and x₂ are children of pₖ of the same sort but with different ordinals. By layer 3's freshness premise on whichever sibling-generating rule produced this sort (R-intention for g_k, R-detect for Xk/Pk, R-interest for iN), the ordinals are distinct — the address segments differ at the ordinal.

In all three cases, c₁'s and c₂'s addresses differ at the divergence step, hence the full address sequences are syntactically distinct. By the syntactic-to-congruence preliminary (§13.1.3.2: no Layer 3 generator — A2, D5, M4 — collapses distinct internal path-nodes or distinct ordinals), syntactic distinctness implies non-congruence. So `addr(c₁) ≢ addr(c₂)`. ∎

**Sub-cycle discriminator note.** Cases W-1 above assumed both cycles top-level. For cross-cycle divergence involving sub-cycles, the divergence appears at the deepest common ancestor in the lineage — which for two sub-cycles of different parent `g_k`s is at the parent's g-sort discriminator (a Case W-3 application of layer 3's freshness for g_k). **Two sub-cycles of the same parent g_k cannot arise** because **§11.4.5's fresh-g_k premise on R-intention is the mechanism** that forbids it: any re-attempt after a sub-cycle failure must declare a new γ at a fresh `g_k`, and the new sub-cycle then spawns under the fresh `g_k`'s `parent-prefix`. Both failure-cycle exit paths invoke this: **§11.6.6 R-moot** routes the parent to "escalate further (R-spawn against a fresh g_k per §11.4.5)," and **§11.6.7 R-abandon** routes the parent to "R-spawn against a different target — a fresh g_k per §11.4.5." Same-g_k re-spawn after either moot or abandon would share the `parent-prefix/i.` address and collide at this layer of (W); §11.4.5's freshness premise prevents that. The §11.6.11 depth-2 stress test exhibits the cross-cycle prefix-distinctness explicitly: cycle 1's prefix post-D-28 is `Α/i1`, cycle 2's prefix is `Α/i1/o./g1/i.`, cycle 3's prefix is `Α/i1/o./g1/i./o./g./i.` — three distinct prefixes, three distinct cycle scopes.

##### §13.1.3.2 (I) No-aliasing — non-congruent addresses denote distinct constituents

This is the injective direction, near-definitional from tree structure. The proof is by induction on path length.

**Claim.** For any p₁, p₂ ∈ Path(A), `p₁ ≢ p₂  ⟹  denote_A(p₁) ≠ denote_A(p₂)`.

**Proof.** By induction on path length, where path length is the number of slash-separated path-nodes after the agenda root `Α`.

**Compositional congruence preliminary.** Layer 3 congruence is closed under substitution into any context (§10.2 property 4 — congruence proper). For paths `q/x`, this means: if `q₁ ≡ q₂` and `x₁ ≡ x₂`, then `q₁/x₁ ≡ q₂/x₂`. Contrapositive: if `q₁/x₁ ≢ q₂/x₂`, then `q₁ ≢ q₂` OR `x₁ ≢ x₂`. This makes Cases 1 and 2 below exhaustive.

**Syntactic-to-congruence preliminary (for Case 2).** Distinct single path-nodes `x₁ ≠ x₂` are also non-congruent `x₁ ≢ x₂`, because no Layer 3 generator acts on a single path-node: A2 is about slash rebracketing (multi-node paths); D5 is about set ordering (not paths); M4 is about the root glyph (only Α/A, not internal nodes). So distinct sort-labels or distinct sub-indices are non-congruent.

**Base case (path length 0): the agenda root.** The only path of length 0 in `Path(A)` is `Α`. Under M4, `A` and `Α` are normalized to the same root, so `A ≡ Α` — the only "distinct" length-0 strings are congruent. The base case is vacuous (no non-congruent length-0 pair exists), so the implication holds trivially.

**Inductive step (path length n+1, assuming the claim holds for all paths of length ≤ n).** Consider two paths p₁, p₂ ∈ Path(A) of length n+1 with p₁ ≢ p₂. Write p₁ = q₁ / x₁ and p₂ = q₂ / x₂. By the compositional-congruence preliminary, `q₁ ≢ q₂` OR `x₁ ≢ x₂`.

- **Case 1: q₁ ≢ q₂.** By the induction hypothesis, `denote_A(q₁) ≠ denote_A(q₂)`. Each constituent in A's agenda has its own admissible-children set per §9.3.1; two distinct parent constituents have disjoint child sub-trees. So `denote_A(q₁/x₁) ≠ denote_A(q₂/x₂)`.
- **Case 2: q₁ ≡ q₂ and x₁ ≢ x₂** (the alternative left after Case 1; by the syntactic-to-congruence preliminary, `x₁ ≢ x₂` ⟺ `x₁ ≠ x₂` for single path-nodes). Then p₁ and p₂ name two children of the same parent constituent π (where `denote_A(q₁) = denote_A(q₂) = π`). Two sub-cases:
  - **Case 2a: x₁ and x₂ are children of different sorts** (e.g., target `t.` vs outcome `O.` under interest `i.`). Distinct sort-labels denote distinct child constituents of π.
  - **Case 2b: x₁ and x₂ are children of the same sort but distinct sub-indices** (e.g., intention `g1` vs intention `g2` under objective `o.` under the same parent π). Per A7, distinct sub-indices under the same parent denote distinct sibling constituents.

In both sub-cases, `denote_A(p₁) ≠ denote_A(p₂)`. ∎

##### §13.1.3.3 Surjectivity — every constituent is reachable by some path

**Claim.** For every constituent c ∈ Constituents(A), there exists a path p ∈ Path(A) such that `denote_A(p) = c`.

**Proof.** By construction. The agenda tree of actor A is built up by the lifecycle and failure-family transition rules of §11; every constituent in A's agenda is introduced by some transition-rule firing that writes an operation-bearing declaration to M. Each such declaration includes the constituent's path:

- R-interest's body `[Α/i.]` (the interest constituent itself) — declares the path `Α/i.` for the interest constituent.
- R-detect's body `{ [Α/i./t.], [Α/i./t./D./P.], [Α/i./t./D./X1], ... }` — declares paths for target, preferred-position, adverse-alternatives.
- R-objective declares ω's body containing the projected Σ → P clause whose paths denote the objective and the projected selection/position.
- R-intention declares γ at path `Α/i./o./g_k`, plus the Γ inside γ's body at path `Α/i./t./D./G.`.
- R-required-resources declares θ at path `Α/i./o./g_k`, with body declaring `[Α/i./o./g_k/q.]`.
- ... and so on through R-execute, R-perceive, R-select (staged), R-outcome, R-obtained-utility, R-flowback.

Every operation rule's body either contains an explicit path designation for each constituent introduced, or the constituent is reachable by composing the operation's argument path with the body's sort marker (e.g., R-flowback's `Φ(Α/i./O./Q.) := E` makes the obtained-Q designations in E reachable as children of `Α/i./O./Q.`). The failure-family rules (R-spawn, R-resume, R-close-nested, etc.) do not introduce new constituents — they manage cycle transitions — so no constituents fall outside the lifecycle's declarations.

By induction on the transition sequence's length, every constituent in A's agenda tree has been introduced by some operation-rule firing, and the firing's body assigns it a path. Therefore every c ∈ Constituents(A) has at least one p ∈ Path(A) with `denote_A(p) = c`. ∎

##### §13.1.3.4 Bijection

(W), (I), and surjectivity together establish that `denote_A : Path(A)/≡ → Constituents(A)` is a bijection. (I) is the injectivity of `denote_A` (modulo `≡`); (W) is equivalent to the well-definedness of the inverse `addr : Constituents(A) → Path(A)/≡` (distinct constituents map to distinct paths); surjectivity is the surjectivity of `denote_A`. The bijection makes path = constituent in A's agenda tree the rigorous statement of the dissertation's "no constituents will ever share the same designation" (Lam 2018 p.164, the textual source for (W)).

∎

#### §13.1.4 Corollaries

**Corollary 13.1.1 (Two-actor non-interference).** For actors A ≠ A', no path p ∈ Path(A) "is the same constituent as" any path p' ∈ Path(A'), even if p and p' are syntactically identical. Constituents are per-actor; the actor context disambiguates.

*Proof.* By Theorem 13.1's scope: the theorem is stated per-actor, so cross-actor identification of constituents is outside its claim. Operationally: `denote_A` and `denote_{A'}` are distinct functions whose domains happen to share path-syntax but whose codomains are disjoint (A's agenda tree and A''s agenda tree are distinct objects). ∎

**Corollary 13.1.2 (Same-actor path identity).** For any actor A, no two syntactically distinct, non-congruent paths in `Path(A)` denote the same constituent.

*Proof.* Contrapositive of Theorem 13.1: if p₁ and p₂ denote the same constituent in A's agenda, then p₁ ≡ p₂. So distinct (modulo ≡) paths cannot share a referent. ∎

**Corollary 13.1.3 (Path-as-address discipline).** Within a single actor's transition sequence, every operation-form's path argument (the `(arg)` in `[prefix]op(arg)`) names a unique constituent. The address discipline is mechanical: a path-string is a constituent reference, and two distinct (non-congruent) path-strings in the same actor's M reference two distinct constituents.

*Proof.* Direct application of Theorem 13.1 to the path arguments of operation-bearing constituents (§8.5.1). ∎

#### §13.1.5 What Theorem 13.1 does not claim

- **It does not claim global uniqueness across actors.** Multi-actor LSPI analyses require external actor-tagging; the path notation alone does not support cross-actor reference disambiguation. The dissertation's framing is per-actor; LSPI honors that exactly.
- **It does not claim that path-strings serialize without ambiguity in a multi-actor system.** Serialization requires actor-context outside the path. A path written in isolation cannot be resolved without knowing which actor's agenda it belongs to.
- **It does not claim uniqueness of operation declarations.** Two operation declarations like `[a.]θ(Α/i./o./g1) := { ... }` can appear at different cycle-positions in the same actor's M for the same g1 (e.g., once initially, once after R-objective-revise rewrites a sibling ι, with θ's entry persisting unchanged — though R-objective-revise as currently scoped only revises ι, not θ). Operation-declaration uniqueness is a separate property and is not what Theorem 13.1 claims.
- **It does not claim path-uniqueness across transition time.** A path like `Α/i./o./g1/q.` references the same constituent at all transition steps in A's sequence, but the *q-designation it names* may have different obtained values across cycles (the actor may earn q at one cycle and consume q at another). Path identity is structural; designation content evolves through M.

#### §13.1.6 Implications

**For single-actor analyses (the dissertation's canonical use case).** Theorem 13.1 says path = constituent. An analyst working within a single actor's agenda tree can trust that `Α/i./t./D./P.` always refers to the same preferred-position constituent across the cycle's transition sequence. The path is a stable address; reasoning about that constituent's properties across transitions is sound.

**For multi-actor analyses (extensions beyond the dissertation).** The analyst must tag each path with its actor context externally. Syntactic path equality alone does not establish cross-actor reference; the actor disambiguates. This is a use-case caveat, not a system limitation — LSPI was designed for single-actor analysis per the dissertation, and the per-actor scope reflects that design choice.

**For §13's subsequent theorems.** Theorems 13.2 through 13.6 will reason about LSPI terms in a single actor's transition sequence. Each such theorem implicitly cites Theorem 13.1 when it uses "the constituent denoted by path p" — without Theorem 13.1, each downstream theorem would have to re-prove path-to-constituent uniqueness. The load-bearing nature of Theorem 13.1 is exactly that: it is the foundational uniqueness claim that the rest of §13 builds on.

#### §13.1.7 Dissertation citation

Lam 2018 p.164, verbatim (the textual source for the (W) no-collision claim and the per-actor scope):

> "...if done properly by using the correct slash addressing and correct ordinal designation when mapping all elements of all agendas of a single actor, **no constituents will ever share the same designation**."

Two load-bearing phrases in this passage: **"all agendas of a single actor"** establishes the per-actor scope, and **"no constituents will ever share the same designation"** is the (W) no-collision claim that Theorem 13.1's §13.1.3.1 sub-proof discharges. The dissertation also names the construction discipline ("correct slash addressing and correct ordinal designation"), which is what §8.5's slash composition and A7's ordinal designator (Part I §5) formally specify — the same discipline §13.1.3.1's proof argues from.

The scope-correction in §1.6 and §7.5.1 (changing an earlier LSPI over-claim of "globally unique" to "unique within an actor's agenda tree") brought the LSPI text into alignment with the dissertation's "all agendas of a single actor" framing. Theorem 13.1 is the formal proof obligation that scope-correction created: it proves the dissertation's exact (W) claim (no-collision) plus the two completing halves ((I) no-aliasing and surjectivity) that make `denote_A` a bijection.

---

### §13.2 Subject reduction (type preservation under transitions)

Theorem 13.2 is the second of §13's six theorems. The statement: every transition-rule firing preserves Layer 2 well-typedness — if the configuration before the firing is well-typed and the rule's premises are satisfied, the configuration after is well-typed. This is what makes the type system (§9) compatible with the transition relation (§11): the rules don't just match well-typed redexes, they produce well-typed contracta. Without type preservation, the type system would be a one-shot check at parse time with no guarantee that transitions preserve the property; with it, well-typedness is a stable invariant of the system.

#### §13.2.1 Statement

**Theorem 13.2 (Subject reduction — type preservation under transitions).** Let `⟨C ; M ; S ; R⟩` be a configuration in which every entry in M is well-typed at Layer 2 (per §9.3.1's lattice, §9.4's prefix-admissibility, §9.6's body-form typing, and §9.7's comparison/perception typing). Let R be any of the 21 transition rules of §11.4 and §11.6, and suppose R's premises are satisfied at the current configuration. If R fires, producing `⟨C' ; M' ; S' ; R'⟩`, then every entry in M' is well-typed at Layer 2.

In particular, M' = M ⊎ (new entries the rule appends), and the new entries are well-typed. Combined with M's pre-existing well-typedness (preserved because M is append-only — no entry is rewritten), every entry in M' is well-typed.

The C-pointer, S-stack, and R-multiset components are not themselves "typed" in the §9 sense (they are configuration metadata, not LSPI terms), but their transitions are constrained by the rules' premises and contractums; the proof confirms those transitions respect the §11.1 conventions (active-pointer monotonicity per identity, S-entry structure, R as a multiset of resource designations).

#### §13.2.2 Proof

**By a finite case enumeration over the 21 transition rules** (one case per rule). For each rule, identify the contractum (the new M-entry the rule appends), verify it is well-typed at Layer 2, and confirm the C/S/R transitions respect §11.1.

The proof is mostly mechanical because **every rule that has a surface redex pattern-matches on a form §8 admits and §9 types** (the "redex-discipline" property stated in §11.2 and re-asserted in every rule's worked-case validation across §11.4 and §11.6). The redex-less rules — R-open (§11.4.1), R-spawn (§11.6.2), R-moot (§11.6.6), R-abandon (§11.6.7) — have no surface redex and instead append only structural markers, which are typed by the marker convention below (untyped meta-entries in the §9 sense). For the rules that do have a surface redex, the rule's premise structurally guarantees the redex's typedness; the contractum's typedness then follows from either (i) the same typing rule that types the redex (when the contractum is a body-form of the same shape), (ii) §9's structural typing of the contractum's syntactic form (when the contractum is a fresh declaration), or (iii) trivially-typed structural-marker convention (when the contractum is a structural marker rather than an LSPI term).

**Independence from Theorem 13.1.** §13.2's claim is about *sort-inhabitation* — every M-entry inhabits a Layer-2 sort. This is independent of Theorem 13.1's path-uniqueness, which is about which constituents paths denote. §13.2 does not cite §13.1, deliberately: type preservation reasons about the syntactic shape of M-entries, not about the constituents they reference. The downstream theorems §13.3–§13.6 do reason about "the constituent denoted by path p" and therefore cite §13.1 as their path-uniqueness premise; §13.2 does not.

**Cases by rule family:**

**Lifecycle rules (§11.4, 14 cases).** For each rule, the contractum is either an operation declaration (typed per §9.4.3, §9.6.1, §9.6.2, or §9.7.4 depending on the operation) or a structural marker (untyped, see Marker convention below):

- **R-open (§11.4.1):** contractum is `⟨open, C+1⟩`, a structural marker. No Layer 2 typing required.
- **R-interest (§11.4.2):** contractum is `[a.]ι(Α/iN) := { [Α/iN/Q.] }` (top-level, post-D-28) or `[a.]ι(parent-prefix/i.) := { parent-pending-q }` (sub-cycle, per §11.4.2's sub-cycle branch). Both are attribution-forms per §9.6.2; both satisfy §9.4.1's prefix-admissibility (ι actor-prefixed). The top-level body's path `[Α/iN/Q.]` is well-typed per §9.3.1's lattice (interest with Q child). The sub-cycle body's `parent-pending-q` = `[Α/i./o./g_k/q.]` is well-typed per §9.3.1 (intention-with-q-child — `q` is a child of the intention `g_k`, not of the objective `o.`, per §11.4.6's θ-declaration path); it is read from the top S-entry, which holds the parent's gated q-designation (typed at S-stack push per §11.6.2), so the sub-cycle's ι body inherits the parent's already-well-typed designation rather than constructing a new path requiring its own typing derivation.
- **R-detect (§11.4.3):** contractum is `[a.]δ(Α/i./d.) := { [Α/i./t.], [Α/i./t./D./P.], [Α/i./t./D./Xk], ... }`. δ-body is an attribution-form per §9.6.2 with the body's members all constituent-designations of varying terminal sort (target, preferred-position, adverse-alternatives — unified at `constituent-designation` per §9.6.2). The Xk freshness premise (§11.4.3) ensures each Xk is a valid distinct designation per A7 / §9.3.1.
- **R-objective (§11.4.4):** contractum is `[a.]ω(Α/i./o.) ≡ { [Α/i./t.]Σ(Α/i./t./D.)′ → [Α/i./t./S./P.]′ }` — equivalence-form per §9.6.1 with a projection-clause body. The body's Σ is target-prefixed (admissible per §9.4.1), primed (sort `primed-form(σ)` per §9.2); the arrow's RHS is a primed designation per **§9.5.2's projection-clause typing** (C7b — the projection sense of `→` used inside ω's primed equivalence body, distinct from the effect-form arrow of §9.5.1/C7a used by R-execute).
- **R-intention (§11.4.5):** contractum is `[a.]γ(Α/i./o./g_k) ≡ { [Α/i./t.]Γ(...)′ = { ... } }` — equivalence-form per §9.6.1 with a perception-evaluation body. The inner Γ is target-prefixed (admissible per §9.4.1) and primed; the comparison's operands are primed utilities, admitted by §9.7.2's `⟨cmp-operand⟩` rule.
- **R-required-resources (§11.4.6):** contractum is `[a.]θ(Α/i./o./g_k) := { [Α/i./o./g_k/q.] }` — attribution-form per §9.6.2 with a single required-resource designation in the body. Well-typed by the same template as δ-body.
- **R-gate (§11.4.7):** contractum is `⟨gate-pass, [Α/i./o./g_k/q.]⟩`, a structural marker carrying a designation as payload. The payload designation is well-typed (it is the q from the premise's matched θ-body). Marker itself untyped.
- **R-execute (§11.4.8):** contractum is `[a.]ε(Α/i./o./g_k/e.) → { … }` — the `→` is the **effect-form arrow** per **§9.5.1 (C7a, the effect-form/realized sense of →, distinct from §9.5.2's projection-clause sense used in ω's body)**; the body is an arithmetic-form set typed per **§8.4.4 / §9.7 (family D arithmetic)**, with operands either utility designations, cost designations, or required-resource designations.
- **R-perceive (§11.4.9):** contractum is `[Α/i./t.]Γ(Α/i./t./D./G.) = { [Α/i./t./D./P./u.] > [Α/i./t./D./X./u.] }` — perception-evaluation per §9.7.4 (outer `=` typing) with target-prefix (admissible per §9.4.1). The comparison-set body is well-typed per §9.7.2 (`>` over realized utility designations).
- **R-select (§11.4.10):** contractum is `⟨select-staged, σ⟩` where σ = `[Α/i./t.]Σ(Α/i./t./D.) → [Α/i./t./S./P.]` (an unprimed projection-clause). The σ-clause is well-typed per **§9.5.2/C7b** (projection-clause typing, which admits primed-or-unprimed operands and explicitly notes that projection-clauses "appear inside `⟨set⟩` or as the body of an `≡`" per §8.9); Σ is target-prefixed (admissible per §9.4.1). At R-select's firing, σ is wrapped as the payload of the `⟨select-staged, σ⟩` marker — not yet inside an `≡`-body — so the marker convention (untyped meta-entry) carries σ until R-outcome folds it into Ω's `≡`-body. R-outcome's typing then places σ legally inside `Ω(...) ≡ { σ }` per §8.9, satisfying the "projection-clause inside an equivalence body" admissibility (see R-outcome below for the legal-placement step).
- **R-outcome (§11.4.11):** contractum is `Ω(Α/i./O.) ≡ { σ }` — equivalence-form per §9.6.1, Ω systemic (no prefix per §9.4.1), body the projection-clause σ inherited from R-select's staged marker. The σ is already well-typed by R-select's contractum; placing it inside an equivalence-body satisfies §8.9's "projection-clauses appear inside equivalence bodies" admissibility.
- **R-obtained-utility (§11.4.12):** contractum is `[Α/i./t.]Λ(Α/i./O./U.) := { [Α/i./t./D./P./u.] }` — attribution-form per §9.6.2, Λ target-prefixed (admissible per §9.4.1), argument terminating at `obtained-utility` sort, body declaring a realized utility designation.
- **R-close (§11.4.13):** contractum is `⟨close, C⟩`, a structural marker. Untyped.
- **R-flowback (§11.4.14):** contractum is two entries: `[a.]Φ(Α/i./O./Q.) := E` (attribution-form per §9.6.2 with obtained-resource designations in E) + `⟨flowback-recorded, E⟩` (structural marker). The Φ-declaration's well-typedness inherits from §9.4.3 (Φ typing rule) and §9.6.2 (attribution-form). The marker is untyped.

**Failure-family rules (§11.6, 6 cases).** Similar mechanical verification:

- **R-spawn (§11.6.2):** contractum is `⟨gate-fail, [base-prefix/o./g_k/q.]⟩` + `⟨open, C+1⟩`, both structural markers. The payload q-designation is the same q the premise's θ-body declared, already well-typed. Markers untyped; S-entry construction (`⟨parent-C, q, parent-prefix⟩`) is a configuration update, not an M-entry, but per §11.6.1's S-entry structure-discipline its fields are well-formed.
- **R-close-nested (§11.6.3):** contractum is three entries: `⟨close-nested, C, parent-C⟩` (marker) + `[a.]Φ(parent-prefix/i./O./Q.) := E` (attribution-form, same typing as R-flowback's Φ but with nested prefix) + `⟨flowback-recorded, E⟩` (marker). All well-typed by R-flowback's analysis with the parent-prefix substituting for Α/i.
- **R-resume (§11.6.4):** contractum is `⟨resume, parent-C, parent-pending-q⟩`, a structural marker. Untyped.
- **R-perceive-failure (§11.6.5):** contractum is two entries: a Γ-body (well-typed identically to R-perceive's contractum — same syntactic form, the rule difference is in the validation premise, not in the redex shape) + `⟨perceive-failure, C⟩` (structural marker, untyped).
- **R-moot (§11.6.6):** contractum is `⟨moot, C⟩`, a structural marker. Untyped.
- **R-abandon (§11.6.7):** contractum is `⟨abandon, C⟩`, a structural marker. Untyped.

**Non-destructive rule (§11.7, 1 case — R-objective-revise; R-unfold and R-prime-preserve are non-firing per §11.7.1 and §11.7.3 respectively, so they have no contractum to type).**

- **R-objective-revise (§11.7.2):** contractum is two entries: `⟨objective-revised, C, ι, original ↦ new⟩` (structural marker) + `[a.]ι(p) := { new-body }` (attribution-form, same typing template as R-interest with the revised body). The revised ι is well-typed by R-interest's analysis.

**Marker convention.** Structural markers (`⟨open, …⟩`, `⟨gate-pass, …⟩`, `⟨select-staged, …⟩`, `⟨close, …⟩`, `⟨close-nested, …⟩`, `⟨gate-fail, …⟩`, `⟨resume, …⟩`, `⟨perceive-failure, …⟩`, `⟨moot, …⟩`, `⟨abandon, …⟩`, `⟨flowback-recorded, …⟩`, `⟨objective-revised, …⟩`) are audit-trail meta-entries, not LSPI terms in the §8/§9 sense. They are not subject to Layer 2 typing; their payloads (when present) carry LSPI terms whose typing is verified separately as part of the rule that wrote the marker. The marker-vs-term distinction is what allows §8.9's "projection-clauses are not top-level terms" restriction to coexist with R-select's staging of a Σ → P clause as marker payload — the marker is a meta-entry, the staged clause is data inside the marker, and neither is a top-level term that §8.9 would reject.

**M's pre-existing well-typedness.** Since M is append-only (§7.5, §10's persistence invariant), no rule rewrites any existing M-entry. The entries in M before the rule fires remain in M' unchanged, so their well-typedness is preserved automatically. Only the new entries the rule appends need to be verified for well-typedness; the per-rule analysis above does this for each of the 21 rules.

**Configuration transitions (C, S, R).** Each rule's contractum specifies how C, S, R transition. The transitions respect §11.1's conventions:

- C either stays (lifecycle rules within a cycle), advances (R-open, R-spawn), or returns to a parent (R-resume, R-abandon for nested case). The per-rule tagging clause (§11.1) ensures M-entry cycle-tags are well-defined across transitions.
- S either stays (most rules), grows by one entry (R-spawn), or pops one entry (R-resume, R-abandon for nested case). S-entry structure is `⟨parent-C, parent-pending-q, parent-prefix⟩`, well-formed per §11.6.1.
- R either stays, shrinks (R-execute deducts cost via `⊖`), or grows (R-flowback / R-close-nested add earnings via `⊎`). R is a multiset of resource designations, all well-typed per §9.3.1.

∎

#### §13.2.3 Why this matters

Type preservation is the bridge that lets §9's parse-time typing assertions extend to transition-time invariants. Without Theorem 13.2, the type system would be a one-shot check: parse a term, verify it types, and then transitions could produce ill-typed configurations that the type system would no longer catch. With Theorem 13.2, well-typedness is a *stable* invariant of the system — every configuration reachable by transitions from a well-typed initial configuration is itself well-typed.

This matters operationally because:

- **The lifecycle rules' phase-ordering premises read M-entries by structural shape** (`last(M-cycle-C) = ι-body`, `M-cycle-C contains θ-body`, etc.). If transition produced ill-typed entries, these structural reads could match the wrong shape and the lifecycle could proceed on a malformed cycle. Type preservation rules this out.
- **The failure-family rules' premises pattern-match on markers and on the prefix-admissibility of inherited paths**. The marker shapes are structurally guaranteed; the path admissibility relies on type preservation to ensure that nested-cycle prefixes (`parent-prefix/...`) are themselves well-typed paths in the §9.3.1 lattice.
- **The §13 theorems that follow (13.3 through 13.6) all assume well-typed configurations as their starting condition.** Type preservation is what makes that assumption discharge-able to "every configuration reachable from a well-typed initial state is well-typed," rather than requiring each downstream theorem to re-verify typing at each transition step.

### §13.3 Congruence decidability

Theorem 13.3 is the third of §13's six theorems. The statement: the Layer-3 structural congruence relation `≡` on well-typed LSPI terms is decidable, and the §10.6 For-AI-engines normalize-then-compare procedure is a decision algorithm running in time linear in term size in the expected sense (under randomized hash-multiset representation of set bodies), or deterministically in O(n log n) under sorted canonical-order representation. The proof discharges three obligations the §10.6 procedure took on credit: soundness (the algorithm's "true" answer implies congruence), completeness (congruent inputs always yield "true"), and the asymptotic bound (with the representation caveat above). **The proof is independent of both Theorem 13.1 and Theorem 13.2** — a correction from the §13.2 inventory's anticipation that §13.3 would need path-uniqueness as a premise. Having drafted the proofs, none of §13.3.2/3/4 invokes the bijection: deciding the syntactic congruence requires only §10's three generators and the Layer-3 properties of equivalence-relations + congruence-under-context. §13.1 bridges syntactic `≡` to constituent-identity (its bijection makes `≡`-classes coincide with same-constituent classes within an actor's agenda), but §13.3's theorem statement asks only about the syntactic relation — no claim about constituent identity is made or needed. §13.1 first genuinely bites at §13.4 or §13.6, where transition steps quantify over "the constituent at path p" across the operation record; §13.3 stays on the term-shape side of that bridge.

#### §13.3.1 Statement

**Theorem 13.3 (Congruence decidability).** For any two well-typed LSPI terms `s, t`, the relation `s ≡ t` (Layer-3 structural congruence as defined in §10) is **decidable**. The decision algorithm is the normalize-then-compare procedure of §10.6's For-AI-engines section:

```
decide_congruence(s, t):
   s' = normalize(s)
   t' = normalize(t)
   return syntactic_equal(s', t')

normalize(term):
   apply A2 — re-bracket all slash compositions to a canonical bracketing (right-associative)
   apply M4 — normalize every Α/A character occurrence at any path-root position to Α
   apply D5 — canonicalize all set bodies (members in a fixed total order, or via hash-multiset
              representation; see §13.3.4 for the linear-time discipline)
   return normalized term
```

The procedure is **sound** (if it returns true, `s ≡ t`), **complete** (if `s ≡ t`, it returns true), and runs in time **O(n) expected** under the hash-multiset representation of set bodies (randomized hashing with collision resolution) or **O(n log n) deterministic worst-case** under the sorted canonical-order representation. The two representations are sound and complete in identical ways and produce the same `≡`-decision; they differ only in asymptotic guarantee strength — the hash representation gives faster expected time at the cost of randomization, the sorted representation gives a deterministic worst-case at the cost of a log factor. §13.3.4 argues both bounds; §10.6's For-AI-engines procedure can be implemented under either.

#### §13.3.2 Soundness

**Claim.** If `decide_congruence(s, t)` returns true, then `s ≡ t`.

**Proof.** Each generator (A2, D5, M4) is an instance of `≡` by definition (§10.1's three generators). So each individual normalization step preserves `≡` — that is, `s ≡ normalize(s)` and `t ≡ normalize(t)` for any inputs. If `syntactic_equal(s', t')` returns true (where `s' = normalize(s)` and `t' = normalize(t)`), then `s' = t'` as syntactic objects, hence `s' ≡ t'` (by reflexivity, which `≡` has as an equivalence relation per §10.2 property 1). Composing: `s ≡ s' = t' ≡ t`, so `s ≡ t` by transitivity (§10.2 property 3). ∎

#### §13.3.3 Completeness

**Claim.** If `s ≡ t`, then `decide_congruence(s, t)` returns true.

**Proof.** Five steps: three lemmas (i)–(iii) establishing the rewrite system's equational closure, confluence, and termination, chained via Church-Rosser (iv) and a final composition (v). Per-term uniqueness of normal forms is not by itself enough — two `≡`-equivalent terms could each have a unique but *different* normal form unless the rewrite system's equational closure is exactly `≡`. The Church-Rosser bridge is what makes "same `≡`-class ⟹ same normal form" go through.

**(i) The oriented generators' equational closure is exactly `≡`.** Treat A2, D5, M4 as oriented rewrite rules (each one-way: A2 right-associates slash compositions, D5 canonicalizes set members to a fixed order or hash-multiset, M4 maps Latin A to Greek Α). Their symmetric-transitive-reflexive closure `↔*` under context is the smallest equivalence relation closed under congruence that contains them — which is exactly `≡` by §10.1's definition (`≡` is the least congruence over {A2, D5, M4}). So `s ↔* t ⟺ s ≡ t`.

**(ii) The three generators are confluent.** Two parts: rule out inter-generator critical pairs, then handle intra-generator critical pairs rule by rule.

*Inter-generator critical pairs: none.* The three generators rewrite **three syntactically disjoint constructor categories**: A2 rewrites slash-composition nodes, D5 rewrites set-brace nodes, M4 rewrites the root glyph. A slash rewrite never creates or destroys a set-brace redex or a root-glyph redex; a set rewrite never creates or destroys a slash redex or a root-glyph redex; the root-glyph rewrite affects only Α/A at root positions, untouchable by the other two. So no inter-generator critical pair can arise.

*Intra-generator critical pairs: each generator individually locally confluent.* A2 (associativity) **does have intra-rule critical pairs** — associativity is the textbook confluent-but-not-orthogonal system, with self-overlaps like `((a/b)/c)/d`'s two overlapping outer-vs-inner redexes that rejoin at `a/(b/(c/d))`. These critical pairs are **joinable** (the standard associativity result: any two A2-rewrites of a single term reach a common normal form via finitely many further A2-rewrites). D5 and M4 are trivially locally confluent because their patterns are non-overlapping within their own categories (D5's set canonicalization commits to a single canonical order or hash-multiset, with no overlapping sub-set rewrites; M4 substitutes a character at a fixed root position, with no overlap on that position).

*Combine.* Inter-generator critical pairs are absent; intra-generator critical pairs are joinable for each generator. Hence the combined system is **locally confluent**. With termination from (iii) below, **Newman's lemma** gives confluence. The system is therefore confluent but **not orthogonal** (orthogonality would require zero critical pairs even intra-rule, which A2's associativity violates); the §8.2.2 confluence argument for the five lexer rules used the disjoint-categories logic as the route to confluence, but that argument applies *only* to the inter-rule analysis — §13.3.3's confluence of {A2, D5, M4} requires the additional intra-A2 joinability step that §8.2.2's lexer rules (none of which is an associativity-style self-overlapping rule) did not need.

**(iii) Termination.** Each generator is strongly normalizing on its own measure: A2's right-association rewrite strictly decreases left-bracketing count (a non-negative integer measure); M4 monotonically reduces Latin-A count; D5's set canonicalization terminates after one pass over each set body. **Joint termination follows from the disjoint-categories observation in (ii)**: because no generator rewrites a constructor category another generator's measure depends on, no generator can *increase* another's measure. So the sum measure `(left-bracketing count) + (Latin-A count) + (set-disorder count)` is a single non-negative integer that strictly decreases on every rewrite step, regardless of which generator fired. The combined system is therefore strongly normalizing on a single well-founded measure, not just on three independent ones.

**(iv) Church-Rosser.** Confluent (ii) + terminating (iii) ⟹ the rewrite system is **convergent** (Church-Rosser). For a convergent system, the **canonical form theorem** holds: `s ↔* t ⟺ nf(s) = nf(t)` syntactically, where `nf(·)` denotes the unique normal form reached by repeated application of the generators.

**(v) Compose (i) and (iv).** From (i), `s ≡ t ⟺ s ↔* t`. From (iv), `s ↔* t ⟺ nf(s) = nf(t)`. Composing: `s ≡ t ⟺ normalize(s) = normalize(t)` syntactically. So if `s ≡ t`, then `normalize(s) = normalize(t)`, and `syntactic_equal(s', t')` returns true. ∎

#### §13.3.4 Linear-time bound (argued from procedure structure, not asserted)

**Claim.** Under the hash-multiset representation of set bodies (randomized structural hashing with collision resolution), `decide_congruence(s, t)` runs in **O(n) expected** time where n = |s| + |t| (sum of token counts of the two inputs). Under the sorted canonical-order representation, the same algorithm runs in **O(n log n) deterministic worst-case** time. The two representations agree on what the canonical normal form is (a term-tree whose set-nodes are multisets); they differ only in how that canonical object is encoded — as a hash-multiset (O(n) expected, randomized) or as a sorted sequence (O(n log n) deterministic). §13.3.3's correctness proofs apply uniformly to both.

**Proof.** Decompose `decide_congruence` into its constituent operations and bound each:

- **A2 (slash re-bracketing) — O(n).** A single bottom-up tree traversal that re-associates every slash composition to right-associated form. Each path-node is visited once; the re-bracketing operation at each node is constant-time (swap two pointers). Total work: O(n).
- **M4 (Α/A normalization) — O(n).** A single pass that substitutes every Latin-A character at a path-root position with Greek-Α. Each character occurrence is examined once; the substitution is constant-time per occurrence. Total work: O(n).
- **D5 (set canonicalization) — O(n) expected under the hash-multiset representation.** Each set body's members are LSPI terms whose structural hashes are computable in O(member-size) bottom-up (Merkle-style: hash(term) = hash(constructor, hash(child₁), hash(child₂), ...)). Once all members have structural hashes, the set's canonical representation is the hash-multiset (mapping from hash-values to multiplicities), constructed in O(set-size) using counting over fixed-size hash slots. Multiset equality between two sets is then O(min(|S₁|, |S₂|)) — comparing two multiplicity maps. **Critically**: hashes for a term's subterms are computed once at the term's first traversal and reused for every set comparison the term participates in, so the total hashing work across the entire normalization is O(n), not O(n × number-of-set-comparisons). **The "expected" qualifier**: fixed-size structural hashes can collide, so a positive hash-equality test is not by itself a positive multiset-equality test — collision-resolution requires falling back to direct member comparison on hash-bucket matches. With well-randomized hashing, collisions are sparse and the expected total comparison work stays O(n); in the adversarial worst case (every hash collides) the bound degrades. So the O(n) bound here is **expected**, not deterministic. The deterministic guarantee is given by the sorted alternative below.
- **syntactic_equal — O(n).** Comparing two normalized terms for syntactic equality is a single parallel tree traversal: at each constructor node, check the constructors match and recurse on children. Each token contributes constant-time work. Total: O(n).

Composing the four bounds: A2 (O(n)) + M4 (O(n)) + D5 (O(n)) + syntactic_equal (O(n)) = **O(n)**.

**Without the hash-multiset representation** (e.g., if set canonicalization sorts members lexicographically by their normalized form), the D5 step becomes O(n log n) because sorting k items requires Θ(k log k) comparisons in the comparison-based model, and even though each comparison is amortized O(member-size) via shared subterm hashing, the total sorting work across all sets is O(n log n) in the worst case (one large set with n members at a single nesting level). The total then becomes O(n log n), dominated by sorting. The hash-multiset representation is what licenses the linear claim; sorted-set representations cost a log factor.

**Why the hash-multiset representation is available to LSPI.** LSPI's set bodies have well-defined member types (constituent designations, comparison-forms, projection-clauses — all per §9.6.2 and §9.7's typing rules), and the post-A2/post-M4 normalized form of each member is a finite tree of bounded constructor types. Structural hashing over a finite constructor alphabet is well-defined and gives a fixed-size hash per member. So the linear-time bound is achievable in any implementation that chooses the hash-multiset representation — it is not a forced cost, it is the implementer's choice. The §10.6 For-AI-engines procedure assumes this choice.

∎

#### §13.3.5 Independence from Theorem 13.1 (and Theorem 13.2)

§13.3 is **independent of both Theorem 13.1 and Theorem 13.2** — same clean independence §13.2 has, for a different reason. **This corrects a §13.2-inventory anticipation** that §13.3 would be the first downstream theorem to depend on §13.1's bijection. Having drafted §13.3's proofs, no step invokes the bijection: deciding the syntactic congruence `≡` requires only §10's three generators and the Layer-3 properties of equivalence-relations and congruence-under-context. Walking the proofs to confirm:

- **normalize (A2/D5/M4) — purely syntactic.** Each generator is a syntactic rewrite over LSPI's constructor categories (slash-composition nodes, set-brace nodes, root glyph). No claim about what paths denote is made or used.
- **syntactic_equal — token/tree comparison.** Two normalized terms are syntactically equal iff their constructor trees are pointwise equal. The comparison treats designation members of set bodies as syntactic objects (multiset comparison via hash or sort); two designation-occurrences `[Α/i./o./g_k/q.]` and `[Α/i./o./g_j/q.]` are syntactically equal iff `k = j` — a pure string comparison. No appeal to "what constituent does this path denote" is needed.
- **§13.3.2 soundness** — uses only §10.1 (the three generators) + §10.2 (reflexivity, symmetry, transitivity, congruence-under-context). No §13.1.
- **§13.3.3 completeness** — uses confluence + termination ⟹ Church-Rosser, applied to the rewrite system {A2, D5, M4} whose equational closure is `≡` by §10.1. No §13.1.
- **§13.3.4 complexity** — traversal and hashing bounds over term-shape. No §13.1.

**What §13.1 actually bridges**, and why §13.3 does not need it: §13.1's bijection makes `≡`-classes coincide with same-constituent classes within an actor's agenda. That bridge `(≡-class ⟷ constituent-identity)` is a **different claim** from `(≡ is decidable)`. §13.3 stays on the syntactic side of the bridge: it decides `≡` by reasoning about term-shapes, not about what those term-shapes denote. A reader who wants the *stronger* statement "constituent-identity within an actor's agenda is decidable in O(n) expected / O(n log n) deterministic" can compose §13.3 with §13.1 explicitly — `(s ≡ t)` decidable by §13.3, plus `(s ≡ t) ⟺ (denote_A(s) = denote_A(t))` from §13.1's bijection (applied to designations), yields `denote_A(s) = denote_A(t)` decidable in the same time bounds. §13.3 as stated does not need that composite claim; if a future use case (audit, replay, multi-actor comparison) needs the constituent-identity decider, the composite is what to state.

**Where §13.1 first genuinely bites in §13.** Likely §13.4 (resource conservation across nested cycles) and §13.6 (uniqueness of derivation), where transition steps quantify over "the constituent at path p" across the operation record M and the path-to-constituent identification matters. Those theorems will check explicitly when drafted; the §13.2 inventory's blanket "downstream theorems cite §13.1" attribution was correct for the *general intent* of the inventory but does not survive case-by-case scrutiny — §13.2 didn't need §13.1, §13.3 doesn't need §13.1, and §13.4/§13.5/§13.6 will be tested as drafted rather than assumed-dependent.

§13.3 also does not depend on §13.2 (type preservation): the decision algorithm operates on syntactic forms regardless of typing. Type-checking is a Layer 2 prerequisite for being asked about congruence (the theorem is stated over well-typed terms), but type-preservation under transition is irrelevant to deciding `≡` on already-given terms.

#### §13.3.6 Implications

- **Equational reasoning at Layer 3 is computationally tractable.** Decidability plus the linear-time bound means LSPI's congruence is not a metatheory-only notion — it can be invoked in real-time during AI-engine LSPI processing, in `≡_named` reasoning for future LSPI extensions that exercise §11.7.1 R-unfold (which expands named bodies and needs to verify equivalence with their original forms), and in any audit or replay over the operation record M. (Note: §13.6's corrected coarse reading establishes uniqueness as pointwise-identical transition sequences under fixed σ, with empty independence — no comparison of sequences modulo `≡` is performed there. See §13.6.5's retraction of the prior fine-reading claim.)
- **The §10.6 For-AI-engines procedure is now formally certified.** §10.6 stated the procedure and asserted its linear-time bound; §13.3 discharges both claims with the soundness, completeness, and asymptotic proofs above.
- **The procedure is deterministic.** Given inputs (s, t), the algorithm always produces the same output. This matters for audit reproducibility: a later replay can verify a past `≡`-decision by re-running the procedure on the same inputs and confirming the same output.
- **Implementer choice on representation.** The linear-time bound depends on the hash-multiset representation for set bodies; implementers who prefer sorted-set representations (perhaps for debugging or human-readability) pay an O(n log n) cost instead. Both representations are sound and complete; only the asymptotic differs.

### §13.4 Resource conservation across nested cycles

Theorem 13.4 is the fourth of §13's six theorems. The statement: the actor's R-multiset behaves conservatively across the entire transition sequence — every q removed from R is matched by a prior addition (no leaks), every Q added is added exactly once per sub-cycle completion (no duplications), and the R ∋ q resume guard correctly enforces the discipline that a parent cycle resumes only when the sub-cycle's flowback has supplied the q the parent needed. The proof is per-cycle conservation (within a single cycle, R-execute deducts cost and R-flowback / R-close-nested adds earnings, both logged in M) chained with cross-cycle conservation (across the escalation stack, R-close-nested transfers sub-cycle earnings to the parent's R, R-spawn/R-resume preserve R, and the S-stack's parent-pending-q binds the deduction-addition pair).

**Same disposition as §13.3 on dependency-walking**: I trace which premises each proof step consumes rather than inherit the inventory's attribution. **Critical framing fix**: the conservation invariant is a **multiset** claim, not a set claim — set notation (`∪`, `\`) cannot express conservation because set difference removes a designation entirely regardless of multiplicity, reporting zero where the answer is one. The earlier set-based framing (now corrected) silently relied on path-uniqueness across designations to make conservation sound — which would have smuggled in §13.1. The multiset framing (`⊎`, `⊖`) is what genuinely delivers §13.1-independence. **Result walked below**: §13.4 as stated about R-multiset arithmetic is **independent of §13.1 and §13.2**. A stronger composite statement ("the actor's holdings of *resources* are correctly tracked" — bridging designations to constituents) would compose §13.4 with §13.1's bijection; another composite ("R contains well-typed resource designations across transitions" — bridging arithmetic to typed semantics) would compose §13.4 with §13.2's type preservation. Both composites are available; neither is consumed inside §13.4's proofs.

#### §13.4.1 Statement

**Theorem 13.4 (Resource conservation across nested cycles).** Let R₀ be the actor's initial resource multiset at the start of the transition sequence. At any point T in the sequence, the configuration's R-component satisfies the multiset conservation invariant:

```
R(T) = R₀  ⊎  (⊎ all R-flowback additions in M before T)
            ⊎  (⊎ all R-close-nested additions in M before T)
            ⊖  (⊎ all R-execute deductions in M before T)
```

where `⊎` is multiset sum (additive: holding two units of a resource then gaining one yields three units) and `⊖` is multiset difference (subtractive: holding two units then spending one yields one unit, not zero). Equivalently, R(T) is uniquely determined by R₀ plus the audit trail of additions and deductions logged in M up to T, counting multiplicities. From this invariant follow two corollaries (proved as §13.4.4):

- **No leaks.** Every designation occurrence deducted from R via R-execute was either in R₀ or was added by a prior R-flowback / R-close-nested. No designation occurrence appears as a deduction without a matching prior addition (counting multiplicities).
- **No duplications.** Every R-flowback addition fires exactly once per top-level cycle's completion; every R-close-nested addition fires exactly once per sub-cycle's completion; **and at most one sub-cycle exists per parent gate failure** (per §11.4.5's fresh-g_k discipline cited from §11.6.6 / §11.6.7) so no two sub-cycles can both credit the parent's pending q. No earnings are double-counted.

#### §13.4.2 Per-cycle R conservation

**Claim.** Within a single cycle C, from R-open at C's open to R-flowback at C's flowback (or R-close-nested if C is a sub-cycle), R changes are exactly: one deduction at R-execute (of `cost([Α/i./o./g_k/q.])` where g_k is the cycle's gated intention's index) and one addition at R-flowback/R-close-nested (of E = earnings(cycle C)). Net change: R(after-flowback) = R(at-open) ⊖ cost(q_k) ⊎ E.

**Proof.** Within cycle C, the lifecycle rules that touch R are R-execute (deducts via `⊖`) and R-flowback (adds via `⊎`) for top-level cycles; R-execute (deducts) and R-close-nested (adds) for sub-cycles. R-open, R-interest, R-detect, R-objective, R-intention, R-required-resources, R-gate, R-perceive, R-select, R-outcome, R-obtained-utility, R-close: all leave R unchanged (their side conditions specify "R unchanged" explicitly per §11.4 / §11.6). So within cycle C, the only R-changes are the cost deduction at R-execute and the earnings addition at R-flowback or R-close-nested. By the append-only M discipline (§7.5, the Persistence Invariant), the cost and earnings are recoverable structurally from M: `cost(·)` reads the q-designation declared by θ at row R-required-resources (§11.1's notation conventions); `earnings(·)` returns E (per §11.1), the addition R-flowback writes into Φ's body at §11.4.14 (or R-close-nested writes into the nested Φ-body at §11.6.3 for sub-cycles), so E is **recorded** in Φ's body and **recoverable** from M by reading that body — corrected from an earlier draft that mis-sourced earnings to Ω's body (Ω holds the Σ→P selection projection-clause; the obtained-Q designations live in Φ). Both values (cost from θ's row, earnings via Φ's row) are deterministic, so R(after-flowback) is determined uniquely by R(at-open) and the entries M-cycle-C records. The per-cycle conservation invariant holds. ∎

#### §13.4.3 Cross-cycle R conservation (escalation stack)

**Claim.** Across the escalation stack, R is preserved correctly: R-spawn and R-resume do not modify R; R-close-nested transfers the sub-cycle's earnings to the parent's R; the parent's R when resumed = parent's R when suspended ⊎ (sub-cycle's net R change), where "net R change" denotes the multiset composition of the sub-cycle's R-execute deductions (`⊖`) and R-flowback/R-close-nested additions (`⊎`) across its lifecycle.

**Proof.** By induction on stack depth.

**Base case (depth 1 — single sub-cycle).** When R-spawn fires from a parent cycle, R is unchanged (§11.6.2 explicit). The sub-cycle then runs its lifecycle, modifying R per §13.4.2's per-cycle invariant. When R-close-nested fires (§11.6.3), the sub-cycle's earnings are added to R via `R ⊎ E`. When R-resume fires (§11.6.4), R is unchanged. So the parent's R at resume = parent's R at suspend (R-spawn) `⊎` (sub-cycle's deductions and additions across its lifecycle, ending with R-close-nested's addition). This is exactly the parent's R at suspend `⊎` (sub-cycle's net R change).

**The required-q ↔ earned-Q pinning** (the load-bearing step). R-resume's `R ∋ parent-pending-q` premise is **literal multiset membership** of the parent's required-q designation in R. For this premise to fire, R must contain exactly the designation `parent-pending-q` (the parent's gated `[Α/i./o./g_k/q.]` that triggered R-spawn). This works because **the sub-cycle's interest body is `{ parent-pending-q }` by R-interest's sub-cycle branch (§11.4.2)** — the sub-cycle's want IS the parent's literal q-designation, not a sub-cycle-rooted obtained-Q at a different path. On the normal path, the ι↔Φ identity (§11.1's normal-path property) holds, so the sub-cycle's Φ-body delivers exactly `parent-pending-q` as the obtained designation; R-close-nested's `R ⊎ E` then adds `parent-pending-q` to R; R-resume's premise fires by literal multiset membership; the parent's gate re-test (post-resume, per §11.4.7's second-trigger premise) reads `parent-pending-q` from the resume marker and tests `R ∋ parent-pending-q`, which passes by the same membership. **No constituent-identification step is needed** — the match is by literal path equality, which is what makes §13.4 independent of §13.1. Without this pinning (i.e., under an earlier draft where the sub-cycle's interest body was `{ [parent-prefix/i./Q.] }` at a different path), the resume guard would require a cross-path identification step that *would* invoke §13.1's constituent-identity bridge; the §11.4.2 sub-cycle body update keeps that bridge unnecessary.

**Inductive step (depth N+1 — nested sub-cycle).** Assume conservation holds at depth N. At depth N+1, a sub-cycle's own gate fails, R-spawn fires (R unchanged), the sub-sub-cycle runs (by IH, conservation holds for its R-changes), R-close-nested transfers sub-sub's earnings to R, R-resume returns control to the sub-cycle. The sub-cycle's R at resume = sub-cycle's R at suspend ⊎ (sub-sub-cycle's net R change). Combined with the per-cycle invariant for the sub-cycle's own changes, conservation holds at depth N+1.

By induction, conservation holds at arbitrary stack depth. The §11.6.11 depth-2 stress test exhibits this: cycle 1 (parent) → cycle 2 (sub) → cycle 3 (sub-sub), with R-changes at each level composing additively, no leaks, R returning to cycle 1's context with all gains preserved. ∎

#### §13.4.4 No leaks, no duplications

These follow directly from §13.4.2 and §13.4.3.

**No leaks.** For any deduction of `cost([Α/i./o./g_k/q.])` via R-execute in cycle C, the gate at C's gate-step (R-gate, §11.4.7) verified that `R ∋ [Α/i./o./g_k/q.]` before R-execute fired. So the deducted designation was in R (with positive multiplicity) at the time of deduction. By the per-cycle conservation invariant, the designation was either in R₀ or was added by a prior R-flowback / R-close-nested. Every deduction is matched by a prior addition or by R₀, counting multiplicities. ∎

**No duplications.** Two premises needed: (a) **firing-once per cycle** — each top-level cycle's R-flowback fires once per cycle's completion (after R-close, per §11.4.14's premise `last(M-cycle-C) = ⟨close, C⟩`); each sub-cycle's R-close-nested fires once per sub-cycle's completion (after the sub-cycle reaches Λ-body, per §11.6.3's premise). The premises ensure single-firing per cycle; the append-only M discipline ensures the firing is logged exactly once. (b) **At most one sub-cycle per parent gate failure** — this is **§11.4.5's fresh-g_k discipline**, cited from §11.6.6 R-moot's "escalate further (R-spawn against a fresh g_k)" and §11.6.7 R-abandon's "R-spawn against a different target — a fresh g_k." Without (b), a parent could spawn two sub-cycles for the same gated g_k; both could fire R-close-nested; both could credit `parent-pending-q` to R; the parent's R would gain two copies where the parent needs one — a duplication. The fresh-g_k premise prevents this by requiring any re-spawn to declare a new γ at a fresh `g_k` (via R-intention's freshness, §11.4.5), so the parent's M never holds two sub-cycles aimed at the same g_k. Combining (a) and (b): each earnings addition is added to R exactly once per parent need. ∎

#### §13.4.5 Independence from both Theorem 13.1 and Theorem 13.2 (with composites available)

Same disposition as §13.3: walk each proof step and check whether either earlier theorem is invoked. Applying the same scrutiny to **both** dependencies (the earlier draft asserted a §13.2 dependency without the same step-by-step trace it gave for §13.1 — the user-review caught this asymmetry).

**Step-by-step trace.**

- **§13.4.2 per-cycle conservation**: uses only R-multiset arithmetic (`⊎`, `⊖`), the per-rule R-change conventions (§11.4 / §11.6), and the structural reads `cost(·)` and `earnings(·)` per §11.1. `cost(·)` reads the q-designation at θ's body positionally and returns a token; `earnings(·)` reads the obtained-Q designations at Φ's body positionally and returns a multiset of tokens. Neither read **inspects a type** — they retrieve syntactic content at known positions. The multiset arithmetic balances tokens regardless of sort. **No constituent-identity claim; no type-inspection step.**
- **§13.4.3 cross-cycle conservation**: induction on stack depth; uses R-spawn/R-resume's "R unchanged" + R-close-nested's `R ⊎ E` + S-stack's parent-pending-q-binding. The R ∋ parent-pending-q resume guard is **literal multiset membership** of a designation token in R (enabled by the §11.4.2 sub-cycle interest-body pinning per §13.4.3's "required-q ↔ earned-Q pinning" paragraph). No constituent-identity claim; no type-inspection.
- **§13.4.4 no leaks / no duplications**: derived from the conservation invariant + R-gate's `R ∋ q` check + the firing-once premises (§11.4.14 / §11.6.3) + the fresh-g_k premise (§11.4.5). The premises cited are all syntactic/structural rule-conditions; no constituent identity or type-inspection invoked.

**Composites available, neither consumed.**

- **§13.1 composite** ("actor's holdings of *resources* are correctly tracked"): the conservation invariant tracks designation tokens in R. §13.1's bijection (path-uniqueness within an actor's agenda) gives "each designation denotes a unique constituent in the actor's holdings." Under that bridge, the multiset arithmetic conservation corresponds to "the actor's actual resource *holdings* are conserved" — a semantic claim about the actor's situation, not just about the R-multiset. §13.4 itself stays on the syntactic side; the composite is available by composing §13.4 with §13.1's bijection-on-designations.
- **§13.2 composite** ("R contains well-typed resource designations across transitions"): the per-cycle invariant positionally retrieves designations from θ-bodies (cost) and Φ-bodies (earnings) without inspecting their sorts. §13.2's type preservation guarantees that those designations remain well-typed across transitions, so under that bridge the composite "the actor's R holds well-typed resource designations whose conservation is tracked correctly" is available. §13.4 itself does not need the type-discipline grounding — the multiset arithmetic balances tokens regardless of sort — but the composite makes the typing-conservation claim explicit if a future use case needs it.

**Neither composite is consumed inside §13.4's proofs.** The earlier draft's "§13.4 depends on §13.2" claim was the same trap the §13.3 walkback resolved for §13.1 — instinct attribution rather than premise-tracing. The clean disposition: §13.4 is independent of both; either composite is available; neither is required.

#### §13.4.6 Implications

- **R-set bookkeeping is auditable from M alone.** At any point T, an auditor can compute R(T) by replaying M's R-affecting entries (R-execute deductions + R-flowback/R-close-nested additions, plus R₀). No external state is needed.
- **The R ∋ q resume guard is conservation's enforcement point.** R-resume's premise is what binds parent-pending-q (from S) to R's contents (from M). If the sub-cycle obtained the wrong q, R-resume cannot fire and the parent cycle does not resume — preventing a "fake success" where the sub-cycle completes but did not produce what the parent needed. The §11.6.4 design and §13.4.3's cross-cycle proof together establish this.
- **The single-spawn-per-g_k discipline (§11.4.5 freshness, cited from §11.6.6 / §11.6.7) prevents conservation violations.** Same-g_k re-spawn would create two sub-cycles with the same parent-prefix/i. address (a Theorem 13.1 (W) violation), but it would also create two competing Φ-bodies for the same parent g_k — a conservation violation, since the parent's gate test on parent-pending-q would not uniquely identify which sub-cycle's earnings to use. The §11.4.5 freshness premise prevents this at the addressing layer; §13.4.4's no-duplications result holds because of it.

### §13.5 Termination and S-stack composition

Theorem 13.5 is the fifth of §13's six theorems. The statement: under the well-formedness conditions WF-1 through WF-6 (Axis-6-resolved 2026-06-24, adding WF-6 bounded-q-per-intention with disjoint q-sets), every transition sequence from a well-formed initial configuration terminates in finitely many steps at a terminal configuration. The functional-q_of specialization (|q_of(g_k)| = 1 for every g_k, automatically satisfied by WF-6 with Q_max = 1) covers Charles K=1, Jim K=2, Nathan K=2 depth-2, Sarah K=2; the relational case (Q_max ≥ 2) covers Rusty K=3, source-verified at §14.5.1 with q_of pairwise disjoint across γ_k. Termination is **strong normalization plus progress**; both halves are load-bearing, and the proof discharges them separately before composing in §13.5.6.

**Thread A reframe (2026-06-24).** The depth-weighted lexicographic measure `μ : Reachable → ℕ × ℕ` (§13.5.2) supersedes the prior `(D − |S|, cycle_budget)` measure, which was unsound (the |S| component increased at R-resume; cycle_budget jumped across cycle switches). The new μ orders cycles by depth-weighted remaining budget summed across the stack, with `B = max-budget + 1` as the depth-base that makes parent firings strictly outweigh sub-cycle contributions. The Bucket-1/2/3 partition of co-admissible rule pairs (§13.6.5) and the per-K Embrace diamonds (Lemma 13.6.7) live downstream of this measure.

**The proof discharges six obligations, in the order each is needed by the next:**

1. **§13.5.1 Statement** — preconditions, scope (full corpus, post-Axis-6), and the WF-1 through WF-6 well-formedness conditions in detail.
2. **§13.5.2 Termination measure** — depth-weighted lex μ over ℕ × ℕ.
3. **§13.5.3 Per-step decrease** — every rule strictly decreases μ.
4. **§13.5.4 Well-foundedness** — μ ranges over ℕ × ℕ lex-ordered, hence SN.
5. **§13.5.5 Progress** — every reachable non-terminal state has an admissible rule (phase-by-phase enumeration; R-abandon as the explicit backstop, load-bearing only at the maximally-escalated single-intention resource-blocked gate).
6. **§13.5.6 Conclusion** — SN + Progress = Termination.

**§13.5.7** walks each step's premise consumption to confirm independence from Theorems 13.1, 13.2, 13.3, and 13.4 (preserved from the prior draft as historical record; the specific subsection references in §13.5.7's bullet list reflect the pre-Thread-A numbering and are kept verbatim for traceability). **§13.5.8** closes with what termination does and does not claim. **§13.5.9** catalogs §11 specification gaps surfaced by the §13 proof series.

#### §13.5.1 Statement

> **Theorem 13.5 (Termination over the full corpus, post-Axis-6 resolution).** Let `WF` be the conjunction of WF-1 (intention-count bound K_C), WF-2 (revision-count bound J_C), WF-3 (escalation depth bound D), WF-4 (top-level-cycle bound L), WF-5 (perceive-pattern CyclePattern conformance), and **WF-6 (bounded q-per-intention with disjoint q-sets)** — there exists `Q_max ∈ ℕ⁺` such that for every cycle C and every g_k ∈ DeclaredIntentions(M-cycle-C), `|q_of(M-cycle-C, g_k)| ≤ Q_max`, AND for every pair of distinct g_a, g_b ∈ DeclaredIntentions(M-cycle-C), `q_of(g_a) ∩ q_of(g_b) = ∅`.
>
> Under `WF`, every transition sequence from a well-formed initial configuration `⟨0 ; ∅ ; [] ; R_0⟩` terminates in finitely many steps at a terminal configuration (one where no rule is admissible).
>
> **Scope.** Full corpus coverage under WF-6: Charles K=1 (Q_max=1), Jim K=2 (Q_max=1), Nathan K=2 depth-2 (Q_max=1), Sarah K=2 (Q_max=1; full transition including the post-Srini-resume R-moot-intention(g_2) → R-execute(g_1) → … → R-close path), **Rusty K=3 (Q_max=2; γ_1 binds q_1 + q_2; q-sets pairwise disjoint per §14.5.1)**. The functional-q_of specialization (Q_max = 1) covers four cases; relational q_of with Q_max ≥ 2 covers Rusty under Axis-6's Layers A/B/C (§11.4.6 multi-θ standing-option re-firing; §11.4.7 conjunctive gate; §11.1 recognizer's `q ∈ q_of(g_k)` membership extension). **General-case scoped-out extensions** (absent in corpus): resource contention (q-sets share a q across γ_k) and multi-simultaneously-missing-q at R-gate-fail (σ-picks q_failed when |q_of(g_k) \ R| > 1) — opens as new-Bucket-1 forks only if an engagement exhibits them.

**Functional-q_of fragment (single-clause definition).** An engagement is **functional-q_of** iff every g_k declared in every cycle C of the engagement binds exactly one required resource — i.e., exactly one θ-declaration per g_k in M-cycle-C; equivalently, `q_of(M-cycle-C, g_k)` is single-valued for every g_k. The clause is purely about R-component bindings, not matrix-position designations: preferred-position designations `[Α/i./t./D./P.]` live in the perception-comparison body and never enter R, so the clause is silent on multi-P-per-matrix cases (Sarah's X1/X2, Charles/Jim's multi-X δ-bodies are all in scope; Rusty K=3 is out only because g_1 binds q_1 AND q_2).

**WF preconditions — detailed definitions (preserved from the pre-Thread-A draft, with WF-5 added under Thread A's CyclePattern derived view).** The Layer-1 check (§8 axioms + §8.3.1 lattice + §9.3.4 recursion note + §11.4.14 R-flowback's R-open trigger) reveals that none of the four operator-discretionary parameters is bounded by the system's mechanics. The findings:

**(i) Intentions per objective (γ-count per cycle).** The lattice (§8.3.1) admits `intention` as a child of `objective` without cardinality bound. A7 admits ordinals over ℕ⁺ without upper bound. A9 enforces sibling completeness — if γ_k exists, γ_1, …, γ_(k-1) all exist — but not a cap on k. R-intention (§11.4.5) requires fresh g_k per firing, which gives distinctness but not boundedness. **No Layer-1 mechanism bounds γ-count per cycle.**

**(ii) Escalation / resource-dependency depth (S-stack depth).** §9.3.4 explicitly states: "The recursion is bounded only by the engagement's stack depth, not by the lattice." A sub-cycle's gate may itself fail, spawning a sub-sub-cycle, recursively. R-spawn (§11.6.2) has no premise capping the S-stack height before push. **No Layer-1 mechanism bounds escalation depth per engagement.**

**(iii) ι-revisions per cycle (R-objective-revise firings).** R-objective-revise (§11.7.2) may fire repeatedly within a cycle, each firing appending a new ι-declaration to M while preserving the prior. The rule's only premise is that the original ι exists in M-cycle-C; nothing caps how many times the revised body itself can be re-revised. **No layer bounds revision-count per cycle.**

**(iv) Top-level cycles per engagement.** R-open at C+1 fires after every R-flowback marker (per §11.4.14) — the trigger keys off the flowback-recorded marker, opening the next top-level cycle. R-open has no premise capping the cycle ordinal; the lattice admits arbitrarily many `Α/iN` interest-paths (A7's ordinal range is ℕ⁺ unbounded); the iN discipline at the agenda root (§11.4.2) gives distinctness across cycles but not a cap on cycle count. The engagement could in principle run unboundedly many sequential top-level cycles, each individually terminating, summing to an infinite transition sequence. **No Layer-1 mechanism bounds top-level cycle count per engagement.**

The termination theorem therefore takes **engagement-specification preconditions**:

- **WF-1 (Bounded intention-set per cycle).** For every cycle C in the engagement, there exists `K_C ∈ ℕ⁺` such that at most `K_C` distinct g_k are declared via R-intention within cycle C.
- **WF-2 (Bounded revision-count per cycle).** For every cycle C in the engagement, there exists `J_C ∈ ℕ⁺` such that at most `J_C` ι-revisions fire within cycle C via R-objective-revise.
- **WF-3 (Bounded escalation depth per engagement).** There exists `D ∈ ℕ⁺` such that the S-stack never exceeds depth D at any point in the engagement's transition sequence.
- **WF-4 (Bounded top-level cycle count per engagement).** There exists `L ∈ ℕ⁺` such that at most `L` top-level cycles open via R-open within the engagement (across the full transition sequence).
- **WF-5 (Perceive-pattern cycle-conformance, added 2026-06-24 to close Gate (4) + Axis 8-Sarah; fold scope refined post-review to *declared* γ_k, see §11.1 Stability paragraph for the rationale).** For every cycle C in the engagement, **all γ_k declared via R-intention within C (i.e., all `g_k ∈ DeclaredIntentions(M-cycle-C)`) agree on `CyclePattern(M-cycle-C)`** (per §11.1's CyclePattern derived view): either all declared γ_k's projected Γ-comparison bodies reference sole-dot at the matrix-position level (cycle), or each declared γ_k's projected Γ-comparison body references its own ordinal index at the matrix-position level (per-intention). The conformance condition rides on R-intention's existing "well-typed at Layer 2" premise — R-intention(g_k) at k ≥ 2 fails Layer-2 typing if g_k's body would violate the cycle's already-established CyclePattern. Under WF-5 — combined with §7.5's append-only γ-declarations — **CyclePattern is set by the first R-intention firing in a cycle and stable thereafter** (no further writers; no commutation surface; R-moot-intention is not a domain-writer because the `DeclaredIntentions` fold-domain is monotone-growing under append-only M, not the `LiveIntentions` view which R-moot-intention shrinks). The conformance is corpus-verified: Charles (cycle, vacuous K=1), Jim (cycle, sole-dot P with cost/benefit sub-indices), Nathan (cycle, sole-dot P with c1/c2 cost sub-indices), Sarah (per-intention, X1/X2 ordinally indexed), Rusty (per-intention, P1/P2 ordinally indexed).

**Why this is the honest form.** As standard for typed operational semantics, termination is stated conditionally on well-formedness: λ-calculus termination proofs assume well-typed terms (the typing system bounds the structure that ensures termination); LSPI's strong normalization assumes well-formed engagement specifications (the operator's intention-set, revision-count, escalation depth, and top-level-cycle count are all finite). The preconditions are **not** a weakening — they accurately describe what LSPI models, since the analyst chooses how many intentions to declare, how often to revise, how deeply to escalate, and how many top-level cycles to run in a given engagement. The dissertation's worked cases all exhibit specific finite values: Charles L=1, K=1; Sarah L=1, K=2, J=1 (Table 14 revision); Rusty L=1, K=3, D=1 (Tables 16–19 escalation). The system admits any finite values; the theorem guarantees termination for all such finite choices.

**What WF-3 and WF-4 do *not* assume.** WF-3 bounds the maximum depth reached during the engagement, not the depth admissible by Layer 1 (Layer 1 admits arbitrary depth per §9.3.4). WF-4 bounds the top-level cycle count per engagement, not the cycle count admissible by Layer 1 (the iN discipline admits arbitrary ordinals per A7). Both bounds are per-engagement, not LSPI-wide; different engagements may have different D and L values.

#### §13.5.2 Termination measure

Define the lexicographic measure `μ : Reachable → ℕ × ℕ`:

```
μ(⟨C ; M ; S ; R⟩) = ⟨ L − top_opened(M) ,
                       Σ_{c ∈ S ∪ {active_C}}  B^(D − depth(c)) · rem_budget(c, M) ⟩
```

ordered lexicographically (outer component dominant), where:

- `L`, `D` are the WF-4 and WF-3 engagement bounds
- `top_opened(M)` = number of R-open firings in M (≤ L)
- `depth(c)` = c's position in the stack S ∪ {active_C}, with top-level = 0
- `B` = (max per-cycle remaining budget achievable in the engagement) + 1, strictly greater than any single `rem_budget` value
- `rem_budget(c, M)` = remaining firing budget for cycle c per the inline per-cycle bound under WF-1 + WF-2 + WF-6: `(1 + J_C) · PerCycleSkeleton + K_C · PerIntentionBound − firings_already_in(M, c)`. **PerCycleSkeleton = 5** non-g_k skeleton rules that re-fire on R-objective-revise (R-detect, R-objective, R-outcome, R-obtained-utility, R-close — plus R-flowback as the cycle-shared close; the cycle-pattern case adds +1 for R-perceive-cycle / R-perceive-failure-cycle). **PerIntentionBound = 4 + 4·Q_max** (Axis-6-corrected formula, 2026-06-24, replacing the prior `≈ 6` which undercounted escalated intentions): 1 (R-intention) + Q_max (R-rr, one per q) + (1 + Q_max) (R-gate, 1 initial + 1 re-fire per resume) + Q_max (R-spawn per missing q) + Q_max (R-resume) + 1 (R-execute) + 1 (R-perceive); finite under WF-6's Q_max bound. The prior `≈ 6` reads as the unescalated-Q_max=1 case (Charles, Jim) and was wrong for any escalated intention (Nathan's γ_2, Sarah's γ_1 + γ_2, all Rusty intentions); §14's worked-case bounds recomputed under the corrected formula 2026-06-24.

#### §13.5.3 Per-step decrease (every rule strictly decreases μ)

| Rule | Outer Δ | Inner Δ | μ direction |
|---|---|---|---|
| R-open (top level) | **−1** | +(B − 1) · B^D (new top-level cycle full-budget) | ⬇ outer dominates |
| R-spawn (parent depth d → sub depth d+1) | 0 | −B^(D−d) + B^(D−d−1)·(B−1) = −B^(D−d−1) | ⬇ strict |
| R-resume (sub depth d+1 → parent depth d) | 0 | −B^(D−d) (parent firing) − B^(D−d−1)·sub.rem_budget (pop) | ⬇ strict |
| R-close-nested (sub depth d+1) | 0 | −B^(D−d−1) | ⬇ |
| R-abandon (sub depth d+1, nested case) | 0 | −B^(D−d) − B^(D−d−1)·sub.rem_budget | ⬇ |
| R-abandon (top level, S=[]) | 0 | −B^(D−d) | ⬇ |
| Per-K rules (R-intention, R-rr, R-gate, R-execute, R-perceive, R-perceive-cycle, R-perceive-failure, R-perceive-failure-cycle, R-moot-intention) at depth d | 0 | −B^(D−d) | ⬇ |
| R-objective-revise (at depth d, counted in (1+J_C)) | 0 | −B^(D−d) | ⬇ |
| R-select, R-outcome, R-obtained-utility, R-close, R-flowback (cycle-shared close at depth d) | 0 | −B^(D−d) | ⬇ |
| R-moot (cycle-shared at depth d) | 0 | −B^(D−d) | ⬇ |

Strict-decrease justification at the load-bearing spots:

- **R-spawn**: net inner change `−B^(D−d) + B^(D−d−1)(B−1) = B^(D−d−1)(B − B) − B^(D−d−1) = −B^(D−d−1)`. Strictly negative because `B^(D−d−1) ≥ 1`. The "B = max + 1" choice is load-bearing: B sets the inner-sum's positional value at depth d strictly greater than any total contribution from depth d+1 with any rem_budget ≤ B − 1.
- **R-resume**: net inner change `−B^(D−d) − B^(D−d−1) · sub.rem_budget ≤ −B^(D−d) < 0` (sub.rem_budget ≥ 0; parent firing strictly accounts for the −B^(D−d) term). The pop's contribution is non-positive.
- **R-open**: outer drops 1, dominating any inner increase by lexicographic ordering.

#### §13.5.4 Well-foundedness

μ ranges over `ℕ × ℕ` ordered lexicographically. This is well-founded: no infinite strictly-descending chain in ℕ × ℕ under lex order (any descending chain in the outer eventually stops; for each fixed outer, descending chains in the inner stop). Therefore strong normalization (SN) holds: no infinite transition sequence.

#### §13.5.5 Progress (every reachable non-terminal state has an admissible rule)

A configuration is terminal iff no rule is admissible. Progress establishes that terminal configurations are exactly the **done** configurations, not stuck states. By exhaustive case analysis over the active cycle's phase:

**(1) Between cycles** (`S = []`, `last(M) = ⟨flowback-recorded, _⟩` or `M = ∅`): if `top_opened(M) < L`, R-open is admissible (WF-4 budget remains); if `top_opened(M) = L`, no rule is admissible and the configuration is **done — terminal by design**.

**(2) Cycle-prologue** (per-intention phase not yet active): the last cycle-scoped entry licenses exactly its successor — `⟨open, C⟩ → R-interest`, `ι → R-detect`, `δ → R-objective` (which writes ω, activating the per-intention phase).

**(3) Per-intention phase active**: at least one of the following conditions holds, each licensing a rule:
- some g_k undeclared with `|DeclaredIntentions| < K_C` → **R-intention**;
- `PendingTheta ≠ ∅` → **R-rr**;
- g_k at θ-written with `R ∋ q_k` → **R-gate**, with `R ∌ q_k` and `depth < D` → **R-spawn**;
- g_k at `gate-passed` → **R-execute**;
- g_k at `executed` with `CyclePattern = per-intention` → **R-perceive** / **R-perceive-failure** (guard-determined);
- all live executed with `CyclePattern = cycle` and `⟨perceive, C⟩ ∉ M` → **R-perceive-cycle** / **R-perceive-failure-cycle**;
- all live g_k terminal → **R-select** (its F5 guard is satisfied: no live g_k sits at executed-without-⟨perceive, C⟩, so the executed-existential implication holds).

The one state with no forward rule is `θ-written ∧ R ∌ q_k ∧ depth = D` (R-spawn blocked by WF-3) `∧ K = 1` (R-moot-intention blocked, `|LiveIntentions \ {g_k}| = 0`): there **R-moot** (cycle objective now unreachable) or **R-abandon** (universal premise, §13.5.9 forward-guard) is admissible — the intended operator exit from an unresolvable escalation, not a stuck lifecycle. At `K ≥ 2` the same state additionally licenses **R-moot-intention(g_k)**.

**(4) Suspended parent** (active cycle is a sub-cycle): progress is the sub-cycle's progress (cases 2–3 at sub scope); its μ strictly decreases, so it reaches `⟨flowback-recorded⟩` in finitely many steps, then case (5) fires R-resume.

**(5) Cycle-shared close** (`⟨select-staged⟩ ∈ M-cycle-C`): `⟨select-staged⟩ → R-outcome`, `Ω → R-obtained-utility`, `Λ → R-close`, `⟨close, C⟩ → R-flowback`; after `⟨flowback-recorded⟩`, `S` non-empty → **R-resume**, `S` empty → case (1).

Every non-done configuration admits a rule. R-abandon's universal premise is the **explicit backstop**, but the enumeration shows it (and R-moot) is **load-bearing only at the case-(3) dead-end** — a maximally-escalated, single-intention, resource-blocked gate; everywhere else a forward, close, or resume/open rule carries progress. The terminal configurations are exactly the done configurations of case (1) with `top_opened = L`. ∎

#### §13.5.6 Conclusion

SN (§13.5.4) + Progress (§13.5.5) = Termination. Every transition sequence from a well-formed initial configuration under `WF` (WF-1 through WF-6) reaches a terminal configuration in finitely many steps. ∎


#### §13.5.7 Independence from Theorems 13.1 through 13.4

Same disposition as §13.3 and §13.4: walk each proof step and check whether any earlier theorem is consumed.

- **§13.5.1 WF preconditions block** (folded into Statement under Thread A): just states finiteness assumptions; no theorem citations. **No earlier theorem consumed.**
- **§13.5.5 progress** (renumbered from old §13.5.3 under Thread A): per-configuration rule-applicability case analysis. Each case reads `last(M-cycle-C)` (a syntactic position read), checks membership predicates (decidable on multisets), and enumerates applicable rules. **No constituent-identity claim (no §13.1), no type inspection (no §13.2), no congruence decision (no §13.3), no resource-conservation arithmetic (no §13.4).** R-moot / R-abandon / R-spawn-fresh-g_k exhaustiveness is read from §11.6's rule specifications.
- **§13.5.2 termination measure + §13.5.3 per-step decrease** (superseding the old §13.5.4 per-cycle firing-count bound under Thread A's depth-weighted lex μ): the depth-weighted μ is defined directly over `ℕ × ℕ` and the per-step decrement table reads each rule's premise/contractum from §11.4 / §11.6 / §11.7 against M's append-only discipline (§7.5) — a syntactic check, not a constituent identification. **No earlier theorem consumed.**
- **§13.5.2 depth-keyed measure** (subsumes the old §13.5.5 well-bracketing argument; **the crux of independence**): the user-flagged check confirmed by per-rule inspection that R-spawn writes parent-C as integer, R-resume reads parent-C as integer, R-abandon reads C as integer. Pop-to-push matching is by integer equality, not by path; μ's depth coordinate `d` is the integer key. **§13.1 is not consumed.** This was the load-bearing trace step the user specifically asked to verify; under Thread A the integer-keying is enforced structurally by μ's depth-`d` indexing rather than as a standalone well-bracketing lemma.
- **§13.5.4 well-foundedness + §13.5.6 conclusion** (replacing the old §13.5.6 arbitrary-depth induction under Thread A's μ-over-`ℕ × ℕ` framing): well-foundedness of lex `ℕ × ℕ` plus per-step decrease (§13.5.3) gives SN directly; the conclusion composes SN with progress (§13.5.5). WF-3's depth bound and WF-4's top-level-cycle bound enter through μ's structure rather than through a separate induction. M's append-only discipline (§7.5) is used by the per-step decrement table. **No earlier theorem consumed.** Specifically, the user-flagged check on §13.4 confirmed: exit-reachability (sub-cycle reaches close-nested ∨ moot ∨ abandon) is what termination needs, not resource-conservation arithmetic. §13.4's resource-balance is available as a composite (termination composes with §13.4 to give "no resource leaks at termination") but is not consumed inside §13.5's proof — exit-reachability is established by §13.5.5 (progress, via R-abandon's universal availability) + §13.5.2/§13.5.3 (depth-weighted μ + per-step decrease) alone.

**Composites available, none consumed.** §13.1's actor-holdings-conservation composite is available — the termination claim composes with §13.1 to give "the actor's holdings stabilize at engagement-end." §13.2's typed-state-preservation composite is available — termination composes with §13.2 to give "every reachable configuration is well-typed at termination." §13.4's resource-balance composite is available — termination composes with §13.4 to give "no resource leaks at termination." §13.3's congruence-decidability composite is available — termination composes with §13.3 to give "the normalized form at termination is decidable in linear-expected / O(n log n)-deterministic time." All four composites are available; none is required inside §13.5's proof.

**Conclusion.** Theorem 13.5 is **independent of Theorems 13.1, 13.2, 13.3, and 13.4**. The proof reasons about transition-sequence length, rule applicability, and integer cycle identity — none of which requires constituent-identity bridging, type inspection, congruence decision, or resource arithmetic.

#### §13.5.8 Implications

- **The "well-formedness precondition" framing is honest, not a weakening.** LSPI models analyst-discretionary processes; the analyst chooses K_C (intention count), J_C (revision count), and D (escalation depth) for each engagement. The system's job is to guarantee that for any finite choice, the transition sequence terminates with progress. Claiming unconditional termination would require Layer-1 caps on operator discretion, which would mis-model the descriptive nature of LSPI.
- **Progress is what prevents the "ghost cycle" failure mode.** A sub-cycle that closes without satisfying parent-pending-q would, absent progress, hang the parent forever. R-abandon — via its `any state from which the principal elects not to continue` premise — is what unconditionally ensures the parent can always pop S and continue (or abandon up); R-moot writes the failure marker; R-spawn-fresh-g_k is the optional retry path. §13.5.5's case analysis confirms their exhaustiveness over the post-failure states. **The §11.4.5 specification gap discovered during this proof** — that §11.4.5's premise set `{ ω-body, γ-body, ε-body, ⟨perceive-failure, C⟩ }` does not admit the post-sub-cycle-failure state — means the retry path requires a §11.4.5 extension to be mechanically supported; the abandon-up path has no such gap and alone suffices for progress.
- **Well-bracketing matches via integer cycle identity, not via path identity.** This is the structural reason §13.5 stays independent of §13.1: if the system matched pops to pushes by path, the §13.1 bijection would be the matching mechanism, and termination would inherit §13.1's reasoning. The integer-C-keying is what isolates termination from constituent identity. The choice to track cycle identity by integer (made in §11.1's configuration definition) was load-bearing for this independence — visible only at this theorem.
- **Exit-reachability is the real termination predicate, not exit-success.** A cycle that R-moots or R-abandons has terminated in the well-foundedness sense, even though it did not succeed. §13.5's theorem covers all three exits — close, moot, abandon — because LSPI's audit-trail integrity requires every cycle to reach *some* terminal state, even if the substantive outcome is failure. The dissertation's worked cases include both successful cycles (Charles, most of Sarah, Rusty's escalation success) and failed cycles (Sarah's mooted information sub-cycle, Rusty's eventual abandonment) — all terminate in LSPI's sense.
- **The Layer-1 check was the load-bearing planning step.** Before drafting, confirming that Layer 1 doesn't bound intentions, revisions, depth, or top-level-cycle count was what decided the theorem's form (conditional, with preconditions) rather than letting the proof discover the conditional-ness halfway through. The check found §8.3.1 admits γ-child-of-ω and ι-child-of-γ-spawn without cardinality; A7 admits ordinals over ℕ⁺; §9.3.4 explicitly notes recursion is bounded only by engagement, not lattice; R-objective-revise has no firing-count cap; R-open's R-flowback-marker trigger has no cap on top-level-cycle count. **Candidate (c) (well-formedness preconditions) was the right call.** The fourth parameter (top-level cycle count) was added during review of the old §13.5.6 base case (now §13.5.6 Conclusion under Thread A) — it parallels the first three at the engagement-rather-than-cycle level and is the "hidden finiteness" one level up that planning did not initially enumerate.

- **Discovered §11.4.5 specification gap.** During §13.5.5's progress analysis, the post-sub-cycle-failure retry path required R-intention to fire at a state — `last(M-cycle-parent-C) = ⟨gate-fail, ...⟩` (after R-abandon-on-moot popped S) — that §11.4.5's currently-enumerated premise set `{ ω-body, γ-body, ε-body, ⟨perceive-failure, C⟩ }` does not admit. The dissertation does not exhibit parent-retry-after-sub-cycle-moot in any worked case, which is why §11.4.5 wasn't extended for it. **The §13.5 progress claim is not blocked** — R-abandon-up is always available and alone suffices for progress — but the retry path requires either (a) extending §11.4.5's premise to include the post-sub-cycle-failure positions, or (b) introducing an intermediate rule that transitions the parent's `last` to one §11.4.5 accepts. Catalogued in §13.5.9 as a §11.4.5 follow-up.

#### §13.5.9 Known §11 specification gaps surfaced by the §13 proof series

**Reading note (post-Thread-A numbering).** The gap catalog below was assembled during the pre-Thread-A §13.5 draft; some entries reference the prior §13.5.X subsection structure (old §13.5.3 = Progress; old §13.5.4 = Per-cycle termination; old §13.5.5 = Well-bracketing of S; old §13.5.6 = Arbitrary-depth induction). Under Thread A's reframe (see §13.5 preamble), these consolidate as: progress is now §13.5.5; the old per-cycle bound and arbitrary-depth induction are subsumed by §13.5.2 (termination measure) + §13.5.3 (per-step decrease); well-bracketing is subsumed by μ's integer depth coordinate. The forward-guard and individual Gap entries below have been touched-up where the reference would mislead a reader; deeper historical-context references in long quoted discussions retain the old numbering with parenthetical Thread-A glosses. The gaps themselves (Gap-§11.4.5, Gap-§11.7.2, Gap-§13.4.3-resume-guard-designation-variance, Gap-§11.4-multi-intention-sequencing, Gap-§11.7-non-firing-disciplines) are unchanged in substance.

The trace-don't-inventory discipline applied across §13.1 through §13.5 has surfaced §11 specification gaps that the spec writers had not previously identified. Tracked here as a set so they remain visible across batches and are addressed as a deliberate §11 revision pass rather than as ad-hoc patches mid-§13. Each entry: provenance (which §13 proof found it), nature of the gap, status, and any interactions with other §13 proofs.

**Forward-guard for any §11 revision pass: do not tighten R-abandon.** R-abandon's `last(M-cycle-C) = (any state from which the principal elects not to continue)` premise (§11.6.7 line 2153, verbatim) is the **load-bearing progress mechanism for the entire §13.5 theorem**. The two-part progress structure (§13.5.5, renumbered from old §13.5.3 under Thread A) routes every failure state through R-abandon's universal availability as the backstop that prevents stuck non-terminal configurations. Any revision that narrows R-abandon's trigger — from "any state" to a specific premise set, or by adding side conditions that exclude post-failure states (moot, close-nested-without-satisfaction, gate-fail) — **must re-check §13.5.5's progress proof**, because narrowing the trigger could re-open the stuck-state question that §13.5.5 specifically discharged via R-abandon's breadth. R-abandon's permissive trigger is structurally protected by §13.5. (R-moot has a similar operator-discretionary trigger and is the other principal-choice rule of the failure family, but it does not transfer control — R-abandon does, which is why it is the one that matters for stuck-state avoidance.) Some entries in this catalog propose tightenings of neighboring rules (e.g., R-objective-revise in Gap-§11.7.2's resolution path); none of those proposed tightenings touch R-abandon, but a spec-revision pass should treat R-abandon's breadth as a known dependency rather than incidentally narrowable.

**Gap-§11.4.2 — generic sub-cycle ι body vs Sarah worked example (RESOLVED during §13.2 / §13.4 review).** Originally §11.4.2's generic sub-cycle interest body was `{ [interest-path/Q.] }` — the sub-cycle's own obtained-Q at `parent-prefix/i./Q.`. Sarah Table 13's worked example used `{ [Α/i./o./g1/q.] }` — the parent's required-q. The two forms disagreed. The §13.4 proof's required-q ↔ earned-Q pinning required the Sarah form to make R-resume's literal multiset membership work without invoking §13.1's bijection. Resolved by updating §11.4.2's sub-cycle branch to `{ parent-pending-q }` literally (read from the top S-entry), reconciling the rule with Sarah's example and the §13.4 independence claim. Also propagated to §13.2.2's R-interest case to keep type preservation consistent.

**Gap-§11.4.5 — R-intention premise set missing the post-sub-cycle-failure state (this proof, OPEN).** R-intention's current premise: `last(M-cycle-C) ∈ { ω-body, γ-body, ε-body, ⟨perceive-failure, C⟩ }`. The post-sub-cycle-failure state (parent's `last(M-cycle-C)` = gate-fail marker after R-abandon-on-moot or R-abandon-on-close-nested-failure popped S) is not in this set. Consequence: §11.6.6's "escalate further (R-spawn against a fresh g_k)" prose endorsement and §11.6.7's parallel parent-retry option are permitted in spirit but not mechanically supported — the parent cannot declare γ_(k+1) via R-intention from the post-sub-cycle-failure state, so R-spawn-fresh-g_k can't fire. **Status: non-blocking for §13.5** (R-abandon-up is always available via §11.6.7's "any state" premise and alone suffices for progress); **flagged for §11 follow-up**. Two resolution options: (a) extend §11.4.5's premise set to include `⟨gate-fail, ...⟩` (and possibly `⟨abandon, ...⟩` tagged with a sub-cycle if accessed post-pop), or (b) introduce an intermediate rule that transitions the parent's `last(M-cycle-C)` to one §11.4.5 already accepts (e.g., a "R-retry-prepare" rule that converts the gate-fail-after-pop state into a γ-body-equivalent). **Interaction with the per-cycle firing-count bound** (old §13.5.4/§13.5.6 discussion, now folded into §13.5.2's depth-weighted μ under Thread A)**:** the bound currently assumes "at most one sub-cycle per parent gate" because the retry path is blocked. If §11.4.5 is extended per (a) or (b), the bound re-derives as at most K_C sub-cycles per parent gate (charged against K_C's intention budget); total firing count becomes (per-cycle) × L × K_C × D, still finite but with the K_C factor folded in. Either resolution preserves termination; the bound just shifts.

**Gap-§11.7.2 — Sarah Table 14 ι revision body uses old generic form (flagged D-6 during §13.4 review, OPEN).** §11.7.2's worked-case validation cites Sarah Table 14 lines 359 → 361: the initial sub-cycle ι body is `{ [Α/i./o./g2/q.] }` (matches the new `{ parent-pending-q }` form post-Gap-§11.4.2 resolution), but the **revised body** is `{ [Α/i./o./g2/i./Q.] }` — the OLD generic form, sub-cycle's own obtained-Q. Under the new pinning, on the normal path the revised Φ-body equals the revised ι-body (`{ [Α/i./o./g2/i./Q.] }`), so R-resume's literal multiset membership test (`R ∋ parent-pending-q`) **returns false** — R correctly contains the `[Α/i./o./g2/i./Q.]` the sub-cycle actually obtained, but not `parent-pending-q = [Α/i./o./g2/q.]`. The dissertation shows Sarah completing the revised interest without the parent being mooted, which the system's current rules would route as a resume-fail (no `R ∋ parent-pending-q`) leading to R-abandon-up at the parent.

**Scope: fidelity, not soundness.** This gap does **not** reopen any cleared theorem.

- **§13.4 robust.** Conservation holds — R correctly contains the designation the sub-cycle obtained (`[Α/i./o./g2/i./Q.]`), accounted under multiset arithmetic; no leak, no duplication. §13.1 is not invoked — the resume-guard's literal multiset membership is the same syntactic check; it just returns false instead of true. Both §13.4.3's pinning paragraph and §13.4's independence claim are robust under the revised case: the pinning works as designed when ι↔Φ delivers parent-pending-q; when revision routes ι to a different path, the check correctly fails and the parent abandons-up. **No conservation violation; no §13.1 bridge required either way.**
- **§13.5 robust.** Termination and progress hold — the revised-ι case routes cleanly through resume-fail → R-abandon-up (per §13.5.5's case-(3) backstop, renumbered from old §13.5.3 under Thread A), terminating in finite steps. The depth-weighted μ (§13.5.2) and per-step decrement table (§13.5.3) are unaffected; the §13.5.4/§13.5.6 well-foundedness + conclusion compose unchanged.

The gap is purely a **fidelity** question: can LSPI model Sarah-as-described — completing the revised interest with the parent ultimately benefiting — rather than the parent abandoning-up after the resume-fail? Not a soundness question about any cleared theorem.

**Resolution is gated by a ground-truth classification only the dissertation can decide.** The three readings collapse to a binary classification of what Sarah's Table 14 nested cycle *is*:

- **If it's an escalation** (spawned by a gate failure to fetch a resource the parent's gate needed), then its ι is definitionally `{ parent-pending-q }` — the sub-cycle exists *solely* to obtain the parent's needed resource — and revising that ι to a different path is incoherent (it would mean the escalation has stopped fetching what the parent needs). A sub-cycle needing a *different* resource to first obtain parent-pending-q is sub-escalation, handled by R-spawn going deeper, not by R-objective-revise. So R-objective-revise of an escalation sub-cycle's ι has no legitimate use, and **resolution (3) — side-condition R-objective-revise to bar sub-cycle ι revision when the sub-cycle is an escalation** — is the principled choice. Clean, no new structure. Resolution (2)'s "system correctly disciplines the dissertation" is essentially the escalation reading with the conclusion that Table 14 is a dissertation error; preventing the incoherent revision via (3) is cleaner than documenting its bad consequence via (2), so (3) supersedes (2) under the escalation classification.

- **If it's voluntary nesting** (Sarah pursuing a sub-interest that isn't a gate-failure resource fetch), then it's not bound by the parent-pending-q pinning at all, its ι is genuinely its own `[.../i./Q.]` and freely revisable, and it returns through a different mechanism than the resume guard. **Resolution (1) is right** — the system is missing the escalation-vs-voluntary distinction entirely. This means R-spawn has two modes with different ι-pinning and different return discipline, recorded by an S-entry tag (e.g., `⟨spawn-origin: escalation⟩` vs `⟨spawn-origin: voluntary⟩`), with corresponding updates throughout the failure family (R-resume's premise must dispatch on the tag; R-objective-revise's side condition must dispatch on the tag). This is the bigger lift.

**Classification reopened during Part IV §14.4 source verification (Block E):** The prior classification (resolution (3), based on a one-sided p.119 citation) does not survive the source's internal contradiction. **p.119's narrative chapter** ("Sarah had a simple plan. Over lunch she told Srini about the management responsibilities...") supports dissuasion-planned-from-the-start → relabeling → (3). **T14's detection-row narrative** ("upon after a conversation with Srini, Sarah discovered that a different approach would be preferable. Instead of ... altering the judges' perception ... Sarah observed...") supports mid-conversation voluntary redirect → (1). These are a **source-internal contradiction**: the narrative chapter and the formalized table tell different stories about when Sarah formed the dissuade-Srini plan. Q2 is similarly mixed: T14's Φ-label `[Α/i./o./g_2/q.]` matches the original parent-pending-q (→ relabeling, →3), but its substantive effect — R-moot for Intention 2 at the parent (per Block B of §14.4) — is a substantive parent change (→ voluntary redirect, →1). **Status: (1)-vs-(3) reopened.** The classification cannot be cleanly resolved from p.119 alone (the prior draft's reading); resolution requires either picking which source axis to privilege (narrative chapter vs formalized table) or accepting that the dissertation's own account is internally ambiguous on this point.

**The classification must come from the dissertation text** (Lam 2018 Table 14 + surrounding narrative). Two diagnostic questions, used together:

- **Q1 — Why did Sarah revise?** Was the revision driven by a gate-failure (the sub-cycle's gate couldn't pass and she redirected) or by her own re-evaluation of the situation (independent of any gate test)? Gate-failure-driven points toward escalation; independent re-evaluation points toward voluntary.
- **Q2 — What did the revision produce?** Did the parent ultimately obtain the resource it originally gated on (`parent-pending-q = [Α/i./o./g2/q.]`), or a different one? If the parent still got the original parent-pending-q despite the sub-cycle's revision, the revised body is doing something other than redirecting the fetch (sub-structure, relabeling, or an intermediate-form-that-resolves-to-the-original-q), which points away from a clean voluntary reading. If the parent's outcome substantively changed (different resource obtained, or different downstream effect), that is consistent with either a redirected escalation or a genuine voluntary pursuit.

The two diagnostics together disambiguate better than either alone: (Q1 gate-failure-driven) + (Q2 parent got original q) → escalation with revision-as-relabeling, points to (3) with possibly an additional formal note that escalation sub-cycle ι is structurally pinned and may only be re-stated, not redirected; (Q1 independent re-evaluation) + (Q2 parent's outcome changed) → genuine voluntary nesting, points to (1) and the bigger structural lift; mixed answers (Q1 one way, Q2 the other) require closer reading of what specifically Sarah re-evaluated and how the outcome propagated. This is a "ground truth before formalism" call analogous to the Layer-1 check that gated §13.5: it cannot be resolved by inspecting the system alone. **Resolution awaits the dissertation classification.**

**The two resolutions have very different cross-§13 costs — worth pricing before reading Table 14.**

- **Resolution (3) (escalation) is contained.** It narrows R-objective-revise (not an S-modifying rule), reinforces the §13.4.3 pinning (no escalation-ι revision means the pinning always holds), and touches no independence claim. **No cleared theorem is reopened.** §13.4.3, §13.5.2's depth-keyed measure (formerly §13.5.5's well-bracketing argument under pre-Thread-A numbering), and §13.6's permutation argument all inherit the existing structure with R-objective-revise's narrower applicability automatically respected.

- **Resolution (1) (voluntary) ripples back through two already-cleared proofs.** Resolution (1) adds a voluntary-nesting mode: a voluntary-spawn (push) and a voluntary-return (pop), "returning through a different mechanism than the resume guard." Both already-cleared S-stack proofs depend on properties the new machinery must be **explicitly re-verified** against — they do NOT automatically inherit:
  - **§13.4.3 (pinning) becomes escalation-scoped.** The required-q ↔ earned-Q pinning is proved for sub-cycles whose ι = parent-pending-q — i.e., escalation sub-cycles. Voluntary sub-cycles have ι = own `[.../i./Q.]` and return through a different mechanism, so they are **outside the pinning's scope** and need their own conservation/flowback argument. If the voluntary-return identifies the returned resource by path (rather than by the literal multiset membership of an integer-keyed designation), **§13.4 could acquire a §13.1 dependency in the voluntary case** that the escalation pinning specifically avoids. Re-scope §13.4.3 to "escalation sub-cycles" and add a voluntary-case conservation step.
  - **§13.5.2 depth-keyed measure (subsuming the old §13.5.5 well-bracketing / §13.1-independence claim) must be re-verified for the new rules.** Under Thread A, μ's integer depth coordinate `d` enforces the integer-keyed pop-to-push matching that was previously a standalone well-bracketing lemma — verified per-rule for R-spawn / R-resume / R-abandon. The voluntary-spawn and voluntary-return are **new S-modifying rules**; §13.5's §13.1-independence holds for the voluntary mode only if they **also** key on integer C (so that μ's depth coordinate remains well-defined and decreasing). If the "different return mechanism" matches by path, **§13.5 acquires a §13.1 dependency in the voluntary case**. The integer-keying check must be re-run on the two new rules before §13.5's §13.1-independence claim extends to voluntary nesting.

**Net pricing.** Resolution (3) reopens nothing — the existing §13.4 and §13.5 independences carry forward unchanged, and only §13.6's permutation set adjusts (a small effect, since R-objective-revise's narrower applicability shrinks rather than expands the permutation candidates). Resolution (1) reopens **two already-cleared proofs** (§13.4.3 and §13.5.2's depth-keyed measure, formerly §13.5.5's well-bracketing) for the voluntary case, each requiring fresh per-rule integer-keying / pinning-scope verification, and **also** changes §13.6's permutation set via the new dispatch on spawn-origin. The classification's resolution doesn't just decide §13.6's setup — **a voluntary verdict is materially more expensive than an escalation one**, and that cost is a legitimate input to how carefully the surrounding narrative deserves reading.

**Interaction with the historical per-cycle termination discussion** (pre-Thread-A §13.5.4; now superseded by §13.5.2's depth-weighted μ — preserved here as historical record of the bound's evolution)**.** The per-cycle bound went through three forms: original `12 + 4·K_C + J_C + 1` (pre-§13.6-correction, ignored lifecycle reset); interim `(1 + J_C) · (12 + 4·K_C) + J_C + 1` (added the `(1 + J_C)` factor for re-passes but collided with WF-1's K_C cap by scaling the iterating rules per-pass); **final, under Reading B: `5·(1 + J_C) + 6·K_C + J_C + 5`** (only the non-g_k-indexed skeleton scales with passes; g_k-indexed rules stay at K_C total across passes per WF-1's global cap). The **third aspect of Gap-§11.7.2 discovered during the §13.6 correction pass** is R-objective-revise's lifecycle-reset semantics: its contractum makes the new ι-body `last(M-cycle-C)`, which resets the lifecycle to R-detect (the only rule whose premise matches the new `last`), so the downstream skeleton re-fires per revision while R-intention's global K_C budget is preserved. The corrected bound is finite under WF-1 and WF-2; termination is preserved across all three bound forms. **Reset semantics pinned (Reading B): R-intention's freshness premise is global across passes; budget-exhaustion forces R-moot or R-abandon as the cycle's exit (per §11.6.6 / §11.6.7, both available from any state).** Reading A — "re-passes reuse existing g_k" — was rejected because R-detect after revision produces new target/preferred-position/adverse-alternative paths, and reusing an old g_k whose objective-body referenced the old detection would be semantically inconsistent with the revised cycle.

**Independent of Gap-§11.7.2's resolution choice (1 vs 3)**: the corrected bound's form is the same under either resolution (3 narrows R-objective-revise's applicability for escalation sub-cycles, which reduces effective J_C for those sub-cycles but doesn't change the bound's structure; 1 adds the S-entry tag, which doesn't affect the per-cycle firing-count structure either).

**Interaction with §13.6 (forward-note).** §13.6's permutation-of-independent-transition-steps argument needs to enumerate which transition steps can permute. R-objective-revise is currently freely-firing within a cycle; if resolution (3) is selected, its applicability narrows (no firings on escalation sub-cycle ι), which shrinks the permutation set. If resolution (1) is selected, R-spawn's two modes and R-resume's dispatched premise change the independence relation across the voluntary-vs-escalation boundary. Additionally, **independence between transition steps may itself become a §13.1-dependent question under resolution (1)** if voluntary-mode return matches by path — the entire §13.6 architecture depends on whether step-independence is decidable on M-slice disjointness alone (syntactic/integer-keyed) or requires constituent identity (§13.1-consumed). **Settle the classification before drafting §13.6's permutation argument** — the proof skeleton depends on the resolved rule set, and the cleared-theorem reopening question depends on it too.

**Shared lineage with Gap-§13.4.3-resume-guard-designation-variance.** Sarah's Gap-§11.7.2 and the resume-guard-designation-variance gap (Rusty T17, see entry below) both live downstream of Gap-§11.4.2's resolved routing decision: R-resume's literal multiset membership test was deliberately routed against `parent-pending-q` read from the top S-entry (not against the sub-cycle's ι) to keep §13.4.3's pinning proof independent of §13.1's bijection. That routing opened the syntactic-vs-semantic equality gap at two distinct points in the lifecycle. **Sarah's mismatch lives in what the routing opened** (the sub-cycle's ι can be revised away from parent-pending-q without the guard noticing, because the guard reads the S-entry not ι — §11.4.2's branch is upstream of the guard). **The resume-guard-designation-variance mismatch lives in what the routing didn't fix** (the guard still demands literal designation equality between Φ-delivered R-multiset and parent-pending-q; Erik T17's Φ delivers sole-dot `q.` against parent-pending-q ordinal `q_2`). Same abstract pattern (the source has multiple ways of writing the same designation, the system has one), but mechanically distinct from Sarah (which breaks upstream of the guard). Filing separately to preserve the mechanical divergence; cross-referencing here to preserve the common ancestor with Sarah. The gap is named for the mechanism (resume-guard designation-variance) rather than for the case (Rusty), so that future instances on different designation axes — if they actually exercise the same mechanical break point — can be filed under the existing entry.

**Gap-§13.4.3-resume-guard-designation-variance — Erik T17 Φ-body delivers sole-dot `q.` against parent-pending-q ordinal `q_2`, breaking R-resume's literal multiset membership test (surfaced during Part IV §14.5 source verification; one source-verified instance to date, OPEN).** Rusty T16 escalates to Erik T17 for parent-pending-q `[A/i./o./g1/q2]` (q_2 ordinal, the second of two required resources at g_1 — see Gap-§11.4 Axis 6). Erik's sub-cycle ι body is `{ [A/i./o./g1/q2] }` at start (pinning holds at start per Gap-§11.4.2's resolved branch — R-spawn's contractum *sets* the sub-cycle ι := { parent-pending-q }, so the start-state designation always matches by construction). Erik's lifecycle runs to completion and emits **Φ-body `{ [A/i./o./g1/q.] }`** (sole-dot, book pages 207–208). R-resume's premise `R ∋ parent-pending-q` tests `R ∋ [A/i./o./g1/q2]` against R containing `[A/i./o./g1/q.]`. **Literal multiset membership returns false** — `q.` (sole-dot) and `q2` (ordinal) are syntactically distinct designations; no §8.2.2 lexer rule (D-26, D-27, D-28, or any other) normalizes between sole-dot and ordinal q-designations. The dissertation continues as if Erik's resume passes (T18 R-execute(γ_1) cites both q_1 and q_2 as consumed cost designations); the system's current rules route this as a resume-fail.

**Critical scope discipline (post-§14.3 Nathan walk, single-instance reaffirmed):** A candidate second instance — Nathan T8's numeral `21` rendering in Wanda's ι-row (book page 181) vs parent-pending-q's ordinal `g2` — was considered during §14.3 walk and **demoted out of this gap on mechanical grounds**. The `21` rendering lives in Wanda's ι row, which is a value R-spawn *produces* (R-spawn's contractum sets `ι(sub-cycle) := { parent-pending-q }` per Gap-§11.4.2's resolved branch). R-spawn does not *test* a pre-existing ι against parent-pending-q — there is no membership test at the spawn step to fail. Critically, every other o-segment in Wanda's sub-cycle (T8 detection body, intention, θ, execution; T10 perception, Φ) renders `g2` correctly; Wanda's Φ at T10 row 5 delivers `[A/i./o./g2/q.]` (book page 188), matching Randy's parent-pending-q literally. Randy's R-resume guard passes literally. The `21` is a transcription artifact in a row the system *writes* as `g2` anyway, with zero mechanical consequence. **Different mechanical break point** (no break point at all, in fact — the guard reads matching designations). Same abstract pattern (designation-rendering variance) but mechanically distinct from Rusty T17, which is exactly the don't-fold test applied to keep Sarah and Rusty separate two turns ago. Applied consistently here: Nathan T8's `21` is **not** Gap-§13.4.3 Instance 2; it is an F-4 transcription-class finding (see §14.3.3 scan) alongside the T8 detection-operator g_1 mislabel — same transcription species, resolution (1), no mechanical consequence.

**Three readings, open-three with resolution (2) labeled as semantic-not-syntactic** (parallel to Gap-§11.7.2's resolution disposition — not an exit):

1. **Source transcription error.** Erik's Φ should have rendered `q_2`; the sole-dot is a typo. Pinning holds under corrected reading. Manual representation correction by the analyst.
2. **Sole-dot `q.` is the source's shorthand for "the q this sub-cycle was tasked with."** The narrative gloss ("the authorization needed to change the department's requisition policy" — the Q_2 thing) semantically matches parent-pending-q, but the syntactic designation differs. **Pinning holds under semantic reading; FAILS under literal multiset membership** — same syntactic-vs-semantic split Sarah forced on the revision axis, here forced on the resource-ordinal axis. **Resolution (2) is semantic-not-syntactic, NOT a clean fourth option**; it is the narrative-confidence path that the system's literal-membership test does not honor. Listing it explicitly as resolution (2) keeps the parallel with Gap-§11.7.2 visible.
3. **Genuine divergence.** The system's literal-membership test is more disciplined than the source's rendering. Representing Rusty faithfully requires either an analyst-level representation correction (rewrite Erik's Φ as `q_2`) or a system extension (a "designation-folding" lexer rule that admits `q.` ↔ `q_k` equivalence in resume-guard contexts, with side conditions to avoid breaking §13.1 elsewhere).

**Scope: fidelity, not soundness — for the case where pinning literally holds.** Like Gap-§11.7.2, this gap does **not** reopen any cleared theorem on its own:

- **§13.4 robust for the literal-pinning-holds cases.** Rusty T19 (Φ-body `{ [A/i./o./g2/q.] }` = parent-pending-q `[A/i./o./g2/q.]` literally) and T21 (Φ-body `{ [A/i./o./g3/q.] }` = parent-pending-q `[A/i./o./g3/q.]` literally) hold. Nathan T9 (Mike's Φ-body = Wanda's parent-pending-q literally at depth-2) and T10 (Wanda's Φ-body = Randy's parent-pending-q literally at depth-1) both hold. Conservation holds for all literal-pinning cases. §13.4.3's pinning succeeds.
- **§13.4 contingent for the single variance-instance case (Rusty T17).** Conservation arithmetic operates on whatever designations R holds; no leak, no duplication regardless of pinning's literal-vs-semantic resolution. The open question is whether the parent's resume advancement is well-defined when literal-membership fails — under resolution (1) or (3), pinning holds (in the corrected/extended system); under resolution (2), the system's literal test fails while the source proceeds.
- **§13.5 robust.** Resume-fail routes to R-abandon-up (per §13.5.5's case-(3) backstop, renumbered from old §13.5.3); termination preserved either way.

The gap is a **fidelity** question: can LSPI model Rusty-as-described — with Erik T17 contributing q_2 to the parent's R despite the Φ rendering — rather than the parent abandoning-up after the resume-fail?

**Mechanical divergence from Gap-§11.7.2 (different rule, different step, different fix).** Both gaps share an abstract pattern (the source has multiple ways of writing the same designation; the system's literal-membership test honors only one), but the mechanical failure points are distinct:

- **Sarah's Gap-§11.7.2 breaks at the ι↔Φ identity step (upstream of the resume guard).** Sarah's resume guard reads parent-pending-q `[Α/i./o./g2/q.]` from the S-entry and tests R for membership of that exact path. Sarah's sub-cycle delivers Φ-body `{ [Α/i./o./g2/i./Q.] }`. R after flowback contains `[Α/i./o./g2/i./Q.]`. The resume guard tests `R ∋ [Α/i./o./g2/q.]` and returns false — the same failure mode at the surface, but the **break is upstream**: it's R-objective-revise modifying the sub-cycle's ι away from parent-pending-q, in a system where the guard reads the S-entry not ι. The fix-points are R-objective-revise's applicability (resolution 3), R-spawn's tagging (resolution 1), or the dissertation classification (resolution 2 with narrative-only fidelity).
- **Rusty's Gap-§13.4.3-resume-guard-designation-variance breaks at the resume-guard membership test directly.** Rusty's sub-cycle ι body never diverges from parent-pending-q (T17 starts with ι = `{ [A/i./o./g1/q2] }`, literal pinning at start by R-spawn's contractum). The break is purely in **Φ's rendering of the obtained resource at delivery**: the lifecycle's R-obtained-resource → Φ-flowback chain delivers `q.` (sole-dot) when the sub-cycle was started for `q_2` (ordinal). The fix-points are different: source-correction (resolution 1), narrative-only fidelity (resolution 2), or a lexer-level designation-folding rule (resolution 3, distinct from Gap-§11.7.2's resolution 3 which narrows R-objective-revise).

Filing separately preserves the mechanical divergence — different rules accept different fixes — while the shared-lineage sentence (above, in the Gap-§11.7.2 entry) preserves the common §11.4.2-routing-decision ancestor.

**Resolution awaits dissertation classification + §8.2.2 lexer-rule consideration.** Parallel to Gap-§11.7.2, the classification must come from the dissertation text; additionally, the §8.2.2 lexer family must be inspected for whether designation-folding (sole-dot ↔ ordinal at q-suffix) is consistent with the existing normalization discipline (D-26 inserts `/t./`, D-27 inserts `/D./`, D-28 normalizes top-level `A/i.` to `A/i1` — all path-segment-level, not ordinal-suffix-level; adding a designation-folding rule would extend the lexer's scope and needs its own consistency check against §13.1's bijection).

**Status: OPEN.** Pinning holds literally for the literal-pinning-holds cases (Rusty T19, T21; all Nathan pinning points across T8/T9/T10 — Wanda's Φ and Mike's Φ both match parent-pending-q verbatim; Randy's resume guard passes literally). Fails literally only for the single variance instance (Rusty T17). §13.4's correctness modulo this gap is documented in §14.5.2 with the explicit T17 caveat. §13.5.9 status paragraph (below) reflects this gap as the second pinning-fidelity case alongside Gap-§11.7.2.

**Gap-§11.4-multi-intention-sequencing — multi-intention lifecycle is under-specified for K>1 (OPEN; catalog relocated to working register, by-name pointer here).** The full working-register catalog — Block A/B/C/D editorial history, eight inherited axes (Axes 1a, 1b, 2, 3a, 3b, 4, 5, 6, 7, 8), per-case verdicts, retraction trail across four re-classification passes — has been **relocated to LPIC-Part-IV-prep.md Section I as its single home** (no mirror; foundations holds by-name pointer only, per the §1.4.5 state-fork pivot). The structurally cleaner derivation — lifecycle-state-fork table with the two judgment surfaces (Pillar 2 guard-firing at `ε-body`; Pillar 4 σ-sequencing at `γ_1-body single-γ` and `⟨perceive-failure, C⟩`) made visible — is at §1.4.5 above.

**Open specification fix-targets (three remain, after §11.4.6's 2026-06-23 revision closed the first):**

- ~~**§11.4.6 pending-θ-set premise** — RESOLVED 2026-06-23~~ covered Axis 1b Site (i) at `γ_2-body` AND Site (ii) at `ε_1-body` γ-pending AND the θ-reachability half of Axis 3b at `⟨gate-fail, q_k⟩-with-pending-γ`. The pending-θ-set premise replaces the prior `last`-keyed premise; declaration-order θ-firing at K=2 (two-case confirmed Sarah + Nathan; K≥3 caveat preserved); PendingTheta computed as a derived view over M-cycle-C per §7.5 Persistence Invariant discipline. §13.6 empty-independence argument repaired via the symmetric-write half of the last-dependency clause (§13.6.2 + §13.6.3); per-cycle θ-firings = K_C by construction, so the depth-weighted μ (§13.5.2) and per-step decrement table (§13.5.3) are unaffected. (Note: the §13.6 empty-independence reference points to the pre-Thread-A coarse-reading argument; under Thread A's three-bucket / Newman framing, the per-K θ-firing accounting plays through §13.6.5's Bucket-2 standing-option × distinct-g_k row.) See §11.4.6 for the revised rule.
- **§11.6.6 intention-scoped moot rule** (or structural reframe of K intentions as separately closable sub-units) — covers Axis 4 post-resume operator-attested R-moot defect (Sarah T14/T15: source moots Intention 2 while cycle closes successfully on Intention 1; cycle-scoped contractum is wrong granularity).
- **§11.4.8 body-resolution side condition** (or representation correction / fidelity divergence) — covers Axis 8-Sarah at `⟨gate-pass, q⟩` Sarah-K=2-uniform-sole-dot ε (Sarah's body's sole-dot leaves `R ⊖ [.../q.]` ambiguous; the other four corpus patterns resolve under the current rule).
- **§11.4.7 multi-q gate semantics + R-spawn target-identification** — covers Axis 6 Layer C at `⟨gate-fail⟩` multi-q-θ-conjunction (Rusty T16: source's per-q escalation relies on per-θ inference no rule licenses).

**Needs-inspection items (one narrowed by §11.4.6's revision, one unchanged):**

- **Axis 3b NARROWED**: the θ-reachability half (Sarah's "θ_2 before spawn") is resolved by §11.4.6's pending-θ-set premise — at `⟨gate-fail, q_1⟩` with PendingTheta = {γ_2}, R-required-resources is now admissible and writes θ_2, with σ disambiguating between R-rr and R-spawn at this state. The remaining question is the §11.6 active-C-transfer admissibility of double R-spawn stacking on S after both θ are written and both gates have failed (Sarah's batched-θ-multi-spawn fully exercised configuration). That sub-question remains needs-inspection.
- **Axis 5 unchanged**: §11.4.8 re-firing premise structure for per-intention multi-execute (Sarah T14 Srini sub-cycle, leaning defect).

Both located by state in §1.4.5; full analysis in working register at LPIC-Part-IV-prep.md Section I.

**§13's correctness is unaffected** by any of the above (termination, conservation, determinism each hold for whichever §11.4 representation is ultimately pinned). The three remaining fix-targets are §11 spec-revision work (down from four after §11.4.6's 2026-06-23 revision landed); the §13 series is complete in the sense that all six theorems are drafted.


**Gap-§11.7-non-firing-disciplines — R-unfold and R-prime-preserve are presented as active disciplines but neither is invoked by any §13 theorem (clarified during the §13.6 correction pass, OPEN as a §11.7 presentation issue).** §11.7's text presents R-unfold (§11.7.1) and R-prime-preserve (§11.7.3) as active non-firing disciplines that the metatheory invokes for proof-level reasoning. The §13.6 correction-round checks (in §13.6.5) verified per-discipline that:

- **R-unfold is reserved for the `≡_named` relation**, distinct from §10's `≡` syntactic congruence. None of §13's six theorems reasons over `≡_named`, so R-unfold is genuinely unused (not load-bearing-but-skipped). It remains available for future work involving named-equivalence reasoning (LSPI extensions with named sub-procedures, applications that decide cycle-description equivalence modulo named-unfolding, etc.).
- **R-prime-preserve is a corollary of §13.2 + §7.5 composition**: §13.2 ensures every M-entry is well-typed when written (including prime-sorts); §7.5 (Persistence Invariant) ensures prior entries are not modified. The prime-sort preservation across C-transitions follows automatically. R-prime-preserve's explicit statement is redundant but readable.

**Status: open as a §11.7 presentation issue, NOT a §13 architectural issue.** §11.7 should mark these two as **"reserved for `≡_named` work"** (R-unfold) and **"directly-readable corollary of §13.2 + §7.5"** (R-prime-preserve) rather than as active disciplines a reader expects to see used. An unused active rule reads as an oversight; a reserved rule reads as intent. **Resolution option**: §11.7 prose update (re-label the two as reserved / corollary) with no rule-body changes. **§13 series correctness is unaffected** by which presentation §11.7 adopts.

**Common provenance.** All five open gaps (Gap-§11.4.5, Gap-§11.7.2, Gap-§13.4.3-resume-guard-designation-variance, Gap-§11.4-multi-intention-sequencing, Gap-§11.7-non-firing-disciplines) plus the one resolved gap (Gap-§11.4.2) are products of writing §13 proofs and §14 worked-case validations honestly under the trace-don't-inventory discipline. None was identifiable from reading §11 alone (each requires a specific §13 proof step or a specific §14 source-row walk to surface — or, in the §11.7-non-firing case, a specific accounting of which §13 proofs invoke which §11.7 disciplines). This is the discipline's value: §13's review and §14's source verification uncovered spec issues that the spec writers would not have found from their own inspection. The §13 series is complete in the sense that all six theorems are drafted; the five open catalog entries above don't block §13's correctness.

**Where to look for what**: **Gap-§11.4-multi-intention-sequencing** is structurally resolved at **§1.4.5's state-fork table** (Pillar-4 derivation — two σ-discretion forks, one guard-determined state, four genuine defects, two needs-inspection); the full audit-trail catalog with Block A/B/C/D editorial history, axis-by-axis evolution, and per-case verdicts is at **LPIC-Part-IV-prep.md Section I** (single home, no mirror). **Gap-§11.4.5, Gap-§11.7.2, Gap-§13.4.3-resume-guard-designation-variance, Gap-§11.7-non-firing-disciplines** are catalogued directly here in §13.5.9 above; they're separate spec issues that didn't dissolve into the state-fork derivation. **Gap-§11.4.2** is resolved (entry preserved here for traceability).

**Spec-layer split (updated 2026-06-23 after §11.4.6's pending-θ-set revision landed)**: four of the five open gaps are §11 spec-clarity follow-ups (Gap-§11.4.5 missing premise state; Gap-§11.7.2 ι-revision classification + R-objective-revise applicability; Gap-§11.4-multi-intention-sequencing's **three remaining fix-targets** per §1.4.5 — §11.6.6 intention-scoped moot, §11.4.8 body-resolution, §11.4.7 multi-q gate; the §11.4.6 pending-θ-set fix-target has been **closed** by the 2026-06-23 revision (see §11.4.6 for the rule and §1.4.5's standing-option principle for the surface it established); Gap-§11.7-non-firing-disciplines presentation re-label). **Gap-§13.4.3-resume-guard-designation-variance is NOT a §11 follow-up** — its three resolutions are source-correction (analyst-level), semantic-classification (dissertation-level), or an §8.2.2 lexer extension (designation-folding rule on the q-rendering axis); §11.4 / §11.6 rules are not touched. Gap-§11.7.2 and Gap-§13.4.3-resume-guard-designation-variance share a §11.4.2-routing-decision ancestor and an abstract semantic-vs-syntactic pattern but require mechanically and layer-wise distinct fixes (see shared-lineage sentence in Gap-§11.7.2 entry).

### §13.6 Uniqueness of derivation

Theorem 13.6 is the sixth and final theorem of §13. The statement: under the same scope as Theorem 13.5 (full corpus, WF-1 through WF-6), for every operator strategy σ resolving Bucket-1 forks, the transition is **deterministic in the ≅_perm quotient** — every two transition sequences from a well-formed initial configuration that respect σ reach the same normal form modulo ≅_perm.

**Thread A reframe (2026-06-24).** The prior coarse-reading framing (Theorem 13.6 as the trivial determinism corollary of §13.5, with empty independence relation) was correct for the pre-Thread-A system but does **not** survive Thread A's IntentionPosition reframe: the per-K-filtered IntentionPosition reads + §8.6's Embrace commitment make per-intention parallelism real, so the independence relation `I` is non-empty (Bucket 2 of §13.6.5 contains genuine commuting pairs like R-execute(g_a) × R-execute(g_b) at distinct g_a ≠ g_b). The corrected proof uses the **three-bucket partition** (Bucket 1: irreversible licensed, σ-fixed; Bucket 2: I-independent diamonds; Bucket 3: non-co-admissible by F5 or premise-disjointness), the **R-execute Embrace diamond as the Bucket-2 archetype** (Lemma 13.6.7), and **Newman's lemma applied in the ≅_perm quotient** (where ≅_perm is a transition congruence per Lemma 13.6.3, established by the literal-`last` enumeration across all §11 rules).

**Historical record.** §13.6.2 (≅_perm definition), §13.6.4 (independence relation I), and the original §13.6.5-§13.6.7 (R-unfold retraction, dependency disposition, implications) of the pre-Thread-A draft are superseded. The pre-Thread-A correction history (fine-vs-coarse reading, the §13.1 composability finding) remains valid as a separate methodological observation about §13.1's role across the proof series and is referenced in §13.6.9's Pillar discussion. The subsection numbering now runs §13.6.1 through §13.6.10 to accommodate Thread A's expanded confluence machinery.

**The corrected proof discharges ten obligations:**

1. **§13.6.1 Statement** — per-σ confluence in the ≅_perm quotient.
2. **§13.6.2 ≅_perm definition** — permutation modulo mutually-I-independent firings.
3. **§13.6.3 Congruence lemma** — ≅_perm is preserved by every transition (literal-`last` enumeration).
4. **§13.6.4 Independence relation I** — formalized.
5. **§13.6.5 Three-bucket partition** — Bucket 1 (σ-fixed) / Bucket 2 (I-independent) / Bucket 3 (non-co-admissible).
6. **§13.6.6 F5 non-co-admissibility theorem** — item one (R-select × R-execute(g_b) etc.).
7. **§13.6.7 Bucket-2 archetype** — R-execute Embrace diamond + generalization.
8. **§13.6.8 Global per-σ confluence** — μ-≅_perm-invariance + Newman in the quotient + σ formulation (b) (σ as a sequence-quantification).
9. **§13.6.9 Pillar 2 and Pillar 3 — formal content** — boundary of computation; canonical-modulo-permutation audit trail.
10. **§13.6.10 Scope (post-Axis-6 resolution)** — full corpus coverage under WF-6 with disjoint q-sets, including Rusty K=3; resource contention and multi-simultaneously-missing-q scoped out as deliberate general-case extensions.

#### §13.6.1 Statement

> **Theorem 13.6 (Per-σ confluence over the full corpus, post-Axis-6 resolution, in the ≅_perm quotient).** Under the same scope as Theorem 13.5 (WF-1 through WF-6 with disjoint q-sets): let σ be a strategy resolving operator choices at Bucket-1 forks (defined below). For every σ, every transition sequence from a well-formed initial configuration reaches a **unique normal form modulo ≅_perm** — i.e., the transition is deterministic in the ≅_perm quotient.
>
> Equivalently: per-σ, the engagement's outcome is determined by the operator's σ-choices; the machine's scheduling freedom (which I-independent rule fires first when multiple are admissible) never changes the outcome.

#### §13.6.2 ≅_perm — precise definition

> **Definition (≅_perm).** Configurations s, s' are **≅_perm-equivalent** iff M(s) and M(s') differ only by permutation of entries written by **mutually I-independent firings** along the transition path from a common ancestor — where "mutually I-independent" means: every pair of firings whose entries are permuted satisfies r_1 I r_2 (per the I-catalog of §A4 + §A5.4, post-Batch-5 reconciliation including F5 and CyclePattern non-coupling).
>
> Per-g_k intra-lifecycle ordering (γ → θ → ⟨gate-pass⟩ → ε → ⟨perceive, g_k⟩ for a single g_k) is **preserved** because same-g_k lifecycle entries are written by I-dependent sequential rules (same-K coupling per §A4.1). Consequently each g_k's IntentionPosition reads identically in both configurations: the most-recent g_k-tagged position-bearing entry is invariant across permutation because permutation never crosses two entries about the same g_k.

#### §13.6.3 Lemma 13.6a — ≅_perm is a transition congruence

> **Lemma.** If s ≅_perm s' and s → t via rule r firing, then there exists s' → t' via the same rule r with t ≅_perm t'.

**Proof.** Equivalent obligation: no rule's premise distinguishes the relative order of mutually-I-independent per-intention entries. Every rule's premise falls into one of three forms with respect to M-reads:

| Form | Description | Permutation-invariance? |
|---|---|---|
| (A) | Per-K-filtered fold (IntentionPosition / per-K predicates) | Invariant by §11.1's "most-recent entry **about g_k**" — permuting entries about distinct g_k's doesn't change either's per-K fold |
| (B) | Global derived-view fold (F1–F5, PendingTheta, CyclePattern, etc.) | Invariant — these are set-valued / cardinality / universal / existential reads; permutation doesn't change set membership |
| (C) | Literal `last(M-cycle-C)` (or `last(M)`) read | **Must check each instance**: invariant iff the literal-last target is a marker/body that no permutable per-intention entry can be appended-after relative to the read |

The proof reduces to enumerating form (C) — every literal-last read — and verifying each targets a cycle-shared/cycle-scoped marker that no permutable per-intention entry follows in M-cycle-C.

**Complete enumeration of literal-`last` readers (from source grep):**

| Rule | Premise's literal-`last` read | Entry class | Permutable per-intention entries possibly after it? |
|---|---|---|---|
| **R-open** (§11.4.1) | `last(M) = ⟨flowback-recorded, _⟩` ∨ initial | Cycle-scoped marker (cycle-terminal) | No — ⟨flowback-recorded⟩ is the final entry of the prior cycle; the engagement is between cycles at this point, no per-intention entry appended-after exists |
| **R-interest** (§11.4.2) | `last(M-cycle-C) = ⟨open, C⟩` | Cycle-scoped marker (cycle-prologue) | No — ⟨open, C⟩ is the first entry in M-cycle-C; per-intention phase is not yet active (ω not written), no per-intention entry can exist yet |
| **R-detect** (§11.4.3) | `last(M-cycle-C) = ι-body` | Cycle-shared body (cycle-prologue OR post-R-objective-revise reset) | No — ι is single-instance until R-objective-revise re-fires; per-intention phase not active before R-objective writes ω |
| **R-objective** (§11.4.4) | `last(M-cycle-C) = δ-body` | Cycle-shared body | No — same as R-detect; per-intention phase not yet active |
| **R-intention** (§11.4.5, post-reframe) | — | — | (Form A + global folds; no literal-last) |
| **R-rr** (§11.4.6, post-reframe) | — | — | (Form B; PendingTheta read) |
| **R-gate** (§11.4.7, post-reframe) | — | — | (Form A; IntentionPosition + R-test) |
| **R-execute** (§11.4.8, post-reframe) | — | — | (Form A; IntentionPosition + R-test) |
| **R-perceive** (§11.4.9, Rusty, post-reframe) | — | — | (Form A + form B; IntentionPosition + CyclePattern) |
| **R-perceive-cycle** (§11.4.9, Nathan, post-Phase-3) | — | — | (Form B; F4 universal + CyclePattern) |
| **R-select** (§11.4.10, post-Batch-4+6) | — | — | (Form B; F4 universal + F5 implication + CyclePattern) |
| **R-outcome** (§11.4.11) | `last(M-cycle-C) = ⟨select-staged, σ⟩` | Cycle-scoped marker (phase-terminal handoff) | **No — ⟨select-staged, σ⟩ ends the per-intention phase per the §11.1 boundary; no per-intention rule can fire after it (all per-intention rules require per-intention phase active, which excludes ⟨select-staged⟩-present states)** |
| **R-obtained-utility** (§11.4.12) | `last(M-cycle-C) = Ω-body` | Cycle-shared body | No — Ω is appended after ⟨select-staged⟩; per-intention phase ended at R-select |
| **R-close** (§11.4.13) | `last(M-cycle-C) = Λ-body` | Cycle-shared body | No — same |
| **R-flowback** (§11.4.14) | `last(M-cycle-C) = ⟨close, C⟩` | Cycle-scoped marker (cycle-terminal) | No — ⟨close⟩ is the cycle-terminal marker; no further entries until R-flowback's own contractum |
| **R-spawn** (§11.6.2, post-reframe) | — | — | (Form A + form B; IntentionPosition + R-test) |
| **R-close-nested** (§11.6.3) | `last(M-cycle-sub-C) = Λ-body` (sub-cycle scope) | Cycle-shared body | No — sub-cycle's Λ is appended after sub-cycle's per-intention phase (which ended at sub-cycle's R-select) |
| **R-resume** (§11.6.4) | `last(M-cycle-sub-C) = ⟨flowback-recorded, E⟩` (sub-cycle scope) | Cycle-scoped marker (sub-cycle-terminal) | No — sub-cycle's R-close-nested appends this; no further sub-cycle entries follow |
| **R-perceive-failure** (§11.6.5.1, Rusty, post-reframe) | — | — | (Form A + form B; IntentionPosition + CyclePattern) |
| **R-perceive-failure-cycle** (§11.6.5.2, Nathan) | — | — | (Form B; F4 universal + CyclePattern) |
| **R-moot** (§11.6.6.1, RETAINED) | `last(M-cycle-C) = ⟨perceive-failure, C⟩` ∨ operator-attested | Cycle-scoped marker | **Subtle — handled by §11.6.6.2's transparent-`last`**: ⟨perceive-failure, C⟩ is appended by R-perceive-failure-cycle at the all-executed Nathan state; subsequent per-intention writes that could occur (only ⟨moot, C, g_k⟩ via R-moot-intention firings) are **transparently skipped by operative-`last` per §11.6.6.2's lifecycle-wide convention**. So R-moot's literal-last read is permutation-invariant w.r.t. intention-moot markers. **Rusty path note**: under Rusty, R-perceive-failure writes ⟨perceive-failure, g_k⟩ (per-K, not the cycle-scoped form R-moot reads); the first-disjunct trigger doesn't match in the Rusty case — R-moot fires only via the operator-attested branch in the Rusty pattern, which has no literal-last constraint |
| **R-moot-intention** (§11.6.6.3, post-Batch-3) | — | — | (Form A + form B; IntentionPosition + LiveIntentions cardinality) |
| **R-abandon** (§11.6.7) | "any state" — explicit universal premise per §13.5.9 forward-guard | None (universal admission) | N/A — no literal-last constraint at all |
| **R-objective-revise** (§11.7.2) | `M-cycle-C contains [a.]ι(...)` (containment, not last) | Containment over ι-bodies | N/A — containment is permutation-invariant by definition |
| **R-prime-preserve** (§11.7.3) | — (invariant clause, not a transition) | — | N/A |

For every rule in §11, the literal-`last` read targets one of: a cycle-scoped marker appended at a phase boundary (⟨open, C⟩, ⟨select-staged, σ⟩, ⟨close, C⟩, ⟨flowback-recorded, E⟩, ⟨perceive-failure, C⟩); a cycle-shared body in a fixed lifecycle position (ι, δ, Ω, Λ); or no literal-`last` read at all (post-reframe per-intention rules read IntentionPosition / global folds; R-abandon admits universally). **No rule reads a permutable per-intention entry as its literal `last(M-cycle-C)`.** The transparent-`last` convention covers the one subtle case (R-moot) exactly. ≅_perm is preserved by every transition. ∎

**Note.** The Thread A reframe is load-bearing for this lemma: pre-reframe, R-execute read `last = ⟨gate-pass, q⟩` literally (per-K marker — permutation would matter); R-perceive read `last = ε-body` (per-K — permutation would matter); R-gate had two-trigger positional reads. The reframe rewrote every per-intention rule to read IntentionPosition (per-K fold) or global folds, eliminating literal-last reads on permutable entries. §8.6's Embrace commitment becomes a theorem here.

#### §13.6.4 Independence relation I (formalized)

> **Definition.** For rules r_1, r_2 and a reachable state s where both are admissible: `r_1 I_s r_2` iff (a) r_1's writes don't change r_2's premise-read values at s, (b) r_2's writes don't change r_1's premise-read values at s, (c) r_1 and r_2's non-M side-effects on R, S, C commute. **I = ⋂_{s} I_s** over all reachable states (the relation holds whenever both rules are co-admissible).

#### §13.6.5 Three-bucket partition

Every pair (r_1, r_2) of co-admissible rules falls into exactly one bucket:

**Bucket 1 (non-commuting AND licensed; σ-discretion at irreversible forks):**
- Same-g_k σ-elections: `R-moot-intention(g_k) × any-proceed-rule-at-g_k`; `R-rr × R-moot-intention(g_a where g_a is earliest pending)`
- Cycle-scoped operator elections: `R-moot × any-proceed-rule`; `R-abandon × any-proceed-rule`
- R-objective-revise × R-intention(fresh g_b)
- Cardinality-boundary state-conditional: `R-moot-intention(g_a) × R-moot-intention(g_b)` at K=2; `R-intention(g_a) × R-intention(g_b)` at K_C-cap boundary
- **Universal-over-live × R-intention(g_b) class** (by criterion): R-select × R-intention; R-perceive-cycle × R-intention; R-perceive-failure-cycle × R-intention

**Bucket 2 (I-independent; commuting diamonds):**
- Distinct-g_k per-K Embrace diamonds: R-execute(g_a) × R-execute(g_b); R-perceive(g_a) × R-perceive(g_b) (Rusty pattern); R-perceive-failure(g_a) × R-perceive-failure(g_b) (Rusty); R-gate(g_a) × R-gate(g_b); R-execute(g_a) × R-perceive(g_b); R-execute(g_a) × R-perceive-failure(g_b); R-execute(g_a) × R-moot-intention(g_b); R-perceive(g_a) × R-moot-intention(g_b); R-moot-intention(g_a) × R-moot-intention(g_b) at K ≥ 3
- Standing-option × distinct-g_k: R-rr × R-intention(g_b); R-rr × R-execute(g_b); R-rr × R-perceive(g_b); R-rr × R-gate(g_b); R-rr × R-moot-intention(g_b at distinct earliest)
- R-objective-revise × per-K-on-already-declared-g_b (per §11.7.2 preservation): × R-rr, × R-gate(g_b), × R-execute(g_b), × R-perceive(g_b), × R-perceive-failure(g_b), × R-moot-intention(g_b)
- R-intention pairs below K_C cap

**Bucket 3 (non-co-admissible; vacuous obligation):**
- **F5 / LifecyclePosition disjointness**: R-select × R-execute(g_b); R-select × R-spawn(g_b); R-select × R-gate(g_b); R-select × R-rr — all proven non-co-admissible (Theorem 13.6.6 below)
- CyclePattern-gated: R-perceive × R-perceive-cycle; R-perceive-failure × R-perceive-failure-cycle
- Pillar-2 guard-determined: R-perceive(g_k) × R-perceive-failure(g_k); R-perceive-cycle × R-perceive-failure-cycle; R-gate(g_k) × R-spawn(g_k)
- Position-disjoint same-g_k pairs (different IntentionPosition requirements)

#### §13.6.6 Theorem (F5 non-co-admissibility) — item one

> **Theorem.** R-select and R-execute(g_b) are never co-admissible at any reachable state, for any g_b ∈ DeclaredIntentions(M-cycle-C). Symmetric results hold for R-select × R-spawn(g_b), R-select × R-gate(g_b), R-select × R-rr.

**Proof.** R-execute(g_b)'s premise requires `IntentionPosition(g_b) = gate-passed q_b`. The position `gate-passed q_b` is reachable only post-`declared` and pre-`mooted` (R-gate writes ⟨gate-pass⟩ only for declared, non-mooted g_b; no LifecyclePosition transition admits gate-passed-then-revived after mooting). Therefore `g_b ∈ LiveIntentions(M-cycle-C)` whenever R-execute(g_b) is admissible.

R-select's premise (conjunct (ii)) requires `∀ g_k ∈ LiveIntentions: PerIntentionTerminal(IntentionPosition(g_k))` where `PerIntentionTerminal(p) ::= p ∈ {perceived, executed, mooted}`.

For g_b in LiveIntentions: R-execute(g_b) admissible ⟹ `IntentionPosition(g_b) = gate-passed q_b` ⟹ `IntentionPosition(g_b) ∉ {perceived, executed, mooted}` (LifecyclePosition disjointness) ⟹ R-select's universal **fails** for g_b ⟹ R-select inadmissible.

Therefore no reachable state has both admissible. The "dual polarity" between F4 and F5 expresses as a **strict sequencing constraint** (R-execute strictly precedes R-select in any transition sequence reaching R-select), not as a commutation pair. ∎

#### §13.6.7 Bucket-2 local confluence (archetype)

**Lemma 13.6.7 (R-execute Embrace diamond, post-Axis-6 generalization).** For distinct g_a, g_b ∈ DeclaredIntentions(M-cycle-C) under WF-6 with disjoint q-sets (`q_of(g_a) ∩ q_of(g_b) = ∅`), if R-execute(g_a) and R-execute(g_b) are both admissible at state s, then `s →_{R-execute(g_a)} s_α →_{R-execute(g_b)} s_αβ` and `s →_{R-execute(g_b)} s_β →_{R-execute(g_a)} s_βα` with `s_αβ ≅_perm s_βα`.

**Proof.** Six-check structure:

1. **Per-K reads disjoint**: R-execute(g_a)'s premise reads IntentionPosition(g_a) (filtered by g_a); R-execute(g_b)'s reads IntentionPosition(g_b). Disjoint per-K folds.
2. **Per-K writes disjoint**: R-execute(g_a) writes ε_a-body tagged g_a; R-execute(g_b) writes ε_b-body tagged g_b. Disjoint per-K tags.
3. **R-component effects commute**: R-execute(g_a) writes R ⊖ cost(q_of(g_a)) (the full multiset deduction over all q ∈ q_of(g_a) — a single firing's cost-list per §11.4.8 lists every q the intention binds; T18 Rusty source-verified: γ_1's ε-body lists both q_1 and q_2). R-execute(g_b) writes R ⊖ cost(q_of(g_b)). **Under WF-6 with disjoint q-sets: q_of(g_a) ∩ q_of(g_b) = ∅** (distinct g_k → disjoint q-sets in the corpus; Rusty source-verified at §14.5.1, Charles/Jim/Nathan/Sarah trivially since |q_of(g_k)| = 1 with path-disjoint sole-dot or ordinal designations). Multiset difference over disjoint operand sets commutes regardless of operand size: `(R ⊖ cost(q_of(g_a))) ⊖ cost(q_of(g_b)) = (R ⊖ cost(q_of(g_b))) ⊖ cost(q_of(g_a))`. The functional-q_of specialization (|q_of(g_k)| = 1) is the singleton case.
4. **C, S unchanged in both paths**: R-execute is per-intention, doesn't transition C or write S.
5. **Cycle-shared derived views unchanged**: CyclePattern (set on declaration, no change), DeclaredIntentions, LiveIntentions, MootedIntentions, PendingTheta all unchanged by ε-body writes (not in their fold-domains).
6. **M permutation-equivalent**: ε_a and ε_b in different orders; ≅_perm by Lemma 13.6.3 (literal-last enumeration covers).

Therefore `s_αβ ≅_perm s_βα`. ∎

**Generalization to other Bucket-2 pairs.** Each pair satisfies the six checks:
- Per-K read disjointness: §11.1 tightened recognizer + distinct g_k.
- Per-K write disjointness: per-K-tagged writes for distinct g_k.
- R-component commutation: WF-6 with disjoint q-sets (for pairs touching R; multiset difference over disjoint operand sets commutes at any |q_of(g_k)| ≤ Q_max); no R-effect (for pairs that don't touch R like R-perceive(g_a) × R-perceive(g_b)).
- C, S commutation: cycle-shared writes (when present) commute on disjoint operands; same-S/C writes are handled in Bucket 1 (R-spawn ↔ R-resume) or Bucket 3 (active-C exclusion).
- Derived views unchanged.
- M ≅_perm by Lemma 13.6.3.

#### §13.6.8 Global per-σ confluence

**μ is ≅_perm-invariant.** For `s ≅_perm s'`, `μ(s) = μ(s')`: permuting mutually-I-independent per-intention entries changes no `top_opened(M)` (R-open firings aren't per-intention entries), no `depth(c)`, and no `rem_budget(c, M)` (per-cycle firing counts are permutation-stable). Hence strong normalization (Theorem 13.5) descends to the ≅_perm quotient.

**Per-σ confluence (sequence formulation).** Fix a well-formed initial configuration s₀ and let ρ, ρ′ be two maximal transition sequences from s₀ making the same choice at every Bucket-1 fork — this is what "fixing σ" means: σ resolves only the irreversible operator elections of §13.6.5 and does not constrain Bucket-2 scheduling. Every point at which ρ and ρ′ diverge is a co-admissibility fork, hence Bucket 1, 2, or 3. Bucket-3 pairs are non-co-admissible (Theorem 13.6.6 + premise-disjointness), so no fork arises there; Bucket-1 forks are resolved identically by the fixed σ. So every actual divergence is a Bucket-2 scheduling fork, which by Lemma 13.6.7 closes as a local-confluence diamond modulo ≅_perm, and by Lemma 13.6.3 (≅_perm is a transition congruence) the reconverged states continue reducing identically up to ≅_perm. Since μ is well-founded on the quotient, finitely many such diamonds compose (equivalently, Newman's lemma on the relation over ≅_perm-classes, which is locally confluent once σ has emptied Bucket 1 and Bucket 3 is vacuous): ρ and ρ′ reach the same ≅_perm-class, the unique normal form modulo ≅_perm for (s₀, σ). ∎

#### §13.6.9 Pillar 2 and Pillar 3 — formal content

**Pillar 2 (Boundary of computation).** Theorem 13.6 states that the machine's scheduling freedom — which I-independent rule fires first when multiple are admissible — **never changes the engagement's outcome**. The outcome is σ-determined: only the operator's choices at Bucket-1 irreversible forks affect the engagement's normal form. **Determinism modulo scheduling, with genuine choice exactly where human judgment lives.** Bucket 1 IS the operator's decision surface; everything else is invariant under judgment-free scheduling. This is the precise formal content of "the boundary of computation."

**Pillar 3 (Audit trail).** The audit trail M is canonical modulo ≅_perm: byte-stable for sequenced operations (cycle-shared rules, cycle-prologue rules, escalation boundaries, σ-elected commitments) and canonical-modulo-permutation for parallel operations (per-intention rules at distinct g_k). Asserting strict byte-identity regardless of scheduling would falsely sequence genuinely concurrent operations — an operator pursuing two intentions at distinct g_k truly has no "real order" between their per-K firings. The right inviolability is **the audit trail faithfully records what's sequenced AND faithfully records that parallel-class entries are parallel**. Lemma 13.6.3 (≅_perm congruence) is the formal statement of this. This is the precise formal content of "inviolable audit trail."

#### §13.6.10 Scope and the Axis-6 extension

**Full corpus coverage under WF-1..WF-6 with disjoint q-sets** (Axis 6 resolved 2026-06-24): Charles K=1, Jim K=2, Nathan K=2 depth-2, Sarah K=2 (Q_max = 1, functional-q_of specialization), **and Rusty K=3 (Q_max = 2, relational q_of)** — all reduce terminating + confluent per Theorems 13.5 and 13.6 under the Axis-6-extended rules (§11.4.6 PendingTheta admits θ-written for Layer-A standing-option re-firing; §11.4.7 R-gate's conjunctive `R ⊇ q_of(g_k)` premise + Layer-C specific-q gate-fail; §11.1 recognizer's `q ∈ q_of(g_k)` membership extension).

**The Rusty K=3 case and the σ-quantification (batched-σ diamond).** Theorem 13.6.1 quantifies over *every* operator strategy σ; Rusty's dissertation source σ exhibits sequential intention-addition (γ_2 declared only after R-perceive-failure(γ_1); γ_3 after R-perceive-failure(γ_2)), but the theorem covers all σ-respecting transition sequences — including **batched σ** that declares γ_1, γ_2, γ_3 upfront (admissible per Rusty's WF-5-conformant per-intention pattern, since each γ_k references its own ordinal P_n in the projected Γ-comparison body, so the cycle-pattern conformance is satisfied at first-declaration time and remains stable). Under batched σ, R-execute(g_1), R-execute(g_2), R-execute(g_3) become co-admissible at simultaneously-gate-passed states. **The §13.6.7 R-execute Embrace diamond holds genuinely under batched σ** by the disjoint-q-sets generalization (Lemma 13.6.7 step 3, post-Axis-6 form): Rusty's q-sets are pairwise disjoint (q_of(g_1) = {q_1, q_2}, q_of(g_2) = {q_γ2}, q_of(g_3) = {q_γ3}, source-verified at §14.5.1), so multiset difference over disjoint operand sets commutes regardless of operand size. Under Rusty's source σ the diamond's co-admissibility precondition is vacuous (sequential per-intention lifecycle: R-execute(g_a) at IP(g_a)=gate-passed terminates before R-intention(g_b) admits the next γ); under batched σ the diamond is genuinely exercised and closes by disjoint-q-sets. **Both σ-classes covered; the theorem holds.**

**General-case extensions (named, scoped out as deliberate design problems opened only if exhibited in an engagement):**

1. **Resource contention** — two intentions sharing a required q (q_of(g_a) ∩ q_of(g_b) ≠ ∅). Would expose a new Bucket-1 fork: executing one intention disables the other's gate (R-multiset reduces below q_of(g_other)'s requirement). Absent in the dissertation corpus (Rusty's q-sets verified pairwise disjoint; Charles/Jim/Nathan/Sarah trivially at |q_of|=1).

2. **Multi-simultaneously-missing-q at R-gate-fail** — σ-picks q_failed when |q_of(g_k) \ R| > 1 (which missing q to spawn for first). Absent in the corpus (Rusty γ_1 has only q_2 missing at first gate-fire since q_1 is already held). Already accommodated by §11.4.7's R-gate-fail σ-pick clause; engagements that exercise it open a deliberate Bucket-1 catalog entry.

---


# End of Part II — signed off

---

# Part IV — Worked-case validation

Part IV traces each of Lam 2018 Chapter 5's five documented engagements (Charles, Jim, Nathan, Sarah, Rusty) against the §13 theorems, identifying which case exercises which theorem and which structural property remains validated by no case. The validation discipline follows the trace-don't-inventory rule that produced the §13 series' calibrated architecture: each case's trace is read from the source tables directly (with table/line citations so the matches are independently checkable), not inherited from prior summaries.

**The honesty boundary up front.** §11 was *fitted* to these cases — Charles row-by-row, the lexer normalizations (D-21, D-26, D-27, D-28) introduced to reconcile the dissertation's notation, the §11.4 / §11.6 lifecycle ordered against the worked tables. Reproducing the cases confirms the formalization is faithful to its source and internally consistent on these instances; it is **not an independent correctness proof**, because the rules were built to reproduce exactly these traces. What the validation can establish:

- **Density of empirical coverage**: single-cycle lifecycle (Charles, Jim); multi-intention K-loop (Jim K=2, Nathan K=2, Rusty K=3); depth-1 escalation with pinning (Sarah, Rusty); depth-2 escalation with pinning and two-level conservation (Nathan); multi-spawn well-bracketing (Rusty ×3).
- **Divergences where the system is more disciplined than the source**: Sarah Table 14's ι↔Φ violation (the basis for Gap-§11.7.2 resolution 3), Nathan Table 8's g1/g2 detection-row mislabel, Nathan Table 9's intra-path spacing artifacts. These are the informative outcomes — the places where worked-case validation carries information beyond clean reproduction of a fitting case.

What the validation **does not** establish: depth-≥3 nesting (Nathan bottoms out at depth 2), parent-retry-after-sub-cycle-failure (every sub-cycle in all five cases succeeds), legitimate non-escalation ι-revision (the only "New Interest" row is Sarah T14, and resolution 3 bars it at the system level). Those three structural properties rest on the abstract §13 proofs alone; no worked case exercises them.

**Draft order.** Sections are presented in dissertation order (Charles → Jim → Nathan → Sarah → Rusty), with the cross-case findings catalog at §14.9. The drafting order, however, ran Sarah → Nathan → Rusty → Charles → Jim — Sarah establishes the template at depth-1, Nathan stresses it at depth-2 (the hard test immediately after the template), then breadth follows. Below the sections appear in dissertation order; the template's establishment in Sarah is referenced by Nathan's depth-2 trace and by the briefer Charles/Jim sections.

### §14.1 Charles — Table 5 (K=1 single-cycle; the primary fitting case)

Charles Table 5 documents a single-table engagement: one top-level cycle, one intention, no escalation, no sub-cycles, no revision. It is the simplest of the five cases and the one §11 was fitted against most directly — the §11.5 end-to-end trace walks Charles T5 row-by-row, and the lexer normalizations (D-26, D-27) and the Θ→Φ/Λ retokenization (D-21) were calibrated to reconcile exactly these rows. Charles is therefore the **maximal-circularity** case in Part IV: reproducing it confirms that §11.4's fourteen lifecycle rules compose into the normal path the dissertation depicts, and confirms nothing about the rules' correctness beyond that depiction. The informative content of §14.1 is not the clean reproduction (which is guaranteed by construction) but the three F-4 divergences the row-walk surfaces (§14.1.3) and the **scope** Charles establishes vs. leaves open (§14.1.4).

Source verified directly against PDF pp.169–172 (book pp.169–172); rows quoted from the Representation column.

#### §14.1.1 Case overview and structural skeleton

**Single top-level cycle** `ι(Α/i.)` (Charles's interest: damage Harry's credibility with the CFO; agenda "See Harry removed as Director"). **K_C = 1** intention (γ at `g.`), gate **passes** (no escalation). The full row sequence (Table 5, source notation, post-D-21/D-26/D-27/D-28 normalization noted inline):

| Row | Category | Source notation | Normalized / rule |
|-----|----------|-----------------|-------------------|
| Interest | ι | `[a.]ι(Α/i.) := { [Α/i./Q.] }` | post-D-28 `Α/i1`; R-interest |
| Detection | δ | `[a.]δ(Α/i./d.) := { [Α/i./t.], [Α/i./t./D./P.], [Α/i./t./D./X1], [Α/i./t./D./X2] }` | R-detect; **two** adverse alts X1/X2 |
| Target / Pref / Adverse | — | `[Α/i./t.]`, `[Α/i./t./D./P.]`, `[Α/i./t./D./X.]` | representative rows; **standalone Adverse uses sole-dot `X.`** (F-4 C-1) |
| Objective | ω | `[a.]ω(Α/i./o.) ≡ { [Α/i./t.]Σ(Α/i./t./D.)′ → [Α/i./t./S./P.]′ }` | R-objective |
| Intention | γ | `[a.]γ(Α/i./o./g.) ≡ { [Α/i./t.]Γ(Α/i./t./G.)′ = { [Α/i./t./D./P./u.]′ > [Α/i./t./D./X./u.]′ } }` | projected Γ drops `/D.` → D-27 inserts; R-intention |
| Required resources | θ | `[a.]θ(Α/i./o./g1) := { [Α/i./o./g1/q.] }` | **ordinal `g1`**; R-required-resources |
| Resource check | gate | `[a./R.] ∋ [Α/i./o./g1/q.]` | gate **passes**; R-gate |
| Execution | ε | `[a.]ε(Α/i./o./g./e.) → { [Α/i./t./D./X./c.] + [Α/i./o./g./q.] }` | **sole-dot `g.` at operator AND body** (Axis 8 baseline); R-execute |
| Perception | Γ | `[Α/i./t.]Γ(Α/i./D./G.) = { [Α/i./D./P./u.] > [Α/i./D./X./u.] }` | realized Γ drops `/t.` → D-26 inserts; R-perceive |
| Outcome | Ω | `Ω(Α/i./O.) ≡ { [Α/i./t.]Σ(Α/i./t./D.) → [Α/i./t./S./P.] }` | systemic, no prefix; R-outcome |
| Obtained utility | Λ | `[Α/i./t.]Θ(Α/i./O./U.) := { [Α/i./t./D./P./u.] }` | post-D-21 Θ→Λ (target-prefixed); R-obtained-utility |
| Obtained resource | Φ | `[a.]Θ(Α/i./O./Q.) := { [Α/i./Q.] }` | post-D-21 Θ→Φ (actor-prefixed); R-flowback |

**Engagement WF parameters** (Reading B): L = 1, K_C = 1, K_exec = 1, J_C = 0, escalation depth D = 0, max S-stack depth 0, **Q_max = 1** (WF-6 trivially, |q_of(g_1)| = 1). Per-cycle bound (inline in §13.5.2's `rem_budget`, Axis-6-corrected formula 2026-06-24): `5·(1+0) + (4 + 4·1)·1 + 0 + 5 = 18` firings (prior formula `6·K_C` undercount fix: 16 → 18; Charles's non-escalated lifecycle realizes 14 firings, ≤ 18); the §11.5 trace realizes 14 rule firings / 15 M-entries, within bound. The lifecycle runs once, gate-passes once, no failure-family rule fires.

#### §14.1.2 Per-theorem trace

**§13.1 path-uniqueness (clean at the cycle layer; one F-4 wrinkle).** Single cycle, single γ at `g.`, single interest at `i.` (post-D-28 `Α/i1`). No sole-dot reuse of the Sarah-instance-1 kind (Charles has only one intention, so no g./g. collision can arise). Per-actor scope holds; bijection holds trivially. **The one §13.1-relevant wrinkle**: the δ-body enumerates two adverse alternatives `[Α/i./t./D./X1]`, `[Α/i./t./D./X2]`, while the standalone Adverse-alternative row writes sole-dot `[Α/i./t./D./X.]`. Taken literally, `X.` ("the only adverse alternative," A6 sole-of-type) contradicts the existence of X1 and X2. Per §11.3's row-correspondence note, **LSPI adopts the δ-body's enumeration as source of truth** (X1, X2 are the declared constituents); the standalone row's `X.` is a representative class-marker for the adverse-alternative *sort*, not a sole-of-type assertion. Under that adoption X1 ≠ X2 are distinct constituents at distinct addresses and §13.1(W) holds. **§13.1 validated at the cycle layer with the X1/X2-vs-`X.` inconsistency resolved by the §11.3 δ-body-canonical adoption** (F-4 C-1 below).

**§13.2 type preservation.** The fourteen lifecycle rules fire once each in fixed order (R-open → … → R-flowback; the §11.5 trace is the witness). Each contractum is well-typed per §13.2.2: ι/δ/θ/Λ/Φ attribution-forms (§9.6.2), ω/Ω equivalence-forms (§9.6.1), γ perception-evaluation body (§9.7.4), ε effect-form (§9.5.1/C7a), Γ perception-evaluation (§9.7.4), structural markers untyped (marker convention). The projected Γ in γ's body (`Γ(Α/i./t./G.)′`, drops `/D.`) and the realized Γ in the Perception row (`Γ(Α/i./D./G.)`, drops `/t.`) are normalized by D-27 and D-26 respectively into canonical `Γ(Α/i./t./D./G.)` before Layer-2 typing. **§13.2 validated; no contingency** — Charles fires no multi-intention, revision, or failure-family rule, so none of the Gap-§11.4 axes is exercised here (Axis 8's ε-rendering question is *present* — see C-3 — but at K=1 it is cosmetic, not a reproduction failure; the body's single `[Α/i./o./g./q.]` is unambiguous because only one q exists).

**§13.3 congruence decidability.** No non-trivial congruence decision arises (single cycle, no repeated sub-structure to compare). Σ-clauses and Γ-bodies parse to standard Layer-3 forms post-D-26/D-27 normalization. **§13.3 validated abstractly.**

**§13.4 resource conservation (single-cycle; NO pinning exercised).** R changes exactly twice: R-execute deducts `cost([Α/i./o./g./q.])` via `⊖`; R-flowback adds `{ [Α/i./Q.] }` via `⊎`. Net: `R(after) = R(at-open) ⊖ cost(q) ⊎ { [Α/i./Q.] }`. No leak (the gate verified `R ∋ [Α/i./o./g1/q.]` before R-execute), no duplication (single R-flowback firing). **Charles does NOT exercise the §13.4.3 required-q↔earned-Q pinning** — there is no escalation, no sub-cycle, no S-entry, no R-resume guard. Pinning is exercised only by Sarah (depth-1, two points), Rusty (depth-1, three points incl. the T17 variance gap), and Nathan (depth-2, both points literal). Charles validates only the **per-cycle** half of §13.4 (§13.4.2), not the cross-cycle half (§13.4.3). **§13.4 per-cycle conservation validated; cross-cycle pinning not reached.**

**§13.5 termination + progress.** WF-1 (K_C=1), WF-2 (J_C=0), WF-3 (D=0), WF-4 (L=1) all trivially bounded. The lifecycle advances deterministically through fourteen `last`-keyed phase transitions to R-flowback; no gate-fail (so no R-spawn), no perceive-failure (so no R-moot/R-abandon branch), no stuck state. **§13.5 validated** as the minimal single-cycle terminating sequence; it exercises termination but not the depth coordinate of μ (§13.5.2; subsumes old §13.5.5 well-bracketing, no push/pop) or the depth-≥1 levels of the depth-weighted induction (§13.5.4 well-foundedness + §13.5.6 conclusion; formerly old §13.5.6 arbitrary-depth induction; D=0 base of bases).

**§13.6 determinism (σ genuinely trivial — Charles's distinctive contribution).** Charles is the one case where the operator choice sequence σ is **trivially empty of discretionary forks**: no multi-intention σ-discretion (K=1, so the `γ_1-body` single-γ fork never arises), no R-objective-revise (J_C=0, so no advance-vs-revise fork), no `⟨perceive-failure, C⟩` state reached (perception validates), no `post-resume operator-attested` state reached. At every `last`-position exactly one rule applies. **§13.6 validated for Charles with NO contingency** — unlike Sarah (post-resume R-moot defect [Axis 4 legacy] remaining; Site (i) γ_2-body defect RESOLVED 2026-06-23 by §11.4.6's pending-θ-set revision) and Rusty (determinism modulo Gap-§13.4.3). Charles is the clean determinism witness: fixed (empty) σ + `last`-driven dispatch → pointwise-unique transition sequence, no open gap attached.

#### §14.1.3 Source-level inconsistencies surfaced (F-4 instances) — per-row + per-leaf-path scan

Per the §14.4.3 methodology (every ι/δ/γ/θ/ε/Γ/Σ/Ω/Λ/Φ row walked; per-leaf-path enumeration within ε; count set by scan, not pre-committed; each divergence cites its handling mechanism):

**Charles F-4 instance C-1: standalone Adverse-alternative row sole-dot `X.` vs δ-body ordinals `X1`/`X2`.** The δ-body (Detection row) enumerates `[Α/i./t./D./X1]` and `[Α/i./t./D./X2]`; the standalone Adverse-alternative row writes `[Α/i./t./D./X.]` (sole-dot). Source-internal inconsistency (PDF pp.169–170). **Classification: δ-body canonical per §11.3's row-correspondence note** — the standalone row is descriptive accompaniment (a representative class-marker), not an operation-row declaration; the δ-body is the operational source of truth. No lexer rule applies; this is a representation-adoption decision already recorded in §11.3. Not a §13.1(W) violation under that adoption (X1 ≠ X2 are distinct constituents at distinct addresses).

**Charles F-4 instance C-2: Γ-path divergence (projected drops `/D.`, realized drops `/t.`).** Intention-row projected Γ is `Γ(Α/i./t./G.)′` (drops `/D.`); Perception-row realized Γ is `Γ(Α/i./D./G.)` (drops `/t.`). Same §13.1(W)-inverse-shape (one constituent at two non-congruent paths, prime-distinguished) as Sarah F-4 instance 3, Rusty F-4 instance 6, Nathan F-4 instance N-8. **Classification: automatic lexer normalization** — D-27 (§8.2.2 line 549) inserts `/D./` into the projected form; D-26 (§8.2.2 line 534) inserts `/t./` into the realized form; both reach canonical `Γ(Α/i./t./D./G.)` before Layer-2 typing. Verified for both Γ rows.

**Charles F-4 instance C-3: ε uniform sole-dot `g.` at operator AND body, while θ/gate use ordinal `g1` (Axis 8 K=1 baseline).** Execution row: `[a.]ε(Α/i./o./g./e.) → { [Α/i./t./D./X./c.] + [Α/i./o./g./q.] }` — sole-dot `g.` at both the operator argument and the cost-deduction body term. The same cycle's θ row (`θ(Α/i./o./g1)`) and gate (`∋ [Α/i./o./g1/q.]`) use ordinal `g1`. **Classification: Axis 8 (R-execute operator-to-g_k resolution), K=1 baseline — notational, NOT a reproduction failure.** At K=1 the actor holds exactly one required-resource designation, so `R ⊖ [Α/i./o./g./q.]` resolves unambiguously despite the sole-dot (only one q can match). This is the unmarked-default end of the Axis 8 three-way variance (Charles K=1 sole-dot; Jim/Nathan sole-dot-operator/ordinal-body; Rusty uniform ordinal; Sarah uniform sole-dot at K>1 = the reproduction-failure sub-case). **Refinement to the Axis 8 Charles gloss:** the catalog currently glosses the K=1 baseline as "no ordinal to disambiguate, so sole-dot is the unmarked default." Charles's θ/gate rows demonstrably *use* ordinal `g1`, so the sole-dot at ε is a notational habit, not forced by ordinal-absence — Charles *has* the ordinal and drops it at ε anyway. The Axis 8 conclusion (sole-dot ε is notational, body resolves at K=1) is unaffected and arguably strengthened; the catalog's stated rationale should read "sole-dot is the unmarked ε form even where the same cycle's θ uses the ordinal" rather than "no ordinal to disambiguate." Filed under Axis 8 (§13.5.9).

**Per-leaf-path enumeration within ε rows:** Charles has **one** ε firing (single `/e.` leaf). No T14-style ε_1/ε_2 double-execution. K_exec = 1. Charles does not corroborate Sarah F-4 instance 4 (per-intention multi-execute); that remains Sarah-only.

**Narrative-column observation (out of F-4 notation scope, recorded for completeness):** the Obtained-resource row's narrative reads "…damaged Harry's credibility with the CFO and as a result **Randy** was fired" (PDF p.172) — but Charles's target throughout is the CFO and the removed party is **Harry**; "Randy" is a name from the Nathan engagement. This is a narrative-column transcription slip with **zero notational/mechanical consequence** (the Representation column `[a.]Θ(Α/i./O./Q.) := { [Α/i./Q.] }` is clean). Noted because the F-4 methodology forbids the universal-negative ("no inconsistencies") without recording what the scan saw; this one is narrative-only and does not enter the F-4 count.

**Scan conclusion: three F-4 instances** (C-1 standalone-`X.`-vs-δ-body, C-2 Γ-path, C-3 ε sole-dot/Axis 8), plus one narrative-column slip out of scope. Count set by the per-row + per-leaf-path walk; none pre-committed. Each instance cites its handling mechanism (§11.3 adoption; D-26/D-27; Axis 8).

#### §14.1.4 Validation outcome

Charles Table 5 establishes:

- **§13.1**: validated at the cycle layer; the δ-body-canonical adoption (§11.3) resolves the X1/X2-vs-`X.` source inconsistency. No multi-intention sole-dot reuse (K=1).
- **§13.2**: type preservation across the fourteen single-cycle lifecycle rules; Γ-paths handled by D-26/D-27. No Gap-§11.4 axis exercised (K=1).
- **§13.3**: congruence decidability abstractly (no non-trivial decision arises).
- **§13.4**: **per-cycle conservation only** (§13.4.2). Charles does NOT reach the §13.4.3 cross-cycle pinning — no escalation, no sub-cycle, no R-resume guard.
- **§13.5**: termination + progress for the minimal single-cycle sequence. Does NOT exercise the depth coordinate of μ (§13.5.2; subsumes old §13.5.5 well-bracketing) or the depth-≥1 levels of the depth-weighted induction (§13.5.4 well-foundedness + §13.5.6 conclusion; formerly old §13.5.6 arbitrary-depth induction).
- **§13.6**: **the clean determinism witness** — σ genuinely trivial (no discretionary fork of any kind), validated with NO open-gap contingency, unlike Sarah and Rusty.

Charles does **not** establish: any escalation property (depth-0, no sub-cycles), the §13.4.3 pinning, S-stack composition, multi-intention sequencing (any Gap-§11.4 axis beyond Axis 8's K=1 baseline), revision (J_C=0), or any failure-family rule (gate passes, perception validates). Those rest on the other four cases and the abstract §13 proofs.

**Honesty boundary (sharpest here).** Charles is the case §11 was fitted against row-by-row (§11.5). Its clean reproduction is guaranteed by construction and confirms fit, not correctness. The information Charles carries is in the three F-4 divergences (the X1/X2-vs-`X.` source inconsistency, the Γ-path normalization, the Axis 8 K=1 baseline) and in the **scope delimitation** — Charles is the lower bound of Part IV's coverage (single cycle, no escalation, trivial σ), the baseline against which the multi-intention, escalation, and depth-2 cases are the genuine stress tests.

### §14.4 Sarah — Tables 12–15 (depth-1, multi-intention, source-level ι↔Φ inconsistency)

Sarah Tables 12–15 document a four-table engagement: T12 (Sarah-Margaret parent cycle, part 1), T13 (Sarah-Beth depth-1 sub-cycle for g1's resource), T14 (Sarah-Srini depth-1 sub-cycle for g2's resource), T15 (Sarah-Margaret parent cycle, part 2 — execution and outcome after the sub-cycles resume). This case is where the template for Part IV is established; the trace below is the model subsequent §14.x sections follow.

#### §14.4.1 Case overview and structural skeleton

**Parent cycle** `ι(Α/i.)` (Sarah's interest: win the competition for the certification of achievement). **K_parent = 2** intentions: γ1 (alter judges' perception via Beth), γ2 (alter judges' perception of Srini). Both gates fail in T12 (`[a./R.] ∌ [Α/i./o./g1/q.]` line ~330 and `[a./R.] ∌ [Α/i./o./g2/q.]` line ~332), each spawning a depth-1 sub-cycle.

**Beth sub-cycle (T13)** `ι(Α/i./o./g1/i.) := { [Α/i./o./g1/q.] }` — parent-pending-q for g1, **pinning holds**. Beth's own gate passes (T13 line ~346, `[a./R.] ∋ [Α/i./o./g1/i./o./g./q.]`); Beth completes via R-perceive → R-select → R-outcome → R-obtained-utility → R-close-nested + Φ-flowback. The Φ-body delivers `[Α/i./o./g1/q.]` to R, satisfying the parent's resume guard.

**Srini sub-cycle (T14)** `ι(Α/i./o./g2/i.) := { [Α/i./o./g2/q.] }` initially — parent-pending-q for g2, **pinning holds**. The case's load-bearing feature: T14's New Interest row (book page 197) records `[a.]ι(Α/i./o./g2/i.) := { [Α/i./o./g2/i./Q.] }` — the revised ι-body is the sub-cycle's own obtained-Q, **not** parent-pending-q. **However, T14's Obtained-resource Φ-body** (book page 200) **is `[Α/i./o./g2/q.]`** — the *original* parent-pending-q, not the revised ι's reference. The dissertation records a sub-cycle whose Φ-body violates its own revised ι. **Sarah's J_C status is contingent on Gap-§11.7.2's (1)-vs-(3) classification, which is reopened per Block E** (see §14.4.3 instance 2 and §13.5.9 Gap-§11.7.2): under resolution (3), the revision is reframed as narrative-only relabeling and J_C = 0; under resolution (1), the revision is a substantive voluntary redirect and J_C = 1 (one R-objective-revise firing). The classification is not resolvable from p.119 alone; J_C ∈ {0, 1} pending the dissertation-internal contradiction's resolution.

**Parent cycle resumption (T15)** — after Beth's flowback delivers `[Α/i./o./g1/q.]` and Srini's delivers `[Α/i./o./g2/q.]`, the parent's S-stack pops twice (one R-resume per sub-cycle close-nested). The parent re-attempts its gates: T15 shows the parent executing **only Intention 1** (line ~382, `[a.]ε(Α/i./o./g./e.) → { ... }` — note the sole-dot path; per the dissertation's notation Srini's withdrawal mooted g2 such that Intention 2 didn't need to fire — Sarah's narrative on page 120 confirms: "Srini was eliminated as a potential competitor.").

**Engagement WF parameters** (Reading B):
- L = 1 (one top-level cycle).
- Parent: K_C = 2 (γ1, γ2), J_C ∈ {0, 1} contingent on Gap-§11.7.2's reopened classification (Block E), depth = 1.
- Beth: K_C = 1, J_C = 0, depth = 0 (Beth's own cycle doesn't escalate further).
- Srini: K_C = 1, J_C = 0, depth = 0.
- Maximum S-stack depth across engagement: D = 1.

Per-cycle bound (inline in §13.5.2's `rem_budget`, Axis-6-corrected formula 2026-06-24): `5·(1+0) + (4 + 4·Q_max)·K + 0 + 5 = 8K + 10` at Q_max = 1 (Sarah's functional-q_of specialization). **Parent (K=2): 26** (prior formula `6·K_C` undercounted Sarah's escalated intentions: 22 → 26; γ_1 escalates to Beth, γ_2 escalates to Srini before being mooted, both intentions consume the escalated-path firings). **Beth: 18** (16 → 18). **Srini: 18** (16 → 18). Engagement total ≤ 62 firings (loose). Finite under WF-1..WF-6.

#### §14.4.2 Per-theorem trace

**§13.1 path-uniqueness (DIVERGENCE — source violates uniqueness; system disciplines it).** Sarah's source tables exhibit a path-uniqueness violation that LSPI's representation has to renumber to resolve. **T12 declares both parent intentions at the same sole-dot path**: Intention 1 as `[a.]γ(Α/i./o./g.)` and Intention 2 also as `[a.]γ(Α/i./o./g.)`. Two distinct constituents at one syntactic path is exactly what §13.1's (W) direction forbids — the bijection requires `p₁ ≢ p₂ ⟹ denote_A(p₁) ≠ denote_A(p₂)`, contrapositively, two distinct constituents cannot share a path. **If LSPI took the source's paths literally, the second R-intention firing would fail its fresh-`g_k` premise** (`g.` is not fresh after the first firing already used it), and the system could not represent Sarah's K=2 structure at all.

The source's own resource rows (`θ(Α/i./o./g1)`, `θ(Α/i./o./g2)`) and sub-cycle interest declarations (Beth at `ι(Α/i./o./g1/i.)`, Srini at `ι(Α/i./o./g2/i.)`) use `g1` / `g2` distinctly — so the inconsistency is internal to the source: intentions notated `g.` / `g.`, their downstream resources / sub-cycles notated `g1` / `g2`. LSPI's representation renumbers the γ-rows to `γ(Α/i./o./g1)` and `γ(Α/i./o./g2)`, which (a) restores §13.1(W) by giving the two intentions distinct paths, (b) makes the γ-rows consistent with the θ-rows and sub-cycle prefixes, and (c) satisfies R-intention's fresh-`g_k` premise. Post-renumbering: per-actor scope holds (all paths within Sarah's agenda), the iN discipline gives `Α/i.` post-D-28 → `Α/i1` (Sarah has one top-level cycle), sibling-completeness holds for `g1` / `g2` post-renumbering, both bijection directions are satisfied.

**§13.1 as divergence, not clean validation.** Sarah's case demonstrates §13.1's discipline operating on a source that doesn't satisfy it: the bijection's (W) direction forces a renumbering the dissertation didn't perform, and that renumbering is what makes LSPI's representation possible. The honest claim is: "LSPI's representation of Sarah is the source renumbered to `g1` / `g2` so the system can represent the K=2 intentions at all"; the stronger weak-claim "LSPI validates §13.1 cleanly against Sarah" overstates what the trace establishes. **This is a stronger divergence than the T14 ι↔Φ relabeling (§14.4.3), and it's the load-bearing finding for what Sarah establishes about §13.1.**

**§13.2 type preservation.** Sarah's transition sequence at the system level fires R-open, R-interest, R-detect, R-objective, R-intention (×2 for γ_1 and γ_2 — both declared upfront per T12 lines 326 and 328, source-verified), R-required-resources (×2 for θ_1 and θ_2 — T12 lines 327 and 329, source-verified), R-gate (×2, both fail → R-spawn), R-spawn (×2 for Beth and Srini sub-cycles — both sub-cycles run per T13 and T14, source-verified), each sub-cycle's full lifecycle (T13 Beth, T14 Srini — including T14's two ε firings ε_1 and ε_2 per F-4 instance 4 below), R-close-nested (×2), R-resume (×2), R-gate post-resume for g_1 (passes — R contains [Α/i./o./g_1/q.] from Beth's Φ), R-execute(g_1) — parent's Intention 1 in T15 — then R-perceive, R-select, R-outcome, R-obtained-utility, R-close, R-flowback. **R-moot fires for γ_2** (T14's final row narrative explicitly states the sub-cycle's outcome "render[s] Intention 2 ... as moot"; §13.5/§13.6 dispositions updated below to reflect this). Every rule's contractum is well-typed at Layer 2 per §13.2.2's per-rule analysis. **§13.2's R-objective-revise case is not exercised** because Gap-§11.7.2 resolution status is reopened per Block E below (the (1)-vs-(3) call is unresolved against the source's p.119 vs T14 contradiction). **One mechanism-caveat (from §14.4.3 F-4 instance 3): Sarah's Γ-bodies as written in the source do not conform to the standard Layer-2 form** — the projected Γ rows drop `/D.` and the realized Γ rows drop `/t.`, while §11.4.5 / §11.4.9 both prescribe `Γ(Α/i./t./D./G.)`. **The §8.2.2 lexer normalizations D-26 (`/i?./D./` → `/i?./t./D./`, line 534) and D-27 (`/t./G.` → `/t./D./G.`, line 549) automatically insert the missing segments before parsing**, so Sarah's source Γ-bodies are normalized into the standard form at the lexer, and the normalized form passes Layer-2 type-check.

**Structural divergences surfacing §11.4 specification gaps** (Gap-§11.4-multi-intention-sequencing in §13.5.9, re-scoped per Block C source-verification):

1. **Batching gap.** Sarah's source declares γ_1, γ_2, θ_1, θ_2 and fails both gates **all before any sub-cycle runs** (T12 sequential rows). §11.4's failure family runs per-intention (gate-fail → spawn → resume → gate-pass → execute), with no clear path for "after gate_1 fails and R-spawn fires for Beth, the cycle goes back to declare θ_2 and fail gate_2 before Beth completes." The source's batching pattern isn't representable under §11.4's literal lifecycle.

2. **Moot disposition gap.** After both sub-cycles flow back (R contains both parent-pending-q's), the source executes g_1 (T15) and **moots g_2** (T14's last row). §11.4 has R-moot as a discretionary exit (operator-attested premise becoming void), which fits — but the "void by sub-cycle's outcome" trigger isn't a current R-moot premise position. Currently R-moot fires from any state via operator attestation; making the system's representation of Sarah's case requires R-moot firing for γ_2 at the parent's post-resume position, where the operator (Sarah) attests that g_2's substantive need has been resolved (Srini withdrew). **This works under R-moot's discretionary trigger**, but the discretionary firing means σ at this point is non-trivial (operator picks R-moot over R-gate-then-execute).

3. **Per-intention multi-execute gap.** Within T14's Srini sub-cycle, the source records **two distinct execute operations** (`ε_1` at `/e1` leaf and `ε_2` at `/e2` leaf) for the single γ. §11.4's R-execute premise (`last = ⟨gate-pass, q⟩`) fires once per gate-pass; after ε_1 fires, `last = ε_1-body` and R-execute cannot re-fire. The source's two-execute-per-intention pattern isn't representable. Filed as F-4 instance 4 below and as a sub-aspect of Gap-§11.4.

§13.2 type-checks the per-rule contractums correctly for the rules that fire (R-spawn, R-close-nested, R-resume, R-execute, R-perceive, R-select, R-outcome, R-obtained-utility, R-close, R-flowback, R-moot — all well-typed per §13.2.2). The structural gaps above are §11.4 specification issues, not §13.2 failures.

**§13.3 congruence decidability.** Sarah's Σ-clauses (T12 line 324, T15 line 384: `[Α/i./t.]Σ(Α/i./t./D.)′ → [Α/i./t./S./P.]′`) parse and type to standard Layer-3 forms. **Source Γ-bodies as written do not** — the source's `/t./G.` (projected) and `/D./G.` (realized) forms diverge from the standard `/t./D./G.` (F-4 instance 3). **D-26 (§8.2.2 line 534) normalizes the realized Γ form by inserting `/t./`; D-27 (§8.2.2 line 549) normalizes the projected Γ form by inserting `/D./`**; both source variants reach Layer 2 in canonical `/t./D./G.` form after the lexer. The normalized forms then read through `last`-matching with no non-trivial congruence-decision step. **§13.3 validated abstractly (decidability holds for any inputs Sarah's case produces after normalization); the normalization is performed by D-26 / D-27 at the lexer per §8.2.2.**

**§13.4 resource conservation (source-verified two-sub-cycle reading per Block A).** Sarah's R-multiset evolves through **both sub-cycles** (T13 Beth and T14 Srini both run; verified against source rows):

- **Beth sub-cycle (T13, g_1 escalation)**: R-execute deducts `cost([Α/i./o./g_1/i./o./g./q.])` (Beth's already-held information about her own career goals); R-close-nested adds Φ-body `{ [Α/i./o./g_1/q.] }` (parent-pending-q for g_1 delivered, pinning holds).
- **Srini sub-cycle (T14, g_2 escalation)**: R-execute fires **twice** (T14 records ε_1 at `/e1` and ε_2 at `/e2` for the single γ; this is F-4 instance 4 below — §11.4's R-execute fires once per gate-pass, the source's two-execute pattern is a per-intention multi-execute divergence). The sub-cycle's combined deduction is `cost([Α/i./o./g_2/i./o./g./q.])` (whichever single q-token §11.4's representation tracks; source has the resource consumed across both executes). R-close-nested adds Φ-body `{ [Α/i./o./g_2/q.] }` (parent-pending-q for g_2 delivered, pinning holds; T14 line 374 source-verified).
- **Parent post-resumes**: both R-resume's fire (after Beth's close-nested and after Srini's close-nested), bringing R back at the parent with both parent-pending-q's present. **R-execute(g_1) fires** (T15 line ~382 source-verified, `ε(Α/i./o./g./e.) → { ... }` — used in the Tim → Margaret influence chain). **R-moot fires for g_2** (T14's last-row narrative source-verified: "render Intention 2 ... as moot"). R-flowback adds `{ [Α/i./Q.] }` (certification of achievement obtained).

**Pinning check (§13.4.3): both sub-cycles deliver Φ-body = parent-pending-q literally.** Beth's Φ is `[Α/i./o./g_1/q.]`; Srini's Φ is `[Α/i./o./g_2/q.]`. The required-q ↔ earned-Q pinning holds at both depth-1 escalations. Conservation: no leak (every deduction matched by a prior addition or by R₀); no duplication (single-spawn-per-g_k via fresh-`g_k`, two sub-cycles target different g_k). **§13.4 validated at depth 1 with the pinning exercised at both sub-cycles.**

**Note on the §11.4 batching gap (Gap-§11.4 / Block C):** while §13.4's conservation holds against the source two-sub-cycle reading, §11.4's literal lifecycle doesn't cleanly represent the source's batching order (both gates fail before either sub-cycle spawns; both sub-cycles run before parent executes). Conservation's correctness doesn't depend on which order §11.4 ultimately pins; the §13.4 trace works under either the batched representation (if §11.4 is extended to admit it) or the interleaved representation (if Sarah's case is reframed accordingly).

**§13.5 termination + progress (corrected per Blocks A/B).** WF-1 (K_C bounded per cycle: parent K=2, Beth K=1, Srini K=1; both parent intentions are executed-or-mooted per source — g_1 executes via R-execute, g_2 exits via R-moot), WF-2 (J_C depends on Gap-§11.7.2 resolution which is reopened per Block E), WF-3 (D=1, sub-cycle depth bounded), WF-4 (L=1, single top-level cycle). Per-cycle bound finite; engagement total finite. Progress at every state: parent's gate-fails route to R-spawn (deterministic by R ∌ q); sub-cycles' gates pass (R ∋ q → R-gate fires); R-resume's `R ∋ parent-pending-q` premise holds post-flowback (pinning gives literal multiset membership). **R-moot fires for g_2 at the parent's post-resume state** — Srini's sub-cycle outcome made Intention 2's goal substantively achieved (Srini withdrew from competition), and the operator (Sarah) attests the parent's premise for executing g_2 has become void. R-moot's `any state from which the principal elects not to continue` premise admits this. **The mooted g_2 is a clean failure-family exit, not an orphan** — §13.5.5's progress (renumbered from old §13.5.3 under Thread A) holds at the moot-marker position (the parent's terminal exit is via R-flowback after R-execute(g_1); g_2's branch terminates at R-moot, which doesn't transition C or block R-flowback). No stuck states; no infinite sequences; termination holds. **§13.5 validated; the multi-intention K-loop is exercised at K=2 in the parent (γ_1 → R-execute, γ_2 → R-moot), with both intentions reaching terminal-state dispositions.**

**§13.6 determinism (contingent — corrected per Block B).** Sarah's σ is **non-trivial**: R-moot fires for g_2 at the parent's post-resume state (Block B / B-corrected reading), and R-moot's operator-discretionary trigger means **σ has a genuine choice point at this position** (R-moot vs R-gate-then-execute-then-perceive for g_2). The operator chose R-moot in Sarah's case (per T14's narrative); under a different operator's choice σ would route through execute-and-perceive. **σ is therefore not effectively trivial for Sarah.**

**Additional state-fork dispositions per §1.4.5 (post-state-fork pivot).** Beyond the post-resume R-moot defect (Axis 4 legacy) that the prior paragraph established, Sarah's lifecycle reaches two additional states the §1.4.5 table classifies:

1. **`last = γ_1-body` single-γ state**: R-intention(γ_2) and R-required-resources(θ_1) both admissible; **licensed σ-discretion per §1.4.5** (Sarah and Nathan pick R-intention first; Rusty picks R-required-resources). The σ choice is the actor's strategic stance; determinism holds per fixed σ.
2. **`last = γ_2-body` multi-γ state (was Site (i) defect, Axis 1b legacy — RESOLVED 2026-06-23)**: §11.4.6's pending-θ-set premise admits θ_1 from this state (PendingTheta = {γ_1, γ_2}, earliest-declared = γ_1). Sarah T12 row 12 reproduced. Prior `last`-keyed premise's structural unreachability of Sarah's θ_1 firing is no longer in effect.
3. **`last = ε-body` no-γ-pending state**: per §1.4.5 row 123, this is **guard-determined (Pillar 2)** — R-perceive vs R-perceive-failure selected by the operator's reading of the realized comparison, not by σ. The prior "R-intention vs R-perceive at ε-body" framing was the phantom dissolved per §1.4.5 (no case witnesses R-intention firing from `last = ε-body`; Axis 2's content re-located to `⟨perceive-failure, C⟩`).

The σ-discretion at `γ_1-body single-γ` produces materially different transition sequences across cases (upfront-batch vs interleaved); the σ at §13.6 carries the operator's choice. The Site (i) defect that previously blocked Sarah's θ_1 firing was resolved 2026-06-23 by §11.4.6's pending-θ-set premise.

**§13.6 status for Sarah: contingent on Axis 4 only (post-2026-06-23).** The Site (i) defect has been resolved — Sarah's θ_1-before-θ_2 firing at `last = γ_2-body` is now mechanically admissible (R-rr fires for `earliest-declared γ ∈ PendingTheta = {γ_1, γ_2}` = γ_1). The remaining §13.6 contingency for Sarah is the post-resume operator-attested R-moot defect (Axis 4 legacy): §11.6.6's cycle-scoped `⟨moot, C⟩` contractum doesn't supply the intention-scoped moot the source needs (T14 moots Intention 2 while T15 closes the cycle on Intention 1). **§13.6 for Sarah K=2 = §13.6 abstract result + Axis 4 §11.6.6 fix (or structural reframe)**, with Sites (i) and (ii) no longer contingencies. Filed under Gap-§11.4-multi-intention-sequencing in §13.5.9 (thin pointer to §1.4.5 state-fork table and LPIC-Part-IV-prep.md Section I).

#### §14.4.3 Source-level inconsistencies surfaced (F-4 instances)

**Methodology note (template-level, applies to every §14.x case).** The F-4 step for each case is **an explicit scan of every γ / θ / ι / ε / Γ / Σ / Φ row** for path consistency (g-numbering, sole-dot vs ordinal, path-spacing artifacts, prefix consistency across nested levels, conformance to the §11.4 / §11.6 rule contractums' standard path forms), with divergences listed per case. **Three failure modes the methodology must rule out, named through Sarah's iterated correction history**:

1. **"Assert clean unless something jumps out"** — the universal-negative-without-scanning pattern: writing "no inconsistencies" without scanning the rows that would falsify it. The initial Sarah draft made this error: "no other source-level inconsistencies" was asserted without scanning T12's γ rows (which would have surfaced F-4 instance 1's g./g1/g2 issue).

2. **"Scan the rows but pre-commit the count"** — the count-before-scan-completes pattern: writing "N instances total; no other" after a scan that didn't cover every row or every leaf-path within a row. **Two worked instances so far in this very subsection, V-1 and the present re-scan**: (a) V-1 wrote "two instances total" before the Γ-rows had been scanned (surfaced F-4 instance 3); (b) the V-2-era scan wrote "three instances total" after a per-row walk that glanced at T14's ε row but didn't enumerate its **leaf paths** — missing the ε₁/ε₂ pair that became F-4 instance 4. Both pre-commitments named a number that turned out incomplete; both were caught by re-scan. **Per-row alone isn't sufficient — the walk has to descend into per-leaf-path enumeration within every row that carries leaf ordinals (notably ε, but in principle any ordinal-bearing leaf).** The methodology note must teach the live lesson, not just the prior one; this paragraph is the live correction record for the §14.4.3 scan that produced it.

3. **"Assert a handling mechanism without citing it"** — the mechanism-without-verification pattern: writing "normalization-handles this" or "a rule covers this" without citing which specific §8.2.2 normalization or §11.4 rule does the work. The V-2 correction made this error: "LSPI's representation normalizes Sarah's Γ paths to the standard form" asserted a mechanism without citing it. The V-3 review then caught the assertion — and **the verification itself was symmetric**: D-26 and D-27 of §8.2.2 (segment-insertion rules) DO exist and DO handle instance 3 automatically, contrary to a prior characterization of D-26/27/28 as only "sole-dot ↔ ordinal" (D-28 is sole-dot ↔ ordinal; D-26 and D-27 are segment-insertion). The discipline catches both the assertion-without-verification (positive form) and the rule-out-without-verification (negative form) — both are the same shape, both must be verified.

**Generalization for all §14.x scans.** Every claim in the trace gets verified against the source or the spec before it's written. That includes (a) the *cleanliness* assertion (V-0 lesson), (b) the *count* claim (V-1 lesson), (c) the *classification* of each divergence and any "X handles this" mechanism assertion (V-2/V-3 lesson). The scan SETS the count by walking every row; each divergence's classification CITES the specific §8.2.2 / §11.4 rule that handles it (with line number), or explicitly states "no rule exists; this is a manual representation correction the analyst applies before the system can represent the case." Neither positive nor negative assertions about handling mechanisms are made without the §-citation backing them.

**Subsequent §14.x cases (Nathan, Rusty, Charles, Jim) follow this strengthened methodology**: per-row walk, divergences listed without pre-commitment, each classified with the cited handling mechanism (rule + line number) or explicit "no rule, manual correction."

**Sarah F-4 instance 1: T12 parent intentions notated at the same sole-dot path (the stronger §13.1 divergence; classification: manual representation correction, no lexer rule handles it).** T12 declares both Intention 1 and Intention 2 as `[a.]γ(Α/i./o./g.)` — identical paths for two distinct constituents. The downstream resource rows (`θ(Α/i./o./g1)`, `θ(Α/i./o./g2)`), sub-cycle interest declarations (Beth at `ι(Α/i./o./g1/i.)`, Srini at `ι(Α/i./o./g2/i.)`), and T15's parent execution row (`ε(Α/i./o./g./e.)`, cost `[Α/i./o./g./q.]` — sole-dot again) are internally inconsistent across γ vs θ/ι/ε/Φ notation. **No §8.2.2 lexer rule covers this normalization**: D-28 (§8.2.2 line 560) handles sole-dot ↔ ordinal **only at the agenda root** (`Α/i.` → `Α/i1`) and explicitly does not apply to sub-cycle or γ-level sole-dot (§11.4.2's sub-cycle branch and §8.2.2 line 562 both state this). The g./g. → g1/g2 distinction is driven by **R-intention's fresh-`g_k` premise (§11.4.5)** as a representation-level correction the analyst applies before the system can represent Sarah's K=2 intentions at all. See §14.4.2's §13.1 trace for the full divergence analysis. **The dissertation's source violates §13.1's uniqueness in the γ rows; the system is the more disciplined of the two, and the discipline operates via R-intention's freshness premise (representation-level), not via lexer normalization** — this is the load-bearing §13.1 finding for Sarah.

**Sarah F-4 instance 2: T14 ι↔Φ violation.** The revised ι is `{ [Α/i./o./g2/i./Q.] }` (T14 New Interest row, book page 197), but the obtained-resource Φ-body is `{ [Α/i./o./g2/q.] }` (T14 Obtained resource row, book page 200). Under the normal-path ι↔Φ identity (§11.1), Φ-body should equal the operative ι-body; the dissertation records them as different. The relabeling-vs-redirect classification (Gap-§11.7.2, resolution (1) vs (3)) is **reopened** per Block E: p.119's narrative chapter ("Sarah had a simple plan…") supports dissuasion-planned-from-the-start → relabeling → (3), while T14's own detection-row narrative (book page 196: "upon … a conversation with Srini, Sarah discovered that a different approach would be preferable") supports a mid-conversation voluntary redirect → (1). These are a source-internal contradiction; Q2 is also mixed (Φ-label matches original parent-pending-q → (3); its R-moot effect on Intention 2 per Block B is a substantive parent change → (1)). The classification is not resolvable from p.119 alone. See §13.5.9 Gap-§11.7.2 for the reopened analysis and cross-§13 cost.

**Sarah F-4 instance 3: Γ-path divergence from the §11.4.5 / §11.4.9 standard form (a §13.1(W)-shape divergence of inverse shape from instance 1).** Sarah's source has Γ rows in two systematic patterns that both diverge from the system's standard `Γ(Α/i./t./D./G.)`:

- **Projected (intention) Γ rows drop `/D.`**: T12 line 41/55, T13 line 127, T14 line 258 use `Γ(Α/i./…/t./G.)′` instead of `Γ(Α/i./…/t./D./G.)′`.
- **Realized (perception) Γ rows drop `/t.`**: T13 line 156, T14 line 326, T15 line 398 use `Γ(Α/i./…/D./G.)` instead of `Γ(Α/i./…/t./D./G.)`.

§11.4.5 R-intention's contractum (line 1842) and §11.4.9 R-perceive's contractum (line 1910) both prescribe `Γ(Α/i./t./D./G.)` at the **same path modulo prime** — projected (primed) and realized (unprimed) are denotationally one constituent (the same Γ-operator at the same address, with prime distinguishing projection from realization). Sarah's source therefore places **one constituent at two non-congruent paths** (`Α/i./t./G.` for projected, `Α/i./D./G.` for realized) — which is exactly what §13.1(W) forbids in inverse-shape from instance 1 (instance 1: two constituents at one path; instance 3: one constituent at two paths).

**Classification: handled automatically by §8.2.2 lexer normalizations D-26 and D-27** (cited mechanism, verified). **D-26 (§8.2.2 line 534) fires on `/i?./D./` and inserts `/t./`** — handles Sarah's realized Γ rows: `Γ(Α/…/i./D./G.)` → `Γ(Α/…/i./t./D./G.)`. **D-27 (§8.2.2 line 549) fires on `/t./G.` and inserts `/D./`** — handles Sarah's projected Γ rows: `Γ(Α/…/t./G.)′` → `Γ(Α/…/t./D./G.)′`. Both source-form Γ-paths are normalized into the canonical `Γ(Α/i./t./D./G.)` form at the lexer, before Layer 2 typing. **The normalization is automatic and spec'd; no manual representation correction is required for instance 3** (in contrast to instance 1, where no lexer rule applies and R-intention's freshness premise drives the analyst correction).

**Cross-check on the interpretation.** The classification "one constituent at two paths" depends on the projected-Γ / realized-Γ "same constituent modulo prime" reading, which the system's rules commit to (both use the same Γ-name, same path). The alternative reading ("two distinct constituents — projected perception vs realized perception — legitimately at different paths") is not supported by the rule contractums: §11.4.5 line 1845 (contractum; line 1842 is the well-typedness premise) uses `Γ(...)′` (primed) and §11.4.9 line 1910 (contractum) uses `Γ(...)` (unprimed) at identical paths, treating prime as the projected/realized discriminator, not the path. So Sarah's source's divergence-from-the-rule-contractum is a real §13.1(W)-shape issue under the system's intended reading, and the resolution (D-26 + D-27 normalization) carries the system's discipline into a representation that satisfies §13.1.

**Sarah F-4 instance 4: T14 double-execution ε_1 / ε_2 within a single γ (per-intention multi-execute divergence; caught by re-scan, missed by the initial scan that asserted "Three instances found").** T14 records **two distinct execute operations** within Srini's single-γ sub-cycle: `[a.]ε_1(Α/i./o./g_2/i./o./g./e_1) → { [Α/i./o./g_2/i./t./D./X./c.] + [Α/i./o./g_2/i./o./g./q.] }` and `[a.]ε_2(Α/i./o./g_2/i./o./g./e_2) → { [Α/i./o./g_2/i./t./D./P./b.] + [Α/i./o./g_2/i./o./g./q.] }` — two ε operators at two distinct leaf paths (`/e_1` and `/e_2`). §11.4's R-execute premise (`last = ⟨gate-pass, q⟩`, line 1891) fires once per gate-pass marker; after ε_1 fires, `last = ε_1-body` and R-execute cannot re-fire because the gate-pass marker is no longer `last`. **The source's two-execute-per-intention pattern isn't representable** under §11.4's literal lifecycle. Classification: **no rule handles two ε per gate-pass; manual representation correction or §11.4 spec extension**. Filed as a sub-aspect of Gap-§11.4-multi-intention-sequencing in §13.5.9.

**Scan conclusion (set by the scan, count corrected from "three" to four after re-scan caught T14's ε_1/ε_2; methodology failure documented).** The initial §14.4.3 scan walked the ε rows of T13/T14/T15 and reported "ε paths ... internally consistent with their respective sub-cycle prefixes" — flagging only T15's sole-dot as instance 1's downstream propagation. **The scan missed T14's two-ε pattern** (ε_1 and ε_2 at distinct leaf paths within Srini's sub-cycle). This is exactly failure mode (a) or (b) from the methodology note above (assert clean unless something jumps out / scan partially but commit a count), occurring in the finalized template that was about to propagate to Nathan and Rusty. **Re-scan caught it; the methodology must include explicit per-leaf-path verification within each ε row, not just per-row glance.**

**Four instances found at re-scan completion, each with a cited handling mechanism**:

- **F-4 instance 1** (γ-row sole-dot reuse → §13.1(W) violation, source side): **manual representation correction** driven by R-intention's fresh-`g_k` premise (§11.4.5). **No lexer rule covers it**; D-28 (§8.2.2 line 560) handles only agenda-root sole-dot, not γ-level sole-dot.
- **F-4 instance 2** (T14 ι↔Φ violation → Gap-§11.7.2 (1)-vs-(3) basis, **reopened per Block E**): the (1)-vs-(3) classification is **unresolved against the source's contradiction**. p.119 narrative (Sarah's "simple plan" was dissuasion from the start) supports relabeling → (3); T14's detection-row narrative ("upon after a conversation... Sarah discovered that a different approach would be preferable") supports voluntary redirect → (1). The draft's prior citation of p.119 alone was one-sided. Q2 (what the revision produced) is similarly mixed: Φ-label matches original parent-pending-q (→3), but its effect (R-moot for Intention 2 per Block B) is a substantive parent change (→1). **Honest status: (1)-vs-(3) reopened pending the dissertation-internal contradiction's resolution.** This re-prices §13.5.9's cross-§13 cost analysis for Gap-§11.7.2 — resolution (1) was flagged as expensive (reopens §13.4.3 and §13.5.5 for the voluntary case); it now has more weight at the dissertation-evidence axis than the draft acknowledged.
- **F-4 instance 3** (Γ-path divergence → §13.1(W)-inverse-shape): **automatic lexer normalization** via D-26 (§8.2.2 line 534, inserts `/t./` for realized Γ) and D-27 (§8.2.2 line 549, inserts `/D./` for projected Γ). Verified.
- **F-4 instance 4** (T14 per-intention double-execute → §11.4 multi-execute gap): **no rule handles two ε per gate-pass**; filed as sub-aspect of Gap-§11.4-multi-intention-sequencing. Manual correction or §11.4 extension required.

The count is what the (re-)scan returned; no instance was anticipated before the row-walk reached it. **Each classification cites the specific mechanism (rule + §-line, or "no rule, manual correction" with named premise driver); none asserts a mechanism without verification. The "three instances" prior conclusion was itself an instance of failure mode (b) — a count pre-committed before the scan reached T14's ε leaf paths**; the re-scan correction is itself the discipline operating on the template's prior assertion.

#### §14.4.4 Validation outcome

Sarah Tables 12–15 establish:

- **§13.1**: **divergence case** — the source violates uniqueness at the γ rows (both Intentions notated at the same sole-dot `g.`); LSPI's representation renumbers to `g_1` / `g_2` to satisfy R-intention's fresh-`g_k` premise and §13.1(W). Sarah demonstrates §13.1's discipline operating on a non-conforming source, not a clean source that the discipline confirms.
- **§13.2**: type preservation across two R-spawn / R-close-nested / R-resume pairs (Beth and Srini sub-cycles both run, per Block A source-verification). R-objective-revise status reopened pending Gap-§11.7.2's (1)-vs-(3) resolution (per Block E). Γ-path conformance handled by D-26 + D-27 (§14.4.3 instance 3). T14's per-intention double-execute (F-4 instance 4) is a structural divergence §11.4 doesn't represent.
- **§13.3**: congruence decidability (abstractly; no non-trivial congruence decision arises post-D-26/D-27 normalization).
- **§13.4**: resource conservation with the pinning explicitly held at **two** depth-1 escalations (Beth's Φ-body = parent-pending-q for g_1; Srini's Φ-body = parent-pending-q for g_2; both source-verified per Block A). Conservation correct under the system's two-sub-cycle reading; the §11.4 batching gap (Gap-§11.4 / Block C) is a representation-order issue, not a conservation issue.
- **§13.5**: termination + progress for K=2 parent with two depth-1 escalations, parent executes g_1 (R-execute) and moots g_2 (R-moot — per Block B source-verification of T14's "render Intention 2 ... as moot" narrative).
- **§13.6**: **contingent, not validated** — per §1.4.5's state-fork derivation (post-2026-06-23 §11.4.6 revision), Sarah's lifecycle reaches the **post-resume operator-attested R-moot defect** (Axis 4 legacy: §11.6.6's cycle-scoped contractum cannot supply the intention-scoped moot the source needs). The `γ_2-body` Site (i) defect was RESOLVED 2026-06-23 by §11.4.6's pending-θ-set revision; Sarah's θ_1 firing at this state is now mechanically admissible. Sarah's `γ_1-body single-γ` state is licensed σ-discretion (Sarah picks R-intention first), not an open fork. The prior framing of "two unresolved ordering forks at `γ-body` and `ε-body`" was superseded: `γ-body` single-γ is licensed, `γ-body` multi-γ is resolved by §11.4.6, and `ε-body` was the phantom dissolved per §1.4.5 (Axis 2 re-located, guard-determined Pillar 2 surface). **§13.6 for Sarah now requires only the Axis 4 §11.6.6 fix (or structural reframe)** — down from "Site (i) §11.4.6 fix AND Axis 4 §11.6.6 fix" prior to the 2026-06-23 revision.

Sarah does **not** establish: R-objective-revise's lifecycle-reset (status depends on Gap-§11.7.2 (1)-vs-(3) reopened per Block E), depth-≥2 nesting (max D=1), parent-retry-after-sub-cycle-failure (both sub-cycles succeed). Those properties are tested by no Sarah trace; they rest on (a) Nathan T7–9 for depth-2 (§14.3), and (b) the abstract §13 proofs alone for R-objective-revise (pending resolution) and parent-retry.

**Open §11 specification gaps Sarah's system-level trace surfaces** (filed in §13.5.9):

- **Gap-§11.4 batching** (Block C): §11.4's failure family runs per-intention; the source's batching of two gate-fails before either sub-cycle spawns isn't representable. Three resolution options (a) extend §11.4 to admit batching, (b) reframe as sequential top-level cycles, (c) accept as fidelity divergence — all need re-pricing against the now-source-confirmed two-sub-cycle-run reality (option (b) is weakened: Sarah's two escalations feed one parent outcome, not two independent cycles).
- **Gap-§11.4 moot-by-sub-cycle-outcome** (Block B): the source moots g_2 at the parent post-resume state via Sarah's attestation that Srini's withdrawal made g_2 substantively achieved. §11.4's R-moot trigger (operator-attested premise-void) admits this, but makes σ non-trivial at the parent's post-resume position.
- **Gap-§11.4 per-intention multi-execute** (Block D / F-4 instance 4): T14's two ε firings within one γ aren't representable under §11.4's once-per-gate-pass R-execute premise.
- **`last = ε-body` was the phantom Axis 2** (Block C secondary, now dissolved per §1.4.5): no case witnesses R-intention firing from `last = ε-body`; Axis 2's intention-addition content re-located to `⟨perceive-failure, C⟩`. R-perceive vs R-perceive-failure at `last = ε-body` is guard-determined (Pillar 2), not σ-sequenced.
- **Gap-§11.7.2 (1)-vs-(3) reopened** (Block E): p.119 vs T14 contradiction means the relabeling-vs-redirect classification isn't cleanly resolvable from p.119 alone.

**Template note: Sarah's §14.4 is held open pending §11 disposition of Sarah-specific Gap-§11.4 axes 3–5, NOT pending Rusty's trace.** Rusty's pre-§14.5 source walk (T16 → T18 → T20) showed γ_2 declared after R-perceive(γ_1) and γ_3 declared after R-perceive-failure(γ_2) — the §11.4.5 interleaved pattern verbatim. **Rusty does not validate Sarah's batched two-escalation pattern, and does not reproduce Sarah's R-moot disposition or Sarah's T14 double-execute.** Rusty narrows Gap-§11.4 by isolating Axes 3 (batching), 4 (moot-by-sub-cycle-outcome), and 5 (per-intention multi-execute) as Sarah-specific outliers. Sarah's §14.4 finalization waits on §11's disposition of those three axes (which may settle in any of: §11.4 extension to admit batched declarations; reframing Sarah's K=2 narrative as outside the system's representation; or accepting Sarah as a fidelity divergence parallel to Gap-§11.7.2). The prior "Rusty settles Sarah's batching" framing is rejected per Rusty's source walk.

**Four F-4 instances for Sarah** (count set by the re-scan that corrected the prior "three"; each with cited handling mechanism):

1. **T12 γ-row sole-dot reuse** — §13.1(W) violation, two constituents at one path. Manual representation correction via R-intention's fresh-`g_k` premise (§11.4.5); no lexer rule applies.
2. **T14 ι↔Φ violation** — Gap-§11.7.2 (1)-vs-(3) **reopened** (Block E); p.119 vs T14 source-internal contradiction, not resolvable from p.119 alone.
3. **Γ-path divergence** (projected drops `/D.`, realized drops `/t.`) — §13.1(W)-inverse-shape. Automatic lexer normalization via D-26 (§8.2.2 line 534) and D-27 (§8.2.2 line 549); verified.
4. **T14 double-execution ε₁/ε₂ within one γ** — per-intention multi-execute. No §11.4 rule admits two ε per gate-pass; filed under Gap-§11.4. Manual correction or §11.4 extension (or reframe as one ε-body with two effect-clauses).

Instances 1 and 3 are complementary §13.1(W) divergences (two constituents/one path; one constituent/two paths), disciplined at two layers (R-intention freshness; D-26/D-27 lexer). Instances 2 and 4 are open §11 questions, not clean validations. **The count was corrected three→four by re-scan; that correction is itself the discipline operating on the template's own prior assertion.** Subsequent §14.x cases inherit §14.4.3's strengthened scan — explicit per-row **and per-leaf-path** walk, count set by the scan, classifications cited.

**The Sarah trace establishes the validation template** for Part IV: structural skeleton (parameters + per-cycle structure), per-theorem trace (§13.1 through §13.6 with explicit pinning checks where relevant), source-level inconsistencies (F-4 instances catalogued case-by-case), and validation outcome (what the case empirically establishes vs what it leaves to the abstract proofs). Sections §14.1 (Charles), §14.2 (Jim), §14.3 (Nathan), §14.5 (Rusty) follow this template; §14.9 records the cross-case findings catalog.

### §14.5 Rusty — Tables 16–22 (depth-1 multi-spawn via interleaved K=3; R-perceive-failure-driven; source-verified)

Rusty Tables 16–22 document a seven-table engagement: T16 (Rusty-Todd parent, Part 1 of 4), T17 (Rusty-Erik depth-1 sub-cycle for g_1's q_2), T18 (Rusty-Todd Part 2 of 4 with γ_1 execute + γ_2 declaration), T19 (Rusty-Erik depth-1 sub-cycle for g_2's q), T20 (Rusty-Todd Part 3 of 4 with γ_2 execute + R-perceive-failure + γ_3 declaration), T21 (Rusty-Gerry depth-1 sub-cycle for g_3's q), T22 (Rusty-Todd Part 4 of 4 with γ_3 execute + outcome).

**Rusty's structural significance**: this is the **interleaved K=3 validator** for §11.4.5's line 1850 dynamic-intention-addition pattern. The source declares γ_2 after R-perceive(γ_1) and γ_3 after R-perceive-failure(γ_2) — the §11.4.5 firing positions "after R-execute" and "after R-perceive-failure" verbatim. Combined with depth-1 multi-spawn (three sub-cycles, one per intention; all three sub-cycles run to completion; T19 and T21 deliver parent-pending-q literally, while T17's delivery raises Gap-§13.4.3-resume-guard-designation-variance — Erik returns sole-dot `q.` against parent-pending-q ordinal `q_2`, see §14.5.3 instance 2 and §13.5.9 entry), Rusty validates K>1 in a way Sarah does not: the **interleaved pattern is canonical under §11.4.5**, and Sarah's batched-with-moot pattern is the unrepresentable outlier (per Gap-§11.4 Axes 3–5, isolated to Sarah by Rusty's source walk).

Rusty also surfaces two new structural findings the source walk made unavoidable: (a) **Gap-§13.4.3-resume-guard-designation-variance** — Erik's T17 Φ-body delivers sole-dot `q.` while parent-pending-q is ordinal `q_2`, breaking R-resume's literal multiset membership test at a different point in the §13.4.3 pinning chain than Sarah's ι↔Φ violation; and (b) **Gap-§11.4 Axis 6** — T16's two-θ-for-one-γ structure stacks three under-specifications (R-required-resources can't re-fire, R-gate has no multi-q semantics, and R-spawn's target-identification only works under one of the two unlicensed gate-firing readings).

#### §14.5.1 Case overview and structural skeleton

**Parent cycle** `ι(A/i.)` (Rusty's interest: protect morale + gain CEO credibility; agenda "Indirectly persuade Todd to leave voluntarily"). **K_decl = 3** intentions, **declared interleaved** across T16/T18/T20:

- **γ_1 declared T16** (book page 204): "Create a new work environment such that would require more work for Todd."
  - **Two required resources at the same intention path** (`θ(A/i./o./g1)` rows, both at g_1 ordinal — Axis 6 Layer A under-spec):
    - **q_1** ("Authority to change communication procedures", book page 204): gate ∋ q_1 (held by Rusty as VP).
    - **q_2** ("Authority to change requisition policies", book page 205): gate ∌ q_2 (requires CFO/CEO authorization). Escalate to T17 Erik.
- **T17 Erik sub-cycle** (book pages 205–208): `ι(A/i./o./g1/i.) := { [A/i./o./g1/q2] }` — **pinning holds at start** (sub-cycle's ι is parent-pending-q `q_2` literally). Sub-cycle runs through detection / objective / intention / required-resources / gate-pass / execute / perceive / outcome to obtained-resource. **Φ-body delivers `{ [A/i./o./g1/q.] }`** (sole-dot, NOT q_2 — **Gap-§13.4.3-resume-guard-designation-variance pinning failure at delivery**, see §14.5.3 instance and §13.5.9 entry).
- **T18 Rusty resumes** (book pages 208–209): R-resume's literal multiset membership test on `[A/i./o./g1/q2]` against R containing `[A/i./o./g1/q.]` is the open Gap-§13.4.3-resume-guard-designation-variance case. The dissertation continues as if the resume passes:
  - **R-execute(γ_1)**: `ε(A/i./o./g1/e.) → { [A/i./t./D./X./c.] + [A/i./o./g1/q1] + [A/i./o./g1/q2] }` (book p208, **source-verified during §14.3.4 corpus ε sweep**) — single execute row, body lists both q_1 and q_2 cost designations. Uniform ordinal at operator AND body — the disciplined form per Axis 8 in §13.5.9.
  - **R-perceive-failure(γ_1) fires**: the realized perception is `[A/i./D./P1/u.] ≤ [A/i./D./X./u.]` (Todd voices displeasure but does not yet prefer leaving; PDF p.208). The realized comparison does not validate γ_1's projected `>`; R-perceive-failure writes `⟨perceive-failure, C⟩` to last.
  - **γ_2 declared after R-perceive-failure(γ_1)** — §11.4.5 line 1841's premise admits `⟨perceive-failure, C⟩`. This is what licenses γ_2's declaration mechanically; γ_2's reachability does NOT depend on perceiving from `last = ε-body` (which is not in R-intention's premise set anyway). γ_2: "Alter the structure of the organization such that Todd will have reduced responsibilities and diminished span of control." **Both γ_1 (T18) and γ_2 (T20) perceptions fail; only γ_3 (T22) validates** — the prior catalog prose mis-attributing γ_1's perception as validating was a source error caught during the §1.4.5 row-walk; corrected here.
  - θ_2: `θ(A/i./o./g2) := { [A/i./o./g2/q.] }`. Gate ∌ q (needs CEO approval). Escalate to T19 Erik.
- **T19 Erik sub-cycle** (book pages 210–212): `ι(A/i./o./g2/i.) := { [A/i./o./g2/q.] }` — pinning holds at start. **F-4 mislabels surface in T19**: Detection operator at g_2 with body using g_1 paths; Objective ω at g_2 with Σ-argument at g_1 (see §14.5.3). Sub-cycle runs; **Φ-body `{ [A/i./o./g2/q.] }`** (sole-dot, matches parent-pending-q `[A/i./o./g2/q.]` literally — **pinning holds at delivery**).
- **T20 Rusty resumes** (book pages 212–213): R-resume guard passes literally. R-execute(γ_2): `ε(A/i./o./g2/e.)`. **R-perceive of γ_2 returns `[A/i./D./P1/u.] ≤ [A/i./D./X./u.]`** — adverse utility ≥ preferred utility. **R-perceive-failure fires** (the realized comparison does not validate γ_2's projected `>`).
  - **γ_3 declared after R-perceive-failure(γ_2)** — §11.4.5 line 1850's "after R-perceive-failure" firing position. γ_3: "Add to the incentive for Todd to leave voluntarily."
  - θ_3: `θ(A/i./o./g3) := { [A/i./o./g3/q.] }`. Gate ∌ q (Rusty doesn't have a job offer for Todd). Escalate to T21 Gerry.
- **T21 Gerry sub-cycle** (book pages 214–216): `ι(A/i./o./g3/i.) := { [A/i./o./g3/q.] }` — pinning holds at start. Sub-cycle runs; Φ-body `{ [A/i./o./g3/q.] }` matches parent-pending-q `[A/i./o./g3/q.]` literally. **Pinning holds at delivery.**
- **T22 Rusty resumes** (book pages 216–217): R-resume guard passes literally. R-execute(γ_3): `ε(A/i./o./g3/e.) → { [A/i./t./D./P1/b.] + [A/i./o./g3/q.] }`. R-perceive(γ_3) validates (Todd sees net utility of leaving > staying). R-select, R-outcome (Todd elects to take the new job), R-obtained-utility, R-close, R-flowback. **Cycle closes successfully.**

**Engagement WF parameters** (per §13.5.2):
- L = 1 (one top-level cycle, Rusty-Todd)
- Parent K_C = 3 declared interleaved across T16/T18/T20; K_exec = 3 (each intention executes); J_C = 0 (no R-objective-revise firings)
- Each sub-cycle (Erik T17, Erik T19, Gerry T21): K_C = 1, J_C = 0, depth = 0
- Max S-stack depth D = 1

Per-cycle bound (inline in §13.5.2's `rem_budget`, Axis-6-corrected formula 2026-06-24): `5·(1 + 0) + (4 + 4·Q_max)·3 + 0 + 5 = (4 + 8)·3 + 10 = 46` for parent at Q_max=2 (γ_1 binds q_1 + q_2; γ_2 and γ_3 each bind one q; max |q_of| = 2). Prior formula `6·K_C` undercounted at 28 (Rusty's three escalated intentions plus γ_1's multi-θ standing-option re-firing). Sub-cycles each Q_max=1 → bound 18. Engagement total ≤ 46 + 3·18 = 100 firings (loose); realized ≈ 82 firings (4 prologue + 9 γ_1 + 8 γ_2 + 8 γ_3 + 5 close + 3·~16 sub-cycle); ≤ 100 ✓. Finite under WF-1..WF-6.

#### §14.5.2 Per-theorem trace

**§13.1 path-uniqueness**: Rusty's parent agenda has γ rows at distinct g_k ordinals (`γ(A/i./o./g1)`, `γ(A/i./o./g2)`, `γ(A/i./o./g3)`) — **no Sarah-style sole-dot reuse**. Per-actor scope holds. iN discipline (D-28) normalizes top-level `A/i.` to `A/i1`. Sibling completeness for g_1/g_2/g_3 holds. R-intention's fresh-`g_k` premise (§11.4.5) is satisfied per declaration. **§13.1(W) verified at the γ-row layer**. T19's operator-vs-body path mismatches (δ operator at g_2 with body using g_1 paths; ω with Σ-argument at g_1 inside g_2 sub-cycle) are flagged in §14.5.3 as F-4 instances of operator-template-edit-artifact shape — not §13.1(W) violations of Sarah-instance-1 shape (which was constituent-uniqueness-at-path) but cross-cycle path-reference inconsistency. Manual representation correction required; no lexer rule applies. **§13.1 validated at the γ-row layer; T19 mislabels carried as separate F-4 instances.**

**§13.2 type preservation**: Sequence fires R-open, R-interest, R-detect, R-objective, R-intention(γ_1), **R-required-resources ×2 at the same g_1** (Axis 6 Layer A), **R-gate ×2 at the same g_1** (Axis 6 Layer B), R-spawn for q_2, T17's full lifecycle, R-close-nested, R-resume (with Gap-§13.4.3-resume-guard-designation-variance open at this step), R-execute(γ_1), R-perceive(γ_1) success, R-intention(γ_2), R-required-resources(γ_2), R-gate(γ_2), R-spawn for γ_2's q, T19's full lifecycle, R-close-nested, R-resume (literal-membership passes for γ_2), R-execute(γ_2), R-perceive-failure(γ_2), R-intention(γ_3), R-required-resources(γ_3), R-gate(γ_3), R-spawn for γ_3's q, T21's full lifecycle, R-close-nested, R-resume (literal-membership passes for γ_3), R-execute(γ_3), R-perceive(γ_3) success, R-select, R-outcome, R-obtained-utility, R-close, R-flowback. Each rule's contractum is well-typed at Layer 2 per §13.2.2. **Three caveats**: (1) Axis 6 Layer A — R-required-resources writing two θ for one γ is under-spec'd; LSPI's representation either folds into one θ with multi-element body or extends §11.4.6 to admit re-firing. (2) Axis 6 Layer B — R-gate testing multi-q θ is under-spec'd (conjunction vs per-θ semantics); the source's spawn-targeting (escalate for q_2 specifically) relies on per-θ semantics no rule licenses. (3) T19 mislabels require representation correction before per-rule type-check. **§13.2 validated contingent on Axis 6's three under-specifications being pinned and T19's mislabels being treated as representation corrections.**

**§13.3 congruence decidability**: Rusty's Σ-clauses (T16/T18/T19/T20/T21/T22 targets-resolution-yields-position projections) parse and type to standard Layer-3 forms. Γ-bodies show the same path-divergence pattern as Sarah (projected drops `/D.`, realized drops `/t.`); **D-26 (§8.2.2 line 534) and D-27 (§8.2.2 line 549) handle automatically**. No non-trivial congruence-decision step exercised. **§13.3 validated abstractly post-D-26/D-27 normalization**.

**§13.4 resource conservation (with Gap-§13.4.3-resume-guard-designation-variance caveat)**: Per-cycle conservation holds within each sub-cycle's R-multiset arithmetic (R-execute deducts cost via `⊖`; R-close-nested adds Φ via `⊎`; no leak, no duplication per fresh-`g_k` discipline). **Cross-cycle conservation across the three depth-1 escalations** — the §13.4.3 pinning question — splits:
- **T17 Erik → Rusty for g_1's q_2**: **pinning FAILS literally** under R-resume's membership test. Parent-pending-q = `[A/i./o./g1/q2]` (q_2 ordinal); Erik's Φ-body delivers `[A/i./o./g1/q.]` (sole-dot). R-resume's premise `R ∋ parent-pending-q` returns false under literal multiset membership; no normalizer between sole-dot and ordinal q designations exists in §8.2.2. **Gap-§13.4.3-resume-guard-designation-variance open** with three readings (see §14.5.3 instance + §13.5.9 entry).
- **T19 Erik → Rusty for g_2's q**: **pinning holds literally**. Parent-pending-q = `[A/i./o./g2/q.]`; Erik's Φ-body delivers `[A/i./o./g2/q.]`. Literal match.
- **T21 Gerry → Rusty for g_3's q**: **pinning holds literally**. Parent-pending-q = `[A/i./o./g3/q.]`; Gerry's Φ-body delivers `[A/i./o./g3/q.]`. Literal match.

Conservation arithmetic (multiset `⊎` and `⊖`) operates on whatever designations R holds regardless of pinning's literal-vs-semantic resolution; no leak, no duplication. The open question Gap-§13.4.3-resume-guard-designation-variance raises is whether the parent's resume advancement is well-defined when literal-membership fails. **§13.4 validated for the two pinning-holds cases (T19, T21); T17 contingent on Gap-§13.4.3-resume-guard-designation-variance classification.**

**§13.5 termination + progress (with R-perceive-failure → R-intention validated as distinct from F-3)**: WF-1 (K_C bounded — parent K=3, sub-cycles K=1), WF-2 (J_C = 0), WF-3 (D = 1), WF-4 (L = 1). Per-cycle bound finite; engagement total finite. **Progress at every state**: gate-fails route to R-spawn deterministically (R ∌ q); sub-cycles' gates pass (R ∋ q); resumes either pass (T19, T21) or surface Gap-§13.4.3-resume-guard-designation-variance (T17). **R-perceive-failure → R-intention(γ_3) is exercised** at T20: perception of γ_2's execute returns `≤` (adverse-utility ≥ preferred-utility), failing γ_2's projected `>`; R-perceive-failure fires; γ_3 declared via §11.4.5's "after R-perceive-failure" position; lifecycle advances into γ_3's full chain (success at T22). **This validates §11.4.5's dynamic-intention-addition mechanism.**

**F-3 status (parent-retry-after-sub-cycle-failure) — UNVALIDATED, distinct from R-perceive-failure**: F-3 asks whether the system admits parent retry when a **sub-cycle fails to deliver** parent-pending-q. **All three Rusty sub-cycles succeed at delivery** (Erik T17 delivers `q.` instead of `q_2` but the sub-cycle runs to flowback; Erik T19 delivers `q.` matching parent-pending-q `q.`; Gerry T21 delivers `q.` matching parent-pending-q `q.`). Rusty's R-perceive-failure for γ_2 in T20 is at the parent's own perception step (parent's execute didn't yield the projected utility), **not at a sub-cycle's failure**. These are distinct mechanisms. **Conflating them would manufacture a false F-3 validation.** F-3 stays abstract; no worked case in the dissertation exercises it.

**§13.5 validated**: multi-intention K=3 interleaved with one R-perceive-failure-driven dynamic intention addition exercised; termination + progress hold modulo Gap-§13.4.3-resume-guard-designation-variance's resolution.

**§13.6 determinism**: σ for Rusty has the canonical §11.4.5 line 1850 dispatch — R-intention fires at positions "after R-objective", "after another γ-body", "after R-execute", or "after R-perceive-failure"; R-required-resources fires at `last = γ-body`; R-gate fires at `last = θ-body`. Under §11.4.5's interleaved spec, Rusty's σ is effectively trivial: lifecycle advances deterministically at each `last`-position. The (R-required-resources vs R-intention) fork at `last = γ_1-body` (Axis 1 of Gap-§11.4, surfaced for Sarah's batched case) does not arise for Rusty because γ_2 is not declared until after R-perceive(γ_1) — only one rule is applicable at each step. The fork once framed at `last = ε-body` (the prior "Axis 2 = R-perceive vs R-intention") is a phantom per §1.4.5's state-fork derivation — no case witnesses R-intention firing from `last = ε-body`. **Axis 2's content re-locates to `last = ⟨perceive-failure, C⟩`** (the actual lifecycle state where Rusty's dynamic intention-addition discretion lives, per §11.4.5 line 1841's premise and the §14.5.1 perception correction); at that state the discretion is licensed and witnessed by Rusty. **§13.6 validated for Rusty modulo Gap-§13.4.3-resume-guard-designation-variance's classification (which affects whether T17's resume completes the sequence)**. Under §11.4.5's interleaved spec, σ is effectively trivial.

#### §14.5.3 Source-level inconsistencies surfaced (F-4 instances) — per-row + per-leaf-path scan

**Methodology note** (inherited from §14.4.3): every γ / θ / ι / ε / Γ / Σ / Φ row across T16–T22 walked individually, **plus per-leaf-path enumeration within ordinal-bearing rows** (especially ε and θ). Divergences listed as the scan reaches them; count set by scan completion; classifications cite mechanisms. Three failure modes named in §14.4.3 (universal-negative, pre-committed-count, asserted-mechanism) ruled out as the scan proceeds. The six candidates I named pre-draft are the pre-scan inventory; the scan adds to or confirms them.

**Per-row walk record (T16 → T22, γ then θ then ι then ε then Γ then Σ then Φ across all tables):**

**Rusty F-4 instance 1: T16 two-θ-per-γ stacked under-specification (Gap-§11.4 Axis 6, three beats).** T16 declares γ_1 once at `[a.]γ(A/i./o./g1)` (book page 204), then **two distinct θ contractums** at the same intention argument:
- `[a.]θ(A/i./o./g1) := { [A/i./o./g1/q1] }` (book page 204, "Required resources 1 for Intention 1")
- `[a.]θ(A/i./o./g1) := { [A/i./o./g1/q2] }` (book page 205, "Required resources 2 for Intention 1")

The dissertation explicitly labels both as "for Intention 1" — these are two required resources for one intention, not two intentions wearing one path (verified against §13.1(W) walk: not a Sarah-instance-1 shape). **Three stacked under-specifications**:

1. **Layer A — §11.4.6 R-required-resources** (declaration): premise `last = γ-body`. After θ_a fires, `last = θ_a-body`; §11.4.6 has no re-firing premise from `last = θ-body`. To get two θ at the same g_k, §11.4.6 needs to either (i) admit multi-element θ-body in one contractum (`θ(...) := { q_1, q_2 }`) or (ii) extend the premise set to admit re-firing from `last = θ-body` or `last = ⟨gate-pass, q⟩`.

2. **Layer B — §11.4.7 R-gate** (testing): premise `last(M-cycle-C) = ([a.]θ(...) := { [.../q.] })` — singular q. Multi-q θ-body's gate behavior is under-spec'd: **conjunction reading** (`R ∋ q_1 ∧ R ∋ q_2` — single gate, fails if any q missing) vs **per-element reading** (test each q independently, multiple gate-passes/fails). §11.4.7 doesn't license either over the other.

3. **Layer C — Spawn-target identification** (the load-bearing under-specification): if the source's representation uses singular-q θ bodies but two θ contractums (per Layer A's extension option (ii)), R-gate fires twice — once per θ — and R-spawn targets the failing q (q_2) cleanly because there's a per-θ gate-fail event. **But if** the representation folds into multi-element θ-body (Layer A option (i)) **and** R-gate uses conjunction semantics (Layer B), the gate fails as a whole and **no rule identifies which q broke the conjunction** — R-spawn has nothing to target. The source escalates for q_2 specifically, which works only under the per-θ-with-targeting reading. **No rule licenses per-θ over conjunction; the source's spawn-targeting relies on an unlicensed inference.** This is the third beat — the one that makes Axis 6 more than a notational nit.

**Classification: Gap-§11.4 Axis 6 — three stacked under-specifications.** Filed under Gap-§11.4-multi-intention-sequencing in §13.5.9 as a new axis alongside Sarah's Axes 3–5.

**Rusty F-4 instance 2: T17 Erik Φ-body sole-dot-vs-ordinal pinning failure (Gap-§13.4.3-resume-guard-designation-variance).** T17 Erik sub-cycle (book pages 205–208) is spawned for parent-pending-q `[A/i./o./g1/q2]` (q_2 ordinal, per T16's failing gate at book page 205). Erik's ι body is `{ [A/i./o./g1/q2] }` (pinning holds at start). Erik's lifecycle runs through detection / objective / intention / required-resources / gate-pass / execute / perceive / outcome to obtained-resource. **Erik's Φ-body delivers `[a.]Θ(A/i./o./g1/i./O./Q.) := { [A/i./o./g1/q.] }`** (sole-dot, book pages 207–208).

**Pinning fails at delivery**: R-resume's premise `R ∋ parent-pending-q` tests `R ∋ [A/i./o./g1/q2]` against R containing `[A/i./o./g1/q.]` (delivered by Erik's Φ). **Literal multiset membership returns false** — `[A/i./o./g1/q.]` and `[A/i./o./g1/q2]` are syntactically distinct designations; no §8.2.2 lexer rule normalizes between sole-dot and ordinal q.

**Three readings, open-three with resolution (2) labeled as semantic-not-syntactic** (parallel to Gap-§11.7.2's resolution disposition):

1. **Source transcription error** — should have been `q_2` in Erik's Φ-body, rendered sole-dot by mistake. Pinning holds under corrected reading.
2. **Sole-dot `q.` is the source's shorthand for "the q this sub-cycle was tasked with"** — semantic match to parent-pending-q via the dissertation's narrative ("the authorization needed to change the department's requisition policy"), but syntactically distinct. **Pinning holds under semantic reading; FAILS under literal multiset membership** — same split Sarah forced on the revision axis, not an exit from it. The narrative-purpose gloss is not a clean fourth option; it is resolution (2) wearing a confident hat.
3. **Genuine divergence** — the system's literal-membership test is more disciplined than the source; representing Rusty requires manual representation correction (analyst rewrites Erik's Φ-body as `q_2`).

**Classification: Gap-§13.4.3-resume-guard-designation-variance, OPEN.** Filed as new §13.5.9 entry with shared-pattern note (semantic-vs-syntactic gap in Φ rendering, same abstract pattern as Gap-§11.7.2) and explicit mechanical-divergence note (Sarah's resume guard passes; Rusty's fails — different rule, different step, different fix). Common §11.4.2-resolution-lineage sentence: both gaps live downstream of Gap-§11.4.2's deliberate routing of the resume guard around the sub-cycle's ι (to keep §13.1 out of the pinning proof); Sarah's mismatch lives in the gap that routing opened (ι and Φ can diverge without the guard noticing), Rusty's mismatch lives in what that routing didn't fix (the guard still demands literal q-designation equality).

**Rusty F-4 instance 3: T19 Erik detection-row operator-vs-body path mismatch.** T19 Detection (book page 210): operator `[a.]δ(A/i./o./g2/i./d.)` (at g_2) with body `{ [A/i./o./g1/i./t.], [A/i./o./g1/i./t./D./P.], [A/i./o./g1/i./t./D./X.] }` (at g_1). The operator's argument carries the sub-cycle's parent-prefix `g_2` correctly, but the body's three constituent-designation paths reference g_1 within the same sub-cycle. **Classification on T19's own evidence**: source-internal mislabel — content originally for the g_1 sub-cycle (T17) was retargeted to g_2 (T19) but inner path designators missed update. **No lexer rule fixes operator-vs-body path inconsistency** (D-26/27/28 don't operate on g_k ordinals at all; they handle /i./D./, /t./G., agenda-root sole-dot). Manual representation correction or §11 spec extension required. Same shape *of inconsistency* as Nathan T8's detection-row mismatch, which §14.3.3 has now walked and classified as **N-4** (T8 δ operator at g_1 with body at g_2 — row-verified against PDF p.181, manual representation correction, no lexer rule applies). The Rusty-T19 and Nathan-T8 detection-row mismatches are the same operator-template-edit-artifact shape, both row-verified, both requiring manual representation correction.

**Rusty F-4 instance 4: T19 Erik objective-row Σ-argument path mismatch.** T19 Objective (book page 210): `[a.]ω(A/i./o./g2/i./o.) ≡ { [A/i./o./g2/i./t.]Σ(A/i./o./g1/i./t./D.)′ → [A/i./o./g2/i./t./S./P.]′ }`. The ω operator and the outer Σ-prefix and the projection target use g_2 correctly, but the **Σ-argument inside the projection-clause uses g_1**. Same template-edit-artifact shape as instance 3. Manual representation correction required.

**Rusty F-4 instance 5: T16 two-preferred-positions structure.** T16 detection body declares two preferred positions (book page 204): `[A/i./t./D./P1]` ("Todd leaves voluntarily") and `[A/i./t./D./P2]` ("Rusty is terminated Todd"). Charles, Jim, Sarah, Nathan each have a single P in detection. **Classification**: source-side declaration of an alternative-preferred-position with explicit ordinal (P1, P2). §11.4.3 R-detect's contractum admits multi-element body (`{ [Α/i./t.], [Α/i./t./D./P.], [Α/i./t./D./Xk], ... }`) but exhibits a single P. Whether §11.4.3 admits multiple `Pk` siblings under the same matrix is **under-spec'd in §11.4.3**; the rule's prose lists "preferred-position" (singular) but the worked case demonstrates two. Filing as a **sub-aspect of Gap-§11.4 Axis 6** (multi-P-per-matrix, structurally parallel to multi-q-per-θ) or as a separate §11.4.3 finding.

**Rusty F-4 instance 6: Γ-path divergences (D-26 / D-27 normalization-handled).** Walk of intention rows (T16 γ_1's Γ at book page 204, T18 γ_2's Γ at book page 209, T20 γ_3's Γ at book page 213) shows projected Γ rows in form `Γ(A/i./t./G.)′` — drop `/D.`. Walk of perception rows (T17 book page 207 `Γ(A/i./o./g1/i./D./G.)`, T18 book page 208 `Γ(A/i./D./G.)`, T19 book page 211 `Γ(A/i./o./g2/i./D./G.)`, T20 book page 213 `Γ(A/i./D./G.)`, T21 book page 215 `Γ(A/i./o./g3/i./D./G.)`, T22 book page 217 `Γ(A/i./D./G.)`) shows realized Γ rows in form `Γ(A/.../D./G.)` — drop `/t.`. **Same shape as Sarah F-4 instance 3**: §13.1(W)-inverse-shape (one constituent at two paths). **Automatic lexer normalization** via D-26 (§8.2.2 line 534, inserts `/t./` for realized) and D-27 (§8.2.2 line 549, inserts `/D./` for projected). Verified for every Γ row in T16–T22.

**Per-leaf-path enumeration within ε rows:** T17 has one ε (book page 207), T18 has one ε (book page 208), T19 has one ε (book page 211), T20 has one ε (book page 212), T21 has one ε (book page 215), T22 has one ε (book page 216). **No T14-style ε_1/ε_2 double-execution within any single Rusty sub-cycle.** Each γ has a single ε firing. **Rusty does NOT corroborate Sarah F-4 instance 4** (per-intention multi-execute); Sarah's double-execute remains a Sarah-specific finding, isolated under Gap-§11.4 Axis 5.

**Scan conclusion** (count set by the row + leaf-path walk above, no pre-committed total): **six F-4 instances surfaced**, each with cited handling mechanism:
1. T16 two-θ-per-γ structure (Axis 6, three beats — declaration, gate-semantics, spawn-target). Gap-§11.4-multi-intention-sequencing.
2. T17 Erik Φ sole-dot q. vs parent-pending-q_2. Gap-§13.4.3-resume-guard-designation-variance, open-three readings.
3. T19 detection operator-vs-body g_1/g_2 mismatch. Manual representation correction.
4. T19 objective Σ-argument g_1 in g_2 sub-cycle. Manual representation correction.
5. T16 two-preferred-positions (P1, P2). §11.4.3 multi-P under-spec, sub-aspect of Axis 6 or separate §11.4.3 finding.
6. Γ-path divergences across every projected and realized Γ row in T16–T22. Automatic lexer normalization (D-26, D-27).

**No instance was pre-committed; the count emerged at scan completion.** The pre-scan inventory listed six candidates; the scan confirmed all six on the rows, classified them per Rusty's own evidence, and **per the per-leaf-path discipline ruled out a T14-style multi-execute miss** (Sarah's instance 4 does not repeat in Rusty).

#### §14.5.4 Validation outcome

Rusty Tables 16–22 establish:

- **§13.1**: validated at the γ-row layer (g_1/g_2/g_3 distinct ordinals, no Sarah-instance-1 reuse). T19 mislabels are cross-cycle path references, separate F-4 finding, not §13.1(W) violations.
- **§13.2**: validated contingent on Axis 6's three under-specifications being pinned and T19's mislabels being treated as representation corrections.
- **§13.3**: validated abstractly post-D-26/D-27 normalization.
- **§13.4**: validated for the two pinning-holds escalations (T19, T21). **T17 contingent on Gap-§13.4.3-resume-guard-designation-variance's classification** (open-three readings).
- **§13.5**: validated; multi-intention K=3 interleaved exercised; **§11.4.5's R-perceive-failure → R-intention dynamic addition validated** (T20). **F-3 (parent-retry-after-sub-cycle-failure) remains UNVALIDATED** — R-perceive-failure is at the parent's own perception step, not a sub-cycle's delivery failure; conflating them would manufacture a false F-3 validation.
- **§13.6**: validated for Rusty modulo Gap-§13.4.3-resume-guard-designation-variance's classification. Under §11.4.5's interleaved spec, σ is effectively trivial.

Rusty does **not** establish: depth-≥2 nesting (Rusty bottoms out at depth-1 per sub-cycle; **§11.6.11 now re-cites Nathan T7–T9 as the row-verified depth-2 case, not Rusty Tables 16–19** — the re-cite was executed once §14.3 walked T7–T9 on their own rows and confirmed literal pinning at both depths; §4.2 and §11.6.11 updated accordingly), parent-retry-after-sub-cycle-failure (F-3, abstract), Sarah's Axes 3–5 (batching, moot-by-sub-cycle-outcome, per-intention multi-execute — Sarah-only outliers per Rusty's source walk; Rusty does not reproduce any).

**Rusty narrows Gap-§11.4 by isolating Sarah's three Axes (3b, 4, 5) as Sarah-only outliers** and **witnessing Axis 2 at its corrected lifecycle state**: per §1.4.5's state-fork derivation, Axis 2's intention-addition discretion lives at `last = ⟨perceive-failure, C⟩` (not at `last = ε-body` — that framing was the phantom). Rusty's γ_2 declaration at T18 (after γ_1's perceive-failure) and γ_3 declaration at T20 (after γ_2's perceive-failure) are the source-witnessed firings of R-intention from `⟨perceive-failure, C⟩` admitted by §11.4.5 line 1841 — the §14.5.1 perception correction established that both intermediate perceptions fail, which is what licenses the intention-additions. **Rusty does NOT validate Axis 1**: under interleaving, only one γ is in scope at a time, so Axis 1's sub-questions (1a γ-vs-θ at `last = γ-body`; 1b which γ_k's θ fires with multiple γ-bodies in `last`) never arise. Avoiding a fork is not validating its resolution. **Rusty introduces Axis 6** (two-θ-per-γ stacked under-spec) as a new structural finding distinct from Sarah's. **Rusty also surfaces Gap-§13.4.3-resume-guard-designation-variance** (pinning failure on resource-ordinal axis at T17) as a second pinning-failure-against-source case, mechanically distinct from Sarah's Gap-§11.7.2 (Sarah's resume guard passes; Rusty's fails). Both gaps share an abstract pattern (semantic-vs-syntactic gap in Φ rendering) but require different fixes; filed separately, with shared-pattern and mechanical-divergence notes explicit.

**Six F-4 instances for Rusty** (count set by §14.5.3 per-row + per-leaf-path scan): T16 two-θ-stacked-under-spec (Axis 6); T17 q.-vs-q_2 pinning failure (Gap-§13.4.3-resume-guard-designation-variance); T19 detection mislabel; T19 objective Σ-argument mislabel; T16 two-preferred-positions; Γ-path divergences (D-26/D-27 handled). The methodology's three failure modes (universal-negative, pre-committed-count, asserted-mechanism) all foreclosed per the row + leaf-path discipline; **per-leaf-path enumeration on ε rows confirms Sarah F-4 instance 4 does not repeat in Rusty.**

**Back-reference to §14.4** (per Block C draft-order's cross-reference plan): Rusty's source walk **rejects** the §14.4 forward note's prior framing ("Rusty settles Sarah's batching"). The corrected reading: Rusty's interleaved K=3 pattern is canonical under §11.4.5; Sarah's batched K=2 pattern is the unrepresentable outlier. Rusty narrows Gap-§11.4 by isolating Sarah's Axes 3–5 as Sarah-specific. Sarah's §14.4 finalization waits on §11's disposition of those three axes, not on Rusty. Sarah and Rusty exhibit structurally different K>1 patterns; the dissertation includes both, and the system's representation needs to either extend §11.4 to handle Sarah's batched pattern (per Gap-§11.4 Axes 3–5) or accept Sarah's pattern as a fidelity divergence parallel to Gap-§11.7.2.

### §14.3 Nathan — Tables 7–11 (depth-2 escalation chain; batched γ-declarations; terminal interest-level perceive; source-verified)

Nathan Tables 7–11 document a five-table engagement: T7 (Nathan-Randy parent, Part 1 of 2), T8 (Nathan-Wanda depth-1 sub-cycle Part 1), T9 (Nathan-Mike depth-2 sub-cycle complete), T10 (Nathan-Wanda depth-1 sub-cycle Part 2 / resume-completion), T11 (Nathan-Randy parent Part 2 of 2 / resume-completion). PDF pages 83–94 of `Lam-2018-Pepperdine-Chapter-5.pdf`; book pages 178–189.

**Nathan's structural significance**: this is the **depth-2 nesting validator** for §11.4 / §11.6's S-stack discipline at depth ≥ 2. The source exhibits Randy (top, `A/i.`) → Wanda (depth-1, prefix `A/i./o./g2/i.`) → Mike (depth-2, prefix `A/i./o./g2/i./o./g./i.`) as a single chained escalation: Randy gate-fails on g_2's q, spawns Wanda; Wanda gate-fails on her required-resource q, spawns Mike; Mike's gate passes, runs full lifecycle, returns Φ; Wanda resumes, runs her remaining lifecycle, returns Φ; Randy resumes, runs his remaining lifecycle for γ_2's execute, perceives, outcomes, closes. **Pinning holds literally at both depths** (Mike's Φ matches Wanda's parent-pending-q; Wanda's Φ matches Randy's parent-pending-q). **The depth-weighted induction's empirical base case at D ≥ 2 is earned** (§13.5.2 measure + §13.5.4 well-foundedness; formerly old §13.5.6's arbitrary-depth induction) — the induction now has a source-verified depth-2 chain to ground its base, rather than the constructed-only trace at §11.6.11.

Nathan surfaces three structural findings the source walk made unavoidable: (a) **Axis 3a (batched γ-declarations) is reproduced by Nathan**, falsifying the prior "Axis 3 is Sarah-only" framing — this drove the Axis 3a/3b split in Gap-§11.4 (see §13.5.9 entry); (b) **Axis 1 sub-question 1b reproduction-failure (two-case confirmed post-§14.3.4 PDF pass)** — Nathan's T7 row 11 fires θ for γ_1 at `last = γ_2-body`, and Sarah's T12 row 12 (book p192) fires θ_1 at the analogous state. Both sources pick **θ_1 before θ_2** when γ_1, γ_2 are batched. §11.4.6's `last`-keyed premise can only produce θ_2 from that state, so the rule cannot reproduce either source. Per Rule 2 this is a rule-structural signal: §11.4.6's `last`-pointer cannot represent multi-element pending-θ obligations under batched declarations and must be replaced by a set-based premise. **Structural defect AND firing-order discipline now two-case confirmed**: declaration-order (the more conservative framing) at K=2; oldest-first is its K=2 specialization indistinguishable from declaration-order on K=2 data, so "declaration-order" is the strongest pin the data licenses. K≥3 batched would be needed to refine further; no such case exists in the corpus. The prior catalog claim that "R-required-resources fires on most-recent γ-body" (canonical under Rusty) is falsified — both Nathan and Sarah pick θ_1 at `last = γ_2-body`, which the most-recent reading cannot produce, and Rusty's interleaved spec never tests this fork in the first place. (c) **Per-intention vs terminal perceive-cardinality observation (Axis 7 legacy, dissolved per §1.4.5)** — Nathan exhibits K executes with 1 terminal interest-level perceive; Rusty exhibits K executes / K perceives; Sarah exhibits 1 execute + 1 moot. The §1.4.5 state-fork derivation dissolves the prior "Axis 7 multi-modal axis" framing: Rusty's per-intention perceiving is `ε-body` **guard-determined Pillar 2** (not σ-discretion), and Nathan's "terminal perceive" is an artifact of the Site (ii) defect (ε_1 → θ_2 transition is unreachable under §11.4.6's current premise; perceive lands at ε_2 by accident of which transition the source happens to write). Sarah's "1 perceive + 1 moot" attaches to the Axis 4 post-resume defect. The observation stays as source-verified data; the disposition moves from "open Axis 7" to "resolved per §1.4.5 across three different lifecycle states." (d) **Axis 8 R-execute body-resolution (one Sarah-T15 reproduction-failure plus a corpus ε-notation survey, surfaced during §14.3.4 ε sweep)** — Sarah's K=2 uniform-sole-dot body leaves R-execute's `R ⊖ [body-path]` genuinely ambiguous about which q is consumed; this is the gap. The §14.3.4 ε sweep also surveyed Charles K=1 (uniform sole-dot, harmless at K=1), Jim K=2 and Nathan K=2 (operator-sole-dot / body-ordinal — R-execute resolves because the body specifies), and Rusty K=3 (uniform ordinal — disciplined form). The survey is informative about corpus ε convention but does not extend the gap beyond the Sarah-T15 sub-case.

**One transcription artifact verified during the §14.3 walk but explicitly NOT a structural finding**: Wanda T8 row 1's ι body renders the o-segment as numeral **`21`** rather than ordinal `g2` (book page 181). This was initially considered as a candidate Gap-§13.4.3 Instance 2 (g-rendering axis variance, parallel to Rusty T17's q-rendering variance) and is now **demoted to an F-4 transcription-class finding** (resolution 1, no mechanical consequence). The mechanical analysis: R-spawn's contractum (per Gap-§11.4.2's resolved branch) *sets* the sub-cycle ι := { parent-pending-q } — R-spawn writes the ι, does not test a pre-existing ι against parent-pending-q. The `21` lives in a row the system *produces* at `g2`, with every other o-segment in Wanda's sub-cycle rendering `g2` correctly (T8 detection body, intention, θ; T10 perception, Φ). Wanda's Φ at T10 row 5 delivers `[A/i./o./g2/q.]` and Randy's R-resume guard reads matching designations from both sides — the guard passes literally. Mechanically unlike Rusty T17 (which breaks at the resume-guard membership test on a real divergence in a row the system *reads*). Filing as F-4 transcription-class alongside the T8 detection-operator g_1 mislabel — same species (transcription artifact, resolution 1).

**Verification boundary note (carried as a standing caveat throughout §14.3).** This section's source-row citations come from PDF pages 83–94 read directly during this turn; rows are quoted verbatim. The downstream classifications (F-4 instances, the 3a/3b split, the perceive-cardinality finding, the Instance 2 filing) load on those quoted rows. If any quoted row turns out mis-transcribed under closer inspection, the downstream classifications move with the rows; this is a standing fidelity boundary on the section, not a hedge on the discipline. Per-theorem trace below cites specific rows by table-and-book-page so the trace is verifiable against the PDF directly.

#### §14.3.1 Case overview and structural skeleton

**Parent cycle** `ι(A/i.) := { [A/i./Q.] }` (Nathan's interest: authorization to proceed with ISO 9000 engagement; agenda "Build new culture based on continuous improvement"). **K_decl = 2 batched upfront** (γ_1 and γ_2 declared in adjacent rows BEFORE any θ fires).

**Top-level row order in T7 (book pages 178–180), as-traced:**

|  Row   |       Constituent        |                                          Source notation                                          |
|--------|--------------------------|---------------------------------------------------------------------------------------------------|
| 1      | Actor                    | `[a.]` (Nathan)                                                                                   |
| 2      | Agenda                   | `[A.]`                                                                                            |
| 3      | Interest                 | `[a.]ι(A/i.) := { [A/i./Q.] }`                                                                    |
| 4      | Detection                | `[a.]δ(A/i./d.) := { [A/i./t.], [A/i./t./D./P.], [A/i./t./D./X.] }`                               |
| 5      | Target                   | `[A/i./t.]` (Randy, CEO)                                                                          |
| 6      | Preferred position       | `[A/i./t./D./P.]`                                                                                 |
| 7      | Adverse alternative      | `[A/i./t./D./X.]`                                                                                 |
| 8      | Objective                | `[a.]ω(A/i./o.) ≡ { [A/i./t.]Σ(A/i./t./D.)′ → [A/i./t./S./P.]′ }`                                 |
| **9**  | **Intention 1**          | `[a.]γ(A/i./o./g1) ≡ { [A/i./t.]Γ(A/i./t./G.)′ = { [A/i./t./D./P./c1]′ < [A/i./t./D./P./c1] } }`  |
| **10** | **Intention 2**          | `[a.]γ(A/i./o./g2) ≡ { [A/i./t.]Γ(A/i./t./G.)′ = { [A/i./t./D./P./c2]′ > [A/i./t./D./P./c2]′ } }` |
| 11     | Required resources (γ_1) | `[a.]θ(A/i./o./g1) := { [A/i./o./g1/q.] }`                                                        |
| 12     | Resource check           | `[a./R.] ∋ [A/i./o./g1/q.]` (gate **passes**)                                                     |
| 13     | Execution 1              | `[a.]ε(A/i./o./g./e1) → { [A/i./t./D./P./c.] - [A/i./o./g1/q.] }`                                 |
| 14     | Required resources (γ_2) | `[a.]θ(A/i./o./g2) := { [A/i./o./g2/q.] }`                                                        |
| 15     | Resource check           | `[a./R.] ∌ [A/i./o./g2/q.]` (gate **fails** → spawn Wanda)                                        |

**γ-declarations are batched upfront (rows 9 and 10) before any θ — Axis 3a pattern, source-verified at book page 179.** After γ_1, γ_2 are declared, the lifecycle runs sequential per-intention θ/gate/ε firing (rows 11–13 for γ_1, then rows 14–15 for γ_2). γ_2's gate fails → spawn Wanda.

**Sub-cycle 1 depth-1** (Nathan → Wanda, T8 + T10):

- **T8 row 1 Interest**: `[a.]ι(A/i./o./21/i.) := { [A/i./o./21/q.] }` (book page 181). Uses **numeral `21`** at the o-segment where R-spawn's contractum writes `g2` (per Gap-§11.4.2's resolved branch — R-spawn *sets* the sub-cycle ι := { parent-pending-q }; the rule writes the row, the source's `21` rendering is a transcription artifact in a value the system produces as `g2`). **F-4 transcription-class instance**; mechanically harmless because R-spawn does not test a pre-existing ι against parent-pending-q — there is no equality test at the spawn step to fail. Every other o-segment in Wanda's sub-cycle renders `g2` correctly, and Randy's R-resume guard at T11 reads matching `g2` designations from both sides (passes literally). See §14.3 lead for the full demotion analysis.
- **T8 row 2 Detection**: `[a.]δ(A/i./o./g1/i./d.) := { [A/i./o./g2/i./t.], [A/i./o./g2/i./t./D./P.], [A/i./o./g2/i./t./D./X.] }` — operator argument at **g_1**, body at **g_2** (F-4 instance N-2).
- T8 rows 3–6: Target / Preferred / Adverse / Objective all at `A/i./o./g2/i./...` (consistent).
- **T8 row 7 Intention**: `[a.]γ(A/i./o./g2/i./o./g.) ≡ { [A/i./o./g2/i./t.]Γ(A/i./o./g2/i./t./G.)′ = { [A/i./o./g1/i./t./D./P./u.]′ > [A/i./o./g1/i./t./D./X./u.]′ } }` — γ at **g_2** with inner Γ body using **g_1** paths (F-4 instance N-3).
- T8 row 8 Required resources: `[a.]θ(A/i./o./g2/i./o./g.) := { [A/i./o./g2/i./o./g./q.] }`.
- T8 row 9 Resource check: `[a./R.] ∌ [A/i./o./g2/i./o./g./q.]` (gate **fails** → spawn Mike).
- T10 row 1 Execution: `[a.]ε(A/i./o./g2/i./o./g./e.) → { [A/i./o./g2/i./t./D./P./b.] + [A/i./o./g2/i./o./g./q.] }` (consumes Mike's delivered q).
- T10 rows 2–5: Perception, Outcome, Obtained utility, Obtained resource — all at `A/i./o./g2/i./...` consistent.
- **T10 row 5 Obtained resource (Φ-body)**: `[a.]Θ(A/i./o./g2/i./O./Q.) := { [A/i./o./g2/q.] }` (book page 188). **Matches Randy's parent-pending-q `[A/i./o./g2/q.]` LITERALLY** — pinning holds at depth-1 delivery.

**Sub-cycle 2 depth-2** (Nathan → Mike, T9, single complete lifecycle, no further spawn):

- **T9 row 1 Interest**: `[a.]ι(A/i./o./g2/i./o./g./i.) := { [A/i./o./g2/i./o./g./q.] }` (book page 183). **Matches Wanda's parent-pending-q `[A/i./o./g2/i./o./g./q.]` LITERALLY** — pinning holds at depth-2 start.
- T9 row 2 Detection: `[a.]δ(A/i./o./g2/i./o./g./i. /d.) := { ... }` (stray space `i. /d.`, otherwise clean).
- T9 rows 3–7: Target / Preferred / Adverse / Objective / Intention all at `A/i./o./g2/i./o./g./i./...` (consistent throughout, no cross-segment mislabel).
- T9 row 8 Required resources: `[a.]θ(A/i./o./g2/i./o./g./i./o./g.) := { [A/i./o./g2/i./o./g./i./o./g./q.] }`.
- T9 row 9 Resource check: `[a./R.] ∋ [A/i./o./g2/i./o./g./i./o./g./q.]` (gate **passes** — **Mike bottoms out at depth-2**, no further escalation).
- T9 rows 10–13: Execution, Perception, Outcome, Obtained utility (Mike's perspective).
- **T9 row 14 Obtained resource (Φ-body)**: `[a.]Θ(A/i./o./g2/i./o./g./i./O./Q.) := { [A/i./o./g2/i./o./g./q.] }`. **Matches Wanda's parent-pending-q `[A/i./o./g2/i./o./g./q.]` LITERALLY** — pinning holds at depth-2 delivery.

**Parent resume completion in T11 (book pages 188–189):**

- T11 row 1 Execution of Intention 2: `[a.]ε(A/i./o./g./e.) → { [A/i./t./D./P./c.] - [A/i./o./g2/q.] }` — ε path uses sole-dot `g.` (F-4 instance N-5) but consumes parent-pending-q at ordinal `g2`.
- T11 row 2 Perception: `[A/i./t.]Γ(A/i./D./G.) = { [A/i./D./P./u.] > [A/i./D./X./u.] }` — **single terminal interest-level perceive** (not per-intention).
- T11 row 3 Outcome: `Ω(A/i./O.) ≡ { [A/i./t.]Σ(A/i./t./D.) → [A/i./t./S./P.] }`.
- T11 row 4 Obtained utility: `[A/i./t.]Θ(A/i./O./U.) := { [A/i./t./D./P./u.] }`.
- T11 row 5 Obtained resource: `[a.]Θ(A/i./O./Q.) := { [A/i./Q.] }` — matches Nathan's original ι `[A/i./Q.]`. Top-level cycle closes successfully.

**Engagement WF parameters** (per §13.5.2):
- L = 1 (one top-level cycle, Nathan-Randy)
- Parent K_C = 2 batched-declared in T7; K_exec = 2 (γ_1 executes in T7 row 13, γ_2 executes in T11 row 1); J_C = 0 (no R-objective-revise firings)
- Sub-cycle 1 (Wanda T8/T10): K_C = 1, J_C = 0, depth = 1
- Sub-cycle 2 (Mike T9): K_C = 1, J_C = 0, depth = 2
- Max S-stack depth D = 2

Per-cycle bound (inline in §13.5.2's `rem_budget`, Axis-6-corrected formula 2026-06-24): `5·(1 + 0) + (4 + 4·Q_max)·2 + 0 + 5 = 26` for parent at Q_max=1; **prior formula `6·K_C` undercounted at 22 (Nathan's γ_2 escalates to Wanda then to Mike; realized parent firings ≈ 23 violated the prior 22 bound, which the Axis-6 correction now dominates: 23 ≤ 26 ✓)**. Wanda and Mike each `5·(1+0) + 8·1 + 0 + 5 = 18` (16 → 18 for the Q_max=1 sub-cycle bound). Engagement total finite under WF-1..WF-6.

#### §14.3.2 Per-theorem trace

**§13.1 path-uniqueness**: Nathan's parent has γ rows at distinct g_k ordinals (`γ(A/i./o./g1)`, `γ(A/i./o./g2)`) — no Sarah-style sole-dot reuse at the parent's γ level. Per-actor scope holds. iN discipline (D-28) normalizes top-level `A/i.` to `A/i1`. R-intention's fresh-`g_k` premise (§11.4.5) is satisfied per declaration. **§13.1(W) verified at the parent's γ-row layer.**

T8's operator-vs-body path mismatches (δ at g_1 with body at g_2, T8 row 2; γ at g_2 with inner Γ body at g_1, T8 row 7) and T7/T11's sole-dot-vs-ordinal mismatches at ε-paths are **representation inconsistencies between operator argument and body**, not §13.1(W) violations of Sarah-instance-1 shape. These are F-4 instances of the same operator-template-edit-artifact shape as Rusty T19's mismatches, requiring manual representation correction (no lexer rule applies). **§13.1 validated at the parent's γ-row layer; T8 / T7 / T11 mislabels carried as separate F-4 instances, classified in the §14.3.3 scan (N-2/N-4/N-5/N-7).**

**§13.2 type preservation**: Sequence fires R-open, R-interest, R-detect, R-objective, R-intention(γ_1), R-intention(γ_2) [Axis 3a batched declaration — both γ's before any θ], R-required-resources(θ_1), R-gate(γ_1) passes, R-execute(γ_1) [T7 row 13], R-required-resources(θ_2), R-gate(γ_2) fails, R-spawn for γ_2's q [push Randy onto S], T8 Wanda lifecycle through to her gate-fail, R-spawn for Wanda's q [push Wanda onto S; depth-2 reached], T9 Mike full lifecycle to R-close-nested + R-flowback to Wanda's R, R-resume to Wanda's gate-pass [depth-2 pinning holds literally], T10 Wanda lifecycle through R-execute / R-perceive / R-outcome / R-close-nested + R-flowback to Randy's R, R-resume to Randy's gate-pass [depth-1 pinning holds literally for parent-pending-q `[A/i./o./g2/q.]`], R-execute(γ_2) [T11 row 1], R-perceive [T11 row 2 — terminal interest-level], R-select, R-outcome, R-obtained-utility, R-close, R-flowback. Each rule's contractum is well-typed at Layer 2 per §13.2.2.

**Three caveats**:
1. **Axis 3a precedence**: at `last = γ_1-body` (after T7 row 9), both R-intention(γ_2) and R-required-resources(θ_1) match — §11.4 doesn't pin the precedence. Nathan's source picks R-intention first (row 10 fires before row 11). The trace assumes this precedence; if §11.4 pins the opposite (R-required-resources first), Nathan's representation needs reframing.
2. **Wanda T8 ι rendering (transcription artifact, NOT a structural gap)**: T8 row 1 ι reads `[A/i./o./21/q.]` in the source, but R-spawn's contractum *writes* this row at `g2` per Gap-§11.4.2's resolved branch (`ι(sub-cycle) := { parent-pending-q }`). The `21` rendering is a transcription artifact in a value the system produces as `g2`; there is no equality test at the spawn step to fail. Every other o-segment in Wanda's sub-cycle renders `g2` correctly; Randy's R-resume guard reads matching `g2` designations and passes literally. No type-preservation consequence — R-spawn's contractum is well-typed at the designation it writes. F-4 transcription-class only, no caveat on §13.2.
3. **T8 operator-vs-body mislabels** (rows 2, 7): require representation correction before per-rule type-check.

**§13.2 validated contingent on Axis 3a precedence being pinned, T8 mislabels being treated as representation corrections, and Axis 8's R-execute operator-to-g_k resolution being specified (notational variance reading suffices for Nathan's T7/T11 ε rows since body specifies `g_k`; reproduction-failure resolution needed only for Sarah's uniform-sole-dot sub-case, not Nathan). Axis 1b Sites (i) and (ii) are NO LONGER §13.2 contingencies as of 2026-06-23 — §11.4.6's pending-θ-set premise revision admits Nathan's θ_1 (T7 row 11) and θ_2 (T7 row 14) firings directly; the rule's contractums are well-typed at Layer 2 per §13.2.2 in the new form just as in the prior. The T8 `21` rendering is a transcription artifact in an R-spawn-produced row and carries no §13.2 contingency.**

**§13.3 congruence decidability**: Nathan's Σ-clauses (T7 objective, T8 objective, T9 objective, T11 outcome) parse and type to standard Layer-3 forms. Γ-bodies exhibit the standard projected/realized path divergence pattern: projected `Γ(.../G.)′` drops `/D./` (T7 γ_1 row 9, T7 γ_2 row 10, T8 γ row 7, T9 γ row 7); realized `Γ(.../D./G.)` drops `/t./` (T9 perceive row 11, T10 perceive row 2, T11 perceive row 2). **D-26 (§8.2.2 line 534) and D-27 (§8.2.2 line 549) handle both automatically.** No non-trivial congruence-decision step exercised. **§13.3 validated abstractly post-D-26/D-27 normalization.**

**§13.4 resource conservation (depth-2; all pinning-relevant points literal-hold)**: Per-cycle conservation holds within each cycle's R-multiset arithmetic. **Cross-cycle conservation across the depth-2 chain** — the §13.4.3 pinning question at two depths, all three pinning-relevant points hold literally under R-spawn's contractum-writes-ι discipline:

- **Spawn-start (Randy → Wanda)**: R-spawn's contractum (per Gap-§11.4.2's resolved branch) *sets* Wanda's ι := { parent-pending-q } = `{ [A/i./o./g2/q.] }`. R-spawn does not test a pre-existing ι; it writes the row. The source rendering of Wanda's ι at T8 row 1 as `{ [A/i./o./21/q.] }` is a transcription artifact in a row the system produces at `g2` (see §14.3 lead for full demotion analysis). **All four pinning-relevant points are consistent under R-spawn's contractum.**
- **Spawn-start (Wanda → Mike)**: R-spawn sets Mike's ι := { Wanda's parent-pending-q } = `{ [A/i./o./g2/i./o./g./q.] }`. Mike's T9 row 1 ι reads `{ [A/i./o./g2/i./o./g./q.] }` literally — **matches by construction**.
- **Depth-2 delivery (Mike → Wanda)**: Mike's Φ-body `{ [A/i./o./g2/i./o./g./q.] }` (T9 row 14) = Wanda's parent-pending-q `[A/i./o./g2/i./o./g./q.]` (captured in S-entry at Wanda's R-spawn for Mike). **Literal multiset membership PASSES.** Wanda's R-resume premise `R ∋ parent-pending-q` returns true. R-execute(Wanda's γ) consumes Mike's delivered q via `⊖`. Conservation holds at depth-2.
- **Depth-1 delivery (Wanda → Randy)**: Wanda's Φ-body `{ [A/i./o./g2/q.] }` (T10 row 5) = Randy's parent-pending-q `[A/i./o./g2/q.]` (captured in S-entry at Randy's R-spawn for Wanda). **Literal multiset membership PASSES.** Randy's R-resume premise returns true. R-execute(γ_2) at T11 row 1 consumes Wanda's delivered q. Conservation holds at depth-1.

Conservation arithmetic (multiset `⊎` and `⊖`) operates on whatever designations R holds; no leak, no duplication. **§13.4 validated for Nathan with NO contingency** — all four pinning-relevant points hold literally under R-spawn's contractum-writes-ι discipline; the T8 row 1 `21` rendering has no mechanical consequence because R-spawn writes the row.

**Depth-2 base case for the depth-weighted induction (§13.5.2 measure + §13.5.4 well-foundedness; formerly old §13.5.6) is EARNED**: Nathan supplies the source-verified depth-2 chain with literal-pinning-holds at both delivery points (Mike's depth-2 delivery and Wanda's depth-1 delivery), satisfying the §13.4.3 pinning at both depths with no contingency on the resume-guard-designation-variance gap. The arbitrary-depth induction now has empirical grounding at the base; previously it carried the discipline on theoretical grounds only.

**§13.5 termination + progress (the perceive-cardinality observation is now Site-(ii)-attributed per §1.4.5)**: WF-1 (K_C bounded — parent K=2, sub-cycles K=1 each), WF-2 (J_C = 0 throughout), WF-3 (D = 2 bounded), WF-4 (L = 1). Per-cycle bound finite; engagement total finite. **Progress at every state**: gate-fails route to R-spawn deterministically; gate-passes route to R-execute deterministically; the depth-2 nesting unwinds via R-close-nested + R-resume pairs without stuck states.

**Perceive-cardinality observation (Axis 7 legacy — re-attributed per §1.4.5; post-2026-06-23 §11.4.6 revision)**: Nathan exhibits K executes (2) with **1 terminal interest-level perceive** at T11 row 2. R-perceive's premise `last = ε-body` is satisfied after T11 row 1's R-execute(γ_2); R-perceive fires once at T11 row 2 with Γ-argument `A/i./D./G.` (interest-level realized form, not per-intention). γ_1's R-execute in T7 row 13 has **no paired R-perceive** anywhere in T7 — the lifecycle moves directly to T7 row 14's R-required-resources(γ_2). **§11.4.6's revised pending-θ-set premise admits this transition**: at `last = ε_1-body` with PendingTheta = {γ_2}, R-rr is admissible and writes θ_2. Nathan's "no per-intention perceive at ε_1" is a **licensed σ-choice** at this state (operator chose to defer perceiving and resource γ_2 instead) — σ disambiguates among R-perceive, R-perceive-failure, and R-rr at the now-σ-discretion state per §1.4.5 row 122 (updated). The prior framing of this transition as the "Site (ii) defect" was correct under the pre-2026-06-23 `last`-keyed premise; the §11.4.6 revision converted it from defect to licensed σ-discretion.

**§13.5 validated** with no Axis 7 contingency under the §1.4.5 derivation: depth-2 termination + progress hold; the perceive-cardinality observation is structural variance attributable to specific lifecycle states (guard-determined at ε-body no-γ-pending for Rusty; licensed σ-discretion at ε_1-body γ-pending for Nathan's terminal pattern, post-2026-06-23; Axis 4 R-moot defect for Sarah), not to an open spec axis.

**§13.6 determinism**: σ for Nathan has the following non-trivial choices given the batched declarations:
- **At `last = γ_1-body`** (after T7 row 9): R-intention(γ_2) vs R-required-resources(θ_1) both match. Source picks R-intention first. **Axis 1's `last = γ-body` fork**; Nathan exemplifies the "R-intention first" pick.
- **At `last = γ_2-body`** (after T7 row 10): under §11.4.6's premise `last = γ-body` (line 1857), the rule matches and its contractum writes θ for the γ named in `last` — i.e., **θ_2**, since `last = γ_2-body`. Source picks **θ_1** (T7 row 11 fires `θ(A/i./o./g1)`, book page 179). **§11.4.6 as currently written cannot reproduce Nathan's θ_1 from this state** — there is no σ-choice or premise-disambiguation that produces θ_1 before θ_2; the rule deterministically writes θ_2. Per Rule 2 (worked cases are ground truth; if a rule fails to reproduce a worked-case step, the rule is wrong), this is a **rule-structural fix needed**, not a σ-gap: §11.4.6's `last`-pointer cannot represent multi-element pending-θ obligations under batched declarations and must be replaced by a set-based premise. **Established (post-§14.3.4 PDF pass with Sarah 1b confirmation): structural defect AND firing-order discipline.** Both Nathan (T7 row 11) and Sarah (T12 row 12, book p192) fire θ_1 before θ_2 at the analogous state — **two-case confirmation of declaration-order θ-firing at K=2**. Pin: declaration-order (the conservative framing; oldest-first is its K=2 specialization indistinguishable on K=2 data; K≥3 batched would refine further but no such case exists in the corpus). See Axis 1 sub-question 1b in §13.5.9's Gap-§11.4 entry, including the carryover-note's discipline warning about not over-specifying from K=2 data to "oldest-first" without K≥3 evidence.
- **At `last = ε_1-body`** (after T7 row 13): per §1.4.5's state-fork table (updated 2026-06-23 after §11.4.6's pending-θ-set revision), this state now hosts **licensed σ-discretion** among R-perceive, R-perceive-failure (per validation premise), and R-required-resources (per §11.4.6's pending-θ-set premise — PendingTheta = {γ_2} at this state, R-rr admissible). Source writes θ_2 at row 14 — R-rr fires with `earliest-declared γ ∈ PendingTheta` = γ_2 (the only element), writes θ_2. **Site (ii) defect is RESOLVED** by §11.4.6's revision; the earlier framing of this site as "the rule cannot reach the source firing regardless of σ" was correct under the pre-2026-06-23 `last`-keyed premise and is no longer correct. Nathan's "no per-intention perceive at ε_1" becomes a licensed σ-choice (operator chose to defer perceiving and resource γ_2 instead) rather than a defect artifact. σ at §13.6 carries this choice; the §13.6 empty-independence argument (repaired §13.6.2 + §13.6.3) catches R-rr via its symmetric `LastEffect = θ-body` write that breaks every downstream `last`-reading rule's premise.
- **At `last = ε_2-body`** (after T11 row 1): R-perceive fires (T11 row 2). The terminal perceive is the lifecycle's only R-perceive firing.

Under §11.4's premise structure (post-2026-06-23 §11.4.6 revision), Nathan's σ has non-trivial choice points at the licensed σ-discretion states per §1.4.5: `γ_1-body single-γ` (R-intention vs R-required-resources — Nathan picks R-intention first) and `ε_1-body γ-pending` (R-perceive vs R-perceive-failure vs R-required-resources — Nathan picks R-rr to write θ_2, per §11.4.6's pending-θ-set premise). **§13.6 validated for Nathan with the §11.4.6 revision landed and σ-choices at the licensed forks made explicit.** Under §11.4.6's set-based premise plus σ-pinning at the licensed forks (e.g., "R-intention first at `last = γ_1-body`; R-rr first at `last = ε_1-body` with PendingTheta ≠ ∅"), Nathan's trace is determinate. The firing-order discipline within the pending-θ set is two-case confirmed (Sarah + Nathan) as declaration-order at K=2; the conservative pin keeps the door open for K≥3 batched data to refine further but doesn't require it for determinacy at K=2. The §13.6 empty-independence argument (repaired §13.6.2 + §13.6.3) catches R-rr via its symmetric `LastEffect = θ-body` write. Whether the set-based §11.4.6 with declaration-order plus the σ-pinning is the normative §11 policy or a case-class σ-choice is open, but **§13.6's correctness for Nathan no longer rests on a pending §11.4.6 fix — the fix has landed.**

The §14.3.3 F-4 scan, §14.3.4 validation outcome, and back-reference to §14.4/§14.5 follow after the per-theorem trace's pause checkpoint.

#### §14.3.3 Source-level inconsistencies surfaced (F-4 instances) — per-row + per-leaf-path scan

**Methodology note** (inherited from §14.4.3 / §14.5.3): every γ / θ / ι / ε / Γ / Σ / Φ / δ / ω / Ω row across T7–T11 walked individually, plus per-leaf-path enumeration within ordinal-bearing rows (especially ε and θ). Divergences listed as the scan reaches them; count set by scan completion; classifications cite mechanisms. Three failure modes named in §14.4.3 (universal-negative, pre-committed-count, asserted-mechanism) ruled out as the scan proceeds. Per Finding 2 of the §14.3 review pass, the candidate "Gap-§13.4.3 Instance 2" (T8 numeral `21`) is reclassified as F-4 transcription-class on mechanical grounds (R-spawn writes the ι; the guard reads matching `g2` designations elsewhere).

**Per-row walk record (T7 → T11):**

**Nathan F-4 instance N-1: T7 Intention 2 sign + both-primed semantic incoherence — CONFIRMED transcription-class (resolved during §14.3.4 PDF pass).** T7 row 10 (book page 179): `[a.]γ(A/i./o./g2) ≡ { [A/i./t.]Γ(A/i./t./G.)′ = { [A/i./t./D./P./c2]′ > [A/i./t./D./P./c2]′ } }`. The inner Γ body as quoted compares `[A/i./t./D./P./c2]′` against itself with `>` — **semantically incoherent** under the most natural reading (a path is not strictly greater than itself; the comparison is reflexively false). Compare T7 row 9 γ_1: `[A/i./t./D./P./c1]′ < [A/i./t./D./P./c1]` (primed-vs-unprimed, `<`, narratively "cost-with-Tom's-support < cost-without"). The narrative for γ_2 expects the same shape ("cost-with-Wanda's-approval < cost-without"), which would render as `[A/i./t./D./P./c2]′ < [A/i./t./D./P./c2]`. The most plausible reading of the source-as-quoted is a transcription error on both the sign (`>` vs `<`) and the second prime (extra prime on the right-hand side); under that reading, manual representation correction by the analyst (resolution 1).

**Verification boundary (resolved during §14.3.4 PDF pass)**: row re-pulled from the PDF; the source quote is identical (`[c2]′ > [c2]′`, both primed, sign `>`). Compared to Sarah's standard γ projection shape (`[D./P./u.]′ > [D./X_k/u.]′` — preferred utility > adverse alternative utility, distinct paths, both primed for projection), Nathan's γ_2 doesn't fit — its both-primed comparison is on the SAME path (`c2`), making the comparison reflexively false rather than a meaningful projection. The §14.4 Sarah-instance-2 lesson was that "obviously a typo" sometimes hides substantive divergence; here the alternative substantive reading (e.g., comparing two distinct projected utility computations under different premise sets with `′` overloaded) is **not supported by the row or the surrounding narrative** — Nathan T7's narrative for γ_2 ("cost-with-Wanda's-approval would be less than cost-without") aligns with γ_1's primed-vs-unprimed shape, not with any premise-overloading. **Classification confirmed: source-class transcription error, resolution (1).** Manual representation correction by the analyst.

**Nathan F-4 instance N-2: T7 Execution 1 ε path sole-dot `g.` at operator vs ordinal `g1` in body — CONFIRMED Jim/Nathan-pattern F-4 instance (resolved during §14.3.4 PDF pass).** T7 row 13: `[a.]ε(A/i./o./g./e1) → { [A/i./t./D./P./c.] - [A/i./o./g1/q.] }`. ε operator argument at `A/i./o./g./e1` uses **sole-dot `g.`** at the o-segment; ε body's cost-deduction term uses `[A/i./o./g1/q.]` with **ordinal `g1`**.

**Verification boundary (resolved during §14.3.4 PDF pass)**: corpus-wide ε operator-segment sweep completed across all five cases. **Outcome (a) "systematic notation" FALSIFIED; outcome (b) "per-case variance" CONFIRMED in a stronger three-way (four-way counting Charles K=1 baseline) form than originally framed.** Source-verified renderings:

- **Charles T5 (K=1, baseline, book p171)**: `ε(A/i./o./g./e.) → { ... + [A/i./o./g./q.] }` — uniform sole-dot at operator and body, **even though the same cycle's θ/gate use ordinal `g1`** (so sole-dot at ε is a notational habit, not ordinal-absence); harmless at K=1 because only one q exists. Sole-dot is the **unmarked ε form**. Now row-walked in §14.1 (F-4 N-3).
- **Jim T6 (K=2, book pages 175–176)**: operator sole-dot, body ordinal `g_k`.
- **Nathan T7 row 13, T11 row 1**: same operator-sole-dot / body-ordinal pattern as Jim.
- **Sarah T15 (K=2, book p201)**: `ε(A/i./o./g./e.) → { ... - [A/i./o./g./q.] }` — uniform sole-dot at operator AND body at K=2 (Sarah's broader sole-dot reuse pattern, F-4 instance 1, carries through to ε).
- **Rusty T18 (K=3, book p208)**: `ε(A/i./o./g1/e.) → { ... + [A/i./o./g1/q1] + [A/i./o./g1/q2] }` — uniform ordinal at operator AND body. §14.5.1's prior analytic claim **source-verified**.

**Classification confirmed**: N-2 is a real F-4 instance, classified on the ε row's own evidence as a **Jim/Nathan-pattern (operator-sole-dot / body-ordinal at top-level K=2 multi-intention ε)** — **NOT Rusty-T19 family** (those are detection / intention row cross-cycle mislabels, structurally distinct). **Mechanism**: at K=1 sole-dot is the unmarked default; at K=2, Jim and Nathan retain sole-dot at operator while specifying g_k at body (the body recovers what the operator's sole-dot omits). **Mechanical consequence**: R-execute's `R ⊖ [body-path]` resolves unambiguously because the body specifies the ordinal — the operator's sole-dot is **notational variance R-execute tolerates**. This is structurally distinct from Sarah's uniform-sole-dot pattern, which IS a reproduction-failure sub-case (body's sole-dot is ambiguous). **Filed under Axis 8 (R-execute operator-to-g_k resolution under-spec); see §13.5.9 Gap-§11.4 Axis 8 entry for the corpus-wide structural finding and the precise Sarah-sub-case-only reproduction-failure framing.**

**Nathan F-4 instance N-3: T8 ι row 1 numeral `21` rendering vs ordinal `g2` (transcription-class, demoted from Gap-§13.4.3 candidate per §14.3 review Finding 2).** T8 row 1 (book page 181): `[a.]ι(A/i./o./21/i.) := { [A/i./o./21/q.] }`. Uses numeral `21` at the o-segment where parent-pending-q's ordinal `g2` is expected. **Mechanical analysis**: R-spawn's contractum (per Gap-§11.4.2's resolved branch) sets the sub-cycle ι := { parent-pending-q } — R-spawn *writes* this row. R-spawn does not *test* a pre-existing ι; there is no equality test at the spawn step to fail. Every other o-segment in Wanda's sub-cycle (T8 rows 2–9 detection body, intention, θ; T10 rows 1–5 execution, perception, outcome, obtained utility, Φ) renders `g2` correctly. Randy's R-resume guard at T11 reads `[A/i./o./g2/q.]` from Wanda's Φ (T10 row 5, book page 188) against `[A/i./o./g2/q.]` in the S-entry — passes literally. **The `21` is a transcription artifact in a row the system produces as `g2` anyway, with zero mechanical consequence.** Visual similarity of `g2` and `21` in some fonts is the most plausible origin. Resolution (1) source-correction; manual representation correction by the analyst.

**Nathan F-4 instance N-4: T8 Detection row 2 operator-vs-body g_1/g_2 mismatch.** T8 row 2 (book page 181): `[a.]δ(A/i./o./g1/i./d.) := { [A/i./o./g2/i./t.], [A/i./o./g2/i./t./D./P.], [A/i./o./g2/i./t./D./X.] }`. δ operator argument at **g_1**, body at **g_2**. Same shape as Rusty T19 detection-row mismatch (instance 3 in §14.5.3). Manual representation correction required.

**Nathan F-4 instance N-5: T8 Intention row 7 γ-at-g_2-with-inner-Γ-body-at-g_1 mismatch.** T8 row 7 (book page 182): `[a.]γ(A/i./o./g2/i./o./g.) ≡ { [A/i./o./g2/i./t.]Γ(A/i./o./g2/i./t./G.)′ = { [A/i./o./g1/i./t./D./P./u.]′ > [A/i./o./g1/i./t./D./X./u.]′ } }`. Outer γ at `(A/i./o./g2/i./o./g.)` with inner Γ body using **g_1** paths. Cross-cycle path reference: a g_2 sub-cycle's intention body references g_1-prefix paths. Same shape as Rusty T19 instance 4 (Σ-argument g_1 in g_2 sub-cycle). Manual representation correction required.

**Nathan F-4 instance N-6: T9 Detection row 2 stray space `i. /d.` (formatting artifact).** T9 row 2 (book page 183): `[a.]δ(A/i./o./g2/i./o./g./i. /d.) := { ... }`. The argument path has a stray space between `i.` and `/d.` — formatting artifact, not a semantic divergence. The constituent path is otherwise well-formed. Lexer-level whitespace normalization handles it; no representation correction needed.

**Nathan F-4 instance N-7: T11 Execution row 1 ε path sole-dot `g.` at operator vs ordinal `g2` in body — CONFIRMED Jim/Nathan-pattern F-4 instance (resolved during §14.3.4 PDF pass; same corpus sweep as N-2).** T11 row 1 (book page 188): `[a.]ε(A/i./o./g./e.) → { [A/i./t./D./P./c.] - [A/i./o./g2/q.] }`. ε operator argument at `A/i./o./g./e.` uses **sole-dot `g.`** at the o-segment; ε body's cost-deduction term uses `[A/i./o./g2/q.]` with **ordinal `g2`**. Same row-type as N-2 and resolves identically: per the corpus sweep, this is the Jim/Nathan operator-sole-dot / body-ordinal pattern at top-level K=2 multi-intention ε — notational variance R-execute tolerates because the body specifies `g_k`. **Filed under Axis 8** alongside N-2; both instances of the same corpus-wide pattern.

**Nathan F-4 instance N-8: Γ-path divergences across projected and realized perception rows (D-26/D-27 normalization-handled).** Walk of Γ rows: projected forms in γ-bodies (T7 row 9 γ_1, T7 row 10 γ_2, T8 row 7 γ, T9 row 7 γ) use `Γ(.../G.)′` — drop `/D./`; realized forms in perception rows (T9 row 11 perceive, T10 row 2 perceive, T11 row 2 perceive) use `Γ(.../D./G.)` — drop `/t./`. Same shape as Sarah F-4 instance 3 and Rusty F-4 instance 6. **Automatic lexer normalization** via D-26 (§8.2.2 line 534, inserts `/t./` for realized) and D-27 (§8.2.2 line 549, inserts `/D./` for projected). Verified for every Γ row in T7–T11.

**Per-leaf-path enumeration within ε rows** (the methodology's V-3-strengthening, per §14.4.3's prior catch of Sarah's ε_1/ε_2 double-execute): T7 has one ε (row 13, leaf `/e1`); T8 has no ε (lifecycle interrupted at gate-fail row 9); T9 has one ε (row 10, leaf `/e.`); T10 has one ε (row 1, leaf `/e.`); T11 has one ε (row 1, leaf `/e.`). Total ε firings across T7–T11: **four**, each at a distinct intention-path within its respective cycle. **No T14-style ε_1/ε_2 double-execute within any single Nathan cycle.** Nathan's top-level cycle has K_exec = 2 (γ_1 at T7, γ_2 at T11) but each γ has a single ε firing; sub-cycles each have K_exec = 1. **Nathan does NOT corroborate Sarah F-4 instance 4** (per-intention multi-execute); Sarah's double-execute remains a Sarah-specific finding, isolated under Gap-§11.4 Axis 5.

**Scan conclusion (post-§14.3.4 PDF pass — all eight items settled)**:

1. **N-1**: T7 γ_2 sign + both-primed semantic incoherence. **Transcription-class confirmed** via row re-pull (no plausible substantive alternative reading from row or narrative). Resolution (1), manual representation correction.
2. **N-2**: T7 ε_1 sole-dot `g.` at operator vs ordinal `g1` in body. **F-4 instance confirmed via corpus-wide ε sweep**: Jim/Nathan operator-sole-dot / body-ordinal pattern at top-level K=2 multi-intention ε — notational variance R-execute tolerates (body specifies `g_k`). Filed under Axis 8 (corpus-wide R-execute operator-to-g_k resolution under-spec). **Not Rusty-T19 family** (those are detection / intention row cross-cycle mislabels, structurally distinct).
3. **N-3**: T8 ι numeral `21` vs ordinal `g2`. **Transcription-class, demoted from Gap-§13.4.3 candidate** per §14.3 review Finding 2 (R-spawn writes the ι; zero mechanical consequence). Settled.
4. **N-4**: T8 δ operator-body g_1/g_2 mismatch (cross-cycle reference in detection row). Manual representation correction. Settled.
5. **N-5**: T8 γ-at-g_2-with-inner-Γ-body-at-g_1 (cross-cycle reference in intention row). Manual representation correction. Settled.
6. **N-6**: T9 δ stray space `i. /d.`. Lexer whitespace normalization. Settled.
7. **N-7**: T11 ε_2 sole-dot `g.` at operator vs ordinal `g2` in body. **F-4 instance confirmed via same corpus sweep as N-2**: identical Jim/Nathan-pattern at the resume-completion turn. Filed under Axis 8.
8. **N-8**: Γ-path divergences across all projected and realized perception rows in T7–T11. Automatic lexer normalization (D-26, D-27). Settled.

The methodology's three failure modes (universal-negative, pre-committed-count, asserted-mechanism) all foreclosed per the row + leaf-path discipline; **per-leaf-path enumeration on ε rows confirms Sarah F-4 instance 4 (per-intention multi-execute) does not repeat in Nathan**, matching Rusty. **The §14.3.4 PDF pass also surfaced one new corpus-wide structural finding (Axis 8) that no single case's local scan would have caught** — it took the multi-case ε sweep to reveal that the operator-to-g_k resolution at §11.4.8 is under-specified across all five cases, with Sarah's uniform-sole-dot pattern as the reproduction-failure sub-case and the others as notational variance R-execute tolerates. The Axis 8 finding is structurally distinct from any F-4 instance (which is per-row representation evidence) — see §13.5.9 Gap-§11.4 Axis 8 entry.

#### §14.3.4 Validation outcome

Nathan Tables 7–11 establish:

- **§13.1**: validated at the parent's γ-row layer (g_1/g_2 distinct ordinals at the parent, no Sarah-style sole-dot reuse at parent level). Sub-cycle prefixes (`A/i./o./g2/i.` at depth-1; `A/i./o./g2/i./o./g./i.` at depth-2) maintain per-actor scope. **Settled cross-cycle-reference mislabels** (N-4 T8 δ operator at g_1 with body at g_2; N-5 T8 γ at g_2 with inner Γ body at g_1) are operator-body mismatches in detection / intention rows classified on their own evidence as F-4 instances, not §13.1(W) violations. **N-2 (T7 ε_1) and N-7 (T11 ε_2) — settled post-§14.3.4 corpus ε sweep**: per-case variance confirmed (outcome (b), three-way / four-way counting Charles baseline); N-2/N-7 are F-4 instances of the Jim/Nathan operator-sole-dot / body-ordinal pattern at top-level K=2 multi-intention ε, classified on the ε rows' own evidence — **distinct from N-4/N-5's detection/intention-row cross-cycle mislabels**. The earlier conflation was retracted in §14.3.3. The corpus-wide structural finding the sweep surfaced is **Axis 8 (R-execute operator-to-g_k resolution under-spec)**, filed at the catalog level rather than as a §13.1 finding because the mechanism is at R-execute's body-resolution premise, not at path-uniqueness.
- **§13.2**: validated contingent on Axis 3a precedence being pinned, and T8 mislabels being treated as representation corrections. **Axis 1b Sites (i) and (ii) are no longer §13.2 contingencies (as of 2026-06-23)**: §11.4.6's pending-θ-set premise revision admits Nathan's θ_1 (T7 row 11, Site (i)) and θ_2 (T7 row 14, Site (ii)) firings directly; the rule's contractums are well-typed at Layer 2 per §13.2.2 in the revised form just as in the prior. The T8 `21` rendering is transcription-class and carries no §13.2 contingency.
- **§13.3**: validated abstractly post-D-26/D-27 normalization (per N-8).
- **§13.4**: **validated for Nathan with NO contingency** — all four pinning-relevant points hold literally under R-spawn's contractum-writes-ι discipline (spawn-start Randy→Wanda; spawn-start Wanda→Mike; depth-2 delivery Mike→Wanda; depth-1 delivery Wanda→Randy). **The depth-weighted induction's depth-2 base case (§13.5.2 measure + §13.5.4 well-foundedness; formerly old §13.5.6) is EARNED**, with no resume-guard-designation-variance shadow.
- **§13.5**: validated; depth-2 termination + progress hold; the K-executes/1-terminal-perceive observation re-attributed per §1.4.5 (per-intention perceiving is `ε-body` no-γ-pending guard-determined Pillar 2; the terminal-only pattern is now-licensed-σ-discretion at `ε_1-body` γ-pending per §11.4.6's 2026-06-23 revision, formerly the Site (ii) defect artifact) — not an open Axis 7.
- **§13.6**: **validated for Nathan (no pending §11.4.6 contingency as of 2026-06-23)**. §11.4.6's pending-θ-set premise revision admits Nathan's θ_1 (Site (i)) and θ_2 (Site (ii)) firings; σ at the licensed forks per §1.4.5 (γ_1-body single-γ → R-intention; ε_1-body γ-pending → R-rr — Nathan's chosen sequence) makes the trace determinate. §13.6's empty-independence argument is repaired via the symmetric-write half of the last-dependency clause (§13.6.2 + §13.6.3), catching R-rr's `LastEffect = θ-body` write. The prior framing's "Axis 7 perceive-vs-skip σ choice" was a mis-classification (the Site (ii) state now hosts licensed σ-discretion among R-perceive, R-perceive-failure, and R-rr — Nathan picks R-rr; σ disambiguates). The Site (i) and Site (ii) "defect-blocked under the current rule" framings are superseded by the §11.4.6 revision.

Nathan does **not** establish: depth-≥3 nesting (Mike bottoms out at depth-2; T9 row 9 gate ∋ confirms no further escalation); parent-retry-after-sub-cycle-failure (F-3, abstract — Nathan's three sub-cycles all succeed at delivery); Rusty's Axis 6 (two-θ-per-γ — Nathan's θ rows are each singular-q); **Axis 2 at its corrected state `⟨perceive-failure, C⟩` per §1.4.5** (Rusty-witnessed only — Nathan does not have the dynamic-intention-addition pattern; the prior characterization of Axis 2 as "ε-body fork" was the phantom dissolved during the state-fork pivot); Sarah's Axes 3b (batched θ with multi-spawn — Nathan spawns Wanda before declaring θ_2 alternatively, but per the source γ_2 declaration precedes θ_1 — see Axis 3a vs 3b note), 4 (moot-by-sub-cycle-outcome — Nathan's both intentions execute and produce utility), 5 (per-intention multi-execute — Nathan has one ε per γ per the per-leaf-path scan).

**Nathan grounds Gap-§11.4 across multiple lifecycle states per §1.4.5's state-fork derivation (post-2026-06-23 §11.4.6 revision)** (in addition to confirming depth-2 for the depth-weighted induction's base case (§13.5.2 measure + §13.5.4 well-foundedness; formerly old §13.5.6)): **Axis 3a (batched γ-declarations)** reproduced as a second case alongside Sarah — locates at the `γ_1-body single-γ` state, licensed σ-discretion in the §1.4.5 table; **Axis 1b Sites (i) and (ii)** exercised at `last = γ_2-body` (with Sarah) and at `last = ε_1-body` (Nathan-only) — both defects surfaced the Rule 2 reproduction-failure signal on §11.4.6's prior `last`-keyed premise (two-case confirmed Sarah + Nathan, declaration-order θ-firing at K=2). **Both Sites RESOLVED 2026-06-23 by §11.4.6's pending-θ-set revision**: Nathan's θ_1 and θ_2 firings are now mechanically admissible. Nathan's "no per-intention perceive at ε_1" becomes a licensed σ-choice at the Site (ii) state (now σ-discretion, no longer defect) — operator chose to defer perceiving and resource γ_2 instead, with σ at §13.6 carrying the choice. **The perceive-cardinality observation** (Nathan's K-executes/1-terminal-perceive contrasted with Rusty's K/K and Sarah's 1+moot) re-attributed per §1.4.5 across three distinct lifecycle states — guard-determined `ε-body` for Rusty's per-intention pattern; licensed σ-discretion at `ε_1-body γ-pending` for Nathan's terminal pattern (post-2026-06-23 revision); Axis 4 R-moot defect for Sarah's 1+moot pattern. **Axis 8 R-execute body-resolution** at `⟨gate-pass, q⟩` — Sarah-T15-only reproduction failure, Nathan's T7/T11 ε rows survey as non-problem (body specifies `g_k`).

**Eight items surfaced from Nathan's §14.3.3 per-row + per-leaf-path scan — all settled post-§14.3.4 corpus PDF pass**:

- **Transcription-class** (two): **N-1** T7 γ_2 sign + both-primed semantic incoherence (row re-pull confirmed no plausible substantive alternative reading; resolution 1, manual representation correction). **N-3** T8 ι numeral `21` (R-spawn writes the ι; zero mechanical consequence; demoted from Gap-§13.4.3 candidate per §14.3 review Finding 2).
- **Cross-cycle-reference mislabels in detection/intention rows** (two): **N-4** T8 δ operator at g_1 with body at g_2 (manual representation correction). **N-5** T8 γ at g_2 with inner Γ body at g_1 (manual representation correction).
- **Jim/Nathan top-level ε operator-body convention** (two — filed under Axis 8): **N-2** T7 ε_1 sole-dot `g.` at operator vs ordinal `g1` in body, **N-7** T11 ε_2 sole-dot `g.` at operator vs ordinal `g2` in body. Per-case variance confirmed by §14.3.4 corpus sweep; notational variance R-execute tolerates because the body specifies `g_k`. Filed under Axis 8 (corpus-wide R-execute operator-to-g_k resolution under-spec).
- **Formatting / lexer-handled** (two): **N-6** T9 δ stray space `i. /d.` (lexer whitespace normalization). **N-8** Γ-path divergences across all projected and realized perception rows (D-26/D-27 normalization-handled).

The methodology's three failure modes all foreclosed per the row + leaf-path discipline; per-leaf-path enumeration confirms Sarah F-4 instance 4 does not repeat in Nathan (matching Rusty's per-leaf-path scan result). **The §14.3.4 PDF pass also surfaced Axis 8 (R-execute operator-to-g_k resolution under-spec) as a corpus-wide structural finding that no single-case scan could have caught** — it took the multi-case ε sweep to reveal the five-case structural under-specification at §11.4.8, with Sarah's uniform-sole-dot as the reproduction-failure sub-case and the others as notational variance. The Axis 8 finding is filed at the catalog level (Gap-§11.4) rather than as a Nathan F-4 instance, because its mechanism is at R-execute's body-resolution premise rather than at per-row representation evidence; N-2 and N-7 are filed both as Nathan F-4 instances (the per-row evidence) AND under Axis 8 (the corpus-wide structural home).

**Next-PDF-pass scope (closed post-§14.3.4 PDF pass — all four verifications resolved)**:

1. **Sarah T12 row order under the Axis 1b lens** ✓ resolved: Sarah's T12 fires θ_1 (row 12, book p192) before θ_2 (row 14), matching Nathan. **Two-case confirmation of declaration-order θ-firing at K=2.** Axis 1b pin: declaration-order (the conservative framing K=2 data supports; oldest-first is the K=2 specialization indistinguishable on K=2 data; K≥3 batched would refine further but no such case exists in corpus).
2. **Corpus-wide ε operator-segment sweep across all five cases** ✓ resolved: Charles T5 K=1 baseline (uniform sole-dot — unmarked default); Jim T6 K=2 (operator sole-dot, body ordinal — notational variance); Sarah T15 K=2 (uniform sole-dot at K>1 — reproduction-failure sub-case); Nathan T7/T11 K=2 (Jim-pattern); Rusty T18 K=3 (uniform ordinal — disciplined form, §14.5.1 inherited claim source-verified). **Outcome (b) per-case variance confirmed in stronger five-case form than originally framed.** Surfaced **Axis 8** as new corpus-wide structural finding (R-execute operator-to-g_k resolution under-spec; reproduction-failure only for Sarah sub-case, notational variance for others — see §13.5.9 Gap-§11.4 Axis 8 entry).
3. **N-1 row re-pull** ✓ resolved: Nathan T7 row 10 source quote confirmed (`[c2]′ > [c2]′`, both primed, sign `>`); no plausible substantive alternative reading from row or surrounding narrative; transcription-class classification confirmed.
4. **Charles T5 ε corpus completeness check** ✓ resolved: Charles T5 K=1 execution at uniform sole-dot (book p171). Establishes sole-dot as the unmarked default form at K=1, with ordinal as the marked variation used when K>1 needs disambiguation. This baseline reading sharpens Axis 8's framing — Sarah's uniform-sole-dot is "default form preserved into K>1 territory where disambiguation is needed and breaks," while Rusty's uniform-ordinal is the explicit marked form. Five-of-five corpus cases now source-verified at the ε level.

**The prep-doc mirror is now unblocked** — the catalog state is settled at the eight-axis structure with declaration-order Axis 1b pin, Axis 8 as the new corpus-wide finding, all eight Nathan F-4 instances classified, and Jim newly visible in the cross-case distribution. The mirror update should reflect these settled findings; deferred to next turn unless directed otherwise.

**Back-reference to §14.5 Rusty** (the K>1 contrast that §1.4.5's state-fork derivation re-attributes across three lifecycle states, rather than as a single Axis 7): Rusty's interleaved K=3 with per-intention R-perceive lands at `ε-body` no-γ-pending guard-determined Pillar 2 state per §1.4.5 row 123 — the firing is selected by the realized comparison (Pillar 2 interpretive judgment), not by σ-discretion. Nathan's batched K=2 with terminal R-perceive lands at `ε_1-body` γ-pending — now licensed σ-discretion at this state (post-2026-06-23 §11.4.6 revision; R-rr, R-perceive, R-perceive-failure all admissible per σ); the prior framing of this state as the "Site (ii) defect" was correct under the pre-2026-06-23 premise but is now superseded — Nathan's terminal-only perceive is the operator's σ-choice to defer perceiving and write θ_2 instead. Sarah's batched K=2 with 1 execute + 1 moot lands at the post-resume R-moot defect (§1.4.5 Axis 4 legacy — cycle-scoped contractum can't supply intention-scoped moot; this defect remains open). **The "perceive-cardinality multi-modal axis" framing was superseded by §1.4.5's state-fork derivation**: each case's perceive-pattern attaches to its own lifecycle state, with two of the three states now hosting licensed σ-discretion (Rusty's and Nathan's, post-§11.4.6 revision) and one remaining a defect (Sarah's, Axis 4). The observation that the three cases differ in their perceive behavior stays as source-verified data; the disposition is "resolved per §1.4.5 across three states (two licensed σ, one remaining defect at Axis 4)" rather than "open at one axis."
