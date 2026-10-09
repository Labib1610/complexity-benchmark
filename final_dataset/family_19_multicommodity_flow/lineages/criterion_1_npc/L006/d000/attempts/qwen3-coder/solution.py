from collections import defaultdict, deque
import sys

def solve():
    n, m, k = map(int, input().split())
    
    groups = []
    for i in range(k):
        s, t, d = map(int, input().split())
        groups.append((s-1, t-1, d))  # Convert to 0-indexed
    
    edges = []
    edge_dict = {}
    capacity = []
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
        edge_dict[(u-1, v-1)] = i
        capacity.append(cap)
    
    # Build graph for flow
    graph = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        graph[u].append((v, idx))
        graph[v].append((u, idx))  # Add reverse edge for residual graph
    
    def bfs(source, sink, res_graph, edge_flow):
        parent = [-1] * len(res_graph)
        visited = [False] * len(res_graph)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v, edge_idx in res_graph[u]:
                if not visited[v] and edge_flow[edge_idx] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return parent
        return None
    
    def find_flow(source, sink, res_graph, edge_flow):
        parent = bfs(source, sink, res_graph, edge_flow)
        if parent is None:
            return 0, []
        
        # Find minimum flow along the path
        path_flow = float('inf')
        s = sink
        path = []
        while s != source:
            p = parent[s]
            # Find the edge from p to s
            edge_idx = None
            for v, idx in res_graph[p]:
                if v == s:
                    edge_idx = idx
                    break
            path_flow = min(path_flow, edge_flow[edge_idx])
            path.append(edge_idx)
            s = p
        
        return path_flow, path
    
    # For each group, compute a flow
    group_flows = []
    
    for source, sink, demand in groups:
        # Create residual graph with edge capacities
        res_graph = [[] for _ in range(n)]
        edge_flow = capacity[:]  # Copy of capacities
        
        # Add forward edges
        for idx, (u, v) in enumerate(edges):
            res_graph[u].append((v, idx))
            res_graph[v].append((u, idx))  # Reverse edge for residual
        
        # Find max flow for this group
        flow_paths = []
        total_flow = 0
        
        # We'll track the flow for this group on each edge
        group_edge_flow = [0] * m
        
        while total_flow < demand:
            path_flow, path = find_flow(source, sink, res_graph, edge_flow)
            if path_flow == 0:
                break
            
            actual_flow = min(path_flow, demand - total_flow)
            total_flow += actual_flow
            
            # Update residual capacities and track group flow
            for edge_idx in path:
                edge_flow[edge_idx] -= actual_flow
                group_edge_flow[edge_idx] += actual_flow
        
        if total_flow < demand:
            print("NO")
            return
            
        group_flows.append(group_edge_flow)
    
    # Check if combined flow satisfies capacity constraints
    total_usage = [0] * m
    for g_flow in group_flows:
        for i in range(m):
            total_usage[i] += g_flow[i]
    
    for i in range(m):
        if total_usage[i] > capacity[i]:
            print("NO")
            return
    
    print("YES")
    for g_flow in group_flows:
        print(' '.join(map(str, g_flow)))

solve()