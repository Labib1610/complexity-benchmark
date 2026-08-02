#!/usr/bin/env python3
"""Realistic baseline for family 12 / criterion 1 (0/1 knapsack, large values).

Recursive include/exclude search, O(2^n), with the standard pruning: never include an
item that would exceed the remaining budget. It tracks the best value AND a subset that
achieves it. Natural without meet-in-the-middle. With a tight budget (B ~ sum/2) the
pruning barely helps and it explores ~2^n, while MITM is 2^(n/2).
"""
import sys


def main():
    sys.setrecursionlimit(1 << 20)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    items = []
    for _ in range(n):
        c = int(data[idx]); v = int(data[idx + 1]); idx += 2
        items.append((c, v))

    best = [-1, 0]      # [best value, best mask]
    cur = [0]

    def rec(i, cost, val):
        if i == n:
            if val > best[0]:
                best[0] = val; best[1] = cur[0]
            return
        rec(i + 1, cost, val)                          # exclude i
        nc = cost + items[i][0]
        if nc <= B:                                    # include i (only if it fits)
            cur[0] |= (1 << i)
            rec(i + 1, nc, val + items[i][1])
            cur[0] &= ~(1 << i)

    rec(0, 0, 0)

    chosen = [i + 1 for i in range(n) if best[1] >> i & 1]
    sys.stdout.write(f"{best[0]}\n")
    sys.stdout.write(" ".join(map(str, chosen)) + "\n")


main()
