import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u][v] = True
        adj[v][u] = True
    
    # ring[i] will be 1, 2, or 3. 0 means unassigned.
    ring = [0] * n
    
    # We use a recursive backtracking approach with pruning.
    # For each node, we try to assign a ring from {1, 2, 3}.
    # A ring r is valid for node u if no neighbor v of u has ring[v] == r.
    
    # To optimize, we can order nodes by degree (descending) to fail faster.
    # However, for n=40, simple recursion is often sufficient if well-pruned.
    # Let's just iterate 0 to n-1.
    
    found = False
    
    def backtrack(u):
        nonlocal found
        if found:
            return
        if u == n:
            found = True
            return
        
        # Optimization: if node u is already assigned (due to some logic), skip.
        # In this basic loop, it won't be. But if we reordered, we'd check.
        
        # Try rings 1, 2, 3
        for r in range(1, 4):
            # Check validity
            valid = True
            # We only need to check against neighbors v < u (already assigned)
            # since neighbors v > u are not yet assigned.
            # However, checking all neighbors is safer if logic changes.
            # Given the loop order 0..n-1, only v < u are assigned.
            # But checking all is fine.
            for v in range(n):
                if adj[u][v] and ring[v] == r:
                    valid = False
                    break
            
            if valid:
                ring[u] = r
                backtrack(u + 1)
                if found:
                    return
                ring[u] = 0 # Backtrack
    
    backtrack(0)
    
    if found:
        print("YES")
        print(*(ring))
    else:
        print("NO")

if __name__ == '__main__':
    solve()