#!/usr/bin/env python3
"""Realistic baseline for family 13 / criterion 2 (partition).

If the total is odd, print NO. Otherwise search for a subset of tasks summing to
total/2 by recursive include/exclude, pruning branches whose running sum exceeds the
target. Natural without meet-in-the-middle (criterion 1) / without the DP (criterion 2).
On even-sum-but-UNSPLITTABLE instances the target is never hit, so it explores
exhaustively and TLEs; the reference (MITM / DP) is fast.
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    d = [int(data[1 + i]) for i in range(n)]
    total = sum(d)
    if total % 2 != 0:
        sys.stdout.write("NO\n"); return
    target = total // 2

    chosen = []
    ans = [None]

    def rec(i, s):
        if s == target:
            ans[0] = chosen.copy(); return True
        if i == n or s > target:
            return False
        if s + d[i] <= target:
            chosen.append(i + 1)
            if rec(i + 1, s + d[i]):
                return True
            chosen.pop()
        return rec(i + 1, s)

    if rec(0, 0):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, ans[0])) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
