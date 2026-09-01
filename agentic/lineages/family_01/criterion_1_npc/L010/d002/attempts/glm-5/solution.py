import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # Check if graph is 3-colorable using backtracking with pruning
    # We use bitmask representation for efficiency
    # color[i] will be 0, 1, or 2 (representing grids 1, 2, 3)
    
    color = [-1] * n
    possible = True
    
    # Process vertices in order 0, 1, ..., n-1
    # For each vertex, try colors 0, 1, 2 in order (lexicographically smallest)
    
    def backtrack(idx):
        if idx == n:
            return True
        
        u = idx
        used = 0
        # Check already colored neighbors
        for v in range(u):
            if (adj[u] >> v) & 1 and color[v] != -1:
                used |= 1 << color[v]
        
        for c in range(3):
            if not (used & (1 << c)):
                color[u] = c
                if backtrack(idx + 1):
                    return True
                color[u] = -1
        
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(str(c + 1) for c in color))
    else:
        print("NO")

solve()