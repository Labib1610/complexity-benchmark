import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0]); m = int(data[1])
    constraints = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        constraints.append((u, v))
    
    # For E(x) = x^2 - (cu+cv)x + cu*cv = (x-cu)(x-cv)
    # Minimum over real x is <= 0 always (achieved at x=cu or x=cv).
    # Strictly negative minimum iff cu != cv.
    # So each constraint requires cu != cv.
    # We need a 3-coloring of the graph; lexicographically smallest.
    
    adj = [[] for _ in range(n+1)]
    for u, v in constraints:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0]*(n+1)
    
    def valid(c, node):
        for nb in adj[node]:
            if color[nb] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
        for c in (1, 2, 3):
            if valid(c, node):
                color[node] = c
                if backtrack(node+1):
                    return True
                color[node] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(' '.join(str(color[i]) for i in range(1, n+1)))
    else:
        print("NO")

solve()