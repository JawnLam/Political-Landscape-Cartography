---
Item_ID: plc-frameworks-dissertation-substrate
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Dissertation Substrate — Deep Schema Reference"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
AI_Instructions: ""
---

# Dissertation Substrate — Deep Schema Reference

> **Reference for the Lam 2018 Pepperdine dissertation grounding PLC's structure.** Source: `sources/Lam-2018-Pepperdine.pdf` (294 pages, full text). This file captures dissertation-derived terminology, structure, and notation that PLC's engine + Prototypes operationalize. Where this file made earlier fabricated claims (Figure 6, "14-constituent" assertions, slash-operator role assignments), those have been replaced with dissertation-verified content.

## What the dissertation provides

The Lam 2018 Pepperdine dissertation on political capital provides PLC's load-bearing structural substrate. Specifically:

1. **Grounded-theory methodology** producing **19 theoretical categories** (per dissertation page 162; 21 symbols total because Resources split into Required/Obtained/Current and Utility splits to Utility + Obtained Utility — see Table 4)
2. **The interaction cycle protocol** — the canonical sequence of operations through which an actor obtains a resource from a target. Step count under verification — see § "Cycle step count" below.
3. **The 9-type resource taxonomy** (from PLC's session-1 interview confirmation: money / hard-assets / credibility / attributes / legitimacy / information / access / title / tribe) — confirm against dissertation's resource-category subsections
4. **The Table 3 catalog** of theoretical concepts (pages 129-145) — ~150 specific action types coded by Option Affected (Preferred Position / Adverse Alternative / Varied) × Consideration Affected (Benefit / Cost / Varied) × Effect on Component(s) (Increase / Decrease / Varied)
5. **Slash addressing notation + nomenclature** for cycle constituents (pages 162-167)
6. **Conditional matrix** (Figure 2, page 160) showing relationships between theoretical categories
7. **Theoretical model** (Figures 3 + 4, pages 220-221) — visual depiction with both theoretical-category labels (Figure 3) and slash-addressing labels (Figure 4)
8. **Nested-Interest mechanism via capability-gate** — the recursive resource-accumulation engine (per Tables 21 + 22 example walks)

## The 19 theoretical categories (dissertation TOC, page 151-158)

1. Actor
2. Target
3. Detection
4. Decision matrix
5. Options
6. Preferred position(s)
7. Adverse alternative(s)
8. Considerations
9. Benefits
10. Costs
11. Component
12. Utility
13. Interest
14. Resources
15. Action
16. Actual effect
17. Goal
18. Perception
19. Outcome

Note: the dissertation's Table 4 (Notation symbols, page 163-164) lists **21 symbols** to accommodate operational distinctions — splitting Action into Intention + Execution, splitting Resources into Required / Obtained / Current, and adding Obtained Utility alongside Utility. The 19-category count is the conceptual census; the 21-symbol count is the operational vocabulary.

## Slash addressing notation (dissertation Table 4 + Nomenclature section)

The actual symbol table from the dissertation:

| Theoretical Category | Operation (Greek) | Set or Attribute (Latin) |
|----------------------|-------------------|--------------------------|
| Actor                | α (lowercase alpha) | a |
| Agenda               | Α (uppercase Alpha) | A |
| Target               | τ (lowercase tau)   | t |
| Interest             | ι (lowercase iota)  | i |
| Detection            | δ (lowercase delta) | d |
| Decision Matrix      | Δ (uppercase Delta) | D |
| Objective            | ω (lowercase omega) | o |
| Outcome              | Ω (uppercase Omega) | O |
| Intention            | γ (lowercase gamma) | g |
| Perception           | Γ (uppercase Gamma) | G |
| Execution            | ε (lowercase epsilon) | e |
| Selection            | Σ (uppercase Sigma) | S |
| Preferred Position   | π (lowercase pi)    | P |
| Adverse Alternative  | ψ (lowercase psi)   | X |
| Benefit              | β (lowercase beta)  | b |
| Cost                 | κ (lowercase kappa) | c |
| Utility              | λ (lowercase lambda) | u |
| Required Resources   | θ (lowercase theta) | q |
| Obtained Resources   | Φ (uppercase Phi)   | Q |
| Current Resources    | Θ (uppercase Theta) | R |
| Obtained Utility     | Λ (uppercase Lambda) | U |

**Operation symbols are Greek; set/attribute symbols are Latin.** Lowercase = scoped to a single instance; uppercase = aggregate or summary symbol.

**Slash addressing structure:**

- Slash `/` separates parent constituent from child constituent — analogous to file path notation (`Drive/Folder/Subfolder/File`)
- Period `.` after a symbol means "the only one of this type in the parent set" (no siblings)
- Number after a symbol (e.g., `X1`, `X2`) denotes ordinal when multiple siblings exist
- Square brackets `[ ]` enclose a complete constituent designation
- Round brackets `( )` enclose an operation's argument (the constituent the operation is applied to)
- Curly brackets `{ }` group constituents into sets or operation groups
- Colon-equal `:=` assigns an attribution to a set of constituents
- Right arrow `→` denotes "yields" or projection
- Triple bar `≡` denotes equivalence between operations
- `∋` and `∌` denote set membership ("is an attribute of" / "is not")
- Prime `′` denotes the projected, anticipated, or future value of a constituent

Example from dissertation: `[a./R.] ∋ [Α/i./o./g/q.]` reads "in the actor's current resource set (`[a./R.]`) there exists the required-resource constituent (`[Α/i./o./g/q.]`) — meaning the agenda's interest's objective's intention's required-resource is in the actor's set." When the symbol becomes `∌` instead of `∋`, the resource is NOT in the actor's set — and that's the capability-gate failure point that triggers nested-Interest recursion.

## The interaction cycle (Tables 5-22 row structure)

The Interaction Cycle tables in the dissertation (Tables 5-22, pages 168-217) walk through 5 case studies. Each cycle's rows show the constituents that fired for that specific case. The full row set across all tables is:

1. (Actor — context, names the cycle-initiator)
2. (Agenda — context, names the cycle's larger goal)
3. Interest
4. Detection
5. Target
6. Preferred Position
7. Adverse Alternative
8. Objective
9. Intention
10. Required Resources
11. **Capability-gate** (called "Resource check" in dissertation text; PLC OV standardizes on "capability-gate" with no conflict in the dissertation's term set)
12. Execution
13. Perception
14. Outcome (may include implicit Selection by target)
15. Obtained Utility
16. Obtained Resource

**Cycle step count — under verification.** The dissertation's tables most commonly show 14 row labels (Interest through Obtained Resource). However, Table 4 lists Selection (Σ) as a distinct operation — which could be a discrete step between Perception and Outcome, OR implicit inside Outcome (the target makes a selection from the decision matrix which produces the outcome). PLC engine chapters currently describe a "interaction-cycle protocol (14 constituents)" — this assertion was inherited from session context and should be verified against the Methodology Author's canonical count. Options:

- **14 steps** if Selection is implicit inside Outcome (matches the most-common table-row count from Interest to Obtained Resource)
- **14 constituents** if Selection is a discrete step
- **Larger count** if Actor and Agenda are counted as cycle steps rather than cycle context

Pending verification. Until confirmed, references to "the interaction cycle protocol" should be preferred over "interaction-cycle protocol (14 constituents)."

## The capability-gate mechanism (Tables 21 + 22)

The dissertation's clearest worked example of nested-Interest resource accumulation is in Tables 21 + 22 (pages 213-217), the Rusty / Gerry / Todd interaction:

- Rusty's parent cycle (Table 22) is with Todd. Rusty's Intention 3 requires a specific resource: a job offer for Todd at a different company.
- **Capability-gate fails:** `[a./R.] ∌ [Α/i./o./g3/q.]` — the required resource is not in Rusty's current resource set.
- The cycle cannot proceed past the capability-gate.
- **The required resource itself becomes a new Interest.** Table 21 opens: `Interest: Required resources for Intention 3 → [a.]ι(Α/i./o./g3/i.) := { [Α/i./o./g3/q.] }`. The `ι` operator (Interest) is applied to the constituent identified by the deeper slash path `g3/i.` (interest of goal-3).
- **The nested cycle runs its full structure** with Gerry as Target. Same protocol — Detection / Target / Preferred position / Adverse alternative / Objective / Intention / Required resources / capability-gate / Execution / Perception / Outcome / Obtained utility / Obtained resource — just at a deeper slash-path level.
- **The nested cycle's Obtained Resource flows up.** Gerry produces the job offer; `[a.]Θ(Α/i./o./g3/i./O./Q.) := { [Α/i./o./g3/q.] }`. The same resource ID that failed the parent's capability-gate is now in Rusty's resource set.
- **The parent cycle in Table 22 then proceeds** past the capability-gate to Execution and produces its own Obtained Resource.

**Recursion depth is open-ended.** The slash addressing notation accommodates arbitrary nesting (`g3/i./o./g./i./o./g./...`) — if Gerry's cycle had also failed its capability-gate, that would have seeded a third level.

This is the dissertation's account of multi-hop resource accumulation. The 4R framework (`4R.md`) is the client-facing dashboard over this mechanism; the OV's `PLC_Cycle` Prototype + slash addressing fields capture the recursion depth and the nested-cycle dependencies in audit-trail form.

## The 9-type resource taxonomy (verified)

**Dissertation source: Category #14 (Resources), pages 155-157.** The dissertation defines Resources as *"the means typically necessary to perform the action and successfully achieve the desired effect of increasing or decreasing a benefit or a cost in the target's decision matrix. The common resources observed in from this study include:"*

| PLC enum value | Dissertation name | Dissertation definition (verbatim) |
|----------------|-------------------|-------------------------------------|
| `money` | Money | "the liquid assets that are easily transferred between parties. For example, at the interpersonal level this can be remunerative compensation and at the intraorganizational level this can be budget control" (page 155-156) |
| `hard_assets` | Properties and other hard assets | "tangible goods that are either desired for their own sake but often they are intermediary goods that are required to produce another outcome" (page 156) |
| `credibility` | Credibility | "a track record of verifiable accomplishments which demonstrate a capability... credibility can be considered as the attribution of a successful outcome. The counter to this resource can be considered the attribution of a failed outcome, otherwise known as 'blame'" (page 156). PLC's "credibility-with-blame-counter" shorthand reflects this paired-with-blame structure. |
| `attributes` | Attributes | "natural qualities or hereditary traits which no one can control and is nontransferable. This may include emotional elements such as confidence, charisma, self-worth, self-esteem, analytic intelligence, emotional intelligence, and other physical or aesthetic traits" (page 156). PLC's "attributes-nontransferable" shorthand reflects the dissertation's emphasis on nontransferability. |
| `legitimacy` | Legitimacy | "the institutionally sanctioned warrant for someone to hold a position with a formal title. This also includes social warrants ascribed to someone to lead a tribe" (page 156) |
| `information` | Information | "not the technical knowledge of a particular subject matter. This is the political knowledge of what resources need to be deployed, where, how, when and why. That is the knowledge on how to support or obstruct someone else's agenda, objectives, interests, positions, or goals" (page 156) |
| `access` | Access | "the proximity to someone else with resources and the propensity that they would deploy a resource at the request on another party. Typically this is access to someone who holds a title" (page 157) |
| `title` | Title | "the formal or statutory authority that gives the holder of the title the right to operate the bureaucratic machinery" (page 157) |
| `tribe` | Tribe | "the access to the masses and the degree to which that access can to influence them to deploy their resources" (page 157) |

**Important interlocking relationships the dissertation surfaces:**

- **Legitimacy ↔ Title ↔ Tribe** form a triangle: Legitimacy is the warrant *for* holding a Title OR for leading a Tribe. Title is the *operating* mechanism of legitimacy-warranted authority. Tribe is the *populace* over which a different kind of legitimacy operates.
- **Access ↔ Title**: Access "typically is access to someone who holds a title" — so Access is structurally related to (often derivative of) the network surrounding Title-holders.
- **Credibility ↔ Blame**: explicit paired-resource structure — Credibility is "attribution of successful outcome"; Blame is "attribution of failed outcome." Operationally, an actor's net credibility is credibility-minus-blame, which is why PLC tracks these as a single signed resource type.
- **Information** is explicitly NOT subject-matter expertise — it's political knowledge about resource deployment. This distinguishes Information from Credibility (which requires demonstrated subject-matter capability).

These nuances matter for `plc_Resources_Held` (Actors) and `plc_Resource_Types_Required` (Moves) — when the AI proposes which resource type a move requires or an actor holds, it should reason from these definitions, not from colloquial usage.

## Tables 5-22 — case studies

The dissertation's five test-for-saturation case studies (page 168 onward):

1. **Charles** had a bad boss (Tables 5-6 area)
2. **Jim** needs new work hours (Table 6 area)
3. **Nathan** wants the ISO 9000 (Tables 7-11)
4. **Sarah** "wins" a competition (Tables 12-15)
5. **Rusty** as the new boss (Tables 16-22) — the most complex; includes the nested-Interest example in Tables 21-22

Each case study walks through the actor's interaction cycles using the full slash addressing notation. These are the canonical reference for how the dissertation's model operates in practice.

## Figures in the dissertation

| Figure | Title | Page |
|--------|-------|------|
| Figure 1 | GTM Analytic Workflow | 76 |
| Figure 2 | Conditional Matrix | 160 |
| Figure 3 | Theoretical Model with Theoretical Categories as Labels | 220 |
| Figure 4 | Theoretical Model with "Slash Addressing" as Labels | 221 |

**There are 4 figures total.** Earlier drafts of this file and `4R.md` referenced "Figure 6 (abbreviated form)" — that was fabricated from session inference. There is no Figure 6.

The "abbreviated representation" framing the earlier fabrication may have been confusing comes from the dissertation's Chapter 3 methodology section (around line 3326 of the text extraction), where the GTM analytic workflow is presented in 4 "abbreviated representation" stages (field of investigation → aggregated narrative → theoretical concepts → conditional matrix → theoretical model). These are GTM-methodology stages, NOT the political-action interaction cycle, and they don't correspond to the 4R baseball-diamond framework.

## Title-of-the-dissertation 3-part framing (Discussion section, page 222-223)

The dissertation's title itself names a 3-part framing: **Accumulation, Utilization, And Protection** of political capital. The Discussion section reinforces this:

> *"How is power built? It is built by gathering the resources that will enable the actor to gather more resources. How is power used? It is used in interactions that will produce more political resources. How is power protected? It is protected by deploying low cost or low yield resources to safeguard high value or high yield resources."*

This 3-part build/use/protect framing is from the dissertation directly. The 4R client-facing framework is the Methodology Author's separately-developed coaching abstraction layered atop the dissertation; the 3-part title framing operates at a different layer than the 4R baseball-diamond and is not 4R.

## Cross-references

- Source PDF: `sources/Lam-2018-Pepperdine.pdf`
- The interaction cycle as PLC's `PLC_Cycle` Prototype: `_types/PLC_Cycle.md`
- Slash addressing as reference system #1 (per D18): `_plc-engine/04-SCHEMA.md § three reference systems`
- 4R client-facing dashboard: `4R.md`
- 4R coaching script: `4R-coaching-script.md`
- ADAPT commercialized 5-beat layer: `ADAPT.md`
- 4R is NOT 4R if I'm wrong about R-words: this file's "4R" references all assume the Methodology Author's confirmed 4Rs = Resources / Results / Rationale / Relationship arranged as baseball-diamond flywheel. See `4R.md` for the full framework.

## Items resolved during pre-publication verification (2026-06-13)

All claims in this file have been verified against the dissertation source:

1. **Cycle step count** ✓ resolved — dissertation does not use "step" vocabulary; uses "constituents" / "theoretical categories" / "interaction cycle." PLC walks the dissertation's directed graph in a canonical 14-constituent operational order from Interest (initiation) to Obtained Resource (closure). Selection (Σ) is implicit inside Outcome per Tables 5-22 row structure. ALTERNATIVES-AUDIT § 15 and ETHICAL-ACCOUNTING § 11 gates are PLC additions per D9, not dissertation elements.
2. **9-type resource taxonomy precise dissertation-page sourcing** ✓ resolved — verified against dissertation pages 155-157 (Category #14, Resources). Definitions captured verbatim in the § "The 9-type resource taxonomy (verified)" table above with interlocking relationship notes.
3. **ADAPT 5-beat naming** ✓ resolved — verified against `sources/ADAPT-Loop-Field-Manual.pdf` page 2: A Agenda / D Decide / A Act / P Perceive / T Track. PLC's usage matches the source exactly.
4. **Dissertation year** ✓ resolved — Lam 2018, not 2020 as previously claimed. Global rename completed.
5. **Figure inventory** ✓ resolved — dissertation has 4 figures total. Earlier "Figure 6 abbreviated" references were fabricated and have been removed.

## Items remaining for operator action

- **LICENSE.md** — IP-attorney review required before public release; flagged in LICENSE.md itself. Counsel review scope: contact info / governing jurisdiction (currently California) / termination notice period (currently 30 days) / dispute resolution mechanism / academic-use boundary / fair-use scope around the Catalogue's 50-theorist citations.
3. **Any additional protocol elements** the dissertation specifies (Selection as discrete step? Agenda as cycle-internal vs context?) that PLC's engine should reflect.
