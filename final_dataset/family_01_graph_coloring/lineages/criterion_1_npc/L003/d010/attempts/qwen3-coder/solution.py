from itertools import product

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Interference matrix
    I = [
        [6, -3, -3],
        [-3, 6, -3],
        [-3, -3, 6]
    ]
    
    target_total = -3 * m
    
    # Try all 3^n assignments
    for assignment in product([1, 2, 3], repeat=n):
        total = 0
        valid = True
        
        # Check if this assignment gives the target total
        for u, v in edges:
            mode_u = assignment[u - 1] - 1  # Convert to 0-indexed
            mode_v = assignment[v - 1] - 1  # Convert to 0-indexed
            total += I[mode_u][mode_v]
            
        if total == target_total:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()