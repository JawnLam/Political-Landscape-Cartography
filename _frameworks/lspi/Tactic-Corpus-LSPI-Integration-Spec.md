---
Item_ID: plc-lspi-tactic-corpus-integration-spec
type: Fleeting
timestamp: "2026-07-24T00:00:00Z"
title: "Tactic-Corpus ↔ LSPI Integration Spec (mirror)"
Date_Added: 2026-07-24
Date_Modified: 2026-07-24
Needs_Processing: false
AI_Instructions: "Mode C mirror — do not edit here; changes originate upstream and are re-mirrored (CONTRIBUTING mirror rule). This is the binding contract the catalogue integration implements: the sidecar INDEX-lspi.json, the ε-template form, and the facet passes in WS4-RUNBOOK.md all answer to this spec. Cite it when checking conformance."
---

# Integration Spec — Binding the 782-Tactic Corpus to LSPI

*Goal: turn the `_political_tactics_markdown_files` corpus (783 records, 782 analyzed) into the concrete **action layer** of LSPI, and enrich each tactic with the facets it currently lacks (resources, detectability, certainty, ethical valence, structured counters). The corpus already supplies the **content**; LSPI already supplies the **grammar**. This spec is the bridge.*

---

## 0. The core claim

LSPI's atomic `ε` (execution) operator is, today, an opaque primitive: an action that applies signed deltas to decision-matrix components. The corpus is precisely an enumerated, analyzed library of *what those actions can be* — 782 of them, each already decomposed into signed effects on benefit/cost of two options. So the integration is conceptually clean: **each corpus tactic becomes a typed `ε`-template; LSPI's "action" stops being a primitive and becomes a citation into the catalog.**

---

## 1. Notation reconciliation — and a collision to fix first

The two systems use the same decision-matrix idea but **clash on the letter "X."**

| Corpus lever | Plain meaning | LSPI component (slash-addressed) | LSPI sign |
|---|---|---|---|
| `B(X)↑` | raise benefit of the option the actor *wants* | `[…/D/P/b]` — benefit of **preferred position** | `+` |
| `C(X)↓` | lower cost of the wanted option | `[…/D/P/c]` — cost of preferred position | `−` |
| `B(Y)↓` | lower benefit of the option the actor *opposes* | `[…/D/X/b]` — benefit of **adverse alternative** | `−` |
| `C(Y)↑` | raise cost of the opposed option | `[…/D/X/c]` — cost of adverse alternative | `+` |

**The collision:** corpus **`X` = LSPI `P`** (preferred position), and corpus **`Y` = LSPI `X`** (adverse alternative — LSPI labels it with ψ/`X`). The same glyph "X" denotes *opposite* options in the two systems.

**Resolution (mandatory before any merge):** in all integrated artifacts, retire the bare letters `X`/`Y` and use the LSPI roles **`P` (preferred position)** and **`Adv` (adverse alternative)**. Keep a fixed alias map (`corpus.X→P`, `corpus.Y→Adv`) in the tooling so the 782 lever strings translate mechanically and unambiguously.

---

## 2. The `ε`-template (the binding object)

Define each tactic **T** as a template:

```
ε_T  :=  ⟨ ΔT , θT , meta T ⟩
  ΔT   = set of signed, intensity-weighted deltas over components {P/b, P/c, Adv/b, Adv/c}
  θT   = required-resource set (typed; see §3)
  meta = detectability, certainty, ethics, counters, provenance (see §3)
```

Instantiating **T** in a live interaction binds the slash-address prefix (the actor/agenda/interest/target path) and the concrete resource instances, yielding a normal LSPI execution line:

```
[a.] ε(<addr>/e.)  →  { <signed component deltas from ΔT>  consuming <θT resources> }
```

`ΔT` is *already latent* in every corpus file — the "Active Levers" section gives each lever's sign and an intensity (1–3). So generating `ΔT` for all 782 tactics is a **mechanical extraction**, not new analysis. This is the cheapest, highest-value first step.

---

## 3. New facets to add (what the corpus lacks)

The corpus index currently carries only: `generic_strategy`, `cluster`, `versatility`, `theorists`. Add five structured facets — each maps to a dissertation idea the corpus leaves on the table:

| New facet | Schema | Source idea | How to populate |
|---|---|---|---|
| `lspi_levers` | `[{component: P/b\|P/c\|Adv/b\|Adv/c, sign:+\|−, intensity:1-3}]` | LSPI binding | **Mechanical** from existing "Active Levers" |
| `required_resources` | `[{type: money\|asset\|credibility\|attribute\|legitimacy\|information\|access\|title\|tribe, role: enabling\|consumed}]` | **#2** (9 currencies of power) | LLM-assisted from prose; currently **absent (0)** |
| `detectability` | `{level: low\|med\|high, signature: "…"}` | **#4** (detection / opacity) | LLM-assisted; today sporadic (~24 files) |
| `certainty_class` | `certain \| probable \| extra_conditional \| spurious` | **#7** (effect reliability) | LLM-assisted; today sporadic (~63 files) |
| `ethical_valence` | `{axes:[deception\|coercion\|fairness\|transparency…], severity:1-3}` | PLC ethical-accounting gate | LLM-assisted; today ~98 files |
| `counter_tactic_ids` | `[tactic_id…]` | defense graph | **Promote** existing "Resolution Approach" prose (777 files) into structured tactic-to-tactic links |

Add the same keys to `INDEX.json` so the catalog becomes **filterable** by resource consumed, detectability, certainty, and ethics — none of which is possible today.

---

## 4. Provenance cross-walk (close the empirical loop)

The corpus is grounded in 50 external theorists, **not** in Lam's own data. For academic defensibility and to prove coverage, add a `provenance` facet linking tactics back to the dissertation's empirical base:

```
provenance: { lam_table3_refs: [Table-3 action rows…], vignette_refs: [Charles|Jim|Nathan|Sarah|Rusty …] }
```

A one-pass cross-walk of Table 3's ~100 actions and the five vignettes' `ε` steps onto corpus IDs yields two things: (1) validation that the 782-item corpus *covers* the grounded-theory base, and (2) a citable bridge from the catalog back to the 25 interviews.

---

## 5. Worked example — end to end

**Tactic 0158 — "The Favor Bank Run"** · corpus strategy *#8 Cost Contrast* · levers `C(X)↓ + C(Y)↑`.

**Translate (corpus → LSPI):**

- `C(X)↓` → decrease `[…/D/P/c]` (lower the cost of the cooperating option)
- `C(Y)↑` → increase `[…/D/Adv/c]` (raise the cost of refusing)

**`ε`-template:**

```
ε_0158  →  { [<addr>/t/D/P/c.] − θ_favor ,  [<addr>/t/D/Adv/c.] + θ_favor }
  θ_favor : required_resources = [{type: credibility(obligation), role: consumed}]
  detectability = low (private, deniable)
  certainty_class = extra_conditional (depends on counterpart valuing the relationship)
  ethical_valence = {axes:[coercion(soft)], severity:1}
```

**Provenance — this binds cleanly to your own data.** Dissertation Table 3 lists *"Recalling of favors owed → Adverse Alternative · Cost · Increase"* — exactly the `C(Adv)↑` half. And the **Rusty → Gerry** vignette executes it verbatim:

```
[a.] ε(Α/i./o./g3/i./o./g./e.) → { [Α/i./o./g3/i./t./D./X./c.] + [Α/i./o./g3/i./o./g./q.] }
```

i.e., raise the cost of Gerry's adverse alternative (refusing the favor), consuming `q` = the previously banked pledge. **Corpus tactic 0158 ↔ LSPI `ε` ↔ Table 3 row ↔ live vignette** — one mechanism, expressed in all three registers. That round-trip is the proof the binding works; reproduce it for a sample of tactics to validate the scheme before scaling.

---

## 6. Sequencing

1. **Adopt the `P`/`Adv` alias** and retire bare `X`/`Y` in integrated artifacts. *(Prevents silent corruption.)*
2. **Auto-generate `lspi_levers`** for all 782 from the existing lever analysis. *(Mechanical; instantly makes the catalog LSPI-native.)*
3. **Promote `counter_tactic_ids`** from the existing Resolution-Approach prose to structured links. *(Turns 777 prose sections into a defense graph.)*
4. **Tag `required_resources`** against the 9 currencies. *(The #2 integration; biggest conceptual win.)*
5. **Add `detectability`, `certainty_class`, `ethical_valence`.** *(Lights up #4, #7, and the PLC ethical gate.)*
6. **Provenance cross-walk** Table 3 + the five vignettes → corpus IDs. *(Validation + academic defensibility.)*
7. **Extend `INDEX.json`** with all new facets; the vector-DB/semantic-search layer (already on the corpus's own `NEEDED_NEXT.md`) can follow.

Steps 1–3 are mostly mechanical and could be done in days; 4–6 are LLM-assisted tagging passes over text that already contains the raw material. None of it is "build the catalog" — that's done. It's "make the catalog speak LSPI and carry the four facets it's missing."
