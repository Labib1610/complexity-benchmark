#!/usr/bin/env python3
"""Realistic baseline for family 15 / criterion 3 (disjoint alphabets, no shared motif).

A solution that does NOT intersect alphabets and instead tries to actually find a shared
motif -- the same memo-less recursive LCS over the k sequences. With mutually disjoint
alphabets no letter is ever shared, so it never takes a letter and explores the whole
interleaving tree (exponential) before concluding length 0 -> TLE. Only then does it
print NONE. The reference's O(total) alphabet intersection is instant.
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
                return 0
        chars = {seqs[j][pos[j]] for j in range(k)}
        best = 0
        if len(chars) == 1:
            best = 1 + lcs(tuple(p + 1 for p in pos))
        for j in range(k):
            nxt = list(pos); nxt[j] += 1
            v = lcs(tuple(nxt))
            if v > best:
                best = v
        return best

    L = lcs(tuple([0] * k))
    print("NONE" if L == 0 else "SOME")


main()
