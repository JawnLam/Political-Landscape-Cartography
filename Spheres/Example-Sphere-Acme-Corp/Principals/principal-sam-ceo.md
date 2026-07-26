---
type: PLC_Principal
timestamp: "2026-06-13T00:00:00Z"
Item_ID: principal-sam-ceo
title: "Sam — Principal"
Date_Added: 2026-04-15
Date_Modified: 2026-07-15
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Principal_Name: "Sam"
plc_Principal_Role: "CEO, 4 years tenure"
plc_Authority_Scope_Unilateral: "Full P&L; capital allocation up to $5M; board-relations lead; org-design within existing structure"
plc_Authority_Scope_Coalition: "Capital allocation > $5M (board); board composition (board); succession planning (board + family); compensation revisions for direct reports (compensation committee)"
plc_Authority_Scope_Forbidden: "Unilateral board restructure; family ownership structure; bypass of independent directors on audit; family-personal succession discussions (per sphere scope boundary)"
plc_Current_Agenda: "Through 2026-Q4: preserve operating mandate through succession-planning cycle. Specifically — keep the family voting bloc 3-1 in his favor; prevent Carol's shadow-CEO consolidation; maintain independent-director confidence in his leadership through Q4 ratification window."
plc_Principal_Funnel_Sharpness: 4
plc_Funnel_Last_Refined_Date: 2026-06-10
plc_Engagement_Status: active
plc_Active_Campaigns:
  - "[[campaign-succession-q3]]"
AI_Instructions: ""
---

# Sam — Principal

## Current

### Funnel

**Agenda:** Preserve operating mandate through succession-planning cycle (through 2026-Q4).

**Decision criteria** (sharpness 4 — Sam can derive considered-move set directly from these without scaffolding):

1. Does this move preserve or strengthen the 3-1 family voting bloc?
2. Does this move avoid handing Carol additional unilateral resource control?
3. Does this move maintain Sam's standing with the 3 independent directors?
4. Can this move be reversed if the political read turns out wrong?

Anything failing #1 or #2 is out. Anything passing all four is in. The funnel is the cycle-by-cycle filter that drives RUN-CYCLE's selected-moves narrowing after the ALTERNATIVES-AUDIT and ETHICAL-ACCOUNTING gates clear.

### Authority Scope

- **Unilateral** (recently expanded — see Engagement History 2026-05-15): full P&L authority; capital allocation up to $5M; board-relations lead; org-design within existing structure
- **Coalition required:** capital > $5M (board majority); board composition (board); succession plan ratification (board + family); compensation for direct reports (compensation committee)
- **Forbidden:** unilateral board restructure; family ownership structure changes; bypass of independent directors on audit matters; family-personal succession discussions (the sphere scope boundary per `_sphere-decisions.md` § 001)

### Active Coaching Themes

- **Detection discipline.** Sam runs on relationship intuition; we're building structured perception-gap checks at every cycle close. Sam now reliably names cold-reading indicators before forming conclusions. Working theme: extending this discipline from individual actor reads to coalition-state reads.
- **Coalition asymmetry.** Sam underweights Robert (board chair, family — swing) as a swing actor — tends to assume Robert's family loyalty translates to political alignment. Explicit coalition-mapping at each cycle close addresses this; Cycle-0008 is currently working Robert's signal-readiness.
- **Funnel-vs-relationship boundary.** Sam's strength is relationship work; the funnel's structural discipline sometimes feels (to him) like over-engineering relationship dynamics. Coaching theme: holding the funnel as protection FROM relationship-instinct overreach in high-stakes moves.

### Mastery Signals

**Sharpness 4 earned 2026-06-10 at Cycle-0007 close.** Evidence:

- Sam independently derived the Cycle-0007 considered-moves set from his funnel criteria before the AI surfaced any moves
- Funnel survived Cycle-0006 pressure-test against Carol's budget-memo escalation without revision
- Sam's coaching-theme discussions now reference funnel criteria by number, not as external scaffolding

**Sharpness 5 would require** the funnel becoming Sam's working frame without explicit reference. Currently he still works *from* the written criteria (file pulled up during cycles); 5 means he works *through* them as internalized cognition. Estimated 6-12 months at current cadence.

### Current Resource Holdings

This is LSPI's **R** — Sam's resource **multiset**, as of 2026-07-15. Quantities are load-bearing: two banked asks are not one, and a set cannot say so. Executions deduct exactly once; flowbacks from closed cycles append exactly once (Theorem 13.4). This block is the canonical R; the cycle files' `## LSPI Configuration` sections point here rather than restating it.

| Resource | Qty | Carrier | Effect signature | Durability |
|----------|-----|---------|------------------|------------|
| Delivery credibility — the Q2 consolidation record | 1 | credibility | `P/b +` with the board generally; strongest with Elena and the independents | durable (the *record* persists; the quarterly *attention* it takes to deploy does not — tracked separately below) |
| Professional trust with Elena | 1 | credibility / access | enabling; converts to access rather than moving cells directly | durable |
| Ask-capital with Robert | **1** (was 2) | other | `P/c −` — one direct ask he will absorb without cost to the relationship | fragile; does not replenish within a quarter |
| Board-relations lead standing | 1 | title | `Adv/c +` broadly; low yield, high protective value | durable |
| Board-secretary filing slots (this quarter) | **1** (was 2) | other | enabling; the standard channel into committee process | fragile; resets quarterly |
| Q2 delivery attention (this quarter) | **0** (was 1) | other | the deployment cost of the credibility record | fragile; consumed |
| Robert's committed swing-vote alignment through Q3 | **1** (obtained 2026-07-15) | tribe | `Adv/c +` with the rest of the family bloc — a chair who has moved a succession item and spoken for it on the record makes the Carol path costlier for the other three. **Not** convertible into an ask: a position is not a licence, which is why this row and the ask-capital row both exist and are not netted | fragile; expires with Q3 by its own terms, and conditional on the next item arriving procedurally clean. Robert committed to moving clean items, not to Sam — his perception held `ambivalent` at the 07-15 close |

**Carrier note.** Three rows carry `other`. Ask-capital, filing slots and delivery attention are all costly, target-conditional capacities to move a cell — resources by the primary intensional definition (`08-ESTIMATION` § The actuator) — and none of them is money, hard assets, credibility, attributes, legitimacy, information, access, title or tribe. The nine types are a basis of carriers for elicitation, not a partition. Forcing these into `credibility` would have made the multiset unreadable at exactly the point it mattered: the ask-capital count is what said "you get one shot at Robert this quarter." The 07-15 flowback row is deliberately **not** a fourth `other`: a committed swing-vote alignment is an ally's position inside a bloc, which is precisely what `tribe` names. Reaching for `other` when a listed carrier fits is the same error as forcing a fit, running the other way.

**Transaction ledger — cycles 0009 + 0010 (the spawn/flowback chain).** Every line is either a deduction or an append; each appears exactly once. **Deductions are dated at the execution that spent the resource (`ε`), not at the close that reports it**; appends are dated at the flowback that recorded them. The two dates diverge whenever a cycle runs on past its last spend — cycle-0009's did, by a week — and dating a deduction at close is the easiest way to make a conserved ledger look like it double-counts.

| Date | Kind | Resource | Δ | Where |
|------|------|----------|---|-------|
| 2026-06-25 | deduct | Q2 delivery attention | 1 → 0 | g_1's execution (folded into the probe-2 dual-use pre-brief — see the discipline note) |
| 2026-06-27 | convert | professional trust (Elena) ⇝ joint-meeting access | +1 access; trust stock unchanged | transfer edge, rate ≈ 1; a durable node yielding a fragile instance |
| 2026-06-27 | deduct | joint-meeting access | 1 → 0 | `ε(g_2)` — cycle-0009 Move 1 |
| 2026-07-03 | deduct | board-secretary filing slot | 2 → 1 | `ε` of cycle-0010's only intention — the filing submitted 09:00, five days before that cycle closed |
| 2026-07-08 | **append** | finance-committee procedural clearance | 0 → 1 | `⟨flowback-recorded, { [Α/i.1/o./g3/i./Q.] }⟩` at `⟨close-nested, C10, C9⟩` |
| 2026-07-08 | deduct | finance-committee procedural clearance | 1 → 0 | `ε(g_3)` — spent when the ask was placed on the cleared item that afternoon, not when the motion carried on 07-15 |
| 2026-07-08 | deduct | ask-capital with Robert | 2 → 1 | `ε(g_3)` — the co-sign ask, same execution |
| 2026-07-15 | **append** | Robert's committed swing-vote alignment through Q3 | 0 → 1 | `[a.]Φ(Α/i.1/O./Q.) := { [Α/i.1/Q.] }` at cycle-0009 close |

**Conservation check (Theorem 13.4), by inspection.** Two resources obtained across the chain — the clearance (07-08) and the swing-vote alignment (07-15) — each appended exactly once, each traceable to one flowback marker. Five resources spent — delivery attention, joint-meeting access, filing slot, clearance, ask-capital — each deducted exactly once, each traceable to one execution. The clearance is the interesting one: obtained by the sub-cycle and spent by the parent, appearing once on each side and never in both places at once. No leaks, no duplications.

**One honest gap in the check, stated rather than netted.** The 06-25 delivery-attention deduction has no `θ`/`ε` pair in cycle-0009's Operation Record — g_1's cost was carried inside the probe-2 dual-use execution and never declared as a required resource. The spend is real and is deducted here so the multiset stays conserved, but LSPI's own ledger cannot see it, because the transition rules deduct `cost(q_k)` only for resources a `θ` declared. Two things follow, and both are worth knowing: a plan member that is *held* gets no `θ`/gate test — only the *missing* member does — so held-member spends are conserved in this block and nowhere else; and the record-discipline lesson is logged at [[cycle-0009]] § Lessons rather than papered over.

**Protection.** Board-relations lead standing is the durable low-yield resource spent defending the fragile high-yield ones: it is what keeps the ask-capital with Robert replenishing across quarters and what makes a filing arrive as routine rather than as a manoeuvre. It moves almost nothing on its own, which is why it is the easiest holding to under-price.

## Engagement History

- 2026-07-15: Cycle-0009 closed with the mandate objective met on its **revised** position. Resource holdings net of the cycle: one ask-capital instance and one filing slot spent, one clearance obtained and spent, Robert's Q3 alignment obtained. Sub-cycle [[cycle-0010]] spawned and closed inside it — first acquisition route run in this engagement. (Source: [[cycle-0009]], session [[2026-07-15_014_RUN-CYCLE]].)
- 2026-06-27: `### Current Resource Holdings` opened as an explicit multiset; the professional-trust ⇝ joint-meeting-access transfer edge recorded; one ask-capital instance earmarked against the then-undeclared γ_3. (Source: [[cycle-0009]] augmented gate, session [[2026-06-27_011_RUN-CYCLE]]. **Claimed by session 011 and not applied at the time; applied 2026-07-24 as an F5 repair — see [[2026-07-24_015_QUARTERLY-AUDIT]].**)
- 2026-06-10: Engagement status confirmed `routine` post-Cycle-0007 close. Active campaigns: campaign-succession-q3 only.
- 2026-05-15: Unilateral capital authority raised from $2M to $5M per board action. Authority scope expanded; affects every subsequent cycle's considered-move envelope. (Sphere decision § 003.)
- 2026-05-01: Campaign-Succession-Q3 opened with Sam as principal owner.
- 2026-04-15: Engagement opened; principal added to sphere at bootstrap (CQ2). Initial role + authority scope captured.

## Mastery History

- 2026-06-10: Sharpness 3 → 4. Reason: Cycle-0007 close — Sam independently derived considered-moves set before AI surfaced. (Source: `Cycles/cycle-0007.md` § Lessons.)
- 2026-05-08: Sharpness 2 → 3. Reason: Funnel survived Cycle-0006 pressure-test against Carol's budget-memo escalation. Funnel-as-operational confirmed by surviving one full cycle's adversarial pressure. (Source: `Cycles/cycle-0006.md` § Lessons.)
- 2026-04-22: Sharpness 1 → 2. Reason: Initial funnel drafted from CQ3-CQ7 answers at sphere-open. Decision criteria explicit; not yet pressure-tested. (Source: Session `2026-04-22_002_PRACTITIONER-ASSESSMENT.md`.)
- 2026-04-15: Sharpness 0 (baseline at engagement start; agenda articulated but no decision criteria yet).

## Cross-References

- Sphere: [[acme-corp-manifest]]
- Sphere state: [[acme-corp-state]]
- Active campaigns: [[campaign-succession-q3]]
- Most recent cycle: [[cycle-0009]] (closed 2026-07-15; sub-cycle [[cycle-0010]] closed 2026-07-08)
- Still open: [[cycle-0008]] (engaged past the capability-gate since 2026-06-13)
- Prior cycle: [[cycle-0007]] (closed 2026-06-10)
- OPC current diagnostic (§§ 16-17 carry Sam-specific readiness; § 2.4 sets the sphere's depth bias): [[opc-2026-06-01]]
