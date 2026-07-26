---
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-engine-03-session-protocol
title: "PLC Engine — 03 Session Protocol"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
doc_type: engine
role: session-protocol
scope: subject-agnostic-within-PLC
updated: 2026-06-13
---

# 03 — SESSION PROTOCOL

> **How a PLC engagement actually unfolds across sessions. Activities, decision algorithm, embedded gates, audit-mode protocol, and quality gates.**

## Session lifecycle

```
1. READ engine + sphere state (per 00-START-HERE.md)
2. DIAGNOSE current engagement stage + open threads
3. PROPOSE a session activity with rationale
4. WAIT for operator confirmation or override
5. EXECUTE the activity
6. CAPTURE decisions, updates, audit-trail captures
7. WRITE the session log
8. UPDATE _sphere-state.md (rollup) and _sphere-decisions.md (if a sphere-level decision was locked)
9. END with one explicit Open Thread for next session
```

Steps 1, 6, 7, 8, 9 are non-negotiable per P1, P2. Step 5 varies by activity.

## The 16 universal session activities

| Code | Activity | Right default when |
|------|----------|---------------------|
| **SPHERE-OPEN** | Open a new sphere cartridge | No active sphere; operator opening a new engagement |
| **SPHERE-CLOSE** | Close engagement; generate retrospective | Sphere-close criteria met; operator declares engagement ending |
| **PRACTITIONER-ASSESSMENT** | Walk OPC §§ 16 + 17 (consultant) or § 16 only (principal-self) | Engagement-open (mandatory consultant); quarterly refresh |
| **OPC-DIAGNOSE** | Walk OPC §§ 2-13 (sphere-level diagnostic) | Engagement-open; quarterly refresh; significant sphere-level change |
| **ACTOR-UPDATE** | Update an Actor file; capture perception-gap | Real-world Detection event; routine maintenance; quarterly touchup; cycle close |
| **CAMPAIGN-LIFECYCLE** | Stage transition: open / pause / revive / close | New campaign starts; existing campaign goes dormant; archived campaign revived; campaign completed |
| **RUN-CYCLE** | Execute one 14-constituent ADAPT cycle; embeds two gates | Operator decides to act |
| **ANALYZE-CYCLE** | Retrospective walk of a closed cycle | After cycle close; before next related cycle; learning extraction |
| **FORECAST-CYCLE** | Predict adversary's or own next cycle | Before RUN-CYCLE for prediction-calibration; UNCOVER finding |
| **QUARTERLY-AUDIT** | Forced 90-day cadence per principal | 90 days since last audit per principal; triggered by sphere-state timer |
| **SCAN** | Recurring detection: what's surfaced since last session? | Session-start when not running another specific activity; default lightweight activity |
| **UNCOVER** | Multi-hop synthesis across resource graph + network + perception trajectory | Operator requests "what should I be paying attention to?"; quarterly synthesis |
| **ESTIMATE** | Forward hypothesis-design loop against one target: differential → VoI-selected probes with pre-registered predictions → update → stop rule (per `08-ESTIMATION.md`) | A cycle's gate routes to re-probe; a target's read is load-bearing but soft; margin or depth uncertainty blocks planning |
| **MOVE-LOOKUP** | Query Catalogue by signature / strategy / cluster / free-text | Operator needs tactic options; pattern matching against adversary moves |
| **THEORIST-LOOKUP** | Query Catalogue by theorist | Operator wants to understand a theorist's principle; theorist-pattern recognition |
| **EXPORT-SHAREABLE** | Generate sanitized deliverable for audience | Operator needs to share output with principal / client / board / etc. |

Plus **two embedded gates inside RUN-CYCLE** (not standalone activities):

- **ALTERNATIVES-AUDIT** (OPC § 15 walkthrough)
- **ETHICAL-ACCOUNTING** (OPC § 11 walkthrough)

## Decision algorithm — proposing the next activity

Evaluate in order. First condition that fires determines the default proposal.

### Step 1 — Hard overrides

- **If** `_sphere-state.md` is missing or contradictory → stop and tell the operator (per `00-START-HERE.md` § "If the sphere is in an unexpected state")
- **If** the operator has explicitly named the activity → execute that (with mode-availability check)

### Step 2 — Pre-engagement gate (consultant mode)

- **If** `plc_Operator_Mode = consultant` AND `plc_Engagement_Status = pre_engagement` AND no PRACTITIONER-ASSESSMENT in last 7 days → propose **PRACTITIONER-ASSESSMENT** (mandatory per P9)

### Step 3 — Quarterly cadence

- **If** any active principal has `plc_Last_Quarterly_Check_In` more than 90 days ago → propose **QUARTERLY-AUDIT** for that principal (forced cadence per D4)

### Step 4 — Sphere lifecycle transitions

- **If** sphere-close criteria appear met (per `_sphere-manifest.md`'s `plc_Sphere_Close_Criteria` field) → propose **SPHERE-CLOSE**
- **If** sphere just opened and OPC-DIAGNOSE hasn't been run → propose **OPC-DIAGNOSE**

### Step 5 — Cycles in flight

A cycle is **in flight** when `plc_Cycle_Status` is `active` or `engaged`. There is no `open` status — the enum is `planning | active | engaged | closed | mooted | abandoned | e_immutable`, and "open cycle" wherever it appears in prose is informal shorthand for the in-flight pair. `planning` is not yet running; `closed` / `mooted` / `abandoned` / `e_immutable` are terminal. Test the status values, never the word.

- **If** any cycle is in flight with steps not yet completed → propose continuing that **RUN-CYCLE**
- **If** a cycle has just transitioned to `closed` and hasn't been analyzed → propose **ANALYZE-CYCLE** for that cycle

### Step 6 — Pattern surfacing

- **If** quarterly check-in surfaced un-investigated patterns → propose **UNCOVER** for synthesis
- **If** SCAN at session-open surfaced significant changes → propose **ACTOR-UPDATE** for affected Actors
- **If** an in-flight cycle's augmented gate last routed to re-probe, OR an active Detection Record has budget remaining and unresolved threshold-adjacent uncertainty → propose **ESTIMATE** for that target

### Step 7 — Default

- If nothing else fires → propose **SCAN** as the default lightweight session activity

### Step 8 — Post-proposal

Present the proposal:

```
Proposed activity: <CODE> — <plain-English description>
Rationale: <which conditions fired>
Alternative: <next-priority activity>
Your call.
```

Wait. Do not begin until confirmation or override.

## RUN-CYCLE protocol (the central operational activity)

RUN-CYCLE walks the dissertation's interaction cycle. The dissertation describes the cycle as a directed graph with **19 theoretical categories** (page 162) and **21 operational symbols** (Table 4, page 163-164), bounded by a defined initiation (actor + Interest + desired Resource) and a defined closure (target Selection → Outcome → Obtained Utility for target + Resource obtained-or-not for actor) per page 164. PLC walks the graph in a **canonical 14-constituent operational order** from initiation to closure. The two embedded gates (ALTERNATIVES-AUDIT § 15 + ETHICAL-ACCOUNTING § 11) are PLC additions per D9 — not in the dissertation — that fire after the capability-gate confirms resources are available but before Execution proceeds.

### The 14 constituents (PLC operational walk through the dissertation's directed graph)

Each constituent corresponds to a dissertation theoretical category or operational symbol. Actor and Agenda are cycle context (set at initiation, referenced throughout) per Tables 5-22, not cycle-internal constituents.

**Each step below names the rule(s) that fire there.** The trigger, premises, and state change for every rule live in `09-LSPI-RULES.md` — the rule catalogue and state machine. Cite it at the step; do not restate a rule's premises here. When the AI names admissible next steps to the operator (see § State-by-state discipline), the names come from that chapter.

1. **Interest** — what the agenda requires this cycle to acquire. Dissertation operator: `ι` (lowercase iota); `[a.]ι(Α/i.)` initiates the cycle. **Rules: `R-open` then `R-interest`.**
2. **Detection** — the actor's read of who controls the desired resource and what their decision matrix looks like. Dissertation operator: `δ` (lowercase delta). **Rule: `R-detect`** — the same rule that declares constituents 3-5.
3. **Target** — the actor whose decision matrix the cycle will move. Symbol: `t` / `τ`. **Declared by `R-detect`.**
4. **Preferred Position** — the target's preferred column of the decision matrix. Symbol: `P` / `π`. **Declared by `R-detect`.**
5. **Adverse Alternative** — the target's alternative column (the "no" path). Symbol: `X` / `ψ`. **Declared by `R-detect`.**
6. **Objective** — the target Selection direction the actor is pursuing. Operator: `ω` (lowercase omega). **Rule: `R-objective`**; mid-cycle revision is `R-objective-revise` (non-destructive — both bodies persist).
7. **Intention** — the specific actor-side action chosen to move the target's matrix. Operator: `γ` (lowercase gamma). **Rule: `R-intention`**, once per intention `γ_k` when K ≥ 2.
8. **Required Resources** — what the Intention costs to execute. Symbol: `q` / `θ`. **Rule: `R-required-resources`**, per intention.
9. **capability-gate** — two layers (v1.2+; see `08-ESTIMATION.md` § "The augmented gate"). **Rules: `R-gate-pass` on possession; `R-gate-fail` → `R-spawn` → `R-close-nested` → `R-resume` on `∌`.** (The catalogue has no bare `R-gate` entry — `R-gate` names the pass/fail pair; cite the variant that fired.)
   - **Possession check:** `[a./R.] ∋ <Required Resource>`? One q per gate test (LSPI §11.4.7 constraint). **NO** → spawn a nested Interest where the missing resource becomes the new desired Resource (recursive resource accumulation per dissertation Tables 21-22).
   - **Augmented gate over the intended plan Π:** *Sufficiency* — the plan is expected to close the target's margin (risk allowance for belief variance — an uncalibrated allowance, flag (f); and the sum over members assumes additivity, flag (m6))? *Inclusion* — every member's marginal contribution given the rest exceeds its own cost? *Affordability* — total plan cost ≤ the interest's value? **PASS ⟺ an affordable, sufficient plan exists within held resources with every member clearing inclusion.** Never test one member's worth against the total margin (the M1 scale error); a multi-resource plan where no single member suffices but the set closes the margin PASSES.
   - **The five verdicts.** The gate returns exactly one of: **PASS** (proceed to Execution) / **acquire** (spawn a sub-cycle for the missing resource — `R-spawn`) / **rescope** (shrink the interest and re-run the gate — `R-objective-revise`) / **re-probe** (route back to the detection loop, probe chosen by VoI, budget permitting) / **abandon** (`R-abandon`; cycle status → `abandoned`). Abandon is a verdict, not a failure to reach one — a gate that cannot reach PASS and has no affordable acquisition or rescope has *decided something*, and the record should say so. Record the verdict and the gate block in the cycle file.
   - **GATE 9a: ALTERNATIVES-AUDIT § 15** (PLC addition per D9) — walk OPC § 15's 10 constructive approaches; have legitimate alternatives been considered first?
   - **GATE 9b: ETHICAL-ACCOUNTING § 11** (PLC addition per D9) — walk OPC § 11's harm scopes (3 × 10 grid) + 5 ethical-framework weighting
10. **Execution** — the actor's move enters the world. Operator: `ε` (lowercase epsilon). **Rule: `R-execute`**, per intention; deducts the spent resources from `[a./R.]`.
11. **Perception** — the target's reading of the executed move. Operator: `Γ` (uppercase Gamma). **Rules: `R-perceive`** when the operator judges the projection validated; **`R-perceive-failure`** when it does not (intention-scoped), **`R-perceive-cycle` / `R-perceive-failure-cycle`** at cycle scope. This is a guard, not a σ-fork — the operator's reading of the realized world selects the rule.
12. **Outcome** — the target's Selection (Σ / `S`) from the decision matrix, implicit inside Outcome per Tables 5-22's row structure. Operator: `Ω` (uppercase Omega). **Rules: `R-select` then `R-outcome`.**
13. **Obtained Utility** — utility realized by the target as a result of the Outcome. Symbol: `U` / `Λ`. **Rule: `R-obtained-utility`.**
14. **Obtained Resource** — what the actor obtained (or did not obtain); cycle closes here. Symbol: `Q` / `Φ`. Flows back into the actor's Current Resources `[a./R.]` (Symbol: `R` / `Θ`). **Rules: `R-close` then `R-flowback`** — and `R-prime-preserve` holds across the whole walk, so projections survive their realizations.

### The LSPI formal spine (v1.2+; substrate authority 5)

The 14-constituent order above is the operator-facing gloss. The formal spine is LSPI's 21 transition rules in three families — **lifecycle**, **failure**, **non-destructive**. **`09-LSPI-RULES.md` carries the catalogue and the state machine:** each rule's trigger, premises, and state change, plus which rules are admissible from which state. That chapter is the single maintained copy; this one cites rules at the steps where they fire and never restates their premises. (Upstream source: `_frameworks/lspi/LSPI-Foundations.md` §11 — navigate by section, never read whole.) The AI administers the walk; it never computes it (Pillar 2, F11).

**State-by-state discipline.** At each state, name the admissible next steps — **read them off `09-LSPI-RULES.md`'s admissibility table for the current state; never improvise the list** — and ask ONE question (P3) to elicit the operator's pick. Two kinds of judgment, logged to the cycle's `## σ / Guard Log` separately:

- **σ-forks (strategic, Pillar 4):** multiple rules are admissible and the pick is a sequencing choice. The **standing option** applies throughout: whenever any declared intention still lacks its required-resources declaration, "resource a pending intention now" is admissible alongside whatever else is. The operator's **strategic stance** governs the pattern: *adaptive* (declare each lever only after perceiving the last one's effect — the Rusty pattern), *pre-committed resource-careful* (declare all levers upfront; secure and apply each before the next — Nathan), *pre-committed resource-batched* (declare everything, identify all gaps, then pursue the missing pieces — Sarah). Record the stance in `plc_Strategic_Stance`; receive it, don't choose it.
- **Guards (interpretive, Pillar 2):** the world-reading judgments — does the actor possess q? does the realized comparison validate the projection? Perceive is guard-determined, not a σ-fork: the operator's reading of the realized world selects validated vs failed.

**On perceive-failure:** three admissible continuations, a σ-choice — declare a new intention (adaptive), moot (cycle-scoped; or intention-scoped when K ≥ 2 and at least one live intention remains — the cycle then continues on the rest), or abandon.

**On gate-fail (`∌`):** spawn a sub-cycle whose Interest is the missing resource (recursive acquisition); the parent suspends; on sub-cycle close, obtained resources flow back and the parent resumes at its gate. One q per gate test (upstream §11.4.7 constraint — declare separate gate tests per resource). Sibling sub-cycles don't run simultaneously; spawn order is a σ-choice.

**On moot (`R-moot` / `R-moot-intention`):** the cycle's premise stops holding — the target leaves, the resource is granted by someone else, the interest evaporates. Nothing failed and nothing was decided against; the question stopped being a question. Cycle-scoped moot sets `plc_Cycle_Status: mooted` and closes the cycle. Intention-scoped moot (`R-moot-intention`) requires K ≥ 2 with at least one live intention remaining — the cycle continues on the rest and its status does not change. Record what removed the premise; a mooted cycle with no stated cause is indistinguishable from an abandoned one that no one wanted to log.

**On abandon (`R-abandon`):** the operator elects to stop. Sets `plc_Cycle_Status: abandoned`. **Admissible from any state** — before the gate, at the gate, mid-execution, after a perceive-failure, in a suspended parent, inside a sub-cycle. That universal admissibility is not a convenience; it is the escape hatch the termination argument rests on, which is why its premise must never be narrowed to a subset of states. Abandon is a *verdict* (see constituent 9's five verdicts), so it gets a reason line: what made continuing not worth it — cost exceeded the prize, the ethical accounting landed badly, the landscape moved. Abandon differs from moot in agency: moot is the world removing the question, abandon is the operator answering it with "not this."

**On close:** both projected (′) and realized values persist in the Operation Record — the realization never overwrites the projection (Persistence Invariant; see `06-STATE-PERSISTENCE.md`). Mid-cycle objective revision (the Sarah pattern) appends the revised body alongside the superseded one.

### Gate 9a: ALTERNATIVES-AUDIT

Walk OPC § 15.1 constructive_approaches:

1. **Honest dialogue** with the relevant party — have you tried just talking?
2. **Mutual benefit** framing — is there a non-tactical win-win available?
3. **Trust building** — would a trust-building move serve the agenda better long-term?
4. **Competence demonstration** — would demonstrating capability shift the matrix without political action?
5. **Value creation** — is there a real improvement you could make that changes the calculus?
6. **Problem solving** — is the underlying problem solvable in a way that dissolves the tactical need?
7. **Innovation pursuit** — is there a new approach that bypasses the political conflict entirely?
8. **Culture building** — would a culture intervention serve better than a tactical move?
9. **Talent development** — would developing someone serve the objective better?
10. **Sustainable success** — does the long-term alternative dominate the tactical-cycle alternative?

Capture the walkthrough in Cycle log's `## Alternatives Audit` section. Set `alternatives_audit_completed_at: <ISO timestamp>` in frontmatter.

### Gate 9b: ETHICAL-ACCOUNTING

Walk OPC § 11.1 (potential harm) across three scopes:

- **Individual impact** — 10 categories (career destruction, psychological damage, financial ruin, reputation annihilation, relationship damage, health impact, family impact, legal jeopardy, industry exile, identity destruction)
- **Organizational damage** — 10 categories (culture toxification, trust annihilation, productivity collapse, talent exodus, innovation death, morale destruction, reputation damage, customer loss, investor flight, regulatory intervention)
- **Systemic effects** — 10 categories (institutional rot, knowledge destruction, succession crisis, legitimacy loss, social capital destruction, innovation paralysis, ethical collapse, systemic dysfunction, contagion spread, generational impact)

Plus OPC § 11.2 (ethical evaluation) across 5 frameworks:

- **Consequentialist** — ends justify means?
- **Deontological** — actions inherently wrong?
- **Virtue ethics** — character implications?
- **Care ethics** — relationship damage?
- **Justice** — fairness violated?

Capture the walkthrough in Cycle log's `## Ethical Accounting` section. Set `ethical_accounting_completed_at: <ISO timestamp>` in frontmatter.

### Override discipline

The operator can override either gate. The AI does not refuse — it documents:

- `accounting_overrides: ["<justification>"]` in frontmatter
- Stated reason in the gate's section body
- Session log records the override and the operator's articulated reason

Overrides are documented choices, not refusals (per P10).

## QUARTERLY-AUDIT protocol

Triggered every 90 days per principal (forced cadence per D4). Single session, single file output: `Sessions/<YYYY-MM-DD>_<NNN>_quarterly-audit-<principal-slug>.md`.

### Base protocol (both modes)

1. **Perception-gap audit** — for each significant Actor in the principal's sphere, has the operator's read drifted from observable reality? Walk the `plc_Perception_Gap_Log` history. Flag chronic patterns (e.g., *"you've over-read Carol's loyalty 4 of 6 recent cycles"*).
2. **Eight Benefits of Power inventory** — for the principal, did they experience each of the 8 outcomes from dissertation body p.222 this quarter? Trend direction since last quarter? (favored-subordinate opportunities; exceed-limits authority; disproportionate comp influence; assist-someone-in-need; meeting agenda influence; fast superior response; frequent access to higher decision-makers; advance org updates)
3. **Actor-trajectory review** — sort Actors by `last_touched` ascending. Surface those untouched 90+ days. Propose ACTOR-UPDATE sessions for the most consequential stale Actors.
4. **Forecast-calibration review (v1.2+)** — walk closed cycles' projected (′) vs realized values from their Operation Records. The Persistence Invariant keeps both precisely so this comparison is possible; run it. Flag systematic bias (chronic overshoot/undershoot per target or per tactic family).
5. **Belief-hygiene review (v1.2+)** — for each active Detection Record: stale differentials (no probe or update in 90+ days while load-bearing), depth estimates never revisited, held-resource worth estimates never re-priced after probes. For each principal: resource-conservation eyeball across the quarter's spawn/flowback chains — obtained resources appear exactly once, spent resources deducted exactly once, no leaks or duplications (Theorem 13.4).

### Consultant-mode additions (per D11)

6. **§ 16.9 self-check questions** — walk the 10 questions from OPC § 16.9 (e.g., *"What does my sponsor specifically want me to find? Am I finding it?"*)
7. **§ 17.9 engagement health checks** — walk the 10 questions from OPC § 17.9 (e.g., *"Am I still being heard, or has my access narrowed?"*)
8. **§ 13.2 arc-position review** — where in the engagement arc are we? Which intensification points have we crossed? Which resolution arc are we trending toward?
9. **§ 11 retrospective harm review** — have actual harms accumulated past the threshold the operator set at sphere-open? If yes, surface for sphere-level decision.

### Output

Quarterly audit log captures all sections. Updates `_sphere-state.md` `## Decided` rollup with any sphere-level decisions surfaced. Updates principal's `plc_Last_Quarterly_Check_In` date.

## Other activity protocols

Each of the remaining 14 activities follows a defined protocol. Below are the key elements; see template files in `_plc-engine/_templates/` for the full scaffold each activity produces.

### SPHERE-OPEN

Routes to `BOOTSTRAP-NEW-SPHERE.md` at OV root. Walks pre-engagement (consultant) → 10 CQs → creates 3 backbone files + 7 directory shells + initial Principal(s) + initial Actor inventory + first OPC-DIAGNOSE. Produces `Sessions/<YYYY-MM-DD>_000_sphere-open.md`. Transitions `plc_Engagement_Status` to `routine` once quality gates pass.

### SPHERE-CLOSE

Generates engagement retrospective per D23 Layer 2. Walks: cycles run + pass rate; campaigns history; perception-gap trajectories per Actor; resource trajectory per principal; forecast accuracy; pattern recognition accuracy; Eight Benefits inventory at open vs close; UNCOVER-payoff log (the OV's cognitive-prosthetic claim). Consultant mode adds handoff documentation per OPC § 17.7. Transitions `plc_Engagement_Status` to `closed`. Generates Layer 3 structured export.

### PRACTITIONER-ASSESSMENT

Walks OPC § 16 (practitioner self-assessment) in full. Consultant mode adds OPC § 17 (advisor engagement politics). Produces `OPC-Diagnostics/practitioner-self-assessment-<YYYY-MM-DD>.md` (and `engagement-politics-<YYYY-MM-DD>.md` in consultant mode). Mandatory pre-engagement (consultant); recommended pre-engagement (principal-self).

### OPC-DIAGNOSE

Walks OPC §§ 2-13 (sphere-level structural diagnostic). Produces `OPC-Diagnostics/opc-<YYYY-MM-DD>.md`. Updates `_sphere-state.md`'s `## OPC Current Summary` rollup section.

v1.2+: OPC § 4.3 (blind-spot audit) and § 9 (monitoring & counter-detection) are **inputs to the estimation loop**, not terminal checklists — blind spots surfaced here seed Detection Record differentials; § 9 warning signals become candidate probes. The § "political intensity" reading calibrates the depth-bias `b` (see `08-ESTIMATION.md`).

### ACTOR-UPDATE

Updates a specific Actor's file. **The Actor layout is flat by default: one file per Actor at `Actors/actor-<slug>.md`** — this is what `_types/PLC_Actor.md` specifies and what the shipped worked example uses. Section discipline per D28: `## Current ...` sections overwrite; `## ... History` sections append. Captures perception-gap delta if observable. Updates `plc_Last_Touched` and `plc_Actor_Completeness` if level changes.

**Optional multi-principal overlay pattern (not the default; not shipped).** When one sphere serves several principals whose reads of the same Actor must be kept separate and separately redactable, an operator may elect to split that Actor into a directory: `Actors/<slug>/_baseline.md` for the shared observable record plus one `_view-<principal>.md` per principal carrying that principal's private read. Nothing in the engine assumes this layout and no shipped sphere uses it. Adopt it only where a sphere's principal count actually demands it, record the choice in `_sphere-decisions.md`, and apply it per-Actor — never convert a sphere wholesale. Where a sphere does use it, ACTOR-UPDATE writes the baseline and the relevant view; otherwise it writes the single flat file. If you find both a flat `actor-<slug>.md` and an `<slug>/` directory for the same Actor, that is a drift condition — surface it, do not pick one silently.

### CAMPAIGN-LIFECYCLE

Stage transition with parameter (`open | pause | revive | close`). Updates `plc_Lifecycle_Stage` enum on the Campaign file. `open` creates a new Campaign from `PLC_Campaign_TEMPLATE.md`. `pause` moves to `dormant`. `revive` moves back to `executing`. `close` triggers final retrospective on the Campaign + archival.

### ANALYZE-CYCLE

Retrospective walk of a closed cycle. Compare expected vs actual vs perceived utility. Capture perception-gap delta. Update Actor files affected. If the cycle's selected tactic produced unexpected outcomes, propose pattern updates (P11 reciprocal discipline). If the operator's forecast was wrong, log for forecast-skill calibration (D21 family 12).

### FORECAST-CYCLE

Predict adversary's or own next cycle. Use the inferred Actor profile (agenda, observation node, perception biases, recent tactic patterns, theorist frame). Capture forecast in Cycle frontmatter (`plc_Forecast: ...`) or as standalone `Cycles/forecast-<YYYY-MM-DD>_<slug>.md`. Post-hoc, when the actual cycle plays out, ANALYZE-CYCLE compares forecast vs actual.

### SCAN

Recurring lightweight detection. AI surfaces: what's been touched since last session; pending Open Threads from prior session; any stale Actors (90+ days untouched); any in-flight Cycles (`active` / `engaged`) needing attention; any expired Quarterly check-ins. Default session-open activity if nothing else proposed.

### UNCOVER

Multi-hop synthesis across the relation graph. Queries: resource chains the operator might have missed (family 9 traversal); coalitions emerging from network alignment patterns (family 10); information flows being bypassed (family 11); cross-cycle theorist-pattern recognition; chronic perception-gap patterns per Actor. Surfaces hypotheses for the operator to test. NOT predictions — *hypotheses*. v1.2+: UNCOVER outputs are natural ESTIMATE inputs — a surfaced hypothesis about a target's matrix or depth goes into that target's Detection Record differential.

### ESTIMATE (v1.2+)

The forward hypothesis-design loop against ONE target (`08-ESTIMATION.md`; record in `Detection/detection-<actor-slug>.md` per `PLC_Detection_Record`). Steps: (1) open or load the target's Detection Record; seed/refresh the differential from SCAN, UNCOVER, OPC § 4, and the Actor file — each hypothesis pairs a matrix-loading with a depth hypothesis; (2) if depth is unresolved, design a **depth-discriminating probe first** (transparent bait / consistency check / costly-commitment ask); (3) select the probe by **VoI** — what would change the decision, not what's most uncertain; verify budget (`plc_Probe_Budget_Remaining` > 0); (4) **pre-register predicted responses per live hypothesis before the probe runs** — the AI writes them into the Probe Log now; (5) after the operator executes the probe in the world and reports back (possibly next session), record the observation, update credences, re-decode prior signals if depth moved, and re-price any held-resource worth the probe sharpened; (6) stop when no probe's VoI clears its cost — record the Stop Decision. Prefer costly-signal probes; read pooling moves (speaking second, vagueness, delay) as information. The AI proposes probes with rationale; the operator disposes (P10) — and only the operator judges the observed response (Pillar 2).

### MOVE-LOOKUP

Query the Catalogue. Operator provides: signature filter (e.g., *"Cost Contrast tactics in Information Asymmetry cluster"*) OR strategy number (e.g., *"#4 Pure Obstruction"*) OR cluster ID (e.g., *"C24 Trial Balloons"*) OR free-text problem (e.g., *"how do I shift Carol from blocking to supportive?"*). AI scans `_frameworks/political-warfare-catalogue/INDEX.json` first; loads only 1-5 specific tactic files. Returns candidates with strategy classification + theorist lineage + application examples.

### THEORIST-LOOKUP

Query the Catalogue by theorist. AI loads the relevant `_frameworks/political-warfare-catalogue/by-theorist/<name>.md` facet file. Returns: theorist's foundational principle, citation count across the Catalogue, sample tactics that draw on the principle, optional cross-references to Actors tagged with that theorist's frame (per D15 inferred_theorist_frame field).

### EXPORT-SHAREABLE

Operator declares: audience (`principal | client | board | external_counsel | trusted_peer`); source content (cycle log, retrospective, scenario, custom). AI loads matching redaction profile from `_plc-engine/_yaml/redaction-profiles/<audience>.yaml`. Generates sanitized markdown in `Exports/<YYYY-MM-DD>_<audience>_<slug>.md`. Redaction includes: per-D13 internal Actor file content; per-principal overlay files where the optional overlay pattern is in use; slash-addressed constituent IDs abstracted to plain English; tactic IDs redacted by default (some audience profiles permit them); audit trails internal-only by default.

## Audit Mode (§ 4)

When an operator asks the AI to audit an existing sphere (not run sessions in it):

1. **Ask for the path.** Where on disk is the sphere? If accessible, proceed. If not, ask for relevant files to be pasted.

2. **Read the sphere in order:**
   - Its `_sphere-manifest.md`
   - Its `_sphere-state.md` (full read, not just rollups)
   - Its `_sphere-decisions.md` (full read)
   - The most recent OPC diagnostic in `OPC-Diagnostics/`
   - A representative sample of Actor files (`Actors/actor-<slug>.md`; 3-5)
   - A representative sample of Cycle files (5-10 most recent)
   - The most recent Quarterly audit (if any)

3. **Audit against the 13 principles** from `02-PRINCIPLES.md`. Specifically check:
   - [ ] **P1 State lives in files.** Is sphere state on disk and current?
   - [ ] **P2 Write before you end.** Are all sessions logged?
   - [ ] **P3 One question at a time.** Do session logs show multi-question dumps?
   - [ ] **P4 Never invent.** Do tactic references exist in Catalogue? Theorists in by-theorist?
   - [ ] **P5 Never fabricate identity.** Are real names used or placeholders?
   - [ ] **P6 Recursive resource control.** Is the Eight Benefits trajectory tracked?
   - [ ] **P7 Catalog all; gate suggestion.** Are gate completions logged in cycle frontmatter? Any overrides documented?
   - [ ] **P8 Three reference systems.** Are the three systems used appropriately (not conflated)?
   - [ ] **P9 Mode-aware discipline.** Was PRACTITIONER-ASSESSMENT done at pre-engagement (consultant mode)?
   - [ ] **P10 Propose-don't-decide.** Are operator overrides logged with justification?
   - [ ] **P11 Reciprocal updates.** Do relations have reciprocal back-references?
   - [ ] **P12 Cognitive prosthetic.** Are forecasts logged and calibrated post-hoc?
   - [ ] **P13 Scaffolding numbers.** Do estimation-layer quantities (credences, margins, depth, worth, VoI) carry their epistemic status ("working credence," "uncalibrated," "ordinal")? Any number quoted as a finding without a calibration record is a violation.

4. **Surface findings** in three buckets:
   - **Critical** — violations that break audit-grade integrity (closed cycle edits; fabricated identities; missing gate completions)
   - **Significant** — patterns that will produce drift over time (chronic gate overrides without justification; stale Actor files; reciprocal-update failures)
   - **Cosmetic** — small improvements

5. **Propose fixes** in priority order. Do NOT silently modify the sphere — propose and wait for operator's call.

## Writing the session log

At the end of every session, create or finalize a file in `<Sphere>/Sessions/` named:

```
<YYYY-MM-DD>_<NNN>_<activity-code>.md
```

`<NNN>` is zero-padded sequential per sphere. Use `_plc-engine/_templates/PLC_Session_Generic_TEMPLATE.md` (base) or the activity-matched variant per D29 — five specialized session templates ship:

| Activity | Template |
|---|---|
| any activity without a specialized variant | `PLC_Session_Generic_TEMPLATE.md` (base) |
| RUN-CYCLE | `PLC_Session_RUN_CYCLE_TEMPLATE.md` |
| OPC-DIAGNOSE | `PLC_Session_OPC_DIAGNOSE_TEMPLATE.md` |
| QUARTERLY-AUDIT | `PLC_Session_QUARTERLY_AUDIT_TEMPLATE.md` |
| SPHERE-OPEN | `PLC_Session_SPHERE_OPEN_TEMPLATE.md` |
| SPHERE-CLOSE | `PLC_Session_SPHERE_CLOSE_TEMPLATE.md` |

## Updating `_sphere-state.md` and `_sphere-decisions.md`

After every session:

**`_sphere-state.md`** (Mode C — overwrite):
- Update `plc_Engagement_Status` if it advanced
- Update `## Decided` section with any new sphere-level decisions (rollup of `_sphere-decisions.md`)
- Update `## OPC Current Summary` if OPC-DIAGNOSE ran
- Update `## Open Threads` (close any addressed; add new ones)
- Update `## Recent Sessions` (prepend new session pointer)
- Update `## Active Campaigns` (lifecycle stages)

**`_sphere-decisions.md`** (Mode A — append-only):
- Append a dated entry for any sphere-level decision locked this session (per D27 criteria — sphere-close criteria changes, operator-mode switches, domain-validity reassessment, principal additions/departures, strategic pivots, engagement pause/resume, catalogued-move ethical overrides logged retrospectively, cross-engagement continuity decisions)

## Quality gates

Before ending any session, confirm:

- [ ] At least one concrete sphere step taken (cycle progressed; Actor updated; campaign transitioned; OPC refreshed; deliverable exported)
- [ ] Session log written
- [ ] `_sphere-state.md` updated
- [ ] `_sphere-decisions.md` updated (if a sphere-level decision was locked)
- [ ] Explicit Open Thread for next session
- [ ] Any new relations have reciprocal back-references proposed or made (per P11)
- [ ] Any in-flight Cycle's status accurately reflected (D / E per `plc_Cycle_Status`)

If any is no, the session is not complete.
