---
Item_ID: plc-lspi-resource-detection-slot-analysis
type: Fleeting
timestamp: "2026-07-24T00:00:00Z"
title: "Resource & Detection — Where They Slot in the Existing Stack (mirror)"
Date_Added: 2026-07-24
Date_Modified: 2026-07-24
Needs_Processing: false
AI_Instructions: "Mode C mirror — do not edit here; changes originate upstream and are re-mirrored (CONTRIBUTING mirror rule). The stack-placement argument: why resource-valuation and detection are one formal object, and where it attaches to the existing capability-gate. Background for 08-ESTIMATION.md; not itself operational."
---

# Resource & Detection — Where They Slot in the Existing Stack

*Read in full before drafting any formal spec. Sources consulted: `4R.md`, `4R-coaching-script.md`, `ADAPT.md`, `ADAPT-as-consulting-engine.md`, `OPC-Assessment.md`, `dissertation-substrate.md`, and the political-warfare catalogue mirror. The conclusion: the two desiderata are one formal object, and the stack already contains every input it needs except the object itself.*

---

## The one-paragraph thesis

The target's decision matrix `[A/i/t/D]` is a **hidden state**. A **resource** is anything that can apply a signed delta to a cell of that matrix (the dissertation's own Category-14 definition already says exactly this); its *worth* is therefore a function of how the specific target's matrix is loaded. **Detection** is the estimation of that hidden matrix. So resource-valuation and detection are not two problems — they are the **actuator side** and the **estimator side** of a single computation: *estimate the matrix.* The capability-gate you already run (`[a./R.] ∋/∌ θ`) answers only **"do I hold the resource?"** It cannot answer **"what is the resource worth here?"** — because worth requires the estimate that detection produces. That missing second axis is the whole of both gaps.

---

## Part 1 — Resource formalization: what exists, what's missing

**What the stack already has.** A great deal, actually:

- The **9-type taxonomy** (Category 14), with the interlocking structure made explicit in `dissertation-substrate.md` — the legitimacy↔title↔tribe triangle, the signed credibility↔blame pair, access-as-derivative-of-title, information-as-political-knowledge-not-expertise.
- The **functional definition is already latent**: Category 14 defines resources as *"the means necessary to… increasing or decreasing a benefit or a cost in the target's decision matrix."* That **is** the intensional definition.
- The **capability-gate** (`∋/∌`), `plc_Resources_Held`, `plc_Resource_Types_Required`.
- 4R's home plate, including the **compounding distinction** (which resources buy more resources).
- OPC **§5 `tactical_requirements`** already carries the "lever pattern (B(X)↑ / C(X)↓ / …)" language — so the matrix-effect framing is native to your instrument.

**What's missing (your academic itch, precisely located):**

1. **The functional definition isn't the *primary* one.** It sits buried in a category description while the nine boxes do the front-line work. The fix is not better boxes — it's **promoting the functional definition to the definition** and demoting the nine to an explicitly non-exhaustive, overlapping **basis of carriers** kept for elicitation. (Your own OPC mapping corroborates the discomfort: it flags that the engine's "§3 Resources" section was a *fabrication* — there is no resource instrument in OPC; resources are scattered across the dissertation and the gate. The construct has never had a home of its own.)
2. **No value function.** The gate is binary HAVE/HAVE-NOT. There is no representation of **resource worth = projected Δutility this resource can produce *on this target's estimated matrix*.** Worth is target-indexed and currently unmodeled.
3. **No convertibility model.** The interlocking notes (legitimacy→title, credibility↔blame) and the 4R compounding gesture imply a conversion graph, but it's never formalized — no typed transformations, no "exchange rates," no account of which conversions compound.

**Where it slots:** a **resource-valuation layer** that (a) states the intensional definition, (b) adds a **WORTH axis to the capability-gate** (so the gate asks not only "do I hold θ?" but "what is θ worth against *this* target?"), and (c) formalizes the convertibility graph that 4R's home-plate flywheel already assumes. Note that (b) **cannot be computed without detection** — which is the bridge to Part 2.

---

## Part 2 — Detection formalization: what exists, what's missing

**What the stack already has** — and it's more than you'd think, which is why it *feels* covered but isn't:

- **Detection is constituent 4** of the cycle (`δ`): the actor's *imperfect* observation of who controls the resource and the composition of the target's matrix.
- **OPC § 4 `dynamic_assessment`** — § 4.1 current situation, § 4.2 predictive factors (likely responses, cascades), and § 4.3 **`blind_spot_audit`** ("the practitioner's read is itself a model with limits").
- **OPC § 9 `monitoring_and_adaptation`** — intelligence, warning signals, counter-framework detection.
- **ADAPT's Perceive beat + the perception gap** (Actual − Perceived), the funnel-sharpness scale, and the **"starved observation node"** diagnostic.
- The dissertation's **prime (′)** notation — projected vs realized values.

**What's missing — and it's the whole ballgame.** Look at what *kind* of thing each existing piece is:

- OPC § 2 / § 4 / § 13 are **static assessment** — inventories you *fill in* (map the stakeholders, list the predictive factors, name the actor posture). They photograph the board; they don't tell you how to *reduce uncertainty* about a specific hidden cell.
- The perception gap and the prime-notation are **backward-looking error accounting** — measured *after* a move, they tell you that your read was wrong, not how to design the next read.
- § 4.3 blind-spot audit **acknowledges** uncertainty but supplies no procedure to *act against* it.

**Nowhere in the stack is there a forward, sequential, hypothesis-design loop.** That is exactly your sentence — *"if we believe Peter has X, do Y to test it, if Z then confirmed"* — and it is the one epistemic move the apparatus never operationalizes. Detection is *named* everywhere and *proceduralized* nowhere. That is the squishiness, located precisely.

---

## Part 3 — The detection protocol (the object to build)

It is differential diagnosis on a hidden decision matrix. Five parts, each mapping to a slash-addressable constituent so it inherits LSPI's audit-trail discipline:

1. **Belief state** — a *set of weighted hypotheses* over how `[A/i/t/D]` is loaded (the thing LSPI currently hands to the oracle as already-known). Notation candidate: a primed, probability-weighted hypothesis set over the matrix components.
2. **Probe selection** — choose the cheapest action whose responses best *discriminate* among live hypotheses (maximum diagnostic information per unit resource). A probe is a low-stakes `ε` whose payoff is information, not utility-shift.
3. **Observation model** — for each hypothesis, the response it *predicts* ("if Peter values the seat, a trade-offer yields hesitation, not a fast no"). This is the `if Z then H` link.
4. **Update** — revise toward the hypothesis that best explains the observed response (abductive; Bayesian if you want numbers).
5. **Stop rule** — act when expected value of acting exceeds expected value of one more probe.

**The hard, novel core (flagged honestly):** the observation model is **adversarial.** The target may be managing your perception — which is *perception management*, an entire cluster of the catalogue. So this is not inference under noise; it's inference under an agent who can feed false signal. The upside is structural: the **782-tactic catalogue is the enumerated library of obscuring moves**, so the adversarial observation model can be *grounded in known tactics* rather than hand-waved. Items 2, 4, and the catalogue interlock here.

**Where it slots:** *inside* cycle-constituent 4 (`δ`) and *under* ADAPT's **Decide** and **Perceive** beats — giving the beats a forward internal procedure where today they only name the work. It **opens LSPI's oracle**: where σ-discretion currently supplies perception-validation, this is the structured process that produces those values. OPC § 4.3 (blind-spot) and § 9 (counter-detection) become *inputs* to the loop rather than terminal checklists.

**Why it's defensible "like LSPI":** LSPI's defensibility was the **audit trail** (the M-record — every step logged, reconstructable). Give detection its *own* M-record: the hypothesis lattice, the probe chosen and why, the predicted responses, the observed response, the update. "I have a good feel for Peter" becomes a reconstructable epistemic trail — the squishiest part of the practice acquires the cleanest paper trail.

---

## Part 4 — The defensibility capstone (for the academic)

The detection loop **is your dissertation's own method, turned outward.** Chapter 5's epistemology is explicitly abductive grounded theory: *"account for surprises, anomalies, puzzles… imagine all possible theoretical accounts… form and check hypotheses until arriving at the most plausible interpretation."* You ran that loop on **transcripts**. The consultant runs the identical loop on a **live target.** The method becomes the model — so the detection protocol inherits the epistemic warrant you already justified in the dissertation. ADAPT's perception-gap is the half-built residue of this loop (the error term); what's missing is the *forward* design of discriminating probes.

---

## Recommendation

Build them as **one object — a Matrix-Estimation Layer** — not two:

- **Estimator side (Detection):** the five-part adversarial-abductive loop above, slotted into `δ` / ADAPT-Decide-Perceive, with its own audit trail and the catalogue as its observation-model library.
- **Actuator side (Resources):** the intensional definition promoted to primary; the nine demoted to carriers; the capability-gate given a WORTH axis; the convertibility graph formalized.
- **The seam:** resource-worth = projected Δutility on the *estimated* matrix — so the estimator literally prices the actuators. One computation, two faces.

This extends the stack at its existing joints (the `δ` constituent, the capability-gate, the ADAPT beats) rather than competing with it. It is the half of your practice you've never been able to charge for with a straight face — and it's the better spin-off than slash-addressing, because slash-addressing formalized the *bookkeeping* of a maneuver, and this formalizes the *judgment* that the bookkeeping was always waiting on.
