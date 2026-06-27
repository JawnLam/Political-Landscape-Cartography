---
Item_ID: plc-operator-guide
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Political Landscape Cartography — Operator Guide"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
AI_Instructions: ""
---

# PLC Operator Guide

This guide is for the human running PLC — consultant or principal-self. It assumes you've read `README.md` and completed `INSTALL.md`, and that the AI has loaded the engine on at least one session.

The guide is symptom-oriented: most sections answer "what do I do when X happens" rather than "what is the protocol for X." For protocol detail, the engine is canonical — see `_plc-engine/03-SESSION-PROTOCOL.md`.

## How to read this guide

- Sections that apply to both modes have no mode label.
- Sections that fork by mode have **In consultant mode** and **In principal-self mode** subsections explicitly.
- Symptom → cause → fix tables are the workhorse; skim the symptom column for what's matching your situation.

## The four content zones (Convention 8)

You will write into exactly one of these zones at any time. Understanding which zone you're touching is the most important operational discipline in PLC.

| Zone | Path pattern | You may edit? | Updates via |
|------|--------------|---------------|-------------|
| **Engine** | `_plc-engine/`, `AI-BOOTSTRAP.md`, `BOOTSTRAP-NEW-SPHERE.md`, `_types/` | NO | UPDATE-PROMPT (version bumps) |
| **Framework** | `_frameworks/`, `_PATTERNS/` | NO (extend via `*-extensions/`) | UPDATE-PROMPT |
| **Sphere** | `Spheres/<Your-Sphere>/` | YES — fully yours | Never; preserved across updates |
| **Scaffolding** | `_plc-engine/_templates/`, `_plc-engine/_yaml/` | NO (override per-sphere via `_USER.md`) | UPDATE-PROMPT |

If you find yourself wanting to edit a file outside the sphere zone, **stop**. Either you're misreading what's already in the engine (re-read), or you have a legitimate extension that belongs in `_frameworks/<x>-extensions/` or your sphere's `_USER.md`. Edits to engine/framework/scaffolding zones will be overwritten by the next UPDATE-PROMPT run, silently.

## When PLC is the right form / not

PLC is the right form when ALL of these are true:

- The work is **politically substantive** (durable disposition shifts, coalition work, succession-period dynamics) rather than operational management
- The work has **enough horizon** for the interaction cycle to recur — at minimum two cycles before close; ideally six or more
- The work has **stakeholders whose dispositions affect outcomes** — if the work is principal-only, PLC's actor cartography overhead is wasted
- The operator can sustain **session discipline** — bootstrap takes 60-90 min in consultant mode; cycles run 90-150 min each; quarterly audits are ~2 hours

PLC is the WRONG form when any of these are true:

- The decision is **one-shot** with no follow-through cycle expected
- The political read is **already firm** and you're looking for execution-only support
- The audit standards required are **legal or compliance-grade** rather than scholarly-canonical
- The dynamics are **personal** in ways that don't manifest at organizational politics — PLC's gates are designed for power dynamics, not relationships

When the wrong-form signal is present, name it. Telling the principal "this isn't the right tool for this question; here's what is" earns trust. Forcing PLC onto a non-fit corrupts both this engagement's audit trail and your own pattern recognition across engagements.

## Daily operations

The shape of an active PLC engagement:

| Frequency | Activity | Time |
|-----------|----------|------|
| Per session-start | AI re-reads sphere state | ~5 min |
| Per cycle | RUN-CYCLE (14 constituents + 2 gates) | 90-150 min |
| Per cycle | Phase log appended as signals arrive | minutes per signal |
| Per cycle close | ANALYZE-CYCLE (lessons extracted before they fade) | ~45 min |
| Event-driven | ACTOR-UPDATE when material perception/resource signals come in | 30-60 min |
| Event-driven | UNCOVER when an unknown blocks tactical reasoning | 45-90 min |
| Quarterly | QUARTERLY-AUDIT (3-part base + 4 consultant additions in consultant mode) | ~2 hours |
| Engagement-end | SPHERE-CLOSE + retrospective | half-day |

You should not need to manage cadence manually. The AI's session-end recommendations build the queue; the operator disposes (per P10). Following the AI's recommendation is the default, but you can defer or override at any session start.

### In consultant mode

Additional cadences:

- **§§ 16-17 refresh** at each QUARTERLY-AUDIT — practitioner self-assessment + advisor engagement politics. Catches drift you can't catch on your own.
- **Per-engagement supervisor consultation** if your practice supports it. PLC's audit trail makes the supervisor consultation higher-bandwidth — they read the retrospective drafts rather than your verbal summaries.

### In principal-self mode

Additional cadences:

- **No-false-confidence priming check** at each QUARTERLY-AUDIT — verify the AI is still surfacing detection steps rather than confirming your reads. If it's drifting toward confirmation, re-prime via the session protocol.
- **External perspective every 1-2 quarters** — even principal-self operators benefit from an external read. PLC's structured exports (via `peer-consultant-share.yaml` redaction profile) let you share methodology with an outside reviewer without exposing client-identifying detail.

## Symptom → cause → fix

The operator's primary reference. Search the symptom column for what's matching.

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| AI keeps asking me variations of the same question across sessions | Sphere state isn't being read at session start | Tell the AI: "Read `Spheres/<sphere>/_sphere-state.md` and `_sphere-decisions.md` before continuing." Then verify Tier 1 reads loaded per `_plc-engine/00-START-HERE.md` Phase 0. |
| AI gives me a "considered moves" list that includes obvious bad fits | ALTERNATIVES-AUDIT § 15 walked too narrowly | Re-run § 15 explicitly: "Walk OPC § 15's 10 constructive approaches one at a time. For each, propose moves that fit." Don't accept partial gate completion. |
| AI surfaces a "selected move" without flagging ethical concerns | ETHICAL-ACCOUNTING gate skipped or perfunctory | Force the gate: "Walk OPC § 11's 3 harm scopes × 10 categories. For each, name the risk this move poses (or 'none')." |
| Two of my Actor files contradict each other on the same fact | Reciprocal-update discipline failed | Run a QUARTERLY-AUDIT or ad-hoc graph-integrity pass. The audit catches and repairs F5 violations. |
| Cycle log lessons say "preserved mandate" but the actor-perception evidence contradicts | Confirmation drift in cycle-close synthesis | Re-open the cycle (status: `closed` → `active`) within the grace window. Re-do the cycle-close synthesis (Lessons section). Document the correction in `## Lessons`. |
| Principal funnel sharpness has stayed at 2 for six cycles | Either the funnel is genuinely vague or the AI hasn't been pushing | Schedule a dedicated session: "Sharpen the principal funnel. Walk through the 0→5 mastery scale; identify what level we're at and what would justify the next level." |
| I keep skipping ALTERNATIVES-AUDIT in time-critical cycles | Time pressure overriding gate discipline | This is F8. Each skip MUST log an override with justification. Pattern of skips means engagement design is wrong; surface in next QUARTERLY-AUDIT. |
| AI invokes a theorist I've never heard of | Could be legitimate Catalogue citation OR F2 fabrication | Verify: "Show me the file at `_frameworks/political-warfare-catalogue/by-theorist/<name>.md`." If the file exists, the citation is legitimate. If not, F2 — retract the citation. |
| AI uses the wrong principal's name | F3 (identity inference from file path or context) OR genuine mistake | Tell it: "Use `[PRINCIPAL]` placeholder until I confirm the name. Per P5/F3, do not infer." |
| EXPORT-SHAREABLE produces an artifact with content I didn't authorize | Wrong redaction profile applied | Re-run with explicit profile name: "Apply `external-board-summary.yaml` redaction profile." Verify the output before sending. |
| I can't find a decision I made three weeks ago | Decision wasn't elevated to `_sphere-decisions.md` | Either it's in a session log (search `Sessions/`), OR the elevation criterion was misapplied. If the decision is sphere-level material, append to `_sphere-decisions.md` now with a note about the late elevation. |
| QUARTERLY-AUDIT keeps flagging F5 violations every quarter | Session-end reciprocal-update protocol not running | Add it explicitly to your session-close routine: "Before closing, run the reciprocal-update protocol per `03-SESSION-PROTOCOL.md` step 8." |
| Sphere state file has accumulated 40 lines of `## Decided` bullets | `## Decided` is overwrite zone; you've been accumulating instead of overwriting | Refactor: keep only currently-active decisions in `## Decided`. Superseded positions live in `_sphere-decisions.md`'s supersession chain, not in state. |
| Closed cycle file shows edits in git history after seal date | Mode E violated | This corrupts the audit trail. Document the violation in the next session log; do not attempt to undo. Going forward, treat the cycle's content as advisory rather than canonical. |
| AI says "based on what you've told me before" without me having told it that | Hallucinated context | Tell it: "Cite the file and section where I stated that. If no citation, retract." |
| I have two principals and the AI gets confused about whose agenda is active | Multi-principal sphere without `plc_Coprincipal_Conflict_Discipline` populated | Open the manifest. Populate the field. Tell the AI: "Re-read the manifest. Note the conflict-discipline. Confirm whose agenda is active for this cycle." |
| Sphere bootstrap CQs were answered but no manifest got materialized | Bootstrap session closed without materialization step | Re-open the bootstrap session; run § 11 of `BOOTSTRAP-NEW-SPHERE.md` (Sphere materialization). |

### Symptoms specific to consultant mode

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| OPC § 16 self-assessment flagged something I didn't address | Pre-engagement gate skipped or incomplete | Address now. § 16 gates are protocol per D11 — leaving flags unmitigated risks the engagement and your practice |
| Client requested detail that's only in `audit-trail-full` | Client is asking for advisor-confidential content | Decline. Use `internal-leadership-summary` or `external-board-summary` profiles. If the request is legitimate, surface it in your own supervisor consultation rather than expanding the export profile |
| §17 advisor-engagement politics flagged drift between QUARTERLY audits | Engagement conditions shifted without your noticing | Pause active cycles. Re-do § 17 walkthrough. Either renegotiate engagement conditions OR close engagement |
| Family-personal scope keeps creeping into actor work | Engagement charter boundary not held | Re-read the manifest's `## Engagement Scope`. If the principal wants the expanded scope, run a new SPHERE-OPEN — don't drift |

### Symptoms specific to principal-self mode

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| AI keeps confirming my read of an actor without surfacing detection steps | No-false-confidence priming drifted | Re-prime: "Per D12, do not confirm reads without evidence. If you lack evidence, propose a Detection step and stop." |
| I'm drafting moves but not running them because I want AI validation first | Operator-disposes discipline inverting | The AI proposes; you dispose. If you're waiting for the AI to validate, you've inverted the loop. Make the move OR explicitly decide not to; document the decision in the cycle log |
| My OPC diagnostics keep scoring high on my own §16 fit | Self-assessment without external check | Schedule an external read every 2-4 quarters using `peer-consultant-share.yaml` |

## Working with the AI register

PLC ships with a default communication register:

- **Peer** — adult-to-adult, not teacher-to-student
- **Direct** — substantive over encouraging
- **Minimal hedging** — once-and-done, no qualifier piles
- **No filler** — "great question," "interesting" forbidden
- **No emojis**

If these defaults don't fit your style, override in `Spheres/<sphere>/_USER.md`:

```markdown
---
type: Fleeting
Item_ID: <sphere-slug>-user
title: "<Sphere Name> — User Register Overrides"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
---

# Register Overrides

## Tone
<Any tone adjustments. E.g., "warmer register acceptable" or "I prefer 'we' over 'you' framing.">

## Format
<Any format adjustments. E.g., "use plain-text tables instead of pipe tables" or "longer responses are fine">

## Mode-specific
<Mode-specific overrides if applicable>
```

The AI consults `_USER.md` at every session start. If you don't have one, defaults apply.

## Updates and troubleshooting

When `UPDATE-PROMPT.md` runs to upgrade your OV:

1. **Your sphere cartridges in `Spheres/` are preserved verbatim.** Untouched.
2. **The engine, frameworks, and scaffolding zones get updated.** Your local edits to these zones are overwritten — that's why Convention 8 says don't edit them.
3. **Templates and Types are updated.** Per-sphere overrides (in `_USER.md`) persist.

If you have local edits to engine/framework/scaffolding zones (you shouldn't, but it happens), stash them before update:

```bash
cd /path/to/Political-Landscape-Cartography-v1.0
git stash push -m "pre-update local edits"
# Run UPDATE-PROMPT
git stash pop
# Resolve conflicts on a per-file basis
```

If `git stash pop` produces conflicts, you have two options:
- **Accept the new version** for engine/framework/scaffolding files (recommended) — your local edits were against the design intent
- **Migrate your edits** into a sphere-local override (`_USER.md`) or framework extension (`_frameworks/<x>-extensions/`)

Do not merge engine-zone conflicts directly; the version semantics will break.

## Anti-patterns (the operator's, not the AI's)

| Anti-pattern | What goes wrong | Discipline |
|--------------|-----------------|------------|
| Editing the engine "just this once" | Next UPDATE-PROMPT overwrites; you lose the edit; the edit was never the right fix anyway | Surface the underlying need in `CONTRIBUTING.md` channels |
| Running cycles without QUARTERLY-AUDIT | F5 graph drift accumulates; pattern recognition weakens; engagement degrades quietly | Calendar the audit; don't defer |
| Skipping `## What Didn't Work` in retrospectives | Defensive retrospectives propagate bad patterns forward to next engagement | Honest enumeration mandated by template; don't shortcut |
| Asking the AI to "summarize the cycle" when what's needed is RUN-CYCLE work | The summary becomes the work; structural protocol bypassed | Distinguish surface synthesis from protocol execution |
| Accepting the AI's "all gates passed" without spot-checking | F8 silent-skip violations can hide in fast cycles | Spot-check gate completion timestamps; verify override justifications when present |
| Treating shipped Catalogue as a menu to skim | Strategic reasoning collapses to "pick from list"; Move-Tactic composition lost | Use ALTERNATIVES-AUDIT to drive Catalogue surfacing; don't browse |
| Skipping principal feedback on retrospective draft | Retrospective becomes consultant's view, not joint truth | Even when principal is silent, surface the draft for explicit acknowledgment |
| Letting actor count grow past ~20 active | AI context budget overwhelmed; perception nuance lost | Tier actors: active (5-15) vs. dormant (rest); only active load every cycle |

## Where to go from here

- **Stuck mid-engagement:** check the symptom table above; if not listed, open an issue
- **Want to extend PLC:** `CONTRIBUTING.md` — what's in scope, what triggers a version bump
- **Upgrading:** `UPDATE-PROMPT.md`
- **Closing an engagement:** `_plc-engine/03-SESSION-PROTOCOL.md` § SPHERE-CLOSE
- **Methodology question:** the dissertation in `_frameworks/sources/` is canonical for theory; the engine is canonical for protocol
