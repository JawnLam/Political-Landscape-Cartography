---
Item_ID: plc-frameworks-dissertation-table-3-readme
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Dissertation Table 3 — Granular Moves"
Date_Added: 2026-06-13
Date_Modified: 2026-07-24
Needs_Processing: false
AI_Instructions: ""
---

# Dissertation Table 3 — Granular Moves

> **Scaffolded folder for the 148 granular Moves from the Lam 2018 dissertation Table 3.** Each Move is a `PLC_Move` Item with the PP/AA/B/C/Inc/Dec 6-field signature. Operator populates at ship time from the dissertation source.

> **v1.2 update:** the complete row inventory now exists as **`Table-3-Manifest.md`** — all **148** Table 3 rows transcribed with Option / Consideration / Effect and LSPI component mapping (P/b±, P/c±, Adv/b±, Adv/c±, varied). The manifest is the base for the provenance cross-walk (upgrade-plan WS4 **pass 6**, complete 2026-07-24 — results in `Table-3-Manifest.md` § Cross-walk results); authoring the remaining full Move files stays on the ROADMAP backlog (3 of 148 authored). Note the dissertation yields 148 rows, not the "~100" estimate used at v1.0 — treat any surviving "~100" as stale.

## What lives here

Per D14 + D20, the dissertation Table 3 catalog of 148 granular Moves ships as first-class `PLC_Move` Items. These are the elemental atoms; the higher-order Tactics in `_frameworks/political-warfare-catalogue/tactics/` are composed of these Moves via the reciprocal `plc_Composed_Of` ↔ `plc_Appears_In_Tactics` relation.

## File naming

`Move-<NNN>.md` where `<NNN>` is the 3-digit Move number from the dissertation's Table 3 enumeration.

## Template

Use `_plc-engine/_templates/PLC_Move_TEMPLATE.md` as the starter scaffold for each Move file.

## How to populate

For each of the 148 Moves in dissertation Table 3 (row numbers and signatures are in `Table-3-Manifest.md`):

1. Copy the template to `Move-<NNN>.md`
2. Set `plc_Move_Number` to the dissertation's Move number
3. Set `plc_Move_Name` to the dissertation's name
4. Populate `plc_Move_Signature` with the PP/AA/B/C/Inc/Dec 6-field signature from the dissertation
5. Populate `plc_Resource_Types_Required` from the 9-type taxonomy
6. Populate the body sections (Signature explanation; Description; When to Use; When Not to Use)
7. Wire reciprocal relations to any Tactics in `_frameworks/political-warfare-catalogue/tactics/` that compose this Move (update both sides: `plc_Appears_In_Tactics` here, `plc_Composed_Of` on the Tactic file)

## Ship-time population status

**Substrate-pending.** 3 of 148 Move files are authored (`Move-001`–`Move-003`); the remaining 145 have not been drafted. Each Move requires content from the dissertation's Table 3 source. Operator populates at SHIP-PREP from the dissertation PDF. All 148 rows are transcribed in `Table-3-Manifest.md`, and per-tactic corpus provenance is in `../political-warfare-catalogue/INDEX-lspi.json` (`provenance.lam_table3_refs`) — 127 of 148 rows have a corpus descendant; the 21 that do not are listed in the manifest.

## Cross-references

- Move Prototype: `_types/PLC_Move.md`
- Move Template: `_plc-engine/_templates/PLC_Move_TEMPLATE.md`
- Reciprocal Tactic catalog: `_frameworks/political-warfare-catalogue/tactics/`
- Dissertation source: `_frameworks/sources/Lam-2018-Pepperdine.pdf`
- Substrate reference: `_frameworks/dissertation-substrate.md`
