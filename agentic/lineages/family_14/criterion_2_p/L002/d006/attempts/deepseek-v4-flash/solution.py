import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    focal = list(map(int, input().split()))
    focal_set = set(focal)
    
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t == 1:
        print(0)
        return
    
    # If t is large, use tree marking method
    if t > 15:
        # Root at 1
        parent = [0]*(n+1)
        depth = [0]*(n+1)
        stack = [(1, 0, 0)]
        parent[1] = -1
        while stack:
            u, p, d = stack.pop()
            depth[u] = d
            for v, w in adj[u]:
                if v != p:
                    parent[v] = u
                    stack.append((v, u, d+1))
        
        # Mark nodes on paths from focal nodes to root
        marked = [False]*(n+1)
        for f in focal:
            x = f
            while x != -1 and not marked[x]:
                marked[x] = True
                x = parent[x]
        
        # Sum edges where both endpoints are marked
        total = 0
        for u, v, w in edges:
            if marked[u] and marked[v]:
                total += w
        print(total)
        return
    
    # Small t: bitmask DP
    focal_index = {v: i for i, v in enumerate(focal)}
    full_mask = (1 << t) - 1
    
    dp = [[float('inf')] * (1 << t) for _ in range(n+1)]
    
    def dfs(u, p):
        dp[u][0] = 0
        if u in focal_index:
            dp[u][1 << focal_index[u]] = 0
        
        for v, w in adj[u]:
            if v == p:
                continue
            dfs(v, u)
            new_dp = [float('inf')] * (1 << t)
            for mask_u in range(1 << t):
                if dp[u][mask_u] == float('inf'):
                    continue
                for mask_v in range(1 << t):
                    if dp[v][mask_v] == float('inf'):
                        continue
                    # Option 1: don't take edge (u,v)
                    new_dp[mask_u | mask_v] = min(new_dp[mask_u | mask_v], dp[u][mask_u] + dp[v][mask_v])
                    # Option 2: take edge (u,v)
                    new_dp[mask_u | mask_v] = min(new_dp[mask_u | mask_v], dp[u][mask_u] + dp[v][mask_v] + w)
            dp[u] = new_dp
    
    dfs(1, 0)
    print(dp[1][full_mask])

if __name__ == "__main__":
    solve()