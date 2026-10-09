import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    contracts = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        contracts.append((s, t, d))
    
    edges = []
    adj = [[] for _ in range(n)]
    for j in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))
        adj[u].append((v, j))
    
    # Build flow network
    # Nodes: 0..n-1 are original terminals
    # Node n is super source, node n+1 is super sink
    total_nodes = n + 2
    super_source = n
    super_sink = n + 1
    
    # Edge structure: (to, capacity, flow, rev_index)
    graph = [[] for _ in range(total_nodes)]
    edge_info = []  # (from, to, capacity, edge_idx_in_graph[from])
    
    def add_edge(u, v, cap):
        graph[u].append([v, cap, 0, len(graph[v])])
        graph[v].append([u, 0, 0, len(graph[u]) - 1])
        return len(graph[u]) - 1
    
    # Add edges from super source to each contract origin
    for i, (s, t, d) in enumerate(contracts):
        add_edge(super_source, s, d)
    
    # Add rail segments with shared capacity
    for j, (u, v, c) in enumerate(edges):
        edge_info.append((u, v, c, add_edge(u, v, c)))
    
    # Add edges from each contract destination to super sink
    for i, (s, t, d) in enumerate(contracts):
        add_edge(t, super_sink, d)
    
    # Dinic's algorithm
    level = [0] * total_nodes
    ptr = [0] * total_nodes
    
    def bfs():
        for i in range(total_nodes):
            level[i] = -1
        level[super_source] = 0
        q = deque([super_source])
        while q:
            u = q.popleft()
            for edge in graph[u]:
                v, cap, flow, _ = edge
                if cap - flow > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[super_sink] != -1
    
    def dfs(u, pushed):
        if pushed == 0 or u == super_sink:
            return pushed
        for i in range(ptr[u], len(graph[u])):
            ptr[u] = i
            edge = graph[u][i]
            v, cap, flow, rev = edge
            if level[v] != level[u] + 1 or cap - flow == 0:
                continue
            tr = dfs(v, min(pushed, cap - flow))
            if tr == 0:
                continue
            edge[2] += tr
            graph[v][rev][2] -= tr
            return tr
        return 0
    
    total_flow = 0
    while bfs():
        ptr = [0] * total_nodes
        while True:
            pushed = dfs(super_source, float('inf'))
            if pushed == 0:
                break
            total_flow += pushed
    
    total_demand = sum(d for _, _, d in contracts)
    if total_flow != total_demand:
        print("NO")
        return
    
    print("YES")
    
    # For each contract, find flow on each edge
    # We need to decompose flow by contract
    # Use the approach: for each contract, find paths and subtract flow
    
    # Get current flow on each edge
    edge_flows = []
    for j, (u, v, c, idx) in enumerate(edge_info):
        edge_flows.append(graph[u][idx][2])
    
    # For each contract, compute flow on each edge
    result = [[0] * m for _ in range(k)]
    
    for contract_idx in range(k):
        s, t, d = contracts[contract_idx]
        remaining = d
        
        # Build residual graph for this contract
        # We can use flow that's already assigned
        # Use BFS/DFS to find paths from s to t
        
        # Create adjacency with remaining capacities
        radj = [[] for _ in range(n)]
        for j, (u, v, c, idx) in enumerate(edge_info):
            # Forward edge: can use up to edge_flows[j] (flow already there)
            # But we need to track which contract's flow
            # Actually, we need to decompose the total flow
            
            # For decomposition, we look at the flow network
            # and find augmenting paths for each contract
            pass
        
        # Simpler approach: use the flow network directly
        # For each contract, find paths from s to t in the flow graph
        # and push flow along those paths
        
        # Rebuild a subgraph for this contract
        # We can use any flow that exists in the network
        
        # Actually, let's use a different approach:
        # For each contract, compute max flow from s to t in a graph
        # where each edge has capacity = current flow on that edge
        # Then subtract that flow from the edge capacities
        
        # Build flow network for this contract
        contract_nodes = n
        contract_graph = [[] for _ in range(contract_nodes)]
        contract_edge_info = []
        
        for j, (u, v, c, idx) in enumerate(edge_info):
            cap = edge_flows[j]
            if cap > 0:
                contract_graph[u].append([v, cap, 0, len(contract_graph[v])])
                contract_graph[v].append([u, 0, 0, len(contract_graph[u]) - 1])
                contract_edge_info.append((u, len(contract_graph[u]) - 1, j))
        
        # Find max flow from s to t
        contract_level = [0] * contract_nodes
        contract_ptr = [0] * contract_nodes
        
        def contract_bfs():
            for i in range(contract_nodes):
                contract_level[i] = -1
            contract_level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for edge in contract_graph[u]:
                    v, cap, flow, _ = edge
                    if cap - flow > 0 and contract_level[v] == -1:
                        contract_level[v] = contract_level[u] + 1
                        q.append(v)
            return contract_level[t] != -1
        
        def contract_dfs(u, pushed):
            if pushed == 0 or u == t:
                return pushed
            for i in range(contract_ptr[u], len(contract_graph[u])):
                contract_ptr[u] = i
                edge = contract_graph[u][i]
                v, cap, flow, rev = edge
                if contract_level[v] != contract_level[u] + 1 or cap - flow == 0:
                    continue
                tr = contract_dfs(v, min(pushed, cap - flow))
                if tr == 0:
                    continue
                edge[2] += tr
                contract_graph[v][rev][2] -= tr
                return tr
            return 0
        
        contract_flow = 0
        while contract_bfs():
            contract_ptr = [0] * contract_nodes
            while True:
                pushed = contract_dfs(s, float('inf'))
                if pushed == 0:
                    break
                contract_flow += pushed
                if contract_flow >= d:
                    break
            if contract_flow >= d:
                break
        
        # Extract flow on each edge
        for u, graph_idx, j in contract_edge_info:
            flow_on_edge = contract_graph[u][graph_idx][2]
            result[contract_idx][j] = flow_on_edge
            edge_flows[j] -= flow_on_edge
    
    for row in result:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    solve()