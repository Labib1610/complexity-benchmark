#!/usr/bin/env python3
"""Realistic baseline for family 06 / criterion 1 (bin packing).

Backtracking, heaviest-first, placing each item into every container 1..k that has
room -- but WITHOUT the reference's symmetry cut (which refuses to open more than one
currently-empty container, since empty containers are interchangeable). This is the
natural, competent solution a model writes without thinking about symmetry breaking.
On instances with duplicate weights and interchangeable empty bins it explores
astronomically many equivalent orderings and explodes, while the symmetry-pruned
reference survives.
"""
import sys


def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    w = [int(data[idx + i]) for i in range(n)]; idx += n

    order = sorted(range(n), key=lambda i: -w[i])     # heaviest-first (strong, standard)
    load = [0] * k
    assign = [0] * n

    def solve(pos):
        if pos == n:
            return True
        i = order[pos]; wi = w[i]
        for b in range(k):
            if load[b] + wi <= C:
                load[b] += wi
                assign[i] = b + 1
                if solve(pos + 1):
                    return True
                load[b] -= wi
            # (no symmetry cut: every empty container is tried separately)
        return False

    if solve(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, assign)) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
