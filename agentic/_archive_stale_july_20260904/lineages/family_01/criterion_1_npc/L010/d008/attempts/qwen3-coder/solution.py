from itertools import product

def solve():
    n, m = map(int, input().split())
    
    # Read proximity pairs
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    
    # For E(x) = x^3 - (f_u + f_v)x^2 + (f_u * f_v)x to have 3 distinct real roots,
    # it must have 3 distinct real roots. 
    # E(x) = x(x^2 - (f_u + f_v)x + (f_u * f_v)) = x(x - f_u)(x - f_v)
    # So the roots are 0, f_u, and f_v.
    # For three distinct real roots, we need 0, f_u, f_v to be distinct.
    # Since f_u, f_v ∈ {1, 2, 3}, we need f_u ≠ f_v.
    
    # So for every edge (u,v), we need f_u ≠ f_v
    
    # Try all possible assignments in lexicographical order
    for assignment in product([1, 2, 3], repeat=n):
        valid = True
        for u, v in edges:
            if assignment[u] == assignment[v]:
                valid = False
                break
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()