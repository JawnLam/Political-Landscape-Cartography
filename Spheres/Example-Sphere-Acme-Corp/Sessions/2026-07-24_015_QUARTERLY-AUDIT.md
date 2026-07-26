---
type: PLC_Session
timestamp: "2026-07-24T00:00:00Z"
Item_ID: session-acme-corp-015
title: "Acme Corp — Session 015 — QUARTERLY_AUDIT"
Date_Added: 2026-07-24
Date_Modified: 2026-07-24
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Session_Number: 15
plc_Activity: QUARTERLY_AUDIT
plc_Session_Started_At: "2026-07-24T09:00:00"
plc_Session_Ended_At: "2026-07-24T13:30:00"
plc_Operator_Mode: consultant
plc_Files_Touched:
  - "[[actor-robert-board-chair]]"
  - "[[actor-carol-cfo]]"
  - "[[actor-elena-independent-director]]"
  - "[[principal-sam-ceo]]"
  - "[[detection-robert-board-chair]]"
  - "[[opc-2026-06-01]]"
  - "[[cycle-0007]]"
  - "[[cycle-0008]]"
  - "[[cycle-0009]]"
  - "[[acme-corp-state]]"
plc_Reciprocal_Update_Count: 7
plc_Next_Activity_Recommended: RUN_CYCLE
plc_Next_Activity_Chosen: later
AI_Instructions: ""
---

# Acme Corp — Session 015 — QUARTERLY_AUDIT

## Activity Recap
First quarterly audit of the engagement (90-day forced cadence from sphere-open 2026-04-15). Base protocol walked in full, plus the consultant-mode additions. The audit found more than a healthy sphere should: an F5 cluster of writes that three session logs claimed and none had applied, an evidence chain terminating in a section that did not exist, and one ill-typed expression in the cycle file the engine points other cycles at. All repaired, all logged.

The pleasant finding is separate and real: the Persistence Invariant paid for itself the first time it was asked to. Cycle-0009 retained both its original and revised projections alongside the realized outcome, and the forecast-calibration pass had something to read.

## Files Touched
- `[[opc-2026-06-01]]`: § 2.4 political-intensity reading **back-filled** (nine indicators, `elevated-structural` band, the two-sided loss justifying `b = 0.5`, the re-read trigger, and the scale-provenance flag); Headline Reads gains an intensity line; Score History appended
- `[[detection-robert-board-chair]]`: citation corrected from "opc-2026-06-01 § 13" to § 2.4; correction stated in the body rather than silently re-pointed
- `[[actor-robert-board-chair]]`: `plc_Estimated_By` wired; `plc_Depth_Estimate` populated; per-resource effect signatures, costs and durability written; `### Convertibility Edges` and `### Estimated Matrix Summary` added; `plc_Resources_Held` gains `other`; OPC archetype propagated
- `[[actor-carol-cfo]]`, `[[actor-elena-independent-director]]`: OPC archetype assignments propagated (session 007's claim made true); Elena's coalition note applied
- `[[principal-sam-ceo]]`: `### Current Resource Holdings` opened as an explicit multiset with the transaction ledger and conservation check
- `[[cycle-0007]]`, `[[cycle-0008]]`: slash constituents normalized (F9/F10 repair); normalization notes appended
- `[[cycle-0009]]`: one malformed expression repaired in place with the repair recorded at the record
- `[[acme-corp-state]]`: cross-references corrected to describe what is on disk; `plc_Active_Cycles_Count` corrected

## Decisions Made
- **Cycle-level:** none — no cycle ran.
- **Sphere-level:** none elevated. Considered and declined: elevating "the shipped Catalogue cannot carry reciprocal pointers" to `_sphere-decisions.md`. It is an engine fact, not a sphere decision, and belongs in the audit record where a future operator meets it in context.
- **Not taken:** the seal on [[cycle-0007]] and [[cycle-0009]]. Both are past or near their grace windows and both would satisfy the shipping checklist's "at least one sealed cycle" item if flipped. The D → E flip is operator-explicit (P10) and was not requested. Proposed and left open rather than done — sealing a cycle to satisfy a checklist would be the checklist driving the record, which is backwards.

## Reciprocal Updates Applied
7 updates, all repairs of writes claimed by earlier sessions and never applied: `actor-robert.plc_Estimated_By` ↔ `detection-robert.plc_Target_Actor` (the estimates / estimated-by pair, the central F5); Robert's depth estimate propagated from the record; Sam's holdings multiset opened against cycle-0009's gate claims; Elena's coalition note; three OPC archetype propagations (Robert, Carol, Elena) from the 06-01 diagnostic.

## Gate Outcomes
N/A — no cycle ran, so neither accounting gate applies. Noted rather than omitted, per the F8 discipline: an empty gate field must be explained, not left blank.

## Activity-Specific Block (QUARTERLY_AUDIT)

### 1. Perception-gap audit
- **Robert.** The standing coaching theme — Sam over-reads operational engagement as loyalty — held again, in a new shape. The gap this quarter was not about warmth; it was about *capacity*. Sam's read had Robert able to co-sign on his own authority, and Robert could not. Both the estimate and the funnel's success criterion inherited that error. Reframed coaching line: before asking whether the actor is willing, ask whether the act is his to perform.
- **Carol.** Fresh gap, opened this quarter: Sam read the 07-07 clearance as a thaw. It was not, and her file now says so explicitly with the reasoning attached. Compliance from a `defensive` actor on a procedurally ordinary item is evidence about the procedure.
- **Elena.** No gap. One caveat logged: two observations inside a fortnight against a normally quarterly signal is a warmer read than her file usually supports.
- Chronic pattern: 2 of 4 tracked actors carry an active perception-gap theme. Not alarming at this stage of an engagement; worth watching if it reaches 3.

### 2. Eight Benefits of Power inventory
Trend since sphere-open: **up on two, flat on six.** Meeting-agenda influence rose materially — Sam's item reached the calendar-lock session with the board chair moving it. Frequent access to higher decision-makers rose slightly via the Elena channel. No movement on comp influence, favored-subordinate opportunities, exceed-limits authority, assist-someone-in-need, fast superior response, or advance org updates. Directional read only; no baseline calibration exists for this sphere.

### 3. Actor-trajectory review
- `[[actor-david-coo]]`: **untouched since 2026-06-09** — 45 days. That is **under** the 90-day staleness trigger (`03-SESSION-PROTOCOL` § QUARTERLY-AUDIT step 3), so the cadence rule does not fire and this is not a staleness finding. ACTOR-UPDATE proposed anyway, on consequence rather than on age: David sits at completeness 1 (stub — no behavioral notes, no resource history), he is Carol's coalition partner, and the predicted Q3 procurement bid runs through operations. A stub on the path of the next predicted inflection point is worth advancing at 45 days; the rule would have let it sit another 45.
  - *Repaired in place rather than silently.* This row first read "untouched since 2026-04-15 — 100 days." 2026-04-15 is the **sphere-open** date, not David's last touch: his file carries `Date_Modified: 2026-06-09` and a Perception History entry that day. The proposal survived the correction; its **basis** did not — as first written it reported a threshold crossing that never happened. An audit is the one file whose arithmetic no other file checks.
- Independent-Director-2 and -3: still outside the active cast; queued since Cycle-0007's Lessons and now twice-deferred.
- Robert, Carol, Elena, Sam: all current.

### 4. Forecast-calibration review (projected ′ vs realized)
The Persistence Invariant's payoff, run for the first time in this sphere.

| Projection (with date) | Realized | Read |
|---|---|---|
| `[a.]ω(Α/i.1/o.)` 06-24 → `[Α/i.1/t./S./P.1]′` — Robert co-signs on chair authority before the lock | never realized; superseded 07-02 | **Miss, and the informative kind.** The projection was not merely optimistic — it was aimed at an act the target could not perform. Both bodies are still in the record, which is the only reason this row can be written at all. |
| `[a.]ω(Α/i.1/o.)` 07-02 → `[Α/i.1/t./S./P.2]′` — Robert moves the cleared item and speaks for it | `Ω(Α/i.1/O.)` 07-15, matching | **Hit**, at 13 days. |
| `γ_1` 06-24 → `[Α/i.1/t./D./P./b.]′ +` | partial validation 06-25 | Hit, weakly. Under-separated at the time and still is. |
| `γ_2` 06-27 → `[Α/i.1/t./D./X./c.]′ +` | validated 07-01 | Hit. |
| `γ_3` 07-02 → `P.2/u.′ > X/u.′` | validated 07-15 | Hit. |
| cycle-0010 `ω` 07-02 → Carol clears via consent | realized 07-07 | Hit, at 5 days. |

**Systematic bias flagged:** 1 of 6 projections missed, and the miss was structural rather than directional — the forecasts about *effects* were good, and the forecast about *what the target could do* was wrong. That is not an overshoot/undershoot pattern the arithmetic can correct; it is an under-specified differential. One quarter is not a calibration record and nothing here graduates to an answer (P13).

### 5. Belief-hygiene review
- **[[detection-robert-board-chair]]:** differential refreshed 07-01, depth re-estimated, stop decision re-checked after the revision. Not stale. One structural weakness logged in the record itself: both live hypotheses were dispositional, and the binding fact was institutional. Carry into the next differential.
- **Held-resource worth estimates:** re-priced after the 07-01 observation — the Elena member's realized worth as a margin-mover was lower than priced, its worth as context far higher; the co-sign ask re-priced sharply upward once the item was clean.
- **Resource conservation across the quarter's spawn/flowback chain (Theorem 13.4):** walked line by line against [[principal-sam-ceo]] § Current Resource Holdings. Two resources obtained, each appended exactly once; five spent, each deducted exactly once; the clearance appears once on the obtained side and once on the spent side and never in both places at once. **No leaks, no duplications.** One honest gap: g_1's delivery attention was spent without a `θ`/`ε` pair, so it is conserved in the Principal's ledger and invisible to LSPI's. Recorded in both places rather than netted away.

### 6. Reciprocal-update audit (F5)

Every session log in the sphere checked against the graph as it actually stands.

| Session | Count claimed | Verified now | Disposition |
|---|---|---|---|
| 000 SPHERE-OPEN | 4 | 4 | Holds. |
| 007 OPC-DIAGNOSE | 5 | 5 | 3 archetype propagations were claimed and were **not** in the Actor bodies; applied today. The seed-diagnostic `plc_Superseded_By` write targets `opc-2026-04-22-seed`, which is not shipped in this cartridge — counted as standing, since the pointer on the surviving side is correct. |
| 009 RUN-CYCLE | 7 | **4** | 2 Tactic `plc_Cited_In_Cycles` writes (0044, 0156) and 1 Theorist `plc_Invoked_In_Cycles` write (Schelling) are **structurally impossible**: the shipped Catalogue is Mode E and ships without frontmatter, so there is no slot to write into. The log states they were "actually applied," and they were not and could not be. |
| 010 ESTIMATE | 4 | 4 | Holds — but only as of today. `plc_Estimated_By` did not exist on Robert's file until this session. |
| 011 RUN-CYCLE | 6 | **5** | The claim list counts `0044 ↔ cycle` in "both directions"; the Catalogue direction is impossible, so that item contributes 1, not 2. Two further claims — actor↔detection and the campaign's active-cycles entry — were never applied and were applied today. |
| 012 / 013 / 014 RUN-CYCLE | 3 / 5 / 6 | 3 / 5 / 6 | Hold. |

**Repairs applied:** 7 (listed above). **F5 incident count: 1 cluster spanning sessions 010 and 011**, plus the session-007 archetype gap. That is above the three-in-one-audit threshold for a workflow review only if the cluster is counted per-write; counted per-incident it is two. The distinction is not worth arguing — the discipline that failed is the same one in both cases, and it is named in Open Threads.

**Session frontmatter left as written.** `plc_Reciprocal_Update_Count` on sessions 009 and 011 still reads 7 and 6. PLC_Session is Mode A: correcting by mutation is exactly what an append-only record forbids, and a session log that quietly acquires the right number afterwards is worth less than one that carries a visible correction. A `## Reciprocal-Update Audit` block has been **appended** to each of those two logs instead, and to session 010 confirming its count now holds.

### 7. § 16.9 practitioner self-check (consultant mode)
Ten questions walked. Two non-green:
- *"What does my sponsor specifically want me to find? Am I finding it?"* — Sam wants to find that Robert is loyal. The quarter produced something better and less comfortable: Robert is *available*, on the right ask. Worth watching that the engagement keeps reporting the second thing rather than the first.
- *"Am I documenting what I would not want read back to me?"* — this audit is the answer, and the honest version is that three sessions in a row claimed writes nobody verified. The claim-then-verify order was inverted. § 16.8 `disengagement_triggers` remains the standing yellow from 06-01, unchanged and still mitigated.

### 8. § 17.9 engagement health checks
Ten questions walked, all green. Access has widened rather than narrowed; deliverable politics unchanged; no messenger risk surfaced this quarter.

### 9. § 13.2 arc-position review
Intensification points crossed this quarter: § 13.2.1.1 `deadline_compression` (the calendar lock), § 13.2.1.6 `cascade_initiation` (unchanged from 06-01). **Not** crossed: `irreversibility_threshold`, `loyalty_forcing_events`, `alignment_reversal`. Trending toward § 13.2.2.1 `decisive_resolution` on the current read, with § 13.2.2.7 `deferred_resolution` still live if the Q4 window slips. The § 2.4 intensity register is unchanged at `elevated-structural` — none of the four escalation indicators appeared this quarter, so `b` stays at 0.5 and no re-decode is required.

### 10. § 11 retrospective harm review
Two collateral-impact flags on Carol across the campaign (cycle-0009 Gate 2; cycle-0010 Gate 2). Both are foreclosure-of-option and pressure-shaped-ask, both low-severity, neither involving deception or personal cost. Below the threshold Sam set at sphere-open. **Surfaced to Sam anyway**, because two flags on one actor in one campaign is a trend even when each is small, and the point of the threshold is not to be the only time anyone looks.

## Open Threads
- **Claim-then-verify discipline.** The reciprocal-update protocol was being run as a narration step, not as a check. Sessions 012–014 write their counts only against pointers confirmed present. Carried as a standing session-close habit.
- **[[cycle-0008]] has been `engaged` for 41 days** with lessons-extraction deferred since 2026-06-13. Workflow-drift anomaly; either close it or state why it stays open.
- **Seal prompts pending** on [[cycle-0007]] (grace expired 2026-06-17) and [[cycle-0009]] (grace expires 2026-07-22). Operator's call.
- **[[actor-david-coo]] untouched 45 days** — below the 90-day trigger, so this is a judgment call and not a cadence finding. ACTOR-UPDATE proposed on consequence (completeness 1; the predicted Q3 procurement bid runs through operations). Basis corrected in § 3.
- **Re-walk the active cast for `other`-carrier resources.** Robert's procedural motion standing was invisible for three cycles because the nine-carrier elicitation walk has no box for decision rights. That blind spot is in the walk, not in Robert.
- Carol's Q3 procurement-authority bid still unobserved; predicted at opc-2026-06-01 § 14.3.

## Next Activity Recommendation
RUN_CYCLE to close out cycle-0008, or ACTOR-UPDATE on David. Recommending the former first — an aging open cycle distorts every subsequent SCAN.

## Next Activity Chosen
later (Sam is in Q3 close through end of month; both queued for August).

## Cross-References
- Sphere: [[acme-corp-manifest]] · Prior session: [[2026-07-15_014_RUN-CYCLE]]
- Items materially affected: [[opc-2026-06-01]], [[actor-robert-board-chair]], [[principal-sam-ceo]], [[detection-robert-board-chair]]
- Cycles audited: [[cycle-0007]], [[cycle-0008]], [[cycle-0009]], [[cycle-0010]]

## Citation Audit — appended 2026-07-25

The reciprocal-update audit in § 6 caught that session 009's Tactic writebacks were *impossible*. It did not catch that the tactics themselves were *fabricated*, which is the worse F2 and the one this appendix records.

Checked: every Catalogue ID, cluster code, strategy number and theorist link in the sphere, against `by-cluster/`, `by-strategy/`, `by-theorist/`, `INDEX.json` and `INDEX-lspi.json`.

| Cited as | Actually on disk | Disposition |
|---|---|---|
| `0029` Selective Disclosure Choreography | `0029` **The 'Decoy' Initiative** | cycle-0007 re-pointed to `0210` Selective Transparency. `0029` was already correct in cycle-0009 |
| `0301` Asymmetric Briefing Cascade | `0301` **Temporal Arbitrage** | cycle-0007 re-pointed to `0392` The Pre-Meeting Protocol |
| `0044` Coalition Signal Exchange | `0044` **Strategic Benevolence** | name corrected in cycles 0008 and 0010; cycle-0009's r2 re-pointed to `0392` (Strategic Benevolence is not a pre-meeting) |
| `0156` Operational Context Briefing | `0156` **Data Overload (The 'Haystack' Defense)** | cycle-0008 Move 2 recorded as **non-catalogue** — no tactic in the 782 fits, and none was forced |
| `0112` Pre-Board Chair Briefing | `0112` **Lexicon Control** | cycles 0007 and 0010 re-pointed to `0380` The Skip-Level Gambit |
| `0418` Coalition-Strengthening Through Pre-Position | `0418` **The 'Process as Punishment'** | cycle-0008 re-pointed to `0572` The 'Hostile Takeover' of a Committee |
| Cluster `C12` Information-Choreography | `C12` **Internal Compliance, Audit & HR Weaponization** | clusters now derived from the cited tactics, not asserted |
| Cluster `C44` Coalition-Stabilization | `C44` **Reputation Assassination, Smear & Praise-as-Poison** | as above |
| Strategy 7 Coalition Preservation | Strategy 7 **Benefit Contrast** (`B(X)↑ + B(Y)↓`) | no Catalogue strategy is named "coalition preservation"; cycles now carry the strategy their selected tactics actually carry |
| `[[theorist-lukes]]`, `[[theorist-tilly]]` | **no file in `by-theorist/`** | replaced with cited theorists that exist — Goffman (cycle-0007), Cialdini (cycle-0008), Bourdieu (pattern file) |

Correct all along, and worth saying so: the whole of [[detection-robert-board-chair]]. Every cluster→tactic pair in it (`C03 → 0210`, `C09 → 0392`, `C04 → 0366`, `C27 → 0405`, `C60 → 0219`, `C79` at cluster level) resolves on disk with the right title. The Detection Record is the file the rest of the sphere should have been copying from.

**Repairs applied:** cycles 0007–0010 and the Pattern file (all Mode D). Sessions 009 and 011 are Mode A and carry appended `## Citation Correction` blocks instead — the § 6 discipline, applied to the same class of defect. The `(0044, 0156)` and `0044 ↔ cycle` references in § 6's session-009 and session-011 rows are left as written for the same reason: they accurately record what those logs claimed, which is the only thing a reciprocal-update audit is entitled to assert about them.

**Open thread carried:** the phantom-edge problem § 6 identified is unchanged. Cycle-0007's `## Refinement` still lists Tactic, Strategy and Theorist writebacks. Those IDs are now true; the edges are still impossible, and they are left standing so the finding stays legible rather than being quietly tidied away.
