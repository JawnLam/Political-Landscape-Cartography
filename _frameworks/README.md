---
Item_ID: plc-frameworks-readme
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "PLC Frameworks — README"
Date_Added: 2026-06-13
Date_Modified: 2026-07-24
Needs_Processing: false
AI_Instructions: ""
---

# PLC Frameworks

> **Substrate authorities and reference materials.** This directory holds (a) source documents PLC's methodology draws on, (b) lookup cards and craft layers for operators, (c) the shipped Political Warfare Catalogue mirror, and (d) the Mode C mirrors of the LSPI Formal Foundation (`lspi/`).

## Contents

| Path | Type | Purpose |
|------|------|---------|
| `sources/` | source docs | Access notes and request stubs for the substrate sources — see the shipping-status table below for what is actually on disk |
| `political-warfare-catalogue/` | shipped Catalogue mirror | 782 tactics + 16 strategies + 83 clusters + the `ORIGINAL` sentinel + 50 theorists + `INDEX.json` + the `INDEX-lspi.json` LSPI facet sidecar |
| `lspi/` | Mode C mirror folder | **Substrate authority #5** — the LSPI Formal Foundation build folder mirrored: `LSPI-Foundations.md`, `Matrix-Estimation-Layer-v0.4.md`, `Reflexivity-Layer-v0.1.md`, `Tactic-Corpus-LSPI-Integration-Spec.md`, `Content-Audit-v0.3.md`, `Resource-Detection-Slot-Analysis.md`. Mirrors are **Mode C: never edit here** — changes originate upstream. Orientation, runbook and grounding notes (`_lspi-README.md`, `WS4-RUNBOOK.md`, `observation-model-grounding.md`) are PLC-authored and editable |
| `OPC-Assessment.md` | lookup | OPC v3.0 sphere diagnostic — 17 sections with 6-level hierarchical IDs |
| `ADAPT.md` | lookup card | 5-beat coaching frame quick reference |
| `ADAPT-as-consulting-engine.md` | craft layer | How operators deploy ADAPT inside PLC's RUN-CYCLE protocol |
| `dissertation-substrate.md` | deep reference | 19 categories + slash addressing + 9-type resource taxonomy from the dissertation |
| `4R.md` | mnemonic | Simplest summary of the coaching loop |
| `4R-coaching-script.md` | craft layer | The deployable 4R walk-through, voiced for executive register |
| `reflexivity-frontier.md` | **frontier** (`frontier: true`) | PLC-facing summary of the level-ℓ signaling frontier — orientation only; **nothing in it enters RUN-CYCLE mechanics, gates or templates** |
| `dissertation-table-3/` | substrate folder | **148** granular Moves with PP/AA/B/C/Inc/Dec signature — full row manifest in `Table-3-Manifest.md` |
| `strategies/` | substrate folder | Operator notes on the 16 strategy atoms — primary atoms live in `political-warfare-catalogue/by-strategy/` |

## How PLC uses these

- **At session start** the AI consults `OPC-Assessment.md` and `ADAPT.md` as load-on-demand Tier 2 references per `_plc-engine/00-START-HERE.md` Phase 0
- **During RUN-CYCLE**:
  - ALTERNATIVES-AUDIT § 15 walk uses OPC § 15
  - ETHICAL-ACCOUNTING § 11 walk uses OPC § 11
  - Tactics surface from `political-warfare-catalogue/` via MOVE-LOOKUP activity
  - Theorist citations flow through `political-warfare-catalogue/by-theorist/`
- **Across cycles** the dissertation substrate grounds the interaction-cycle protocol (14 constituents) and the recursive Interest tree mechanics
- **For coaching** ADAPT operates at the principal-coaching layer above the PLC political-landscape layer

## Source provenance

The methodology authorship credit is fixed per `LICENSE.md`:

- **Lam 2018 Pepperdine dissertation on political capital** — Methodology Author's separately-copyrighted academic work; incorporated by author's permission
- **ADAPT Loop** — Methodology Author's separately-developed commercial framework; incorporated by author's permission
- **OPC Assessment v3.0** — Methodology Author's separately-developed diagnostic instrument
- **Political Warfare Catalogue** — Methodology Author's curated scholarly substrate organizing 50 cited theorists; theorists' primary works remain under their own copyrights, used under academic fair-use citation only

## Ship-time population status

*Status is stated against what is actually on disk in this volume. A file named in a cross-reference but absent from the tree is recorded as **referenced, not shipped** — never as shipped.*

| File | Source available at ship | Status |
|------|--------------------------|--------|
| `political-warfare-catalogue/` | ✓ on disk | ✓ **present** — 782 tactic files, facet folders, `INDEX.json`, `INDEX-lspi.json` |
| `lspi/` | ✓ upstream build folder | ✓ **present** — 6 Mode C mirrors + 3 PLC-authored notes. The two reference diagrams (`Figure-3-…`, `Figure-4-…`) are named upstream and are **not mirrored** into this volume |
| `reflexivity-frontier.md` | derived from the mirrored frontier spec | ✓ **present** — frontier summary, non-operational |
| `OPC-Assessment.md` | operator instrument (not digitized) | scaffolded; operator populates from OPC v3.0 source |
| `ADAPT.md` | operator's commercial framework | scaffolded with 5-beat structure; operator confirms |
| `ADAPT-as-consulting-engine.md` | operator's craft knowledge | scaffolded; operator populates |
| `dissertation-substrate.md` | dissertation full text | scaffolded; operator populates from dissertation |
| `4R.md` / `4R-coaching-script.md` | operator's mnemonic + craft knowledge | ✓ **present** |
| `dissertation-table-3/` | dissertation Table 3 (148 rows) | **partial** — `Table-3-Manifest.md` transcribes all 148 rows; 3 of 148 full Move files authored (`Move-001`…`003`); the remaining 145 are ROADMAP backlog |
| `strategies/` | by-strategy/ inside Catalogue | **gap** — contains `_README.md` only. `07-SHIPPING-CHECKLIST.md` expects 16 strategy atom files here; the canonical atoms ship inside the Catalogue at `political-warfare-catalogue/by-strategy/`. Recorded in `strategies/_README.md` |
| `sources/Lam-2018-Pepperdine.md` | ✓ on disk | ✓ **present** — the access/request note, **not** the dissertation text |
| `sources/Lam-2018-Pepperdine.pdf` | dissertation PDF (operator's own copy) | **referenced, not shipped** — gitignored by design; operator places their authorized copy |
| `sources/ADAPT-Loop-Field-Manual.pdf` | operator's commercial framework | **referenced, not shipped** — no such file in `sources/` |
| `sources/OPC-v3.0.md` | OPC source | **referenced, not shipped** — no such file in `sources/` |
| Catalogue JSON source (`99_assembled_output.json`) | upstream corpus build | **referenced, not shipped** — the markdown layer + indexes are the shipped form |

`sources/` currently contains exactly one file: `Lam-2018-Pepperdine.md`. Everything else the cross-references name is an operator-supplied or upstream artifact that this volume points at rather than carries.

Items marked "operator populates" require the operator's proprietary source materials and cannot be drafted in an automated pass without violating F2 (fabrication prevention). The scaffolds preserve structure; the operator fills substance from the canonical sources at ship time.
