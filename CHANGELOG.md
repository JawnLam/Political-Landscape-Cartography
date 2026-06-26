---
Item_ID: plc-changelog
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Political Landscape Cartography — Changelog"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
AI_Instructions: ""
---

# Political Landscape Cartography — Changelog

All notable changes to PLC are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/) conventions with PLC-specific section conventions added:

- **Added** — new Prototypes, Templates, scaffolding, Catalogue extensions, patterns, principles, session activities, framework references
- **Changed** — modifications to existing engine prose, framework content, scaffolding, or Catalogue entries
- **Deprecated** — features still present but slated for removal in a future major
- **Removed** — features deleted (always a major bump)
- **Fixed** — typo / clarification / formatting corrections
- **Security** — any change to redaction profiles, gate semantics, or boundary-of-disclosure discipline
- **BREAKING** — any change that breaks installed sphere cartridges (always a major bump; requires `MIGRATION-v<x>-to-v<y>.md`)
- **Migration notes** — for minor or major bumps, what existing cartridges need to do

PLC follows semantic versioning. See `CONTRIBUTING.md` § "In-scope vs major-version-bump scope" for the categorization rules.

---

## [1.1.0] — 2026-06-26

Google OKF v0.1 conformance (coordinated with vault Master_Schema v1.23.0 + OVE v2.4.0). Universal Core renamed to OKF field names (Item_Prototype→type, Title→title, Tags→tags; added timestamp from Date_Modified, optional description/resource). Convention-6 folder _Prototypes/ → _types/. Date_Modified kept, time-synced with timestamp. Hugo excluded.

## [1.0.0] — 2026-06-13

First shipping release. Establishes the v1.0 schema, the four substrate authorities, the 16 Prototypes, the 22 Templates, the 6 YAML scaffolding files, the operator-facing documentation set, the bootstrap protocols, and the worked-example sphere cartridge.

### Added — Foundations
- **Lam 2018 Pepperdine dissertation on political capital** integrated as the grounded-theory substrate. 19 axial-coded categories; interaction-cycle protocol (14 operational constituents per PLC's walk-through); 9-type resource taxonomy (money / hard assets / credibility / attributes / legitimacy / information / access / title / tribe); slash-addressing notation; Table 3 inventory of ~100 granular Moves. Source PDF in `_frameworks/sources/`.
- **ADAPT Loop** integrated as the commercialized 5-beat coaching frame (Agenda → Decide → Act → Perceive → Track). Source PDF in `_frameworks/sources/`. Lookup card at `_frameworks/ADAPT.md`; craft layer at `_frameworks/ADAPT-as-consulting-engine.md`.
- **OPC Assessment v3.0** integrated as the 17-section sphere diagnostic with 6-level hierarchical IDs. Includes § 11 (Harm & Ethical Evaluation — drives ETHICAL-ACCOUNTING gate), § 15 (Legitimate Alternatives — drives ALTERNATIVES-AUDIT gate), § 16 (Practitioner Self-Assessment — consultant mode), § 17 (Advisor Engagement Politics — consultant mode). Located at `_frameworks/OPC-Assessment.md`.
- **Political Warfare Catalogue** integrated: 782 tactics, 16 strategies, 84 thematic clusters, 50 scholarly theorists. Source mirror at `_frameworks/political-warfare-catalogue/`. Full INDEX.json plus by-strategy / by-cluster / by-theorist facet directories.

### Added — Engine (8 chapters)
- `AI-BOOTSTRAP.md` — AI entry point (4 engagement paths; Phase 0 pre-flight; readiness statement requirements; mode-aware path decision)
- `_plc-engine/00-START-HERE.md` — operator identification; active-sphere identification; Tier 1 + Tier 2 reads; mode-aware pre-engagement hard precedence; sandbox mode; 12 core principles overview
- `_plc-engine/01-WHAT-IS-PLC.md` — definition; 4 substrate authorities; bimodal operator model; what PLC is NOT; 6 distinguishing properties; when right form / when not
- `_plc-engine/02-PRINCIPLES.md` — P1-P12 in full with consequences and anti-patterns
- `_plc-engine/03-SESSION-PROTOCOL.md` — 9-step session lifecycle; 15 activities + 2 embedded gates; full RUN-CYCLE protocol with ALTERNATIVES-AUDIT § 15 + ETHICAL-ACCOUNTING § 11 walkthroughs; QUARTERLY-AUDIT (3-part base + 4 consultant additions); Audit Mode; quality gates checklist
- `_plc-engine/04-SCHEMA.md` — 16 Prototypes; 12 relation families with 24 reciprocal pairs; three reference systems (slash addressing / OPC hierarchical IDs / Catalogue Reference IDs); mastery scales; folder structure; frontmatter conventions
- `_plc-engine/05-WRITING-FOR-AI.md` — 4 audiences; AI-facing + operator-facing prose conventions; tone discipline with mode-aware no-false-confidence priming; F1-F9 documented failure modes; quality checks
- `_plc-engine/06-STATE-PERSISTENCE.md` — 5 durability modes (A/C/D/E/D→E); per-Prototype mode table; Current/History section discipline; cycle lifecycle state machine; reciprocal-update enforcement; sphere-backbone rollup discipline; status-flag pattern
- `_plc-engine/07-SHIPPING-CHECKLIST.md` — 10-section pre-ship gauntlet plus Major Bump Addendum; F1-F9 regression checklist; Convention 1-8 compliance signoff

### Added — Prototypes (16)
- Sphere backbone trio: `PLC_Sphere_Manifest`, `PLC_Sphere_State`, `PLC_Sphere_Decisions`
- Identity + cast: `PLC_Principal`, `PLC_Actor`
- Operational: `PLC_Campaign`, `PLC_Cycle` (the D→E status-flag-transitioning Prototype), `PLC_Session` (with 15-activity enum)
- Diagnostic + retrospective: `PLC_OPC_Diagnostic`, `PLC_Engagement_Retrospective`
- Substrate: `PLC_Move` (smallest grain), `PLC_Tactic` (composed; Catalogue Reference ID 0001-0782), `PLC_Strategy` (1-16), `PLC_Cluster` (C01-C84), `PLC_Theorist` (50 scholarly atoms per D15)
- Discovery: `PLC_Pattern` (single Prototype with 6-family enum: stakeholder_archetypes / change_initiator_postures / opposition_postures / arc_dynamics / power_dynamics_themes / ethical_dilemmas)

### Added — Templates (22)
22 blank-but-conforming starter scaffolds in `_plc-engine/_templates/`. Per-Prototype distribution: Actor 2 flavors (Full + Stub); Session 4 specialized (RUN_CYCLE + OPC_DIAGNOSE + QUARTERLY_AUDIT + Generic); OPC_Diagnostic 3 scopes (Full + Partial + Seed); other Prototypes 1 each.

### Added — YAML scaffolding (6)
1. `export-schema.yaml` — structured-export schema for D23 Layer 3 longitudinal-signals
2. `redaction-profiles/internal-leadership-summary.yaml` — internal leadership audience
3. `redaction-profiles/external-board-summary.yaml` — strictest in regular flow; board-chair-escalation protocol included
4. `redaction-profiles/peer-consultant-share.yaml` — anonymizes identity; preserves methodology
5. `redaction-profiles/principal-private.yaml` — consultant §§ 16-17 redacted; advisor-eyes-only flag honored
6. `redaction-profiles/audit-trail-full.yaml` — no redaction; source of truth for all derived profiles

### Added — Operator-facing documentation
- `README.md` — front door with one-line pitch + three quick-start paths (deploy / orient / methodology-study) + Foundations section naming all 50 theorists at ship time
- `INSTALL.md` — 5-step install with Convention 1 folder naming enforced + 11-row troubleshooting table
- `OPERATOR-GUIDE.md` — single file with partitioned mode sections per D3; 20-row universal symptom→cause→fix + 4-row consultant-specific + 3-row principal-self-specific; AI register overrides via `_USER.md`; stash-pop conflict guidance
- `CONTRIBUTING.md` — 4-zone contribution table; patch/minor/major version criteria; "what's frozen between majors" list; 3-tier contribution workflow

### Added — Bootstrap protocols
- `BOOTSTRAP-NEW-SPHERE.md` — 12-section new-sphere intake; pre-engagement hard precedence in consultant mode (OPC §§ 16-17 BEFORE CQ1); quality floor at sphere-open; CQ1-CQ8 required + CQ9-CQ10 optional
- `UPDATE-PROMPT.md` — 12-step AI-facing version-update protocol per Convention 7; sphere-preservation discipline; F1-F9 regression spot-check at every update

### Added — Pattern seeds (6 families)
- `_PATTERNS/stakeholder-archetypes/` — from OPC § 2.2.1
- `_PATTERNS/change-initiator-postures/` — 10 from OPC § 13.1.1
- `_PATTERNS/opposition-postures/` — 10 from OPC § 13.1.2
- `_PATTERNS/arc-dynamics/` — 20 from OPC § 13.2
- `_PATTERNS/power-dynamics-themes/` — 10 from OPC § 13.3.1
- `_PATTERNS/ethical-dilemmas/` — 10 from OPC § 13.3.2

### Added — Worked-example sphere
A populated example sphere cartridge demonstrating the full schema. See `Spheres/Example-Sphere-Acme-Corp/` — Acme Corp engagement (consultant mode; family-board succession scenario) materializing the worked examples used across the Prototype definitions. Serves as the F-code regression canary per `07-SHIPPING-CHECKLIST.md` § 7. Intentionally mid-engagement (not closed) — demonstrates active-state cartridge form rather than retrospective-final state.

### Added — License + version metadata
- `LICENSE.md` — proprietary, all-rights-reserved license with explicit permission grants required for consulting deployment, derivative works, redistribution, embedding, organizational deployment
- `VERSION.md` — canonical version reference; compatibility matrix
- `CHANGELOG.md` — this file
- `.gitignore` — sphere-cartridge exclusion patterns

### Security
- ALTERNATIVES-AUDIT § 15 + ETHICAL-ACCOUNTING § 11 gates established as mandatory inside RUN-CYCLE protocol; override discipline documented (per D9)
- Five redaction profiles establish baseline output-disclosure discipline (per D13 + D16)
- F1-F9 documented failure modes establish baseline AI-misbehavior discipline (per `05-WRITING-FOR-AI.md`)

### Migration notes
First shipping release; no prior cartridges to migrate. Operators installing PLC for the first time follow `INSTALL.md`.

### Acknowledgments
PLC v1.0.0 was designed using **Operating Volume Engineering v1.2** (the meta-OV for designing other OVs). The design engagement ran 2026-06-07 through 2026-06-13 across three sessions: BOOTSTRAP (CQ1-CQ10 → D1-D13), CATALOGUE-INTEGRATION (D14-D16), and SCHEMA-DESIGN (Q0-Q13 → D17-D30). The ARTIFACT-DRAFT phase materialized this v1.0 set of shipping files.

The 50 cited theorists are acknowledged in `README.md` § Foundations and individually in `_frameworks/political-warfare-catalogue/by-theorist/`. Their scholarly works remain subject to their own copyrights; PLC cites under fair-use academic conventions and does not redistribute their primary work.

---

## Format conventions for future entries

When adding a new release section:

- Place above prior releases (newest first)
- Use the format `## [<version>] — <YYYY-MM-DD>`
- Group entries under the standard headings (Added / Changed / Deprecated / Removed / Fixed / Security / BREAKING / Migration notes)
- BREAKING entries MUST be prefixed `BREAKING:` and MUST include a pointer to the migration guide
- Acknowledgment block at end of substantive releases

## Format conventions for pre-release work

Pre-release versions (alpha, beta, rc) follow semantic versioning with the convention:

- `1.0.0-alpha.1` — early development, schema unstable
- `1.0.0-beta.1` — schema stable; documentation gaps acceptable
- `1.0.0-rc.1` — release candidate; ship-checklist passing; awaiting final sign-off

Pre-release entries are documented separately under `## [Unreleased]` until they reach a numbered release.
