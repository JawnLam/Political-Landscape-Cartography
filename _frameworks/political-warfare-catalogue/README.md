# Organizational Political Warfare — Tactical Catalogue

**782 fully-analyzed political tactics, optimized for AI agent consumption.**

This directory is the **AI-readable layer** over the corpus. JSON source-of-truth lives in `../99_assembled_output.json`; this layer is for AI agents, humans, and downstream tools that benefit from markdown's lower token cost and structural navigation.

## How to use

### Read a single tactic
Open any file under `tactics/` — e.g., `tactics/0382-the-black-budget-slush-funding.md`. Each file is ~10-26 KB, self-contained, structured H1/H2/H3.

### Search the index first
Read `INDEX.json` (871 KB) before scanning individual files. It has one record per tactic with:
- `tactic_id`, `title`, `description`, `slug`
- `tactic_type`, `cluster_id`, `cluster_name`
- `specific_strategy`, `generic_strategy` (number, name, lever combination)
- `theorists_cited`, `theorist_count`
- `versatility` level
- `file_markdown` path (relative to workspace root)

Filter the index for candidates, then load only the markdown files you actually need.

### Browse by facet

| Facet | Directory | Files | Use case |
|---|---|---|---|
| **By Strategy** | `by-strategy/` | 16 | "Show me all Resistance Triple tactics" |
| **By Cluster** | `by-cluster/` | 84 | "What tactics are in the Coalition cluster?" |
| **By Theorist** | `by-theorist/` | 50 | "What tactics cite Schelling?" |

Each facet file is a markdown table listing tactics in that group with links into `tactics/`.

## Directory structure

```
markdown/
├── README.md                     ← this file
├── INDEX.json                    ← 871 KB structured index, 783 records
├── INDEX-lspi.json               ← LSPI facet sidecar, 783 records (see "LSPI binding" below)
├── tools/                        ← extract-lspi-levers.py (regenerates the sidecar)
├── tactics/                      ← 782 per-tactic markdown files
│   ├── 0001-power-structure-mapping.md
│   ├── 0002-sacred-cows-untouchables.md
│   └── ... (782 total)
├── by-strategy/                  ← 16 strategy facet files (#1–#16)
├── by-cluster/                   ← 84 thematic cluster facet files
└── by-theorist/                  ← 50 theorist facet files
```

## Token efficiency

- **JSON (12.9 MB)**: ~3.2M tokens to load full corpus
- **Markdown (11.5 MB)**: ~2.4M tokens to load full corpus
- **Per-tactic load** (median 14.9 KB): ~3.7K tokens per tactic
- **INDEX-first lookup**: ~200K tokens to scan all 783 records, then load only the 1-5 tactics actually needed

For most LLM agent queries, **read INDEX.json → identify candidates → load 1-5 tactic markdown files** is the efficient path.

## Structure of each tactic file

Every per-tactic markdown follows this template (sections shown only when present in source):

```markdown
# {ID} — {TITLE}

> {description}

**Type:** `{specific|generic|hybrid}` · **Strategy:** {#N Name} · **Cluster:** {cluster_id} — {name}
**Cited principles:** {comma-separated theorists}

---

## Classification Rationale
**Ambiguity Source.** ...
**Specific Interpretation.** ...
**Generic Interpretation.** ...
**Primary Classification:** ...
**Reasoning.** ...

---

## Specific Analysis
### Choice Architecture
- **Option X:** ...
- **Option Y:** ...
- **Context:** ...

### Active Levers
#### B(X)↑ — Active · intensity 2 (Moderate)
{mechanism-specific evidence}

#### C(X)↓ — Active · intensity 3 (Intense)
{evidence}

#### B(Y)↓ — Not active
{why it's not active — diagnostic}

#### C(Y)↑ — Active · intensity 3 (Intense)
{evidence}

### Strategy
**#8 Cost Contrast** · `C(X)↓ + C(Y)↑`
**Rationale.** ...
**Effectiveness factors.** ...

---

## Generic Analysis
### Influence Mechanism
**Psychological principle.** {named theorist citations}
**Decision alteration.** ...
**Optimal conditions.** ...

### Representative Scenario 1
{full scenario with template levers}

### Representative Scenario 2
{distinct scenario}

### Versatility
**Level:** high
**Explanation.** ...

### Core Strategy
**#8 Cost Contrast** · `C(X)↓ + C(Y)↑`

### Application Examples
- Corporate: ...
- Government: ...
- Academic: ...
- Military: ...

---

## Integrated Insights
### Pattern Recognition
...

### Strategic Implications
...

### Resolution Approach
...

---

## Metadata
- **Tactic ID:** `{tid}`
- **Cluster:** `{cluster_id}`
- **Source index:** {N}
- **Theorists cited:** {list}
```

## Not yet implemented

**See `../NEEDED_NEXT.md` for outstanding requirements.** The most important: **vector DB for semantic search** is a need-to-have, not yet built.

## Provenance

This markdown layer was generated from `../99_assembled_output.json` on 2026-06-10. To regenerate after any source updates, re-run the markdown generation script (logic preserved in workspace).

## LSPI binding (v1.2+)

The catalogue is bound to LSPI as its typed action layer via the sidecar **`INDEX-lspi.json`** (the tactic files themselves are Mode E and unmodified). Per tactic: `lspi_levers` (signed, intensity-weighted deltas over the decision-matrix cells) and an `epsilon_template` — instantiating a tactic binds the slash-address prefix and concrete resources, yielding a normal LSPI execution line. **Alias map (mandatory in all integrated artifacts):** corpus `X` → **P** (preferred position), corpus `Y` → **Adv** (adverse alternative) — LSPI's own `X` names the *adverse* alternative, so bare letters silently invert meaning across the two systems. The lever prose inside tactic bodies keeps its native B(X)/C(Y) language; the sidecar translates at the boundary.

### Facet coverage — complete (v1.2.0, sidecar `1.2.0-ws4.6`, 2026-07-24)

All seven LSPI facets are now populated for the full corpus. WS4 passes 1–6 are done; status, measured coverage and the extraction exceptions are in `../lspi/WS4-RUNBOOK.md`.

| Facet | Coverage | Vocabulary |
|---|---|---|
| `lspi_levers` + `epsilon_template` / `epsilon_tuple` | 779 records (4 have no derivable levers) | components `P/b`, `P/c`, `Adv/b`, `Adv/c`; sign `+` / `−`; intensity 1–3. Template is the spec's three-place form: `[a.] ε_ID(<addr>/e.) → { deltas } consuming { θ }` |
| `required_resources` | 782 of 783 | 9 carrier types — `money`, `hard_asset`, `credibility`, `attribute`, `legitimacy`, `information`, `access`, `title`, `tribe`; role `enabling` (needed to act) or `consumed` (spent by acting) |
| `detectability` | 782 of 783 | level `low` / `med` / `high`, plus a per-tactic `signature` — the observable tell, which doubles as the probe target for the estimation loop |
| `certainty_class` | 782 of 783 | `certain` / `probable` / `extra_conditional` / `spurious` |
| `ethical_valence` | 782 of 783 | axes `deception`, `coercion`, `fairness`, `transparency`, `dignity`, `loyalty_exploitation`, `harm_to_third_parties`, `institutional_damage`; severity 1–3 — feeds the ETHICAL-ACCOUNTING gate |
| `counter_tactic_ids` | 152 records / 174 links | tactic IDs only; `counters_tactic_ids` (70 records) is the **derived reciprocal**, never hand-authored |
| `provenance` | 606 records | `lam_table3_refs` (Lam 2018 Table 3 row numbers) + vignette references; covers 127 of the 148 manifest rows |

The one record without facets is `0037`, the corpus placeholder ("not a tactic"); its `facet_status` says so explicitly rather than leaving the gap silent. Interpretive facets are **P10 proposals pending operator QA**, not findings.

### The Mode E rule, plainly

**Facets live in `INDEX-lspi.json`. Tactic bodies are never edited.** Every LSPI addition to this catalogue is an addition to the sidecar — a separate file keyed by `tactic_id`. No pass, script or agent writes into `tactics/`, `by-strategy/`, `by-cluster/`, `by-theorist/` or `INDEX.json`. This keeps the corpus byte-identical to its upstream source so it can be re-generated at any time without merging hand-edits, and it keeps derived, interpretive material (which is revisable) physically separate from the analyzed substrate (which is not). Regenerate with `tools/extract-lspi-levers.py` — idempotent, and it preserves the interpretive facets it did not produce. Bare corpus `X`/`Y` appear **only** in `lspi_levers[].corpus_lever`, `alias_map`, `component_map` and the sidecar's own `_doc` note; everything downstream speaks `P`/`Adv` (F9/F10).
