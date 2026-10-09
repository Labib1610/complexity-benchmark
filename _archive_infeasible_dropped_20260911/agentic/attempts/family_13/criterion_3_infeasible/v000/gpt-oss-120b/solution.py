import sys
import math

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:]

    total = sum(a)

    # 1. odd total
    if total & 1:
        print("ODD")
        return

    half = total // 2

    # 2. a task longer than half
    if max(a) > half:
        print("MAX")
        return

    # 3. common divisor that does not divide half
    g = 0
    for v in a:
        g = math.gcd(g, v)

    # problem guarantee ensures this condition holds here
    print(f"MOD {g}")

if __name__ == "__main__":
    solve()