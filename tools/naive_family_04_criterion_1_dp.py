#!/usr/bin/env python3
"""Alternative naive for family 04 / criterion 1: boolean DP over sums, O(n*T).

This is *pseudo-polynomial*: with the target T up to 4*10^10 the reachable-sum
array cannot be allocated (MemoryError) let alone filled in time. It demonstrates
that the second plausible naive route is also blocked by the large-value design.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    costs = [int(data[1 + i]) for i in range(n)]
    T = int(data[1 + n])
    if T < 0:
        print("NO"); return
    reach = bytearray(T + 1)          # size up to 4e10 -> MemoryError on large T
    reach[0] = 1
    for c in costs:
        if c > T:
            continue
        for j in range(T, c - 1, -1):
            if reach[j - c]:
                reach[j] = 1
    print("YES" if reach[T] else "NO")


main()
