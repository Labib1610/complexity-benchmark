#!/usr/bin/env python3
"""Realistic baseline for family 11 / criterion 1 (set cover decision).

Try every combination of k consultants, union their skill masks, check full coverage
(early exit on the first covering selection). Natural without the bitmask DP. Costs
O(C(s,k)); with u held moderate and s pushed up, C(s,k) explodes while the 2^u*s DP
reference is unaffected -- that asymmetry is the window.
"""
import sys
import itertools


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    u = int(data[idx]); s = int(data[idx + 1]); k = int(data[idx + 2]); idx += 3
    masks = []
    for _ in range(s):
        cnt = int(data[idx]); idx += 1
        mk = 0
        for _ in range(cnt):
            sk = int(data[idx]); idx += 1
            mk |= 1 << (sk - 1)
        masks.append(mk)

    full = (1 << u) - 1
    for combo in itertools.combinations(range(s), k):
        cov = 0
        for i in combo:
            cov |= masks[i]
        if cov == full:
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(str(i + 1) for i in combo) + "\n")
            return
    sys.stdout.write("NO\n")


main()
