---
type: PLC_Actor
timestamp: "2026-06-13T00:00:00Z"
Item_ID: actor-robert-board-chair
title: "Robert Hayes — Board Chair (family)"
Date_Added: 2026-04-22
Date_Modified: 2026-07-15
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Actor_Name: "Robert Hayes"
plc_Actor_Role: "Board Chair (family director)"
plc_Hierarchical_Position: board
plc_Current_Perception_Toward_Principal: ambivalent
plc_Network_Distance_From_Principal: 1
plc_Resources_Held: [legitimacy, access, title, tribe, other]
plc_Coalitions: []
plc_Opposed_By: []
plc_Actor_Completeness: 4
plc_Last_Updated_Cycle: "[[cycle-0009]]"
plc_Estimated_By:
  - "[[detection-robert-board-chair]]"
plc_Depth_Estimate: "ℓ̂_T ≈ 1 (cr: 1 → 0.60, 2 → 0.28, 0 → 0.12); as of 2026-07-01. Working, uncalibrated — full trail in [[detection-robert-board-chair]]."
AI_Instructions: ""
---

# Robert Hayes — Board Chair (family)

## Current

### Profile
Board chair (family director). Family principal's brother-in-law; second-generation family in board capacity for 12 years; chair for the past 5. Background: regional banking executive (retired 2021). Tenure on Acme board predates Sam's CEO appointment by 8 years. Position in family voting bloc: respected elder; tie-breaking voice when the bloc splits. Public posture: deliberative, consensus-preferring, slow to take controversial positions.

**OPC archetype (propagated from [[opc-2026-06-01]] § 2.2.1):** § 2.2.1.3 `the_kingmaker` — controls succession outcomes. Sphere extension: preservationist disposition; institutional-stewardship frame.

### Perception Toward Principal
**Ambivalent** as of 2026-06-13. Not actively opposed; not reliably allied. The swing in the 3-1 family voting bloc — if Robert shifts toward Carol's framing of operational conservatism, the bloc moves 2-2 and Sam loses his unilateral preserve. If Robert holds with Sam, the bloc remains 3-1 and Sam's mandate is preserved through ratification.

**Why ambivalent (not defensive):** No detection-signal pattern matching opposition posture. Communication channels with Sam remain intact (regular monthly 1:1s preserved); board-meeting interactions remain professional and collaborative on operational matters. The ambiguity is on succession-specific framing, not on Sam personally.

**Key uncertainty for the engagement:** Robert's prior relationship with Carol (regional-CFO colleagues 2014-2016 at a different firm — surfaced at Cycle-0006 UNCOVER work) introduces information-flow risk. Carol may be shaping Robert's read of Sam's operational performance through that backchannel.

### Resources Held

Per-resource effect signature (which decision-matrix cells it can move, and in which direction, **conditional on the target**), rough cost to deploy, and durability. Signatures are ordinal reads, not measurements (P13) — they rank what Robert can move, they do not quantify it.

- **Legitimacy** — board-chair role; family-elder standing; tie-breaker authority on bloc-internal disagreements.
  - *Effect:* `P/b +` and `Adv/c +` for whichever side he visibly backs. **Target-conditional:** strong on the family bloc, near-zero on the three independents, who read him as a family voice rather than a neutral one.
  - *Cost:* high — every deployment spends visible impartiality, which is the input that makes the resource work at all.
  - *Durability:* durable (role-anchored); the impartiality that powers it is **fragile**.
- **Access** — direct line to all board members (formal); direct line to the family voting bloc (informal, kinship-based); historical relationship with Carol (regional-CFO colleagues 2014-2016; not currently activated but available).
  - *Effect:* moves no cell by itself. **Enabling** — it is the carrier other resources ride on. Recorded because a resource that moves nothing directly is exactly the one a naive read over-prices.
  - *Cost:* near-zero to use; the Carol channel costs deniability if used visibly.
  - *Durability:* durable. The Carol channel is dormant-but-live — dormancy is not absence.
- **Title** — board-chair agenda authority; controls what reaches formal consideration.
  - *Effect:* `P/c −` (an item he puts on the agenda arrives with the friction already paid) and `Adv/b −` (an option not on the agenda has no benefit path).
  - *Cost:* low per use but **capped** — one or two agenda impositions per calendar before the bloc reads it as steering.
  - *Durability:* durable while he chairs; fragile against a chair rotation, which is inside the succession question itself.
- **Tribe** — family voting bloc membership; second-generation cohort standing.
  - *Effect:* `P/b +` within the bloc only. Zero outside it.
  - *Cost:* low. *Durability:* durable — kinship does not lapse.
- **Other — procedural motion standing on succession-adjacent items** (surfaced 2026-07-01, cycle-0009).
  - *Effect:* `P/c −` specifically for succession-adjacent agenda items — he can move a cleared item at the calendar-lock session and speak for it on the record. This is the resource cycle-0009's revised objective actually turns on.
  - *Cost:* low, and notably lower than the Title route, because moving a **procedurally-cleared** item spends no impartiality.
  - *Durability:* durable — it rides the family-bloc convention, not his office.
  - *Carrier note:* filed under `other`, not forced into `title`. It is a procedural/decision right; the dissertation's nine-type basis is a basis of **carriers for elicitation**, not a partition, and it has no box for decision rights (`08-ESTIMATION` § The actuator). `other` was added to the enum in v1.2 for exactly this case. Forcing it into `title` would have hidden the thing that made the cycle work — the standing belongs to any family director, not to the chair.

### Convertibility Edges

Edges Robert's resources participate in, with edge type and a rough sphere-indexed rate. Rates are estimates like everything else here — estimation all the way down.

- `title (agenda authority)` ⇝ `legitimacy (board-visible endorsement)` — **transfer**, rate ≈ 1 per calendar, non-repeatable within a window. Putting an item on the agenda transfers some of his standing to it.
- `tribe (elder standing)` ⇝ `legitimacy (bloc tie-break)` — **earn-sanction**. The bloc grants the tie-break and can withdraw it; the rate is high but wholly conditional on visible impartiality. This is the edge Sam most often misreads as unconditional.
- `access (Carol channel)` ⇝ `information` — **transform**, low rate, currently dormant. Available to Carol as much as to Robert; the edge is not Sam's to use.
- `other (procedural motion standing)` ⇝ `legitimacy` — **transfer**, rate ≈ 1 per item, and — the point — **it does not draw on impartiality**, because the procedure, not Robert, certified the item.

**Gain-cycle test: negative.** The tempting read is that `tribe ⇝ legitimacy ⇝ title ⇝ (agenda control reinforcing elder standing)` is a compounding loop. Walked as a loop, its rate-product sits at or below 1 in this sphere: each turn consumes visible impartiality, which is the same input the first edge requires. That makes it a **depreciating loop, not a gain-cycle** — a bare loop with rate-product ≤ 1 compounds nothing (`08-ESTIMATION` § Convertibility). Recorded as a negative result on purpose: the failure mode is calling every loop a flywheel.

**Protection:** Robert spends durable low-yield impartiality signalling — the visible even-handedness, the habit of surfacing his read last — to defend the fragile high-yield tie-break. Reading the even-handedness as indecision, which is Sam's standing temptation, mistakes the defence for the disposition.

### Estimated Matrix Summary

Current best read of how Robert loads keep-vs-relinquish on the live question, as of 2026-07-15. Summary only — the differential, the pre-registered probes and the trail live in [[detection-robert-board-chair]].

The question ran against the wrong position for most of cycle-0009. Estimated against **P.1** (co-sign the Q3 framing on his own chair authority), Robert's margin was adverse and, on the evidence now available, probably never movable — the ask required him to spend the impartiality his whole position is built to protect. Estimated against **P.2** (move the procedurally-cleared item at the calendar-lock session and speak for it), the margin is **mildly favorable and was already favorable before any lever landed**: P.2 costs him nothing he is defending.

Direction: favorable on P.2, holding. What moved the estimate was not a probe but a **revision** — the read of what to ask for changed, and the margin changed with it. Depth settled at ℓ̂_T ≈ 1 (was 1–2) on the same observation.

The standing caution is unchanged and now better evidenced: Robert's loyalty is to the family-ownership institution, not to the CEO the family installed. Under P.2 that is a *reason he moves*, not an obstacle — the item's procedural cleanliness is what he is endorsing. Nothing here says he would hold under a Carol bid that arrived equally clean. That question has not been probed and is not answered by this cycle.

### Network Position

- **Coalitioned with:** None currently mapped at this completeness level. Family voting bloc affiliation is implicit but not formalized as a coalition relation (the bloc is a structural position, not an active coalition).
- **Opposed by:** None currently
- **Brokers between:** Family voting bloc ↔ board independents (this is the high-leverage brokerage position); also potentially family-bloc ↔ Carol via the historical relationship (active brokerage potential)

### Behavioral Notes

Slow to commit; values deliberation; values being seen as fair across factions. Coaching theme observation (Sam's coaching): Robert's family-loyalty does NOT automatically translate to political alignment with Sam — Sam underweights this. Robert's loyalty is to the family-ownership institution, not to whichever CEO the family has installed. If Carol's framing positions her as the better guardian of family-institutional interests (vs. Sam's framing positioning himself as the operating-mandate guardian), Robert's vote follows institutional loyalty rather than CEO loyalty.

Decision style: tends to surface his read at the END of board discussions, not the beginning. Implication: detection signals on Robert's positioning come late in board cycles; pre-board work on Robert is high-leverage.

## Perception History

- 2026-07-15: `ambivalent` **held** at Cycle-0009 close. Robert moved the cleared succession item at the calendar-lock session and spoke for it on the record. Deliberately not read as a shift to `allied`: he endorsed a procedurally-clean item, not Sam, and the same act was available to any family director. Completeness 3 → 4, with one leg weaker than the other: the multi-cycle resource trajectory is now genuinely there (baseline → Carol channel → effect signatures and durability → the `other`-carrier standing), but level 4 also asks for opposition mapping and Robert has none to map — `plc_Opposed_By` is empty and the body says so. Recorded as a caveat rather than waved through, because inflating the scale is how an intelligence gap gets hidden behind a number. (Source: [[cycle-0009]] § Refinement, session [[2026-07-15_014_RUN-CYCLE]].)
- 2026-07-01: Depth estimate revised ℓ̂_T 1–2 → ≈ 1 on the joint-pre-meeting observation; cr(H1) 0.55 → 0.60. Robert named the finance-committee clearance convention unprompted and supplied the alternative route himself — a costly, checkable disclosure a depth-2 broker would not volunteer. Prior signals re-decoded. Not a probe; no pre-registration. (Source: [[detection-robert-board-chair]] § Post-stop observation, session [[2026-07-02_012_RUN-CYCLE]].)
- 2026-06-27: `plc_Estimated_By` wired to [[detection-robert-board-chair]]; estimated-matrix summary and depth estimate written to this file; per-resource effect signatures, durability and convertibility edges recorded. (Source: [[cycle-0009]], sessions [[2026-06-20_010_ESTIMATE]] + [[2026-06-27_011_RUN-CYCLE]]. **These writes were claimed by sessions 010 and 011 and not in fact applied at the time; applied 2026-07-24 as an F5 repair — see [[2026-07-24_015_QUARTERLY-AUDIT]]. Dated to the sessions that claimed them, with the repair date stated rather than hidden.**)
- 2026-06-13: Confirmed `ambivalent` at Cycle-0008 cold-reading. No shift; status held. Cycle-0008's central question is whether Robert moves toward or away from Carol's framing.
- 2026-06-09: Network position fully mapped (completeness 2 → 3); Carol-historical-relationship surfaced at Cycle-0006 UNCOVER and propagated to this file.
- 2026-04-29: Reviewed at first OPC partial diagnostic; status held `ambivalent`.
- 2026-04-22: Baseline at sphere-open — `ambivalent` (family-loyalty assumption from Sam noted as uncoaching-baseline; coaching theme flagged for revision).

## Resource History

- 2026-07-01: `other` — procedural motion standing on succession-adjacent items surfaced. Not newly acquired; it was always held and never elicited, because the nine-carrier walk has no box for a decision right and the walk is what the elicitation used. Recorded under the v1.2 `other` carrier. (Source: [[cycle-0009]] § LSPI Operation Record, 2026-07-01 perceive.)
- 2026-06-27: Effect signatures, deployment costs and durability recorded per resource; convertibility edges mapped; gain-cycle test run on the `tribe ⇝ legitimacy ⇝ title` loop and returned **negative** (depreciating, rate-product ≤ 1). No resource gained or lost — this is a pricing entry, not a transfer. (Source: [[cycle-0009]] augmented gate, session [[2026-06-27_011_RUN-CYCLE]]; applied 2026-07-24 per the F5 repair noted above.)
- 2026-06-09: Carol-relationship surfaced (resource not newly acquired — historical relationship now visible); added to access resources.
- 2026-04-22: Baseline — board chair; family elder standing; access to bloc + board.

## Cross-References

- Sphere: [[acme-corp-manifest]]
- Most recent cycle: [[cycle-0009]] (closed 2026-07-15; Robert's swing-vote alignment is the cycle's central work)
- Estimated by: [[detection-robert-board-chair]] (reciprocal: that record's `plc_Target_Actor`)
- Prior cycles referencing: [[cycle-0008]] (Robert coalition mapping), [[cycle-0006]] (UNCOVER surfaced Carol-historical-relationship)
- Member of campaign: [[campaign-succession-q3]] (swing actor in the campaign cohort)
- Pattern manifestation: [[pattern-family-succession-pressure-loop]] (Robert's positioning is a critical inflection point in the pattern's lifecycle)
