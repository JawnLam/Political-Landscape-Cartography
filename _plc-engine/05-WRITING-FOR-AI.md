---
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-engine-05-writing-for-ai
title: "PLC Engine — 05 Writing for AI"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
doc_type: engine
role: writing-discipline
scope: subject-agnostic-within-PLC
updated: 2026-06-13
---

# 05 — WRITING FOR AI

> **Writing prose that an AI will execute as instructions is different from writing prose for humans. Different conventions, different failure modes, different quality bar. This file documents the discipline.**

## The four audiences of PLC's prose

Every line of prose in PLC is read by one of four audiences. Understand which before writing.

1. **The AI on session start** — reads `AI-BOOTSTRAP.md`, `00-START-HERE.md`, and Tier 1 files in full. Writes for this audience must be operational, unambiguous, ordered.
2. **The AI mid-session** — consults specific engine files on demand. Writes here must be retrieval-friendly with clear headers and self-contained sections.
3. **The operator reading docs** — README, INSTALL, OPERATOR-GUIDE, CONTRIBUTING. Writes here must be explanatory, persuasive, lightly motivating.
4. **The operator reading the sphere cartridge** — manifest, state, decisions, sphere content. Writes here must be terse, factual, scannable.

Don't blur the lines. README prose belongs in README, not in the engine. Engine prose belongs in the engine, not in README.

## Conventions for AI-facing prose

### Be operational, not theoretical

Don't write *"Consider the relationship between the principal's agenda and the political landscape."* Write *"Before drafting the Principal's funnel, walk through CQ3 with the operator one question at a time. If the operator can't articulate the Agenda, return to CQ6 and probe for the motivating political context."*

The AI is going to execute the prose. Make it executable.

### Use imperative voice

*"Read the file."* not *"The file should be read."*
*"Ask one question."* not *"Multi-bullet questionnaires are to be avoided."*

### Numbered steps for sequences; tables for sets

Sequences are ordered; sets are unordered. Use the right structure.

The interaction-cycle protocol (14 constituents) uses numbered steps because the order is load-bearing. The 13 relation families use a table because they're a set of types, not a sequence.

### Headers must reflect actual structure

The AI navigates by headers when consulting on demand. Headers must be descriptive enough to find without reading the body.

`## Q7 — Custom session activities` is fine; `## Things to think about` is not.

### State the negative as well as the positive

For every "do this," include "don't do that" where there's a known failure mode. The AI's default behavior is often the failure mode; the explicit "don't" prevents reversion.

`02-PRINCIPLES.md` follows this discipline — each principle has working consequences AND an explicit anti-pattern.

### Reference other files explicitly

When a section depends on another file, link it: *"See `03-SESSION-PROTOCOL.md` § Audit Mode for the audit protocol."* The AI will follow the reference if needed.

### Use YAML frontmatter for machine-readable metadata

Every file the AI parses has YAML frontmatter at the top. Schemas and per-Item state live in YAML. Prose lives in the body.

### Apply Convention 1-2 frontmatter conventions

When drafting any file with YAML frontmatter:

- Six Universal Core fields: `type`, `Item_ID`, `Title`, `Date_Added`, `Date_Modified`, `Needs_Processing`
- Property naming: prefix `plc_` (lowercase); body `Title_Snake_Case`; acronyms fully capitalized
- Enum identifiers: `plc_<lowercase_plural>`
- `type: PLC_<TypeName>` on Items; `type: Fleeting` on non-Item files
- `AI_Instructions: ""` field present even when empty (matches OVE_OV_Manifest pattern)

These are not subject-specific stylistic choices. They are vault-compatibility defaults inherited from OVE's conventions; **this section is PLC's statement of record for them.** There is no `_meta/CONVENTIONS.md` in this volume — a frontmatter or naming question resolves here, and the shipped `_types/` files are the worked witnesses.

### LSPI notation discipline (substrate authority 5)

When AI-facing prose contains slash-addressed expressions: projected values carry the prime `′` and are never overwritten by realizations — both persist (Persistence Invariant; forecast calibration depends on it). Decision-matrix options are written `P` (preferred position) and `Adv` (adverse alternative); bare corpus lever letters `X`/`Y` never appear in integrated artifacts (alias map: corpus `X`→`P`, corpus `Y`→`Adv`).

**The rule bans the *corpus's* lever letters. It does not touch LSPI's own constituent symbols.** Table 4 (`04-SCHEMA.md` System 1) makes `X` the Latin symbol for the **adverse alternative** — so `X` inside a slash path is correct and stays: `[Α/i./t./D./P./u.] > [Α/i./t./D./X./u.]` is the canonical comparison form, witnessed throughout the worked cycle file the generation discipline tells you to copy patterns from. Rewriting that `X` to `P` inverts the expression's meaning and is an F10 silent coercion, not a style fix. The two systems assign `X` opposite roles — corpus `X` is the *preferred* lever, LSPI `X` is the *adverse* option — which is precisely why the alias map exists. Every LSPI path is keyed by owning actor. See `04-SCHEMA.md` System 1 for the full discipline; F10/F11 below for the failure modes.

### Don't write trivia

If the AI doesn't need it to do the work, leave it out. The context window is a public good — and PLC's engine + frameworks + Catalogue ship as ~5MB of structured prose; every unnecessary word burns budget the operator will need for actual sphere work.

## Conventions for operator-facing prose

### README

- Lead with the one-line pitch (*"Political Landscape Cartography is a markdown-based operating volume for mapping and navigating organizational political landscapes"*)
- Show quick-start in the first screen
- Tell the operator what to read next based on what they want to do (consultant deploying / principal self-coaching / orientation only)
- Don't explain what you're building until they're invested
- The "Foundations" section names the five substrates and the 50 theorists explicitly per D15 (defensible scholarly canon)

### INSTALL

- Step-by-step, minimal prose
- Convention 7 install snippet with the OV's actual GitHub URL filled in
- Major.minor folder convention named explicitly (`<OV-Name>-v<major>.<minor>`)
- Anticipate the failure modes
- Troubleshooting table

### OPERATOR-GUIDE

- Pattern: symptom → likely cause → fix
- "Engine vs your work" section explaining the four content zones (Convention 8)
- "Updates and troubleshooting" with stash-pop conflict guidance
- "When PLC is the right form / not the right form" honestly named per D26 boundary
- Mode-aware sections — separate paths for consultant operators vs principal-self operators
- Operator guide ships as a single `OPERATOR-GUIDE.md` with partitioned mode sections (`## In consultant mode` / `## In principal-self mode` subsections inside each topic where the modes diverge; universal prose where they don't). Mirrors D3's "schema identical across modes; only register and ethical-layer checks fork" symmetry. Single-file approach selected over split variants at ARTIFACT-DRAFT.

### CONTRIBUTING

- Crisp distinction: what's in-scope vs. what requires a major version bump (per D13 schema-freeze policy adapted to PLC)
- Four zones enumerated with concrete path patterns (Convention 8)
- Voice and tone conventions stated explicitly

## Tone (applies across all prose)

**Defaults** (override per `_USER.md` if operator prefers otherwise):

- **Peer register.** Adult-to-adult, not teacher-to-student.
- **Direct.** Substantive over encouraging.
- **No filler.** "Great question," "interesting," etc. are forbidden.
- **No flattery.** Strong work is called strong; weak work is called weak.
- **Minimal hedging.** When unsure, say so once and move on — don't pile up qualifiers.
- **No emojis.** Plain prose unless the operator explicitly requests.

### Mode-aware addition for principal-self mode (per D12)

When `plc_Operator_Mode = principal_self`, the AI register adds the **no-false-confidence priming** discipline:

> When the AI does not have evidence to confirm the operator's read, say so once, propose a Detection step, then stop.

Reason: a principal-self operator running PLC under client pressure is vulnerable to absorbing confident-sounding AI output as confirmation. The dissertation's perception-gap discipline applied recursively to the AI-operator interaction prevents the AI from becoming a source of confirmation bias.

In consultant mode, this addition does not apply — the consultant brings their own analytical distance via the §§ 16 + 17 protocols.

## Documented failure modes the writing must guard against

PLC has eleven documented failure modes (F1-F11), plus the F4b worked-example quarantine rule carried under F4. Each is named, numbered, and watched for during writing and execution. This section is the canonical catalogue — there is no `_meta/FAILURE-MODES.md`; F-code lookups resolve here.

### F1 — Multi-bullet questionnaire

When opening sphere intake (CQ1-CQ10) or any discovery-style activity, the AI's natural failure is to dump a numbered list of 5-10 questions in one message. **This must not happen.**

The fix in the writing: every prompt that initiates discovery includes the literal instruction *"Ask one question at a time, conversationally."* The protocol is repeated in `BOOTSTRAP-NEW-SPHERE.md`, in `03-SESSION-PROTOCOL.md` § PRACTITIONER-ASSESSMENT, and in this file. Triple-redundant by design — this failure is documented, recurring, and worth the prose overhead.

Per P3.

### F2 — Fabrication of tactics, theorists, facts, persons

When the AI is asked about a tactic, theorist, person, or fact and cannot confirm from the substrate, the failure is to fabricate plausibly. **This must not happen.**

The fix in the writing: every section that involves referencing external material includes *"If you are not certain the tactic / theorist / fact exists in the Catalogue or in `_frameworks/sources/`, say so or decline to reference it."*

Per P4.

### F3 — Identity inference from indirect signals

When the AI needs to use a principal's or operator's name in prose, the failure is to parse a username, file path, git config, or environment metadata into a guessed real name. **This must not happen.**

The fix in the writing: every template that includes a name field uses `[PRINCIPAL]`, `[OPERATOR]`, `[CLIENT]` placeholders. The principle is stated in `02-PRINCIPLES.md` P5 and called out repeatedly in `00-START-HERE.md` Phase 0.

Per P5. The "Lam-not-John-Lam" discipline applied to PLC.

### F4 — Engine drift into sphere-specifics

When writing engine files, the failure is to slip in sphere-specific examples that become hardcoded. **This must not happen.**

The fix in the writing: examples in engine files come from a small fixed set (shipped worked-example sphere `Example-Sphere-Acme-Corp`; generic placeholders `<Sphere>`, `<Principal>`, `<Actor>`) and are always introduced as *"for example"* or *"e.g."* — never as the canonical case.

If you find yourself writing *"when Alice's CFO Carol..."* in an engine file (rather than in the worked example), stop and refactor.

### F4b — Worked-example bleed into live spheres (quarantine rule)

`Spheres/Example-Sphere-Acme-Corp/` is FICTION — a pedagogical demonstration. Its people, events, credences, margin estimates, probe budgets, and outcomes are fabricated to illustrate mechanics. The failure: citing the example as evidence or precedent in a live sphere ("Carol-type CFOs usually...", "at Acme a three-member plan worked, so...", "0.55/0.40 is a typical opening split").

The rule: the example teaches FORMAT (copy its structures, section shapes, and notation patterns freely — that is what it is for) and never teaches FACTS (never cite its content as data, base rates, defaults, or precedent). Its numbers are not priors. If you catch yourself typing "as at Acme" in a live sphere's reasoning, stop — that is F4b.

### F5 — Asymmetric graph corruption (reciprocal-update failure)

When the operator or AI adds a relation in one direction without the corresponding reverse update, the graph corrupts. Searches in one direction succeed; reverse searches silently fail. **This must not happen.**

Example: adding `plc_Cites_Theorists: [[Schelling]]` to a Tactic file without adding the reverse `plc_Citing_Tactics: [[Tactic-0029]]` to the Theorist file.

The fix in the writing: every Mode D template includes a `## ... Reciprocal` section with comments explaining the reciprocal-update discipline. The session-end protocol in `03-SESSION-PROTOCOL.md` enforces: scan touched files for new relations; locate related Items; propose reverse updates.

Per P11.

### F6 — Drift between root mirror and engine canonical

PLC has both a root-level `AI-BOOTSTRAP.md` and an `00-START-HERE.md` inside the engine. The failure: these drift out of sync.

The fix: the root file is a thin pointer ("read the engine"); the engine file is canonical. If they ever disagree, the engine file wins — and the disagreement is itself an F6 violation to flag and fix.

This is the same F6 inherited from OVE. PLC adopts it verbatim.

**Generalized precedence when any two in-volume documents disagree** (a count, a feature, a path): `CHANGELOG.md` (most recent entry) > engine chapters (`_plc-engine/`) > Type files (`_types/`) > templates > front-door docs (README / INSTALL / OPERATOR-GUIDE / BOOTSTRAP files). Report the stale document to the operator; fix only with approval; NEVER resolve a disagreement by removing the newer feature, and NEVER silently harmonize — the report is the point.

### F7 — Writing for the operator when the AI is the reader

The failure: the engine starts with *"In this section we will discuss..."* — that's writing for a human reader of a textbook, not for an AI executing instructions. **The AI doesn't need to know what's coming; it needs to know what to do.**

The fix: cut all meta-prose about what the section is going to do. Open with the operational directive.

This file's section openings demonstrate the discipline — each opens with the operational point, not with a paragraph about what the section will cover.

### F8 — Gate skip without override logging

When the operator chooses to skip ALTERNATIVES-AUDIT or ETHICAL-ACCOUNTING during RUN-CYCLE, the AI must log the override with the operator's stated justification. **The failure is silent skipping — the AI proceeds without recording the override.**

The fix: every RUN-CYCLE protocol step that involves a gate explicitly checks for completion timestamp in frontmatter; if absent, surfaces the gate; if operator chooses to skip, captures justification before proceeding.

Per P7. The gates are mandatory protocol; overrides are mandatory documentation.

### F9 — Reference system conflation

PLC uses three coexisting reference systems (slash addressing + OPC IDs + Catalogue Reference IDs per D18). The failure: mixing them in a single field or using one in the other's grain.

Examples of F9 violations:

- Writing `α.1/2.1.6.4.2/0029` (slash + OPC + Catalogue in one path — meaningless)
- Putting `0029` in `plc_Slash_Constituents` (Catalogue ID in slash-addressing field)
- Using OPC ID `2.1.6.4.2` to reference a tactic (wrong system; tactics use Catalogue Reference IDs)

The fix: every relevant template clearly labels which reference system applies to which field. Cycle log frontmatter has separate field families: `plc_Slash_Constituents:` (slash addressing), `plc_OPC_Diagnostic_Refs:` (OPC IDs), `tactic_ids_*:` (Catalogue Reference IDs).

Per P8.

### F10 — Silent coercion of malformed LSPI

Slash addressing is the surface syntax of a typed formal system (substrate authority 5; `_frameworks/lspi/`). The failure: an AI encounters a malformed or ill-typed slash expression and "helpfully" fixes it — re-bracketing, guessing an ordinal, swapping a Greek/Latin form, inventing a path segment — instead of rejecting it. Silent coercion corrupts the audit trail: the record no longer says what the operator said, and the uniqueness/typing guarantees no longer apply to what's stored.

The fix: process LSPI expressions in layer order (parse → type-check → congruence → transition). On rejection at any layer, surface the rejection to the operator **with a citation to the violated rule** and ask ONE question (P3) to resolve it. The three lexer normalizations (Α/A glyph, Θ/Φ/Λ context disambiguation, `t.`-insertion — see `04-SCHEMA.md` System 1) are the ONLY licensed automatic corrections; everything else goes back to the operator.

Examples of F10 violations:

- Reading `[Α/i./t./D./P.]` and `[A/i/t/D/P]` as different constituents (missing the licensed Α/A and dot normalizations — under-normalizing is also F10)
- Encountering `θ.q3` where only two required-resources exist and silently renumbering to `q2`
- Accepting a comparison between a benefit cell and a utility (`[…/P/b] > […/X/u]`) — ill-typed; comparisons are utilities-only

**The generation half (writing LSPI, not just reading it).** Never invent notation. When writing a slash expression or Operation Record entry:

1. **Copy an existing pattern.** Find the matching entry shape in the worked example (`Spheres/Example-Sphere-Acme-Corp/Cycles/cycle-0009.md` § LSPI Operation Record) or the 04-SCHEMA System 1 examples, and substitute your constituents into that exact shape.
2. **If no pattern matches, write plain English and flag it.** `"(plain English — no validated LSPI pattern for this; operator/upstream to formalize)"` is ALWAYS correct. An invented-but-plausible slash expression is ALWAYS wrong — it poisons the record with strings that look formal but validate against nothing.
3. **Never compose new operator combinations** (a Greek form you haven't seen applied, a bracket nesting you haven't seen, a new prefix class). If the treatise doesn't show it and the worked cases don't witness it, it does not exist for you.

The asymmetry is deliberate: plain English in the record costs a little precision; fabricated notation costs the audit trail's integrity.

### F11 — Executability claim

LSPI is descriptive, not executable (Pillar 2 — the boundary of computation). Its guards — does the actor possess `q`? does the realized comparison validate the projection? — are resolved by human interpretive judgment, not mechanical evaluation. The failure: prose or chat implying the machine can run a maneuver, compute an outcome, or decide a guard.

Banned formulations: "political computation," "LSPI is executable," "the system will determine whether," "running the cycle shows," "the model predicts the target will select." Correct register: the AI **administers and records**; the operator **drives**. "The gate fires when *you judge* that…"; "the record shows…"; "under your stated read, the admissible next steps are…".

The meta-theorems are real and may be claimed — subject reduction, congruence decidability, resource conservation, strong normalization, per-σ confluence — but they are guarantees about the *bookkeeping*, oracle-relative, not claims that the politics is computable. Never let rigor language shade into effectiveness language.

## Quality checks before committing prose

For engine files:

- [ ] Can a fresh AI follow this without prior context? (Test by reading top-to-bottom as if for the first time.)
- [ ] Are the failure modes explicit?
- [ ] Are cross-references specific (file + section)?
- [ ] Is the imperative voice consistent?
- [ ] Is there any meta-prose ("In this section...") that should be cut?
- [ ] Are tables used for sets and numbered steps used for sequences?
- [ ] Does every section header reflect navigable content?

For operator-facing files:

- [ ] Does the first screen contain enough for the operator to start?
- [ ] Is the quick-start under 5 lines?
- [ ] Is the troubleshooting table representative of actual operator failures?
- [ ] Is the prose readable aloud without sounding stilted?
- [ ] Are the four content zones (Convention 8) named clearly?
- [ ] Is the mode-aware fork (consultant vs principal-self) consistent throughout?

For sphere-content prose (manifest, state, decisions, Actor files, Cycle logs):

- [ ] Is `## Current` content current and `## ... History` content append-only?
- [ ] Are reciprocal relations updated on the related Items?
- [ ] Are the three reference systems used in their native grains (no F9 conflations)?
- [ ] Are gate overrides logged with justification (no F8 silent skips)?
- [ ] Are LSPI expressions layer-validated, with rejections surfaced rather than coerced (no F10)?
- [ ] Do projected values carry `′` and persist alongside realizations (never overwritten)?
- [ ] Are matrix options written as `P` / `Adv` (no bare *corpus* `X`/`Y` in integrated artifacts — LSPI's own `X` inside a slash path is the adverse alternative and must be left alone)?
- [ ] Is every LSPI path keyed by owning actor (uniqueness is per-actor, Theorem 13.1)?
- [ ] Does any sentence claim or imply executability (F11)? If so, re-register it.
- [ ] Do estimation-layer numbers carry their epistemic status (P13: "working," "uncalibrated," "ordinal")? A bare number presented as a finding fails the check.

If any check fails, revise.
