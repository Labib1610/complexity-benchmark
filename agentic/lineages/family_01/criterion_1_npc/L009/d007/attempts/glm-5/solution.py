import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    constraints = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u > v:
            u, v = v, u
        constraints.append((u, v))
    
    # For values in {1,2,3}, points (c, c^2, c^3) are collinear with origin iff c_u == c_v
    # So constraint (u,v) means c_u != c_v
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in constraints:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n  # 0 = unassigned, 1/2/3 = assigned value
    
    def check_ok(node, val):
        for nb in adj[node]:
            if color[nb] == val:
                return False
        return True
    
    def dfs(idx):
        if idx == n:
            return True
        for val in (1, 2, 3):
            if check_ok(idx, val):
                color[idx] = val
                if dfs(idx + 1):
                    return True
                color[idx] = 0
        return False
    
    if dfs(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()