#!/usr/bin/env python3
"""Realistic baseline for family 06 / criterion 3 (an oversized item).

A solution that does NOT notice the oversized item and instead tries to actually pack
the shipment: it guesses the number of containers as ceil(sum/C) and backtracks,
placing each item (in input order) into any container with room. The oversized item
fits in none, so no packing exists; when that item sits at a HIGH index the search
packs the earlier items in exponentially many ways before failing. It TLEs at scale;
the reference's O(n) scan for the oversized item is instant.
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    w = [int(data[idx + i]) for i in range(n)]; idx += n

    total = sum(w)
    k = max(1, (total + C - 1) // C)     # a plausible container count (fractional bound)
    load = [0] * k

    def pack(i):
        if i == n:
            return True
        wi = w[i]
        for b in range(k):
            if load[b] + wi <= C:
                load[b] += wi
                if pack(i + 1):
                    return True
                load[b] -= wi
        return False

    pack(0)                              # exhaustive attempt (fails: oversized item)

    for i in range(n):
        if w[i] > C:
            print(i + 1); return


main()
