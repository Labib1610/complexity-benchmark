import sys
from collections import deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    edges = []
    graph = [[] for _ in range(n+1)]
    
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u, v, w))
        graph[u].append((v, w, i))
        graph[v].append((u, w, i))
    
    # Binary search on the maximum edge weight we can allow in our path
    def can_block(B_val):
        # We want to check if we can disconnect s and t by removing edges with total cost <= B
        # This is equivalent to finding a min-cut between s and t where the sum of weights of removed edges <= B
        # But since we have weights, we can model this as finding if there's a path from s to t using only edges 
        # with total cost > B. Instead, we'll use a different approach.
        
        # Actually, we can think of this as: we want to remove a set of edges such that there's no path from s to t,
        # and the sum of their weights is <= B. This is the minimum cut problem.
        # Since graph is undirected, we can use max flow/min cut.
        # But let's implement a simpler version: try all subsets of edges with total cost <= B and see if removing them disconnects s and t.
        # That's exponential. Let's do better.
        
        # Let's sort edges by weight and binary search on the answer.
        # For a fixed max edge weight W, we can remove all edges with weight > W and see if s and t are disconnected.
        # But that doesn't account for the budget B properly.
        
        # Correct approach: Model this as a flow network. Each edge has capacity equal to its weight.
        # The minimum cost to disconnect s and t is the minimum cut, which equals the maximum flow from s to t.
        # If max_flow(s,t) <= B, then we can secure the site.
        # Then we need to find which edges are part of the min-cut.
        
        # Implementing Ford-Fulkerson or Edmonds-Karp for max flow
        from collections import defaultdict
        
        # Build flow network
        capacity = {}
        edge_index_map = {}
        for i, (u,v,w) in enumerate(edges):
            if (u,v) not in capacity:
                capacity[(u,v)] = 0
                capacity[(v,u)] = 0
            capacity[(u,v)] += w
            capacity[(v,u)] += w
            edge_index_map[(u,v)] = edge_index_map.get((u,v), []) + [i]
            edge_index_map[(v,u)] = edge_index_map.get((v,u), []) + [i]
            
        def bfs_find_path(source, sink, parent):
            visited = [False] * (n+1)
            queue = deque([source])
            visited[source] = True
            
            while queue:
                u = queue.popleft()
                for v in range(1, n+1):
                    if not visited[v]:
                        if capacity.get((u,v), 0) > 0:
                            queue.append(v)
                            visited[v] = True
                            parent[v] = u
                            if v == sink:
                                return True
            return False
        
        def ford_fulkerson(source, sink):
            parent = [-1] * (n+1)
            max_flow = 0
            
            while bfs_find_path(source, sink, parent):
                path_flow = float('inf')
                s = sink
                while s != source:
                    path_flow = min(path_flow, capacity[(parent[s], s)])
                    s = parent[s]
                
                v = sink
                while v != source:
                    u = parent[v]
                    capacity[(u,v)] -= path_flow
                    capacity[(v,u)] += path_flow
                    v = parent[v]
                    
                max_flow += path_flow
                
            return max_flow
        
        # Make a copy of capacities for flow computation
        original_capacity = {k:v for k,v in capacity.items()}
        
        flow_value = ford_fulkerson(s, t)
        
        # Restore capacities
        for k in capacity:
            capacity[k] = original_capacity[k]
            
        if flow_value > B:
            return False, []
        
        # Now we need to find the actual edges in the min-cut
        # Run BFS to find reachable nodes from s in residual graph
        visited_cut = [False] * (n+1)
        queue_cut = deque([s])
        visited_cut[s] = True
        while queue_cut:
            u = queue_cut.popleft()
            for v in range(1, n+1):
                if not visited_cut[v] and capacity.get((u,v), 0) > 0:
                    queue_cut.append(v)
                    visited_cut[v] = True
                    
        # Edges crossing the cut (S, T) where S = {nodes reachable from s}
        cut_edges = []
        for i, (u,v,w) in enumerate(edges):
            # Check if u in S and v in T OR u in T and v in S
            if (visited_cut[u] and not visited_cut[v]) or (not visited_cut[u] and visited_cut[v]):
                cut_edges.append((u, v))
                
        return True, cut_edges
    
    # Since implementing max-flow correctly is complex, let's simplify:
    # Sort edges by weight, and greedily add edges until s and t are disconnected.
    # But that's not optimal either. Let's just implement the correct solution.
    
    # Re-implementing with proper flow network
    INF = float('inf')
    
    # Create adjacency list with edge indices
    adj = [[] for _ in range(n+1)]
    for i, (u,v,w) in enumerate(edges):
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        
    # Function to compute max flow
    def max_flow(source, sink):
        # Residual graph as adjacency list
        res_graph = [[] for _ in range(n+1)]
        edge_list = []  # To store edges for reconstruction
        
        index_map = {}  # map original edge index to new edge indices
        
        for i, (u,v,w) in enumerate(edges):
            # Add forward and backward edges
            # Store (to, capacity, reverse_edge_index)
            fwd_idx = len(edge_list)
            edge_list.append([v, w, 0])  # forward edge
            bwd_idx = len(edge_list)
            edge_list.append([u, 0, 0])  # backward edge
            edge_list[fwd_idx][2] = bwd_idx
            edge_list[bwd_idx][2] = fwd_idx
            
            res_graph[u].append(fwd_idx)
            res_graph[v].append(bwd_idx)
            
            if i not in index_map:
                index_map[i] = []
            index_map[i].append(fwd_idx)
            
        def bfs_level_graph():
            level = [-1] * (n+1)
            level[source] = 0
            q = deque([source])
            while q:
                u = q.popleft()
                for e_idx in res_graph[u]:
                    to, cap, rev = edge_list[e_idx]
                    if level[to] == -1 and cap > 0:
                        level[to] = level[u] + 1
                        q.append(to)
            return level[sink] != -1, level
        
        def send_flow(u, sink, flow, level, start):
            if u == sink:
                return flow
            while start[u] < len(res_graph[u]):
                e_idx = res_graph[u][start[u]]
                to, cap, rev = edge_list[e_idx]
                if level[to] == level[u] + 1 and cap > 0:
                    curr_flow = min(flow, cap)
                    temp_flow = send_flow(to, sink, curr_flow, level, start)
                    if temp_flow > 0:
                        edge_list[e_idx][1] -= temp_flow
                        edge_list[rev][1] += temp_flow
                        return temp_flow
                start[u] += 1
            return 0
        
        max_flow_result = 0
        while True:
            has_path, level = bfs_level_graph()
            if not has_path:
                break
            start = [0] * (n+1)
            while True:
                flow = send_flow(source, sink, INF, level, start)
                if flow == 0:
                    break
                max_flow_result += flow
                
        return max_flow_result, edge_list, res_graph, index_map
    
    # Compute max flow
    flow_val, final_edge_list, res_graph_final, index_map_final = max_flow(s, t)
    
    if flow_val > B:
        print("NO")
        return
    
    # Find min-cut edges
    # BFS from source in residual graph to find reachable nodes
    level_cut = [-1] * (n+1)
    queue_cut = deque([s])
    level_cut[s] = 0
    while queue_cut:
        u = queue_cut.popleft()
        for e_idx in res_graph_final[u]:
            to, cap, rev = final_edge_list[e_idx]
            if level_cut[to] == -1 and cap > 0:
                level_cut[to] = level_cut[u] + 1
                queue_cut.append(to)
                
    # Edges in min-cut: those going from reachable to unreachable
    cut_edges_output = []
    for i, (u,v,w) in enumerate(edges):
        # In original graph, check if this edge crosses the cut
        # u reachable and v unreachable OR u unreachable and v reachable
        u_reachable = (level_cut[u] != -1)
        v_reachable = (level_cut[v] != -1)
        if u_reachable != v_reachable:
            cut_edges_output.append((u, v))
            
    print("YES")
    print(len(cut_edges_output))
    for u, v in cut_edges_output:
        print(u, v)

if __name__ == "__main__":
    main()