import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    clients = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        clients.append((s, t, d))
    
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Build shortest path distances for each client
    # BFS on unweighted graph (each edge weight 1)
    dist = []
    for c in range(k):
        s, t, d = clients[c]
        dist_c = [-1] * n
        dist_c[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, _ in adj[u]:
                if dist_c[v] == -1:
                    dist_c[v] = dist_c[u] + 1
                    q.append(v)
        dist.append(dist_c)
    
    # Build layered graph for each client
    # Nodes: (junction, layer) where layer = dist from source
    # We need to find max flow of d for each client
    
    # Total nodes: sum over clients of (n * max_layer)
    # But we can process each client separately
    
    # For the global capacity, we use a combined approach:
    # Each edge has capacity limit. We need to assign flow for each client.
    
    # Since we need to output the actual flows, let's do:
    # 1. For each client, find a flow of d from s to t
    # 2. Respect edge capacities
    
    # This is a multi-commodity flow problem, but with the special structure
    # that we can use shortest paths (layered network).
    
    # Actually, the problem is general multi-commodity flow which is hard.
    # But let's try a greedy/iterative approach:
    # For each client, compute max flow in residual graph.
    
    # Let's implement a simple approach: for each client, find augmenting paths
    # using BFS (Edmonds-Karp) on the residual graph.
    
    # Edge capacities are shared. We track remaining capacity.
    remaining = [edges[i][2] for i in range(m)]
    flow = [[0]*m for _ in range(k)]
    
    # Build adjacency for flow network
    # For each edge i: u->v with capacity remaining[i]
    # Reverse edge: v->u with capacity flow (for residual)
    
    # We'll use a standard max flow approach per client.
    # But since flows are separate per client, we need to track per-client flow
    # on each edge for residual purposes.
    
    # Actually, the residual capacity for client c on edge i is:
    # remaining[i] (shared) + flow[c][i] (client's own flow, can be "undone")
    
    # Let's implement BFS to find augmenting path for client c.
    
    def find_path(c):
        s, t, d = clients[c]
        # BFS in residual graph
        # Edge i (u->v): residual = remaining[i] + flow[c][i] (can push forward)
        # Edge i (v->u): residual = flow[c][i] (can push backward, i.e., reduce)
        
        parent = [-1] * n  # parent node
        pedge = [-1] * n    # edge used to reach parent
        visited = [False] * n
        visited[s] = True
        q = deque([s])
        
        while q:
            u = q.popleft()
            if u == t:
                break
            for v, i in adj[u]:
                eu, ev, _ = edges[i]
                # Determine direction
                if eu == u:  # forward edge u->v
                    res = remaining[i] + flow[c][i]
                else:  # backward edge, original is v->u, so this is u<-v, meaning we're at u which is v in original
                    res = flow[c][i]
                
                if res > 0 and not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    pedge[v] = i
                    q.append(v)
        
        if not visited[t]:
            return None
        
        # Reconstruct path and find bottleneck
        path_edges = []
        node = t
        while node != s:
            i = pedge[node]
            path_edges.append((node, i))
            node = parent[node]
        
        # Find bottleneck
        bottleneck = float('inf')
        for node, i in path_edges:
            eu, ev, _ = edges[i]
            u = parent[node]
            if eu == u:  # forward
                res = remaining[i] + flow[c][i]
            else:  # backward
                res = flow[c][i]
            bottleneck = min(bottleneck, res)
        
        return path_edges, bottleneck
    
    success = True
    for c in range(k):
        s, t, d = clients[c]
        sent = 0
        while sent < d:
            result = find_path(c)
            if result is None:
                success = False
                break
            path_edges, bottleneck = result
            push = min(bottleneck, d - sent)
            
            for node, i in path_edges:
                eu, ev, _ = edges[i]
                u = parent_node = None
                # We need parent info... let's restructure
            
            # Let me restructure the path application
            break
        if not success:
            break
    
    # Let me rewrite with a cleaner approach
    # Using standard Edmonds-Karp per client on shared residual graph
    
    remaining = [edges[i][2] for i in range(m)]
    flow = [[0]*m for _ in range(k)]
    
    for c in range(k):
        s, t, d = clients[c]
        sent = 0
        while sent < d:
            # BFS
            parent = [-1] * n
            pedge = [-1] * n
            visited = [False] * n
            visited[s] = True
            q = deque([s])
            
            while q:
                u = q.popleft()
                if u == t:
                    break
                for v, i in adj[u]:
                    eu, ev, _ = edges[i]
                    if eu == u:
                        res = remaining[i] + flow[c][i]
                    else:
                        res = flow[c][i]
                    
                    if res > 0 and not visited[v]:
                        visited[v] = True
                        parent[v] = u
                        pedge[v] = i
                        q.append(v)
            
            if not visited[t]:
                success = False
                break
            
            # Find bottleneck
            bottleneck = float('inf')
            node = t
            while node != s:
                i = pedge[node]
                eu, ev, _ = edges[i]
                u = parent[node]
                if eu == u:
                    res = remaining[i] + flow[c][i]
                else:
                    res = flow[c][i]
                bottleneck = min(bottleneck, res)
                node = parent[node]
            
            push = min(bottleneck, d - sent)
            
            # Apply flow
            node = t
            while node != s:
                i = pedge[node]
                eu, ev, _ = edges[i]
                u = parent[node]
                if eu == u:
                    # Forward edge: reduce remaining, increase flow
                    remaining[i] -= push
                    flow[c][i] += push
                else:
                    # Backward edge: increase remaining, decrease flow
                    remaining[i] += push
                    flow[c][i] -= push
                node = parent[node]
            
            sent += push
        
        if not success:
            break
    
    if success:
        print("YES")
        for c in range(k):
            print(' '.join(map(str, flow[c])))
    else:
        print("NO")

solve()