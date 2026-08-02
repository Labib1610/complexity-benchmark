#!/usr/bin/env python3
"""Realistic baseline for family 05 / criterion 1 (3-dimensional matching).

Backtracking: assign specialists 1..k in order; each takes an allowed triple whose
machine and slot are still free; backtrack on conflict. This is the natural,
competent solution (it does not add MITM/flow structure). On near-critical NO
instances it explores the search tree exhaustively. Same shape as the reference,
so ground truth is generated offline; here it TLEs at the model limit.
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    by_x = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx + 1]); z = int(data[idx + 2]); idx += 3
        by_x[x].append((y, z))
    for x in range(1, k + 1):
        by_x[x].sort()                  # deterministic order (same shape as reference)

    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    chosen = []

    def solve(x):
        if x > k:
            return True
        for (y, z) in by_x[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = used_z[z] = True
                chosen.append((x, y, z))
                if solve(x + 1):
                    return True
                chosen.pop()
                used_y[y] = used_z[z] = False
        return False

    if solve(1):
        out = ["YES"]; out.extend(f"{x} {y} {z}" for (x, y, z) in chosen)
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
