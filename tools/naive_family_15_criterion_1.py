#!/usr/bin/env python3
"""Realistic baseline for family 15 / criterion 1 (longest shared motif over k seqs).

Recursive LCS over the k sequences WITHOUT memoization: at each position, if all current
letters match take it, otherwise branch on advancing one of the k sequences. This is the
common model mistake and is exponential (~k^L). The k-dimensional memoized DP reference
is O(L^k). Small alphabets maximise the branching.
"""
import sys


def main():
    sys.setrecursionlimit(1000000)
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    seqs = [data[1 + i].decode() for i in range(k)]
    lens = [len(s) for s in seqs]

    def lcs(pos):
        for j in range(k):
            if pos[j] == lens[j]:
                return (0, "")
        chars = {seqs[j][pos[j]] for j in range(k)}
        best = (0, "")
        if len(chars) == 1:
            c = next(iter(chars))
            l, mo = lcs(tuple(p + 1 for p in pos))
            if 1 + l > best[0]:
                best = (1 + l, c + mo)
        for j in range(k):
            nxt = list(pos); nxt[j] += 1
            l, mo = lcs(tuple(nxt))
            if l > best[0]:
                best = (l, mo)
        return best

    L, motif = lcs(tuple([0] * k))
    sys.stdout.write(f"{L}\n{motif}\n")


main()
