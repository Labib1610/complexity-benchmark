#!/usr/bin/env python3
"""Human annotation export + ingest (file 50, PART B8).

export:  write a stratified sample of ~100 versions to a blinded CSV -- no verifier
         scores shown, version ids hashed -- with blank G1..G4 score columns for a human
         to fill. Produce two copies (one per annotator).

ingest:  read two completed sheets, compute Krippendorff's alpha (ordinal) between the two
         annotators per criterion, and judge-vs-human accuracy and F1 at the configured
         acceptance threshold (the verifier's stored scores are the "judge"; the mean of
         the two humans is the "human" reference).

  python tools/human_annotation.py export --family 01 --sample 100
  python tools/human_annotation.py ingest --sheets a.csv b.csv
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

import backends as B
from judge_agreement import collect_sample, _read_json   # reuse stratified sampler

EXPORT_DIR = B.REPORTS_DIR / "human_annotation"
_CRITS = ["G1_unambiguity", "G2_completeness", "G3_faithfulness", "G4_naturalness"]
_SHORT = {"G1_unambiguity": "G1", "G2_completeness": "G2",
          "G3_faithfulness": "G3", "G4_naturalness": "G4"}
_THRESHOLDS = {"G1": 4, "G2": 4, "G3": 5, "G4": 3}


def _hash_id(family, cd, vid) -> str:
    return hashlib.sha1(f"{family}/{cd}/{vid}".encode()).hexdigest()[:10]


# --- export -----------------------------------------------------------------
def do_export(args):
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    thresholds = (B.load_run_config().get("gate", {}) or {}).get("thresholds", _THRESHOLDS)
    key_rows, sheet_rows = [], []
    for family in B.list_families(args.family):
        slug = B.family_slug(family)
        for cd, vdir, gate in collect_sample(family, args.criterion, args.sample):
            hid = _hash_id(family, cd, vdir.name)
            key_rows.append({"hash": hid, "family": family, "criterion": cd,
                             "version": vdir.name,
                             "verifier_composite": gate.get("composite"),
                             **{f"verifier_{_SHORT[c]}": gate.get("graded", {}).get(c, {}).get("score")
                                for c in _CRITS}})
            sheet_rows.append({"hash": hid,
                               "statement": (vdir / "statement.md").read_text(),
                               "G1": "", "G2": "", "G3": "", "G4": ""})
    # blinded sheets (one per annotator) -- statement + blank score columns only
    for who in ("annotator_A", "annotator_B"):
        path = EXPORT_DIR / f"{who}.csv"
        with path.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["hash", "statement", "G1", "G2", "G3", "G4"])
            w.writeheader()
            w.writerows(sheet_rows)
        print(f"[export] {path} ({len(sheet_rows)} rows)")
    # private key map (NOT given to annotators) -- used at ingest time
    keypath = EXPORT_DIR / "key.csv"
    with keypath.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(key_rows[0].keys()) if key_rows else ["hash"])
        w.writeheader()
        w.writerows(key_rows)
    (EXPORT_DIR / "thresholds.json").write_text(json.dumps(thresholds, indent=2))
    print(f"[export] {keypath} (blinding key, keep private)")


# --- Krippendorff's alpha (ordinal) -----------------------------------------
def _ordinal_metric(marginals):
    n_g = marginals

    def delta2(c, k):
        lo, hi = (c, k) if c <= k else (k, c)
        s = sum(n_g[g] for g in range(lo, hi + 1)) - (n_g[lo] + n_g[hi]) / 2.0
        return s * s
    return delta2


def krippendorff_alpha(units, kmax=6):
    """units: list of per-item rating lists (ints, Nones allowed). Ordinal alpha via the
    coincidence-matrix formulation. Returns None if undefined."""
    # coincidence matrix
    o = [[0.0] * kmax for _ in range(kmax)]
    total = 0.0
    for ratings in units:
        vals = [r for r in ratings if r is not None]
        m = len(vals)
        if m < 2:
            continue
        for a in range(m):
            for b in range(m):
                if a != b:
                    o[vals[a]][vals[b]] += 1.0 / (m - 1)
        total += m
    n_g = [sum(o[c]) for c in range(kmax)]        # marginals
    n = sum(n_g)
    if n < 2:
        return None
    delta2 = _ordinal_metric(n_g)
    D_o = sum(o[c][k] * delta2(c, k) for c in range(kmax) for k in range(kmax))
    D_e = sum(n_g[c] * n_g[k] * delta2(c, k) for c in range(kmax) for k in range(kmax)) / (n - 1)
    if D_e == 0:
        return 1.0
    return round(1 - D_o / D_e, 4)


# --- ingest -----------------------------------------------------------------
def _load_sheet(path):
    with open(path, newline="") as fh:
        return {row["hash"]: row for row in csv.DictReader(fh)}


def _to_int(x):
    try:
        return int(str(x).strip())
    except Exception:
        return None


def do_ingest(args):
    a = _load_sheet(args.sheets[0])
    b = _load_sheet(args.sheets[1])
    key = _load_sheet(EXPORT_DIR / "key.csv") if (EXPORT_DIR / "key.csv").exists() else {}
    thresholds = json.loads((EXPORT_DIR / "thresholds.json").read_text()) \
        if (EXPORT_DIR / "thresholds.json").exists() else _THRESHOLDS

    shared = [h for h in a if h in b]
    # per-criterion Krippendorff alpha between the two annotators
    alphas = {}
    for c in _CRITS:
        s = _SHORT[c]
        units = [[_to_int(a[h].get(s)), _to_int(b[h].get(s))] for h in shared]
        alphas[c] = krippendorff_alpha(units)

    # judge-vs-human accept decisions (human = mean of the two annotators, rounded)
    def accept(scores):
        return all(scores.get(_SHORT[c]) is not None and scores[_SHORT[c]] >= thresholds[_SHORT[c]]
                   for c in _CRITS)

    tp = fp = tn = fn = 0
    n_eval = 0
    for h in shared:
        krow = key.get(h, {})
        judge_scores = {_SHORT[c]: _to_int(krow.get(f"verifier_{_SHORT[c]}")) for c in _CRITS}
        human_scores = {}
        for c in _CRITS:
            va, vb = _to_int(a[h].get(_SHORT[c])), _to_int(b[h].get(_SHORT[c]))
            human_scores[_SHORT[c]] = round((va + vb) / 2) if va is not None and vb is not None else None
        if any(v is None for v in judge_scores.values()) or any(v is None for v in human_scores.values()):
            continue
        j, hh = accept(judge_scores), accept(human_scores)
        n_eval += 1
        tp += j and hh
        fp += j and not hh
        tn += (not j) and (not hh)
        fn += (not j) and hh

    precision = tp / (tp + fp) if (tp + fp) else None
    recall = tp / (tp + fn) if (tp + fn) else None
    f1 = (2 * precision * recall / (precision + recall)
          if precision and recall else None)
    accuracy = (tp + tn) / n_eval if n_eval else None

    out = {"n_shared": len(shared), "n_evaluated": n_eval,
           "krippendorff_alpha_ordinal": alphas,
           "judge_vs_human": {"accuracy": round(accuracy, 4) if accuracy is not None else None,
                              "precision": round(precision, 4) if precision is not None else None,
                              "recall": round(recall, 4) if recall is not None else None,
                              "f1": round(f1, 4) if f1 is not None else None,
                              "confusion": {"tp": tp, "fp": fp, "tn": tn, "fn": fn}},
           "thresholds": thresholds}
    outpath = B.REPORTS_DIR / "human_annotation_agreement.json"
    outpath.write_text(json.dumps(out, indent=2))
    print(f"[ingest] {outpath}")
    print(f"  alpha (ordinal): {alphas}")
    print(f"  judge-vs-human: {out['judge_vs_human']}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    e = sub.add_parser("export")
    e.add_argument("--family", required=True)
    e.add_argument("--criterion", type=int, choices=[1, 2, 3])
    e.add_argument("--sample", type=int, default=100)
    i = sub.add_parser("ingest")
    i.add_argument("--sheets", nargs=2, required=True)
    args = ap.parse_args()
    if args.mode == "export":
        do_export(args)
    else:
        do_ingest(args)


if __name__ == "__main__":
    main()
