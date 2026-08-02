#!/usr/bin/env python3
"""Realistic baseline for family 06 / criterion 2 (fractional bin packing).

The material may be split, so the answer is ceil(sum/C). This baseline does not use
the arithmetic shortcut; it SIMULATES filling containers, streaming the material in
and opening a new container each time the current one fills. That inner loop runs
ceil(sum/C) times in total -- O(n + sum/C) -- so with large weights it TLEs, while
the reference's O(n) ceil division is instant.
"""
import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1

    bins = 0
    load = 0
    for i in range(n):
        load += int(data[idx + i])
        while load >= C:                 # fill and close containers one at a time
            load -= C
            bins += 1
    if load > 0:
        bins += 1
    print(bins)


main()
