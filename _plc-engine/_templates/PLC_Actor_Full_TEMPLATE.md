---
type: PLC_Actor
Item_ID: actor-<slug>
title: "<Actor Name> — <Role>"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Actor_Name: "<Name or [ACTOR-N] placeholder>"
plc_Actor_Role: "<Position/title>"
plc_Hierarchical_Position: ic   # executive | director | manager | ic | board | external | other
plc_Current_Perception_Toward_Principal: unknown   # allied | neutral | ambivalent | defensive | opposed | unknown
plc_Network_Distance_From_Principal: 1
plc_Resources_Held: []   # subset of: money, hard_assets, credibility, attributes, legitimacy, information, access, title, tribe, other  (other: name the actual carrier in a Resources Held note)
plc_Coalitions: []   # [[actor-<slug>]] — symmetric reciprocal required
plc_Opposed_By: []   # [[actor-<slug>]] or [[principal-<slug>]]
plc_Actor_Completeness: 2   # 0=Stub 1=Sketched 2=Drafted 3=Detailed 4=Comprehensive 5=Deeply known
plc_Last_Updated_Cycle: ""
# --- Optional LSPI fields (v1.2+; all optional, pre-1.2 actors valid without them) ---
plc_Estimated_By: []   # [[detection-<slug>]] — reciprocal of the Detection Record's plc_Target_Actor (estimates / estimated-by)
plc_Depth_Estimate: ""   # ℓ̂_T + credence + as-of date; full trail in the Detection Record
AI_Instructions: ""
---

# <Actor Name> — <Role>

## Current

### Profile
<One paragraph: position, tenure, professional context, anything material to political reasoning.>

### Perception Toward Principal
**<Perception>** since <YYYY-MM-DD>. Indicators (cold-reading):
1. <indicator>
2. <indicator>
3. <indicator>

<N of 3 indicators present.>

### Resources Held
<One bullet per resource. Per-resource sub-bullets are v1.2+, optional.>

- **<Resource type>:** <specifics; if `other`, name the carrier>
  - *Effect signature (v1.2+, optional):* moves <cells from {P/b, P/c, Adv/b, Adv/c}> <sign +/->; target-conditional on <what makes it bite for this target>; rough cost <cost>
  - *Durability (v1.2+, optional):* durable | fragile
- **<Resource type>:** <specifics>

### Convertibility Edges (v1.2+, optional)
<Conversion paths this actor's resources sit on. Rates are sphere-indexed estimates — same hygiene as matrix hypotheses.>

- <r₁> ⇝ <r₂> — <transfer | transform | earn-sanction | non-transferable>; rough rate: <rate>
- **Gain-cycle:** <loop whose rate-product > 1 — a compounding position — or "none seen">. Protected by: <which durable low-yield resource is spent defending which fragile high-yield one>

### Estimated Matrix Summary (v1.2+, optional)
<Best current read of how this actor loads keep-vs-relinquish on live questions; margin direction with epistemic status (P13). Summary only — the differential and probe trail live in [[detection-<slug>]].>

### Network Position
- **Coalitioned with:** <actors and brief why>
- **Opposed by:** <actors>
- **Brokers between:** <if applicable>

### Behavioral Notes
<Observed patterns. Communication style. What triggers shifts.>

## Perception History
<Append-only. Date prefix. Brief reason + cite.>

- <YYYY-MM-DD>: Baseline — <perception>. (Source: sphere-open or first ACTOR-UPDATE)

## Resource History
<Append-only. Date prefix. Gain/loss + reason + cite.>

- <YYYY-MM-DD>: Baseline — <resources at first capture>

## Cross-References
- Sphere: [[<sphere-slug>-manifest]]
- Most recent cycle: <link>
- Coalitions: <links>
- Opposition: <links>
