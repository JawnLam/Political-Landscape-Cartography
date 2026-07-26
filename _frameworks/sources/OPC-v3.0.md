---
Item_ID: plc-source-opc-v3
type: Fleeting
timestamp: "2026-07-24T00:00:00Z"
title: "Source Pointer — Organizational Political Cartography v3.0"
Date_Added: 2026-07-24
Date_Modified: 2026-07-24
Needs_Processing: false
AI_Instructions: "A source POINTER, not the source. OPC v3.0 is not distributed with this volume; `_frameworks/OPC-Assessment.md` is PLC's in-volume expression of it. Never cite this file as the source text."
---

# Source pointer — Organizational Political Cartography (OPC) v3.0

**Substrate authority 3.** OPC is the Methodology Author's own diagnostic instrument. The full v3.0 document is **not distributed with this volume**.

| | |
|---|---|
| Author | Cong "Jawn" Lam |
| Status in this volume | referenced, not shipped |
| Operator-local drop path | `_frameworks/sources/OPC-v3.0-full.pdf` (gitignored) |
| How to obtain | request directly from the Methodology Author |

## What PLC ships instead

`_frameworks/OPC-Assessment.md` — the in-volume expression of the 17-section structure, sufficient to run OPC-DIAGNOSE and to answer the section references the engine makes.

## Sections the engine depends on by name

These are the OPC sections PLC's machinery actually reads. If any of them is unclear in the in-volume expression, that is a gap worth closing in `OPC-Assessment.md` — not a reason to guess from the missing source.

| Section | What depends on it |
|---|---|
| § 2.4 political intensity | the depth decoder's bias term `b` in `08-ESTIMATION.md` — an adversarial-intensity reading is what keeps `b` from defaulting to paranoia |
| § 4.3 blind-spot audit | an input to the ESTIMATE differential, not a terminal checklist |
| § 9 monitoring | an input to the detection loop |
| § 11 harm scopes | the ETHICAL-ACCOUNTING gate |
| § 13 patterns | the seed set for `_PATTERNS/` |
| § 15 constructive approaches | the ALTERNATIVES-AUDIT gate |
| §§ 16–17 practitioner and engagement politics | PRACTITIONER-ASSESSMENT |

## The discipline

Same rule as the other undistributed sources: if a claim about OPC is not supported by `_frameworks/OPC-Assessment.md`, the honest answer is that the source is not in this volume. Do not reconstruct section content from its section number.
