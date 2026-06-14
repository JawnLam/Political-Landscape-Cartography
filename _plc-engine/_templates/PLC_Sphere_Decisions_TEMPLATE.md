---
Item_Prototype: PLC_Sphere_Decisions
Item_ID: <sphere-slug>-decisions
Title: "<Sphere Name> — Sphere Decisions Log"
Date_Added: <YYYY-MM-DD>
Date_Modified: <YYYY-MM-DD>
Needs_Processing: false
plc_Sphere: "[[<sphere-slug>-manifest]]"
plc_Decision_Count: 0
AI_Instructions: ""
---

# <Sphere Name> — Sphere Decisions Log

> Append-only. Never edit prior entries. To supersede a decision, append a new entry citing the prior §NNN AND flip the prior entry's `Status:` line to `superseded by §<new>`.

> **Elevation criterion:** "Would a future operator — coming in cold to this sphere — need to know this to operate the sphere correctly?" If no, the decision lives in the session log only and is not elevated here.

<!-- Append new entries below. Increment plc_Decision_Count in frontmatter. -->

## §001 — <YYYY-MM-DD> — <One-line title>

**Decided:** <The decision in one sentence.>

**Why:** <One paragraph: motivating context, constraint, or stakeholder ask.>

**Source:** <Session log filename and section, OR `_sphere-state.md` § ..., OR external reference.>

**Status:** active
