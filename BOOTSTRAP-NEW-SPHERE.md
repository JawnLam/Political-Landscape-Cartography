---
Item_Prototype: Fleeting
Item_ID: bootstrap-new-sphere
Title: "PLC — Bootstrap a New Sphere"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
type: bootstrap
role: new-sphere-intake
scope: subject-agnostic-within-PLC
updated: 2026-06-13
---

# BOOTSTRAP A NEW SPHERE

> **A "sphere" in PLC is one political landscape — typically one organization. This file is the intake protocol the AI runs with the operator to open a new sphere cartridge. Do not skip steps. The quality of every downstream cycle, OPC diagnostic, and audit traces back to the quality of this opening.**

## Before reading this file

The AI must have completed Phase 0 of `_plc-engine/00-START-HERE.md`:

- Read the Tier 1 engine chapters (00 through 07)
- Read `01-WHAT-IS-PLC.md`, `02-PRINCIPLES.md`, `04-SCHEMA.md` at minimum
- Confirmed the operator wants to open a NEW sphere (not resume an existing one)

If the operator wants to resume an existing sphere, route to `00-START-HERE.md` § "Active sphere identification" instead.

## The quality floor

Sphere quality is established at open. PLC does not iterate sphere quality across cycles — the sphere either has enough substrate to operate against, or it doesn't. If you reach the end of this protocol and the operator could not answer CQ1-CQ8 substantively, **pause and surface that as a blocker** rather than materializing a sketch sphere that the operator will have to rework mid-engagement.

This is not perfectionism. It's a load-bearing PLC convention. The 14-constituent cycle assumes a populated Actor cast and a sphere state. Opening a sphere without that substrate is opening an empty cartridge that pretends to be full.

## Section 1 — Pre-engagement (mode-aware hard precedence)

Before asking CQ1, the AI must establish the operator mode.

**Ask one question, conversationally:**

> "Before we open the sphere, I need to understand the operator-principal relationship. Are you (a) a consultant working with a principal who is a separate person, or (b) the principal yourself, using PLC for self-coaching?"

Record the answer in working state. This determines the pre-engagement path.

### Path A — Consultant mode (hard precedence)

If `plc_Operator_Mode = consultant`, the AI **MUST** run OPC §§ 16 + 17 before CQ1. This is not optional and not negotiable. Per D11.

- **OPC § 16 — Practitioner Self-Assessment.** Walk the operator through the 14 self-assessment subsections one at a time. Capture answers in working state. Surface any item where the operator scores themselves below threshold; ask whether that constitutes a contraindication for taking the engagement.
- **OPC § 17 — Advisor Engagement Politics.** Walk the operator through the 11 advisor-engagement subsections one at a time. Capture answers in working state. Surface any item that indicates a hostile engagement environment.

If the §§ 16-17 pass surfaces blockers, **stop the bootstrap.** The operator either declines the engagement, mitigates the blockers, or accepts and overrides — and any override is logged with justification at sphere-open.

These two assessments materialize as `Spheres/<Sphere>/Practitioner-Assessment.md` after CQ1 (when the sphere identity is known and the file can be properly named).

### Path B — Principal-self mode (lighter touch)

If `plc_Operator_Mode = principal_self`, the AI **MAY** offer OPC § 16 as optional self-orientation but does not enforce it. § 17 does not apply (no advisor engagement politics when the operator IS the principal).

Instead, the AI flags the **no-false-confidence priming discipline** (per D12, P12) — *"When I lack evidence to confirm your read, I will say so once, propose a Detection step, and stop. I will not become your source of confirmation bias."*

Capture the operator's acknowledgment in working state.

### Don't proceed to CQ1 until pre-engagement closes

If the operator pushes to "just get started" before § 16-17 (consultant mode), respond: *"Per OV protocol, the practitioner assessment runs first in consultant mode. It takes ~30 minutes. I can walk you through it now, or we can defer to a separate session. Which do you prefer?"*

If they defer, materialize a stub sphere with `plc_Pre_Engagement_Status: deferred` and flag the gap in the sphere state. Do not begin RUN-CYCLE until the assessment closes.

## Section 2 — CQ1: Sphere identity

**Ask one question, conversationally:**

> "Which organization is this sphere about? Give me the name as you'd use it in writing — and tell me in a sentence or two what it does."

Listen. Probe for:

- The name as the operator naturally uses it (formal name vs. shorthand vs. anonymized handle)
- Whether the name should be redacted in any exports (EXPORT-SHAREABLE will respect this)
- Industry / sector / scale enough to ground the AI's situational reasoning

**Record in working state:**
- `plc_Sphere_Name`
- `plc_Sphere_Description` (one paragraph)
- `plc_Redaction_Default` (the EXPORT-SHAREABLE default for this sphere)

**Anti-pattern:** Do not infer the organization from the operator's environment, file path, or username. If the operator hasn't named it explicitly, ask.

## Section 3 — CQ2: Principal identity

**Ask one question, conversationally:**

> "Who is the principal? In consultant mode this is your client; in principal-self mode this is you. Give me a name (or `[PRINCIPAL]` placeholder), their role, and what authority they hold in the sphere."

Listen. Probe for:

- Name and role (with `[PRINCIPAL]` placeholder permitted)
- Hierarchical position (CEO / VP / director / individual contributor / board / external)
- Authority scope — what they can decide unilaterally, what requires coalition, what they cannot touch
- Are there co-principals? (PLC supports 1..N principals per sphere — D1)

**Record in working state:**
- `plc_Principal_Name` (or placeholder)
- `plc_Principal_Role`
- `plc_Principal_Authority_Scope`
- `plc_Coprincipal_Count` (default 0)

If co-principals are named, the AI surfaces: *"Note — multi-principal spheres require explicit handling of conflicting principal agendas. We'll capture each principal's funnel separately and flag conflicts during RUN-CYCLE."*

**Anti-pattern:** Do not parse the principal's name from email handles, file paths, or any indirect signal. Per P5 / F3.

## Section 4 — CQ3: Engagement scope & timeframe

**Ask one question, conversationally:**

> "What's the engagement scope? Is this a defined campaign with an end-state in mind, an open-ended advisory relationship, or something else? And what's the timeframe — weeks, months, quarters?"

Listen. Probe for:

- Engagement kind (`new-design` is the OVE term; PLC uses `campaign | advisory | self-coaching | other`)
- Time horizon
- End-state criteria — when does the engagement close?
- Trigger conditions for sphere-close (per D23)

**Record in working state:**
- `plc_Engagement_Kind`
- `plc_Engagement_Horizon`
- `plc_Engagement_End_Conditions`

## Section 5 — CQ4: Initial Actor cast

**Ask one question, conversationally:**

> "Who are the key actors in this political landscape? Not everyone — just the ones whose disposition will materially affect what the principal can accomplish. Give me 5 to 10 names and a sentence on each."

Listen. For each actor, probe lightly:

- Name and role
- Apparent disposition toward the principal (allied / neutral / defensive / opposed / unknown)
- Material resources they hold (per the dissertation's 9-type taxonomy: money / hard assets / credibility / attributes / legitimacy / information / access / title / tribe)
- Network distance from the principal (1 hop / 2 hops / further)

**Don't push for completeness here.** The cast will grow during the engagement. The goal is enough actors to run a first cycle — typically 5-10.

**Record in working state:** stub for each actor with `plc_Actor_Completeness: stub` (per D25). Full Actor files materialize at the end of bootstrap.

**If the operator names < 3 actors:** flag the gap. *"The cycle protocol needs an actor cast to run against. With fewer than 3 actors, the first cycle will have to be an actor-discovery cycle. Do you want to surface more names now, or schedule actor-discovery as the first cycle?"*

## Section 6 — CQ5: OPC diagnostic seed

**Ask one question, conversationally:**

> "Before we do a full OPC diagnostic — which is a separate ~90-minute activity — give me your current read on the sphere across these dimensions: §1 power structure / §2 stakeholders / §13 dynamics / §14 trajectory. Just headline impressions, not detail."

Listen. Probe lightly across the four named sections. Capture whatever the operator gives without forcing depth.

**Record in working state:** a `plc_OPC_Diagnostic_Seed` block in the sphere state file. Mark as `seed` quality (per D25's `plc_OPC_Diagnostic_Completeness` count — this is count 0 of N).

**Schedule a full OPC-DIAGNOSE session** as a follow-up. Default is "within the first week of engagement." Record this commitment in `_sphere-decisions.md`.

## Section 7 — CQ6: Active campaigns / cycles

**Ask one question, conversationally:**

> "Is there anything already in flight that I need to know about? Active campaigns the principal is running, decisions in progress, moves recently made? Or is this a clean start?"

Listen. For each in-flight item, probe lightly:

- Campaign name (if applicable)
- Current state (`planning | executing | dormant`)
- What's at stake
- What the principal has already committed to

**Record in working state:** stubs for each Campaign and Cycle as appropriate.

If there are in-flight cycles, the AI notes: *"Active cycles need to be reconstructed retroactively — agenda, considered moves, alternatives audit, ethical accounting, selected moves. We can either reconstruct now or accept partial audit trail going forward."* Operator chooses.

## Section 8 — CQ7: Ethical and scope guardrails

**Ask one question, conversationally:**

> "What's off-limits? Are there tactics in the Catalogue you don't want suggested under any circumstances? Are there actors you don't want PLC analyzing? Are there topics that should never appear in exports?"

Listen. Probe for:

- Tactic exclusions (e.g., "no clusters tagged sabotage-adjacent")
- Actor exclusions (rare but possible — e.g., a family member in the actor cast the operator declines to analyze)
- Export topic exclusions
- Ethical framework preference (which of OPC § 11's 5 frameworks the operator wants weighted in ETHICAL-ACCOUNTING)

**Record in working state:**
- `plc_Tactic_Exclusions`
- `plc_Actor_Exclusions`
- `plc_Export_Topic_Exclusions`
- `plc_Ethical_Framework_Weighting`

**Anti-pattern:** Don't push for an exhaustive list. Capture what the operator names; trust they'll surface more during ETHICAL-ACCOUNTING gates in RUN-CYCLE.

## Section 9 — CQ8: Engagement bookkeeping

**Ask one question, conversationally:**

> "Last required question: what's your name (or `[OPERATOR]` placeholder), how should I reach you for asynchronous flags, and what's the cadence default — weekly check-ins, biweekly, on-demand?"

Listen.

**Record in working state:**
- `plc_Operator_Name` (placeholder permitted; do not infer)
- `plc_Operator_Contact_Method` (optional)
- `plc_Default_Cadence`

## Section 10 — Optional CQ9-CQ10

These are offered only if the operator hasn't already volunteered the information during CQ1-CQ8.

### CQ9 — Existing artifacts to import (optional)

**Ask:**

> "Do you have any existing notes, decision docs, OPC diagnostics, or related material you want me to pull in? I can read them and incorporate the relevant content into the sphere's substrate."

If yes: capture file paths or content, schedule a separate import session. Don't try to import in the same session as bootstrap — bootstrap is already substantive.

If no: skip.

### CQ10 — Communication preferences (optional)

**Ask:**

> "Anything I should know about how you want me to communicate? Defaults are peer register, substantive over encouraging, minimal hedging, no filler, no emojis. Any of those you want adjusted, or anything else?"

Capture overrides in `_USER.md` (sphere-local) per the convention.

If no overrides: confirm defaults and move on.

## Section 11 — Sphere materialization

Once CQ1-CQ8 are answered (and CQ9-CQ10 optionally addressed), the AI materializes the sphere cartridge.

### Files created at materialization

1. **`Spheres/<Sphere>/_sphere-manifest.md`** (Mode C) — sphere identity, principals, scope, mode, redaction defaults
2. **`Spheres/<Sphere>/_sphere-state.md`** (Mode D) — `## Decided` with the bootstrap decisions, `## OPC Current Summary` with the CQ5 seed, `## State History` with the bootstrap entry
3. **`Spheres/<Sphere>/_sphere-decisions.md`** (Mode A) — append-only log; first entry is "sphere opened" with full CQ1-CQ8 capture
4. **`Spheres/<Sphere>/Principals/<Principal-Name>.md`** (Mode D) — one file per principal with funnel + authority scope
5. **`Spheres/<Sphere>/Actors/<Actor-Name>.md`** (Mode D) — one stub file per actor named in CQ4, each with `plc_Actor_Completeness: stub`
6. **`Spheres/<Sphere>/Campaigns/`** — populated if CQ6 surfaced active campaigns
7. **`Spheres/<Sphere>/Cycles/`** — populated if CQ6 surfaced in-flight cycles
8. **`Spheres/<Sphere>/OPC-Diagnostics/`** — empty, awaiting first full OPC-DIAGNOSE
9. **`Spheres/<Sphere>/Sessions/<date>_000_SPHERE-OPEN.md`** (Mode A) — session log of this bootstrap session
10. **`Spheres/<Sphere>/Practitioner-Assessment.md`** (Mode D) — populated from § 1 if consultant mode

### Frontmatter conformance

Every materialized file conforms to Conventions 1-2:

- Six Universal Core fields present
- `Item_Prototype: PLC_<Type>`
- `plc_*` namespace on properties
- `plc_<lowercase_plural>` for enum identifiers
- `AI_Instructions: ""` field present

### Reciprocal-update enforcement at materialization

When the materialization creates Actor files referenced from Principal files (and vice versa), the reciprocal pointers are wired immediately. No asymmetric graph state at sphere-open.

## Section 12 — Readiness statement

After materialization, the AI emits a readiness statement of the form:

> *"Sphere `<Name>` opened. <N> actors stubbed. OPC seed captured from CQ5. Full OPC diagnostic scheduled. Practitioner assessment <status>. <Active-cycle status>. Ready for: <Next-recommended-activity>."*

The readiness statement is short, factual, and serves as the sphere's first publication.

### What the next activity should be

The recommended next activity depends on the sphere's opening state:

- **If actors are < 5** → recommend ACTOR-UPDATE session to populate the cast
- **If no full OPC diagnostic scheduled** → recommend OPC-DIAGNOSE
- **If an active cycle was named in CQ6** → recommend ANALYZE-CYCLE to reconstruct the audit trail
- **If everything is clean and stubbed** → recommend the first RUN-CYCLE on the principal's top agenda item

The operator chooses. Don't auto-start the next activity.

## Quality checks before closing the bootstrap session

- [ ] CQ1-CQ8 all answered substantively (not stubbed with "TBD")
- [ ] Pre-engagement closed appropriately for the operator's mode (§§ 16-17 ran in consultant mode, or deferred-with-flag captured)
- [ ] All materialized files conform to Conventions 1-2
- [ ] Reciprocal-update protocol passed (no asymmetric graph at open)
- [ ] Session log written and appended to `_sphere-decisions.md` first entry
- [ ] Readiness statement emitted
- [ ] Next-activity recommendation made; operator's choice captured (even if "later")

If any check fails: surface the gap, do not claim the sphere is open.

## Anti-patterns

- **Asking CQ1-CQ8 as a numbered list.** F1 violation. One question, hear the answer, probe, move to the next. Per P3.
- **Inferring the principal's or operator's name from indirect signals.** F3 violation. Use placeholders. Per P5.
- **Skipping § 16-17 in consultant mode because "the operator wants to get started."** P7 / F8 violation. Either run the assessment or capture a logged override with the operator's stated justification.
- **Materializing the sphere with < 3 actors and proceeding as if it's normal.** Per Section 5, this is a gap to surface, not silently accept.
- **Auto-starting the next activity after the readiness statement.** Operator disposes (P10). The AI proposes.
- **Treating CQ9-CQ10 as required.** They're optional. Don't make the operator answer "no" to "do you have existing artifacts?" when they've already implicitly said no by not mentioning them.
- **Letting the operator skip CQ5 (OPC seed) because "we'll do the full diagnostic later."** The seed is not the diagnostic — it's enough substrate to run a first cycle while the full diagnostic is scheduled. Without the seed, the first cycle has no sphere context.
