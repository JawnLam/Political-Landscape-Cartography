---
Item_ID: plc-version
type: Fleeting
timestamp: "2026-06-13T00:00:00Z"
title: "Political Landscape Cartography — Version"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
AI_Instructions: ""
---

# Political Landscape Cartography — Version

**1.2.0**

| Field | Value |
|-------|-------|
| Version | 1.2.0 |
| Release date | 2026-07-24 |
| Supersedes | 1.1.1 |
| Codename | (none) |
| Methodology Author | Cong "Jawn" Lam |
| OVE Substrate | Operating-Volume-Engineering-v1.2 |
| Master Schema Compatibility | v1.22.0+ (PLC namespace registered) |
| License | Proprietary — All Rights Reserved (see `LICENSE.md`) |

## Version semantics

PLC follows semantic versioning with the conventions documented in `CONTRIBUTING.md`:

- **MAJOR** (`v1.x` → `v2.0`) — schema-breaking changes; required-field changes; mode contract changes; reference-system changes; relation family removals; principle removals
- **MINOR** (`v1.0` → `v1.1`) — additive changes; new Types; new Templates; new YAML scaffolding; Catalogue extensions; new patterns; new principles; new session activities; chapter revisions that don't break references
- **PATCH** (`v1.0.0` → `v1.0.1`) — typo corrections; documentation clarifications; markdown rendering fixes; formatting

## Compatibility matrix

| PLC version | OVE substrate | Master Schema | Sphere cartridge compatibility |
|-------------|---------------|---------------|--------------------------------|
| 1.0.0 | 1.2 | 1.22.0+ | first shipping major; no prior cartridges to migrate |
| 1.1.0 | 1.2 | 1.22.0+ | v1.0 cartridges load unchanged; additive Types and Templates only |
| 1.1.1 | 1.2 | 1.22.0+ | patch over 1.1.0; no cartridge impact |
| 1.2.0 | 1.2 | 1.22.0+ | existing v1.1 cartridges load unchanged — all new fields (Detection Records, estimation rollups, LSPI operation-record lines) are optional; pre-1.2 cycles remain valid without backfill |

## Source of truth

This file is the canonical version reference. `README.md`, `CHANGELOG.md`, and `INSTALL.md` must agree with this value. UPDATE-PROMPT.md uses this file to detect the current version.

The version is NOT embedded in the folder name — the install folder is `Political-Landscape-Cartography`, unversioned, so an in-place upgrade never requires a rename. Version strings live in:

- This file (canonical)
- Each Type file's `type_version` frontmatter — a per-Type value, not the volume version. Types unchanged since the first major still declare `"1.0"`; Types introduced or revised at v1.2 declare `"1.2"` (e.g., `PLC_Detection_Record`). A Type's `type_version` moves only when that Type's own definition changes.
- Each YAML scaffolding file's `version: "1.0"` header
