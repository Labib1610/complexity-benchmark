#!/usr/bin/env python3
"""Realistic baseline for family 07 / criterion 3 (forbidden substring).

A solution that does NOT notice the offending fragment and instead tries to actually
assemble a common superstring first (permutation search over the fragments, merging on
max overlap), only afterwards scanning for the fragment that contains the forbidden
string F. The assembly is exponential in the number of fragments, so it TLEs once there
are more than a handful; the reference's O(k*|F|) scan is instant.
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    frags = [data[1 + i].decode() for i in range(k)]
    F = data[1 + k].decode()

    # --- attempt to assemble a shortest common superstring (exponential) ---------
    remove = [False] * k
    for i in range(k):
        for j in range(k):
            if i != j and frags[i] in frags[j] and \
               (len(frags[i]) < len(frags[j]) or (len(frags[i]) == len(frags[j]) and j < i)):
                remove[i] = True
                break
    live = [frags[i] for i in range(k) if not remove[i]]
    m = len(live)
    ov = [[0] * m for _ in range(m)]
    for i in range(m):
        a = live[i]
        for j in range(m):
            if i == j:
                continue
            b = live[j]
            for L in range(min(len(a), len(b)), 0, -1):
                if a[len(a) - L:] == b[:L]:
                    ov[i][j] = L
                    break
    best = [None]

    def search(mask, last, clen, count):
        if count == m:
            if best[0] is None or clen < best[0]:
                best[0] = clen
            return
        if best[0] is not None and clen >= best[0]:
            return
        for j in range(m):
            if mask >> j & 1:
                continue
            search(mask | (1 << j), j, clen + len(live[j]) - ov[last][j], count + 1)

    if m >= 1:
        for st in range(m):
            search(1 << st, st, len(live[st]), 1)

    # --- only now report the offending fragment ---------------------------------
    for i in range(k):
        if F in frags[i]:
            print(i + 1); return


main()
