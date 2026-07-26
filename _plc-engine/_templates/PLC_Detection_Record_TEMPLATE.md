---
type: PLC_Detection_Record
Item_ID: detection-<actor-slug>
title: "Detection — <Actor Name>"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Target_Actor: "[[actor-<slug>]]"   # reciprocal: set plc_Estimated_By on the Actor
plc_Owning_Actor: "[[principal-<slug>]]"   # whose read this is (Thm 13.1: per-actor keying)
plc_Estimand: both   # matrix_content | depth | both
plc_Margin_Estimate: ""   # signed direction + confidence (ordinal fine; honest-coarse > false-precise)
plc_Depth_Estimate: ""   # ℓ̂_T + credence + bias b + OPC political-intensity reading justifying b
plc_Probe_Budget_Remaining: 0
plc_Status: active   # active | stopped_acting | stopped_budget | archived
plc_Cycle_Refs: []   # reciprocal: cycle's plc_Detection_Record_Refs
AI_Instructions: "P13: every quantity in this record (credences, margin, depth, VoI) is scaffolding, not an answer — present with epistemic status attached; directional conclusions only; operator disagreement routes into the differential, never gets outranked by arithmetic."
---

# Detection — <Actor Name>

## Current
<Live hypotheses with credences — each states how the target loads keep-vs-relinquish AND carries a depth hypothesis. Current margin estimate + uncertainty note. Current depth estimate + decoder setting (b and why). Rewrite freely.>

- H1 (cr ~<X>): <hypothesis — matrix loading + depth>
- H2 (cr ~<Y>): <hypothesis>

## Probe Log
<Append-only. NEVER edit a predicted-response block after observing (anti-pattern: post-hoc prediction).>

### Probe 1 — <date> — <short name>
- **VoI rationale:** <what decision this could change; why it beats acting now; cost>
- **Depth-discriminating?** <yes: transparent bait / consistency check / costly-commitment ask | no: content probe>
- **Predicted responses (pre-registered):**
  - H1: <predicted response>
  - H2: <predicted response>
- **Managed-signal sources (v1.2+; required for any predicted branch at depth ≥ 1):** <per branch, the catalogue cluster codes and/or tactic IDs generating it — e.g. "H2 (managing, ℓ=2): C74, C09 → tactics 0221, 0398". Candidate clusters: `_frameworks/lspi/observation-model-grounding.md`. Write each cited tactic's `detectability.signature` (sidecar `INDEX-lspi.json`) into the branch, not just the ID — that signature is the tell this probe should be designed to make visible. Prefer tells costly to counterfeit. Citing a cluster is hypothesis generation, not accusation (P4 / P12); signatures are P10 proposals, not observations. Omit only if every branch is depth 0.>
- **Observed:** <response> (<date>)
- **Update:** <credence shifts; depth re-estimate; prior signals re-decoded if depth moved>
- **Worth re-pricing:** <held-resource worth estimates this probe sharpened, or "none">

## Stop Decision
<no probe's VoI > 0 / budget exhausted / operator override (logged): rationale + date>

## Cross-References
- Target actor: <link> · Owning actor: <link> · Cycles fed: <links>
