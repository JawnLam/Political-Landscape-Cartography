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
