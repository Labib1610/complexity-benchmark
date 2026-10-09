import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    s = int(next(it))
    t = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        radj[v].append((u, w))
        edges.append((u, v, w))
    
    INF = 10**18
    dist_s = [INF] * (n + 1)
    dist_t = [INF] * (n + 1)
    
    # Dijkstra from s
    dist_s[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = pq.pop()
        if d != dist_s[u]:
            continue
        for v, w in adj[u]:
            if dist_s[v] > d + w:
                dist_s[v] = d + w
                pq.append((dist_s[v], v))
    
    # Dijkstra from t
    dist_t[t] = 0
    pq = [(0, t)]
    while pq:
        d, u = pq.pop()
        if d != dist_t[u]:
            continue
        for v, w in radj[u]:
            if dist_t[v] > d + w:
                dist_t[v] = d + w
                pq.append((dist_t[v], v))
    
    # Check if s and t are already disconnected
    if dist_s[t] == INF:
        print("YES")
        print(0)
        return
    
    # Build level graph
    L = dist_s[t]
    level_nodes = [[] for _ in range(L + 1)]
    for v in range(1, n + 1):
        if dist_s[v] + dist_t[v] == L:
            level_nodes[dist_s[v]].append(v)
    
    # Build level graph edges
    level_edges = [[] for _ in range(L)]
    edge_info = {}  # (u, v) -> (w, level)
    
    for u, v, w in edges:
        if dist_s[u] + w + dist_t[v] == L:
            level = dist_s[u]
            level_edges[level].append((u, v, w))
            edge_info[(u, v)] = (w, level)
    
    # DP: dp[l] = min cost to cut all paths from level l to L
    dp = [INF] * (L + 1)
    dp[L] = 0
    
    for l in range(L - 1, -1, -1):
        # Option 1: cut all edges from level l
        cost1 = sum(w for _, _, w in level_edges[l])
        dp[l] = min(dp[l], cost1 + dp[l + 1])
        # Option 2: for each edge, cut it and recurse
        for u, v, w in level_edges[l]:
            if dist_s[v] > l + 1:
                dp[l] = min(dp[l], w + dp[l + 1])
            else:
                dp[l] = min(dp[l], w + dp[dist_s[v]])
    
    if dp[0] > B:
        print("NO")
        return
    
    # Reconstruct solution
    removed = []
    budget_left = B
    
    def cut_level(l, budget):
        nonlocal removed, budget_left
        # Try to cut edges at level l
        for u, v, w in level_edges[l]:
            if w <= budget:
                removed.append((u, v))
                budget -= w
        return budget
    
    # Greedy reconstruction
    for l in range(L):
        for u, v, w in level_edges[l]:
            if w <= budget_left:
                removed.append((u, v))
                budget_left -= w
    
    print("YES")
    print(len(removed))
    for u, v in removed:
        print(u, v)

if __name__ == "__main__":
    solve()