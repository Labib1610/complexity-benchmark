import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    commodities = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        commodities.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Build super source and super sink
    S = n
    T = n + 1
    N = n + 2
    
    # Build adjacency list for Dinic
    adj = [[] for _ in range(N)]
    edge_list = []
    
    def add_edge(u, v, cap):
        idx = len(edge_list)
        edge_list.append([u, v, cap, 0])  # [from, to, cap, flow]
        rev_idx = len(edge_list)
        edge_list.append([v, u, 0, 0])
        adj[u].append((idx, rev_idx))
        adj[v].append((rev_idx, idx))
    
    # Add edges from super source to each commodity origin
    for i, (s, t, d) in enumerate(commodities):
        add_edge(S, s, d)
    
    # Add edges from each commodity destination to super sink
    for i, (s, t, d) in enumerate(commodities):
        add_edge(t, T, d)
    
    # Add original edges with shared capacity
    for u, v, cap in edges:
        add_edge(u, v, cap)
    
    # Dinic's algorithm
    level = [0] * N
    ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        level[S] = 0
        q = deque([S])
        while q:
            u = q.popleft()
            for idx, _ in adj[u]:
                e = edge_list[idx]
                if e[2] > e[3] and level[e[1]] < 0:
                    level[e[1]] = level[u] + 1
                    q.append(e[1])
        return level[T] >= 0
    
    def dfs(u, f):
        if u == T:
            return f
        for i in range(ptr[u], len(adj[u])):
            ptr[u] = i
            idx, _ = adj[u][i]
            e = edge_list[idx]
            if e[2] > e[3] and level[e[1]] == level[u] + 1:
                pushed = dfs(e[1], min(f, e[2] - e[3]))
                if pushed > 0:
                    e[3] += pushed
                    edge_list[idx ^ 1][3] -= pushed
                    return pushed
        return 0
    
    total_demand = sum(d for _, _, d in commodities)
    flow = 0
    while bfs():
        ptr = [0] * N
        while True:
            pushed = dfs(S, float('inf'))
            if pushed == 0:
                break
            flow += pushed
    
    if flow != total_demand:
        print("NO")
        return
    
    # Extract flows for each commodity
    # We need to decompose the flow into paths for each commodity
    # Use flow decomposition
    
    # Build residual graph for flow decomposition
    res_adj = [[] for _ in range(n)]
    for j, (u, v, cap) in enumerate(edges):
        idx = 2 * (k + j) + 4 * k  # This needs recalculation
        # Actually, let's rebuild properly
    
    # Rebuild with tracking
    # Edges: S->s_i (k edges), t_i->T (k edges), then m original edges
    # Edge indices: 0 to 2k-1 are S->s_i and their reverse
    #               2k to 4k-1 are t_i->T and their reverse  
    #               4k to 4k+2m-1 are original edges and their reverse
    
    # Actually let me rebuild the edge tracking properly
    # We have: edges from S to origins (indices 0, 2, 4, ... 2(k-1))
    #          edges from dests to T (indices 2k, 2k+2, ... 2k+2(k-1))
    #          original edges (indices 4k, 4k+2, ... 4k+2(m-1))
    
    # Get flow on S->s_i edges (these tell us how much of each commodity is sent)
    # Then we need to decompose paths
    
    # Simpler approach: for each commodity, find paths from s_i to t_i
    # and track how much flow goes through each original edge
    
    # Build adjacency for original graph with flow info
    orig_adj = [[] for _ in range(n)]
    for j, (u, v, cap) in enumerate(edges):
        # Find the flow on this edge
        # The edge index in edge_list
        pass
    
    # Let me restart with cleaner edge tracking
    # Rebuild the graph with proper indexing
    
    # Clear and rebuild
    adj = [[] for _ in range(N)]
    edge_info = []  # (u, v, cap, flow, is_original, orig_idx)
    
    def add_edge_tracked(u, v, cap, is_orig=False, orig_idx=-1):
        idx = len(edge_info)
        edge_info.append([u, v, cap, 0, is_orig, orig_idx])
        edge_info.append([v, u, 0, 0, False, -1])
        adj[u].append(idx)
        adj[v].append(idx + 1)
        return idx
    
    # Add S->s_i edges
    for i, (s, t, d) in enumerate(commodities):
        add_edge_tracked(S, s, d)
    
    # Add t_i->T edges
    for i, (s, t, d) in enumerate(commodities):
        add_edge_tracked(t, T, d)
    
    # Add original edges
    for j, (u, v, cap) in enumerate(edges):
        add_edge_tracked(u, v, cap, True, j)
    
    # Run Dinic again
    level = [0] * N
    ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        level[S] = 0
        q = deque([S])
        while q:
            u = q.popleft()
            for idx in adj[u]:
                e = edge_info[idx]
                if e[2] > e[3] and level[e[1]] < 0:
                    level[e[1]] = level[u] + 1
                    q.append(e[1])
        return level[T] >= 0
    
    def dfs(u, f):
        if u == T:
            return f
        for i in range(ptr[u], len(adj[u])):
            ptr[u] = i
            idx = adj[u][i]
            e = edge_info[idx]
            if e[2] > e[3] and level[e[1]] == level[u] + 1:
                pushed = dfs(e[1], min(f, e[2] - e[3]))
                if pushed > 0:
                    e[3] += pushed
                    edge_info[idx ^ 1][3] -= pushed
                    return pushed
        return 0
    
    flow = 0
    while bfs():
        ptr = [0] * N
        while True:
            pushed = dfs(S, float('inf'))
            if pushed == 0:
                break
            flow += pushed
    
    if flow != total_demand:
        print("NO")
        return
    
    # Now decompose flows for each commodity
    # For each commodity i, we need to find paths from s_i to t_i
    # and track how much goes through each original edge
    
    # Get outgoing flow from S to each s_i
    commodity_flows = []
    for i, (s, t, d) in enumerate(commodities):
        idx = 2 * i  # S->s_i edge
        flow_on_edge = edge_info[idx][3]
        commodity_flows.append(flow_on_edge)
    
    # For each commodity, decompose its flow
    result = [[0] * m for _ in range(k)]
    
    # Build adjacency list for flow decomposition (only original edges with positive flow)
    flow_adj = [[] for _ in range(n)]
    for idx in range(len(edge_info)):
        e = edge_info[idx]
        if e[4] and e[3] > 0:  # is_original and has flow
            u, v, f = e[0], e[1], e[3]
            flow_adj[u].append((v, f, idx, e[5]))  # (to, flow, edge_idx, orig_idx)
    
    # For each commodity, find paths and assign flows
    for i in range(k):
        s, t, d = commodities[i]
        remaining = d
        
        while remaining > 0:
            # BFS to find a path from s to t with positive flow
            parent = [-1] * n
            parent_edge = [-1] * n
            q = deque([s])
            parent[s] = s
            
            while q and parent[t] == -1:
                u = q.popleft()
                for v, f, eidx, oidx in flow_adj[u]:
                    if f > 0 and parent[v] == -1:
                        parent[v] = u
                        parent_edge[v] = (eidx, oidx)
                        q.append(v)
            
            if parent[t] == -1:
                break
            
            # Find minimum flow on path
            path_flow = remaining
            v = t
            while v != s:
                u = parent[v]
                eidx, oidx = parent_edge[v]
                path_flow = min(path_flow, edge_info[eidx][3])
                v = u
            
            # Update flows and result
            v = t
            while v != s:
                u = parent[v]
                eidx, oidx = parent_edge[v]
                edge_info[eidx][3] -= path_flow
                result[i][oidx] += path_flow
                # Update flow_adj
                for j, (nv, nf, neidx, noidx) in enumerate(flow_adj[u]):
                    if neidx == eidx:
                        flow_adj[u][j] = (nv, nf - path_flow, neidx, noidx)
                        break
                v = u
            
            remaining -= path_flow
    
    print("YES")
    for i in range(k):
        print(' '.join(map(str, result[i])))

if __name__ == "__main__":
    solve()