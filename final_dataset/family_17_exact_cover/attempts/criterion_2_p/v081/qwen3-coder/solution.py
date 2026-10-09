from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # If t < q, impossible to match all modules
    if t < q:
        print("NO")
        return
    
    # Build bipartite graph
    # Left side: originators 1 to q
    # Right side: endpoints q+1 to 2q
    graph = defaultdict(list)
    edges = []
    
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
        edges.append((a, b))
    
    # Try to find a maximum matching using Ford-Fulkerson with BFS (Edmonds-Karp)
    # Create a flow network
    # Source connects to all originators (1 to q)
    # All endpoints (q+1 to 2q) connect to sink
    # All edges have capacity 1
    
    def bfs_find_path(graph_residual, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)
        
        while queue:
            u = queue.popleft()
            
            for v in graph_residual[u]:
                if v not in visited and graph_residual[u][v] > 0:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return True
        return False
    
    # Create residual graph
    # Nodes: 0 (source), 1..q (originators), (q+1)..2q (endpoints), 2*q+1 (sink)
    residual_graph = defaultdict(lambda: defaultdict(int))
    
    # Connect source to originators
    for i in range(1, q+1):
        residual_graph[0][i] = 1
    
    # Connect endpoints to sink
    for i in range(q+1, 2*q+1):
        residual_graph[i][2*q+1] = 1
    
    # Add edges from input
    for a, b in edges:
        residual_graph[a][b] = 1
    
    # Max flow algorithm
    parent = {}
    max_flow = 0
    
    while bfs_find_path(residual_graph, 0, 2*q+1, parent):
        path_flow = float('inf')
        s = 2*q+1
        
        # Find minimum capacity along the path
        while s != 0:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
        
        # Update residual capacities
        v = 2*q+1
        while v != 0:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    if max_flow < q:
        print("NO")
        return
    
    # Reconstruct matching
    result = []
    for a, b in edges:
        # In residual graph, if there's flow from a to b,
        # it means b to a has residual capacity (reverse edge strengthened)
        if residual_graph[b][a] > 0:
            result.append((a, b))
    
    print("YES")
    for a, b in result:
        print(a, b)

solve()