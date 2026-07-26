---
type: Type
timestamp: "2026-07-02T00:00:00Z"
Item_ID: plc-detection-record-type
title: "PLC_Detection_Record — Type Definition"
Date_Added: 2026-07-02
Date_Modified: 2026-07-24
Needs_Processing: false
type_namespace: plc
type_version: "1.2"
---

# PLC_Detection_Record

## Purpose

The reconstructable epistemic trail of estimating one target's hidden decision matrix (and signaling depth). Holds the differential (weighted hypotheses), every probe with its VoI rationale and **pre-registered** predicted responses, observations, updates, and the stop decision. This is the detection M-record: "I have a good feel for Peter" made auditable. Introduced in v1.2 per substrate authority 5 (`_plc-engine/08-ESTIMATION.md`; canonical math in `_frameworks/lspi/Matrix-Estimation-Layer-v0.4.md`).

## Cardinality and grain

One record per (sphere, target actor) under active estimation. Multiple cycles may reference the same record. Retire (Mode E archive) when the target leaves the sphere or the estimation question dissolves.

## Durability mode

**Mode D.** `## Current` (overwrite: current differential summary, margin estimate, depth estimate) + `## Probe Log` (append-only — never rewrite a predicted response after observing; that is the whole point).

## Required frontmatter fields

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must be `PLC_Detection_Record` |
| `Item_ID` | string | `detection-<actor-slug>` |
| `title` | string | `"Detection — <Actor Name>"` |
| `Date_Added` / `Date_Modified` | ISO date | |
| `Needs_Processing` | boolean | Default `false` |
| `plc_Sphere` | link | `[[<sphere-slug>-manifest]]` |
| `plc_Target_Actor` | link | `[[actor-<slug>]]` — reciprocal: Actor's `plc_Estimated_By` |
| `plc_Owning_Actor` | link | Whose read this is (usually the principal) — LSPI paths key per-actor (Thm 13.1) |
| `plc_Estimand` | enum | `matrix_content \| depth \| both` |
| `plc_Margin_Estimate` | string | Signed direction + confidence note (ordinal permitted; prefer honest-coarse over false-precise) |
| `plc_Depth_Estimate` | string | `ℓ̂_T` + credence + chosen bias `b` + the OPC political-intensity reading justifying b |
| `plc_Probe_Budget_Remaining` | integer | Mirrors the referencing cycle's budget when run inside a cycle |
| `plc_Status` | enum | `active \| stopped_acting \| stopped_budget \| archived` |
| `plc_Cycle_Refs` | list[link] | Cycles this record feeds — reciprocal: cycle's `plc_Detection_Record_Refs` |
| `AI_Instructions` | string | Default `""` |

## Required body sections

```markdown
# Detection — <Actor Name>

## Current
<Current differential: live hypotheses with credences (each hypothesis states how keep-vs-relinquish
is loaded AND carries a depth hypothesis). Current margin estimate with uncertainty note. Current
depth estimate and decoder setting. Rewrite freely; history lives below.>

## Probe Log
<Append-only. One block per probe. NEVER edit a predicted-response block after the observation lands.>

### Probe <N> — <date> — <short name>
- **VoI rationale:** <why this probe, why now, what decision it could change; cost>
- **Depth-discriminating?** <yes/no — transparent bait / consistency check / costly-commitment ask / content probe>
- **Predicted responses (pre-registered):**
  - H1 (<hypothesis>): <predicted response>
  - H2 (<hypothesis>): <predicted response>
- **Managed-signal sources (v1.2+; required for any predicted branch at depth ≥ 1):** <per branch, the
  catalogue **cluster codes and/or tactic IDs** generating it — e.g. "H2 (managing, ℓ=2): C74, C09 →
  tactics 0221, 0398". Candidate clusters: `_frameworks/lspi/observation-model-grounding.md`. Each
  cited tactic's `detectability.signature` (sidecar `INDEX-lspi.json`, populated for all 782) is the
  tell this probe should be designed to make visible — write the signature into the branch, not just
  the ID. Prefer tells that are costly to counterfeit. Citing a cluster is hypothesis generation, not
  accusation (P4 / P12); signatures are P10 proposals, not observations.>
- **Observed:** <what actually happened> (<date>)
- **Update:** <credence shifts; any depth re-estimate; if depth moved — note prior signals re-decoded>
- **Worth re-pricing:** <any held-resource worth estimates whose variance this probe changed>

## Stop Decision
<When probing stopped and why: no probe's VoI > 0 / budget exhausted / operator override (logged).>

## Cross-References
- Target actor / owning actor / cycles fed: <links>
```

## Relation slots

- `plc_Target_Actor` ↔ Actor `plc_Estimated_By` (reciprocal pair: **estimates / estimated-by** — v1.2 addition to the relation families)
- `plc_Cycle_Refs` ↔ Cycle `plc_Detection_Record_Refs`

## Anti-patterns

- **Post-hoc prediction.** Writing or editing the predicted-responses block after observing. The pre-registration IS the record's value.
- **Number worship (P13).** Quoting a credence, margin, or depth estimate from this record without its epistemic status ("working," "uncalibrated," "ordinal"). These numbers are scaffolding for judgment; they graduate toward answers only through the QUARTERLY-AUDIT calibration record — never through repetition.
- **Naked managed-signal branch (v1.2+).** Writing a depth ≥ 1 predicted response as "they'd manage the signal" without naming which clusters or tactics produce it. The branch is then unfalsifiable — and unnecessary, since every analyzed tactic now carries a written tell.
- **Entropy chasing.** Probing what you're most uncertain about instead of what would change the decision (VoI ≈ 0 probes).
- **Paranoia by default.** Setting depth bias b = 1 in a cooperative sphere — discards true information; b is loss-calibrated by OPC-measured intensity, not vibes.
- **Budget creep.** Probing past `plc_Probe_Budget_Remaining` = 0 without an operator-logged override.
- **Static photograph.** Treating the record as a stakeholder-map snapshot. It is a forward loop; if no probe is ever designed, it's an Actor file, not a Detection Record.
