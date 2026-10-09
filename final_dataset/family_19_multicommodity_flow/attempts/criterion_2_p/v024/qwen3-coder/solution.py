from collections import deque

def max_flow(n, edges, s, t):
    # Create adjacency list and capacity matrix
    adj = [[] for _ in range(n)]
    capacity = [[0] * n for _ in range(n)]
    
    for i, (u, v, cap) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))  # Add reverse edge
        capacity[u][v] += cap  # Handle multiple edges between same nodes
    
    # Ford-Fulkerson with BFS (Edmonds-Karp)
    def bfs():
        parent = [-1] * n
        visited = [False] * n
        queue = deque([s])
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            
            for v, _ in adj[u]:
                if not visited[v] and capacity[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    
                    if v == t:
                        # Reconstruct path and find bottleneck
                        path_flow = float('inf')
                        curr = t
                        while curr != s:
                            prev = parent[curr]
                            path_flow = min(path_flow, capacity[prev][curr])
                            curr = prev
                        return path_flow, parent
        return 0, None
    
    max_flow_value = 0
    while True:
        flow, parent = bfs()
        if flow == 0:
            break
            
        max_flow_value += flow
        
        # Update residual capacities
        curr = t
        while curr != s:
            prev = parent[curr]
            capacity[prev][curr] -= flow
            capacity[curr][prev] += flow
            curr = prev
    
    return max_flow_value

def solve():
    # Read input
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    s -= 1  # Convert to 0-indexed
    t -= 1
    edges = []
    for _ in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u-1, v-1, cap))  # Convert to 0-indexed
    
    # Check if max flow is at least d
    flow_value = max_flow(n, edges, s, t)
    
    if flow_value < d:
        print("NO")
        return
    
    # Now we need to find a flow of exactly d
    # We'll do this by finding the max flow again but with modified capacities
    # First, let's build the residual graph after finding max flow >= d
    
    # Rebuild capacity matrix
    capacity = [[0] * n for _ in range(n)]
    for u, v, cap in edges:
        capacity[u][v] += cap
    
    # Find flow of exactly d using scaling or binary search approach
    # But simpler: run max flow algorithm and then scale down if needed
    # Actually, let's just run max flow and see if we can get exactly d
    
    # Let's rebuild and find exact flow of d
    # Create a new graph with super source and super sink
    # Super source is n, super sink is n+1
    # Connect super source to s with capacity d
    # Connect t to super sink with capacity d
    
    new_n = n + 2
    new_edges = edges[:]
    new_s = n  # Super source
    new_t = n + 1  # Super sink
    new_edges.append((new_s, s, d))  # Connect super source to original source
    new_edges.append((t, new_t, d))  # Connect original sink to super sink
    
    # Run max flow on this new graph
    adj = [[] for _ in range(new_n)]
    cap = [[0] * new_n for _ in range(new_n)]
    
    for i, (u, v, c) in enumerate(new_edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
        cap[u][v] += c
    
    # Edmonds-Karp
    def bfs():
        parent = [-1] * new_n
        visited = [False] * new_n
        queue = deque([new_s])
        visited[new_s] = True
        
        while queue:
            u = queue.popleft()
            for v, _ in adj[u]:
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == new_t:
                        path_flow = float('inf')
                        curr = new_t
                        while curr != new_s:
                            prev = parent[curr]
                            path_flow = min(path_flow, cap[prev][curr])
                            curr = prev
                        return path_flow, parent
        return 0, None
    
    total_flow = 0
    while True:
        flow, parent = bfs()
        if flow == 0:
            break
        total_flow += flow
        curr = new_t
        while curr != new_s:
            prev = parent[curr]
            cap[prev][curr] -= flow
            cap[curr][prev] += flow
            curr = prev
    
    if total_flow < d:
        print("NO")
        return
    
    # Extract flows on original edges
    flows = []
    for u, v, original_cap in edges:
        # Flow is original capacity minus residual capacity
        flow = original_cap - cap[u][v]
        flows.append(flow)
    
    print("YES")
    print(*flows)

solve()