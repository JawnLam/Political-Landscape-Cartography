---
type: PLC_Cycle
timestamp: "2026-07-08T00:00:00Z"
Item_ID: cycle-0010
title: "Cycle 0010 — Acquire finance-committee procedural clearance (sub-cycle of 0009)"
Date_Added: 2026-07-02
Date_Modified: 2026-07-08
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Campaign: "[[campaign-succession-q3]]"
plc_Principal_Owner: "[[principal-sam-ceo]]"
plc_Cycle_Number: 10
plc_Cycle_Status: closed
plc_Update_Mode: D
plc_Started_Date: 2026-07-02
plc_Closed_Date: 2026-07-08
plc_Sealed_Date: ""
plc_Actor_Touched:
  - "[[actor-carol-cfo]]"
  - "[[actor-robert-board-chair]]"
plc_Slash_Constituents:
  # keyed by owning actor (Thm 13.1); pure System 1 (F9)
  # sub-cycle paths carry the parent's prefix Α/i.1/o./g3/ — the escalation is visible in the address
  - "Sam: [Α/i.1/o./g3/i.]"                  # the sub-cycle's Interest = the parent's missing q
  - "Sam: [Α/i.1/o./g3/i./t.]"               # target: Carol
  - "Sam: [Α/i.1/o./g3/i./t./D./P.]"         # P: clear the item through standard consent
  - "Sam: [Α/i.1/o./g3/i./t./D./X.]"         # Adv: hold it for full-committee substantive review
  - "Sam: [Α/i.1/o./g3/i./o./g1]"            # the sub-cycle's single intention
  - "Sam: [Α/i.1/o./g3/i./O./Q.]"            # obtained resource at nested close
plc_OPC_Diagnostic_Refs: ["6.2", "6.3", "7.2", "13.1.2"]
plc_Tactic_IDs_Considered: ["0044", "0158", "0380"]
plc_Tactic_IDs_Selected: []
plc_Strategy_Number_Selected: 0
plc_Clusters_Engaged: []
plc_Theorists_Invoked: []
plc_Alternatives_Audit_Completed_At: "2026-07-02T16:10:00"
plc_Ethical_Accounting_Completed_At: "2026-07-02T16:45:00"
plc_Accounting_Overrides: []
plc_Strategic_Stance: adaptive
plc_Stance_Rationale: "K = 1 — a single intention, so the stance costs nothing here and is recorded for continuity with the parent. Stated anyway because inheriting a stance silently is how a batched cycle ends up running inside an adaptive one."
plc_Probe_Budget_Remaining: 0
plc_Detection_Record_Refs: []
plc_Suspended_Parent: "[[cycle-0009]]"
plc_Spawned_Subcycles: []
AI_Instructions: ""
---

# Cycle 0010 — Acquire finance-committee procedural clearance (sub-cycle of 0009)

> **Sub-cycle.** Spawned 2026-07-02 by a gate failure (`∌`) in [[cycle-0009]] at `[Α/i.1/o./g3/q.]`. Parent suspended for the duration; closed 2026-07-08 with the resource obtained and flowed back; parent resumed the same day. **Status: closed 2026-07-08. Mode D within the 7-day grace window** (expires 2026-07-15).

## Agenda
Obtain finance-committee procedural clearance for the Q3 succession agenda item, so that the parent cycle's third intention has the resource its gate demanded. The agenda is not "move Carol" — it is the narrower thing the parent actually lacks. A sub-cycle that widens its own interest past the missing resource is no longer an acquisition; it is a second campaign running inside a suspended one.

## Landscape Assessment
The clearance is Carol's to grant as finance-committee chair (opc-2026-06-01 § 6.3; her mandate is structurally legitimate per § 7.2). The convention requiring it — succession-adjacent items clear the committee before reaching the board calendar — surfaced on 2026-07-01 from Robert and was not in the diagnostic; it has since been pushed back into OPC § 6.2.

Carol is `defensive` (three of three indicators, held since 2026-06-10) and is § 13.1.2.3 `covert_operator`. Her behavioural prior is specific and well-evidenced: she acts on data, not relationships, and will not shift through relationship-rebuilding overtures — confirmed the hard way at Cycle-0005. That prior is what makes this cycle short.

**No Detection Record opened on Carol for this question, and that is a decision rather than an omission.** The estimand is a procedural act with a short list of admissible responses and a documented behavioural prior. The differential would carry one live hypothesis; no probe's expected decision-improvement would clear its cost, which is the stop rule firing before the first probe rather than after the fourth. If the clearance had been refused, that refusal would itself have been the probe — and a much better one than anything designable in advance.

## OPC Self-Diagnosis
Sam holds the documentation and the standard filing channel; he holds no path to the clearance that does not run through Carol's committee (§ 6.3). § 4.3 blind-spot input, live here: Sam's instinct on a Carol interaction is to look for the manoeuvre. The register check (§ 2.4: `elevated-structural`, four escalation indicators absent) is the counterweight — this is a sphere where the boring legitimate route is still open, and treating it as closed would be the paranoia error, not prudence.

## Principal Funnel
Against Sam's four criteria:
1. **Preserve/strengthen the family voting bloc?** — Indirectly; the clearance is what makes Robert's motion cheap for him.
2. **Avoid handing Carol additional unilateral resource control?** — Yes, and worth stating precisely: asking Carol to exercise authority she already holds does not enlarge it. Asking her to *waive* it would have.
3. **Maintain standing with independent directors?** — Yes; a procedurally clean item is the version Elena's cohort reads best.
4. **Reversible?** — Yes. A filing can be withdrawn; nothing here is a commitment Sam cannot walk back.

## Augmented Gate (v1.2+; over the intended plan Π — see 08-ESTIMATION)

- **Possession (∋/∌):** `[a./R.] ∋ [Α/i.1/o./g3/i./o./g1/q.]` (one board-secretary filing slot, this quarter — Sam holds 2)? — **∋**. One q, one gate test.

| Plan member (resource) | Effect (cells, sign) | Cost | Worth given rest of plan | Clears inclusion? |
|------------------------|----------------------|------|--------------------------|-------------------|
| s1 — complete standard-form clearance filing routed through the committee secretary, full documentation attached (consumed: one filing slot) | P/c − (consent-clearing becomes the zero-friction default) and Adv/c + (holding a procedurally ordinary succession-calendar item, on the record, with no stated deficiency, is an irregularity Carol personally owns at the audit committee) | low | pivotal — it is the whole plan | yes |

- **Sufficiency:** yes, and this is a **one-member PASS** — recorded deliberately alongside the parent's three-member Rusty PASS, because the augmented gate has to handle both and the shipped example should show both. The margin on a *procedural* question is small: Carol's Adv path here costs her something concrete and buys her nothing she is not already positioned for. Risk allowance: she can clear it *with* a reservation, which is the likely shape and does not block the parent.
- **Affordability:** one filing slot against the parent's mandate objective. Clears by a wide margin.
- **Verdict: PASS.**
- **Three quantities, kept apart (08-ESTIMATION).** The required shift is small. Sam's cost is one filing slot. Carol's obtained utility is **not** equal to the shift and is close to zero — this member closes the margin by raising the cost of her alternative, not by raising the value of her preferred option. That is coercive shift, not inducement, and naming it is what lets Gate 2 evaluate it honestly rather than under the flattering description.
- **P13 note:** uncalibrated. "Small margin" is an ordinal read off Carol's behavioural prior, not a measurement.

## ALTERNATIVES-AUDIT § 15 Pass (Gate 1)

Ten approaches walked. This is the rare cycle where the audit did not modify the tactical plan — it *produced* it.

- § 15.1 **honest dialogue** — **adopted, and it is the plan's spine.** Sam tells Carol directly what the filing is, why it is going in, and that it will be on the committee's consent agenda. No choreography.
- § 15.4 **transparent operating discipline** — **adopted.** The filing is complete, standard-form, and documented to a level that makes a hold visibly unexplained. The discipline *is* the leverage; nothing is withheld to create it.
- § 15.2 third-party mediation — not applicable.
- § 15.3 constructive information-sharing — subsumed by the filing itself.
- § 15.5 reciprocity-based exchange — considered and rejected on Carol's behavioural prior: reciprocity moves do not work on her and burn credibility when tried.
- § 15.6 procedural-fairness invocation — held in reserve. If the item were held without stated reason, invoking the committee's own standard would be the next legitimate step. Not needed.
- § 15.7 coalition-strengthening — not applicable at this grain.
- § 15.8 escalation-de-escalation — explicitly *de*-escalatory: routing through Carol's own process rather than around it.
- § 15.9 rest-and-re-engagement — not available; the calendar lock is 2026-07-15.
- § 15.10 mutual-gain reframing — partially present: a clean item is better for the committee's record too, and Sam said so without dressing it up as generosity.

**Completed:** 2026-07-02T16:10:00

## ETHICAL-ACCOUNTING § 11 Pass (Gate 2)

Harm grid walked across three scopes.

- **Individual (Carol):** low, with one honest flag. The move asks her to do a legitimate thing she has legitimate reason to do, and imposes no cost she has not already assumed by chairing the committee. The flag is the *mechanism*: the plan works by making refusal visibly irregular, which is pressure, not persuasion. Under § 11.1.1 no category is triggered — nothing here touches reputation annihilation, career destruction or the rest — but the pressure is real and is named rather than described as "clarity."
- **Individual (Robert):** none. The cleared item is what makes his motion cheap.
- **Organizational:** low. § 11.1.2 `trust_annihilation` was checked specifically: does routing through Carol's process while opposing her strategically degrade the process? The judgment is no — using someone's legitimate authority as it was designed to be used is the opposite of corroding it.
- **Systemic:** low. Contrast with Cycle-0007's rejected Tactic 0380 (the Skip-Level Gambit — the Carol-bypass), which failed exactly here.
- **Frameworks:** consequentialist — passes; deontological — no deception, no coercion outside legitimate process; virtue — consistent with the earned-mandate posture; **care ethics — the closest call**, since the relationship is already narrowed to email and a pressure-shaped ask does not repair it. Mitigation: Sam raises the filing with Carol directly before it is submitted, so she learns it from him and not from the secretary's agenda. Justice — passes; the committee's standard is applied to Sam's item exactly as to anyone's.
- **Carried forward:** the Carol collateral-impact flag opened at [[cycle-0009]] Gate 2 stands and now has a second entry. Two flags on the same actor in one campaign is the arc-review trigger at QUARTERLY-AUDIT; it fired.

**Completed:** 2026-07-02T16:45:00

## Considered Moves

| Tactic ID | Title (Catalogue) | Status | Why surfaced / why rejected |
|-----------|-------------------------------|--------|------------------------------|
| 0380 | The Skip-Level Gambit | **Rejected at § 11** | The obvious tactical move: get the item calendared without the committee. Rejected here on the same grounds it was rejected in Cycle-0007 — audit-committee exposure via Carol's independent reporting line, and it would make the item procedurally dirty, which is the one property the parent cycle needs it to have. Rejecting the same tactic twice for the same reason is a signal the boundary is real. |
| 0044 | Strategic Benevolence | **Rejected pre-gate** | Reciprocity activation against Carol. Rejected on her documented behavioural prior (acts on data, not relationships) and on Cycle-0005's direct evidence. Not an ethics rejection — a fit rejection. |
| 0158 | The Favor Bank Run | **Rejected at § 11** | Called in as the boundary case again: spend accumulated obligation across the committee to force the clearance. Wildly disproportionate to a routine filing, and terminal. Kept in the record as the considered-and-rejected marker, same as in the parent cycle. |

## Selected Moves

**None from the Catalogue.** All three considered tactics were rejected — two at Gate 2, one on fit. The selected move is non-catalogue: a complete, standard-form clearance filing submitted through the committee secretary with full supporting documentation, preceded by a direct heads-up to Carol.

This is worth pausing on, because the shipped example otherwise risks teaching that a cycle's output is a tactic ID. `plc_Tactic_IDs_Selected` is empty and `plc_Strategy_Number_Selected` is 0 — both are legitimate states. The gates did their job by clearing the field, and what remained was the boring legitimate route.

## Engaged Moves

Status flipped `active` → `engaged` 2026-07-03T09:00:00.

### Move 1: non-catalogue — standard-channel clearance filing
- Engaged: 2026-07-03T09:00:00 (heads-up call to Carol 08:40; filing submitted 09:00)
- Slash address: `Sam: [Α/i.1/o./g3/i./o./g1/e.]`
- Target actor: [[actor-carol-cfo]]
- Intended outcome: P/c − and Adv/c + — consent-clearing becomes the default; an unexplained hold becomes the irregular option

## LSPI Configuration ⟨C; M; S; R⟩

- **C — active cycle:** `C10`, held from the 07-02 spawn to the 07-08 nested close, then returned to `C9` by the parent's resume. C is a pointer, not a counter.
- **M — operation record:** below. Append-only. Every path in it carries the parent prefix `Α/i.1/o./g3/`, so the record says *where this cycle came from* without a separate field having to.
- **S — suspended-parent stack:** `[C9]` for this cycle's whole life. `plc_Suspended_Parent` is the file-level shadow; S is popped by the parent's `⟨resume, C9, q⟩`, not by this cycle's close.
- **R — resource holdings:** canonical in [[principal-sam-ceo]] § Current Resource Holdings. This cycle deducted one board-secretary filing slot (2 → 1) at its execution and appended one clearance at its nested close. Both appear exactly once there.

Δ is a derived fold over M. Not stored here, not stored anywhere.

## LSPI Operation Record (M)

- 2026-07-02: ⟨open, C10⟩ — spawned by ⟨gate-fail, [Α/i.1/o./g3/q.]⟩ in C9; parent suspended, S = [C9]
- 2026-07-02: `[a.]ι(Α/i.1/o./g3/i.)` := { [Α/i.1/o./g3/i./Q.] } — the Interest **is** the parent's missing q: finance-committee procedural clearance on the Q3 succession item
- 2026-07-02: `[a.]δ(Α/i.1/o./g3/i./d.)` := { [Α/i.1/o./g3/i./t.], [Α/i.1/o./g3/i./t./D./P.], [Α/i.1/o./g3/i./t./D./X.] } — detection from the Actor file's behavioural prior; no Detection Record opened (see Landscape Assessment for why the absence is a decision)
- 2026-07-02: `[a.]ω(Α/i.1/o./g3/i./o.)` ≡ { [Α/i.1/o./g3/i./t.]Σ(Α/i.1/o./g3/i./t./D.)′ → [Α/i.1/o./g3/i./t./S./P.]′ } — projected: Carol clears the item through standard consent
- 2026-07-02: `[a.]γ(Α/i.1/o./g3/i./o./g1)` ≡ { [Α/i.1/o./g3/i./t.]Γ(Α/i.1/o./g3/i./t./D./G.)′ = { [Α/i.1/o./g3/i./t./D./P./u.]′ > [Α/i.1/o./g3/i./t./D./X./u.]′ } } — K = 1
- 2026-07-02: `[a.]θ(Α/i.1/o./g3/i./o./g1)` := { [Α/i.1/o./g3/i./o./g1/q.] } — one board-secretary filing slot. One q, one gate test.
- 2026-07-03: ⟨gate-pass, [Α/i.1/o./g3/i./o./g1/q.]⟩ — `[a./R.] ∋ q` (2 slots held this quarter)
- 2026-07-03: `[a.]ε(Α/i.1/o./g3/i./o./g1/e.)` → { [Α/i.1/o./g3/i./t./D./P./c.] − + [Α/i.1/o./g3/i./o./g1/q.] } — filing submitted; one slot consumed
- 2026-07-07: `[Α/i.1/o./g3/i./t.]Γ(Α/i.1/o./g3/i./t./D./G.)` = { [Α/i.1/o./g3/i./t./D./P./u.] > [Α/i.1/o./g3/i./t./D./X./u.] } — realized perception. ⟨perceive, g_1⟩ — **validated**. Carol cleared the item on the consent agenda and attached a note reserving the committee's right to comment at the board session.
- 2026-07-08: ⟨select-staged, [Α/i.1/o./g3/i./t.]Σ(Α/i.1/o./g3/i./t./D.) → [Α/i.1/o./g3/i./t./S./P.]⟩
- 2026-07-08: `Ω(Α/i.1/o./g3/i./O.)` ≡ { [Α/i.1/o./g3/i./t.]Σ(Α/i.1/o./g3/i./t./D.) → [Α/i.1/o./g3/i./t./S./P.] } — outcome. The realization sits alongside the 07-02 projection; the projection is not overwritten.
- 2026-07-08: `[Α/i.1/o./g3/i./t.]Λ(Α/i.1/o./g3/i./O./U.)` := { [Α/i.1/o./g3/i./t./D./P./u.] } — obtained utility, target-side. Small and honest: what Carol gained is a clean committee record, which is worth something to her and is not what Sam paid.
- 2026-07-08: ⟨close-nested, C10, C9⟩ — `[a.]Φ(Α/i.1/o./g3/i./O./Q.)` := { [Α/i.1/o./g3/i./Q.] } and ⟨flowback-recorded, { [Α/i.1/o./g3/i./Q.] }⟩. Parent R ⊎ E. **Φ's body equals ι's body** — the cycle obtained exactly the resource it opened for. That identity is the normal-path property, not a rule: a mooted or abandoned sub-cycle would have obtained nothing and the parent's resume would correctly not have fired.
- 2026-07-08: *(the parent's ⟨resume, C9, [Α/i.1/o./g3/q.]⟩ is logged in [[cycle-0009]], not here — resume pops S in the parent's record, and duplicating it here would put one event in two places)*

## σ / Guard Log

| Date | Kind | State | Admissible options | Pick | Rationale |
|------|------|-------|--------------------|------|-----------|
| 2026-07-02 | σ | ⟨open, C10⟩, interest declared | scope the interest to the missing q / widen it to "shift Carol's posture" | scope to the q | a sub-cycle that widens past the missing resource stops being an acquisition. Carol's posture is a campaign-level question and belongs to a cycle of its own, not to a suspended parent's errand |
| 2026-07-02 | σ | ω-body written | declare one intention / declare filing + a parallel procedural-fairness invocation | one intention | the second lever is only needed if the first is refused, and pre-declaring it would spend design attention on a branch the behavioural prior says is unlikely. Held in reserve, not declared |
| 2026-07-03 | guard | θ-body | ∋ / ∌ | **∋** | two board-secretary filing slots held this quarter; the multiset says two, which is why spending one is affordable and spending both would not be |
| 2026-07-07 | guard | ε-body | perceive-validates / perceive-fails | **validates** | item cleared on the consent agenda. The attached reservation was read against the projection and does not defeat it — the projection was clearance, not endorsement, and reading a reservation as a failure would be scoring against a wish rather than a forecast |
| 2026-07-08 | σ | ⟨perceive, g_1⟩, all live intentions terminal | select and close / declare a further intention to pre-empt the reservation | select and close | the reservation costs the parent nothing. Chasing it would widen the sub-cycle after the resource was already in hand — the acquisition-creep failure |

## Intention Positions
- g_1: declared 2026-07-02 → resourced 2026-07-02 → gated ∋ 2026-07-03 → executed 2026-07-03 → perceived (validated) 2026-07-07. Terminal.

K = 1, so the per-intention tracking is nearly trivial here. Kept anyway: a sub-cycle that skips it because it is short is a sub-cycle whose escalation path cannot be replayed.

## Phase Log

- 2026-07-02: Spawned by the parent's gate failure. Opened at `planning`; both gates walked and closed the same afternoon.
- 2026-07-03: Heads-up call to Carol 08:40 — she asked two questions about the documentation, both answerable, and did not comment on the item's substance. Filing submitted 09:00. Status `active` → `engaged`.
- 2026-07-07: Committee consent agenda circulated; item cleared, with Carol's attached note reserving the right to comment at the board session. No hold, no request for substantive review.
- 2026-07-08: Cycle closed; clearance flowed back to Sam's holdings; parent resumed at its gate the same day.

## Refinement

**OPC updates pushed back to [[opc-2026-06-01]]:** § 6.2 gains the family-bloc clearance convention (succession-adjacent items clear the finance committee before the board calendar). It was governing the parent cycle from its start and was absent from the diagnostic — a structural fact, not a signal, which is why no amount of probing Robert surfaced it and one conversation did.

**Principal funnel:** unchanged.

**Reciprocal updates applied:**
- [[actor-carol-cfo]]: `plc_Last_Updated_Cycle` → cycle-0010; Perception History appended (`defensive` **held**)
- [[cycle-0009]]: `plc_Spawned_Subcycles` ↔ this cycle's `plc_Suspended_Parent`
- [[principal-sam-ceo]]: filing-slot deduction and clearance append recorded in the holdings ledger
- [[campaign-succession-q3]]: cycle-0010 added at open, removed at close

## Lessons

**What worked:**
- **Scoping the sub-cycle to the missing resource and nothing more.** The σ at open is the load-bearing one: "shift Carol's posture" was available and would have turned a six-day acquisition into an open-ended campaign inside a suspended cycle.
- **Asking Carol to use her authority rather than to waive it.** Funnel criterion #2 is about not enlarging her control; exercising authority she already holds does not, and the distinction is what let a `defensive` actor be routed through rather than around.
- **The behavioural prior did the work a probe would have.** Carol's file said what she responds to, and it was right. A Detection Record here would have been ceremony.

**What didn't work:**
- **The clearance convention should have been in the diagnostic.** It cost the parent eleven days of plan aimed at the wrong position. OPC § 6 was walked at the 06-01 diagnostic and captured decision *rights*; it did not capture decision *procedure*. Carry: § 6 walks ask what must happen before an item reaches a decision body, not only who may decide.
- **The reservation was not anticipated.** It cost nothing, but nothing in the plan predicted it either. A one-member plan has no redundancy, which is fine when the margin is small and worth stating when it is not.

**What to carry:**
- One filing slot remains this quarter.
- Carol's clearance is **not** evidence of a posture shift. Her Actor file says so explicitly, because the temptation to read compliance as warming is exactly what the perception-gap discipline exists to catch.

## Cross-References
- Sphere: [[acme-corp-manifest]] · Campaign: [[campaign-succession-q3]] · Principal: [[principal-sam-ceo]]
- **Suspended parent: [[cycle-0009]]** (reciprocal: that cycle's `plc_Spawned_Subcycles`)
- Actors touched: [[actor-carol-cfo]], [[actor-robert-board-chair]]
- OPC diagnostic referenced: [[opc-2026-06-01]] (§ 6.2 refined at this close)
- Sessions: [[2026-07-02_012_RUN-CYCLE]], [[2026-07-08_013_RUN-CYCLE]]
- **No `precedes` / `follows` edge, and the absence is the point.** This cycle's only relation to [[cycle-0009]] is the spawn pair above — suspended parent ↔ spawned sub-cycle. Cycle-0009 is not this cycle's temporal predecessor: it did not run *before* this one, it was suspended *around* it, and it is the cycle holding control again the moment this one closes. An earlier version of this line read "Prior cycle: [[cycle-0009]]", which asserts a `follows` edge whose reciprocal a parent cannot carry — cycle-0009 would have had to name its own sub-cycle as its successor. A sub-cycle takes no position in the sequence its parent occupies; its place in the record is the escalation address (`Α/i.1/o./g3/i.`), which says where it came from more precisely than a sequence edge could

## Citation Repair — 2026-07-25

Appended. Two Considered-Moves entries named tactics that do not exist under those names: `0112` is **Lexicon Control** on disk, not "Pre-Board Chair Briefing," and `0044` is **Strategic Benevolence**, not "Coalition Signal Exchange." The Carol-bypass row is re-pointed to **`0380` The Skip-Level Gambit**, whose Catalogue mechanism — bypassing the immediate chain to reach senior leadership directly — is exactly the move rejected here and in [[cycle-0007]]. `0158` was already correct.

The column header read "Name (as used in this sphere)." That hedge is worth naming rather than deleting quietly: a local alias column is how four fabricated tactic names survived an audit, because it makes a false citation look like a naming convention. The header is now **Title (Catalogue)**, which is a claim that can fail. Full sweep at [[2026-07-24_015_QUARTERLY-AUDIT]] § Citation Audit.
