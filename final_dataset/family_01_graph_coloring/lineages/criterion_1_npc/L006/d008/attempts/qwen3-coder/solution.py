def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Precompute forbidden pairs
    forbidden = set()
    for s_u in [1, 2, 3]:
        for s_v in [1, 2, 3]:
            if (s_u**3 + s_v**3) % 7 == (s_u**2 * s_v + s_u * s_v**2) % 7:
                forbidden.add((s_u, s_v))
    
    # Try all 3^n assignments
    def is_valid_assignment(assignment):
        for u, v in edges:
            if (assignment[u], assignment[v]) in forbidden:
                return False
        return True
    
    # Generate all possible assignments
    def backtrack(index, assignment):
        if index > n:
            return is_valid_assignment(assignment)
        
        for state in [1, 2, 3]:
            assignment[index] = state
            if backtrack(index + 1, assignment):
                return True
        return False
    
    assignment = [0] * (n + 1)
    if backtrack(1, assignment):
        print("YES")
        print(*assignment[1:])
    else:
        print("NO")

solve()