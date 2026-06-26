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

## The 15 universal session activities

| Code | Activity | Right default when |
|------|----------|---------------------|
| **SPHERE-OPEN** | Open a new sphere cartridge | No active sphere; operator opening a new engagement |
| **SPHERE-CLOSE** | Close engagement; generate retrospective | Sphere-close criteria met; operator declares engagement ending |
| **PRACTITIONER-ASSESSMENT** | Walk OPC §§ 16 + 17 (consultant) or § 16 only (principal-self) | Engagement-open (mandatory consultant); quarterly refresh |
| **OPC-DIAGNOSE** | Walk OPC §§ 2-13 (sphere-level diagnostic) | Engagement-open; quarterly refresh; significant sphere-level change |
| **ACTOR-UPDATE** | Update an Actor file (baseline + per-principal overlays); capture perception-gap | Real-world Detection event; routine maintenance; quarterly touchup; cycle close |
| **CAMPAIGN-LIFECYCLE** | Stage transition: open / pause / revive / close | New campaign starts; existing campaign goes dormant; archived campaign revived; campaign completed |
| **RUN-CYCLE** | Execute one 14-constituent ADAPT cycle; embeds two gates | Operator decides to act |
| **ANALYZE-CYCLE** | Retrospective walk of a closed cycle | After cycle close; before next related cycle; learning extraction |
| **FORECAST-CYCLE** | Predict adversary's or own next cycle | Before RUN-CYCLE for prediction-calibration; UNCOVER finding |
| **QUARTERLY-AUDIT** | Forced 90-day cadence per principal | 90 days since last audit per principal; triggered by sphere-state timer |
| **SCAN** | Recurring detection: what's surfaced since last session? | Session-start when not running another specific activity; default lightweight activity |
| **UNCOVER** | Multi-hop synthesis across resource graph + network + perception trajectory | Operator requests "what should I be paying attention to?"; quarterly synthesis |
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

- **If** `plc_Operator_Mode = consultant` AND `plc_Engagement_Stage = pre_engagement` AND no PRACTITIONER-ASSESSMENT in last 7 days → propose **PRACTITIONER-ASSESSMENT** (mandatory per P9)

### Step 3 — Quarterly cadence

- **If** any active principal has `plc_Last_Quarterly_Check_In` more than 90 days ago → propose **QUARTERLY-AUDIT** for that principal (forced cadence per D4)

### Step 4 — Sphere lifecycle transitions

- **If** sphere-close criteria appear met (per `_sphere-manifest.md`'s `plc_Sphere_Close_Criteria` field) → propose **SPHERE-CLOSE**
- **If** sphere just opened and OPC-DIAGNOSE hasn't been run → propose **OPC-DIAGNOSE**

### Step 5 — Open cycles

- **If** any open cycle (`plc_Cycle_Status: open`) exists with steps not yet completed → propose continuing that **RUN-CYCLE**
- **If** an open cycle has just transitioned to `closed` and hasn't been analyzed → propose **ANALYZE-CYCLE** for that cycle

### Step 6 — Pattern surfacing

- **If** quarterly check-in surfaced un-investigated patterns → propose **UNCOVER** for synthesis
- **If** SCAN at session-open surfaced significant changes → propose **ACTOR-UPDATE** for affected Actors

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

1. **Interest** — what the agenda requires this cycle to acquire. Dissertation operator: `ι` (lowercase iota); `[a.]ι(Α/i.)` initiates the cycle.
2. **Detection** — the actor's read of who controls the desired resource and what their decision matrix looks like. Dissertation operator: `δ` (lowercase delta).
3. **Target** — the actor whose decision matrix the cycle will move. Symbol: `t` / `τ`.
4. **Preferred Position** — the target's preferred column of the decision matrix. Symbol: `P` / `π`.
5. **Adverse Alternative** — the target's alternative column (the "no" path). Symbol: `X` / `ψ`.
6. **Objective** — the target Selection direction the actor is pursuing. Operator: `ω` (lowercase omega).
7. **Intention** — the specific actor-side action chosen to move the target's matrix. Operator: `γ` (lowercase gamma).
8. **Required Resources** — what the Intention costs to execute. Symbol: `q` / `θ`.
9. **capability-gate** — `[a./R.] ∋ <Required Resources>`? **YES** → proceed past the two embedded PLC gates below to Execution; **NO** → spawn a nested Interest where the missing resource becomes the new desired Resource (recursive resource accumulation per dissertation Tables 21-22). PLC standardizes on "capability-gate" with "Resource check" as the dissertation cross-reference name.
   - **GATE 9a: ALTERNATIVES-AUDIT § 15** (PLC addition per D9) — walk OPC § 15's 10 constructive approaches; have legitimate alternatives been considered first?
   - **GATE 9b: ETHICAL-ACCOUNTING § 11** (PLC addition per D9) — walk OPC § 11's harm scopes (3 × 10 grid) + 5 ethical-framework weighting
10. **Execution** — the actor's move enters the world. Operator: `ε` (lowercase epsilon).
11. **Perception** — the target's reading of the executed move. Operator: `Γ` (uppercase Gamma).
12. **Outcome** — the target's Selection (Σ / `S`) from the decision matrix, implicit inside Outcome per Tables 5-22's row structure. Operator: `Ω` (uppercase Omega).
13. **Obtained Utility** — utility realized by the target as a result of the Outcome. Symbol: `U` / `Λ`.
14. **Obtained Resource** — what the actor obtained (or did not obtain); cycle closes here. Symbol: `Q` / `Φ`. Flows back into the actor's Current Resources `[a./R.]` (Symbol: `R` / `Θ`).

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

### Consultant-mode additions (per D11)

4. **§ 16.9 self-check questions** — walk the 10 questions from OPC § 16.9 (e.g., *"What does my sponsor specifically want me to find? Am I finding it?"*)
5. **§ 17.9 engagement health checks** — walk the 10 questions from OPC § 17.9 (e.g., *"Am I still being heard, or has my access narrowed?"*)
6. **§ 13.2 arc-position review** — where in the engagement arc are we? Which intensification points have we crossed? Which resolution arc are we trending toward?
7. **§ 11 retrospective harm review** — have actual harms accumulated past the threshold the operator set at sphere-open? If yes, surface for sphere-level decision.

### Output

Quarterly audit log captures all sections. Updates `_sphere-state.md` `## Decided` rollup with any sphere-level decisions surfaced. Updates principal's `plc_Last_Quarterly_Check_In` date.

## Other activity protocols

Each of the remaining 11 activities follows a defined protocol. Below are the key elements; see template files in `_plc-engine/_templates/` for the full scaffold each activity produces.

### SPHERE-OPEN

Routes to `BOOTSTRAP-NEW-SPHERE.md` at OV root. Walks pre-engagement (consultant) → 10 CQs → creates 3 backbone files + 7 directory shells + initial Principal(s) + initial Actor inventory + first OPC-DIAGNOSE. Produces `Sessions/<YYYY-MM-DD>_000_sphere-open.md`. Transitions `plc_Engagement_Stage` to `routine` once quality gates pass.

### SPHERE-CLOSE

Generates engagement retrospective per D23 Layer 2. Walks: cycles run + pass rate; campaigns history; perception-gap trajectories per Actor; resource trajectory per principal; forecast accuracy; pattern recognition accuracy; Eight Benefits inventory at open vs close; UNCOVER-payoff log (the OV's cognitive-prosthetic claim). Consultant mode adds handoff documentation per OPC § 17.7. Transitions `plc_Engagement_Stage` to `closed`. Generates Layer 3 structured export.

### PRACTITIONER-ASSESSMENT

Walks OPC § 16 (practitioner self-assessment) in full. Consultant mode adds OPC § 17 (advisor engagement politics). Produces `Diagnostics/practitioner-self-assessment-<YYYY-MM-DD>.md` (and `engagement-politics-<YYYY-MM-DD>.md` in consultant mode). Mandatory pre-engagement (consultant); recommended pre-engagement (principal-self).

### OPC-DIAGNOSE

Walks OPC §§ 2-13 (sphere-level structural diagnostic). Produces `Diagnostics/opc-<YYYY-MM-DD>.md`. Updates `_sphere-state.md`'s `## OPC Current Summary` rollup section.

### ACTOR-UPDATE

Updates a specific Actor's `_baseline.md` and (in consultant mode) any relevant per-principal `_view-<principal>.md` overlays. Section discipline per D28: `## Current ...` sections overwrite; `## ... History` sections append. Captures perception-gap delta if observable. Updates `plc_Last_Touched` and `plc_Actor_Completeness` if level changes.

### CAMPAIGN-LIFECYCLE

Stage transition with parameter (`open | pause | revive | close`). Updates `plc_Lifecycle_Stage` enum on the Campaign file. `open` creates a new Campaign from TEMPLATE-Campaign.md. `pause` moves to `dormant`. `revive` moves back to `executing`. `close` triggers final retrospective on the Campaign + archival.

### ANALYZE-CYCLE

Retrospective walk of a closed cycle. Compare expected vs actual vs perceived utility. Capture perception-gap delta. Update Actor files affected. If the cycle's selected tactic produced unexpected outcomes, propose pattern updates (P11 reciprocal discipline). If the operator's forecast was wrong, log for forecast-skill calibration (D21 family 12).

### FORECAST-CYCLE

Predict adversary's or own next cycle. Use the inferred Actor profile (agenda, observation node, perception biases, recent tactic patterns, theorist frame). Capture forecast in Cycle frontmatter (`plc_Forecast: ...`) or as standalone `Cycles/forecast-<YYYY-MM-DD>_<slug>.md`. Post-hoc, when the actual cycle plays out, ANALYZE-CYCLE compares forecast vs actual.

### SCAN

Recurring lightweight detection. AI surfaces: what's been touched since last session; pending Open Threads from prior session; any stale Actors (90+ days untouched); any open Cycles needing attention; any expired Quarterly check-ins. Default session-open activity if nothing else proposed.

### UNCOVER

Multi-hop synthesis across the relation graph. Queries: resource chains the operator might have missed (family 9 traversal); coalitions emerging from network alignment patterns (family 10); information flows being bypassed (family 11); cross-cycle theorist-pattern recognition; chronic perception-gap patterns per Actor. Surfaces hypotheses for the operator to test. NOT predictions — *hypotheses*.

### MOVE-LOOKUP

Query the Catalogue. Operator provides: signature filter (e.g., *"Cost Contrast tactics in Information Asymmetry cluster"*) OR strategy number (e.g., *"#4 Pure Obstruction"*) OR cluster ID (e.g., *"C24 Trial Balloons"*) OR free-text problem (e.g., *"how do I shift Carol from blocking to supportive?"*). AI scans `_frameworks/political-warfare-catalogue/INDEX.json` first; loads only 1-5 specific tactic files. Returns candidates with strategy classification + theorist lineage + application examples.

### THEORIST-LOOKUP

Query the Catalogue by theorist. AI loads the relevant `_frameworks/political-warfare-catalogue/by-theorist/<name>.md` facet file. Returns: theorist's foundational principle, citation count across the Catalogue, sample tactics that draw on the principle, optional cross-references to Actors tagged with that theorist's frame (per D15 inferred_theorist_frame field).

### EXPORT-SHAREABLE

Operator declares: audience (`principal | client | board | external_counsel | trusted_peer`); source content (cycle log, retrospective, scenario, custom). AI loads matching redaction profile from `_plc-engine/redaction-profiles/<audience>.yaml`. Generates sanitized markdown in `Exports/<YYYY-MM-DD>_<audience>_<slug>.md`. Redaction includes: per-D13 internal Actor file content; per-principal overlay files; slash-addressed constituent IDs abstracted to plain English; tactic IDs redacted by default (some audience profiles permit them); audit trails internal-only by default.

## Audit Mode (§ 4)

When an operator asks the AI to audit an existing sphere (not run sessions in it):

1. **Ask for the path.** Where on disk is the sphere? If accessible, proceed. If not, ask for relevant files to be pasted.

2. **Read the sphere in order:**
   - Its `_sphere-manifest.md`
   - Its `_sphere-state.md` (full read, not just rollups)
   - Its `_sphere-decisions.md` (full read)
   - The most recent OPC diagnostic in `Diagnostics/`
   - A representative sample of Actor `_baseline.md` files (3-5)
   - A representative sample of Cycle files (5-10 most recent)
   - The most recent Quarterly audit (if any)

3. **Audit against the 12 principles** from `02-PRINCIPLES.md`. Specifically check:
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

`<NNN>` is zero-padded sequential per sphere. Use `_plc-engine/_templates/TEMPLATE-Session.md` (base) or one of the three specialized variants (TEMPLATE-Session-Quarterly.md / TEMPLATE-Session-Sphere-Open.md / TEMPLATE-Session-Sphere-Close.md) per D29.

## Updating `_sphere-state.md` and `_sphere-decisions.md`

After every session:

**`_sphere-state.md`** (Mode C — overwrite):
- Update `plc_Engagement_Stage` if it advanced
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
- [ ] Any open Cycle's status accurately reflected (D / E per `plc_Cycle_Status`)

If any is no, the session is not complete.
