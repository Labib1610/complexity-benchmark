from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    commodity = int(data[idx])
    idx += 1
    
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    
    edges = []
    capacity = []
    graph = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        cap = int(data[idx])
        idx += 1
        edges.append((u, v))
        capacity.append(cap)
        graph[u].append(i)
        graph[v].append(i)
    
    # We model this as a max flow problem
    # Add a super source and super sink
    # Super source connects to s with capacity d
    # t connects to super sink with capacity d
    # All original edges have their capacities
    
    # But we need to check if we can send exactly d flow from s to t
    # Let's use a circulation approach or just max flow with demands
    
    # Actually, let's build a flow network:
    # Nodes 1 to n, plus a source node 0 and sink node (n+1)
    # Source (node 0) -> s with capacity d
    # t -> sink (node n+1) with capacity d
    # Original edges u->v with capacity cap
    
    # But since we want to find if there exists a feasible flow that satisfies
    # the demand exactly, we can model it as a max-flow problem and check if max flow == d
    
    SOURCE = 0
    SINK = n + 1
    
    # Build adjacency list for residual graph
    adj = defaultdict(list)
    edge_list = []  # Store (to, capacity, reverse_index)
    
    def add_edge(u, v, cap):
        # Forward edge
        adj[u].append(len(edge_list))
        edge_list.append([v, cap, len(adj[v])])
        # Backward edge
        adj[v].append(len(edge_list))
        edge_list.append([u, 0, len(adj[u]) - 1])
    
    # Connect source to s
    add_edge(SOURCE, s, d)
    # Connect t to sink
    add_edge(t, SINK, d)
    
    # Add original edges
    for i in range(m):
        u, v = edges[i]
        cap = capacity[i]
        add_edge(u, v, cap)
    
    # Now run Ford-Fulkerson (Edmonds-Karp) to find max flow
    def bfs():
        parent = [-1] * (n + 2)
        visited = [False] * (n + 2)
        queue = deque([SOURCE])
        visited[SOURCE] = True
        
        while queue:
            u = queue.popleft()
            for i in range(len(adj[u])):
                e_idx = adj[u][i]
                to, cap, _ = edge_list[e_idx]
                if not visited[to] and cap > 0:
                    visited[to] = True
                    parent[to] = (u, e_idx)
                    if to == SINK:
                        return parent
                    queue.append(to)
        return None
    
    max_flow = 0
    while True:
        parent_info = bfs()
        if parent_info is None:
            break
            
        # Find minimum capacity along the path
        path_flow = float('inf')
        curr = SINK
        while curr != SOURCE:
            prev, e_idx = parent_info[curr]
            to, cap, rev_idx = edge_list[e_idx]
            path_flow = min(path_flow, cap)
            curr = prev
            
        # Update capacities
        curr = SINK
        while curr != SOURCE:
            prev, e_idx = parent_info[curr]
            edge_list[e_idx][1] -= path_flow  # Reduce forward edge
            rev_edge_idx = edge_list[e_idx][2]
            edge_list[rev_edge_idx][1] += path_flow  # Increase backward edge
            curr = prev
            
        max_flow += path_flow
        if max_flow == d:
            break
    
    if max_flow != d:
        print("NO")
        return
    
    # Extract flow values for original edges
    result = []
    for i in range(m):
        u, v = edges[i]
        # The corresponding edge in our list is at index 2*(i+2) because:
        # 0: source->s, 1: reverse
        # 2: t->sink, 3: reverse
        # 4..4+2*m-1: original edges and their reverses
        # Original edge i corresponds to indices 4 + 2*i (forward) and 4 + 2*i + 1 (backward)
        forward_edge_idx = 4 + 2 * i
        # Flow on this edge = initial capacity - current capacity
        initial_cap = capacity[i]
        current_cap = edge_list[forward_edge_idx][1]
        flow = initial_cap - current_cap
        result.append(str(flow))
    
    print("YES")
    print(" ".join(result))

solve()