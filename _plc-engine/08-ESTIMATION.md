---
Item_ID: plc-engine-08-estimation
type: Fleeting
timestamp: "2026-07-02T00:00:00Z"
title: "08 — Estimation: The Matrix-Estimation Layer, Operationalized"
Date_Added: 2026-07-02
Date_Modified: 2026-07-02
Needs_Processing: false
AI_Instructions: "Load for ESTIMATE sessions, augmented-gate work inside RUN-CYCLE, and any resource-worth or convertibility question. The canonical math is _frameworks/lspi/Matrix-Estimation-Layer-v0.4.md — cite it, don't restate it. This chapter is the operational surface."
---

# 08 — ESTIMATION

> **Operationalizes the Matrix-Estimation Layer (v0.4) — substrate authority 5's buildable core. This is the judgment layer PLC always gestured at: detection was named everywhere and proceduralized nowhere. Now it has a procedure, an audit trail, and a gate. The AI administers; the operator judges (Pillar 2).**

## The object, in one paragraph

The target's decision matrix is a **hidden state**. You never see how a target loads keep-vs-relinquish; you estimate it. Three faces of one object: **estimate it** (detection), **move it** (resources), **account for its being defended** (depth). The target selects your preferred position P exactly when its margin — utility of keeping minus utility of relinquishing — goes below zero. Everything in this chapter is about estimating that margin, pricing what you hold against it, and gating plans on whether they close it.

## Three quantities — never conflate them

1. **Required shift** — the deficit a plan must close (the margin). A gap, not a payment.
2. **Actor's cost** — the resources you spend producing the shift.
3. **Target's obtained utility** — what the target *gains*. Equal to the shift **only for pure inducement** (raising the value of relinquishing). Coercive shift (raising the cost / lowering the benefit of keeping) reduces the target's utility on its alternative while you still pay cost.

An inducement plan and a coercion plan can close the same margin at the same cost and leave the target in very different states — which the ETHICAL-ACCOUNTING gate cares about. Keep the three quantities separate in cycle prose.

## The detection loop (forward, sequential, adversarial)

This is differential diagnosis on a hidden decision matrix. Five parts, run inside an ESTIMATE session against one target, logged in a `PLC_Detection_Record`:

1. **Differential** — a set of weighted hypotheses about how the target's matrix is loaded (each hypothesis also carries a depth hypothesis — see the decoder below). Seed from SCAN findings, UNCOVER outputs, OPC § 4 dynamic assessment, and Actor files.
2. **Probe selection by VoI** — a probe is a low-stakes action whose payoff is decision-relevant information. Choose the probe whose expected improvement to your eventual decision most exceeds its cost — **value of information, not curiosity**. VoI concentrates near the selection boundary (margin ≈ 0): resolving a cell that doesn't change which plan is optimal is worthless even if you're very uncertain about it. **Flag (e) — this VoI is one-step (myopic).** It scores each probe as if it were the last one you will run. It therefore cannot see a probe whose value only appears *after* a later probe — the cheap consistency check that is worthless alone but makes the next costly-commitment ask readable. Full sequential VoI is a deferred POMDP-planning problem. The probe budget is what guards the myopia: it bounds how far a locally-greedy rule can wander. Say so in the record when a probe is rejected on VoI alone, and consider naming the pair you think it belongs to.
3. **Predicted responses — written BEFORE the probe.** For each live hypothesis, what response does it predict? ("If Peter values the seat, a trade-offer yields hesitation, not a fast no.") This is the epistemic commitment that makes the update honest.
4. **Update** — after observing, revise credences toward the hypotheses that best explain the response (abductive; Bayesian if you want numbers).
5. **Stop rule — same currency as selection.** Act when no affordable probe's expected decision-improvement covers its cost. Probing and stopping are priced in the same units (decision payoff); "one more probe to be sure" without a VoI rationale is a budget leak. **Flag (e) again, and it bites harder here:** a myopic rule stops the moment no *single* probe pays for itself, which is exactly when a two-probe sequence might have. Before recording a Stop Decision, ask once whether the remaining candidates are genuinely worthless or only worthless *one at a time* — and log the answer. A stop rule that has never been asked that question is a myopic stop, not a resolved one.

**Probe budget (termination by construction).** Each cycle using the loop sets `plc_Probe_Budget_Remaining` — a hard per-cycle cap. v0.4 §12 **argues** the loop terminates under it, by a well-founded lexicographic measure plus a bounded budget. Say what that argument is: **a sketch at the rigor of LSPI's own §13.5 measure arguments, not a machine-checked proof** — the spec labels it so itself. It sits a paragraph away from LSPI's six meta-theorems (uniqueness, subject reduction, congruence decidability, resource conservation, strong normalization, per-σ confluence) and is *not* one of them; those are proved to a different standard, and proximity is not membership. Claim the budget bounds the loop; never claim the termination is proven at meta-theorem grade. The VoI stop-rule means the budget rarely binds; its presence is what makes "we'll just keep probing" structurally impossible. Decrement on every probe; reset per cycle.

**Setting `N_probe` — the rule the budget rests on.** The bound is **decision-value headroom divided by the cheapest probe you can actually run**:

```
N_probe  ≤  ⌈ ( V* − V(ℬ₀) ) / cost_min ⌉
```

In words: *how many probes could still pay for themselves before the best attainable decision-value is exhausted.* `V*` is the decision value under perfect information — finite, and bounded above by the interest's value to the actor, so affordability caps it. `V(ℬ₀)` is the value of deciding on today's beliefs. `cost_min` is a floor on probe cost — the cheapest probe available to you in this sphere, not a theoretical minimum. Since every probe the loop takes must clear its own cost, only so many can fit inside the headroom. Two consequences worth stating: a target you already read well (small `V* − V(ℬ₀)`) earns few probes no matter how curious you are, and a sphere where every probe is expensive (large `cost_min`) earns fewer still.

In practice the bound is loose. What goes into `plc_Probe_Budget_Remaining` is **a small integer chosen at cycle open, decremented per probe, reset per cycle, and raised only by explicit operator election — which is itself logged**, with what changed to justify the raise (new headroom, a cheaper probe channel). Record which way the number was set, in the Detection Record's Stop Decision block:

- Derived from the bound (headroom and `cost_min` both named, even ordinally) → **termination by construction**.
- Picked because it felt about right → **termination by fiat.** Still bounded, still better than no cap, but say so plainly where a later reader can see it. The worked example's opening 4 is a fiat number; it is not a default, a base rate, or a recommendation (F4b).

**The adversary lives in the observation model.** At depth 0 the target's signals are genuine noise-around-truth. At depth ≥ 1 they are *strategic* — and the branches of "what a managing target would show you" are not hand-waved: they are enumerated by the catalogue's perception-management clusters (see `_frameworks/lspi/observation-model-grounding.md`). Prefer **costly signals** — responses expensive for a hiding target to counterfeit (a commitment, an expenditure, an irreversible concession). A signal that is cheap to fake separates nothing; under misaligned interests, cheap talk babbles. A refusal to send a separating signal — speaking second, vagueness, delay — is itself information (a hiding type or a high-depth player). *Probe leakage* (your probe teaching the target what you're estimating) is a frontier concern — flag it, don't model it.

## The depth decoder

Depth is the decoder ring: how strategically is this target signaling?

1. **Estimate depth FIRST.** Front-load a depth-discriminating probe — transparent bait (a naive target takes it; a sophisticated one counter-signals), a consistency check, a costly-commitment ask. Read all subsequent content through the resulting decoder.
2. **A depth-update re-decodes prior signals.** When the depth estimate moves, walk back through the Detection Record's observed responses and re-read them under the new decoder. (Formally this is a factored-approximation artifact, not a property of exact joint updating — but every real implementation factors, so operationally: re-read the past.)
3. **Choose your operating depth by two-sided loss — never unconditional "assume manipulation."** Operating depth = estimated target depth + a bias `b` between 0 and 1, scaled by the sphere's **adversarial intensity as the OPC political-intensity diagnostic measures it**: b → 1 in adversarial spheres, b → 0 in cooperative ones. Both errors are real: *under*-estimating depth gets you played (you decode managed signals as genuine — the Charles/CFO case: a plot read by a higher-depth player who turned it into an input for his own cycle); *over*-estimating manufactures **paranoia** — you decode genuine signals as bait and throw away true information, mis-reading honest counterparties. Coaching an operator toward unconditional suspicion is a defect, not prudence. **Flag (f) at `b`:** the two-sided loss weights this bias is supposed to minimize (`L_under` / `L_over`) are uncalibrated — no engagement data has fixed them — so `b` is an argued posture, not a computed optimum. Set it ordinally (low / medium / high adversarial intensity), name the OPC political-intensity reading it came from, and record it as a *choice* the operator can contest. P13 is the only backstop here, and P13 is a blanket: it puts an uncalibrated bias parameter in the same register as a well-understood credence. Do not let the two blur — an operator who knows `b` is a posture will argue with it, which is the point.

## The actuator — what a resource is, and what it's worth here

**The definition (primary, intensional):** a political resource is a **costly, target-conditional capacity to apply a signed delta to a cell of a target's decision matrix.** The dissertation's nine types — money, hard assets, credibility, attributes, legitimacy, information, access, title, tribe — are a **non-exhaustive basis of carriers**, kept for elicitation ("walk the nine boxes and ask what the principal holds"), not the definition.

- **Effect signature:** per resource, the signed target-conditional deltas it can apply over {P/b, P/c, Adv/b, Adv/c} and at what cost. Record on the Actor/Principal file.
- **Combined shift is a set function.** Resources interact — synergy and redundancy. Additivity ("the plan's shift is the sum of the members' shifts") is the flagged first-order default, not a law — **flag (g)/(m6)**, and its flag point is the gate's sufficiency judgment, where the sum actually gets used.
- **Worth is contextual pivotality.** A resource's worth is its **marginal contribution to closing the margin given the rest of the plan** — not a scalar property of the resource. A resource with a large nominal shift can be worthless-in-context (redundant given the plan) or partially worth (shrinks the margin without closing it, cheapening the pivotal member). This is the formal content of *"I applied real leverage and nothing happened."* (Exact pivotality is combinatorial — use greedy approximation; flag it.)
- **Run ordinal when magnitudes aren't honest.** If the operator can rank but not quantify, keep the whole loop ordinal; false precision is worse than coarse honesty.

**Convertibility.** Resources convert through cycles: banked favor ⇝ job offer; information + attributes ⇝ authorization. Record edges on Actor/Principal files with edge type (transfer / transform / earn-sanction / non-transferable) and a rough sphere-indexed rate. Two consequences:

- **Compounding = gain-cycles.** A resource compounds **iff it lies on a directed conversion loop whose rate-product exceeds 1** — a net-gain (arbitrage) loop. A bare loop with product ≤ 1 is depreciating, not compounding. This is 4R's flywheel, formalized — and P6's recursive-resource-control thesis given a test: mastery is *holding positions on gain-cycles*.
- **Protection = spending durable low-yield resources to defend fragile high-yield ones.** Durability is a node property; record it.

Exchange rates are themselves estimates (estimation all the way down) — treat convertibility claims with the same hygiene as matrix hypotheses.

**The seam: detection is price discovery.** Worth is an expectation over your beliefs about the margin — so every probe **reduces the variance of the worth estimate**. Sharpening can reveal a held resource is worthless here; that is the probe working, not failing. You cannot price the pivot without an estimate of the margin: the estimator literally prices the actuator.

## The augmented gate (inside RUN-CYCLE, constituent 9)

The binary capability check (`∋`/`∌` — "do I hold it?") is retained. Layered above it, over the intended **plan Π** (the set of deployments):

| Test | Question | Level |
|------|----------|-------|
| **Sufficiency** | Is the plan expected to close the margin (with a risk allowance for belief variance)? | plan |
| ⤷ *flags on this row* | **(f)** the risk allowance is uncalibrated; **(m6)** the plan's shift is assumed additive across members | plan |
| **Inclusion** | Does every member's marginal contribution, given the rest of the plan, exceed **its own cost**? | member |
| **Affordability** | Is the total plan cost ≤ the interest's value to the actor? Never pay more than the prize. | plan |

**Two flags fire inside the sufficiency judgment — name them in the gate block, every time.**

- **(f) The risk allowance is uncalibrated.** "Expected to close the margin, with a cushion for how wrong the belief might be" is the right shape; the size of that cushion has no empirical grounding — no engagement data has fixed it, and neither has anything else. It is the operator's stated conservatism wearing a formal coat. Write the allowance as what it is (*"margin read is ordinal and near-boundary; I am requiring visible headroom, not a hair's breadth"*), never as a number the gate computed. P13 governs it, but P13 is a blanket that makes an uncalibrated risk term read exactly like a well-understood credence — so flag it here, specifically, rather than leaning on the blanket.
- **(m6) Additivity is the default, not the law.** Summing member shifts to test sufficiency assumes the resources don't interact. They often do: two levers aimed at the same consideration are partly redundant (the sum overstates), a lever that only works once another has landed is a complement (the sum understates). Before recording PASS, ask once whether any two members overlap or depend on each other, and record the answer. If they interact, the plan's shift is not the sum, and a sufficiency verdict computed as a sum is a flagged approximation — say so in the gate block. Redundancy also reappears one row down, as an inclusion failure.

**GATE PASS ⟺ an affordable, sufficient plan exists within held resources, every member clearing inclusion.**

Never compare one member's worth to the *total* margin — that scale error rejects every multi-resource plan and is the exact defect the v0.4 audit fixed (M1). The canonical test: a three-resource plan where no single resource suffices but the set closes the margin **passes** (the Rusty pattern — new-procedures + reorg + job-offer flipping Todd).

**Routes on failure (the control flow):**

| Situation | Route |
|-----------|-------|
| A sufficient plan needs a resource not held | **Acquire** — nested sub-cycle (classic `∌` spawn), traversing convertibility edges |
| Held resources collectively sufficient though no single one suffices | **PASS** |
| No affordable sufficient plan even with acquisition | **Abandon** (`R-abandon`; cycle status → `abandoned`), or **rescope** the objective (shrink the interest) |
| Sufficiency uncertain because the margin is uncertain | **Re-probe** — route back to the detection loop, probe chosen by VoI, budget permitting |

*(Frontier, not part of the v1.2 gate: a third eventual verb exists — publicize, changing what is common knowledge so the hidden state stops mattering. See `_frameworks/reflexivity-frontier.md`. Flagged only.)*

The two PLC ethical gates (ALTERNATIVES-AUDIT § 15, ETHICAL-ACCOUNTING § 11) are unchanged and still sit between gate-pass and execution (P7 suggestion-gating).

## The integrated loop

```
detection (+depth) ──sharpens──► belief ──prices──► worth(r | plan) ──► GATE (sufficiency+inclusion+affordability) ──► execute plan
     ▲  ▲                                                                    │   │
     │  └──── sufficiency uncertain: re-probe (by VoI, within budget) ───────┘   │
     └──────────── plan needs an unheld resource: acquire via conversion ────────┘
```

Every pass logs to the Detection Record and the cycle's Operation Record: the differential, the probe and its VoI rationale, predicted vs observed, the update, the plan, the gate decision. **"I have a good feel for Peter" becomes a reconstructable epistemic trail** — the squishiest part of the practice acquires the cleanest paper trail.

## Why this is defensible (the capstone)

The detection loop is the dissertation's own method, turned outward. Chapter 5's epistemology is explicitly abductive grounded theory — account for surprises, imagine the possible accounts, form and check hypotheses until the most plausible interpretation stands. The dissertation ran that loop on transcripts; the operator runs the identical loop on a live sphere. The method becomes the model, and the protocol inherits the epistemic warrant the dissertation already justified. ADAPT's perception gap was always the *backward-looking error term* of this loop; the forward design of discriminating probes is what was missing.

## Calibration flags (open problems — flag inline wherever used; governed by P13)

**P13 — Numbers are scaffolding, not answers (`02-PRINCIPLES.md`) governs every quantity this chapter introduces.** Until a QUARTERLY-AUDIT calibration record exists for a quantity in this sphere, the AI presents it with epistemic status attached ("working credence," "uncalibrated margin read," "ordinal ranking"), draws directional conclusions only (rankings and threshold-crossings, never magnitudes), and treats operator disagreement with an estimate as data for the differential — never as something the arithmetic outranks. Presenting an uncalibrated number as a finding is the quantitative twin of F2.

Every flag has a **flag point** — the place in the loop where it must be named out loud. A flag that lives only in this list is not flagged.

| Flag | What's uncalibrated or approximate | Flag point (say it here, every time) |
|---|---|---|
| **(a)** | managed-signal likelihoods across depth levels — grounded from catalogue tactics, not solved game theory | when a signal is decoded as managed rather than genuine |
| **(b)** | pivotal worth uses greedy approximation (exact pivotality is combinatorial) | the gate's **inclusion** test, per member |
| **(c)** | magnitudes are often not honest — run ordinal | wherever a magnitude would otherwise be written |
| **(d)** | conversion rates are estimated (estimation all the way down) | any acquire route traversing a convertibility edge |
| **(e)** | **VoI is one-step (myopic)** — cannot see a probe whose value only appears after a later probe; the probe budget is what guards it | **probe selection** (detection loop step 2) and the **stop rule** (step 5) — both, not one |
| **(f)** | **the sufficiency risk allowance and the depth-loss weights (`L_under`/`L_over`, hence `b`) are uncalibrated** — no engagement data has fixed them | the gate's **sufficiency** judgment (the risk allowance) and the **depth decoder** where `b` is set |
| **(g)** | **additivity of member shifts (m6)** — the first-order default, not a law; resources interact through synergy and redundancy | the gate's **sufficiency** judgment, before recording PASS |

None of these is hidden machinery: where a judgment leans on one, say so in the record — at the flag point, in the sentence that makes the judgment, not in a footnote. P13 governs all of them, but P13 is a blanket. A blanket makes an uncalibrated risk allowance indistinguishable from a well-understood credence, which is precisely the confusion these per-flag callouts exist to prevent.
