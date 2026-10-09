import sys
from math import gcd
from functools import reduce


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    d = [int(data[1 + i]) for i in range(n)]
    total = sum(d)

    # Certificate 1: an odd total cannot split into two equal whole halves.
    if total % 2 != 0:
        print("ODD")
        return

    # Certificate 2: one task exceeds half the total, so its machine can never be balanced.
    if 2 * max(d) > total:
        print("MAX")
        return

    # Certificate 3: a common divisor g of all durations that does not divide total/2. Every
    # machine total is a multiple of g, so the required half is unreachable.
    g = reduce(gcd, d, 0)
    if g >= 2 and (total // 2) % g != 0:
        print(f"MOD {g}")
        return

    # Inputs for this criterion always satisfy one of the three certificates; defensive fallback.
    print("ODD")


main()
