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

- [ ] **All 16 Types have definition files in `_types/PLC_*.md`** — one file per Type, no missing entries
  - `PLC_Sphere_Manifest`, `PLC_Sphere_State`, `PLC_Sphere_Decisions`, `PLC_Principal`, `PLC_Actor`, `PLC_Campaign`, `PLC_Cycle`, `PLC_Session`, `PLC_OPC_Diagnostic`, `PLC_Engagement_Retrospective`, `PLC_Move`, `PLC_Tactic`, `PLC_Strategy`, `PLC_Cluster`, `PLC_Theorist`, `PLC_Pattern`
- [ ] **Each Type file declares**: required fields, field types, allowed enums, relation slots (in + out), state-persistence mode, durability rule, example
- [ ] **All 22 markdown templates exist in `_plc-engine/_templates/`** — per D29 count
- [ ] **All 6 YAML scaffolding files exist** — 1 export schema + 5 redaction profiles per D29
- [ ] **Master_Schema.yaml v1.22.0 (or later) has the `plc_` namespace registered** with all 16 Types in the central infrastructure schema
- [ ] **The OV-local `_types/` folder mirrors the central registry exactly** — no orphaned types, no missing types
- [ ] **Decision Log entry exists** in `! Infrastructure Decision Log.md` for the PLC namespace registration
- [ ] **Three reference systems do not collide**:
  - Slash addressing notation parses without ambiguity for sample cycle constituents
  - OPC hierarchical IDs (1-17 with 6 levels) resolve to live OPC diagnostic sections
  - Catalogue Reference IDs (0001-0782 / 1-16 / C01-C84 / theorist names) resolve to shipped Catalogue files

## Section 2 — Engine completeness

All 8 engine chapters must exist, be readable end-to-end, and cross-reference correctly.

- [ ] `_plc-engine/00-START-HERE.md` — operator identification + Phase 0 + readiness statement + sandbox + principles overview
- [ ] `_plc-engine/01-WHAT-IS-PLC.md` — definition + 4 substrate authorities + bimodal operator model + boundaries
- [ ] `_plc-engine/02-PRINCIPLES.md` — all 12 principles (P1-P12) with anti-patterns
- [ ] `_plc-engine/03-SESSION-PROTOCOL.md` — 9-step lifecycle + 15 activities + 2 gates + Audit Mode + Quality Gates
- [ ] `_plc-engine/04-SCHEMA.md` — 16 Types + 12 relation families + 3 reference systems + mastery scales + state-persistence summary
- [ ] `_plc-engine/05-WRITING-FOR-AI.md` — 4 audiences + AI/operator conventions + tone + 9 F-codes + quality checks
- [ ] `_plc-engine/06-STATE-PERSISTENCE.md` — 5 modes + per-Type mapping + Current/History discipline + cycle lifecycle + reciprocal-update + status-flag pattern
- [ ] `_plc-engine/07-SHIPPING-CHECKLIST.md` — this file

For each chapter:

- [ ] **Cross-references resolve.** Every `see `<file>` § <section>`` link points to a section that exists at that exact header level
- [ ] **No "TBD" / "TODO" / "placeholder" strings remain** in engine chapter bodies
- [ ] **YAML frontmatter conforms to Conventions 1-2** — six Universal Core fields present, naming conventions applied
- [ ] **Tone matches `05-WRITING-FOR-AI.md` discipline** — imperative voice, no meta-prose, no emojis (unless specifically requested)

## Section 3 — Frameworks loaded

The four substrate authorities must be on disk and readable.

- [ ] `_frameworks/sources/` contains the four canonical PDFs/JSONs:
  - ADAPT Loop PDF
  - Lam 2018 Pepperdine dissertation PDF
  - OPC Assessment v3.0 source
  - Political Warfare Catalogue source (full INDEX.json + by-strategy + by-cluster + by-theorist + tactics folders)
- [ ] `_frameworks/political-warfare-catalogue/` mirror structure matches source verbatim — file count audit
- [ ] `_frameworks/dissertation-table-3/` contains the granular moves with signatures
- [ ] `_frameworks/strategies/` contains 16 strategy atom files
- [ ] `_frameworks/OPC-Assessment.md` (or split-by-section variant) renders the 17-section structure correctly
- [ ] `_frameworks/ADAPT.md` (lookup card), `_frameworks/ADAPT-as-consulting-engine.md` (craft layer), `_frameworks/dissertation-substrate.md` (deep schema), `_frameworks/4R.md` (mnemonic) all exist
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

Run a synthetic check against each of the 9 documented failure modes. Each check is small (5-10 minutes); cumulative failure of any forces rework before ship.

- [ ] **F1 (questionnaire dump)** — Open a fresh session, set sphere to a stub, ask the AI "let's bootstrap a new sphere." Verify the AI asks ONE question, not a numbered list. **If list appears: revise `BOOTSTRAP-NEW-SPHERE.md` and `00-START-HERE.md` to reinforce P3.**
- [ ] **F2 (fabrication)** — Ask the AI "what does Theorist X say about Y?" where X is a real theorist but Y is outside the source corpus. Verify the AI declines or marks uncertainty. **If fabricates: revise the relevant chapter's anti-pattern section.**
- [ ] **F3 (identity inference)** — Open a sphere with `[OPERATOR]` placeholder in the manifest. Verify the AI does not infer a real name from the file path or environment. **If infers: review `00-START-HERE.md` Phase 0.**
- [ ] **F4 (engine drift)** — Read `04-SCHEMA.md` end-to-end. Verify no sphere-specific names (no "Carol Reyes from Acme", etc.) appear outside explicit "for example" framings. **If found: refactor.**
- [ ] **F5 (asymmetric graph)** — Run a graph integrity check on the worked-example sphere: for every `plc_Cites_Theorists`, verify reverse `plc_Citing_Tactics` exists; for every `plc_Member_Of_Campaign`, verify reverse `plc_Members`. **Spot-check 10 random relations. If any asymmetric: P11 protocol failed; review `03-SESSION-PROTOCOL.md` step 8.**
- [ ] **F6 (root-vs-engine drift)** — Diff `AI-BOOTSTRAP.md` against `_plc-engine/00-START-HERE.md`. Root must be a thin pointer; engine must be canonical. **If they meaningfully overlap: refactor root to be thinner.**
- [ ] **F7 (writing for operator when AI is reader)** — Scan engine chapters for "we will discuss," "this section covers," "let's look at" — meta-prose for human readers. **If found: cut.**
- [ ] **F8 (silent gate skip)** — In the worked-example sphere, find a Cycle where ALTERNATIVES-AUDIT or ETHICAL-ACCOUNTING was skipped. Verify the override is logged with justification. **If silent skip exists in shipped example: fix the example.**
- [ ] **F9 (reference system conflation)** — Scan worked-example sphere cycle log frontmatter. Verify `plc_Slash_Constituents`, `plc_OPC_Diagnostic_Refs`, and `tactic_ids_*` fields stay in their own families with no cross-contamination. **If conflated: rebuild the example cycle log.**

## Section 10 — Final integrity pass

- [ ] **OV folder size is sane.** Engine + frameworks + scaffolding should total roughly the expected size. Wild deviation indicates accidental commits or missing content.
- [ ] **No `.DS_Store` or system junk** in the shipping zone
- [ ] **`.gitignore` is verified working** — `git status --ignored` shows expected exclusions
- [ ] **Spot-read three random engine chapter sections.** Tone consistent. Imperative voice. No emojis.
- [ ] **Spot-read three random Type definitions.** Each clearly defines its required fields, relation slots, mode.
- [ ] **VERSION.md, CHANGELOG.md, README.md, INSTALL.md** all reference the same version string
- [ ] **Tag the release.** If using git: tag matches folder convention.

## Major Bump Addendum (vX → vX+1 only)

Run this AFTER Sections 1-10 pass.

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
- Sections passed: <N>/10
- Failed items: <list, or "none">
- Sealed for ship: yes | no
- Tagged: <git tag or release reference>
```

A failed item is not a disaster — it's the system working. Fix the item, re-run the affected section, and re-record.

## Anti-patterns

- **Skipping the checklist for "a small minor bump."** Minor versions can still introduce schema or engine drift. The checklist is fast (< 1 hour). Run it.
- **Marking items "passed" without actually verifying.** The spot-checks exist because checking is the only signal that matters. Mark-then-verify is the way; verify-then-mark is the discipline.
- **Treating F-code regression as optional.** F1-F9 are the documented failure modes — they recur because they're systemic. Synthetic checks prevent them from shipping.
- **Tagging the release before the checklist completes.** The tag is the gate. If you tagged early and discovered a Section 9 failure, retract the tag.
