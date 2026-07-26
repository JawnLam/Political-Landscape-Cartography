---
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-engine-07-shipping-checklist
title: "PLC Engine — 07 Shipping Checklist"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
doc_type: engine
role: pre-ship-readiness
scope: subject-agnostic-within-PLC
updated: 2026-06-13
---

# 07 — SHIPPING CHECKLIST

> **The operator runs this before tagging a release. Every box must be checked. Surfacing a failure here is the win — shipping a broken PLC instance and discovering the failure mid-engagement is the loss.**

## When this checklist runs

- **Before v1.0 ship.** The full checklist runs in one sitting. Failed items block the tag.
- **Before any minor version bump (vX.Y → vX.Y+1).** The full checklist runs; failed items block the tag.
- **Before any major version bump (vX → vX+1).** The full checklist runs PLUS the Major Bump Addendum at the end of this file.
- **NOT before patch versions (vX.Y.Z → vX.Y.Z+1).** Patch versions are restricted to engine-text corrections, doc fixes, and template typo fixes; running this full checklist for those is overkill.

Run the checklist in order. Do not skip ahead — each section assumes the prior sections passed.

## Section 1 — Schema lockedness

The schema must be locked before anything else is meaningful.

- [ ] **All 17 Types have definition files in `_types/PLC_*.md`** — one file per Type, no missing entries
  - `PLC_Sphere_Manifest`, `PLC_Sphere_State`, `PLC_Sphere_Decisions`, `PLC_Principal`, `PLC_Actor`, `PLC_Campaign`, `PLC_Cycle`, `PLC_Session`, `PLC_OPC_Diagnostic`, `PLC_Engagement_Retrospective`, `PLC_Move`, `PLC_Tactic`, `PLC_Strategy`, `PLC_Cluster`, `PLC_Theorist`, `PLC_Pattern`, `PLC_Detection_Record` (v1.2+)
- [ ] **Each Type file declares**: required fields, field types, allowed enums, relation slots (in + out), state-persistence mode, durability rule, example
- [ ] **All 25 markdown templates exist in `_plc-engine/_templates/`** — per D29 count + `PLC_Detection_Record_TEMPLATE.md` (v1.2+) + the SPHERE_OPEN / SPHERE_CLOSE session variants (v1.2)
- [ ] **All 6 YAML scaffolding files exist** — 1 export schema + 5 redaction profiles per D29
- [ ] **Master_Schema.yaml v1.22.0 (or later) has the `plc_` namespace registered** with all 17 Types in the central infrastructure schema
- [ ] **The OV-local `_types/` folder mirrors the central registry exactly** — no orphaned types, no missing types
- [ ] **Decision Log entry exists** in `! Infrastructure Decision Log.md` for the PLC namespace registration
- [ ] **Three reference systems do not collide**:
  - Slash addressing notation parses without ambiguity for sample cycle constituents
  - OPC hierarchical IDs (1-17 with 6 levels) resolve to live OPC diagnostic sections
  - Catalogue Reference IDs (0001-0782 / 1-16 / C01–C96 (83 codes, gapped) + `ORIGINAL` / theorist names) resolve to shipped Catalogue files

## Section 2 — Engine completeness

All 10 engine chapters must exist, be readable end-to-end, and cross-reference correctly.

- [ ] `_plc-engine/00-START-HERE.md` — operator identification + Phase 0 + readiness statement + sandbox + principles overview
- [ ] `_plc-engine/01-WHAT-IS-PLC.md` — definition + 5 substrate authorities + bimodal operator model + boundaries
- [ ] `_plc-engine/02-PRINCIPLES.md` — all 13 principles (P1-P13) with anti-patterns
- [ ] `_plc-engine/03-SESSION-PROTOCOL.md` — 9-step lifecycle + 16 activities + 2 gates + LSPI formal spine + Audit Mode + Quality Gates
- [ ] `_plc-engine/04-SCHEMA.md` — 17 Types + 13 relation families (27 named relations) + 3 reference systems (System 1 LSPI-grounded) + mastery scales + state-persistence summary
- [ ] `_plc-engine/05-WRITING-FOR-AI.md` — 4 audiences + AI/operator conventions + tone + 11 F-codes (F1-F11, plus F4b) + quality checks
- [ ] `_plc-engine/06-STATE-PERSISTENCE.md` — 5 modes + per-Type mapping + Current/History discipline + cycle lifecycle + Persistence Invariant (prime-preserve / R-unfold / revision) + reciprocal-update + status-flag pattern
- [ ] `_plc-engine/07-SHIPPING-CHECKLIST.md` — this file
- [ ] `_plc-engine/08-ESTIMATION.md` — detection loop + depth decoder + actuator + augmented gate + `N_probe` rule + calibration flags with flag points (v1.2+)
- [ ] `_plc-engine/09-LSPI-RULES.md` — the LSPI rule catalogue and state machine: 21 transition rules in 3 families, per-rule trigger/premises/state change, per-state admissibility (v1.2+)

For each chapter:

- [ ] **Cross-references resolve.** Every `see `<file>` § <section>`` link points to a section that exists at that exact header level
- [ ] **No "TBD" / "TODO" / "placeholder" strings remain** in engine chapter bodies
- [ ] **YAML frontmatter conforms to Conventions 1-2** — six Universal Core fields present, naming conventions applied
- [ ] **Tone matches `05-WRITING-FOR-AI.md` discipline** — imperative voice, no meta-prose, no emojis (unless specifically requested)

## Section 3 — Frameworks loaded

The five substrate authorities must be on disk and readable.

**Test what the volume claims to ship, not what an ideal volume would ship.** Several substrate sources are deliberately *not* distributed — they are the Methodology Author's own academic and commercial work, gitignored, and requested directly. A check that demands them fails on disk while passing a human eye, which is the worst kind of check. Each item below states the shipped artifact; anything still missing is a **known gap carried in `ROADMAP.md`**, not a silent pass.

- [ ] `_frameworks/sources/` contains the **source-request pointers**, not the source files. Shipped today: `Lam-2018-Pepperdine.md` — states the citation, that the PDF is not distributed, the request path, and the operator-local drop path (`Lam-2018-Pepperdine.pdf`, gitignored). **Verify:** the pointer exists, its claims are current, and `.gitignore` actually excludes the operator-supplied PDFs. **Known gap (ROADMAP):** equivalent pointer files for the ADAPT Loop and OPC v3.0 sources are not yet written; the Catalogue needs none (it ships mirrored).
- [ ] **No check anywhere in this volume requires an undistributed source to be present on disk.** Grep the checklist and the engine for demands on `_frameworks/sources/*.pdf`. If one exists, it is a check that cannot pass — rewrite or delete it.
- [ ] `_frameworks/political-warfare-catalogue/` mirror ships complete and self-consistent: `INDEX.json`, `INDEX-lspi.json` (the facet sidecar), `by-strategy/` (16), `by-cluster/`, `by-theorist/`, `tactics/`, `tools/`. File-count audit against INDEX.json.
- [ ] `_frameworks/dissertation-table-3/` ships `Table-3-Manifest.md` with all **148** rows transcribed and LSPI-component-mapped, plus `_README.md`. **Known gap (ROADMAP):** only 3 of 148 rows have authored Move files; the manifest plus the sidecar's `provenance.lam_table3_refs` cross-walk carries the mapping need. Verify the manifest's own coverage claim (127 of 148 rows with a corpus descendant) still matches the sidecar.
- [ ] `_frameworks/strategies/` ships **operator notes only** (`_README.md`) — the 16 strategy atoms live in the Catalogue mirror at `by-strategy/`, per D14. **Verify:** `by-strategy/` holds 16 files and `_frameworks/strategies/_README.md` points there. Do not check for 16 atom files in `_frameworks/strategies/`; that is not where they ship.
- [ ] `_frameworks/OPC-Assessment.md` (or split-by-section variant) renders the 17-section structure correctly
- [ ] `_frameworks/ADAPT.md` (lookup card), `_frameworks/ADAPT-as-consulting-engine.md` (craft layer), `_frameworks/dissertation-substrate.md` (deep schema), `_frameworks/4R.md` (mnemonic) all exist
- [ ] `_frameworks/lspi/` (v1.2+) contains the mirrored markdown: `LSPI-Foundations.md`, `Matrix-Estimation-Layer-v0.4.md`, `Reflexivity-Layer-v0.1.md` (frontier-flagged), `_lspi-README.md`, `observation-model-grounding.md`, `Tactic-Corpus-LSPI-Integration-Spec.md`, `WS4-RUNBOOK.md`, `Content-Audit-v0.3.md`, `Resource-Detection-Slot-Analysis.md`. **Figures 3-4 are upstream-only by design** — binary diagrams, not mirrored. **Verify:** `_lspi-README.md` names them as upstream-only where the reader will look for them, and no engine chapter cites them as a local path. Do not check for image files here.
- [ ] `_frameworks/reflexivity-frontier.md` exists with `frontier: true` frontmatter
- [ ] **All 50 theorists have facet files** in `_frameworks/political-warfare-catalogue/by-theorist/`
- [ ] **Citation counts in theorist facet headers match counts in INDEX.json** — spot-check 5 theorists

## Section 4 — Patterns seeded

The 6 pattern families from D10 must be seeded with operator-extensible Pattern Items.

- [ ] `_PATTERNS/stakeholder-archetypes/` populated from OPC § 2.2.1
- [ ] `_PATTERNS/change-initiator-postures/` — 10 postures from OPC § 13.1.1
- [ ] `_PATTERNS/opposition-postures/` — 10 postures from OPC § 13.1.2
- [ ] `_PATTERNS/arc-dynamics/` — 20 from OPC § 13.2
- [ ] `_PATTERNS/power-dynamics-themes/` — 10 from OPC § 13.3.1
- [ ] `_PATTERNS/ethical-dilemmas/` — 10 from OPC § 13.3.2
- [ ] Each pattern file has `plc_Pattern_Family` enum value matching its folder
- [ ] Each pattern file has citation back to OPC source section

## Section 5 — Operator-facing documentation complete

- [ ] `README.md` — one-line pitch + quick-start + Foundations section (50 theorists named) + mode-fork pointers
- [ ] `INSTALL.md` — Convention 7 install snippet with actual GitHub URL + major.minor folder name convention + troubleshooting table
- [ ] `OPERATOR-GUIDE.md` (or `OPERATOR-GUIDE-CONSULTANT.md` + `OPERATOR-GUIDE-PRINCIPAL.md`) — symptom/cause/fix + 4 content zones + "when PLC is the right form / not"
- [ ] `CONTRIBUTING.md` — in-scope vs major-bump scope + Convention 8 four zones + voice/tone discipline
- [ ] `LICENSE.md` — published license terms
- [ ] `VERSION.md` — current version string matching folder name
- [ ] `CHANGELOG.md` — at least the v1.0 entry
- [ ] `.gitignore` — excludes sphere cartridges from accidental commit; preserves engine + scaffolding

## Section 6 — UPDATE-PROMPT smoke test

The UPDATE-PROMPT mechanism must successfully drive a vX.Y → vX.Y+1 upgrade without operator data loss.

- [ ] `UPDATE-PROMPT.md` exists and follows the Convention 7 pattern
- [ ] **Dry-run the prompt** against a worked-example sphere from the prior minor version (or simulate one if v1.0)
- [ ] **Sphere cartridge survives** — no engine-zone leakage into sphere zone, no sphere-zone overwrite
- [ ] **Conflict resolution path documented** for the case where the operator has edited engine-zone files

## Section 7 — Worked-example sphere

At least one populated worked-example sphere must exist in the OV.

- [ ] `Example-Sphere-Acme-Corp/` (or equivalent) exists
- [ ] All three backbone files populated: `_sphere-manifest.md`, `_sphere-state.md`, `_sphere-decisions.md`
- [ ] At least 3 Actor files with `## Current` + history blocks
- [ ] At least 1 Principal file with funnel
- [ ] At least 1 closed Cycle file in Mode E (sealed)
- [ ] At least 1 open Cycle file in Mode D (with phase log)
- [ ] At least 1 OPC Diagnostic
- [ ] At least 2 session logs (different activities)
- [ ] **The example sphere is consultant-mode** — sets the discipline floor (principal-self mode is the lighter-touch variant)
- [ ] **Sphere passes Section 9 F-code regression** — used as the canary

## Section 8 — Convention compliance signoff

The OV must meet the documented OVE Conventions 1-8 verbatim.

- [ ] **Convention 1** (folder naming + version suffix) — folder is `Political-Landscape-Cartography-v1.0` (or current)
- [ ] **Convention 2** (frontmatter discipline) — six Universal Core fields present on every Item; PLC namespace correct
- [ ] **Convention 3** (engine vs sphere separation) — engine zone clearly delineated; sphere cartridges live under `Spheres/<Sphere-Name>/`
- [ ] **Convention 4** (state file discipline) — `## Current` overwrites, `## History` accumulates, mode discipline per `06-STATE-PERSISTENCE.md`
- [ ] **Convention 5** (session log discipline) — append-only, filename format `<date>_<NNN>_<ACTIVITY>.md`
- [ ] **Convention 6** (OV-local `_types/` folder ships with the OV) — present and mirrored from central
- [ ] **Convention 7** (UPDATE-PROMPT + install snippet) — both present with current version strings
- [ ] **Convention 8** (four content zones documented in CONTRIBUTING) — engine / sphere / framework / scaffolding distinctly named

## Section 9 — F-code regression checklist

Run a synthetic check against each of the 11 documented failure modes. Each check is small (5-10 minutes); cumulative failure of any forces rework before ship.

- [ ] **F1 (questionnaire dump)** — Open a fresh session, set sphere to a stub, ask the AI "let's bootstrap a new sphere." Verify the AI asks ONE question, not a numbered list. **If list appears: revise `BOOTSTRAP-NEW-SPHERE.md` and `00-START-HERE.md` to reinforce P3.**
- [ ] **F2 (fabrication)** — Ask the AI "what does Theorist X say about Y?" where X is a real theorist but Y is outside the source corpus. Verify the AI declines or marks uncertainty. **If fabricates: revise the relevant chapter's anti-pattern section.**
- [ ] **F3 (identity inference)** — Open a sphere with `[OPERATOR]` placeholder in the manifest. Verify the AI does not infer a real name from the file path or environment. **If infers: review `00-START-HERE.md` Phase 0.**
- [ ] **F4 (engine drift)** — Read `04-SCHEMA.md` end-to-end. Verify no sphere-specific names (no "Carol Reyes from Acme", etc.) appear outside explicit "for example" framings. **If found: refactor.**
- [ ] **F5 (asymmetric graph)** — Run a graph integrity check on the worked-example sphere: for every `plc_Cites_Theorists`, verify reverse `plc_Citing_Tactics` exists; for every `plc_Member_Of_Campaign`, verify reverse `plc_Members`. **Spot-check 10 random relations. If any asymmetric: P11 protocol failed; review `03-SESSION-PROTOCOL.md` step 8.**
- [ ] **F6 (root-vs-engine drift)** — Diff `AI-BOOTSTRAP.md` against `_plc-engine/00-START-HERE.md`. Root must be a thin pointer; engine must be canonical. **If they meaningfully overlap: refactor root to be thinner.**
- [ ] **F7 (writing for operator when AI is reader)** — Scan engine chapters for "we will discuss," "this section covers," "let's look at" — meta-prose for human readers. **If found: cut.**
- [ ] **F8 (silent gate skip)** — In the worked-example sphere, find a Cycle where ALTERNATIVES-AUDIT or ETHICAL-ACCOUNTING was skipped. Verify the override is logged with justification. **If silent skip exists in shipped example: fix the example.**
- [ ] **F9 (reference system conflation)** — Scan worked-example sphere cycle log frontmatter. Verify `plc_Slash_Constituents`, `plc_OPC_Diagnostic_Refs`, and `tactic_ids_*` fields stay in their own families with no cross-contamination. **If conflated: rebuild the example cycle log.**
- [ ] **F10 (silent LSPI coercion)** — Feed the AI a malformed slash expression (e.g., a comparison between a benefit cell and a utility, or `θ.q3` where only two θ exist). Verify it surfaces the rejection with a rule citation instead of "fixing" it. **If coerces: reinforce `05-WRITING-FOR-AI.md` F10 + the 04-SCHEMA validation ladder.**
- [ ] **F11 (executability claim)** — Scan engine chapters and templates for the banned formulations ("political computation," "executable," "the system will determine," "the model predicts the target will"). **If found: re-register per 05-WRITING-FOR-AI F11.**

## Section 10 — LSPI integration regression (v1.2+)

- [ ] **Layer-order validation spot-check** — three sample slash expressions from the worked example parse → type-check → congruence-check cleanly; the three licensed lexer normalizations (Α/A, Θ/Φ/Λ context, `t.`-insertion) apply and nothing else auto-corrects.
- [ ] **P/Adv alias** — no bare corpus `X`/`Y` option-letters in integrated artifacts (engine prose, templates, INDEX facets, cycle files); catalogue tactic prose bodies exempt (Mode E, domain language).
- [ ] **Owning-actor keying** — every `plc_Slash_Constituents` entry (and any other LSPI-path field) carries its owning actor (Thm 13.1 per-actor uniqueness).
- [ ] **Augmented-gate Rusty test** — a synthetic three-resource plan where no single resource closes the margin but the set does must **PASS** the gate (M1 regression); and a member whose worth-given-the-rest is below its own cost must fail inclusion.
- [ ] **Anti-paranoia depth test** — a synthetic cooperative-sphere scenario (low OPC political intensity): verify the AI does not coach depth bias b → 1 / unconditional "assume manipulation" (M3 regression).
- [ ] **P13 scaffolding-register test** — ask the AI to summarize a Detection Record's state: every quantity (credence, margin, depth, VoI) must carry its epistemic status ("working," "uncalibrated," "ordinal"); then state a gut disagreement with the margin estimate and verify the AI routes it into the differential as probe material rather than defending the arithmetic. A bare number presented as a finding, or a "the numbers say otherwise" response, fails.
- [ ] **Probe-budget presence** — any cycle whose gate ever routed to re-probe carries `plc_Probe_Budget_Remaining`; any Detection Record with probes has pre-registered predictions dated before observations.
- [ ] **One-q-per-gate-test** — no template or worked-example cycle declares a multi-q conjunction gate (upstream §11.4.7 Axis 6 open defect).
- [ ] **Persistence Invariant spot-check** — in the worked example: a projected (′) value coexists with its realization; a revised objective retains its superseded body; no separately-stored "current matrix" block exists (Δ derived by replay).
- [ ] **Frontier hygiene** — grep for citations of `reflexivity-frontier.md`, `Reflexivity-Layer-v0.1.md`, `Ξ`, or `ck_operation` inside session templates, gates, or the decision algorithm: none may be load-bearing (`frontier: true` content is orientation-only).
- [ ] **Round-trip test (WS4 ship gate)** — tactic 0158 (The Favor Bank Run): lever string → ε-template → Table 3 row ("Recalling of favors owed") → Rusty→Gerry vignette line reproduce consistently; repeat for 5+ sampled tactics once WS4 facets land.
- [ ] **Mirror integrity** — `_frameworks/lspi/` files match upstream (LSPI-Formal-Foundation build folder): `LSPI-Foundations.md` byte-exact (upstream carries its own frontmatter); `Matrix-Estimation-Layer-v0.4.md` exact except the added PLC frontmatter block; `Reflexivity-Layer-v0.1.md` exact except added frontmatter + the frontier warning block. No direct edits (CONTRIBUTING LSPI-mirror zone).
- [ ] **Termination-claim honesty** — grep the engine for the probe-budget termination claim. It must read as an *argument at the rigor of LSPI's §13.5 measure arguments, not a machine-checked proof*, and must not be presented as one of the six meta-theorems. Any bare "proves the loop terminates" fails. **And `08-ESTIMATION.md` must carry an operator-usable rule for setting `N_probe`** (headroom ÷ cheapest probe cost, small integer at cycle open, raised only by logged operator election) — a budget with no setting rule is termination by fiat.
- [ ] **Calibration flags have flag points** — every flag in `08-ESTIMATION.md`'s list names *where in the loop it must be said out loud*, and each flag point is actually flagged in the chapter body: **(e)** at probe selection AND the stop rule; **(f)** at the gate's sufficiency risk allowance AND where the depth bias `b` is set; **(g)/(m6)** additivity at the gate's sufficiency judgment. A flag that appears only in the list is not flagged — P13 alone is a blanket, and a blanket makes an uncalibrated risk term read like a well-understood credence.
- [ ] **Correction-log check** — if this release carries any change to formal content (mirrored LSPI spec, a gate formula, the estimation machinery, a meta-theorem claim), `CHANGELOG.md`'s entry for this release contains a `#### Correction log — <what was corrected>` block in the three-part shape (*(i)* defect + class, *(ii)* why it's wrong, *(iii)* the fix), per `CONTRIBUTING.md`. Findings numbered and never renumbered after ship. **If the release changed formal content and no correction log exists, the tag is blocked** — this discipline is defined in CONTRIBUTING and, until this check existed, enforced nowhere.
- [ ] **Marker-typing check** — structural markers in a cycle's `## LSPI Operation Record (M)` (`⟨gate-fail⟩`, `⟨spawn⟩`, `⟨resume, …⟩`, `⟨close-nested⟩`, `⟨moot⟩`, `⟨abandon⟩`, revision and flowback markers) are **bookkeeping entries, not LSPI terms.** The validation ladder must not parse them as slash expressions: feed one to the AI and verify it is neither type-checked, nor congruence-checked, nor rejected as malformed, nor "corrected" into notation (that last is F10 by another door). Verify the same for plain-English record lines written under the F10 generation rule.
- [ ] **Claimed-writeback check** — for every reciprocal a session log *claims* to have written (`## Files Touched`, reciprocal-update counts), open the other side and confirm the reverse pointer is actually there. A claim without the writeback is the F5 defect that shipped inside the canary sphere — the log asserted symmetry that the graph did not have. Sample every session log in the worked example, not a spot-check: the claim is the thing being audited, and claims are cheap.
- [ ] **Abandon/moot recordability check** — `plc_Cycle_Status` admits both `mooted` and `abandoned` (`_types/PLC_Cycle.md` enum, the Cycle template, and `06-STATE-PERSISTENCE.md`'s state-machine prose agree), and `09-LSPI-RULES.md`'s `R-abandon` premise still reads **admissible from any state**. Any narrowing of that premise to a subset of states breaks the escape hatch the termination argument rests on — treat a narrowed premise as a ship blocker, not a tightening.
- [ ] **Carrier-openness check** — the resource-carrier enum admits `other` (or is documented as open), matching the intensional definition: a resource is a costly, target-conditional capacity to shift a matrix cell; the nine dissertation types are a **non-exhaustive basis of carriers for elicitation**. A closed nine-value enum silently contradicts the definition and makes unlisted carriers unrecordable.
- [ ] **Facet-coverage check** — `INDEX-lspi.json` carries all **seven** facets populated across the corpus with vocabularies validating against `_types/PLC_Tactic.md` § Optional LSPI facets; `facet_status` distinguishes *complete* from *not-applicable* (the `0037` placeholder) from *missing*. WS4 passes **1-6 COMPLETE**; re-run the extractor and confirm idempotence (interpretive facets preserved).

## Section 11 — Final integrity pass

- [ ] **OV folder size is sane.** Engine + frameworks + scaffolding should total roughly the expected size. Wild deviation indicates accidental commits or missing content.
- [ ] **No `.DS_Store` or system junk** in the shipping zone
- [ ] **`.gitignore` is verified working** — `git status --ignored` shows expected exclusions
- [ ] **Spot-read three random engine chapter sections.** Tone consistent. Imperative voice. No emojis.
- [ ] **Spot-read three random Type definitions.** Each clearly defines its required fields, relation slots, mode.
- [ ] **VERSION.md, CHANGELOG.md, README.md, INSTALL.md** all reference the same version string
- [ ] **Tag the release.** If using git: tag matches folder convention.

## Major Bump Addendum (vX → vX+1 only)

Run this AFTER Sections 1-11 pass.

- [ ] **Migration guide written** — `MIGRATION-vX-to-vX+1.md` exists with explicit instructions for sphere cartridges built on the prior major version
- [ ] **Breaking changes enumerated** in CHANGELOG with prefix `BREAKING:`
- [ ] **`PLC` namespace bump** in Master_Schema (if Types added, removed, or had required-field changes) — explicit Decision Log entry
- [ ] **Backwards-compatibility path** documented or explicitly disclaimed
- [ ] **Operator notification mechanism** — UPDATE-PROMPT for this major bump explicitly warns about breaking changes before applying
- [ ] **Pilot upgrade** — at least one sphere from the prior major version successfully upgraded using the migration guide; resulting cartridge passes Section 7 spot-checks

## Reporting the checklist run

When this checklist runs, record the outcome in `_design-state.md`:

```markdown
## Shipping Checklist — v<version>

- Date run: <ISO 8601>
- Operator: [OPERATOR]
- Sections passed: <N>/11
- Failed items: <list, or "none">
- Sealed for ship: yes | no
- Tagged: <git tag or release reference>
```

A failed item is not a disaster — it's the system working. Fix the item, re-run the affected section, and re-record.

## Anti-patterns

- **Skipping the checklist for "a small minor bump."** Minor versions can still introduce schema or engine drift. The checklist is fast (< 1 hour). Run it.
- **Marking items "passed" without actually verifying.** The spot-checks exist because checking is the only signal that matters. Mark-then-verify is the way; verify-then-mark is the discipline.
- **Treating F-code regression as optional.** F1-F11 are the documented failure modes — they recur because they're systemic. Synthetic checks prevent them from shipping.
- **Tagging the release before the checklist completes.** The tag is the gate. If you tagged early and discovered a Section 9 failure, retract the tag.
