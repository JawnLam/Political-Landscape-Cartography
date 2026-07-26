---
Item_ID: plc-lspi-reflexivity-v0-1
type: Fleeting
timestamp: "2026-07-02T00:00:00Z"
title: "Reflexivity Layer v0.1 — Level-k Signaling Frontier (mirror)"
Date_Added: 2026-07-02
Date_Modified: 2026-07-02
Needs_Processing: false
frontier: true
AI_Instructions: "Mode C mirror of the LSPI Formal Foundation build folder. Do not edit here; changes originate upstream and are re-mirrored (CONTRIBUTING mirror rule)."
---

# The Reflexivity Layer — Level-k Signaling Spine (v0.1)

> ⚠️ **FRONTIER — research scaffold, not buildable.** This layer is deliberately unbuilt. It is NOT wired into any PLC session activity, gate, or template. The PLC-facing summary is `_frameworks/reflexivity-frontier.md`; the one buildable extension (depth as a second estimand) is delivered by the Matrix-Estimation machinery (`08-ESTIMATION`, `PLC_Detection_Record`).

> ⚠️ **NOTATION SUPERSEDED — see `Matrix-Estimation-Layer-v0.3-Canonical.md` (governing symbol table, §13).** Retained as the frontier reference; concepts stand, symbols are reconciled in v0.3. Depth `k→ℓ` (base `K` = intention count); strategy `s^k→str^ℓ` (base `S` = Selection); the gap `G→margin(·)`. Frontier symbols `Y` (type), `f`/`ck`/`Ξ` (common-knowledge ops) are unchanged.

*Third spec in the Matrix-Estimation series, after `Matrix-Estimation-Layer-v0.1.md` (the estimator) and `Resource-Convertibility-Layer-v0.1.md` (the actuator). This is the **frontier** piece — the one I argued we should build last, because it stands on the payoff space the resource layer defines. It is highest-variance and least-integrated by nature: a structured research scaffold, not a result. Open problems (§10) are larger than in the prior two, by design.*

---

## 0. Scope and stance

The detection layer modeled the target as a **passive hidden state** — the actor probes a matrix that does not probe back. Reflexivity removes that fiction: the target is a **strategic agent** with its own type, its own beliefs about the actor, and the option to manage what the actor learns. This promotes detection from a one-sided estimation problem (a POMDP) to a **two-sided game of incomplete information with signaling**, and it answers your own question precisely: the regress you intuited (I read you reading me…) is real, its fixed point is a known object, but the *right* solution concept is not full-equilibrium common knowledge — it is **bounded reasoning depth (level-k)**, which truncates the regress at a finite, estimable integer. Common knowledge re-enters not as the model but as a **state your tactics manufacture or destroy**.

---

## 1. The promotion — from POMDP to game

A two-player game `Ǥ`:

- **Players:** Actor `A`, Target `T`.
- **Types.** `T`'s type `Y_T = ⟨[t/D], k_T⟩` — its private decision-matrix content (how keep-vs-relinquish is loaded) *and* its reasoning depth (§3). `A` likewise has `Y_A = ⟨intent, k_A⟩`. (Note: `Y` is a fresh symbol; it does not collide with `τ`/Target.)
- **Actions.** `A`: probes `ρ` (epistemic), executions `ε` (utility-shifting, priced by `worth`), and now **publicity operations `Ξ`** (§7). `T`: signals `z` chosen *strategically* — `T`'s signaling strategy `s_T` maps `⟨its type, its belief about A⟩ → z`. (`s` denotes strategy; distinct from `Σ`/Selection.)
- **Payoffs — and why this layer had to come last.** `A`'s payoff = obtaining the resource minus all spend (probes + price + publicity); `T`'s payoff = its utility over the outcome **net of the cost of managing signals**. Those payoffs *are* the resource-worth shifts and the gap `G` from the actuator layer. The reflexivity game is unplayable without that payoff space — which is the entire reason for the build order.

The detection spec's `m ∈ {gen, man}` was this game in embryo: it is `T` choosing its signaling strategy. Reflexivity makes that choice strategic and lets `T` condition it on a model of `A`.

---

## 2. The belief hierarchy and the fixed point you intuited

The state is not `T`'s type alone but the tower: `A`'s belief about `Y_T`; `T`'s belief about `A`'s belief; `A`'s belief about that; … The closure of this tower is the **universal type space** (Mertens–Zamir) — the genuine self-referential fixed point you reached for two turns ago. It exists and is well-defined. We nonetheless do **not** solve the game on it directly, because doing so (Nash / Perfect Bayesian Equilibrium) imposes *common knowledge of rationality* and *infinite* reasoning depth — assumptions real political actors violate, and exactly the regime your work is defined against. The fixed point is the *limit*, not the operating model.

---

## 3. Level-k as the solution concept (the spine)

Truncate the tower at finite depth.

- **Level-0** — the non-strategic anchor. A level-0 actor reads signals at face value (runs the single-agent Bayesian update of the detection spec, treating every `z` as genuine). A level-0 target signals naively (emits a truthful `z`; no management). Level-0 has no theory of mind.
- **Level-k** best-responds to the belief that the opponent is **level-(k−1)**. A level-1 actor models a naive target → reads at face value but accounts for noise. A level-2 actor models a level-1 target → one that signals strategically against a naive prober → so it *decodes/discounts* managed signals. A level-3 actor models a level-2 target → one managing signals *against an actor known to decode* → so it anticipates second-order counter-management. And so on.
- **Cognitive-hierarchy variant** (Camerer–Ho–Chong): best-respond to a *distribution* over all lower levels rather than to a single level. Use this as the smoothed, more realistic form; level-k is the cleaner exposition.

This is how the regress is tamed: **a finite, estimable depth `k`**, not an infinite fixed point. Equilibrium is recovered only as `k → ∞`.

---

## 4. The sophistication ladder is a depth scale

Your 4R ladder is, approximately, a cognitive-hierarchy model — and the All-Star tier is the explicit jump into higher-order reasoning:

| Ladder tier | Behavior (from `4R.md`) | Depth |
|---|---|---|
| Little League | acts without modeling whose mind it must move | `k ≈ 0` |
| Minor League | anticipates the target's matrix, one move ahead | `k ≈ 1` |
| Major League | reverse-engineers what would move the target | `k ≈ 2` |
| All-Star | sees every actor running their own diamond; models others modeling | `k ≥ 3`, approaching the hierarchy |

The strategic edge is **operating one level above your opponent's actual depth** — not maximal depth. Reasoning much deeper than your opponent is wasted effort (they aren't there), so optimal depth is "one above theirs," which makes the **opponent's depth itself a quantity to estimate** (§5).

**The product implication, stated once.** The All-Star's real skill, per your own script, is *not* being intuitively faster — it is "building infrastructure that holds the network view." In these terms: **the OV is a cognitive-hierarchy depth amplifier.** It lets a human operate at higher effective `k` by offloading the belief-tower bookkeeping. That is the formal statement of what the product sells.

---

## 5. Meta-detection — the opponent's depth is a hidden variable

Detection now has **two estimands**, not one:

1. `[t/D]` — the matrix content (the level-0 substance: what the target wants). The original detection loop.
2. `k_T` — the target's reasoning depth (how strategically it is signaling).

These interact: you cannot correctly interpret a signal `z` without a hypothesis about `k_T`, because the same `z` means opposite things from a naive (`k_T=0`) versus a sophisticated (`k_T=2`) target. So the detection differential `H` is extended to range over **⟨matrix-hypothesis × depth-hypothesis⟩** pairs, and probes are now chosen to discriminate depth as well as content — e.g., a probe that a naive target answers straight but a sophisticated one counter-signals is a **depth-discriminating probe**. (A target who falls for a transparent bait reveals low depth; one who "speaks second" reveals high depth.) This is the abductive loop of the detection spec, with depth added to the hypothesis space — and it is what keeps the regress finite: you estimate *how deep they are*, then operate one level above, rather than spiraling.

---

## 6. The signaling sub-game — why cheap talk babbles and costly signals separate

With the misaligned interests that define political interaction, **cheap talk is uninformative** (Crawford–Sobel): a costless signal the target can fake carries no credible information — the equilibrium babbles. Information transmits only through **costly signals** (Spence) — responses expensive for a hiding target to counterfeit. Consequences for probe design (these formalize the detection spec's "costly-signal preference"):

- Prefer probes whose informative response **imposes a real cost on a target who would fake it** (a commitment, an expenditure, an irreversible concession). A signal that is cheap to fake has `μ(z|h,man) ≈ μ(z|h,gen)` and separates nothing.
- The target's **"speaking second," vagueness, and delay** are *pooling/deferral* moves — refusals to send a separating signal. Recognizing a pooling move is itself information (it signals either a hiding type or a high `k_T`).
- Separating vs pooling equilibria become the analytic vocabulary for "did the probe get a real read or a managed non-answer."

---

## 7. Common-knowledge status as a manipulable state (the third operation type)

This is where the concept you raised earns its place — as a **state variable**, not the model.

Assign every fact `f` (e.g., *"A wants resource Q," "T blocked the initiative," "T owes A a favor"*) a status `ck(f) ∈ {priv, mut, com}` (private / mutual-to-depth-k / common). A **publicity operation** `Ξ` shifts it:

```
[a.]Ξ(f) → ck(f)′
```

- **Publication** (`ck↑` toward `com`): the public-setting cluster of the catalogue — *solicit in a public meeting, put on the record, email-shaming, the pre-party*. A **public signal manufactures common knowledge** of `f`'s realization. Effect: it **forecloses the target's managed-signal option about `f`** and can **force a response** (once it is common knowledge that `T` blocked, `T` can no longer pretend it didn't). Publication *changes the game* — often collapsing a signaling sub-game into complete-information play over `f`.
- **Obscuration** (`ck↓` toward `priv`): perception-management and *off-the-record* moves — preserve the target's signaling freedom and the actor's uncertainty.

The deep point: sometimes the correct move is **not to estimate the hidden state but to make a fact common knowledge so the hidden state stops mattering.** You change the game instead of solving it. So the operator now has three verbs, not two:

| Verb | Symbol | Purpose | Priced/typed by |
|---|---|---|---|
| Probe | `ρ` | learn the hidden state | expected information gain (detection layer) |
| Execute | `ε` | move the hidden state | pivotal `worth` (resource layer) |
| **Publicize** | `Ξ` | change the game itself | shift in `ck(f)` (this layer) |

---

## 8. Worked examples — from your own corpus

**Rusty ⟶ Erik (clean level-2 signaling held below common knowledge).** Rusty repeatedly makes requests with a deniable surface ("these changes will help me *learn the department*") carrying a real subtext (squeeze Todd out). The dissertation says Erik "understood the implied intention" and granted it. Both operate at `k ≈ 2`: Rusty crafts a separating-yet-deniable signal; Erik decodes the subtext; *each knows the other knows* — yet it is **never made common knowledge.** `ck(f)` is deliberately held at `mut`, not raised to `com`, because making the real purpose public would cost both of them. This is reflexivity in its mature form: high-depth mutual decoding *plus* deliberate suppression of `ck`. Neither the detection nor the resource layer can represent this; the reflexivity layer is what it requires.

**Charles & colleagues ⟶ CFO (mis-estimated opponent depth → overshoot).** The managers ran a level-1 plot to dent Harry's credibility and aimed only for a transfer or demotion. The coda reveals the CFO "was not unknown" the plot — a **higher-level player** reading their move and running his own game (firing Harry to demonstrate his *own* good leadership before the CEO's visit). The managers mis-estimated `k_T` of the real decision-maker and got an outcome far past their target. In these terms: an unmodeled higher-`k` agent turned their probe-and-execute into an input for his own cycle. This is the cautionary case for §5 — failing to estimate opponent depth produces exactly the projection-vs-realization gap the detection spec's prime-notation flags, now with a strategic cause.

---

## 9. How it slots

- **Detection (`δ`)** gains a second estimand (`k_T`) and depth-discriminating probes (§5).
- **The catalogue** supplies two tactic families this layer needs: the signaling/obscuration moves (the `man` branch and pooling plays) and the **publicity cluster** (the `Ξ` operations). Several catalogue tactics are now revealed as *operations on `ck(f)`* rather than on the matrix.
- **The augmented gate** gains a third route: alongside "probe / acquire-a-worthful-resource," the option **"change `ck(f)`"** — sometimes you publicize rather than estimate or execute.
- **ADAPT's All-Star tier** is formalized as high `k`; **the OV** is formalized as a depth amplifier (§4).
- **LSPI's oracle.** The σ-discretion LSPI punts to now has *strategic structure*: the oracle's "choices" are a strategic agent's level-`k` best-responses. Reflexivity is the deepest opening of the oracle — and, as I flagged when you asked about durability, the part most in tension with LSPI's clean computational boundary. Treat it as a layer that *wraps* LSPI, not one that lives inside its provable core.

---

## 10. Open problems (frontier — these are larger than in the prior two specs)

1. **Depth-estimation regress.** Estimating `k_T` requires reasoning about how the target reasons — which threatens its own regress. Level-k truncates it, but *where* you truncate is a modeling choice with no clean closure. The honest first move: cap depth empirically (most actors, most of the time, are `k ≤ 2`) and treat `k ≥ 3` as rare and worth its own diagnostic.
2. **Discontinuity of common-knowledge operations.** Rubinstein's electronic-mail game and the global-games literature show that *almost*-common-knowledge behaves discontinuously from common knowledge — so `Ξ` operations have tipping/threshold effects, not smooth ones. A publication that gets `f` "almost everywhere" can be strategically worthless until it crosses into genuinely common. Modeling that threshold is hard and important.
3. **Signaling-equilibrium multiplicity.** Pooling vs separating equilibria are non-unique; which obtains depends on off-path beliefs and refinements. The practitioner-facing question ("did my probe get a real read?") inherits that indeterminacy.
4. **Payoff inheritance.** All the worth-estimation caveats from the resource layer (ordinal vs cardinal, pivotality combinatorics) flow into the game's payoffs and compound here.
5. **Empirical depth distributions.** What is the realistic distribution of `k` in executive populations? This is answerable from your own engagement data and would calibrate the cognitive-hierarchy weights — and, usefully, doubles as validation content for the sophistication ladder.
6. **Least-integrated, highest-variance.** As argued in the durability discussion: this layer *wraps* the apparatus rather than slotting cleanly into it, and it is where a result might not land. v0.1 is a scaffold to organize the research, not a claim that the result is in hand. The publishable contribution, if it exists, most likely lives in (1) or (2).

---

*Status: the three layers now stand — estimator, actuator, and (scaffolded) reflexivity. The first two are buildable today; this one is the research program. The single most tractable next move inside it is §5 — depth as a second estimand in the existing detection loop — because it extends machinery you already have rather than requiring the full game to be solved.*
