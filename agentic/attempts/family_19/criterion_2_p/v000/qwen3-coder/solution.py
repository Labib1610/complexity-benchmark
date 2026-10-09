from collections import defaultdict, deque
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    _ = int(data[idx]); idx += 1
    s = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    
    # Build graph
    graph = defaultdict(list)
    capacity = {}
    edges = []
    
    for i in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v, cap))
        graph[u].append((v, i))
        graph[v].append((u, i))  # For residual graph
        capacity[i] = cap
    
    # We need to solve a max flow problem with exactly 'd' flow
    # Add edge from t to s with capacity d to make it a circulation
    super_source = 0
    super_sink = n + 1
    
    # Connect super_source to s with capacity d
    graph[super_source].append((s, m))
    graph[s].append((super_source, m))
    capacity[m] = d
    
    # Connect t to super_sink with capacity d
    graph[t].append((super_sink, m+1))
    graph[super_sink].append((t, m+1))
    capacity[m+1] = d
    
    # Add reverse edge indices
    rev_edge = [m+2+i for i in range(m+2)] + [i for i in range(m+2)]
    
    # Total edges now: original m + 2 new ones
    total_edges = m + 2
    
    def bfs():
        parent = [-1] * (n + 2)
        parent_edge = [-1] * (n + 2)
        visited = [False] * (n + 2)
        queue = deque()
        queue.append(super_source)
        visited[super_source] = True
        
        while queue:
            u = queue.popleft()
            for v, edge_idx in graph[u]:
                if not visited[v] and capacity[edge_idx] > 0:
                    visited[v] = True
                    parent[v] = u
                    parent_edge[v] = edge_idx
                    queue.append(v)
                    if v == super_sink:
                        return parent, parent_edge
        return None, None
    
    # Ford-Fulkerson with BFS (Edmonds-Karp)
    flow = [0] * total_edges
    
    while True:
        parent, parent_edge = bfs()
        if parent is None:
            break
            
        # Find minimum capacity along the path
        path_flow = float('inf')
        s_node = super_sink
        while s_node != super_source:
            edge_idx = parent_edge[s_node]
            path_flow = min(path_flow, capacity[edge_idx])
            s_node = parent[s_node]
        
        # Update capacities and flows
        s_node = super_sink
        while s_node != super_source:
            edge_idx = parent_edge[s_node]
            capacity[edge_idx] -= path_flow
            capacity[rev_edge[edge_idx]] += path_flow
            if edge_idx < m:
                if edge_idx < len(flow):
                    flow[edge_idx] += path_flow
                else:
                    flow.append(path_flow)
            elif rev_edge[edge_idx] < m:
                flow[rev_edge[edge_idx]] -= path_flow
            s_node = parent[s_node]
    
    # Check if we have sent exactly 'd' units from s to t
    # The flow on edge m (s to super_source) should be d
    if capacity[m] != 0:
        print("NO")
        return
    
    # Extract the flow on original edges
    result_flow = flow[:m]
    
    # Verify conservation at each node except s and t
    in_flow = [0] * (n+1)
    out_flow = [0] * (n+1)
    
    for i in range(m):
        u, v, _ = edges[i]
        out_flow[u] += result_flow[i]
        in_flow[v] += result_flow[i]
    
    # Check conservation
    valid = True
    for i in range(1, n+1):
        if i != s and i != t:
            if in_flow[i] != out_flow[i]:
                valid = False
                break
        elif i == s:
            if out_flow[i] - in_flow[i] != d:
                valid = False
                break
        elif i == t:
            if in_flow[i] - out_flow[i] != d:
                valid = False
                break
    
    if not valid:
        print("NO")
        return
    
    # Check if all flows are within capacity
    for i in range(m):
        _, _, cap = edges[i]
        if result_flow[i] < 0 or result_flow[i] > cap:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, result_flow)))

if __name__ == "__main__":
    main()