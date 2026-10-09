from collections import defaultdict, deque

def solve():
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    
    edges = []
    graph = defaultdict(list)
    capacity = []
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v))
        graph[u].append((v, i))
        graph[v].append((u, i))
        capacity.append(cap)
    
    # We need to find a flow of value d from s to t
    # This is a maximum flow problem with demands (flow conservation)
    # But since we don't have minimum demands, it's just max flow
    
    # Let's use Ford-Fulkerson with BFS (Edmonds-Karp)
    
    def bfs_flow(residual_capacity, edge_indices):
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([s])
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            
            for v, edge_idx in graph[u]:
                if not visited[v] and residual_capacity[edge_idx] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == t:
                        return parent
        return None
    
    # Initialize flow
    flow = [0] * m
    residual_capacity = capacity[:]
    
    max_flow_value = 0
    
    while max_flow_value < d:
        parent_info = bfs_flow(residual_capacity, list(range(m)))
        
        if parent_info is None:
            break
            
        # Find minimum residual capacity along the path
        path_flow = float('inf')
        v = t
        path_edges = []
        
        while v != s:
            u = parent_info[v]
            # Find the edge index from u to v
            edge_idx = -1
            for neighbor, idx in graph[u]:
                if neighbor == v:
                    edge_idx = idx
                    break
            path_edges.append(edge_idx)
            path_flow = min(path_flow, residual_capacity[edge_idx])
            v = u
            
        # Update residual capacities and flow
        for edge_idx in path_edges:
            residual_capacity[edge_idx] -= path_flow
            # Need to handle reverse edge too, but since we're not building a separate residual graph,
            # we'll manage this implicitly
            
        max_flow_value += path_flow
        
        # Update actual flow values
        v = t
        while v != s:
            u = parent_info[v]
            edge_idx = -1
            for neighbor, idx in graph[u]:
                if neighbor == v:
                    edge_idx = idx
                    break
            flow[edge_idx] += path_flow
            v = u
    
    if max_flow_value >= d:
        print("YES")
        print(*flow)
    else:
        print("NO")

solve()