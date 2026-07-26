---
Item_ID: plc-lspi-content-audit-v0-3
type: Fleeting
timestamp: "2026-07-24T00:00:00Z"
title: "Mathematical Content Audit — Matrix-Estimation Layer v0.3 (mirror)"
Date_Added: 2026-07-24
Date_Modified: 2026-07-24
Needs_Processing: false
AI_Instructions: "Mode C mirror — do not edit here; changes originate upstream and are re-mirrored (CONTRIBUTING mirror rule). This is the correction-log exemplar CONTRIBUTING.md names: findings M1-M3 and m4-n10 are what Matrix-Estimation-Layer-v0.4.md repairs. Read it before asserting any formal claim from the estimation layer; M3 in particular is the unconditional depth-bias defect."
---

# Mathematical Content Audit — Matrix-Estimation Layer v0.3

*Scope: the formal claims and the three joins in `Matrix-Estimation-Layer-v0.3-Canonical.md`. Method: each claim checked for (i) internal consistency, (ii) type/scale correctness, (iii) agreement with the spec's own worked examples. This audits the **content**, not the notation (that was v0.3). Verdict is stated up front; findings are ranked; every defect gets a fix. Blunt on purpose.*

---

## Verdict

The **architecture is sound** — the hidden-state framing, the three faces (estimate / move / account-for-defense), the loop, and the seam are coherent and the core identities are correct. But the **formal specification has three genuine inconsistencies** and several imprecisions. The most serious is the **augmented gate (§8): it is falsified by the spec's own Rusty worked example.** None of the defects sinks the framework; all are fixable in a v0.4. Do not build tooling on §8 as written.

---

## What checks out (credit where due)

- **Selection rule.** `select P ⟺ u(P) > u(X) ⟺ margin(h) < 0`, with `u(P)=[P/b]−[P/c]`. Algebraically correct and consistent throughout.
- **Update.** `cr′(h) ∝ ν_η(z|h)·cr(h)` is exact Bayesian conditioning. Correct.
- **Joint non-factorization.** `cr(m,ℓ)` does not factor because `ν` couples content and depth. Correct, and the reason depth must be co-estimated.
- **Pivotality is a well-defined object.** "Marginal contribution to crossing the margin" is the Shapley value on a monotone threshold game; that value exists for any (even non-additive) shift structure.
- **Stop-rule *form*.** "Act when acting beats probing" is the correct optimal-stopping shape (modulo Finding 2).
- **Seam *structure*.** worth as an expectation over `ℬ` correctly makes detection price the inventory.

---

## Major findings (genuine inconsistencies)

### M1 — The augmented gate is falsified by the Rusty example (§8 vs §6)

**Claim (§8):** `PASS ⟺ (R ∋ θ) ∧ (worth_t(θ) ≥ price*)`, where `worth_t(θ)` is θ's marginal (Shapley) contribution to crossing the margin and `price* = margin` (the *full* deficit to close).

**Defect — a type/scale mismatch.** `worth_t(θ)` is a **per-resource marginal** value; `price*` is the **total** margin. When a flip requires several resources (the normal case), each one's marginal worth is a *fraction* of the total, so `worth_t(θ) < price*` for every individual θ — and the gate blocks every move. This isn't hypothetical: in the spec's **own Rusty walk**, Intentions 1 and 2 explicitly have partial/zero pivotal worth (Todd doesn't move), yet the model *requires* those moves to shrink the margin so Intention 3 can flip it. The gate as written would reject Intentions 1 and 2 — the very moves §6 and §10 say must happen. **§8 contradicts §6/§10.**

**Fix.** Split the two questions the gate is conflating:
- **Sufficiency (bundle-level):** does the assembled plan's cumulative favorable shift reach `margin`? (`Σ shift ≥ margin` — the "winning bundle" test.)
- **Inclusion (per-resource):** is θ worth deploying *into the plan*? Compare θ's marginal worth to **θ's own cost**, not to `price*`. Deploy θ if `worth_t(θ | plan) ≥ cost(θ)`, even when its worth is partial.

The gate should fire on *sufficiency*; per-resource worth governs *inclusion/prioritization*. Comparing a marginal to a total is the bug.

### M2 — Probe **selection** and probe **stopping** use different currencies (§4)

**Claim (§4):** select `η* = argmax` of *expected entropy reduction of `cr`* per cost (expected information gain, EIG); stop when `E[act|ℬ] ≥ E[η*|ℬ]` (a decision-payoff comparison).

**Defect.** EIG is information-theoretic; the stop rule is decision-theoretic. They are not the same objective. A probe can resolve a matrix dimension that carries real entropy but **does not change which resource is pivotal** — EIG > 0, but **value of information (VoI) = 0**. An EIG-maximizer will run decision-irrelevant probes; a VoI-maximizer (which the stop rule implies you are) will not. The selection criterion is inconsistent with the stated objective.

**Fix.** Select probes by **VoI** — expected improvement in decision payoff (expected reduction in decision loss), the *same* currency as the stop rule. Concretely, weight uncertainty by its effect on the pivotality/worth ranking, so probes near the *selection threshold* (where `margin ≈ 0`) are valued over probes far from it. EIG becomes a valid proxy only in the special case where all matrix uncertainty is equally decision-relevant, which the worth function itself says is false.

### M3 — The "err high on depth" asymmetry is asserted, not established (§5)

**Claim (§5):** operate at `ℓ_A = ℓ_T + 1`, and when unsure bias upward, because "under-estimating depth gets you played; over-estimating just wastes reasoning."

**Defect.** Over-estimating depth is **not** merely wasted reasoning. If you model an `ℓ_T = 0` (naive, truthful) target as `ℓ_T = 2`, you decode its **genuine** signals through a "managed" likelihood — i.e., you discount true information as possible bait. That is a real epistemic cost: paranoia throws away free information and mis-reads honest counterparties (the symmetric failure to the Charles/CFO under-estimation case). The asymmetry may hold in high-stakes adversarial settings, but it is stated as a general rule and is false in low-adversarial ones.

**Fix.** Make the bias **loss-calibrated, not unconditional**: bias upward only when the payoff of being-played dominates the payoff lost to mis-decoding genuine signal — i.e., parameterize by the engagement's adversarial intensity (which OPC's political-intensity diagnostic already measures). State the two-sided loss explicitly.

---

## Moderate findings (imprecise or incomplete)

### m4 — `price* = "obtained utility transferred to the target"` is only true for inducement (§3)

The favorable shift can be produced by **inducement** (raise `u(P)` — transfer utility to the target) or **coercion** (raise `[X/c]` / lower `[X/b]` — destroy the target's alternative). Only inducement transfers utility; coercion *reduces* the target's utility while the actor still pays a resource cost. So `price*` (actor's resource cost / margin to close) **≠** obtained utility to the target in general. *Fix:* define `price*` as the *favorable shift required*, and keep "obtained utility transferred" as the special case of pure-inducement closures.

### m5 — "Compounding = cycles in the graph" needs a gain condition (§6)

A directed cycle `r → … → r` compounds only if the **product of its exchange rates exceeds 1** (a net-gain loop); a cycle with product `< 1` is depreciating. This is exactly currency arbitrage. *Fix:* **compounding resources lie on a cycle with rate-product > 1**; detect them as positive-gain cycles (negative cycles in `−log`-weights).

### m6 — Additivity tension (§6 vs §12e)

§6 describes "cumulative favorable shift crossing the margin" (additive), while open problem §12(e) admits bundle non-additivity (synergy/redundancy). *Fix:* state the additive picture as the special case; define worth via the set-function Shapley in general, and flag where additivity is assumed.

### m7 — worth is contextual but the gate treats it as scalar (§6 vs §8)

`worth_t(θ)` depends on the deployed bundle (Shapley is over a set function), yet §8 writes `worth_t(θ)` as a standalone scalar. *Fix (folds into M1):* everywhere write `worth_t(θ | plan)` and fix the reference plan.

---

## Minor findings (precision)

- **n8 — "A depth-update re-reads the past" (§5).** Exact joint Bayesian updating is order-invariant; the retroactive re-interpretation is a property of a *factored/plug-in* approximation of depth, not of the exact posterior. Operationally real (implementations will factor), but the framing overstates a dynamic the exact model doesn't have. State it as an approximation artifact.
- **n9 — "Detection sharpens worth" (§7).** "Sharpens" should mean *reduces the variance of the worth estimate* (price discovery), not *increases* worth — a probe can reveal a resource is worthless. Word it as precision, not improvement.
- **n10 — No termination argument for the estimation loop (§9).** LSPI's strong-normalization proof (§13.5) covers object transitions, not the new **re-probe** route (`HAVE ∧ ¬WORTH ∧ uncertain → probe`). That loop terminates only if VoI strictly diminishes and probes cost > 0; this needs its own well-foundedness argument. Currently unproven — a gap, not an error.
- **n11 — `ν` at `ℓ ≥ 1` is under-determined without the game (§4).** The managed-signal likelihood presupposes the target's payoffs, which are resource-worth shifts — a forward reference into the actuator/frontier. The buildable layer treats `ν` as calibrated from the catalogue; this is acknowledged in §12(a) but worth restating as the reason the buildable layer is a *model*, not a solved game.

---

## Priority for a v0.4

1. **M1 (gate).** Load-bearing and demonstrably wrong. Fix before anything is built on the gate.
2. **M2 (probe currency).** Unify selection and stopping on VoI. Changes what the estimator actually does.
3. **M3 (depth asymmetry).** Re-state as loss-calibrated; cheap to fix, prevents a coaching error (manufacturing paranoia).
4. **m4–m7** in the same pass (definitions of `price*`, compounding, additivity, contextual worth).
5. **n10 (termination)** is the one open *proof obligation* — worth a dedicated argument, since "defensible like LSPI" was a core promise and LSPI *proved* its termination.

The through-line: the framework's **prose** is more correct than its **formulas**. The concepts are right; three of the crisp formal statements over-reached (a marginal compared to a total, information mistaken for value, an asymmetry assumed). That's the normal gap between a v0.x scaffold and a defensible result — and it's exactly what this kind of audit exists to close.
