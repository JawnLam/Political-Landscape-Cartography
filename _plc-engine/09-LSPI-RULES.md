---
Item_ID: plc-engine-09-lspi-rules
type: Fleeting
timestamp: "2026-07-24T00:00:00Z"
title: "PLC Engine 09 — The LSPI Rule Catalogue and State Machine"
Date_Added: 2026-07-24
Date_Modified: 2026-07-24
Needs_Processing: false
AI_Instructions: "The single maintained copy of LSPI's 21 transition rules and the per-state admissibility table. Read the admissibility table before naming admissible next steps to an operator (03-SESSION-PROTOCOL § State-by-state discipline requires it). Never restate a rule's premises in another chapter — cite this one. LSPI is descriptive: you administer and record, the operator drives (Pillar 2, F11)."
---

# 09 — The LSPI Rule Catalogue and State Machine

> **The formal spine underneath the 14-constituent cycle walk. 21 transition rules in three families, two non-firing disciplines, the derived views their premises read, and the table that says which rules are admissible from which state.**

Substrate authority 5. Upstream source: `_frameworks/lspi/LSPI-Foundations.md` §11 (navigate by section — never read whole; it is ~780 KB). Orientation: `_frameworks/lspi/_lspi-README.md`.

---

## What this chapter is for

`03-SESSION-PROTOCOL.md` instructs the AI, at every state of a cycle, to **name the admissible next steps and ask one question**. Until v1.2 there was nothing to name them from: the rules were listed once, in a paragraph, unattached to any state. This chapter is that lookup.

It is a **reference for administration, not an interpreter**. LSPI is an oracle-parameterized state-transition system: three of its guards are irreducibly interpretive and are resolved by the operator, not by the engine (Pillar 2). Naming which rules *could* fire is bookkeeping and is yours to do. Deciding which one *does* is the operator's. Never write that the system "will determine," "computes," or "predicts" an outcome — that is F11.

**What this chapter does not do.** It does not restate the grammar or the type system (`04-SCHEMA.md` § System 1), does not carry the augmented gate's economics (`08-ESTIMATION.md`), and does not narrate the cycle (`03-SESSION-PROTOCOL.md`). It also does not reproduce the upstream proofs — it records which practice each theorem licenses and where the practice lives.

---

## 1. The configuration ⟨C; M; S; R⟩

Every rule reads and writes one state object. In PLC it is distributed across artifacts you already keep — see `_types/PLC_Cycle.md` § LSPI Configuration for the field-level mapping.

| Slot | What it is | Where it lives in PLC | Notes |
|---|---|---|---|
| **C** | active-cycle pointer | the currently-open Cycle file | Advances on `R-open` / `R-spawn`, **decreases** on `R-resume`. **Not monotonic** — never treat C as a cycle ID. Cycle *identity* is carried structurally by the `⟨open, C⟩` markers in M. |
| **M** | operation record | the Cycle file's `## Operation Record` | Append-only. Entries are tagged with the cycle-identity they semantically record, not with whatever C happens to be active. |
| **S** | suspended-parent stack | `plc_Suspended_Parent` / `plc_Spawned_Subcycles` chain | LIFO. Entries are `⟨parent-C, parent-pending-q, parent-prefix⟩`. Pushed by `R-spawn`, popped by `R-resume`. `R-close-nested` does **not** touch S. |
| **R** | the actor's resource multiset | the Principal's `## Current Resource Holdings` | A multiset, not a set — quantities matter (two banked favors ≠ one). Read at the gate; decremented by `R-execute`; incremented by `R-flowback` and `R-close-nested`. |

**Δ is not a slot.** The decision matrix is a *derived view* — a fold over M. Reconstruct it by replaying the record; never store it as mutable state (Persistence Invariant, `06-STATE-PERSISTENCE.md`).

**Structural markers** are audit-trail meta-entries written into M alongside declarations. The closed vocabulary is in `_types/PLC_Cycle.md` § Structural-marker vocabulary. **Markers are not LSPI terms.** Do not run them down the five-layer validation ladder; they have no Layer-2 sort, and rejecting one as ill-typed is itself an F10 error. Their payloads are typed by the rule that wrote them.

---

## 2. The derived views a rule's premises read

These are folds over M. They are not stored; they are computed on demand. An AI that cannot compute these cannot check a premise.

| View | Definition | Used by |
|---|---|---|
| `last(M-cycle-C)` | most recent entry in M tagged with cycle-identity C | most cycle-shared rules |
| `IntentionPosition(g_k)` | the LifecyclePosition encoded by the most recent *position-bearing* entry **about** `g_k` — `undeclared` if none | every per-intention rule |
| `PendingTheta` | `{ g_k : IntentionPosition(g_k) ∈ {declared, θ-written} }` | `R-required-resources` |
| `DeclaredIntentions` / `MootedIntentions` / `LiveIntentions` | folds over M; `Live = Declared \ Mooted` | `R-intention`, `R-moot-intention`, `R-select` |
| `CyclePattern` | `per-intention` if any *declared* `γ_k`'s projected comparison body references an ordinally-indexed matrix position; `cycle` otherwise | selects the perceive variant |
| `q_of(g_k)` | `g_k`'s bound resource set, read from its θ-declarations | `R-gate`, `R-execute` |
| `cost(·)` / `earnings(·)` | the declared resource designations a step spends / obtains | `R-execute` / `R-flowback` |
| *per-intention phase active* | ω-body written **and** no `⟨select-staged, σ⟩` **and** no `⟨close⟩`/`⟨moot⟩`/`⟨abandon⟩` for this cycle | the phase gate on `R-intention`, `R-required-resources` |

**"About `g_k`" requires shape *and* role.** A path may carry `g_k` as provenance (a sub-cycle's parent-prefix) without being a position-bearing entry about it. Objective, interest and detection bodies never move an intention's position, even when `g_k` appears in their paths.

**The nine LifecyclePosition values:** `undeclared` · `declared` · `θ-written` · `gate-passed q` · `gate-failed q` · `resumed q` · `executed` · `perceived` · `mooted`.

**Operative-`last` convention.** Every `last(M-cycle-C)` read transparently **skips** intention-scoped `⟨moot, C, g_k⟩` markers — mooting one intention must not stall the cycle's shared reads. Cycle-scoped `⟨moot, C⟩` and `⟨abandon, C⟩` are **not** skipped; they are terminal.

---

## 3. The rule catalogue

**Twenty-one transition rules — 14 lifecycle + 6 failure + 1 non-destructive — plus two non-firing disciplines.** Named variants (`R-gate-pass`/`R-gate-fail`, `R-perceive-cycle`, `R-perceive-failure-cycle`, `R-moot-intention`) are sub-rules and do not change the count of 21.

The **Fork** column says who decides when more than one rule is admissible: **σ** = a strategic sequencing choice by the operator (Pillar 4; log to the σ column of the cycle's σ / Guard Log); **guard** = an interpretive reading of the world (Pillar 2; log to the guard column); **—** = structurally determined, no choice.

### 3.1 Lifecycle family (14)

| Rule | Trigger | Premises / guards | Writes | C·S·R effect | Fork |
|---|---|---|---|---|---|
| `R-open` | `M = ∅ ∧ C = 0`, or `last(M) = ⟨flowback-recorded⟩ ∧ S = []` | — | `⟨open, C+1⟩` | C+1 | — |
| `R-interest` | `last = ⟨open, C⟩` | top-level (`S = []`) declares a fresh interest; sub-cycle (`S ≠ []`) declares **the parent's pending q, literally** | ι-body | — | — |
| `R-detect` | `last = ι-body` | ordinal freshness for each new alternative and position | δ-body (target, preferred position, adverse alternatives) | — | — |
| `R-objective` | `last = δ-body` | exactly one ω per cycle | ω-body — **this write opens the per-intention phase** | — | — |
| `R-intention` | per-intention phase active | `IntentionPosition(g_k) = undeclared`; `\|Declared\| < K_C` (WF-1) | γ-body (projected comparison) | — | **σ** — a standing option throughout the phase |
| `R-required-resources` | per-intention phase active | `PendingTheta ≠ ∅`; `g_k` = earliest-declared pending | θ-body | — | **σ** — the standing option |
| `R-gate-pass` | `IntentionPosition(g_k) ∈ {θ-written, resumed q}` | possession: `R ∋ q` | `⟨gate-pass, q⟩` | **R unchanged — the gate is a test, not a deduction** | **guard** (possession) |
| `R-execute` | `IntentionPosition(g_k) = gate-passed q` | — | ε-body | `R ⊖ cost(q)` | — |
| `R-perceive` | `CyclePattern = per-intention`; position `executed` | the realized comparison **validates** the projection | Γ-body + `⟨perceive, g_k⟩` | — | **guard** (perception validation) |
| `R-perceive-cycle` | `CyclePattern = cycle`; **all** live intentions `executed` | validates | Γ-body + `⟨perceive, C⟩` — **no per-intention marker**, so every live `g_k` stays at `executed` | — | **guard** |
| `R-select` | per-intention phase active | four conjuncts read atomically: every live `g_k` terminal; if any is `executed` then a cycle-level `⟨perceive, C⟩` exists; the σ-clause is well-typed | `⟨select-staged, σ⟩` — **ends the per-intention phase** | — | **σ** (which selection) |
| `R-outcome` | `last = ⟨select-staged, σ⟩` | — | Ω-body (**unprefixed** — Ω is systemic) | — | — |
| `R-obtained-utility` | `last = Ω-body` | — | Λ-body (target-prefixed) | R untouched — utility is the target's, not a held resource | — |
| `R-close` | `last = Λ-body` | — | `⟨close, C⟩` | — | — |
| `R-flowback` | `last = ⟨close, C⟩` | — | Φ-body + `⟨flowback-recorded, E⟩` | `R ⊎ E` | — |

*Terminal position set for `R-select`'s universal premise: `perceived` · `executed`-under-a-cycle-level-perceive · `mooted`.*

### 3.2 Failure family (6)

| Rule | Trigger | Premises / guards | Writes | C·S·R effect | Fork |
|---|---|---|---|---|---|
| `R-gate-fail` → `R-spawn` | gate-eligible position | possession fails: `R ∌ q` | `⟨gate-fail, q⟩` (parent-tagged) **+** `⟨open, C+1⟩` (sub-cycle-tagged), atomically | push `⟨parent-C, q, parent-prefix⟩` onto S; C+1; **parent R unchanged** | **guard** (possession); **σ** for spawn order when several q are missing |
| `R-close-nested` | sub-cycle `last = Λ-body`; `S ≠ []` | — | `⟨close-nested, sub-C, parent-C⟩` + nested Φ + `⟨flowback-recorded, E⟩` | `R ⊎ E` — **this rule is the escalation's resource writer** | — |
| `R-resume` | sub-cycle `last = ⟨flowback-recorded⟩`; `S ≠ []` | **safety check: `R ∋ parent-pending-q`** — the resource that failed must actually be held now | `⟨resume, parent-C, q⟩` | pop S; C ← parent-C; **R unchanged** | — |
| `R-perceive-failure` | position `executed` (per-intention pattern) | the realized comparison does **not** validate | Γ-body + `⟨perceive-failure, g_k⟩` | — | **guard** |
| `R-perceive-failure-cycle` | all live intentions `executed` (cycle pattern) | does not validate | Γ-body + `⟨perceive-failure, C⟩` — no per-intention marker | — | **guard** |
| `R-moot` | `last = ⟨perceive-failure, C⟩`, or an operator-attested void premise | the premise the cycle rested on stopped holding | `⟨moot, C⟩` | **R unchanged — a mooted cycle gained nothing** | **σ** (one of three continuations after perceive-failure) |
| `R-moot-intention` | operator-attested void premise for one `g_k` | `g_k ∈ Declared`, `g_k ∉ Mooted`, **`Live \ {g_k} ≠ ∅`** | `⟨moot, C, g_k⟩` | — | **σ** — structurally cannot fire at K = 1 |
| `R-abandon` | **any state from which the principal elects not to continue** | none beyond the election | `⟨abandon, C⟩` | if nested, pop **exactly one** S entry and return to the immediate parent; if top-level, no pop | **σ** |

> **Do not narrow `R-abandon`.** Its "any state" premise is what makes the failure family total — every cycle flows back, moots, or is abandoned — and it is the escape hatch the termination result rests on. Restricting it to a subset of states silently breaks Theorem 13.5. (`R-abandon` is also the one rule no dissertation worked case exercises; it is a coverage rule.)

### 3.3 Non-destructive family (1) and non-firing disciplines (2)

| Rule / discipline | Nature | Scope and rule |
|---|---|---|
| `R-objective-revise` | the single non-destructive **transition** | Requires the original interest in M, an operator-attested detection update, and the same argument path. Writes `⟨objective-revised, C, ι, old ↦ new⟩` **and** the revised body; the superseded body is retained. **Scoped to interest-body revision only** — it does not cover intention addition, cross-cycle revision, or revision of ω/γ bodies. |
| `R-unfold` | non-firing discipline | Directional name→body substitution. One-way: the naming entry persists, and any later reference cites the record entry that established the binding. **Never fold a body back into its name** — that would erase the unfolding step from the record. Not a transition; it has no firing site. |
| `R-prime-preserve` | non-firing discipline | An invariant clause on the three rules that move C (`R-spawn`, `R-resume`, `R-abandon`): the projected/realized status of every designation in M survives the transition. Projections are never overwritten by realizations; both persist. This is what makes forecast calibration possible at QUARTERLY-AUDIT. |

---

## 4. The admissibility table

**Read the admissible set off this table before naming next steps to an operator. Never improvise the list.**

| Current state | Admissible rules | Fork kind |
|---|---|---|
| no cycle open / previous cycle flowed back, `S = []` | `R-open` · `R-abandon` (of the engagement) | — |
| `⟨open, C⟩` written | `R-interest` · `R-abandon` | — |
| interest declared | `R-detect` · `R-objective-revise` (if a detection update supersedes the interest) · `R-abandon` | σ |
| detection declared | `R-objective` · `R-abandon` | — |
| objective written (per-intention phase opens) | `R-intention` · `R-abandon` | — |
| ≥1 intention declared, some pending θ | `R-intention` (another) · `R-required-resources` (**the standing option**) · `R-moot-intention` (K ≥ 2) · `R-abandon` | **σ** |
| θ written for `g_k` | `R-gate-pass` **or** `R-gate-fail`→`R-spawn` — *selected by the possession guard, not by choice* · `R-intention` · `R-required-resources` · `R-abandon` | guard, then σ |
| `gate-passed q` | `R-execute` · `R-abandon` | — |
| `gate-failed q` (parent suspended, sub-cycle running) | the sub-cycle's own admissible set · `R-abandon` (pops one level) | — |
| sub-cycle at Λ-body, `S ≠ []` | `R-close-nested` | — |
| sub-cycle flowed back, `S ≠ []` | `R-resume` — **blocked unless `R ∋ parent-pending-q`** | — |
| `resumed q` | `R-gate-pass` (re-fires) · `R-abandon` | guard |
| `executed`, per-intention pattern | `R-perceive` **or** `R-perceive-failure` — *guard-determined* | guard |
| all live intentions `executed`, cycle pattern | `R-perceive-cycle` **or** `R-perceive-failure-cycle` — *guard-determined* | guard |
| `⟨perceive-failure, …⟩` written | `R-intention` (a fresh intention — the adaptive route) · `R-moot` / `R-moot-intention` · `R-abandon` | **σ** |
| every live intention terminal | `R-select` · `R-intention` · `R-required-resources` · `R-abandon` | **σ** |
| `⟨select-staged, σ⟩` | `R-outcome` | — |
| Ω-body | `R-obtained-utility` | — |
| Λ-body, `S = []` | `R-close` | — |
| `⟨close, C⟩` | `R-flowback` | — |
| `⟨moot, C⟩` · `⟨abandon, C⟩` | **terminal** — no forward rule | — |

**`R-abandon` appears in almost every row.** That is correct and deliberate; do not prune it for brevity when presenting options, but do not lead with it either.

**The one stuck state.** `θ-written ∧ R ∌ q ∧ escalation depth already at its bound ∧ K = 1` has no forward lifecycle rule. This is not a bug: it is the state where the operator must moot or abandon. A stuck configuration is Pillar 2 asking for judgment, not an error to route around.

---

## 5. Which forks are which

Getting this wrong corrupts the audit trail, because the two go in different columns and mean different things at review.

**Guard-determined (Pillar 2 — the operator reads the world):**

- `R-gate-pass` vs `R-spawn` — *does the actor possess q?*
- `R-perceive` vs `R-perceive-failure` (and the cycle-scoped pair) — *did the realized comparison validate the projection?*
- any operator-attested premise (a void premise licensing a moot; a detection update licensing an objective revision)

**σ-forks (Pillar 4 — the operator sequences):** which intention to declare next; whether to resource a pending intention now or advance the current one; spawn order when more than one resource is missing; which continuation after a perceive-failure; which selection to stage; whether to abandon.

**Standing options.** Three rules are admissible across long stretches rather than at a single state, and under-recording them is the most common σ-log defect: `R-required-resources` (whenever any declared intention still lacks its θ), `R-intention` (whenever the cap allows another), and `R-moot-intention` (whenever K ≥ 2 and at least one live intention would remain). Naming only the "next" step hides two live choices.

**The stance governs the pattern, and is received rather than chosen** — `adaptive`, `pre_committed_resource_careful`, `pre_committed_resource_batched`. See `03-SESSION-PROTOCOL.md` § State-by-state discipline.

---

## 6. Termination, and what it actually rests on

Strong normalization (Theorem 13.5) is **conditional**. Four things are unbounded by the mechanics themselves, and the theorem holds only once an engagement bounds them:

| Condition | Bounds |
|---|---|
| WF-1 | intentions per cycle (`K_C`) |
| WF-2 | interest revisions per cycle (`J_C`) |
| WF-3 | escalation depth per engagement (`D`) |
| WF-4 | top-level cycles per engagement (`L`) |
| WF-5 | all declared intentions in a cycle agree on the perceive pattern |
| WF-6 | resources per intention bounded, and distinct intentions' resource sets disjoint |

**In PLC these are engagement-level declarations, not defaults.** Record them once per sphere (Sphere Manifest or the Campaign that scopes the engagement) and check them at QUARTERLY-AUDIT. An engagement with no declared bounds is not "unbounded in practice" — it is an engagement whose termination argument has not been made.

WF-5 and WF-6 are also *correctness* conditions, not just termination ones: WF-6's disjointness is what lets two intentions be worked in either order without changing the outcome, and WF-5 is what stops a cycle from mixing per-intention and cycle-level perceives.

**What each meta-theorem licenses in PLC** — and where the practice lives:

| Theorem | The PLC practice that depends on it | Where |
|---|---|---|
| 13.1 Uniqueness (per-actor) | keying every LSPI path by **owning actor + path** | `04-SCHEMA.md` § System 1 |
| 13.2 Subject reduction | you may apply a licensed rule without re-validating the whole record | this chapter |
| 13.3 Congruence decidability | normalize-then-compare, over exactly three generators | `04-SCHEMA.md` § Congruence |
| 13.4 Resource conservation | the quarterly conservation eyeball — obtained once, spent once | `03-SESSION-PROTOCOL.md` QUARTERLY-AUDIT part 5 |
| 13.5 Strong normalization | the WF declarations above + an unnarrowed `R-abandon` | this chapter |
| 13.6 Per-σ confluence | the σ / Guard Log — fixing σ makes the trace reconstructable | `_types/PLC_Cycle.md` |

Conservation of *totals* is not conservation of *identity*: `R-resume`'s membership check exists so that what flows back is the resource that failed the gate, not merely a resource of equal count. Check the identity, not just the tally.

---

## 7. Known-unsound areas — do not build on them

| Area | Status | PLC's constraint |
|---|---|---|
| Multi-resource gate semantics (upstream §11.4.7, "Axis 6") | **open defect upstream** | **One q per gate test.** If an engagement genuinely needs several resources gated, declare separate gate tests. Templates enforce this; the shipping checklist tests it. |
| Declaring a fresh intention from the post-sub-cycle-failure state | **open upstream** | The prose endorses "escalate against a fresh intention" but no rule licenses it from that state. In PLC, route through abandon-up or a new cycle rather than inventing the transition. |
| Interest revision inside an escalation sub-cycle | **open upstream (fidelity, not soundness)** | A revised sub-cycle interest can break `R-resume`'s literal membership test. Do not revise a sub-cycle's interest; revise the parent's and re-spawn. |
| Simultaneous sibling sub-cycles; per-intention multi-execute | needs-inspection upstream | One sub-cycle per gate failure. Spawn order is a σ-choice, logged. |

Report any of these surfacing in live work to the operator with the citation; do not resolve them locally (`CONTRIBUTING.md` § correction-log discipline — fix first, build second).

---

## 8. Ground truth

Five worked cases carry the mechanics. If a PLC session's cycle behaviour contradicts what these witness, the session is wrong.

| Case | Shape | What it fixes in place |
|---|---|---|
| **Charles** | single intention, one cycle, gate passes | the canonical linear walk |
| **Jim** | single cycle, gate passes | baseline variant |
| **Nathan** | depth-2 escalation, batched intentions, terminal **cycle-level** perceive | `R-spawn` → `R-close-nested` → `R-resume`; the pre-committed resource-careful stance; why `R-perceive-cycle` writes no per-intention marker |
| **Sarah** | batched resourcing, mid-cycle objective revision, intention-scoped moot | `R-objective-revise` with the superseded body retained; `R-moot-intention`; the resource-batched stance |
| **Rusty** | adaptive, three intentions, perceive-failure driving a new intention | the adaptive stance; the standing option; the augmented gate's three-member plan that passes where no single member would |

The worked example sphere (`Spheres/Example-Sphere-Acme-Corp/`) reproduces the Rusty gate pattern, the Sarah revision, and a Nathan-shaped acquisition; it is the volume's regression substrate.
