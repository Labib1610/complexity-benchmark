#!/usr/bin/env python3
"""Worst-case (witness-graded) tier for family 05 — 3-DIMENSIONAL MATCHING.

3DM is NP-complete and has a CHEAP witness (the k chosen triples), so this escapes the gradeable
ceiling exactly like colouring: we plant a perfect matching (guaranteeing YES), add decoy triples near
the hardness threshold, and grade by VERIFYING the model's matching in O(k) -- no reference solve. Near
the threshold, a matching exists but FINDING it needs exponential search -> the solver TLEs.

I/O (same as the seed):
  input : line 1 = "k t"; next t lines = "x y z" allowed triples (1..k).
  output: "YES" then k lines "x y z" (a perfect matching), or "NO".
"""
import argparse, random, sys


def plant(k, ratio, seed):
    """Planted perfect matching {(i, py[i], pz[i])} + random decoy triples up to t = ratio*k.
    The matching guarantees a YES; near ratio ~ the 3DM threshold the decoys hide it."""
    rng = random.Random(seed * 2_650_011 + k)
    py = list(range(1, k + 1)); rng.shuffle(py)
    pz = list(range(1, k + 1)); rng.shuffle(pz)
    triples = set((i + 1, py[i], pz[i]) for i in range(k))   # planted matching
    t_target = int(ratio * k)
    guard = 0
    while len(triples) < t_target and guard < 100 * t_target + 5000:
        guard += 1
        triples.add((rng.randint(1, k), rng.randint(1, k), rng.randint(1, k)))
    trips = list(triples); rng.shuffle(trips)
    lines = [f"{k} {len(trips)}"] + [f"{x} {y} {z}" for x, y, z in trips]
    return "\n".join(lines) + "\n"


def grade(input_text, output_text):
    """WITNESS-only: PASS iff output is a perfect matching using only allowed triples."""
    d = input_text.split(); k = int(d[0]); t = int(d[1])
    allowed = set()
    for i in range(t):
        allowed.add((int(d[2 + 3*i]), int(d[3 + 3*i]), int(d[4 + 3*i])))
    toks = output_text.split()
    if not toks:
        return False, "empty output"
    if toks[0].upper() == "NO":
        return False, "reported NO but a matching was planted"
    nums = toks[1:] if toks[0].upper() == "YES" else toks
    try:
        v = [int(x) for x in nums]
    except ValueError:
        return False, "non-integer in output"
    if len(v) != 3 * k:
        return False, f"expected {k} triples ({3*k} ints), got {len(v)}"
    xs, ys, zs = set(), set(), set()
    for i in range(k):
        x, y, z = v[3*i], v[3*i+1], v[3*i+2]
        if (x, y, z) not in allowed:
            return False, f"triple ({x},{y},{z}) not in allowed set"
        xs.add(x); ys.add(y); zs.add(z)
    if xs != set(range(1, k+1)) or ys != set(range(1, k+1)) or zs != set(range(1, k+1)):
        return False, "not a perfect matching (some element repeated/missing)"
    return True, "valid perfect matching"


def _backtrack_solves(input_text, deadline_s):
    """Simple witness-search solver (used only to measure hardness/TLE), with a wall-clock budget."""
    import time
    d = input_text.split(); k = int(d[0]); t = int(d[1])
    trips = [(int(d[2+3*i]), int(d[3+3*i]), int(d[4+3*i])) for i in range(t)]
    by_x = {}
    for tr in trips:
        by_x.setdefault(tr[0], []).append(tr)
    t0 = time.monotonic()
    usedY, usedZ = set(), set()
    order = sorted(by_x, key=lambda x: len(by_x[x]))  # MRV-ish
    def rec(i):
        if time.monotonic() - t0 > deadline_s:
            raise TimeoutError
        if i == len(order):
            return True
        x = order[i]
        for (_, y, z) in by_x[x]:
            if y not in usedY and z not in usedZ:
                usedY.add(y); usedZ.add(z)
                if rec(i + 1):
                    return True
                usedY.discard(y); usedZ.discard(z)
        return False
    try:
        return rec(0), time.monotonic() - t0
    except TimeoutError:
        return None, time.monotonic() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", action="store_true"); ap.add_argument("--grade", metavar="F")
    ap.add_argument("--k", type=int, default=120); ap.add_argument("--ratio", type=float, default=6.0)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    if a.gen:
        sys.stdout.write(plant(a.k, a.ratio, a.seed))
    elif a.grade:
        ok, msg = grade(open(a.grade).read(), sys.stdin.read())
        print("PASS" if ok else "FAIL", "--", msg); sys.exit(0 if ok else 1)
    else:
        ap.error("use --gen or --grade")


if __name__ == "__main__":
    main()
