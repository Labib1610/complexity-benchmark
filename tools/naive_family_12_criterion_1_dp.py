#!/usr/bin/env python3
"""Alternative naive for family 12 / criterion 1: the pseudo-polynomial O(n*B) DP.

The value table is indexed by budget, size B+1. With B up to ~2e10 this cannot be
allocated (MemoryError) let alone filled -- demonstrating the second plausible naive
route is also blocked by the large-value design.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    dp = [0] * (B + 1)                     # size up to ~2e10 -> MemoryError
    for _ in range(n):
        c = int(data[idx]); v = int(data[idx + 1]); idx += 2
        for j in range(B, c - 1, -1):
            if dp[j - c] + v > dp[j]:
                dp[j] = dp[j - c] + v
    print(dp[B])


main()
