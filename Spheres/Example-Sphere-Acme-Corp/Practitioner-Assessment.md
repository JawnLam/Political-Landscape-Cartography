---
type: Fleeting
timestamp: "2026-06-01T00:00:00Z"
Item_ID: acme-corp-practitioner-assessment
title: "Acme Corp — Practitioner Assessment (§§ 16 + 17)"
Date_Added: 2026-04-15
Date_Modified: 2026-06-01
Needs_Processing: false
plc_Sphere: "[[acme-corp-manifest]]"
plc_Operator_Mode: consultant
plc_Baseline_Date: 2026-04-15
plc_Latest_Refresh_Date: 2026-06-01
plc_Latest_Refresh_Diagnostic: "[[opc-2026-06-01]]"
plc_Section_16_Current_Status: yellow_flagged
plc_Section_17_Current_Status: green
AI_Instructions: ""
---

# Acme Corp — Practitioner Assessment (§§ 16 + 17)

> **Consultant-mode mandatory artifact per D11.** Captures the OPC §§ 16 + 17 outcomes at sphere-open (hard-precedence pre-engagement) and quarterly refresh cadence. Mode D: `## Current` overwrites with latest read; `## Refresh History` accumulates each refresh's outcome chronologically.
>
> **OPC v3.0 canonical reference:** `_frameworks/OPC-Assessment.md`. § 16 has 9 subsections (16.1-16.9); § 17 has 9 subsections (17.1-17.9). This worked example was corrected from earlier session-context fabrications on 2026-06-13 (which had claimed 14 § 16 subsections and 11 § 17 subsections with invented topic names).

## Current

### § 16 — Practitioner Self-Assessment (as of 2026-06-01 refresh)

9 subsections walked. Current status: **YELLOW** (one flag at § 16.8 `disengagement_triggers`).

| OPC subsection | Topic (verbatim) | Status | Notes |
|----------------|------------------|--------|-------|
| § 16.1 | `position_and_standing` | green | Consultant has independent professional standing relative to Acme Corp; no positional vulnerability detected. Family-board succession is within deep-practice domain (10+ similar engagements). |
| § 16.2 | `sponsor_relationship` | green | Sam (sponsor) demonstrated coachability + funnel-receptivity at CQ2-CQ3. No sponsor-capture risk detected at baseline. |
| § 16.3 | `contractual_and_financial_pressures` | green | Engagement fee structured to insulate practitioner judgment; no contingent payments tied to outcome. No financial pressure distorting current advice. |
| § 16.4 | `identity_based_reads` | green | Operator identified own preference for operational-mandate framing over institutional-prudence framing; bias surfaced and flagged for cycle-by-cycle awareness. Not currently distorting the read. |
| § 16.5 | `what_your_sponsor_will_not_tell_you` | green | Sam's pattern of withholding noted at sphere-open: tends to under-report family-bloc internal tensions. Operator probes structurally each session to surface what's not said. |
| § 16.6 | `your_own_stakes` | green | Practitioner reputation upside on a successful succession-period engagement; no career-defining downside on this engagement. Stake-vs-judgment ratio balanced. |
| § 16.7 | `cognitive_distortions_in_play` | green | Self-monitoring active. Operator's tendency to over-weight operational-performance evidence (and under-weight institutional-loyalty signals) named explicitly; checked at each cycle's Detection step. |
| **§ 16.8** | **`disengagement_triggers`** | **yellow** | **Q4 ratification window will likely demand 2-3 days emergency contingency time that current practice schedule cannot absorb without rescheduling other engagements. Calendar buffer scheduled 2026-10 → 2026-11 as mitigation. If buffer is encroached upon, this becomes a disengagement-trigger candidate. Re-assessed 2026-06-01: mitigation holding.** |
| § 16.9 | `self_check_questions` | green | Operator runs the standard self-check protocol at every cycle close. No surfaced concerns this refresh. |

**Action items from § 16 current state:**
- Monitor § 16.8 mitigation through Q3 — re-confirm calendar buffer; consider additional contingency if Q3 inflection points compress the timeline
- Bring § 16.4 identity-based-read awareness into Cycle-0008 close (operator's operational-mandate-framing preference may have over-weighted Robert's positive Cycle-0007 signal)

### § 17 — Advisor Engagement Politics (as of 2026-06-01 refresh)

9 subsections walked. Current status: **GREEN** throughout.

| OPC subsection | Topic (verbatim) | Status |
|----------------|------------------|--------|
| § 17.1 | `engagement_entry` | green — entry conditions clean; principal-initiated; no sponsor coercion |
| § 17.2 | `sponsor_capture_risks` | green — sponsor (Sam) not currently positioned to use advisor for sponsor-internal political work; risk monitored |
| § 17.3 | `deliverable_politics` | green — deliverables clearly scoped to coaching + diagnostic outputs; no deliverable being repurposed politically |
| § 17.4 | `messenger_risks` | green — advisor not being deployed as bad-news messenger; communication flows direct between Sam and stakeholders |
| § 17.5 | `internal_politics_of_the_firm` | green — practitioner's own firm context is clean for this engagement; no internal politics affecting capacity or framing |
| § 17.6 | `engagement_boundaries` | green — boundaries explicit per sphere-decisions § 001 (family-personal succession dynamics out of scope); held throughout |
| § 17.7 | `disengagement` | green — disengagement criteria documented in manifest; conditions for ending the engagement clear to both parties |
| § 17.8 | `career_implications` | green — engagement neither career-defining nor career-risking for practitioner; right size for current trajectory |
| § 17.9 | `engagement_health_checks` | green — health checks running at expected cadence; no health flags surfaced this refresh |

**No § 17 flags surfaced.** Family-ownership structure has produced cleaner advisor-engagement boundaries than typical mid-market — engagement environment durable through engagement horizon.

## Refresh History

> Append-only. Chronological log of each §§ 16-17 walk.

### 2026-06-01 refresh (full OPC diagnostic — `opc-2026-06-01`)
- § 16: yellow on § 16.8 `disengagement_triggers` (carry-over from baseline; calendar-buffer mitigation re-confirmed)
- § 17: green throughout (all 9 subsections)
- No status changes since baseline

### 2026-04-15 baseline (sphere-open hard-precedence pre-engagement)
- § 16: yellow on § 16.8 `disengagement_triggers` — Q4 ratification window schedule-contingency requirement. Mitigation (calendar buffer through 2026-10 → 2026-11) captured at time of flag.
- § 17: green throughout — engagement environment assessed clean; family-ownership structure cleaner than typical mid-market; no contraindications surfaced.
- **Decision at sphere-open:** Engagement proceeded with § 16.8 mitigation in place. No contraindications meeting "decline engagement" threshold.

## Next Refresh

Scheduled at next QUARTERLY-AUDIT (target window 2026-09-01). Earlier ad-hoc refresh triggered if either:
- § 16.8 mitigation breaks down (calendar buffer encroached upon)
- § 17 environment shifts (e.g., new advisor introduced to scope; family-bloc conflict surfaces)
- Operator detects own identity-based-read drift (§ 16.4) in cycle work

## Cross-References

- Sphere: [[acme-corp-manifest]]
- Latest OPC diagnostic carrying §§ 16-17 detail: [[opc-2026-06-01]]
- Sphere-open session: [[session-acme-corp-000]]
- OPC v3.0 canonical reference: `_frameworks/OPC-Assessment.md` § 16 / § 17
- D11 mandate: `_plc-engine/02-PRINCIPLES.md` § P9 (mode-aware discipline) + `BOOTSTRAP-NEW-SPHERE.md` § 1 (consultant-mode hard precedence)
