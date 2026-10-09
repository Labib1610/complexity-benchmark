import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # number of cargo types, always 1
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, i))
        adj[v].append((u, i))  # for residual graph
    
    # Build flow network with residual edges
    # Each edge gets a forward and backward edge in residual graph
    g = [[] for _ in range(n + 1)]
    edge_info = []  # (to, rev_idx, cap, is_forward)
    
    for i, (u, v, cap) in enumerate(edges):
        # Forward edge
        forward_idx = len(g[u])
        backward_idx = len(g[v])
        g[u].append([v, cap, backward_idx])  # [to, cap, rev_idx]
        g[v].append([u, 0, forward_idx])     # reverse edge
        edge_info.append((u, forward_idx))  # track original edge position
    
    def bfs_level(s, t, level):
        level[:] = [-1] * (n + 1)
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev in g[u]:
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] != -1
    
    def dfs_flow(u, t, f, level, ptr):
        if u == t:
            return f
        for i in range(ptr[u], len(g[u])):
            ptr[u] = i
            v, cap, rev = g[u][i]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs_flow(v, t, min(f, cap), level, ptr)
                if pushed > 0:
                    g[u][i][1] -= pushed
                    g[v][rev][1] += pushed
                    return pushed
        return 0
    
    def max_flow(s, t):
        flow = 0
        level = [-1] * (n + 1)
        while bfs_level(s, t, level):
            ptr = [0] * (n + 1)
            while True:
                pushed = dfs_flow(s, t, float('inf'), level, ptr)
                if pushed == 0:
                    break
                flow += pushed
        return flow
    
    flow = max_flow(s, t)
    
    if flow < d:
        print("NO")
        return
    
    print("YES")
    result = []
    for i in range(m):
        u, fwd_idx = edge_info[i]
        # The flow on original edge is original cap minus remaining capacity
        original_cap = edges[i][2]
        remaining = g[u][fwd_idx][1]
        flow_on_edge = original_cap - remaining
        result.append(str(flow_on_edge))
    
    print(' '.join(result))

if __name__ == "__main__":
    solve()