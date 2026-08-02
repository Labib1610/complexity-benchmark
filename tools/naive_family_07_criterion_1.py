#!/usr/bin/env python3
"""Realistic baseline for family 07 / criterion 1 (shortest common superstring).

Permutation search: recursively try each unused fragment next, merging on the max
suffix-prefix overlap, tracking the shortest (then lexicographically smallest) result,
with branch-and-bound pruning on the current length. This is the natural solution when
a model does not think of the Held-Karp bitmask DP. It matches the reference's answer
but, over a small alphabet where many orderings look promising, it explores ~k!
orderings and TLEs.
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    s = [data[1 + i].decode() for i in range(k)]

    # drop contained fragments (identical rule to the reference)
    remove = [False] * k
    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            if s[i] in s[j] and (len(s[i]) < len(s[j]) or (len(s[i]) == len(s[j]) and j < i)):
                remove[i] = True
                break
    frags = [s[i] for i in range(k) if not remove[i]]
    m = len(frags)
    if m == 1:
        sys.stdout.write(frags[0] + "\n")
        return

    ov = [[0] * m for _ in range(m)]
    for i in range(m):
        a = frags[i]
        for j in range(m):
            if i == j:
                continue
            b = frags[j]
            for L in range(min(len(a), len(b)), 0, -1):
                if a[len(a) - L:] == b[:L]:
                    ov[i][j] = L
                    break

    best = [None]

    def search(mask, last, clen, cstr, count):
        if count == m:
            cand = (clen, cstr)
            if best[0] is None or cand < best[0]:
                best[0] = cand
            return
        if best[0] is not None and clen >= best[0][0]:
            return                            # count<m -> final length > clen -> can't win
        for j in range(m):
            if mask >> j & 1:
                continue
            add = frags[j][ov[last][j]:]
            search(mask | (1 << j), j, clen + len(add), cstr + add, count + 1)

    for st in range(m):
        search(1 << st, st, len(frags[st]), frags[st], 1)

    sys.stdout.write(best[0][1] + "\n")


main()
