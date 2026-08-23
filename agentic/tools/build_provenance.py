#!/usr/bin/env python3
"""Consolidated provenance record per criterion (file 50, PART C).

Every version has a parent; every lineage has a depth chain. That history is spread
across many edit.json / gate.json / lineage.json files and is unreadable. This walks
`versions/` and `lineages/` and emits, per criterion:

  reports/provenance/family_01_criterion_1_npc.json   consolidated record (C1)
  reports/provenance/family_01_criterion_1_npc.md     human-readable tree     (C2)
  reports/provenance/family_01_criterion_1_npc.dot    Graphviz export         (C3)

  python tools/build_provenance.py --family 01 [--criterion 1]
  python tools/build_provenance.py --family 01 --check   # consistency mode (C4)
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import backends as B

LINEAGES_DIR = B.AGENTIC / "lineages"
PROV_DIR = B.REPORTS_DIR / "provenance"

_ACCEPT = {"ACCEPT", "PASS"}
_REJECT = {"REJECT", "FAIL"}


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def _gate_brief(gate: dict) -> dict:
    return {"result": gate.get("result"), "composite": gate.get("composite")}


def _bucket(result) -> str:
    if result in _ACCEPT:
        return "accepted"
    if result == "FLAG":
        return "flagged"
    if result in _REJECT:
        return "rejected"
    return "unknown"


# --- collect versions -------------------------------------------------------
def collect_versions(family, crit_dir):
    base = B.VERSIONS_DIR / f"family_{family}" / crit_dir
    versions = {}
    if not base.exists():
        return versions
    for vdir in sorted(base.glob("v*")):
        if not (vdir / "statement.md").exists():
            continue
        edit = _read_json(vdir / "edit.json")
        gate = _read_json(vdir / "gate.json")
        versions[vdir.name] = {
            "parent": edit.get("parent", "seed"),
            "generation": edit.get("generation", 0),
            "source": edit.get("source", "?"),
            "strategies": edit.get("strategies", []) or [],
            "intensity": edit.get("intensity", ""),
            "gate": _gate_brief(gate),
            "used_as_lineage_seed": None,   # filled in from lineages
            "path": str(vdir.relative_to(B.AGENTIC)),
        }
    return versions


# --- collect lineages -------------------------------------------------------
def collect_lineages(family, crit_dir):
    base = LINEAGES_DIR / f"family_{family}" / crit_dir
    lineages = {}
    if not base.exists():
        return lineages
    for ldir in sorted(base.glob("L*")):
        lj = _read_json(ldir / "lineage.json")
        if not lj:
            continue
        per_depth = {e.get("depth"): e for e in lj.get("per_depth", [])}
        depths = []
        for dd in sorted(ldir.glob("d[0-9]*")):
            d = int(dd.name[1:])
            edit = _read_json(dd / "edit.json")
            gate = _read_json(dd / "gate.json")
            pd = per_depth.get(d, {})
            entry = {
                "depth": d,
                "parent": None if d == 0 else f"d{d - 1:03d}",
                "raw_passers": pd.get("raw_passers", []),
                "shortcut": pd.get("shortcut_name"),
            }
            if d == 0:
                entry["statement"] = f"{dd.name}/statement.md"
            else:
                entry["strategy"] = "+".join(edit.get("strategies", []) or [])
                entry["rung"] = edit.get("rung")
                entry["edit_parent"] = edit.get("parent")   # for --check
                entry["gate"] = _gate_brief(gate)
            depths.append(entry)
        lineages[ldir.name] = {
            "base_version": lj.get("base_version"),
            "base_strategy": lj.get("base_strategy", []),
            "outcome": lj.get("outcome"),
            "final_depth": lj.get("final_depth"),
            "depths": depths,
        }
    return lineages


# --- assemble ---------------------------------------------------------------
def build_record(family, crit_dir, slug):
    versions = collect_versions(family, crit_dir)
    lineages = collect_lineages(family, crit_dir)

    for lid, lin in lineages.items():
        bv = lin["base_version"]
        if bv in versions:
            versions[bv]["used_as_lineage_seed"] = lid

    edges = []
    for vid, v in versions.items():
        p = v["parent"]
        parent = "v000" if p == "seed" else p
        edges.append([parent, vid])
    for lid, lin in lineages.items():
        bv = lin["base_version"]
        if lin["depths"]:
            edges.append([bv, f"{lid}/d000"])
        for dep in lin["depths"]:
            if dep["depth"] > 0:
                edges.append([f"{lid}/d{dep['depth'] - 1:03d}", f"{lid}/d{dep['depth']:03d}"])

    buckets = {"accepted": 0, "flagged": 0, "rejected": 0, "unknown": 0}
    by_source, by_generation = {}, {}
    for v in versions.values():
        buckets[_bucket(v["gate"].get("result"))] += 1
        by_source[v["source"]] = by_source.get(v["source"], 0) + 1
        g = str(v["generation"])
        by_generation[g] = by_generation.get(g, 0) + 1
    max_depth = max((lin.get("final_depth") or 0 for lin in lineages.values()), default=0)

    seed_stmt = B.SEEDS_DIR / slug / crit_dir / "statement.md"
    return {
        "family": family,
        "criterion": crit_dir,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "seed": {"id": "v000", "statement_path": str(seed_stmt.relative_to(B.AGENTIC))
                 if seed_stmt.exists() else str(seed_stmt)},
        "versions": versions,
        "lineages": lineages,
        "edges": edges,
        "stats": {
            "versions_total": len(versions),
            "accepted": buckets["accepted"], "flagged": buckets["flagged"],
            "rejected": buckets["rejected"], "unknown": buckets["unknown"],
            "by_source": by_source, "by_generation": by_generation,
            "lineages": len(lineages), "max_depth_reached": max_depth,
        },
    }


# --- human-readable tree (C2) -----------------------------------------------
def render_md(rec) -> str:
    versions = rec["versions"]
    children = {}
    for vid, v in versions.items():
        p = "v000" if v["parent"] == "seed" else v["parent"]
        children.setdefault(p, []).append(vid)
    for kids in children.values():
        kids.sort()

    lines = ["v000  (seed)"]

    def line_for(vid, v):
        strat = "+".join(v["strategies"]) or "-"
        tag = f"{strat}/{v['intensity']}" if v["intensity"] else strat
        res = v["gate"].get("result") or "?"
        comp = v["gate"].get("composite")
        comp_s = f"{comp:.2f}" if isinstance(comp, (int, float)) else "-"
        seed_of = f"   → seed of {v['used_as_lineage_seed']}" if v["used_as_lineage_seed"] else ""
        return f"{vid}  {tag:<22} {v['source']:<12} {res:<7} {comp_s}{seed_of}"

    def walk(pid, prefix):
        kids = children.get(pid, [])
        for i, vid in enumerate(kids):
            last = i == len(kids) - 1
            branch = "└── " if last else "├── "
            lines.append(prefix + branch + line_for(vid, versions[vid]))
            walk(vid, prefix + ("    " if last else "│   "))

    walk("v000", "")

    for lid, lin in rec["lineages"].items():
        lines.append("")
        lines.append(f"{lid}  base={lin['base_version']}  outcome={lin['outcome']}  "
                     f"depth={lin['final_depth']}")
        for dep in lin["depths"]:
            passers = ",".join(dep.get("raw_passers", [])) or "-"
            sc = dep.get("shortcut") or ""
            if dep["depth"] == 0:
                lines.append(f"  d000  passers=[{passers}]              shortcut={sc!r}")
            else:
                g = dep.get("gate", {})
                comp = g.get("composite")
                comp_s = f"{comp:.2f}" if isinstance(comp, (int, float)) else "-"
                arrow = "  → all_defeated" if not dep.get("raw_passers") else ""
                lines.append(f"  d{dep['depth']:03d}  {dep.get('strategy','') or '-'}  "
                             f"{g.get('result','?')} {comp_s}  passers=[{passers}]"
                             f"   shortcut={sc!r}{arrow}")
    return "\n".join(lines) + "\n"


# --- Graphviz (C3) ----------------------------------------------------------
def render_dot(rec) -> str:
    def colour(result):
        return {"ACCEPT": "#bfe6b0", "PASS": "#bfe6b0", "FLAG": "#f5e0a3",
                "REJECT": "#f0b0b0", "FAIL": "#f0b0b0"}.get(result, "#dddddd")

    out = ["digraph provenance {", '  rankdir=LR;',
           '  node [shape=box, style="filled,rounded", fontname="monospace"];',
           '  "v000" [label="v000 (seed)", fillcolor="#cfe3ff"];']
    for vid, v in rec["versions"].items():
        res = v["gate"].get("result")
        pen = ', penwidth=3' if v["used_as_lineage_seed"] else ''
        label = f'{vid}\\n{"+".join(v["strategies"]) or "-"} {res or "?"}'
        out.append(f'  "{vid}" [label="{label}", fillcolor="{colour(res)}"{pen}];')
    # lineage depth nodes
    for lid, lin in rec["lineages"].items():
        for dep in lin["depths"]:
            nid = f"{lid}/d{dep['depth']:03d}"
            res = (dep.get("gate", {}) or {}).get("result")
            out.append(f'  "{nid}" [label="{nid}", fillcolor="{colour(res)}", shape=note];')
    # edges: solid = version derivation, dashed = lineage depth / seed link
    version_ids = set(rec["versions"]) | {"v000"}
    for a, b in rec["edges"]:
        both_versions = a in version_ids and b in version_ids
        style = "solid" if both_versions else "dashed"
        out.append(f'  "{a}" -> "{b}" [style={style}];')
    out.append("}")
    return "\n".join(out) + "\n"


# --- consistency check (C4) -------------------------------------------------
def check_record(rec) -> list[str]:
    problems = []
    versions = rec["versions"]
    known = set(versions) | {"v000", "seed"}
    for vid, v in versions.items():
        p = v["parent"]
        pnorm = "v000" if p == "seed" else p
        if pnorm not in known:
            problems.append(f"{vid}: parent {p!r} does not exist")
        elif pnorm not in ("v000",):
            pg = versions.get(pnorm, {}).get("generation")
            if pg is not None and v["generation"] != pg + 1:
                problems.append(f"{vid}: generation {v['generation']} != parent {pnorm} "
                                f"generation {pg} + 1")
        elif pnorm == "v000" and v["generation"] != 0:
            problems.append(f"{vid}: generation {v['generation']} but parent is the seed")

    for lid, lin in rec["lineages"].items():
        bv = lin["base_version"]
        if bv not in versions:
            problems.append(f"{lid}: base_version {bv!r} is missing")
        elif versions[bv]["gate"].get("result") not in _ACCEPT:
            problems.append(f"{lid}: base_version {bv} was not gate-accepted "
                            f"({versions[bv]['gate'].get('result')})")
        for dep in lin["depths"]:
            if dep["depth"] > 0:
                exp = f"d{dep['depth'] - 1:03d}"
                if dep.get("edit_parent") not in (exp, None) and dep.get("edit_parent") != exp:
                    problems.append(f"{lid}/d{dep['depth']:03d}: edit parent "
                                    f"{dep.get('edit_parent')!r} != {exp}")

    # orphaned dirs on disk with no usable record
    base = B.VERSIONS_DIR / f"family_{rec['family']}" / rec["criterion"]
    if base.exists():
        for vdir in base.glob("v*"):
            if vdir.is_dir() and vdir.name not in versions:
                problems.append(f"orphan version dir with no statement.md: {vdir.name}")
    return problems


# --- driver -----------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)   # id or 'all'
    ap.add_argument("--criterion", type=int, choices=[1, 2, 3])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    PROV_DIR.mkdir(parents=True, exist_ok=True)
    any_problem = False
    for family in B.list_families(args.family):
        slug = B.family_slug(family)
        crits = [B.criterion_dirname(args.criterion)] if args.criterion else \
            ["criterion_1_npc", "criterion_2_p", "criterion_3_infeasible"]
        for crit_dir in crits:
            if not (B.VERSIONS_DIR / f"family_{family}" / crit_dir).exists():
                continue
            rec = build_record(family, crit_dir, slug)
            stem = f"family_{family}_{crit_dir}"
            if args.check:
                problems = check_record(rec)
                any_problem = any_problem or bool(problems)
                tag = "OK" if not problems else f"{len(problems)} ISSUE(S)"
                print(f"[check] {stem}: {tag}")
                for p in problems:
                    print(f"    - {p}")
                continue
            (PROV_DIR / f"{stem}.json").write_text(json.dumps(rec, indent=2))
            (PROV_DIR / f"{stem}.md").write_text(render_md(rec))
            (PROV_DIR / f"{stem}.dot").write_text(render_dot(rec))
            s = rec["stats"]
            print(f"[provenance] {stem}: {s['versions_total']} versions "
                  f"({s['accepted']} acc / {s['flagged']} flag / {s['rejected']} rej), "
                  f"{s['lineages']} lineages, max_depth={s['max_depth_reached']}")
    if args.check and any_problem:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
