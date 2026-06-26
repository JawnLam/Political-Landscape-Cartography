---
Item_ID: plc-frameworks-readme
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "PLC Frameworks — README"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
AI_Instructions: ""
---

# PLC Frameworks

> **Substrate authorities and reference materials.** This directory holds (a) source documents PLC's methodology draws on, (b) lookup cards and craft layers for operators, and (c) the shipped Political Warfare Catalogue mirror.

## Contents

| Path | Type | Purpose |
|------|------|---------|
| `sources/` | source docs | Canonical PDFs and JSONs (ADAPT Loop Field Manual, Lam 2018 dissertation, OPC source, Catalogue source) |
| `political-warfare-catalogue/` | shipped Catalogue mirror | 782 tactics + 16 strategies + 84 clusters + 50 theorists + INDEX.json |
| `OPC-Assessment.md` | lookup | OPC v3.0 sphere diagnostic — 17 sections with 6-level hierarchical IDs |
| `ADAPT.md` | lookup card | 5-beat coaching frame quick reference |
| `ADAPT-as-consulting-engine.md` | craft layer | How operators deploy ADAPT inside PLC's RUN-CYCLE protocol |
| `dissertation-substrate.md` | deep reference | 19 categories + slash addressing + 9-type resource taxonomy from the dissertation |
| `4R.md` | mnemonic | Simplest summary of the coaching loop |
| `dissertation-table-3/` | substrate folder | ~100 granular Moves with PP/AA/B/C/Inc/Dec signature |
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

| File | Source available at ship | Status |
|------|--------------------------|--------|
| `political-warfare-catalogue/` | ✓ on disk | ✓ shipped |
| `sources/ADAPT-Loop-Field-Manual.pdf` | ✓ on disk | ✓ shipped |
| `OPC-Assessment.md` | operator instrument (not digitized) | scaffolded; operator populates from OPC v3.0 source |
| `ADAPT.md` | operator's commercial framework | scaffolded with 5-beat structure; operator confirms |
| `ADAPT-as-consulting-engine.md` | operator's craft knowledge | scaffolded; operator populates |
| `dissertation-substrate.md` | dissertation full text | scaffolded; operator populates from dissertation |
| `4R.md` | operator's mnemonic | scaffolded |
| `dissertation-table-3/` | dissertation Table 3 (~100 moves) | scaffolded with template; operator populates |
| `strategies/` | by-strategy/ inside Catalogue | scaffolded with pointer to Catalogue |
| `sources/Lam-2018-Pepperdine.pdf` | dissertation PDF | operator copies in at ship |
| `sources/OPC-v3.0.md` | OPC source | operator copies in at ship |

Items marked "operator populates" require the operator's proprietary source materials and cannot be drafted in an automated pass without violating F2 (fabrication prevention). The scaffolds preserve structure; the operator fills substance from the canonical sources at ship time.
