---
Item_ID: plc-lspi-ws4-runbook
type: Fleeting
timestamp: "2026-07-02T00:00:00Z"
title: "WS4 Runbook — Catalogue LSPI Binding: Status and Remaining Passes"
Date_Added: 2026-07-02
Date_Modified: 2026-07-24
Needs_Processing: false
AI_Instructions: "The repeatable procedure for completing the catalogue facet passes. Each pass is independent and resumable. Passes 1-6 are COMPLETE as of 2026-07-24; the procedure is retained for re-runs. Update the status table as passes complete. All writes go to INDEX-lspi.json (the sidecar) — never to the Mode E tactic files."
---

# WS4 Runbook — Catalogue LSPI Binding

*Target artifact: `_frameworks/political-warfare-catalogue/INDEX-lspi.json` (the sidecar; the catalogue itself is Mode E and is never edited). Schema reference: `_types/PLC_Tactic.md` § Optional LSPI facets. Spec: the upstream Tactic-Corpus-LSPI-Integration-Spec (mirrored context in `_lspi-README.md`).*

## Status

| Pass | Content | Method | Status |
|------|---------|--------|--------|
| 1 | P/Adv alias adoption | documentation | **DONE** (04-SCHEMA System 1; sidecar `alias_map`; catalogue README note) |
| 2 | `lspi_levers` + `epsilon_template` (783 records) | mechanical extraction — **script saved at `../political-warfare-catalogue/tools/extract-lspi-levers.py`; re-run any time (idempotent; preserves interpretive facets)** | **DONE** 2026-07-02, register corrected 2026-07-24 — 779 records carry levers: **774** from Active Levers sections + **5** from the strategy-combination fallback; 4 empty-lever exceptions (below) |
| 3 | `required_resources` | LLM-assisted tagging, sampled QA | **DONE** 2026-07-24 — 782 of 783 |
| 4 | `detectability`, `certainty_class`, `ethical_valence` | LLM-assisted tagging, sampled QA | **DONE** 2026-07-24 — 782 of 783 |
| 5 | `counter_tactic_ids` (defense graph) | LLM-assisted promotion of Resolution Approach prose | **DONE** 2026-07-24 — 152 records, 174 links; reciprocal on 70 |
| 6 | `provenance` cross-walk (Table 3 + vignettes → tactic IDs) | LLM-assisted matching against `../dissertation-table-3/Table-3-Manifest.md` (148 rows) | **DONE** 2026-07-24 — 606 records; **127 of 148** rows covered; 21 uncovered (below) |

Sidecar as built: `version: 1.2.0-ws4.6`, `generated_at: 2026-07-24`.

## Measured outcome (2026-07-24)

- **Passes 3–4 — full-corpus facet coverage.** **782 of 783** records carry `required_resources`, `detectability`, `certainty_class` and `ethical_valence`. The 783rd is the corpus placeholder `0037` ("not a tactic — placeholder for my notes"), whose `facet_status` records that facets are not applicable rather than missing. No tactic body was touched (Mode E holds).
- **Pass 5 — the defense graph.** **152** records carry `counter_tactic_ids`, totalling **174** links. `counters_tactic_ids` is the *derived reciprocal* (countered-by ↔ counters) and lands on **70** records; it is generated, never hand-authored — regenerating from `counter_tactic_ids` is the only supported way to change it. Sparse by design: prose counters that are postures rather than catalogue tactics were left as prose and given no link (the pass-5 rule below).
- **Pass 6 — provenance.** **606** records carry `provenance.lam_table3_refs`; those references touch **127 of the 148** manifest rows. Per-tactic provenance is the sidecar's, not the manifest's — the manifest still has no corpus-ID column, and the cross-walk results are recorded there in summary form (`../dissertation-table-3/Table-3-Manifest.md`).

### Pass-6 coverage-validation finding — 21 Table-3 rows with no corpus descendant

This is the first of the cross-walk's two products (the second is the citable bridge to the 25 interviews). Every Table 3 row *should* have ≥ 1 corpus descendant; these 21 have none:

> **5, 6, 7, 9, 27, 36, 61, 72, 82, 84, 85, 86, 88, 89, 90, 91, 92, 103, 111, 116, 120**

Read them as a **corpus-coverage gap, not a manifest error**: the rows are dissertation-attested actions the 782-tactic corpus never elaborated (rows 84–92 are almost the whole *"Compromised: made adjustments to the request…"* concession family — the corpus is thin on fine-grained negotiation concessions). Two honest dispositions per row — either a corpus tactic exists and the semantic match was missed (re-check on the next QA sweep), or the action genuinely has no tactic and is a candidate for corpus extension. Do not close a row by weakening the match criterion; sparse-and-true beats dense-and-fabricated (F2).

### Pass-2 exception register (corrected 2026-07-24)

The register published on 2026-07-02 was wrong in two places. Corrected:

- **Empty-lever set = `{0015, 0028, 0031, 0037}`** — four records for which no levers are derivable.
  - `0015`, `0031` — ORIGINAL-type analyses: no Active Levers sections and no strategy lever-combination to fall back on.
  - **`0028` (Malicious Compliance) — every lever heading present but all marked "Not active."** Previously unreported: the earlier register missed it because the record *has* an Active Levers section, so it was counted as a source-hit while yielding zero levers. It is a genuine empty-lever case, not an extraction failure.
  - `0037` — the corpus placeholder record (not a tactic).
- **`0014` (Organizational Gaslighting) is NOT an empty-lever case.** It is partial-but-populated: one statusless `C(X)↓` heading is skipped, its other levers extract normally. Flag only.
- **Source split is 774 / 5, not 775 / 4** — 774 records from Active Levers sections plus 5 from the strategy-combination fallback = 779 with levers. (The raw `lever_source` tally reads 775 for `active-levers-sections` because `0028` carries the tag while yielding nothing; count populated records, not tagged ones.)

The extractor now **reports these cases explicitly** rather than silently dropping them — statusless headings, all-Not-active records, and missing sources each emit a named problem line — and it **dedupes duplicate lever blocks** where the corpus lists the same component twice under alternative interpretations (`0010`, `0012`), merging on the component and keeping the maximum intensity. Re-running is still idempotent and still preserves interpretive facets.

### ε-template conformance (closed 2026-07-24)

The template now carries the spec's **three-place** form:

```
[a.] ε_ID(<addr>/e.) → { deltas } consuming { θ }
```

The earlier two-place rendering dropped the `consuming { θ }` place, which is load-bearing — it is the resource commitment the capability-gate tests. Alongside the string, each record carries `epsilon_tuple` holding the same content **structurally**: `delta` (the signed, intensity-weighted component list), `theta` (typed resources with `enabling` / `consumed` roles), and `meta` (detectability, certainty class, ethical valence). That closes the dropped-θ conformance defect against `Tactic-Corpus-LSPI-Integration-Spec.md` (mirrored in this folder) — consumers should read `epsilon_tuple` and treat the string as display.

## The round-trip anchor (validated 2026-07-02)

Tactic **0158 — The Favor Bank Run** expresses one mechanism in all four registers:

1. **Corpus levers:** `C(X)↓ ·3 + C(Y)↑ ·3` (strategy #8 Cost Contrast)
2. **ε-template (sidecar), three-place form:** `[a.] ε_0158(<addr>/e.) → { [<addr>/t/D/P/c] − ·i3, [<addr>/t/D/Adv/c] + ·i3 } consuming { credibility (consumed), tribe (enabling) }`
3. **Table 3 row** (`Table-3-Manifest.md`): *"Recalling of favors owed"* → Adverse Alternative · Cost · Increase = `Adv/c +` — the coercive half; adjacent rows *"Generating future obligations…"* (`Adv/c +`) and *"The favor bank"* (varied) complete the family
4. **Vignette:** Rusty → Gerry executes it verbatim — raise the cost of Gerry's adverse alternative (refusing the favor), consuming the previously banked pledge

The binding works. Passes 3–6 held this quality bar and are now complete — `0158` is the standing exemplar and carries all seven facets in the sidecar. The procedure below is retained as the **re-run** procedure: on any corpus change or facet revision, validate 5–10 samples end-to-end before scaling, and record the samples here.

## Procedure per pass (3–6) — retained for re-runs

1. Work in tactic-ID batches of ~50 (the `tactics/<range>/` folders are natural batch boundaries).
2. For each tactic: read the markdown body; derive the facet per the schema in `_types/PLC_Tactic.md`; write to the sidecar record; set `facet_status`.
3. Pass-specific guidance:
   - **Pass 3 (`required_resources`):** derive from Choice Architecture + Effectiveness Factors prose; tag against the 9 carriers with role `enabling` (needed to act) vs `consumed` (spent by acting). 0158 exemplar: `[{type: credibility(obligation), role: consumed}]`.
   - **Pass 4:** `detectability.signature` should be the observable tell (it doubles as a probe target for the estimation loop — see `observation-model-grounding.md`); `certainty_class` per the four classes (most tactics are `probable` or `extra_conditional` — reserve `certain` for structural moves); `ethical_valence.axes` feed the ETHICAL-ACCOUNTING gate, so use its vocabulary.
   - **Pass 5:** promote Resolution Approach prose to tactic-ID links ONLY where the counter is genuinely another catalogue tactic; where the counter is a posture or non-tactical move, leave prose and no link. Wire the reciprocal (`counters ↔ countered-by`) in both sidecar records.
   - **Pass 6:** match each tactic against Table-3-Manifest rows (semantic match on mechanism, not title) and the five vignettes (Charles / Jim / Nathan / Sarah / Rusty). Sparse is honest: most tactics have no Table 3 ancestor (the corpus is 5× larger); the cross-walk's product is (a) coverage validation — every Table 3 row should have ≥ 1 corpus descendant — and (b) the citable bridge to the 25 interviews.
4. QA: sample 10% per batch; verify against the tactic body; log misses here.
5. Ship gate: `07-SHIPPING-CHECKLIST.md` Section 10 round-trip item.

## Standing rules

- Sidecar only — never edit Mode E tactic files (CONTRIBUTING zone rules).
- Bare corpus `X`/`Y` never leave the sidecar's `corpus_lever` field; all derived artifacts speak `P`/`Adv` (F9/F10).
- Facet derivations are interpretive: they are proposals under P10 — a human pass over each batch before `facet_status` flips to `complete`.
