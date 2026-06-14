---
Item_ID: plc-readme
Item_Prototype: Fleeting
Title: "Political Landscape Cartography — README"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
AI_Instructions: ""
---

# Political Landscape Cartography (PLC)

A markdown-based **Operating Volume** for mapping and navigating organizational political landscapes. PLC is a structured methodology for either (a) a consultant working with a client principal, or (b) a principal self-coaching through a political environment they're operating in.

PLC ships ~782 documented tactics, 16 strategies, 84 thematic clusters, 50 scholarly theorists, and a interaction-cycle protocol (14 operational constituents per PLC's walk-through) grounded in the Lam 2018 Pepperdine dissertation on political capital. The work runs against a filesystem of markdown files — no database, no application server, no cloud lock-in. Your sphere lives in version-controllable text; the AI is the agent that reads it, reasons against the shipped substrate, and writes back disciplined updates.

## Who PLC is for

- **Consultants and coaches** working with executive principals on succession-period politics, change-leadership campaigns, board-relations strategy, coalition work, or any extended political engagement.
- **Principals themselves** running PLC as a self-coaching scaffold for their own political work, with the AI in a no-false-confidence advisor role.

PLC is NOT a generic decision tool, a stakeholder map, or a CRM. It's a discipline for *political reasoning under audit-trail constraints* — every cycle's tactical choices are logged with both alternatives-considered and ethical-evaluation gates; every suggested move ties back to a documented theorist; every cross-cycle pattern accumulates evidence rather than asserting itself.

## Quick start

Three paths in, depending on what you want:

### Path 1 — Deploy PLC for a real engagement

```bash
# Clone or download the OV folder
git clone https://github.com/<org>/Political-Landscape-Cartography-v1.0.git
cd Political-Landscape-Cartography-v1.0

# Read the AI bootstrap (start here for the AI)
cat AI-BOOTSTRAP.md

# Open a Claude Code (or compatible) session in this folder
# Tell the AI: "Open a new sphere using BOOTSTRAP-NEW-SPHERE.md"
# The AI will walk you through the 10 bootstrap questions
```

### Path 2 — Orient before deploying

Read in this order: `README.md` (this file) → `_plc-engine/01-WHAT-IS-PLC.md` → `_plc-engine/02-PRINCIPLES.md` → `OPERATOR-GUIDE.md` (or the consultant/principal variant for your mode). Total ~30 minutes of orienting reading before you decide whether PLC fits your work.

### Path 3 — Methodology study only

If you're researching the methodology without intent to deploy: start with `_plc-engine/01-WHAT-IS-PLC.md`, then `_plc-engine/04-SCHEMA.md` (the 16-prototype data model), then the dissertation source at `_frameworks/sources/`. The Catalogue at `_frameworks/political-warfare-catalogue/` is browsable independently of the Operating Volume protocol.

## How PLC is shipped

```
Political-Landscape-Cartography-v1.0/
├── README.md                          ← you are here
├── INSTALL.md                         ← installation + update mechanism
├── OPERATOR-GUIDE.md                  ← (or OPERATOR-GUIDE-CONSULTANT.md + OPERATOR-GUIDE-PRINCIPAL.md)
├── CONTRIBUTING.md                    ← what's in scope; what triggers a major version bump
├── UPDATE-PROMPT.md                   ← Convention 7 update mechanism
├── LICENSE.md
├── VERSION.md
├── CHANGELOG.md
├── AI-BOOTSTRAP.md                    ← AI entry point (consult on every session start)
├── BOOTSTRAP-NEW-SPHERE.md            ← new-sphere intake protocol (run once per sphere)
├── _plc-engine/                       ← engine layer (subject-agnostic; do not edit)
│   ├── 00-START-HERE.md
│   ├── 01-WHAT-IS-PLC.md
│   ├── 02-PRINCIPLES.md
│   ├── 03-SESSION-PROTOCOL.md
│   ├── 04-SCHEMA.md
│   ├── 05-WRITING-FOR-AI.md
│   ├── 06-STATE-PERSISTENCE.md
│   ├── 07-SHIPPING-CHECKLIST.md
│   ├── _templates/                    ← 22 starter scaffolds (1 per template variant)
│   └── _yaml/                         ← export schema + 5 redaction profiles
├── _Prototypes/                       ← 16 canonical Prototype definitions
│   └── PLC_*.md
├── _frameworks/                       ← shipped substrate (sourced material)
│   ├── sources/                       ← canonical PDFs + JSONs (ADAPT / dissertation / OPC / Catalogue source)
│   ├── ADAPT.md                       ← lookup card
│   ├── ADAPT-as-consulting-engine.md  ← craft layer
│   ├── dissertation-substrate.md      ← deep-schema reference
│   ├── 4R.md                          ← simplest mnemonic
│   ├── OPC-Assessment.md              ← 17-section sphere diagnostic
│   ├── dissertation-table-3/          ← ~100 granular Moves
│   ├── strategies/                    ← 16 strategy definition atoms
│   └── political-warfare-catalogue/   ← full Catalogue mirror
│       ├── INDEX.json
│       ├── tactics/                   ← 782 tactic files
│       ├── by-strategy/               ← 16 strategy facets
│       ├── by-cluster/                ← 84 cluster facets
│       └── by-theorist/               ← 50 theorist facets
├── _PATTERNS/                         ← shipped pattern seeds (6 families)
│   ├── stakeholder-archetypes/
│   ├── change-initiator-postures/
│   ├── opposition-postures/
│   ├── arc-dynamics/
│   ├── power-dynamics-themes/
│   └── ethical-dilemmas/
└── Spheres/                           ← your sphere cartridges live here
    └── <Your-Sphere-Name>/            ← one folder per sphere (organization)
        ├── _sphere-manifest.md
        ├── _sphere-state.md
        ├── _sphere-decisions.md
        ├── Principals/
        ├── Actors/
        ├── Campaigns/
        ├── Cycles/
        ├── OPC-Diagnostics/
        ├── Sessions/
        └── Patterns/                  ← sphere-specific pattern extensions
```

The **four content zones** (Convention 8):

- **Engine zone** (`_plc-engine/` + `AI-BOOTSTRAP.md` + `BOOTSTRAP-NEW-SPHERE.md` + `_Prototypes/`) — subject-agnostic protocol code. Updated by version bumps via UPDATE-PROMPT. Do not edit by hand.
- **Framework zone** (`_frameworks/` + `_PATTERNS/`) — shipped substrate. Updated by version bumps. Do not edit; extend in `_frameworks/*-extensions/`.
- **Sphere zone** (`Spheres/<Your-Sphere>/`) — your work. Wholly yours. Untouched by version bumps.
- **Scaffolding zone** (`_plc-engine/_templates/` + `_plc-engine/_yaml/`) — starter forms + export schemas. Updated by version bumps; sphere-local overrides go in `Spheres/<Sphere>/_USER.md`.

## Foundations

PLC stands on four substrate authorities (per [D14, D15]):

1. **Lam 2018 Pepperdine dissertation on political capital** — the grounded-theory foundation. 19 axial-coded categories; the interaction-cycle protocol (14 operational constituents per PLC's walk-through); the 9-type resource taxonomy (money / hard assets / credibility / attributes / legitimacy / information / access / title / tribe); slash-addressing notation; the Table 3 inventory of ~100 granular Moves. Lives in `_frameworks/sources/`.

2. **ADAPT Loop** — the commercialized 5-beat (Agenda → Decide → Act → Perceive → Track) the methodology author has been running in consulting practice. Layered atop the dissertation substrate as the operational coaching frame. Lives in `_frameworks/sources/` (42-page PDF) plus `_frameworks/ADAPT.md` (lookup card) and `_frameworks/ADAPT-as-consulting-engine.md` (craft layer).

3. **OPC Assessment v3.0** — the 17-section structured sphere-diagnostic with 6-level hierarchical IDs. Sections include power structure, stakeholders, dynamics, trajectory, harm & ethical evaluation (gates ETHICAL-ACCOUNTING), legitimate alternatives (gates ALTERNATIVES-AUDIT), practitioner self-assessment (consultant pre-engagement), advisor engagement politics (consultant pre-engagement). Lives in `_frameworks/OPC-Assessment.md` with source at `_frameworks/sources/`.

4. **Political Warfare Catalogue** — 782 tactics organized into 16 strategies and 84 thematic clusters, citing 50 theorists across the political-action canon. The defensible scholarly substrate from which PLC's tactical recommendations are sourced. Lives in `_frameworks/political-warfare-catalogue/` mirroring the source folder structure verbatim.

### The 50 theorists

PLC's tactical reasoning is grounded in 50 named theorists across game theory, sociology of power, organizational behavior, conflict theory, social psychology, strategic studies, and political philosophy. Each theorist is a first-class `PLC_Theorist` Item with citation count tied to the Catalogue's tactics.

The complete list with citation counts (highest → lowest), auto-generated from `_frameworks/political-warfare-catalogue/by-theorist/<theorist>.md` files. Counts represent the number of distinct tactics in the 782-tactic Catalogue that cite each theorist (or collaborative pair) as a primary intellectual source. Total citation count across the canon: **~1,980 cite-events** across 782 tactics (mean ~2.5 theorists per tactic).

Naming the canon publicly is intentional. Per [D15], the defensible scholarly substrate is part of the methodology's accountability — the operator can cite, the reader can verify, and the methodology can be evaluated against the explicit tradition it draws on rather than against unstated assumptions.

|       Theorist (or pair)       | Tactics cited |
|--------------------------------|---------------|
| Goffman                        |           226 |
| Cialdini                       |           158 |
| Akerlof                        |           155 |
| Kahneman                       |           146 |
| Schelling                      |           130 |
| Williamson                     |           127 |
| Tversky                        |           124 |
| Pfeffer                        |           117 |
| Festinger                      |            76 |
| Bourdieu                       |            68 |
| Kahneman/Tversky (joint)       |            65 |
| Asch                           |            45 |
| Granovetter                    |            42 |
| Foucault                       |            38 |
| Blumer                         |            37 |
| Arkes                          |            37 |
| Arkes & Blumer (joint)         |            36 |
| Olson                          |            30 |
| Spence                         |            28 |
| Ross                           |            25 |
| Thaler                         |            22 |
| Simon                          |            20 |
| Coase                          |            20 |
| Zeckhauser                     |            17 |
| Samuelson & Zeckhauser (joint) |            17 |
| Samuelson                      |            17 |
| Janis                          |            17 |
| Sun Tzu                        |            14 |
| Hovland                        |            14 |
| Staw                           |            13 |
| Sunstein                       |            10 |
| Machiavelli                    |            10 |
| Latané                         |            10 |
| Darley                         |            10 |
| Edelman                        |             8 |
| Darley & Latané (joint)        |             7 |
| Baron                          |             7 |
| Sherif                         |             6 |
| Greene                         |             6 |
| Rosen                          |             4 |
| Hershey                        |             4 |
| Baron & Hershey (joint)        |             4 |
| Lazear & Rosen (joint)         |             3 |
| Lazear                         |             3 |
| Milgram                        |             2 |
| Aronson                        |             2 |
| Sherif & Hovland (joint)       |             1 |
| Pindyck                        |             1 |
| Dixit-Pindyck (joint)          |             1 |
| Dixit                          |             1 |

The intellectual breadth spans: dramaturgy & impression management (Goffman); influence & social persuasion (Cialdini, Asch, Festinger, Milgram, Aronson, Sherif, Hovland); information economics & signaling (Akerlof, Spence, Coase, Williamson); behavioral decision theory & heuristics (Kahneman, Tversky, Thaler, Sunstein, Simon, Arkes, Blumer, Hershey, Baron, Staw, Ross, Janis); strategic behavior & game theory (Schelling, Sun Tzu, Machiavelli, Greene); organizational power & resource dependence (Pfeffer, Olson); sociology of power & habitus (Bourdieu, Foucault); network sociology (Granovetter); symbolic politics (Edelman); pluralistic ignorance & bystander effects (Darley, Latané); tournament theory & promotion economics (Lazear, Rosen); intertemporal & status-quo decision (Samuelson, Zeckhauser); real-options & decision-under-uncertainty (Dixit, Pindyck).

Each theorist's full citation list with tactic-by-tactic detail lives at `_frameworks/political-warfare-catalogue/by-theorist/<theorist>.md`.

## What PLC requires of the AI

PLC is designed to be run with **Claude Code** or a compatible agentic coding environment. The AI:

- Reads `AI-BOOTSTRAP.md` on every session start
- Loads Tier 1 engine chapters and current sphere state into context
- Asks one question at a time during intake (no multi-bullet questionnaires — per `02-PRINCIPLES.md` P3)
- Refuses to fabricate theorists, tactics, or actor identities (per P4, P5)
- Runs the mandatory ALTERNATIVES-AUDIT and ETHICAL-ACCOUNTING gates inside every RUN-CYCLE; logs any overrides with operator justification
- Writes back disciplined updates with reciprocal-update integrity across the 24 named relations
- Treats Mode E files as immutable (closed cycles, shipped Catalogue, sealed retrospectives)

## What PLC does NOT do

PLC is honest about its boundary. It is not the right form for:

- **Tactical decisions inside operational management** — political reasoning is about durable disposition shifts, not weekly operating decisions
- **HR or compliance investigations** — different audit standards apply; PLC's gates are scholarly-canonical, not legal
- **Personal-relationship counseling** — family dynamics that don't manifest in organizational politics are out of scope (and explicitly so in the engagement charter)
- **One-shot decisions with no follow-through** — the interaction-cycle protocol (14 constituents) assumes recursive cycling and longitudinal pattern accumulation

See `_plc-engine/01-WHAT-IS-PLC.md` § "When PLC is the right form / not" for the full boundary.

## Getting help

- **Operator guide:** `OPERATOR-GUIDE.md` (or consultant/principal variant) — symptom → cause → fix
- **Contributing or extending:** `CONTRIBUTING.md`
- **Update mechanism:** `UPDATE-PROMPT.md`
- **Methodology questions:** open an issue at the project repo, or contact the methodology author

## Version

See `VERSION.md`. PLC ships under semantic versioning: major bumps introduce schema-breaking changes; minor bumps add Prototypes/Templates/Catalogue extensions or substantively revise engine chapters; patch bumps correct documentation or template typos. The CHANGELOG documents every release.

## License

See `LICENSE.md`.
