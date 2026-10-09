from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    product_type = int(data[index])
    index += 1
    
    s = int(data[index])
    index += 1
    t = int(data[index])
    index += 1
    d = int(data[index])
    index += 1
    
    edges = []
    graph = defaultdict(list)
    capacity = {}
    
    for i in range(m):
        u = int(data[index])
        index += 1
        v = int(data[index])
        index += 1
        c = int(data[index])
        index += 1
        edges.append((u, v, c))
        graph[u].append((v, i))
        graph[v].append((u, i))
        capacity[i] = c
    
    # Create residual graph
    res_graph = [{} for _ in range(n+1)]
    edge_index_map = {}
    
    for i in range(m):
        u, v, c = edges[i]
        if v not in res_graph[u]:
            res_graph[u][v] = 0
        if u not in res_graph[v]:
            res_graph[v][u] = 0
        edge_index_map[(u, v, i)] = len(res_graph[u]) - 1 if v in res_graph[u] else len(res_graph[u])
        res_graph[u][v] += c
    
    # Ford-Fulkerson with BFS (Edmonds-Karp)
    def bfs(source, sink):
        parent = [-1] * (n + 1)
        parent_edge = [-1] * (n + 1)
        queue = deque([source])
        parent[source] = source
        min_capacity = [0] * (n + 1)
        min_capacity[source] = float('inf')
        
        while queue:
            current = queue.popleft()
            for neighbor in res_graph[current]:
                if parent[neighbor] == -1 and res_graph[current][neighbor] > 0:
                    parent[neighbor] = current
                    min_capacity[neighbor] = min(min_capacity[current], res_graph[current][neighbor])
                    queue.append(neighbor)
                    if neighbor == sink:
                        return min_capacity[neighbor], parent
        return 0, parent
    
    max_flow = 0
    flow_on_edges = [0] * m
    
    while True:
        flow, parent_list = bfs(s, t)
        if flow == 0:
            break
        max_flow += flow
        
        # Update residual capacities and track flow on edges
        cur = t
        while cur != s:
            prev = parent_list[cur]
            res_graph[prev][cur] -= flow
            res_graph[cur][prev] += flow
            
            # Find the original edge and update flow
            for i in range(m):
                u, v, c = edges[i]
                if u == prev and v == cur:
                    flow_on_edges[i] += flow
                    break
            cur = prev
            
        if max_flow >= d:
            break
    
    if max_flow < d:
        print("NO")
        return
    
    # Adjust flows to exactly match demand d
    if max_flow > d:
        # Need to reduce flow by (max_flow - d)
        excess = max_flow - d
        # Create reverse flow network for reduction
        rev_res_graph = [{} for _ in range(n+1)]
        # Build reverse graph with current flows
        for i in range(m):
            u, v, c = edges[i]
            if v not in rev_res_graph[u]:
                rev_res_graph[u][v] = 0
            if u not in rev_res_graph[v]:
                rev_res_graph[v][u] = 0
            rev_res_graph[u][v] += flow_on_edges[i]
        
        # Push back excess flow
        def push_back_flow(source, sink, amount):
            # BFS to find path from sink to source in residual graph
            parent = [-1] * (n + 1)
            queue = deque([sink])
            parent[sink] = sink
            min_cap = [0] * (n + 1)
            min_cap[sink] = amount
            
            while queue:
                current = queue.popleft()
                if current == source:
                    break
                for neighbor in rev_res_graph[current]:
                    if parent[neighbor] == -1 and rev_res_graph[current][neighbor] > 0:
                        parent[neighbor] = current
                        min_cap[neighbor] = min(min_cap[current], rev_res_graph[current][neighbor])
                        queue.append(neighbor)
                        if neighbor == source:
                            break
            
            if parent[source] != -1:
                # Found path, push flow back
                cur = source
                actual_flow = min_cap[source]
                path = []
                while cur != sink:
                    next_node = parent[cur]
                    path.append((cur, next_node))
                    cur = next_node
                
                for u, v in path:
                    rev_res_graph[u][v] -= actual_flow
                    rev_res_graph[v][u] += actual_flow
                return actual_flow
            return 0
        
        reduced = 0
        while reduced < excess:
            reduced_now = push_back_flow(t, s, excess - reduced)
            if reduced_now == 0:
                break
            reduced += reduced_now
        
        # Recalculate final flows
        for i in range(m):
            u, v, c = edges[i]
            flow_on_edges[i] = rev_res_graph[v][u] if u in rev_res_graph[v] else 0
    
    print("YES")
    print(' '.join(map(str, flow_on_edges)))

solve()