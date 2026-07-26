# Build Prompt for Fable5 — PLC Executive Self-Serve App

> **How to use this file.** Paste everything below the line into Fable5 as a single build brief. Attach the two data files named in §5 (`INDEX.json` and, optionally, a folder of tactic markdown files) so Fable5 builds against the *real* substrate rather than inventing one. If you can only attach one thing, attach `INDEX.json` — it carries all 783 tactic records, 16 strategies, 83 clusters, and 50 theorists in structured form.

---

## ROLE

You are building a working software product. You are not writing an essay about it, not writing a plan, and not writing pseudocode. Your output is a **single self-contained file** that runs immediately when opened. Build the whole thing; do not leave `// TODO` stubs in the primary flows.

## PRODUCT IN ONE SENTENCE

**Political Landscape Cartography (PLC)** is a discipline for reasoning about organizational politics under an audit trail. This app is the *principal-self-coach* edition: a single senior executive uses it themselves — no consultant in the loop — to map the political landscape they operate in, get vetted tactical move recommendations grounded in a scholarly canon, run and log decision cycles over time, and accumulate patterns. Your job is to turn the existing markdown-and-AI methodology into a real, direct-manipulation tool an executive opens and uses.

## WHO THE USER IS

A busy senior executive (CEO, C-suite, VP). Non-technical. Will not read a manual. Operates in `principal_self` mode: they are both the operator and the principal. They return to their "sphere" (their organization's political landscape) repeatedly over weeks and months. They want structured judgment, not a black-box oracle. They value being able to see *why* a recommendation was made and to override it — the tool proposes, the executive disposes.

---

## 1. HARD CONSTRAINTS (non-negotiable)

1. **Single self-contained file.** One `index.html` (or one React single-file build) that opens and runs with no build step, no server, no npm install. Inline all CSS and JS. You may use React + Tailwind via CDN, or vanilla — your call — but it must be one file the user can double-click.
2. **Real saved state that persists across sessions.** The executive's entire sphere (actors, cycles, decisions, diagnostics, patterns) must survive a browser reload and a machine restart. Use **IndexedDB** as the primary store (localStorage is too small for the substrate + history). ALSO provide **Export / Import** to a single `.json` file so the executive owns their data as a portable artifact and can back it up — this honors PLC's "state lives in files" philosophy. Autosave on every mutation; show a subtle "saved" indicator.
3. **Full methodology surfaced, not a toy slice.** All three workflows below ship end-to-end. Depth is behind progressive disclosure, but nothing core is faked.
4. **Ship the substrate, don't invent it.** The tactical catalogue, strategies, clusters, and theorists come from the attached data files (§5). NEVER fabricate a tactic, theorist, strategy, or citation. If the data file is missing a field, show "—", don't make one up.
5. **Offline-first.** No network calls at runtime. Everything the app needs is either in the file or in IndexedDB.

## 2. THE THREE WORKFLOWS (all required, end-to-end)

The app is organized around a sphere. On first run, the executive creates their sphere (name it, e.g. "Acme Corp"). Then three connected surfaces:

### A. MAP THE LANDSCAPE (diagnostic / orientation)
- **Actors.** Add the people in the landscape. Each actor has: name, role/title, and a **posture** toward the principal — one of `allied | ambivalent | defensive | oppositional | unaware`. Plus a free-text read, and a **resource profile** across the 9-type taxonomy: money, hard assets, credibility, attributes, legitimacy, information, access, title, tribe (each rated low/med/high or 0–3). Support relations between actors (ally-of, reports-to, blocks, swing-vote).
- **Power structure.** A short structured capture: formal authority vs. informal/effective authority, coalitions/voting blocs, swing actors, sacred cows.
- **Visualization.** Render the landscape as a **force-directed or clustered graph** (nodes = actors colored by posture, principal at center, edges = relations) AND a simple stakeholder grid (e.g. power × posture quadrants). This is the executive's at-a-glance map. Use a lightweight approach (SVG + a small force sim, or Canvas). No heavy graph library required.
- **OPC snapshot.** A condensed version of the 17-section OPC diagnostic (see §4) — let the executive fill a guided form and store it as a dated diagnostic they can re-run quarterly and compare.

### B. RECOMMEND A MOVE (the catalogue engine + the gates)
This is the intellectual core. The executive describes a situation ("I need the board to approve X but Carol is consolidating against me") and picks a **target actor** and an **intent**. The app then:
- **Surfaces vetted tactical options** from the 783-tactic catalogue, ranked by fit. Fit is computed from: the situation's implied **strategy** (the four-lever model — see §3), the target actor's posture and resources, and versatility. Show the top ~5–8 tactics as cards: title, one-line description, the strategy + lever combination, the theorists cited, and versatility. Let the executive open a tactic to read its full analysis (influence mechanism, optimal conditions, representative scenarios) pulled from the tactic's markdown/description.
- **Runs the two mandatory gates before any move can be "selected":**
  1. **ALTERNATIVES-AUDIT** — the executive must record at least the legitimate alternatives considered (including the do-nothing / go-through-formal-channels option) before committing. The UI blocks selection until this is filled.
  2. **ETHICAL-ACCOUNTING** — the executive must record the harm/ethics evaluation: who could be harmed, is the move proportionate, would it survive daylight. The UI blocks selection until this is filled.
  These are not optional dialogs to dismiss — they are gates. Log both with the move. Allow an explicit "override / proceed anyway" only with a required written justification, and log that too.
- **Theorist grounding is always visible.** Every recommended tactic shows which of the 50 theorists ground it, and the executive can click a theorist to see who they are and what they contribute.

### C. RUN DECISION CYCLES (the longitudinal ADAPT loop)
- A **cycle** is one decision episode structured as **ADAPT: Agenda → Decide → Act → Perceive → Track.**
  - **Agenda** — the executive states intent.
  - **Decide** — pick target, run workflow B (catalogue options + both gates), select a move.
  - **Act** — mark the move executed; timestamp it.
  - **Perceive** — after the fact, record what actually happened vs. what was expected (the perception gap).
  - **Track** — capture the lesson; update the relevant actor's posture/resources; close the cycle.
- **Cycles are append-only history.** A closed cycle is immutable (read-only) — this is the audit trail. Show a timeline of all cycles for the sphere.
- **Patterns.** After several cycles, let the executive name and save a recurring **pattern** (e.g. "succession-pressure-loop") and link the cycles that evidence it. Patterns accumulate evidence rather than being asserted once.

## 3. THE STRATEGY MODEL (four-lever framing — needed for ranking in workflow B)

Every tactic in the catalogue maps to one of **16 generic strategies**, each expressed as a combination of four levers over two options, **X** (the course the principal wants) and **Y** (the alternative/status quo):

- **B(X)↑** — raise the perceived benefit of X
- **C(X)↓** — lower the perceived cost of X
- **B(Y)↓** — lower the perceived benefit of Y
- **C(Y)↑** — raise the perceived cost of Y

A tactic's `generic_strategy` field carries its number, name, and lever combination (e.g. #15 "Full Spectrum" = `B(X)↑ + C(X)↓ + B(Y)↓ + C(Y)↑`). Use these levers as a first-class filter/selector in workflow B: let the executive express "I want to make my option more attractive" (B(X)↑) or "make inaction look costly" (C(Y)↑) and rank tactics whose strategy emphasizes those levers.

## 4. THE OPC DIAGNOSTIC (condensed, for workflow A)

Ship a guided, condensed version of the 17-section sphere diagnostic. Prioritize these sections as the executive-facing form: (1) Power Structure, (2) Stakeholders & Actors, (13) Dynamics [arc-dynamic, opposition-posture, change-initiator-posture], (14) Trajectory [horizon, confidence, key uncertainty], (11) Harm & Ethical evaluation, (15) Legitimate alternatives. Store each completed diagnostic with a date so the executive can re-run and diff over time. Keep it fillable in under 10 minutes — this is a snapshot, not a dissertation.

## 5. DATA YOU ARE BEING GIVEN (bind to it, don't invent)

- **`INDEX.json`** — the catalogue index. A JSON object with a `tactics` array of **783** records. Each record has: `tactic_id`, `title`, `slug`, `description`, `tactic_type`, `cluster_id`, `cluster_name`, `generic_strategy` {number, name, lever_combination}, `versatility` (low/med/high), `theorists_cited` (array), `theorist_count`, and file pointers. **This single file is enough to power workflow B's recommendation engine, cards, strategy filtering, theorist grounding, and cluster browsing.** Load it into IndexedDB on first run.
- **(Optional) tactic markdown files** — richer per-tactic prose (Influence Mechanism, Optimal Conditions, Representative Scenarios). If attached, use for the tactic detail view. If NOT attached, use the `description` field and clearly show that full analysis lives in the source and isn't bundled — do not fabricate scenarios.
- **The 50 theorists** span dramaturgy/impression management (Goffman — most cited), influence/persuasion (Cialdini, Asch, Festinger, Milgram), information economics (Akerlof, Spence, Coase, Williamson), behavioral decision theory (Kahneman, Tversky, Thaler, Sunstein, Simon), game theory/strategy (Schelling, Sun Tzu, Machiavelli, Greene), organizational power (Pfeffer, Olson), sociology of power (Bourdieu, Foucault), networks (Granovetter), symbolic politics (Edelman), bystander effects (Darley, Latané). Derive the theorist roster and per-theorist tactic counts programmatically from `INDEX.json` (`theorists_cited`) — do not hardcode a list you invented.

If neither data file is attached, STOP and tell the user you need `INDEX.json` before you can build the catalogue engine truthfully — do not proceed by fabricating tactics.

## 6. THE DISCIPLINES (these are the soul of PLC — bake them into the UX, not a help page)

1. **The tool proposes; the executive disposes.** Every recommendation is a proposal with visible reasoning and a one-click override. Never present output as an answer the executive must accept.
2. **Never invent.** Tactics, theorists, strategies, citations come only from the data. Missing = "—", never fabricated.
3. **Never fabricate identity.** Do not guess the executive's name or their actors' names from anything — the user types them in. Use placeholders `[PRINCIPAL]` / `[ACTOR]` until provided.
4. **The gates are mandatory.** No move reaches "selected" without ALTERNATIVES-AUDIT and ETHICAL-ACCOUNTING completed, or an explicitly logged override with written justification.
5. **State lives in files.** Autosave to IndexedDB; export to a portable `.json`. If it isn't saved, it didn't happen.
6. **Closed cycles are immutable.** The audit trail is the point. Read-only once closed.
7. **Numbers are scaffolding, not answers.** Any fit score, ranking, or resource rating is a *directional* aid, shown as ordinal/qualitative where possible, always overridable, never presented as a precise truth. If the executive disagrees with a ranking, that disagreement is a signal to revisit the inputs — not something the arithmetic outranks. Avoid false precision (no "87.3% fit").
8. **One thing at a time.** During any intake/guided flow, ask for one thing per step — never dump a multi-field questionnaire wall.

## 7. UX PRINCIPLES

- Calm, executive-grade, information-dense but uncluttered. Think "strategy war-room dashboard," not "consumer app." Muted palette; posture colors used consistently (e.g. allied=green, defensive=amber, oppositional=red, ambivalent=grey, unaware=blue-grey).
- A persistent left nav for the three surfaces (Landscape / Moves / Cycles) plus Sphere settings and Export/Import.
- Home = the landscape map + a status strip (engagement stage, # actors, # active cycles, latest OPC date, open decisions).
- Every recommendation card and every gate is legible at a glance; deep detail is one click away.
- Empty states teach: on first run, guide the executive to name their sphere, add their first actor, and run their first cycle — one step at a time.

## 8. WHAT "WORKING" MEANS (acceptance criteria — self-check before you finish)

- [ ] Opens as one file, no build step, no network.
- [ ] Executive can create a sphere, add actors with posture + resources + relations, and see the landscape graph render.
- [ ] `INDEX.json` loads; workflow B returns real, ranked tactics with strategy, levers, theorists, versatility; tactic detail opens.
- [ ] Strategy/lever filtering works; theorist view lists real theorists with counts derived from the data.
- [ ] A move cannot be selected until BOTH gates are filled; override requires written justification and is logged.
- [ ] A full ADAPT cycle can be run start to finish and closed; closed cycles are read-only; a timeline shows history.
- [ ] Patterns can be created and linked to cycles.
- [ ] Reload the page and restart the browser — all data is still there (IndexedDB). Export produces a `.json`; Import restores from it.
- [ ] No fabricated tactics/theorists anywhere; missing data shows "—".
- [ ] No false-precision numbers; every score is overridable.

## 9. BUILD ORDER (suggested)

1. Shell + IndexedDB persistence layer + Export/Import + sphere creation.
2. Data loader for `INDEX.json` → catalogue store; theorist roster derivation.
3. Landscape surface: actor CRUD, resource/posture model, relations, graph + grid viz, OPC snapshot form.
4. Moves surface: situation intake → ranking engine → tactic cards/detail → the two gates → selection.
5. Cycles surface: ADAPT flow wiring workflow B into Decide; Act/Perceive/Track; immutability on close; timeline; patterns.
6. Polish: empty states, saved indicator, self-check against §8.

Deliver the single file. Then give a 5–10 line note on what's fully wired, what's simplified, and any assumption you made about the data.

---

*Source methodology: Political Landscape Cartography (PLC) v1.1 → v1.2, by Cong "Jawn" Lam, grounded in the Lam 2018 Pepperdine dissertation on political capital, the ADAPT loop, the OPC Assessment, the Political Warfare Catalogue (783 tactics / 16 strategies / 83 clusters / 50 theorists), and the LSPI formal foundation. This app is the principal-self-coach edition.*
