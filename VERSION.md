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

**1.0.0**

| Field | Value |
|-------|-------|
| Version | 1.1.0 |
| Release date | 2026-06-13 |
| Codename | (none) |
| Methodology Author | Cong "Jawn" Lam |
| OVE Substrate | Operating-Volume-Engineering-v1.2 |
| Master Schema Compatibility | v1.22.0+ (PLC namespace registered) |
| License | Proprietary — All Rights Reserved (see `LICENSE.md`) |

## Version semantics

PLC follows semantic versioning with the conventions documented in `CONTRIBUTING.md`:

- **MAJOR** (`v1.x` → `v2.0`) — schema-breaking changes; required-field changes; mode contract changes; reference-system changes; relation family removals; principle removals
- **MINOR** (`v1.0` → `v1.1`) — additive changes; new Prototypes; new Templates; new YAML scaffolding; Catalogue extensions; new patterns; new principles; new session activities; chapter revisions that don't break references
- **PATCH** (`v1.0.0` → `v1.0.1`) — typo corrections; documentation clarifications; markdown rendering fixes; formatting

## Compatibility matrix

| PLC version | OVE substrate | Master Schema | Sphere cartridge compatibility |
|-------------|---------------|---------------|--------------------------------|
| 1.0.0 | 1.2 | 1.22.0+ | first shipping major; no prior cartridges to migrate |

## Source of truth

This file is the canonical version reference. `README.md`, `CHANGELOG.md`, and `INSTALL.md` must agree with this value. UPDATE-PROMPT.md uses this file to detect the current version.

The version is also embedded in:

- The folder name (`Political-Landscape-Cartography-v1.0`)
- Each Prototype file's `prototype_version: "1.0"` frontmatter
- Each YAML scaffolding file's `version: "1.0"` header
