---
Item_ID: plc-install
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Political Landscape Cartography — Install Guide"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
AI_Instructions: ""
---

# Installing Political Landscape Cartography

PLC ships as a single folder you clone or download. There's no daemon, no database, no service to start. The Operating Volume IS the install.

## Requirements

- **Git** (for cloning + future version updates)
- **Claude Code** (or compatible agentic environment that can read/write local markdown). PLC's session protocols assume an AI agent runs against the local filesystem with read+write permissions on the OV folder.
- **A markdown viewer** for reading — Obsidian, VS Code, or any plain-text editor with markdown rendering. PLC files use Obsidian-style `[[wikilinks]]` for cross-references; some sphere operators prefer Obsidian for the graph view.
- **Disk space** ≈ 50-80 MB for the shipped substrate (Catalogue + frameworks + sources). Your sphere cartridges add roughly 1-5 MB per active engagement.

PLC does NOT require:

- Internet connectivity (after install — the OV is fully local)
- Specific OS (works on macOS / Linux / Windows; the prose examples use Unix-style paths but the methodology is platform-agnostic)
- Anthropic API credentials of any specific tier (any Claude Code installation will do; principal-self mode operators may use the AI subscription tier of their choice)
- Python / Node / runtime tooling (markdown + YAML are the only formats)

## Step-by-step install

### 1. Pick the install location

The OV folder belongs alongside your other working-document folders. If you use Obsidian, the OV can live inside a vault as a top-level folder — PLC is vault-compatible by default per Conventions 1-2.

Examples:

```
~/Documents/Political-Landscape-Cartography-v1.0/
~/Obsidian/<Vault>/Political-Landscape-Cartography-v1.0/
~/work/<engagement>/Political-Landscape-Cartography-v1.0/
```

**Folder name MUST follow the major.minor convention** (Convention 1): `Political-Landscape-Cartography-v<major>.<minor>`. The version suffix is load-bearing — UPDATE-PROMPT relies on it to detect the version you're upgrading from.

### 2. Clone the OV

```bash
# From the parent folder where you want PLC installed
git clone https://github.com/<org>/Political-Landscape-Cartography-v1.0.git Political-Landscape-Cartography-v1.0
cd Political-Landscape-Cartography-v1.0
```

*(Replace `<org>` with the actual GitHub organization at publication. Until publication, contact the methodology author for the source location.)*

If you prefer not to use git: download the OV as a zip from the project page and extract to the install location. You'll need git later to update; non-git installs require manual UPDATE-PROMPT runs.

### 3. Verify the install

```bash
# Should print the OV's current version
cat VERSION.md

# Should show the engine + frameworks + Types + scaffolding
ls -la
```

You should see:

```
AI-BOOTSTRAP.md
BOOTSTRAP-NEW-SPHERE.md
CHANGELOG.md
CONTRIBUTING.md
INSTALL.md
LICENSE.md
OPERATOR-GUIDE.md
README.md
UPDATE-PROMPT.md
VERSION.md
_PATTERNS/
_types/
_frameworks/
_plc-engine/
.gitignore
```

`Spheres/` is created automatically when you open your first sphere. It does not exist in a fresh install.

### 4. Open the first session

In Claude Code (or your compatible environment), open a session with the OV folder as the working directory. The first message you send to the AI should be:

```
Read AI-BOOTSTRAP.md and tell me where you want to go from here.
```

The AI will route you to one of four paths:

1. **Bootstrap a new sphere** — run `BOOTSTRAP-NEW-SPHERE.md` for an engagement
2. **Resume an existing sphere** — pick up where you left off
3. **Orient** — read the engine and frameworks before deploying
4. **Methodology study** — explore the substrate without deploying

For a first install, path 3 (orient) before path 1 (bootstrap) is the recommended sequence.

### 5. Open your first sphere

When you're ready to run an engagement, tell the AI:

```
Open a new sphere using BOOTSTRAP-NEW-SPHERE.md.
```

The AI runs the bootstrap protocol — one question at a time per P3. Plan ~60-90 minutes for the bootstrap session in consultant mode (the OPC §§ 16-17 hard-precedence pre-engagement adds ~30 min); ~30-45 minutes in principal-self mode.

## Updates

When a new PLC version releases, run UPDATE-PROMPT to upgrade in place. Your sphere cartridges (in `Spheres/`) are preserved verbatim; only the engine + frameworks + scaffolding zones get updated.

```bash
cd /path/to/Political-Landscape-Cartography-v1.0
# Read the UPDATE-PROMPT and follow its instructions
cat UPDATE-PROMPT.md
```

Major version bumps (e.g., v1.x → v2.0) introduce schema-breaking changes that require explicit migration; see `MIGRATION-vX-to-vY.md` in the new version's folder.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| AI says "I can't find `AI-BOOTSTRAP.md`" | You're not in the OV folder | `cd` into the cloned `Political-Landscape-Cartography-v1.0/` before starting the session |
| AI starts asking multi-bullet questionnaires | AI hasn't read the engine | Tell it: "Read `_plc-engine/02-PRINCIPLES.md` § P3 before continuing" — F1 prevention |
| AI tries to infer your name from the file path | F3 violation | Tell it: "Use the `[OPERATOR]` placeholder. Per P5 / F3, you may not infer my identity." |
| `[[wikilinks]]` show as raw text instead of rendering | Your markdown viewer doesn't support Obsidian-style links | Use Obsidian, or accept that wikilinks are still parseable as text references; the AI handles both |
| Catalogue tactic files (`_frameworks/political-warfare-catalogue/tactics/`) seem missing or partial | Incomplete clone (zip download truncation or git LFS not pulled) | Re-clone with `git lfs install` first if the repo uses LFS; otherwise re-download |
| AI cites a theorist or tactic that doesn't exist | F2 fabrication violation | Tell it: "Stop. Verify by reading the file at `_frameworks/political-warfare-catalogue/by-theorist/<name>.md`. If the file doesn't exist, retract the citation." |
| `_sphere-state.md` and `_sphere-decisions.md` drift apart | Reciprocal-update discipline failed in prior session | Run a QUARTERLY-AUDIT session — it includes a graph-integrity pass that catches and repairs F5 violations |
| Update prompt fails partway through; engine zone partially updated | Partial UPDATE-PROMPT execution | `git stash` your sphere zone, `git pull` cleanly, then `git stash pop` to restore your sphere |
| Multiple sphere cartridges appear in `Spheres/` from different engagements; AI gets confused | No active-sphere designation | Tell the AI explicitly which sphere is active at session start: "Active sphere: `Spheres/<Name>/`" |
| AI claims engine chapters are missing when you can see them on disk | AI didn't load Tier 1 reads at session start | Re-issue: "Read Tier 1 engine chapters per `_plc-engine/00-START-HERE.md` Phase 0 before proceeding" |
| Master_Schema namespace conflicts when integrating with central vault infrastructure | Central + OV-local `_types/` not synchronized | Run the schema-registration step deferred to SHIP-PREP; see `_plc-engine/07-SHIPPING-CHECKLIST.md` § 1 |

If the symptom is not listed here: check `OPERATOR-GUIDE.md` § "Symptom → Cause → Fix" for the operator-facing failure modes, then open an issue at the project repo with the symptom description and your OV version.

## Uninstall

PLC has no global state — uninstall is just deleting the folder.

```bash
# WARNING — this deletes your sphere cartridges along with the engine
rm -rf /path/to/Political-Landscape-Cartography-v1.0/
```

To preserve sphere cartridges across an uninstall, move `Spheres/` out first:

```bash
mv Political-Landscape-Cartography-v1.0/Spheres ~/PLC-spheres-archive/
rm -rf Political-Landscape-Cartography-v1.0/
```

The `Spheres/` folder is portable — it can be moved into a future PLC install of the same major version, and the engagement resumes from where it left off. Major-version migrations require running the migration guide; cross-version sphere portability is not guaranteed without it.

## Next

After install: `OPERATOR-GUIDE.md` (or your mode-specific variant) for symptom → cause → fix mid-engagement guidance.
