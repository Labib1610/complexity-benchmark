import sys
import math

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    costs = [int(next(it)) for _ in range(n)]
    T = int(next(it))
    
    total = sum(costs)
    if T > total:
        print("SUM")
        return
    
    # Compute GCD of all costs
    g = 0
    for c in costs:
        g = math.gcd(g, c)
    
    if g >= 2 and T % g != 0:
        print(f"MOD {g}")
    else:
        # This case shouldn't happen per problem guarantee
        # but we need to output something
        print("SUM")

if __name__ == "__main__":
    solve()