#!/usr/bin/env python3
"""Realistic baseline for family 15 / criterion 2 (LCS of two sequences).

Recursive LCS WITHOUT memoization, O(2^L) -- dead by L~30 -- while the O(L^2) 2-D DP
reference is fast. Reconstructs the lexicographically smallest LCS with the same greedy
as the reference (smallest next letter that stays on an optimal path), so the output
matches on the small instances where it finishes.
"""
import sys


def main():
    sys.setrecursionlimit(1000000)
    data = sys.stdin.buffer.read().split()
    s = data[0].decode()
    t = data[1].decode()
    n, m = len(s), len(t)

    def Llen(i, j):
        if i == n or j == m:
            return 0
        if s[i] == t[j]:
            return 1 + Llen(i + 1, j + 1)
        a = Llen(i + 1, j); b = Llen(i, j + 1)
        return a if a > b else b

    total = Llen(0, 0)
    res = []
    i = j = 0
    rem = total
    while rem > 0:
        for c in range(26):
            ch = chr(97 + c)
            pi = s.find(ch, i); pj = t.find(ch, j)
            if pi != -1 and pj != -1 and Llen(pi + 1, pj + 1) == rem - 1:
                res.append(ch); i = pi + 1; j = pj + 1; rem -= 1
                break

    sys.stdout.write(f"{total}\n" + "".join(res) + "\n")


main()
