from collections import defaultdict, deque
import sys

def solve():
    n, m, _ = map(int, input().split())
    s, t, d = map(int, input().split())
    
    edges = []
    edge_info = []
    
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v, cap))
        edge_info.append((u, v, cap, i))
    
    # Build graph for max flow
    # We'll use Ford-Fulkerson with BFS (Edmonds-Karp)
    
    # Create adjacency list
    graph = defaultdict(list)  # node -> list of (neighbor, capacity, edge_index)
    edge_capacity = []
    edge_index_map = {}  # (u,v,idx) -> edge_index_in_graph
    
    for idx, (u, v, cap) in enumerate(edges):
        # Forward edge
        graph[u].append([v, cap, len(edge_capacity)])
        edge_index_map[(u, v, idx)] = len(edge_capacity)
        edge_capacity.append(cap)
        # Backward edge
        graph[v].append([u, 0, len(edge_capacity)])
        edge_capacity.append(0)
    
    def bfs(source, sink, parent_edge):
        visited = set()
        queue = deque([source])
        visited.add(source)
        
        while queue:
            u = queue.popleft()
            
            for v, cap, edge_idx in graph[u]:
                if v not in visited and cap > 0:
                    visited.add(v)
                    parent_edge[v] = edge_idx
                    if v == sink:
                        return True
                    queue.append(v)
        
        return False
    
    def ford_fulkerson(source, sink):
        parent_edge = [-1] * (n + 1)
        max_flow = 0
        
        while bfs(source, sink, parent_edge):
            # Find minimum capacity along the path
            path_flow = float('inf')
            s_idx = sink
            
            # Traverse back to find min capacity
            while s_idx != source:
                edge_idx = parent_edge[s_idx]
                path_flow = min(path_flow, edge_capacity[edge_idx])
                # Find the predecessor
                for u, neighbors in graph.items():
                    for v, cap, idx in neighbors:
                        if idx == edge_idx and v == s_idx:
                            s_idx = u
                            break
                    else:
                        continue
                    break
            
            # Update capacities
            v_idx = sink
            while v_idx != source:
                edge_idx = parent_edge[v_idx]
                edge_capacity[edge_idx] -= path_flow
                # Backward edge
                edge_capacity[edge_idx ^ 1] += path_flow
                
                # Find predecessor
                for u, neighbors in graph.items():
                    for v, cap, idx in neighbors:
                        if idx == edge_idx and v == v_idx:
                            v_idx = u
                            break
                    else:
                        continue
                    break
            
            max_flow += path_flow
        
        return max_flow
    
    # Check if we can achieve flow d from s to t
    max_flow = ford_fulkerson(s, t)
    
    if max_flow < d:
        print("NO")
        return
    
    # Now we need to find a feasible flow of exactly d
    # We'll use the fact that we can decompose the flow into paths
    
    # Reset and find exact flow of d
    # Rebuild graph
    graph = defaultdict(list)
    edge_capacity = []
    final_flow = [0] * m
    
    for idx, (u, v, cap) in enumerate(edges):
        graph[u].append([v, cap, len(edge_capacity)])
        edge_index_map[(u, v, idx)] = len(edge_capacity)
        edge_capacity.append(cap)
        graph[v].append([u, 0, len(edge_capacity)])
        edge_capacity.append(0)
    
    # Push exactly d flow
    def push_flow(source, sink, target_flow):
        # Use DFS to find paths and push flow
        def dfs(u, sink, flow, visited):
            if u == sink:
                return flow
            
            visited.add(u)
            
            for i, (v, cap, edge_idx) in enumerate(graph[u]):
                if v not in visited and cap > 0:
                    min_flow = min(flow, cap)
                    bottleneck = dfs(v, sink, min_flow, visited)
                    
                    if bottleneck > 0:
                        edge_capacity[edge_idx] -= bottleneck
                        edge_capacity[edge_idx ^ 1] += bottleneck
                        return bottleneck
            
            return 0
        
        total_pushed = 0
        while total_pushed < target_flow:
            visited = set()
            pushed = dfs(source, sink, target_flow - total_pushed, visited)
            if pushed == 0:
                break
            total_pushed += pushed
        
        return total_pushed
    
    pushed = push_flow(s, t, d)
    
    if pushed < d:
        print("NO")
        return
    
    # Now extract the flow on each edge
    result = [0] * m
    
    # For each original edge, check the flow
    for idx, (u, v, cap, orig_idx) in enumerate(edge_info):
        forward_edge_idx = edge_index_map[(u, v, orig_idx)]
        backward_edge_idx = forward_edge_idx ^ 1
        
        # Original capacity - current capacity = flow
        flow = cap - edge_capacity[forward_edge_idx]
        result[orig_idx] = flow
    
    print("YES")
    print(*result)

solve()