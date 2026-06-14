---
Item_ID: plc-frameworks-strategies-readme
Item_Prototype: Fleeting
Title: "Strategies — Operator Notes"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
AI_Instructions: ""
---

# Strategies — Operator Notes

> **The 16 strategy atoms ship as facet files inside the Catalogue mirror, not as separate Items here.** This folder holds operator notes about strategy deployment patterns that complement the Catalogue's strategy facets.

## Where the strategy atoms live

The 16 strategy atoms per D14 ship inside the Political Warfare Catalogue mirror at:

```
_frameworks/political-warfare-catalogue/by-strategy/
├── 01-pure-enhancement.md     — Strategy #1
├── 02-pure-facilitation.md    — Strategy #2
├── 03-pure-undermining.md     — Strategy #3
├── ...                        — through Strategy #16
└── 16-full-spectrum.md        — Strategy #16
```

Each Catalogue strategy facet shows:

- Strategy number + name
- Lever combination notation (e.g., `B(X)↑`, `C(X)↓ + B(Y)↓`, `B(X)↑ + C(X)↓ + B(Y)↓ + C(Y)↑`)
- List of Tactics that deploy the strategy (with `specific` vs `generic` usage notes)

The strategy facets are Mode E shipped substrate per the PLC_Strategy Prototype durability mode.

## What goes in this folder

Operator-extended notes about strategy deployment that DON'T modify the shipped strategy atoms:

- **Strategy deployment patterns** — when each strategy has worked / failed across the operator's engagement portfolio
- **Strategy combinations** — how strategies layer in practice (rare; most cycles use one strategy as the meta-frame)
- **Cross-engagement strategy frequency** — which strategies the operator has deployed most often; which they've never deployed; what that pattern reveals about engagement portfolio bias
- **Strategy-vs-archetype matching** — which strategies fit which stakeholder archetypes; which create conflicts

These notes are operator's craft layer; they don't ship with PLC at v1.0.0 because they don't exist yet (the operator accumulates them through engagement experience).

## Strategy lookup pattern

For an operator looking up a specific strategy during MOVE-LOOKUP work:

1. Read `_frameworks/political-warfare-catalogue/by-strategy/<N>-<slug>.md` for the canonical strategy + member tactics list
2. Read individual tactic files from the strategy's tactic list
3. (Optional) Read this folder's operator-notes file for cross-engagement deployment patterns

## Operator's note (placeholder until populated)

> Operator notes accumulate over engagements. Empty at v1.0.0; populates as the engagement portfolio grows.

## Cross-references

- Strategy Prototype: `_Prototypes/PLC_Strategy.md`
- Strategy Template: `_plc-engine/_templates/PLC_Strategy_TEMPLATE.md`
- Catalogue strategy facets (canonical): `_frameworks/political-warfare-catalogue/by-strategy/`
- Catalogue tactics: `_frameworks/political-warfare-catalogue/tactics/`
