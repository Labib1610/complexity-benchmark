import sys
import functools
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    items = []
    for _ in range(n):
        c = int(data[idx]); v = int(data[idx + 1]); idx += 2
        items.append((c, v))

    # Best value per unit of cost first. Take investments whole while the budget
    # allows; take a fraction of the next one to spend the remaining budget.
    def cmp(x, y):
        lhs = x[1] * y[0]   # x.value / x.cost  vs  y.value / y.cost
        rhs = y[1] * x[0]
        if lhs > rhs:
            return -1
        if lhs < rhs:
            return 1
        return 0

    items.sort(key=functools.cmp_to_key(cmp))

    rem = B
    total = Fraction(0)
    for c, v in items:
        if rem <= 0:
            break
        if c <= rem:
            total += v
            rem -= c
        else:
            total += Fraction(v * rem, c)
            rem = 0

    d = (Decimal(total.numerator) / Decimal(total.denominator)).quantize(
        Decimal("0.000001"), rounding=ROUND_HALF_UP
    )
    sys.stdout.write(f"{d}\n")


main()
