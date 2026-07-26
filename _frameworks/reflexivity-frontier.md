---
Item_ID: plc-reflexivity-frontier
type: Fleeting
timestamp: "2026-07-02T00:00:00Z"
title: "The Reflexivity Frontier — PLC-Facing Summary"
Date_Added: 2026-07-02
Date_Modified: 2026-07-24
Needs_Processing: false
frontier: true
AI_Instructions: "FRONTIER — nothing here enters RUN-CYCLE mechanics, gates, or templates. Read for conceptual orientation and for the depth-estimation cross-reference only. Canonical source: _frameworks/lspi/Reflexivity-Layer-v0.1.md."
---

# The Reflexivity Frontier — PLC-Facing Summary

> ⚠️ **`frontier: true`.** This is the research program, not the product. The Matrix-Estimation Layer (buildable, operational — `_plc-engine/08-ESTIMATION.md`) models the target as a hidden state that signals strategically. Reflexivity removes the remaining fiction: the target is a **strategic agent** with its own type, its own beliefs about the actor, and the option to manage what the actor learns. That promotion — from one-sided estimation to a two-sided signaling game — is deliberately unbuilt. Concepts below are for orientation; none is load-bearing anywhere in the operational path.

> **Symbol reconciliation (v1.2).** This summary now speaks the governing lexicon, not the v0.1 draft's: reasoning depth is **`ℓ`** (`k → ℓ`; base `K` was reassigned to intention count), the level-indexed strategy is `str^ℓ` (`s^k → str^ℓ`; base `S` = Selection), and the gap is `margin(·)` (`G → margin(·)`). The operational layer already writes the estimate as `ℓ̂_T`. Frontier symbols `Y` (type), `f` (fact), `ck` (common-knowledge status) and `Ξ` (publicize) are unchanged. The canonical mirror `_frameworks/lspi/Reflexivity-Layer-v0.1.md` retains the superseded `k` throughout — read it through this map.

## The regress, and how it's tamed

"I read you reading me reading you…" is real. Its closure — the tower of beliefs about beliefs — is a known mathematical object (the universal type space), and it exists. But solving the game on it demands common knowledge of rationality and infinite reasoning depth — exactly what real political actors don't have. So the fixed point is the **limit, not the operating model**. The operating model is **bounded reasoning depth (level-ℓ / cognitive hierarchy)**:

- **Level-0** reads signals at face value and signals truthfully — no theory of mind.
- **Level-ℓ** best-responds to a level-(ℓ−1) opponent: level-1 reads a naive target; level-2 decodes managed signals; level-3 anticipates second-order counter-management.
- The regress truncates at a **finite, estimable integer**. Equilibrium is recovered only as ℓ → ∞.

In the theory, the best response to a level-(ℓ−1) opponent sits one level above it. That is a statement about best response given the opponent's depth is *known* — it is **not** a licence to run one above your guess. The operational rule is loss-calibrated: `operating depth = ℓ̂_T + b`, `b ∈ [0,1]` scaled by the sphere's adversarial intensity (`08-ESTIMATION.md`), because over-estimating manufactures paranoia as surely as under-estimating gets you played. Which makes the opponent's depth itself the thing to estimate.

## The game object (frontier — named here so the promotion is legible)

What "two-sided" means concretely, for orientation only — no PLC artifact instantiates any of it:

- **Players.** `{A, T}` — Actor and Target. The estimation layer's passive hidden state becomes a second player.
- **Types.** The target's type `Y_T = ⟨[t/D], ℓ_T⟩` — its private decision-matrix content *and* its reasoning depth. The actor has one too: `Y_A = ⟨intent, ℓ_A⟩`. The actor being typed is the whole promotion; in the one-sided model only the target had hidden state.
- **The target's strategy.** A signaling strategy `s_T` mapping ⟨its type, its belief about `A`⟩ → the signal it emits. The estimation layer's `m ∈ {gen, man}` branch is this in embryo, with the choice frozen; here `T` chooses it, conditioned on a model of `A`.
- **Payoffs.** `A` obtains the resource **minus all spend** — probes, resource price, and publicity. `T` gets its utility over the outcome **net of the cost of managing signals**. Those payoffs are exactly the resource-worth shifts and `margin(·)` from the actuator layer, which is why this layer had to come last: the game is unplayable without the payoff space the resource layer defines.

## Where it touches LSPI (the single joint)

**LSPI's oracle gains strategic structure under the frontier.** The σ-discretion LSPI deliberately punts to a human — which resource to pursue, which intention to press, when to abandon — is modeled here as a strategic agent's level-ℓ best-responses rather than as exogenous choice. This is the deepest opening of the oracle, and the one place the frontier touches LSPI's provable core. It is also the part most in tension with LSPI's clean computational boundary (Pillar 2): treat reflexivity as a layer that **wraps** LSPI, never one that lives inside the proven meta-theory. Nothing here changes σ-logging, the transition rules, or per-σ confluence (13.6).

## What is already delivered (the buildable extension)

Depth-as-second-estimand — the frontier's own "most tractable next move" — **is in the operational volume**: the Detection Record carries a depth estimate alongside matrix content; ESTIMATE front-loads depth-discriminating probes; the depth decoder's loss-calibrated bias is live (`08-ESTIMATION.md`). The line is exact: **depth estimation is in; the two-sided game, publicity mechanics, and common-knowledge bookkeeping are out.**

## Signaling (why the probe-design rules are what they are)

Under the misaligned interests that define political interaction, **cheap talk babbles** — a costless signal the target can fake carries no credible information. Information transmits through **costly signals**: responses expensive for a hiding target to counterfeit. And a refusal to send a separating signal — *speaking second, vagueness, delay* — is a pooling/deferral move, itself informative (a hiding type or a high-depth player). These results are the theoretical ground for `08-ESTIMATION`'s costly-signal preference; the equilibrium machinery behind them (separating vs pooling, off-path beliefs, refinement multiplicity) stays here.

## Common knowledge as a manipulable state — the third verb

Assign every fact f a status: **private / mutual-to-depth-ℓ / common**. A **publicize operation (Ξ)** shifts it:

- **Publication** (toward common): put it on the record, raise it in the public meeting, the email trail, the pre-party. Manufacturing common knowledge **forecloses the target's managed-signal option about f** and can force a response — once it is common knowledge that T blocked, T can no longer pretend it didn't. Publication *changes the game*, often collapsing a signaling contest into complete-information play.
- **Obscuration** (toward private): off-the-record moves preserve the target's signaling freedom and your uncertainty.

The deep point: **sometimes the correct move is not to estimate the hidden state but to make a fact common knowledge so the hidden state stops mattering.** Change the game instead of solving it. The operator's verb table, in full (only the first two are operational in v1.2):

| Verb | Purpose | Priced by | Status |
|------|---------|-----------|--------|
| Probe | learn the hidden state | value of information | operational (`08-ESTIMATION`) |
| Execute | move the hidden state | contextual worth | operational (gate) |
| **Publicize (Ξ)** | change the game itself | shift in common-knowledge status | **frontier** |

The catalogue's publicity-cluster tactics are, in these terms, operations on common-knowledge status rather than on the matrix (tagged `ck_operation` — see `_frameworks/lspi/observation-model-grounding.md`).

## The two corpus anchors

- **Rusty ⟶ Erik — mature reflexivity.** Rusty signals with a deniable surface ("these changes will help me learn the department") carrying a real subtext; Erik decodes it and grants it. Both at depth ≈ 2; *each knows the other knows* — and the real purpose is deliberately **held at mutual, never raised to common**, because publication would cost them both. High-depth mutual decoding plus deliberate suppression of common knowledge: no operational layer represents this yet.
- **Charles ⟶ CFO — the cautionary case.** A level-1 plot aimed at a demotion; the CFO — an unmodeled higher-depth player — read the move and ran his own game, firing the boss to demonstrate leadership before the CEO's visit. Mis-estimating the real decision-maker's depth turned their probe-and-execute into an input for *his* cycle. This is why `08-ESTIMATION` estimates depth first.

## Why the frontier stays a frontier (open problems, one line each)

1. **Depth-estimation regress** — estimating depth requires reasoning about how the target reasons; cap empirically (most actors, most of the time, are ℓ ≤ 2) and treat ℓ ≥ 3 as rare.
2. **Almost-common-knowledge discontinuity** — publication has tipping/threshold effects, not smooth ones; a fact known "almost everywhere" can be strategically worthless until it crosses into genuinely common (the electronic-mail-game result). This is the sharpest reason Ξ is not operational.
3. **Equilibrium multiplicity** — "did my probe get a real read?" inherits pooling/separating indeterminacy.
4. **Payoff inheritance** — every worth-estimation caveat compounds inside the game's payoffs.
5. **Empirical depth distributions** — what ℓ looks like in executive populations is answerable from engagement data; doubles as validation for the 4R ladder.
6. **Wrapping, not slotting** — this layer wraps the LSPI apparatus rather than extending it at a joint; it is where a result might not land.

## Positioning (the one product sentence)

The 4R sophistication ladder is a depth scale (see `4R.md`), and the All-Star's real skill is infrastructure that holds the network view: **the OV is a cognitive-hierarchy depth amplifier** — it lets a human operate at higher effective ℓ by offloading the belief-tower bookkeeping.
