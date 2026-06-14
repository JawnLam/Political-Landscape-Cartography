---
Item_Prototype: Fleeting
Item_ID: plc-update-prompt
Title: "PLC — Update Prompt"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
type: bootstrap
role: version-update-protocol
audience: AI
---

# PLC UPDATE PROTOCOL

> **AI-facing.** The operator invokes this by saying "run UPDATE-PROMPT" or "update PLC." You read this file and execute the steps in order. Do not skip steps. Do not improvise around hard checks. The operator's spheres are the asset; corrupting them via a half-run update is the loss.

## Step 0 — Confirm you are in an OV folder

Verify the working directory:

- `VERSION.md` exists at root
- `AI-BOOTSTRAP.md` exists at root
- `_plc-engine/` directory exists
- `_Prototypes/` directory exists

If any are missing, STOP. The working directory is not a PLC OV. Tell the operator and ask them to confirm the path.

## Step 1 — Detect current and target versions

```
Current version: <read from VERSION.md>
Target version: <ask operator if not specified, or read from incoming UPDATE-PROMPT context>
```

Classify the version delta:

- **Same version** — nothing to update. Report and exit.
- **Patch bump** (e.g., `v1.0.0` → `v1.0.1`) — minimal protocol; document-only changes typically
- **Minor bump** (e.g., `v1.0` → `v1.1`) — additive changes; sphere cartridges remain compatible
- **Major bump** (e.g., `v1.0` → `v2.0`) — schema-breaking changes; migration guide REQUIRED

If major bump and no `MIGRATION-v<current>-to-v<target>.md` is visible: STOP. Tell the operator the migration guide must exist before proceeding. Do not attempt to "figure out the migration" on the fly.

## Step 2 — Enumerate the sphere zone

List every directory in `Spheres/`:

```bash
ls -la Spheres/
```

For each sphere, capture:

- Sphere slug
- Engagement status (read from `_sphere-manifest.md` frontmatter)
- Count of active cycles
- Count of total session logs

Report this enumeration to the operator. Confirm they recognize all spheres. If a sphere is present that the operator doesn't recognize: STOP. Investigate before any zone-touching operation. Unfamiliar state may represent the operator's other in-progress work.

## Step 3 — Detect local edits in non-sphere zones

Run a git status check:

```bash
git status --short
```

Filter for changes outside `Spheres/`:

- Modified files in `_plc-engine/`
- Modified files in `_frameworks/` (excluding `*-extensions/` which are operator-owned)
- Modified files in `_Prototypes/`
- Modified root-level files (`README.md`, `OPERATOR-GUIDE.md`, etc.)

If any are present, this is a Convention 8 violation — engine/framework/scaffolding zones should not have direct edits. Report the list to the operator and recommend stashing:

```bash
git stash push -m "pre-update-<target-version> local edits in engine/framework zones"
```

If the operator stashes, proceed. If they decline, document the override and proceed with the warning that their edits will be overwritten by the pull.

## Step 4 — Backup checkpoint

Recommend the operator create a checkpoint commit before the pull:

```bash
git add Spheres/
git commit -m "pre-update-<target-version> checkpoint — sphere zone snapshot"
```

This is not strictly required (the git history holds it anyway) but the explicit commit gives the operator a named-rollback target. If the operator declines, proceed without it.

## Step 5 — Pull the new version

```bash
git fetch origin
git pull origin <branch-pointing-at-target-version>
```

If conflicts arise:

- **Conflicts inside `Spheres/`** — should never happen because git rules + this protocol exclude sphere zone from upstream changes. If it does happen, STOP. The repository is misconfigured.
- **Conflicts outside `Spheres/`** — the stashed edits from Step 3 are conflicting with the pull. Resolve by accepting the new version for engine/framework/scaffolding files; offer to migrate the stashed content into appropriate extension folders for the operator to review.

## Step 6 — Verify the new version installed cleanly

Re-read `VERSION.md`. Confirm it matches the target. If it doesn't:

- The pull silently no-oped (already on target — proceed to Step 7)
- The pull failed partway (rollback to checkpoint commit from Step 4; report to operator)

Re-verify the structural sanity:

- All 8 engine chapters present in `_plc-engine/`
- All 16 Prototype files present in `_Prototypes/`
- All 22 template files present in `_plc-engine/_templates/`
- All 6 YAML scaffolding files present in `_plc-engine/_yaml/`
- `Spheres/` directory unchanged (same sphere count as Step 2)

If any structural check fails: STOP. Report to operator.

## Step 7 — Read the CHANGELOG for the target version

Read `CHANGELOG.md`. Find the section for `<target-version>`. Identify:

- **Breaking changes** (prefixed `BREAKING:`) — should only appear in major bumps. If a minor bump CHANGELOG contains BREAKING entries, the version was tagged wrong; STOP and report.
- **Sphere-impacting changes** — additions to required frontmatter fields, changes to Mode contracts, new mandatory gates. These need per-sphere checks.
- **Catalogue extensions** — new tactics, theorists, clusters, strategies. Sphere cartridges may want to add references to these in next QUARTERLY-AUDIT.

Summarize the sphere-impacting changes to the operator.

## Step 8 — Per-sphere compatibility check

For each sphere enumerated in Step 2:

- Read `_sphere-manifest.md` frontmatter. Verify all currently-required fields per the new Prototype definitions are present. If new required fields were added in the bump, surface as a TODO.
- Check `_sphere-state.md` for the `## Decided` + `## OPC Current Summary` + `## State History` structure.
- Spot-check three random Items per sphere (one Actor, one Cycle, one Session log) for frontmatter conformance.

Report findings per sphere. Do NOT auto-edit sphere files. Surfacing TODOs is the protocol; operator-or-AI-edit-on-confirmation is the resolution.

## Step 9 — F-code regression spot-check

Run synthetic checks against F1-F9 (per `_plc-engine/05-WRITING-FOR-AI.md`). Each check is brief (1-2 min):

- **F1:** Confirm `BOOTSTRAP-NEW-SPHERE.md` § 1 still says "Ask one question, conversationally"
- **F2:** Confirm `02-PRINCIPLES.md` § P4 still explicitly forbids fabrication
- **F3:** Confirm `00-START-HERE.md` Phase 0 still says to use `[OPERATOR]` placeholder
- **F4:** Spot-read `04-SCHEMA.md` for sphere-specific names (should be none outside worked examples)
- **F5:** Spot-check three random reciprocal pairs in a sphere (e.g., Actor `plc_Coalitions` symmetric)
- **F6:** Diff `AI-BOOTSTRAP.md` vs `_plc-engine/00-START-HERE.md` — root must remain thin pointer; engine canonical
- **F7:** Spot-read three random engine chapter sections for "we will discuss" or "this section covers" — should be zero
- **F8:** Spot-check three closed cycles in any sphere for gate completion timestamps OR logged overrides
- **F9:** Spot-check one cycle log frontmatter — slash/OPC/Catalogue fields must stay in their own families

If any F-code regression surfaces, surface as a TODO. Don't auto-fix engine zone (that's the engine's responsibility for the next version). Do offer to repair sphere-zone F5 / F8 violations.

## Step 10 — Major bump migration (major bumps only)

If this is a major bump:

- Confirm `MIGRATION-v<old>-to-v<new>.md` was read by the operator (ask explicitly)
- Walk through the migration guide section by section
- For each migration action, surface to operator with explicit confirmation before applying
- Per-sphere migration runs separately; recommend running on the lowest-stakes sphere first as a pilot
- Document each migration action in the affected sphere's `_sphere-decisions.md` as a `migration` entry

## Step 11 — Report the update outcome

Emit a structured report:

```markdown
## PLC Update Report — <ISO date>

- **From version:** <old>
- **To version:** <new>
- **Delta:** patch | minor | major
- **Spheres preserved:** <count> (verified intact)
- **Local edits stashed:** <count>
- **CHANGELOG sphere-impacting items:** <count>
- **TODOs surfaced (per-sphere):** <count>
- **F-code regressions surfaced:** <count>
- **Migration actions applied (major only):** <count>
- **Update sealed:** yes | partial — see TODOs
```

Append this report to a new session log: `Sessions/<sphere-slug>/<YYYY-MM-DD>_UPDATE-PROMPT.md` per sphere affected, OR if no sphere zone was modified, to an OV-level `_meta/update-log.md` (append-only).

## Step 12 — Next-activity recommendation

Based on what surfaced:

- If sphere TODOs > 0: recommend ACTOR-UPDATE or per-sphere remediation session
- If F-code regressions surfaced: recommend the F-specific repair
- If neither: recommend resuming the most recent active sphere

Operator disposes (per P10). Even "later" is a captured choice.

## Anti-patterns this protocol prevents

- **Pulling without enumerating spheres** — risk of overwriting sphere state from a misconfigured repo
- **Pulling without checking local edits** — silent loss of operator's engine-zone work
- **Auto-applying migrations without operator review** — risk of breaking sphere cartridges the operator hadn't migrated mentally yet
- **Skipping F-code regressions** — version drift across releases corrupts the F1-F9 prevention design over time
- **Treating a major bump as "just another update"** — major bumps require migration guides for a reason

## When to NOT run this protocol

- If the operator is mid-cycle (active cycle in `engaged` status) — recommend completing the cycle first, OR explicitly accepting the post-update reconciliation work
- If a QUARTERLY-AUDIT is more than 30 days overdue on any sphere — recommend running it first; the audit catches accumulated F5 violations that the update would otherwise compound
- If the operator's stated state ("everything's fine") conflicts with the working directory's state (uncommitted changes, unfamiliar files, unexpected branch) — investigate first

## Where this protocol fits

Convention 7 of OVE — every OV ships its UPDATE-PROMPT.md as the operator-runs-AI-executes upgrade mechanism. The protocol's job is to preserve the operator's investment in their spheres while propagating the engine + framework + scaffolding zones forward.
