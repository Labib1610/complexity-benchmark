#!/usr/bin/env python3
"""Realistic baseline for family 04 / criterion 2 (subset sum, small values).

Include/exclude subset search, O(2^n), ignoring the small value/target bounds that
make the O(n*T) DP polynomial. On NO instances it explores all subsets whose sum
stays <= T (huge at large n) and TLEs, while the DP reference is instant.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    costs = [int(data[1 + i]) for i in range(n)]
    T = int(data[1 + n])
    sys.setrecursionlimit(1 << 20)
    chosen = []
    ans = [None]

    def rec(i, s):
        if s == T:
            ans[0] = chosen.copy(); return True
        if i == n or s > T:
            return False
        if s + costs[i] <= T:
            chosen.append(i + 1)
            if rec(i + 1, s + costs[i]):
                return True
            chosen.pop()
        return rec(i + 1, s)

    if rec(0, 0):
        print("YES"); print(' '.join(map(str, ans[0])))
    else:
        print("NO")


main()
