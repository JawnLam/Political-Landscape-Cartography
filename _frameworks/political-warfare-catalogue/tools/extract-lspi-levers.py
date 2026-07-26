#!/usr/bin/env python3
"""Regenerate INDEX-lspi.json (WS4 pass 2 — mechanical lever extraction).

Run from anywhere: python3 extract-lspi-levers.py [catalogue-root]
Default catalogue-root: the parent directory of this script.

What it does: for every tactic in INDEX.json, parse the markdown's
"#### <lever> — ... — **Active** · intensity N" headings into lspi_levers
(alias map: corpus X -> P, corpus Y -> Adv; sign per LSPI component),
derive the epsilon_template, and write INDEX-lspi.json.

PRESERVATION CONTRACT (v1.2.0-ws4.6): every interpretive facet written by
WS4 passes 3-6 — required_resources, detectability, certainty_class,
ethical_valence, counter_tactic_ids, counters_tactic_ids, provenance — and
each record's facet_status are carried forward verbatim from the existing
INDEX-lspi.json. Only levers and the derived epsilon forms are regenerated.
The epsilon_template is the spec's THREE-PLACE form:

    [a.] e_<ID>(<addr>/e.) -> { <signed component deltas> } consuming { <theta> }

where theta is rendered from the preserved required_resources facet. Records
with no required_resources emit the delta-only form (theta is unknown, not
empty). epsilon_tuple carries the same content structurally (delta / theta /
meta) so downstream consumers do not have to parse the string.

Safe to re-run any time the catalogue gains lever analyses. Known extraction
exceptions are reported in the `problems` log at the end of the run; see
../lspi/WS4-RUNBOOK.md for the current exception register.
"""
import json, re, os, sys, datetime

CAT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEVER_MAP = {"B(X)↑": ("P/b", "+"), "C(X)↓": ("P/c", "-"),
             "B(Y)↓": ("Adv/b", "-"), "C(Y)↑": ("Adv/c", "+")}
# Interpretive facets produced by WS4 passes 3-6. NEVER regenerated here.
FACETS = ["required_resources", "detectability", "certainty_class",
          "ethical_valence", "counter_tactic_ids", "counters_tactic_ids",
          "provenance"]
DEFAULT_STATUS = "levers_extracted; facets_pending (WS4 passes 3-6)"
line_pat = re.compile(r'^#### (B\(X\)↑|C\(X\)↓|B\(Y\)↓|C\(Y\)↑)([^\n]*)$', re.M)
inten_pat = re.compile(r'intensity\s*(\d)')

idx = json.load(open(os.path.join(CAT, "INDEX.json")))
prior, prior_top = {}, {}
lspi_path = os.path.join(CAT, "INDEX-lspi.json")
if os.path.exists(lspi_path):
    prior_top = json.load(open(lspi_path))
    prior = prior_top.get("tactics", {})


def theta_str(rr):
    """Render the theta (required-resources) half of the epsilon tuple."""
    if not rr:
        return None
    return ", ".join(f'{e.get("type")} ({e.get("role")})' for e in rr)


records, problems = {}, []
for t in idx["tactics"]:
    tid = t["tactic_id"]
    md = (t.get("file_markdown") or "").replace("markdown/tactics/", "tactics/")
    path = os.path.join(CAT, md) if md else ""
    levers, source, seen = [], None, {}
    if path and os.path.isfile(path):
        hits = line_pat.findall(open(path, encoding="utf-8").read())
        if hits:
            source = "active-levers-sections"
            for sym, rest in hits:
                comp, sign = LEVER_MAP[sym]
                if "Not active" in rest:
                    continue
                if "Active" in rest:
                    m = inten_pat.search(rest)
                    inten = int(m.group(1)) if m else None
                    # A tactic may carry several lever blocks (alternative
                    # interpretations). Collapse duplicates on the component,
                    # keeping the strongest declared intensity, so the emitted
                    # epsilon-template never lists the same cell twice.
                    if comp in seen:
                        prev = seen[comp]
                        if inten is not None and (prev["intensity"] is None or inten > prev["intensity"]):
                            prev["intensity"] = inten
                        problems.append((tid, f"duplicate lever block {sym} — merged (max intensity kept)"))
                        continue
                    lev = {"component": comp, "sign": sign,
                           "intensity": inten, "corpus_lever": sym}
                    seen[comp] = lev
                    levers.append(lev)
                else:
                    problems.append((tid, f"statusless heading {sym} — skipped"))
            if not levers:
                # Every heading present but all marked "Not active": a real
                # extraction outcome, not a silent zero. Report it.
                problems.append((tid, "all lever headings marked Not active — no levers"))
    if not levers and source is None:
        combo = ((t.get("generic_strategy") or {}).get("lever_combination", "") or "")
        # Fall back to the specific strategy when the generic one is silent.
        if not re.search(r'B\(X\)↑|C\(X\)↓|B\(Y\)↓|C\(Y\)↑', combo):
            combo = ((t.get("specific_strategy") or {}).get("lever_combination", "") or "")
        found = re.findall(r'(B\(X\)↑|C\(X\)↓|B\(Y\)↓|C\(Y\)↑)', combo)
        if found:
            source = "strategy-lever-combination-fallback"
            for sym in found:
                comp, sign = LEVER_MAP[sym]
                if comp in seen:      # prose often lists alternatives; dedupe
                    continue
                lev = {"component": comp, "sign": sign,
                       "intensity": None, "corpus_lever": sym}
                seen[comp] = lev
                levers.append(lev)
        else:
            problems.append((tid, "no levers found"))

    carried = {f: prior.get(tid, {}).get(f) for f in FACETS}
    deltas = [f"[<addr>/t/D/{l['component']}] {l['sign']}" +
              (f" ·i{l['intensity']}" if l["intensity"] is not None else "")
              for l in levers]
    th = theta_str(carried.get("required_resources"))
    rec = {
        "tactic_id": tid, "title": t["title"],
        "lspi_levers": levers, "lever_source": source,
        "epsilon_template": (("[a.] ε_%s(<addr>/e.) → { %s }" % (tid, ", ".join(deltas)))
                             + (f" consuming {{ {th} }}" if th else "")) if levers else None,
        "epsilon_tuple": ({"delta": deltas,
                           "theta": carried.get("required_resources") or [],
                           "meta": {"detectability": carried.get("detectability"),
                                    "certainty_class": carried.get("certainty_class"),
                                    "ethical_valence": carried.get("ethical_valence")}}
                          if levers else None),
        # Preserve the prior status verbatim when one exists; only brand-new
        # records get the pending default. (The old guard mangled any status
        # that began with "levers_extracted", which silently reverted
        # completed batches — fixed here.)
        "facet_status": prior.get(tid, {}).get("facet_status") or DEFAULT_STATUS,
    }
    rec.update(carried)
    records[tid] = rec

out = {
    "_doc": prior_top.get("_doc") or
            ("LSPI binding sidecar for the Political Warfare Catalogue (PLC v1.2, upgrade-plan WS4). "
             "Alias map: corpus X -> P (preferred position), corpus Y -> Adv (adverse alternative) — mandatory; "
             "bare corpus lever letters never appear in integrated artifacts (04-SCHEMA System 1). Regenerate with "
             "tools/extract-lspi-levers.py (preserves interpretive facets). This file is an ADDITION — "
             "the catalogue itself is Mode E."),
    "version": prior_top.get("version", "1.2.0-ws4.6"),
    "generated_at": datetime.date.today().isoformat(),
    "alias_map": {"corpus.X": "P", "corpus.Y": "Adv"},
    "component_map": {"B(X)↑": "P/b +", "C(X)↓": "P/c -", "B(Y)↓": "Adv/b -", "C(Y)↑": "Adv/c +"},
    "facet_vocabularies": prior_top.get("facet_vocabularies", {}),
    "tactic_count": len(records),
    "tactics": records,
}
with open(lspi_path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(f"records={len(records)}; problems={problems}")
