from collections import defaultdict, deque
import sys

def solve():
    n, m, k = map(int, input().split())
    
    # Store classifications
    classifications = []
    for i in range(k):
        s, t, d = map(int, input().split())
        classifications.append((s, t, d))
    
    # Store edges
    edges = []
    edge_index = {}
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v, cap))
        edge_index[(u, v)] = i
        graph[u].append((v, i))
        graph[v].append((u, i))  # For residual graph
    
    # For each classification, find flow
    result = [[0] * m for _ in range(k)]
    total_usage = [0] * m
    
    # Build a combined graph for all flows
    # We need to solve k separate max-flow problems
    def bfs(capacity, source, sink):
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v, idx in graph[u]:
                if not visited[v] and capacity[idx] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return parent
        return None
    
    def find_path(parent, sink):
        path = []
        current = sink
        while parent[current] != -1:
            prev = parent[current]
            path.append((prev, current))
            current = prev
        path.reverse()
        return path
    
    # Try to route each classification
    for i, (s, t, d) in enumerate(classifications):
        # Create a local capacity array for this flow
        local_capacity = [edges[j][2] - total_usage[j] for j in range(m)]
        
        # Run max flow to see if we can send 'd' units from s to t
        # We'll use Ford-Fulkerson
        flow_sent = 0
        local_flow = [0] * m
        
        while flow_sent < d:
            parent = bfs(local_capacity, s, t)
            if parent is None:
                print("NO")
                return
            
            # Find the minimum capacity along the path
            path = find_path(parent, t)
            min_cap = float('inf')
            for u, v in path:
                idx = edge_index[(u, v)]
                if local_capacity[idx] < min_cap:
                    min_cap = local_capacity[idx]
            
            # Update flow and capacities
            actual_flow = min(min_cap, d - flow_sent)
            flow_sent += actual_flow
            
            for u, v in path:
                idx = edge_index[(u, v)]
                local_flow[idx] += actual_flow
                local_capacity[idx] -= actual_flow
        
        # Update global usage and result
        for j in range(m):
            total_usage[j] += local_flow[j]
            result[i][j] = local_flow[j]
    
    print("YES")
    for row in result:
        print(' '.join(map(str, row)))

solve()