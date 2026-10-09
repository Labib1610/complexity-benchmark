from collections import defaultdict, deque
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    bc = int(data[idx])
    idx += 1
    
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    
    edges = []
    in_edges = defaultdict(list)
    out_edges = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        C = int(data[idx])
        idx += 1
        edges.append((u, v, C))
        out_edges[u].append(i)
        in_edges[v].append(i)
    
    # We'll use a max-flow approach to model the constraints.
    # Each edge has a variable x_i with 0 <= x_i <= C_i
    # For each node i (except s and t):
    #     sum_{j into i} x_j - sum_{j out of i} x_j = 0
    # For node s:
    #     sum_{j out of s} x_j - sum_{j into s} x_j = d
    # For node t:
    #     sum_{j into t} x_j - sum_{j out of t} x_j = d
    
    # This is a system of linear equations with bounds on variables.
    # We can model this as a circulation problem with demands.
    # Each edge has capacity [0, C_i]
    # Each node has demand:
    #   demand[s] = -d
    #   demand[t] = -d
    #   demand[i] = 0 for others
    
    # But we can also solve it as a max-flow problem by adding a super-source and super-sink.
    # However, since we just need feasibility, we can use the fact that a circulation exists
    # iff the total supply equals total demand and all demands can be satisfied.
    
    # Let's model it as a system of linear equations and use a greedy approach or network flow.
    # We'll use the fact that this is a circulation problem with demands and capacities.
    
    # Let's build the constraint matrix and use a network flow approach.
    # We'll create a flow network where:
    # - Each edge variable x_i is a flow on edge i
    # - Each node has a demand (net flow)
    # - Each edge has a capacity [0, C_i]
    
    # The problem is to find a feasible circulation.
    # We can transform it to a max-flow problem:
    # - Add a super-source S and super-sink T
    # - For each node i with demand d_i:
    #   - if d_i > 0, add edge (S, i) with capacity d_i
    #   - if d_i < 0, add edge (i, T) with capacity -d_i
    # - For each edge variable x_i with bounds [0, C_i], keep as is
    # - The system is feasible iff max flow from S to T saturates all demand edges.
    
    # In our case:
    # - demand[s] = -d (net outflow d)
    # - demand[t] = -d (net inflow d)
    # - demand[i] = 0 for others
    
    # So:
    # - Add edge (S, s) with capacity d
    # - Add edge (t, T) with capacity d
    # - All original edges have capacity [0, C_i]
    # - Find max flow from S to T. If it's d, then feasible.
    
    # But we also need to reconstruct the flow values.
    
    # Let's implement a Ford-Fulkerson algorithm with BFS (Edmonds-Karp) to find the flow.
    
    # Number of nodes: n components + S (super-source) + T (super-sink)
    # Let's number components from 0 to n-1, S = n, T = n+1
    S = n
    T = n + 1
    total_nodes = n + 2
    
    # Build adjacency list for the flow network
    # Each edge: (to, capacity, reverse_edge_index)
    graph = [[] for _ in range(total_nodes)]
    
    # Add original edges with capacities
    edge_index_map = {}  # map from edge index in input to (from_node, to_node, index_in_graph)
    for i in range(m):
        u, v, C = edges[i]
        u -= 1  # Convert to 0-based
        v -= 1
        # Add forward edge
        forward_idx = len(graph[u])
        backward_idx = len(graph[v])
        graph[u].append([v, C, backward_idx])  # to, capacity, reverse_index
        graph[v].append([u, 0, forward_idx])   # reverse edge with 0 capacity
        edge_index_map[i] = (u, v, forward_idx)
    
    # Add demand edges
    # demand[s] = -d => need d flow out of s => add edge (S, s) with capacity d
    # demand[t] = -d => need d flow into t => add edge (t, T) with capacity d
    s -= 1
    t -= 1
    
    # Edge (S, s)
    forward_idx_s = len(graph[S])
    backward_idx_s = len(graph[s])
    graph[S].append([s, d, backward_idx_s])
    graph[s].append([S, 0, forward_idx_s])
    
    # Edge (t, T)
    forward_idx_t = len(graph[t])
    backward_idx_t = len(graph[T])
    graph[t].append([T, d, backward_idx_t])
    graph[T].append([t, 0, forward_idx_t])
    
    # Now run max flow from S to T
    def bfs():
        parent = [-1] * total_nodes
        parent_edge = [-1] * total_nodes
        queue = deque()
        queue.append(S)
        parent[S] = -2  # Visited
        
        while queue:
            u = queue.popleft()
            for i, (v, cap, rev_idx) in enumerate(graph[u]):
                if parent[v] == -1 and cap > 0:
                    parent[v] = u
                    parent_edge[v] = i
                    if v == T:
                        return parent, parent_edge
                    queue.append(v)
        return parent, parent_edge
    
    def edmonds_karp():
        max_flow = 0
        while True:
            parent, parent_edge = bfs()
            if parent[T] == -1:
                break
            # Find minimum capacity along the path
            path_flow = float('inf')
            s_node = T
            while s_node != S:
                u = parent[s_node]
                edge_idx = parent_edge[s_node]
                path_flow = min(path_flow, graph[u][edge_idx][1])
                s_node = u
            
            # Update capacities
            v_node = T
            while v_node != S:
                u = parent[v_node]
                edge_idx = parent_edge[v_node]
                graph[u][edge_idx][1] -= path_flow  # decrease forward capacity
                rev_idx = graph[u][edge_idx][2]
                graph[v_node][rev_idx][1] += path_flow  # increase reverse capacity
                v_node = u
            
            max_flow += path_flow
        return max_flow
    
    flow_value = edmonds_karp()
    
    if flow_value != d:
        print("NO")
        return
    
    # Reconstruct the solution
    result = [0] * m
    for i in range(m):
        u, v, forward_idx = edge_index_map[i]
        # The flow on this edge is the original capacity minus current capacity
        original_capacity = edges[i][2]
        current_capacity = graph[u][forward_idx][1]
        flow = original_capacity - current_capacity
        result[i] = flow
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()