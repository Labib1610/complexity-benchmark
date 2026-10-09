import sys

# Set recursion limit for DFS in Dinic's algorithm
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        k = int(next(iterator))
    except StopIteration:
        return

    orders = []
    for _ in range(k):
        s = int(next(iterator))
        t = int(next(iterator))
        d = int(next(iterator))
        orders.append((s, t, d))

    belts = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        cap = int(next(iterator))
        belts.append((u, v, cap))

    # Build the flow network
    # Nodes: 0..n-1 (original desks), n..n+m-1 (belt nodes)
    # Total nodes: n + m
    num_nodes = n + m
    adj = [[] for _ in range(num_nodes)]
    
    # We need to track edges to recover the flow
    # Edge structure: [to, capacity, rev_index]
    # We will store additional info in a separate list or extend the structure
    # Let's use a class or a dict for edges to store original belt index
    # To keep it simple with lists: edges = [to, cap, rev, belt_idx]
    # belt_idx is -1 if not a belt-split edge
    
    edges_info = [] # Stores (u, v, cap, belt_idx) for reconstruction
    
    def add_edge(u, v, cap, belt_idx):
        # Forward edge
        adj[u].append([v, cap, len(adj[v]), belt_idx])
        # Backward edge
        adj[v].append([u, 0, len(adj[u]) - 1, -1])

    # Add edges for each belt
    # Belt i connects u -> v with capacity cap.
    # We split it: u -> (n+i) with cap, (n+i) -> v with cap.
    # The flow on u -> (n+i) is what we need to output.
    for i, (u, v, cap) in enumerate(belts):
        belt_node = n + i
        # u is 1-based in input, convert to 0-based
        add_edge(u - 1, belt_node, cap, i)
        add_edge(belt_node, v - 1, cap, -1)

    # Add source and sink for multi-commodity flow transformation
    # We create a super source and super sink.
    # Source connects to each order's start with order's demand.
    # Each order's end connects to sink with order's demand.
    # If max flow equals total demand, we have a solution.
    
    source = num_nodes
    sink = num_nodes + 1
    adj.append([])
    adj.append([])
    num_nodes += 2
    
    total_demand = 0
    for i, (s, t, d) in enumerate(orders):
        # s, t are 1-based
        add_edge(source, s - 1, d, -1)
        add_edge(t - 1, sink, d, -1)
        total_demand += d

    # Dinic's Algorithm
    level = []
    ptr = []

    def bfs():
        nonlocal level
        level = [-1] * num_nodes
        level[source] = 0
        queue = [source]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v, cap, rev, b_idx in adj[u]:
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[sink] != -1

    def dfs(u, pushed):
        if pushed == 0 or u == sink:
            return pushed
        for i in range(ptr[u], len(adj[u])):
            ptr[u] = i
            v, cap, rev, b_idx = adj[u][i]
            if level[v] != level[u] + 1 or cap == 0:
                continue
            tr = dfs(v, min(pushed, cap))
            if tr == 0:
                continue
            # Update capacities
            adj[u][i][1] -= tr
            adj[v][rev][1] += tr
            return tr
        return 0

    max_flow = 0
    while bfs():
        ptr = [0] * num_nodes
        while True:
            pushed = dfs(source, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed

    if max_flow != total_demand:
        print("NO")
        return

    print("YES")
    
    # Reconstruct the answer
    # ans[order_idx][belt_idx] = flow
    # We need to determine which flow corresponds to which order.
    # The edges from source to order starts carry the flow for that order.
    # We can decompose the flow.
    
    # Create a residual graph representation for decomposition
    # adj_res[u] = list of (v, flow, belt_idx, rev_ptr)
    
    # First, let's map the edges to easily access them.
    # We can just use the `adj` list which has the current capacities.
    # Original capacity = forward_cap + backward_cap (on the backward edge)
    # Flow = backward_cap (on the backward edge) = original_cap - forward_cap
    
    # Let's build a specific graph for decomposition to avoid messing with `adj` pointers
    # which are lists of lists.
    
    # Graph for decomposition: g[u] = list of {to, flow, belt_idx, rev_idx_in_adj}
    # We need to be careful with the "flow" value.
    # For an edge u->v added with capacity C:
    #   adj[u] has [v, rem_cap, rev_idx]
    #   adj[v] has [u, flow_used, rev_idx]
    # So flow_used is in the reverse edge.
    
    g = [[] for _ in range(num_nodes)]
    
    # We only care about edges that can carry flow (not from sink/source logic ideally)
    # But for decomposition we just need to trace paths.
    
    # Let's reconstruct the edges we added.
    # 1. Belt edges: u -> belt_node (idx=i), belt_node -> v
    #    We need flow on u -> belt_node.
    #    In adj[u]: forward edge [belt_node, rem_cap, ...]
    #    In adj[belt_node]: backward edge [u, flow, ...]
    #    So flow on belt i is adj[belt_node][rev_of_forward][1].
    
    # 2. Order source edges: source -> s
    #    Flow is in adj[s][rev][1].
    
    # 3. Order sink edges: t -> sink
    #    Flow is in adj[sink][rev][1].
    
    # We need to attribute flow to orders.
    # Algorithm:
    # For each order i with demand d:
    #   curr = s_i
    #   rem = d
    #   while rem > 0:
    #     find a path from s_i to t_i with positive flow
    #     let f be the min flow along the path
    #     subtract f from all edges on path
    #     add f to the answer for belts used on path
    
    # To speed this up, we can just DFS from s_i and push flow.
    
    ans = [[0] * m for _ in range(k)]
    
    # We need a way to iterate edges from a node efficiently
    # Let's build a residual graph structure for decomposition
    # g[u] contains indices of edges in adj[u]
    # We will modify adj in place during decomposition
    
    # Helper to get flow on edge u->v
    # Edge is adj[u][idx]. Flow is adj[v][rev][1].
    
    def decompose(u, target, f_min):
        if u == target:
            return f_min
        
        while ptr[u] < len(adj[u]):
            e = adj[u][ptr[u]]
            v, cap, rev, b_idx = e
            
            # We are looking for edges with flow > 0
            # Flow on u->v is stored in the reverse edge at adj[v][rev]
            flow_on_edge = adj[v][rev][1]
            
            if flow_on_edge > 0:
                # Check if this edge is part of the valid graph
                # We should not go backwards to source, or forwards from sink
                if v == source:
                    ptr[u] += 1
                    continue
                
                # Recurse
                res = decompose(v, target, min(f_min, flow_on_edge))
                
                if res > 0:
                    # Reduce flow
                    adj[v][rev][1] -= res
                    # Increase capacity (reduce flow on reverse)
                    # Actually adj[u][ptr[u]][1] += res is not strictly necessary 
                    # if we only care about consuming the flow, but correct residual graph
                    # would have it. Here adj[u][ptr] is the forward edge with remaining capacity.
                    # The flow is on the backward edge. We subtract flow from backward edge.
                    # We don't need to update forward edge capacity for correctness of finding *a* path,
                    # but it's cleaner.
                    
                    # If this edge corresponds to a belt, record it
                    if b_idx != -1:
                        # We found flow on belt b_idx
                        # But we don't know which order it belongs to here.
                        # The decomposition is called for a specific order.
                        pass
                    
                    # We need to return the flow amount and the path info
                    # This recursive structure is tricky for recording path.
                    pass
            
            ptr[u] += 1
        return 0

    # The recursive decomposition above is hard to manage for recording belt indices.
    # Let's use an iterative DFS for decomposition.
    
    # For each order
    for order_idx in range(k):
        s, t, d = orders[order_idx]
        s -= 1
        t -= 1
        
        remaining = d
        while remaining > 0:
            # Find one path from s to t
            path = []
            stack = [(s, iter(adj[s]))]
            visited = {s}
            parent = {} # map v -> (u, edge_idx_in_u)
            
            found = False
            curr = -1
            
            while stack:
                u, it = stack[-1]
                if u == t:
                    curr = u
                    found = True
                    break
                
                try:
                    e_idx = next(it)
                    e = adj[u][e_idx]
                    v, cap, rev, b_idx = e
                    
                    # Flow is in reverse edge
                    flow = adj[v][rev][1]
                    
                    if flow > 0 and v not in visited and v != source:
                        visited.add(v)
                        parent[v] = (u, e_idx)
                        stack.append((v, iter(adj[v])))
                except StopIteration:
                    stack.pop()
            
            if not found:
                # Should not happen if max_flow is correct
                break
            
            # Reconstruct path and find min flow
            path_edges = []
            u = t
            flow_val = float('inf')
            while u != s:
                p_u, e_idx = parent[u]
                e = adj[p_u][e_idx]
                v, cap, rev, b_idx = e
                # v is u
                flow = adj[u][rev][1]
                flow_val = min(flow_val, flow)
                path_edges.append((p_u, e_idx))
                u = p_u
            
            # Update flows and record answer
            for p_u, e_idx in path_edges:
                e = adj[p_u][e_idx]
                v, cap, rev, b_idx = e
                # Reduce flow
                adj[v][rev][1] -= flow_val
                # Increase capacity on forward edge (optional but good practice)
                adj[p_u][e_idx][1] += flow_val
                
                if b_idx != -1:
                    ans[order_idx][b_idx] += flow_val
            
            remaining -= flow_val

    for row in ans:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    solve()