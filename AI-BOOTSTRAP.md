---
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
Item_ID: plc-ai-bootstrap
title: "Political Landscape Cartography — AI Bootstrap"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
doc_type: bootstrap
audience: ai
read_order: 0
last_updated: 2026-06-13
---

# Political Landscape Cartography — AI Bootstrap (Read Me First)

> **If you're a human reading this:** this file is the AI's reading list, not yours. For an overview see `README.md`; for setup see `INSTALL.md`; for day-to-day operation see `OPERATOR-GUIDE.md`.

> **If you're an AI assistant (Claude, Gemini, ChatGPT, or any capable model):** the user has pointed you at a Political Landscape Cartography folder. Read this file in full, then complete the bootstrap below, then respond to the user.

You are inside a Political Landscape Cartography (PLC) folder. The user has likely said something like *"help me open a new sphere for my client at Acme Corp"*, or *"continue my work on the Acme sphere"*, or *"audit my Beta sphere"*, or *"explain what Political Landscape Cartography is."*

PLC is a markdown-based operating volume for **mapping and navigating the political landscape of organizations**. It operationalizes (1) the ADAPT Loop framework, (2) the Lam 2018 dissertation on political capital, (3) the Organizational Political Context Assessment (OPC), and (4) the 782-tactic Political Warfare Catalogue. Used by consultants advising senior-executive clients AND by senior executives self-coaching.

Your job is one of:

1. **Open a new sphere** (the bootstrap-new-sphere flow — opens a new cartridge here, walks the operator through pre-engagement protocol + 10 clarifying questions, populates initial state)
2. **Continue an existing sphere in progress** (read the sphere's backbone files; propose the next session activity)
3. **Audit an existing sphere** elsewhere on disk (structural review against PLC principles; surface gaps; propose fixes)
4. **Explain the PLC concept** (orientation only; no sphere needed)

`{ROOT}` in any instruction below means the absolute path to this PLC folder.

## Phase 0: Pre-flight (mandatory before first response)

### 1. Mandatory reads (Tier 1 — always before first user-facing message)

From `{ROOT}/_plc-engine/`:

1. `00-START-HERE.md` — AI entry point; canonical read protocol
2. `01-WHAT-IS-PLC.md` — definition; substrate authorities; bimodal operator framing
3. `02-PRINCIPLES.md` — the operating principles (12 numbered)
4. `03-SESSION-PROTOCOL.md` — the 15 session activities; gates inside RUN-CYCLE; mode-aware fork
5. `05-WRITING-FOR-AI.md` — tone discipline (peer / substantive / minimal hedging / no filler / mode-aware no-false-confidence in principal-self mode)

From `{ROOT}/_frameworks/`:

6. `ADAPT.md` — 5-beat lookup card for the ADAPT framework
7. `OPC-Assessment.md` (or split per section) — 17-section sphere-diagnostic + practitioner self-assessment + advisor engagement politics

Plus, if an active sphere is in play:

8. `<Sphere>/_sphere-manifest.md`
9. `<Sphere>/_sphere-state.md` (read the `## Decided` and `## OPC Current Summary` rollup sections in full)
10. `<Sphere>/_sphere-decisions.md` (skim recent entries)
11. The most recent 1-2 files in `<Sphere>/Sessions/`

Plus, if present at root: `{ROOT}/_USER.md`.

"Skim" is not a valid mode for the Tier 1 set above (excluding the decisions log and OPC, which can be navigated as needed).

### 2. Mandatory environment checks

- **Folder writability.** Verify you can write to `{ROOT}/<Sphere>/Sessions/`, `<Sphere>/_sphere-state.md`, `<Sphere>/Cycles/`, and `<Sphere>/Diagnostics/`. If read-only, declare **sandbox mode** in the readiness statement. **Sandbox mode degrades the OV's defining multi-session statefulness — name it loudly, do not absorb it silently.**
- **Existing spheres.** List the subfolders at `{ROOT}/` (excluding `_plc-engine/`, `_frameworks/`, `_types/`, `Example-Sphere-*`, and dot/underscore-prefixed). Each non-example subfolder is a candidate active sphere.
- **Mode determination.** If continuing an existing sphere, read `plc_Operator_Mode` from the sphere manifest. If opening a new sphere, CQ2 of `BOOTSTRAP-NEW-SPHERE.md` asks this explicitly.

### 3. Decide the path

- **If the user named an existing sphere OR is continuing one in progress** → read that sphere's backbone files; check `plc_Engagement_Stage`; propose a session activity from the 15 standalone activities in `03-SESSION-PROTOCOL.md`. **If consultant mode AND `plc_Engagement_Stage = pre_engagement`, the AI MUST run PRACTITIONER-ASSESSMENT (OPC § 16) BEFORE any other activity** — this is hard-precedence discipline; no override without explicit operator command.
- **If the user wants to open a NEW sphere** → route to `BOOTSTRAP-NEW-SPHERE.md`. Open a new sphere cartridge. Walk the mode-aware pre-engagement protocol (consultant: § 16 → § 17 BEFORE CQ1; principal-self: § 16 optional but recommended), then CQ1 through CQ10 conversationally.
- **If the user wants to audit an EXISTING sphere** elsewhere on disk → ask for the path. Route to the audit protocol in `_plc-engine/03-SESSION-PROTOCOL.md` § Audit Mode.
- **If the user wants conceptual orientation only** ("what is Political Landscape Cartography?") → answer directly from `_plc-engine/01-WHAT-IS-PLC.md`. No sphere needed.

### 4. Readiness statement

Two to four sentences. State which path you took. **Cite one non-guessable thing.**

- **Existing-sphere path:** name one specific fact from sphere state — current engagement stage, most recent locked decision in `_sphere-decisions.md`, or a named open thread.
- **New-sphere or orientation path:** name one specific operating principle from `_plc-engine/02-PRINCIPLES.md` that you will enforce in the first turn (e.g., *"I'll ask one CQ at a time per F1"* or *"I'll use placeholders for the principal's name per P7 until you confirm it"*).

A statement that confidently confirms *"I've read the engine"* without citing a sphere fact or a named principle is the operator's diagnostic that the reads did not actually happen. Re-prompt with: *"Read `AI-BOOTSTRAP.md` in full before responding."*

If you cannot complete pre-flight (missing files, ambiguous user message, read-only substrate), say so and ask what you need.

## What's in this folder

```
{ROOT}/
├── README.md, INSTALL.md, OPERATOR-GUIDE.md, CONTRIBUTING.md   ← human-facing docs
├── AI-BOOTSTRAP.md                                              ← this file
├── BOOTSTRAP-NEW-SPHERE.md                                      ← the new-sphere protocol
├── UPDATE-PROMPT.md                                             ← AI-assisted update workflow
├── VERSION.md, CHANGELOG.md, LICENSE.md, .gitignore
├── _USER.md.template (and possibly _USER.md if operator created one; gitignored)
├── _plc-engine/                                                 ← your operating manual
│   ├── 00-START-HERE.md
│   ├── 01-WHAT-IS-PLC.md
│   ├── 02-PRINCIPLES.md
│   ├── 03-SESSION-PROTOCOL.md
│   ├── 04-SCHEMA.md
│   ├── 05-WRITING-FOR-AI.md
│   ├── 06-STATE-PERSISTENCE.md
│   ├── 07-SHIPPING-CHECKLIST.md
│   ├── _templates/                                              ← 22 markdown + 6 YAML scaffolds
│   ├── redaction-profiles/                                      ← 5 audience-aware YAML profiles
│   └── _meta/
├── _types/                                                 ← 16 PLC_*.md Type definitions
├── _frameworks/                                                 ← reference: ADAPT, OPC, dissertation, Catalogue
│   ├── ADAPT.md
│   ├── OPC-Assessment.md
│   ├── political-warfare-catalogue/                             ← 782 tactics, 16 strategies, 84 clusters, 50 theorists
│   └── sources/                                                 ← canonical PDFs/JSONs
├── Example-Sphere-Acme-Corp/                                    ← shipped worked example
└── <Sphere>/                                                    ← zero or more operator-extended spheres
    ├── _sphere-manifest.md, _sphere-state.md, _sphere-decisions.md
    ├── _PRINCIPALS/<principal>.md
    ├── Actors/<actor>/_baseline.md + _view-<principal>.md
    ├── Campaigns/, Cycles/, Sessions/, Diagnostics/, Exports/
    └── _PATTERNS/ (operator-extensible)
```

## Core principles (apply to every engagement)

These come from `_plc-engine/02-PRINCIPLES.md` in full; the short version:

1. **State lives in files.** Read sphere state at session start; write to it at session end.
2. **One question at a time.** Especially during sphere intake (CQ1-CQ10). Never dump a multi-bullet questionnaire.
3. **Never invent.** If unsure whether a tactic, theorist, person, or fact is real, say so.
4. **Never fabricate identity.** Don't infer the principal's or operator's name from username strings, file paths, or git config. Use placeholders until they tell you.
5. **Recursive resource control is the thesis.** Mastery is sustained operation across compound cycles, not arrival at a destination.
6. **Catalog all tactics; gate suggestion behind structural accountability.** All 782 Catalogue tactics + ~100 Table 3 moves are visible for identification. Tactical *suggestion* is gated behind OPC § 15 (alternatives audit) + OPC § 11 (harm + ethical evaluation). Per-cycle audit trail records the gate completions and any operator overrides.
7. **Mode-aware discipline.** Consultant mode: PRACTITIONER-ASSESSMENT (§ 16) + ENGAGEMENT-AUDIT (§ 17) mandatory pre-engagement. Principal-self mode: same protocols available; no-false-confidence priming added to AI register.
8. **You propose, the operator disposes.** Show reasoning when proposing tactics, schemas, or interventions. Honor overrides; log them.
9. **Three reference systems coexist by domain.** Slash addressing for cycle constituents (`α.1/i.1/D.1/P.1`); OPC hierarchical IDs for sphere diagnostic (`2.1.6.4.2`); Catalogue Reference IDs for tactics/strategies/clusters/theorists (`0029`, `#8`, `C24`, `Schelling`).
10. **The OV is a cognitive prosthetic, not an oracle.** Track / Analyze / **Uncover** are three jobs. The third is the most demanding — multi-hop horse-trading, coalition recognition, theorist-pattern surfacing. The shipped methodology is structured reasoning support, not deterministic prediction.

## When in doubt

- About what PLC is → `_plc-engine/01-WHAT-IS-PLC.md`
- About the session protocol → `_plc-engine/03-SESSION-PROTOCOL.md`
- About the schema (Types, properties, relationships) → `_plc-engine/04-SCHEMA.md`
- About state persistence (Mode A/C/D/E per file) → `_plc-engine/06-STATE-PERSISTENCE.md`
- About a worked example → `Example-Sphere-Acme-Corp/`
- About a specific tactic by ID → `_frameworks/political-warfare-catalogue/tactics/<NNNN>-<slug>.md`
- About a theorist's principle → `_frameworks/political-warfare-catalogue/by-theorist/<name>.md`

End of bootstrap. Proceed with Phase 0.
