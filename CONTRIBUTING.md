---
Item_ID: plc-contributing
Item_Prototype: Fleeting
Title: "Political Landscape Cartography — Contributing Guide"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
AI_Instructions: ""
---

# Contributing to Political Landscape Cartography

PLC is a methodology, not just code. Contributing to it means contributing to a working scholarly substrate, an operational protocol, or both. This file lays out what's in scope for which kind of contribution, how to propose changes, and the prose conventions that keep PLC coherent across contributors.

## Before you contribute

Three orienting reads, in order:

1. `README.md` — what PLC is
2. `_plc-engine/01-WHAT-IS-PLC.md` — the methodology's claim and boundary
3. `_plc-engine/04-SCHEMA.md` — the 16-prototype data model

If you've never deployed PLC end-to-end, contributing engine-zone changes is premature. The methodology's correctness shows up in cycle-execution discipline; without that experience, proposed engine changes tend to ship the wrong abstraction.

For Catalogue extensions, framework extensions, or pattern extensions, deploy-first is not a prerequisite — those are substrate contributions, not protocol contributions.

## Scope by content zone (Convention 8)

PLC has four content zones. Contribution rules differ per zone.

| Zone | Path pattern | Contribution allowed? | Triggers version bump? |
|------|--------------|-----------------------|------------------------|
| **Engine** | `_plc-engine/`, `AI-BOOTSTRAP.md`, `BOOTSTRAP-NEW-SPHERE.md`, `_Prototypes/` | Yes, but high bar | Yes — minor or major depending on shape |
| **Framework** | `_frameworks/`, `_PATTERNS/` | Yes (extensions); shipped substrate is Mode E | Minor (extensions); major (changes to shipped) |
| **Sphere** | `Spheres/<sphere>/` | No — spheres are per-operator | N/A — never shipped |
| **Scaffolding** | `_plc-engine/_templates/`, `_plc-engine/_yaml/` | Yes | Minor |

### What goes where

**Engine contributions** include:

- Edits to engine chapters (`00-START-HERE.md` through `07-SHIPPING-CHECKLIST.md`) for clarity, accuracy, or new documented failure modes
- New principles (P13+) — requires explicit justification and recurring evidence from multiple engagements
- New session activities — requires showing the activity isn't expressible as a combination of existing 15
- Changes to the 12 relation families — requires showing the family doesn't exist or has a documented analytic gap
- New mandatory gates inside RUN-CYCLE — extremely high bar; the current ALTERNATIVES-AUDIT + ETHICAL-ACCOUNTING gates are minimal-sufficient
- Prototype definition changes (`_Prototypes/PLC_*.md`) — schema additions trigger minor bumps; required-field changes or removals trigger major bumps

**Framework contributions** include:

- New Catalogue tactics, theorists, or clusters via `_frameworks/political-warfare-catalogue-extensions/`
- New shipped pattern seeds in `_PATTERNS/<family>/`
- New strategy atoms in `_frameworks/strategies-extensions/`
- Refinements to OPC Assessment v3.0 → v3.1+
- New framework references (e.g., a new theorist's canonical work added to the citation network)

**Scaffolding contributions** include:

- New template variants for an existing Prototype (e.g., adding a `PLC_Actor_External_TEMPLATE.md` for external-actor stubs)
- New redaction profiles for unrepresented audiences (e.g., a `regulatory-disclosure.yaml`)
- Refinements to `export-schema.yaml` for additional longitudinal-signal fields

**Sphere zone is NEVER a contribution target.** Sphere cartridges are per-operator engagement state. They don't ship. If you have a sphere worth using as a worked example, propose it for the shipped example sphere via an engine contribution.

## In-scope vs major-version-bump scope

The schema is frozen between major versions — per D13 adapted to PLC. Changes break down:

### Patch bumps (`v1.0.0` → `v1.0.1`)

- Typo corrections in any zone
- Documentation clarifications that don't change meaning
- Markdown rendering fixes
- Spelling, grammar, formatting

Patch bumps may proceed without UPDATE-PROMPT changes; the operator runs `git pull` and continues.

### Minor bumps (`v1.0` → `v1.1`)

- New Prototypes (additive only)
- New Templates (additive only)
- New YAML scaffolding (additive only)
- New Catalogue tactics / theorists / clusters / strategies via the extensions namespaces
- New shipped patterns in existing families
- New engine principles (P13+) added
- New session activities added
- Engine chapter substantive revisions that don't change required fields or break references
- Relation family additions

Minor bumps require an UPDATE-PROMPT entry. They do NOT require migration guides.

### Major bumps (`v1.0` → `v2.0`)

- Required-field changes or removals on existing Prototypes
- Mode contract changes (e.g., a Mode E file becoming Mode D)
- Reference system changes (the three reference systems per D18 are load-bearing)
- Existing gate semantics changing
- Existing principle removed or substantively redefined
- Relation family removed or semantics changed
- Catalogue ID scheme changes
- Convention changes that break installed cartridges' interpretation

Major bumps REQUIRE:

- Explicit `MIGRATION-v<old>-to-v<new>.md`
- Breaking changes prefixed `BREAKING:` in CHANGELOG
- Master_Schema namespace bump
- Pilot upgrade of at least one sphere from prior major version succeeding
- UPDATE-PROMPT explicitly warning about breaking changes before applying

See `_plc-engine/07-SHIPPING-CHECKLIST.md` § "Major Bump Addendum" for the full pre-ship gauntlet.

### What's frozen between majors

Between `v1.0` and `v2.0`, these do not change:

- The 16 Prototype types (additions are minor; removals are major)
- The 5 durability modes (A/C/D/E/D→E)
- The 12 relation families
- The three reference systems (slash addressing / OPC hierarchical IDs / Catalogue Reference IDs)
- The principle numbers (P1-P12 keep their identifiers even if their text refines)
- The 15 session activities + 2 embedded gates
- The Catalogue Reference ID space (0001-0782 ships fixed; extensions use `EXT-` namespace)

If your contribution would touch one of these, the answer is "open a major-bump proposal," not "edit and PR."

## Voice and tone conventions

PLC's prose conventions are not stylistic. They're functional — the AI reads this prose as instructions. Contributors must match the conventions or the AI will misinterpret.

### For engine chapters

- **Operational, not theoretical.** Write what to do, not what's happening.
- **Imperative voice.** "Read the file" not "the file should be read."
- **Numbered steps for sequences; tables for sets.**
- **Headers must reflect navigable content.** No "Things to think about."
- **State the negative as well as the positive.** Every "do this" with a known failure mode gets a "don't do that."
- **Reference other files explicitly.** `see `<file>` § <section>`` — the AI follows the reference.
- **No meta-prose.** Don't open with "In this section we will discuss..." Cut to the operational point.
- **No emojis** unless the operator explicitly requested.

### For operator-facing docs (README / INSTALL / OPERATOR-GUIDE / this file)

- **Explanatory and lightly motivating.** The reader is human, not AI.
- **Lead with quick-start where applicable.**
- **Symptom → cause → fix** for troubleshooting sections.
- **Mode-aware partitioning** where consultant vs principal-self diverges.
- **Honest about boundary.** Name when PLC is the wrong form.

### For Catalogue / framework contributions

- **Sourced.** Every tactic, theorist, or pattern claim cites a real source. Fabrication is the single largest disqualifier.
- **Defensible.** The scholarly canon's defensibility (per D15) depends on every entry being verifiable against the cited work.
- **Cross-referenced.** Tactics cite theorists; theorists list citing tactics; clusters list adjacent clusters. Reciprocal-update discipline applies to shipped substrate just as it does to sphere state.

If your contribution doesn't match these, expect review pushback on tone alignment before substantive review.

## How to propose a contribution

### For Catalogue, framework, or scaffolding extensions

1. **Open an issue** describing the extension. Include: what's being added; what gap it fills; what source(s) ground it (for Catalogue/framework); how it fits the schema (for scaffolding).
2. **Wait for discussion confirmation** before drafting PR content. Some extensions sound novel but are already covered; the maintainer can route you.
3. **Draft in your fork.** Put extensions in the appropriate `*-extensions/` folder. Use the `EXT-` namespace for IDs to avoid collision with shipped 0001-0782 / 1-16 / C01-C84 ranges.
4. **PR with the extension files + a CHANGELOG entry.** PR description should restate the issue's gap and how the extension fills it.

### For engine improvements

1. **Open an issue** with the proposed change and the evidence motivating it. For new principles or session activities, include 2+ engagement contexts where the gap surfaced.
2. **Wait for discussion confirmation AND scope agreement** before drafting. Engine changes are minor or major bumps; agreeing on which up front saves rework.
3. **Draft in your fork** with engine chapter edits.
4. **PR with the chapter edits + CHANGELOG entry + UPDATE-PROMPT impact assessment.**

### For major-bump proposals

1. **Open an RFC-style issue** with the proposed change, the breaking-change implications, and a draft migration approach.
2. **Wait for explicit major-bump greenlight.** Major bumps require alignment from the methodology author plus consensus from active deployers.
3. **Draft the full ship-checklist gauntlet,** not just the change — `_plc-engine/07-SHIPPING-CHECKLIST.md` § Major Bump Addendum is the gate.
4. **Pilot upgrade** on at least one real sphere before PR.

### What gets fast-tracked

- Patch bumps (typos, formatting, clarifications) — direct PR welcome; minimal review
- Documented F-code regressions surfaced from actual engagement experience — high priority

### What requires more friction

- Engine principle additions
- Schema changes
- Reference system changes
- Convention changes

These are durable commitments; the friction is the point.

## Issue templates

When opening an issue, include:

- **Type:** `extension | engine-improvement | bug | documentation | major-bump-proposal`
- **Zone affected:** `engine | framework | scaffolding | docs`
- **Operator context:** what engagement context surfaced this; consultant or principal-self mode; how many engagements informed the proposal
- **Substantiation:** for extensions, the source(s); for engine improvements, the evidence
- **Backwards-compatibility:** for non-patch changes, what existing cartridges will need to do

## Code of conduct for substantive discussion

PLC's contributor discussions are about political reasoning — a substantive domain where reasonable practitioners disagree. The discussion conventions:

- **Disagree on substance, not framing.** "I think this conflates X and Y" beats "this is unclear."
- **Cite when you can.** "Schelling on commitment problems" beats "as we know from game theory."
- **Hold the boundary on PLC's claim.** PLC is not a general organizational-effectiveness tool; not a leadership-development frame; not a stakeholder mapping app. Contributions that drift toward those adjacent forms get rerouted, not accepted.
- **Respect the bimodal discipline (D3).** Contributions that work in consultant mode but break principal-self mode (or vice versa) need explicit reconciliation.

## Where to discuss

- **Issues** — concrete proposals
- **Discussions** — methodology questions; "is this in scope?" before opening an issue
- **Engagement-private questions** — contact the methodology author directly; PLC's public discussion does not surface client-identifying material

## Acknowledgment

PLC ships under credit-attribution discipline. Contributions to the Catalogue, Pattern library, or Theorist canon are credited in `CHANGELOG.md` per release. Engine contributions are credited in the chapter's footer where substantive. Sphere-zone contributions are not credited (the spheres don't ship).

Methodology authorship credit (Lam 2018 dissertation; ADAPT Loop; OPC Assessment) is fixed and not subject to redistribution per the work's licensing — see `LICENSE.md`.
