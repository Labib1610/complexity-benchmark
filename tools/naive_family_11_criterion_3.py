#!/usr/bin/env python3
"""Realistic baseline for family 11 / criterion 3 (a missing skill).

A solution that does NOT scan for the uncovered skill and instead tries to actually
build a full cover, searching selections of increasing size (all C(s,size)), and only
after that search fails to help does it report the uncoverable skill. Since one skill is
in no consultant, no selection ever covers everything, so the search explodes and TLEs;
the reference's O(total) scan is instant.
"""
import sys
import itertools


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    u = int(data[idx]); s = int(data[idx + 1]); idx += 2
    sets = []
    appears = [False] * (u + 1)
    for _ in range(s):
        cnt = int(data[idx]); idx += 1
        cur = set()
        for _ in range(cnt):
            sk = int(data[idx]); idx += 1
            cur.add(sk); appears[sk] = True
        sets.append(cur)

    # wasteful attempt: search for a full cover by increasing size (exponential)
    for size in range(0, s + 1):
        done = False
        for combo in itertools.combinations(range(s), size):
            cov = set()
            for i in combo:
                cov |= sets[i]
            if len(cov) == u:
                done = True
                break
        if done:
            break

    # only now report the smallest skill that appears in no consultant
    for sk in range(1, u + 1):
        if not appears[sk]:
            print(sk); return


main()
