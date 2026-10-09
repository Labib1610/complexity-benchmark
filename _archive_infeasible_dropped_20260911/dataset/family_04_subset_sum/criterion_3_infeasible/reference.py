import sys
from math import gcd
from functools import reduce


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    costs = [int(data[1 + i]) for i in range(n)]
    T = int(data[1 + n])

    # Certificate 1: the target exceeds the total of all costs -> unreachable.
    total = sum(costs)
    if T > total:
        print("SUM")
        return

    # Certificate 2: a common divisor of all costs that does not divide T. Every subset sum is
    # a multiple of g = gcd(costs); if g does not divide T, no subset can equal T. g >= 2 here
    # because these instances are constructed with a modular obstruction.
    g = reduce(gcd, costs, 0)
    if g >= 2 and T % g != 0:
        print(f"MOD {g}")
        return

    # Inputs for this criterion always satisfy one of the two certificates above; this line is a
    # defensive fallback and is never reached on valid input.
    print("SUM")


main()
