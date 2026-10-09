import sys

def solve():
    data = sys.stdin.read().strip().split()
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
    
    # Forbidden colors for each vertex
    forbidden = [0] * n
    color = [0] * n
    
    # Sort vertices by degree descending to improve pruning
    order = list(range(n))
    order.sort(key=lambda x: -sum(adj[x]))
    
    # Precompute neighbors list for faster iteration
    neighbors = [ [j for j in range(n) if adj[i][j]] for i in range(n) ]
    
    def dfs(k):
        if k == n:
            return True
        
        u = order[k]
        if color[u] != 0:
            return dfs(k + 1)
        
        # Try colors 1, 2, 3
        for c in range(1, 4):
            if forbidden[u] & (1 << c):
                continue
            
            # Check against already colored neighbors
            ok = True
            for v in neighbors[u]:
                if color[v] == c:
                    ok = False
                    break
            if not ok:
                continue
            
            color[u] = c
            
            # Mark forbidden for uncolored neighbors
            changed = []
            for v in neighbors[u]:
                if color[v] == 0:
                    if not (forbidden[v] & (1 << c)):
                        forbidden[v] |= (1 << c)
                        changed.append(v)
            
            if dfs(k + 1):
                return True
            
            # Backtrack
            for v in changed:
                forbidden[v] &= ~(1 << c)
            color[u] = 0
        
        return False
    
    if dfs(0):
        # Reconstruct answer in original order
        ans = [0] * n
        for i in range(n):
            ans[order[i]] = color[order[i]]
        print("YES")
        print(' '.join(map(str, ans)))
    else:
        print("NO")

solve()