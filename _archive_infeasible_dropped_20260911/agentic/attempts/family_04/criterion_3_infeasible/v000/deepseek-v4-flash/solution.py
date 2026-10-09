import math

n = int(input())
costs = list(map(int, input().split()))
T = int(input())

total = sum(costs)
if total < T:
    print("SUM")
else:
    g = 0
    for c in costs:
        g = math.gcd(g, c)
    if g > 1 and T % g != 0:
        print(f"MOD {g}")
    else:
        # This case shouldn't happen per problem guarantee,
        # but fallback to SUM if no divisor works.
        print("SUM")