#!/usr/bin/env python3
"""Realistic baseline for family 12 / criterion 2 (fractional knapsack).

Correct greedy but implemented as a repeated O(n) MAX-RATIO SCAN instead of one sort:
each step scans all remaining items for the best value/cost ratio and takes it. That is
O(n^2) and TLEs at n = 2e5, while the O(n log n) sorted reference is fast. Uses exact
rational arithmetic and identical 6-decimal rounding, so the output matches the
reference on the (small) instances where it finishes.
"""
import sys
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    cost = [0] * n; value = [0] * n
    for i in range(n):
        cost[i] = int(data[idx]); value[i] = int(data[idx + 1]); idx += 2

    taken = [False] * n
    rem = B
    total = Fraction(0)
    for _ in range(n):
        if rem <= 0:
            break
        best = -1
        for i in range(n):                              # O(n) scan each step -> O(n^2)
            if taken[i]:
                continue
            if best == -1 or value[i] * cost[best] > value[best] * cost[i]:
                best = i
        if best == -1:
            break
        taken[best] = True
        c, v = cost[best], value[best]
        if c <= rem:
            total += v; rem -= c
        else:
            total += Fraction(v * rem, c); rem = 0

    d = (Decimal(total.numerator) / Decimal(total.denominator)).quantize(
        Decimal("0.000001"), rounding=ROUND_HALF_UP)
    sys.stdout.write(f"{d}\n")


main()
