---
Item_ID: plc-roadmap
type: Fleeting
timestamp: "2026-07-02T00:00:00Z"
title: "Political Landscape Cartography — Roadmap"
Date_Added: 2026-07-02
Date_Modified: 2026-07-24
Needs_Processing: false
AI_Instructions: "The spin-off ledger: what the dissertation and the LSPI Formal Foundation can still yield, with build status. Consult when the operator asks 'what's next for the methodology' or proposes new formal work."
---

# Roadmap — the Spin-off Ledger

*Chapter 5 of the dissertation contains roughly ten distinct expandable ideas; slash addressing was the one that spun off first (and became LSPI). This ledger tracks all of them plus the frontiers the LSPI Formal Foundation names. Status as of v1.2.0 (2026-07-24).*

**How to read a status.** Upstream (`_frameworks/lspi/` mirrors, and the Expandable-Ideas source) ranks these in three tiers — Tier 1 the deep formal spin-offs, Tier 2 the smaller ones, and a meta tier. Where PLC's status differs from upstream's, the divergence is noted in the row rather than silently resolved. Two housekeeping carries from the source: the ideas already **absorbed** and explicitly not to be re-mined are the interaction cycle itself, the recursion / call-stack structure, the decision-matrix mechanics, the category ontology, and slash addressing (now LSPI); and a "schema landed" status is not a built status — a reserved key with values in it is data, not a theory.

## The ten expandable ideas

| # | Idea | Status | Where it stands |
|---|------|--------|-----------------|
| 1 | **Influence-tactic taxonomy** ("ATT&CK for organizational politics") | **BUILT — and exceeded** (Tier 1) | The 782-tactic catalogue (16 strategies, 83 clusters, 50 theorists). Integration is now complete too: the ε-template binding and all seven facets landed with WS4 passes 1–6 (2026-07-24) |
| 2 | **Resource typology — theory of political capital** | **PARTIALLY BUILT** | The actuator side of the Matrix-Estimation Layer delivers the intensional definition, effect signatures, contextual worth, convertibility edges, and gain-cycle compounding (`08-ESTIMATION.md`). The full "thermodynamics of power" — storage, decay, appreciation, a complete conversion grammar — remains the deepest open formal spin-off |
| 3 | **The favor bank — a formal credit system** | OPEN (vivid, self-contained) | The corpus has the *tactics* (0158 The Favor Bank Run, 0097 Social Debt Creation) and family 9 has the `owes/owed-by` ledger relation; the formal model — issuance, settlement, default (→ blame), interest, timing risk — is unbuilt. Product form: a literal favor ledger |
| 4 | **Detection — epistemics of political reconnaissance** | **BUILT, UNCALIBRATED** (Tier 1) | The Matrix-Estimation Layer (v0.4) is this idea, formalized: belief states, VoI probes, adversarial observation model, depth. Operationalized as `08-ESTIMATION` + `PLC_Detection_Record` + ESTIMATE. **Divergence from upstream:** the source still lists #4 as a co-#1 *open* frontier. Both readings are fair — the machinery is built and shipped, and every quantity in it is uncalibrated (see the six calibration flags in `08-ESTIMATION.md`, governed by P13). Read "built" as *the structure exists and is operable*, not *the numbers are trustworthy* |
| 5 | **Projection vs realization (′) — theory of political miscalculation** | PARTIALLY CARRIED | The prime discipline persists both values; pre-registered predictions + QUARTERLY-AUDIT forecast-calibration review give it a procedure. The full theory (expectation error, second-order effects, overshoot dynamics — Charles got a termination when he projected a demotion) remains open |
| 6 | **Algebra of the tactic space** (antithetical duals; generating basis) | OPEN — but now cheaper (Tier 2) | Table 3 is visibly built from dual pairs (threaten-to-withdraw ↔ pledge-to-offer); the 16 generic strategies already fold some of this in. The conjecture: the tactics are *generated* from a small primitive basis × the four-cell / sign axes. Upstream calls this a **byproduct** of the integration program — and the integration is now done: 2,254 typed lever entries plus the defense graph are exactly the data a generating-basis search would run over |
| 7 | **Certainty classes — probabilistic tactic efficacy** | DATA LANDED (WS4 complete) | `certainty_class` is populated for all 782 tactics (612 extra_conditional / 144 probable / 25 certain / 1 spurious) — but these are **P10 interpretive proposals pending operator QA**, not measurements. The expected-value model of political plays (risk-weighting maneuvers against these classes) remains open, and is what would turn the data into the idea |
| 8 | **Willingness vs ability — two axes of influence** | OPEN | Clean motivation-vs-capacity decomposition cross-cutting the whole catalogue; candidate future tactic facet |
| 9 | **GTM General Structure — reusable grounded-theory pipeline** | OUT OF PLC SCOPE | A methods contribution and AI-tooling candidate (LLM-assisted open/axial/selective coding); a different product line — recorded here so it isn't lost |
| 10 | **The ethics bracket — normative overlay** | PARTIALLY EXPRESSED | PLC's two gates + the WS4 `ethical_valence` facet are the operational expression; the formal normative framework (influence vs manipulation line, ethics of detection) remains open — and connects to the "seatbelt, not wiretap" visibility model |

## Frontiers named by the LSPI Formal Foundation

- **The reflexivity research program** (`_frameworks/reflexivity-frontier.md`, frontier: true): the two-sided level-k signaling game, publicize verb Ξ, common-knowledge bookkeeping. Blocked on its own open problems — sharpest: the almost-common-knowledge discontinuity (publication has tipping effects, not smooth ones). The publishable contribution, if it exists, most likely lives in depth-estimation or the discontinuity.
- **Empirical calibration**: loss weights (L_under/L_over), managed-signal likelihoods, sufficiency risk allowance, and the depth distribution of executive populations — answerable from engagement data; doubles as validation for the 4R ladder.
- **Machine-checked proof** of the LSPI meta-theorems — rigor track, only if wanted.
- **Product/MVP spec** — the named gap: the theory is build-ready; the *product translation* (screens, data model, the loop as a service, catalogue API) is unwritten. Belongs beside the volume, not in it.
- **Vector-DB / semantic search** over the faceted catalogue (the corpus's own NEEDED_NEXT item). **Now unblocked**: the facets landed in `INDEX-lspi.json` (the sidecar, not `INDEX.json` — the catalogue bodies are Mode E and are never edited). Note the consumer-side gap this leaves: MOVE-LOOKUP still reads `INDEX.json`, so nothing yet queries the facets at session time. Wiring that read is the smallest high-value next step in the product track.
- **Remaining upstream defect**: LSPI §11.4.7 multi-q gate semantics (Axis 6) — until resolved upstream, PLC templates hold the one-q-per-gate-test constraint.
- **Table 3 Move files**: 3 of **148** authored; the WS4 pass-6 provenance cross-walk covers the mapping need via the manifest; full authoring is backlog.
- **Coverage finding from the provenance cross-walk** (pass 6, 2026-07-24): 127 of the 148 Table-3 rows have at least one corpus descendant. The 21 rows with none — 5, 6, 7, 9, 27, 36, 61, 72, 82, 84, 85, 86, 88, 89, 90, 91, 92, 103, 111, 116, 120 — are either genuine corpus gaps or rows whose mechanism the corpus expresses under a different frame. Resolving which is a small, well-scoped piece of work with a real payoff: it is the only direct evidence about whether the 782 actually *covers* the grounded-theory base.
- **Missing shipped sources**: `_frameworks/sources/` carries a pointer for the Lam 2018 dissertation only; the ADAPT field manual, OPC v3.0, and the catalogue's own source JSON are referenced but not shipped. `_frameworks/strategies/` holds no strategy atom files (the 16 strategies live only as catalogue `by-strategy/` pages). LSPI Figures 3–4 are upstream-only and not mirrored.

## Sequencing principle (carried from the source)

Pick **one** formal idea at a time, give it the rigor slash-addressing got, and let it earn its own name — while catalogue-integration runs in parallel as the product track. The two deepest candidates for the next genuine formal spin-off: **#2 (political capital)** and **#3 (the favor bank)** — #2 defines what power is made of; #3 is self-contained enough to be its own paper *and* its own product feature.

*(Upstream's own pairing is #2 and #4. PLC substitutes #3 for #4 because #4's machinery is now built and shipped — what remains of #4 is calibration, which is empirical work rather than a formal spin-off. The substitution is recorded here so the change of ranking is visible rather than inherited silently.)*
