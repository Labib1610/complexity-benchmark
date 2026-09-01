import sys
from itertools import product

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Read constraints
    constraints = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        constraints.append((u-1, v-1))  # Convert to 0-indexed
    
    # For a quadratic function E(x) = x^2 - (c_u + c_v)x + c_u*c_v
    # The minimum value occurs at x = (c_u + c_v)/2
    # The minimum value is E((c_u + c_v)/2) = -((c_u - c_v)^2)/4
    # For this to be strictly negative, we need c_u != c_v
    
    # So the constraint is that for each pair (u,v), c_u != c_v
    
    # Try all possible assignments in lexicographical order
    for assignment in product([1, 2, 3], repeat=n):
        valid = True
        for u, v in constraints:
            if assignment[u] == assignment[v]:
                valid = False
                break
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()