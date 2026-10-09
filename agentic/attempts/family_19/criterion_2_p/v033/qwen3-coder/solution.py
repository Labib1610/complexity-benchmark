from collections import deque, defaultdict

def solve():
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
    
    edges = []
    edge_index = {}
    capacity = []
    graph = defaultdict(list)
    rev_graph = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v))
        edge_index[(u, v, i)] = i
        capacity.append(cap)
        graph[u].append((v, i))
        rev_graph[v].append((u, i))
        
    # We need to find a feasible flow of value d from s to t
    # This is a circulation problem with demands
    
    # Create residual graph
    # We will use Ford-Fulkerson with BFS (Edmonds-Karp) to find max flow
    # But we need exactly d flow
    
    # First check if max flow >= d
    # If yes, then we can find a feasible solution
    
    # Build adjacency list for residual graph
    adj = [[] for _ in range(n+1)]
    edge_list = []  # stores (u, v, cap, flow, index_in_original)
    
    for i in range(m):
        u, v = edges[i]
        cap = capacity[i]
        # forward edge
        edge_list.append((u, v, cap, 0, i))
        adj[u].append(len(edge_list)-1)
        # backward edge
        edge_list.append((v, u, 0, 0, i))
        adj[v].append(len(edge_list)-1)
    
    def bfs(source, sink):
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        q = deque([source])
        visited[source] = True
        
        while q:
            u = q.popleft()
            for edge_idx in adj[u]:
                _, v, cap, flow, _ = edge_list[edge_idx]
                if not visited[v] and cap > flow:
                    visited[v] = True
                    parent[v] = edge_idx
                    q.append(v)
                    if v == sink:
                        return parent
        return None
    
    max_flow = 0
    while max_flow < d:
        parent = bfs(s, t)
        if parent is None:
            break
            
        # Find minimum residual capacity along the path
        path_flow = float('inf')
        s_ptr = t
        while s_ptr != s:
            edge_idx = parent[s_ptr]
            _, _, cap, flow, _ = edge_list[edge_idx]
            path_flow = min(path_flow, cap - flow)
            u_idx = edge_idx ^ 1  # XOR to get reverse edge
            _, u, _, _, _ = edge_list[u_idx]
            s_ptr = u
            
        if path_flow == 0:
            break
            
        # Actually we should send min(d - max_flow, path_flow)
        send_flow = min(d - max_flow, path_flow)
            
        # Update residual capacities
        s_ptr = t
        while s_ptr != s:
            edge_idx = parent[s_ptr]
            edge_list[edge_idx] = (edge_list[edge_idx][0], edge_list[edge_idx][1], 
                                  edge_list[edge_idx][2], edge_list[edge_idx][3] + send_flow,
                                  edge_list[edge_idx][4])
            u_idx = edge_idx ^ 1  # XOR to get reverse edge
            _, u, cap, flow, orig_idx = edge_list[u_idx]
            edge_list[u_idx] = (u, s_ptr, cap, flow - send_flow, orig_idx)
            _, u_prev, _, _, _ = edge_list[u_idx]
            s_ptr = u_prev
            
        max_flow += send_flow
    
    if max_flow < d:
        print("NO")
        return
    
    # Extract flows
    result = [0] * m
    for i in range(0, len(edge_list), 2):
        _, _, _, flow, orig_idx = edge_list[i]
        result[orig_idx] = flow
    
    print("YES")
    print(' '.join(map(str, result)))

solve()