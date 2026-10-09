import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # unused '1'
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Build residual graph for max flow
    # Each edge gets a reverse edge with capacity 0
    adj = [[] for _ in range(n + 1)]
    edge_info = []  # (to, rev_idx, cap, original_cap, original_idx)
    
    for i, (u, v, cap) in enumerate(edges):
        # Forward edge
        forward_idx = len(edge_info)
        adj[u].append(forward_idx)
        edge_info.append([v, -1, cap, cap, i])  # rev_idx will be set after reverse is added
        
        # Reverse edge
        reverse_idx = len(edge_info)
        adj[v].append(reverse_idx)
        edge_info.append([u, forward_idx, 0, 0, -1])  # reverse edge, original_idx = -1
        
        # Set reverse index in forward edge
        edge_info[forward_idx][1] = reverse_idx
    
    # Dinic's algorithm
    level = [0] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for eidx in adj[u]:
                to, _, cap, _, _ = edge_info[eidx]
                if cap > 0 and level[to] == -1:
                    level[to] = level[u] + 1
                    q.append(to)
        return level[t] != -1
    
    def dfs(u, flow):
        if u == t:
            return flow
        while ptr[u] < len(adj[u]):
            eidx = adj[u][ptr[u]]
            to, rev_idx, cap, _, _ = edge_info[eidx]
            if cap > 0 and level[to] == level[u] + 1:
                pushed = dfs(to, min(flow, cap))
                if pushed > 0:
                    edge_info[eidx][2] -= pushed
                    edge_info[rev_idx][2] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    max_flow = 0
    while bfs():
        ptr = [0] * (n + 1)
        while True:
            pushed = dfs(s, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed
    
    if max_flow < d:
        print("NO")
        return
    
    print("YES")
    # Extract flow values for original edges
    flow_values = [0] * m
    for eidx, (to, rev_idx, cap, orig_cap, orig_idx) in enumerate(edge_info):
        if orig_idx >= 0:  # This is an original edge
            flow_values[orig_idx] = orig_cap - cap
    
    print(' '.join(map(str, flow_values)))

if __name__ == "__main__":
    solve()