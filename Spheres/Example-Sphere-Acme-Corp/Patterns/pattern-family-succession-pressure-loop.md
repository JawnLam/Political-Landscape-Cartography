---
Item_Prototype: PLC_Pattern
Item_ID: pattern-family-succession-pressure-loop
Title: "Family-Succession-Pressure-Loop — Pattern"
Date_Added: 2026-06-09
Date_Modified: 2026-06-13
Needs_Processing: false
plc_Pattern_Family: arc_dynamics
plc_Pattern_Scope: sphere_specific
plc_Pattern_Source_OPC_Section: "13.2"
plc_Sphere: "[[acme-corp-manifest]]"
plc_Related_Theorists:
  - "[[theorist-pfeffer]]"
  - "[[theorist-tilly]]"
plc_Related_Strategies:
  - "[[strategy-7]]"
  - "[[strategy-13]]"
plc_Confidence_Level: 3+_observations_confirmed
plc_Evidence_Cycles:
  - "[[cycle-0006]]"
  - "[[cycle-0007]]"
  - "[[cycle-0008]]"
plc_Evidence_Diagnostics:
  - "[[opc-2026-06-01]]"
AI_Instructions: ""
---

# Family-Succession-Pressure-Loop — Pattern

## Family

**Family:** `arc_dynamics` (per OPC § 13.2)

## Current

### Pattern Description

In family-board organizations facing succession-planning pressure, opposition actors (typically the CFO or COO archetype) consolidate resource control through finance-committee or operating-committee staffing in the 12-18 months preceding succession ratification. The consolidation generates a feedback loop: consolidated resources create perception-of-shadow-CEO authority → that perception legitimizes further consolidation → which compresses the principal's mandate window → which makes the principal's framing of operational continuity sound increasingly defensive rather than proactive.

The pattern is durable across mid-market family-ownership structures. It does NOT require malicious intent on the opposition actor's part — the consolidation often presents as "responsible succession-period institutional stewardship" rather than overt political maneuvering, which makes it harder to surface and harder to counter without appearing paranoid.

### Detection Signals

Cold-reading indicators for this pattern (no single one is conclusive; 2+ together suggest pattern activation; 3+ confirms):

1. **Committee restructure timing.** Finance- or operating-committee composition changes that move authority away from the principal's allies in the 12-18 months before succession ratification. Especially: replacing a long-serving ally with the opposition actor's deputy.
2. **Independent reporting line expansion.** Existing audit-committee or compliance reporting lines being formalized, expanded, or invoked more visibly. The expansion creates structural information asymmetry against the principal.
3. **Communication channel narrowing.** Opposition actor's prior 1:1 cadence with the principal shifting to written-only, committee-mediated, or asynchronous channels. The principal loses real-time signal access.
4. **External press citation patterns.** Opposition actor's industry-press citations increasing in frequency OR substance (especially substance — citations on the org's operational/financial state position the opposition actor as the public voice rather than the principal).
5. **Family-bloc external relationships.** Discovery that opposition actor has historical relationships with family-bloc swing members predating the current org context.

### What Typically Drives It

- Family-board structures where succession is treated as an institutional event rather than a continuous process. The "succession-planning" framing legitimizes consolidation moves as institutional rather than political.
- Opposition actor's pre-existing functional authority (CFO/COO) is genuinely high-leverage. The consolidation isn't manufactured — it's amplification of legitimate authority.
- Family voting bloc's attention is on family-personal succession dynamics, not operational politics. The principal-vs-opposition political work happens in a window the family isn't watching closely.

### Typical Lifecycle

Four-stage arc:

1. **Initiation (12-18 months pre-succession).** First committee restructure. Opposition actor consolidates one resource (typically finance-committee chair OR operating-committee chair). Principal often misreads this as routine governance; the consolidation establishes the precedent for further moves.
2. **Acceleration (6-12 months pre).** Second and third consolidation moves. Independent directors begin noticing resource shifts. Opposition actor's external-press citations become more substantive. Principal recognizes the pattern at this stage if detection discipline is in place.
3. **Crisis (3-6 months pre).** Family-bloc swing member becomes the lever. Opposition actor either has activated an existing relationship with the swing OR is in the process of doing so. Principal's coalition-preservation moves become the central political work of the engagement.
4. **Resolution (succession event).** Pattern terminates with either (a) principal's mandate preservation through successful coalition-preservation OR (b) principal's exit (negotiated or forced) with opposition actor or alternative successor installed.

### Recommended Strategies (against)

- [[strategy-7]] (Coalition Preservation) — preserves the family voting bloc against fracturing pressure; does not directly contest the opposition actor but protects the principal's position
- [[strategy-13]] (Counter-Consolidation) — directly contests specific committee staffing decisions when the consolidation move is structurally challengeable

### Recommended Strategies (alignment)

N/A — this is an opposition pattern; alignment is not operative.

### Related Theorists

- **Pfeffer** — resource-dependence theory illuminates the consolidation move as classic resource-dependence positioning. The opposition actor expands resource control because resources translate to organizational power; the principal must contest resources directly rather than relying on relationship moves alone.
- **Tilly** — political-opportunity-structure framework illuminates the succession window as the opportunity-structure that makes the pattern possible. Without the succession window, the consolidation moves would be illegitimate. With it, they read as "responsible institutional stewardship."

## Evidence History

> Append-only. Each entry: date + cycle/diagnostic source + evidence + status (CONFIRMS | PARTIAL | CONTRADICTS).

- **2026-06-13: Cycle-0008 evidence.** Robert's positive reciprocity signal at Sam-Robert 1:1 (Tactic 0044) AND Carol's confirmed defensive posture (3/3 indicators) together support Stage 3 (Crisis) characterization. **CONFIRMS** (4th observation). Confidence level held at `3+_observations_confirmed`.
- **2026-08-30 OBS NOT YET — placeholder removed.** *(Note: this placeholder was incorrectly drafted in an earlier version of this Pattern file; the entry was removed when discovered during graph-integrity audit. Real evidence entries only.)*
- **2026-06-13: Cycle-0008 phase log evidence.** Carol's defensive posture detection signals 3/3 present at this cycle's open. Pattern indicator #1 (committee restructure) + #3 (communication channel narrowing) confirmed; #5 (family-bloc external relationships) confirmed via Cycle-0006 Carol-Robert historical relationship. **CONFIRMS** (3rd observation; promoted to `3+_observations_confirmed`).
- **2026-06-09: Cycle-0007 close evidence.** Q2 board meeting outcome — Sam's operational framing led the meeting; Carol's framing was present but secondary. Pattern Stage 2 (Acceleration) consistent with observed Carol consolidation timeline; Cycle-0007's success doesn't disconfirm the pattern (the pattern predicts crisis at Stage 3, not Stage 2). **PARTIAL — supports pattern characterization but not Stage 3 indicators yet.**
- **2026-05-22: Cycle-0006 evidence.** First observation. Carol's budget-memo timing pattern (4 of 6 contentious memos delivered Friday EOD) + finance-committee staffing replacement of Marcus with Diane matched detection indicators #1 + #3 simultaneously. UNCOVER work surfaced Carol-Robert historical relationship matching indicator #5. **PARTIAL** (1 observation).

## Cross-References

- Sphere: [[acme-corp-manifest]]
- Cycles providing evidence: [[cycle-0006]], [[cycle-0007]], [[cycle-0008]]
- Diagnostics surfacing: [[opc-2026-06-01]]
- Carol's pattern instance: [[actor-carol-cfo]]
- Robert's pattern instance (swing actor): [[actor-robert-board-chair]]
- Related patterns: *(Shadow-CEO-Consolidation pattern — operator considering whether to elevate as separate Pattern Item or treat as sub-pattern of this; deferred decision for next QUARTERLY-AUDIT)*
