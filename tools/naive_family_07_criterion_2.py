#!/usr/bin/env python3
"""Realistic baseline for family 07 / criterion 2 (two-string merge).

Computes the max suffix-prefix overlap the naive way: for each candidate length L from
the longest down, test a[-L:] == b[:L] by slicing. Each slice+compare is O(L), and the
scan runs until it finds the overlap, so whenever the true overlap is far below the
string length the total cost is O(n^2). The reference does it in O(n) via KMP. Output
is identical (same candidate merges), so a student solving it correctly passes; the
O(n^2) simulator TLEs at n = 1e5.
"""
import sys


def naive_overlap(a, b):
    for L in range(min(len(a), len(b)), 0, -1):
        if a[len(a) - L:] == b[:L]:            # slicing compare -> O(L) each length
            return L
    return 0


def main():
    data = sys.stdin.buffer.read().split()
    s1 = data[0].decode()
    s2 = data[1].decode()

    cands = []
    if s1 in s2:
        cands.append(s2)
    if s2 in s1:
        cands.append(s1)
    cands.append(s1 + s2[naive_overlap(s1, s2):])
    cands.append(s2 + s1[naive_overlap(s2, s1):])

    best = min(cands, key=lambda x: (len(x), x))
    sys.stdout.write(best + "\n")


main()
