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
    num_products = int(data[idx])
    idx += 1
    
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    
    edges = []
    edge_info = []
    graph = defaultdict(list)
    in_graph = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        c = int(data[idx])
        idx += 1
        edges.append((u, v, c))
        edge_info.append([u, v, c, i])
        graph[u].append((v, c, i))
        in_graph[v].append((u, c, i))
    
    # Build a flow network: add source and sink
    # Source is n+1, sink is n+2
    SOURCE = n + 1
    SINK = n + 2
    
    # Create a new graph for max flow with capacity and reverse edges
    adj = defaultdict(list)
    edge_list = []
    
    # Add original edges
    for u, v, c, i in edge_info:
        # Forward edge with capacity c
        edge_list.append({'from': u, 'to': v, 'cap': c, 'rev': len(adj[v])})
        adj[u].append(len(edge_list) - 1)
        # Backward edge with capacity 0
        edge_list.append({'from': v, 'to': u, 'cap': 0, 'rev': len(adj[u]) - 1})
        adj[v].append(len(edge_list) - 1)
    
    # Add demand constraints
    # For each node except s and t, flow conservation must hold
    # For s: outflow - inflow = d
    # For t: inflow - outflow = d
    # For other nodes: inflow = outflow
    
    # To model this, we'll add edges from SOURCE and to SINK
    demand = {}
    for i in range(1, n+1):
        demand[i] = 0
    demand[s] = -d  # s should have net outflow d
    demand[t] = d   # t should have net inflow d
    
    # For each node, if demand[i] > 0, add edge from SOURCE to i with capacity demand[i]
    # if demand[i] < 0, add edge from i to SINK with capacity -demand[i]
    for i in range(1, n+1):
        if demand[i] > 0:
            # SOURCE -> i with capacity demand[i]
            edge_list.append({'from': SOURCE, 'to': i, 'cap': demand[i], 'rev': len(adj[i])})
            adj[SOURCE].append(len(edge_list) - 1)
            edge_list.append({'from': i, 'to': SOURCE, 'cap': 0, 'rev': len(adj[SOURCE]) - 1})
            adj[i].append(len(edge_list) - 1)
        elif demand[i] < 0:
            # i -> SINK with capacity -demand[i]
            edge_list.append({'from': i, 'to': SINK, 'cap': -demand[i], 'rev': len(adj[SINK])})
            adj[i].append(len(edge_list) - 1)
            edge_list.append({'from': SINK, 'to': i, 'cap': 0, 'rev': len(adj[i]) - 1})
            adj[SINK].append(len(edge_list) - 1)
    
    # Now run max flow from SOURCE to SINK
    def bfs():
        level = [-1] * (n + 3)
        level[SOURCE] = 0
        queue = deque([SOURCE])
        while queue:
            u = queue.popleft()
            for eid in adj[u]:
                e = edge_list[eid]
                if level[e['to']] == -1 and e['cap'] > 0:
                    level[e['to']] = level[u] + 1
                    queue.append(e['to'])
        return level[SINK] != -1, level
    
    def dfs(u, sink, flow, level, start):
        if u == sink:
            return flow
        while start[u] < len(adj[u]):
            eid = adj[u][start[u]]
            e = edge_list[eid]
            if level[e['to']] == level[u] + 1 and e['cap'] > 0:
                cur_flow = min(flow, e['cap'])
                bottleneck = dfs(e['to'], sink, cur_flow, level, start)
                if bottleneck > 0:
                    edge_list[eid]['cap'] -= bottleneck
                    edge_list[e['rev']]['cap'] += bottleneck
                    return bottleneck
            start[u] += 1
        return 0
    
    def dinic():
        max_flow = 0
        while True:
            has_path, level = bfs()
            if not has_path:
                break
            start = [0] * (n + 3)
            while True:
                flow = dfs(SOURCE, SINK, float('inf'), level, start)
                if flow == 0:
                    break
                max_flow += flow
        return max_flow
    
    total_demand = sum(val for val in demand.values() if val > 0)
    max_flow = dinic()
    
    if max_flow < total_demand:
        print("NO")
        return
    
    # Extract the flow on original edges
    result = [0] * m
    for u, v, c, i in edge_info:
        # The flow on this edge is the original capacity minus the residual capacity
        # The forward edge is at index 2*i, backward is at 2*i + 1
        # But we need to find the correct edge in edge_list
        # Let's re-index
        pass
    
    # Let's restructure to correctly extract flows
    # We'll rebuild edge mapping
    edge_mapping = {}
    for i, (u, v, c) in enumerate(edges):
        edge_mapping[(u, v, i)] = i
    
    flow_result = [0] * m
    for u, v, c, i in edge_info:
        # Original forward edge index is 2*i
        # But in our edge_list, we need to find the right one
        # Let's iterate through adj[u] to find the edge to v with original index i
        for eid in adj[u]:
            e = edge_list[eid]
            if e['to'] == v:
                # This is the forward edge for the original edge i
                # The flow is the original capacity minus current capacity
                original_cap = c
                current_cap = e['cap']
                flow = original_cap - current_cap
                flow_result[i] = flow
                break
    
    print("YES")
    print(' '.join(map(str, flow_result)))

solve()