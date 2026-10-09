from collections import defaultdict, deque

def solve():
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    
    # Build graph
    graph = defaultdict(list)
    edges = []
    edge_indices = {}
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v, cap))
        edge_indices[(u, v)] = i
        graph[u].append((v, cap, i))
        graph[v].append((u, 0, i))  # reverse edge with capacity 0 for residual graph
    
    # Ford-Fulkerson with BFS (Edmonds-Karp)
    def bfs():
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([s])
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            
            for v, cap, edge_idx in graph[u]:
                if not visited[v] and cap > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    
                    if v == t:
                        return parent
        return None
    
    # Find maximum flow
    flow = [0] * m
    
    while True:
        parent = bfs()
        if parent is None:
            break
            
        # Find minimum capacity along the path
        path_flow = float('inf')
        current = t
        path_edges = []
        
        while current != s:
            prev = parent[current]
            # Find the edge from prev to current
            found_edge = None
            for v, cap, idx in graph[prev]:
                if v == current:
                    found_edge = (cap, idx)
                    break
            if found_edge is None:
                break
            cap, idx = found_edge
            path_flow = min(path_flow, cap)
            path_edges.append((prev, current, idx))
            current = prev
        
        if path_flow == float('inf'):
            break
            
        # Update flow and residual capacities
        for u, v, idx in path_edges:
            flow[idx] += path_flow
            # Update forward edge
            for i in range(len(graph[u])):
                if graph[u][i][0] == v and graph[u][i][2] == idx:
                    graph[u][i] = (graph[u][i][0], graph[u][i][1] - path_flow, graph[u][i][2])
                    break
            # Update backward edge
            for i in range(len(graph[v])):
                if graph[v][i][0] == u and graph[v][i][2] == idx:
                    graph[v][i] = (graph[v][i][0], graph[v][i][1] + path_flow, graph[v][i][2])
                    break
    
    # Check if we can send the required flow
    total_flow = 0
    current = t
    visited_source = [False] * (n + 1)
    queue = deque([s])
    visited_source[s] = True
    
    while queue:
        u = queue.popleft()
        if u == t:
            # Count how much flow reaches t
            for v, cap, idx in graph[s]:
                if v == t:
                    total_flow += flow[idx]
                elif cap < edges[idx][2]:  # There's flow on this edge
                    total_flow += (edges[idx][2] - cap)
            break
            
        for v, cap, idx in graph[u]:
            if cap < edges[idx][2] and not visited_source[v]:  # There's flow on this edge
                visited_source[v] = True
                queue.append(v)
    
    # Simpler check: compute actual max flow
    max_flow_value = 0
    for v, cap, idx in graph[s]:
        max_flow_value += (edges[idx][2] - cap) if cap < edges[idx][2] else 0
    
    # Actually let's recompute properly
    # The flow into t should equal the flow out of s
    flow_into_t = 0
    for u in range(1, n+1):
        for v, cap, idx in graph[u]:
            if v == t:
                flow_into_t += (edges[idx][2] - cap)
    
    if flow_into_t < d:
        print("NO")
        return
    
    # Reconstruct the actual flows
    result = [0] * m
    for i in range(m):
        u, v, _ = edges[i]
        # Flow on edge (u,v) is original capacity minus current capacity
        for edge_v, edge_cap, edge_idx in graph[u]:
            if edge_v == v and edge_idx == i:
                result[i] = edges[i][2] - edge_cap
                break
    
    print("YES")
    print(*result)

solve()