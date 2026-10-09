import sys
from collections import defaultdict, deque

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
    graph = defaultdict(list)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u, v, w))
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # We want to find the minimum cost to disconnect s and t
    # This is equivalent to finding the minimum cut between s and t
    # Which equals the maximum flow from s to t if we treat edge weights as capacities
    # But since we're dealing with costs (not capacities), we need to think differently.
    # Actually, we want to find the minimum weight edge cut that separates s and t.
    # This is the minimum edge-cut separating s and t, which equals the minimum cost
    # to disconnect s and t.
    
    # We can model this as a shortest path problem in the dual: 
    # The minimum cost to disconnect s and t is the minimum cost of edges that form
    # a cut between s and t. This is exactly the minimum edge-cut problem.
    # It's equivalent to finding the minimum sum of edge weights such that removing
    # those edges disconnects s and t.
    
    # This is solved via max-flow min-cut theorem if we consider edge weights as capacities,
    # but here they are costs. So we can't directly apply max-flow.
    # However, we can use the fact that the minimum cost edge-cut equals the minimum cost
    # to prevent connectivity between s and t.
    
    # Let's use a different approach: binary search on the answer.
    # For a given budget b, check if we can disconnect s and t by removing edges of total cost <= b.
    # To do this, we remove all edges with cost > b, and check if s and t are disconnected.
    # But this doesn't work because we want to minimize the sum of costs, not just threshold.
    
    # Correct approach: This is the minimum edge-cut problem where each edge has a cost.
    # The minimum cost edge-cut separating s and t can be found using flow techniques
    # by transforming the problem appropriately.
    
    # However, let's think simpler: we want to find a subset of edges to remove such that:
    # 1. After removal, s and t are disconnected.
    # 2. Total cost of removed edges <= B.
    # 3. Among all such subsets, we want any one that satisfies 1 and 2.
    
    # The decision version is: does there exist a subset of edges with total cost <= B
    # such that removing them disconnects s and t?
    
    # This is equivalent to checking if the minimum cost edge-cut is <= B.
    # If yes, then we can find such a cut.
    
    # Let's compute the minimum cost edge-cut separating s and t.
    # We can reduce this to a max-flow problem by assigning capacities equal to costs.
    # Then the value of the min-cut will give us the minimum cost.
    # If this value <= B, then YES, otherwise NO.
    
    # But wait, in max-flow, capacities are on edges. Here costs are on edges.
    # Minimizing sum of costs of edges in a cut is exactly what min-cut gives us
    # when we set capacity(u,v) = cost(u,v).
    
    # So we build a flow network with capacities = costs, and compute min-cut value.
    # If min-cut value <= B, then YES, else NO.
    
    # Now, how to get the actual edges in the cut?
    # Run max-flow algorithm, then perform BFS from source in residual graph to find
    # nodes reachable from source. Edges from reachable to non-reachable nodes form the cut.
    
    # Let's implement this.
    
    # First, let's handle the case where s == t
    if s == t:
        print("NO")
        return
    
    # Build the flow network
    # We'll use 1-based indexing
    INF = float('inf')
    
    # Since we're implementing max-flow, let's define a function
    def bfs_flow(capacity, source, sink):
        from collections import deque
        n_nodes = n
        visited = [False] * (n_nodes + 1)
        queue = deque()
        queue.append(source)
        visited[source] = True
        parent = [-1] * (n_nodes + 1)
        
        while queue:
            u = queue.popleft()
            for v in range(1, n_nodes + 1):
                if not visited[v] and capacity.get((u, v), 0) > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return parent
        return None
    
    def edmonds_karp(edges_list, source, sink, num_nodes):
        # Create adjacency list and capacity dict
        capacity = {}
        adj = defaultdict(list)
        for u, v, w in edges_list:
            # Add forward and backward edges
            capacity[(u, v)] = capacity.get((u, v), 0) + w
            capacity[(v, u)] = capacity.get((v, u), 0) + w
            adj[u].append(v)
            adj[v].append(u)
        
        # Make sure all reverse edges exist with 0 capacity initially
        for u in adj:
            for v in adj[u]:
                if (u, v) not in capacity:
                    capacity[(u, v)] = 0
        
        max_flow = 0
        while True:
            parent = bfs_flow(capacity, source, sink)
            if parent is None:
                break
            
            # Find minimum capacity along the path
            path_flow = INF
            s_node = sink
            while s_node != source:
                u = parent[s_node]
                path_flow = min(path_flow, capacity[(u, s_node)])
                s_node = u
            
            # Update capacities
            v_node = sink
            while v_node != source:
                u = parent[v_node]
                capacity[(u, v_node)] -= path_flow
                capacity[(v_node, u)] += path_flow
                v_node = u
            
            max_flow += path_flow
        
        # Now find the min-cut edges
        # BFS from source in residual graph to find reachable nodes
        visited = [False] * (num_nodes + 1)
        queue = deque()
        queue.append(source)
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v in range(1, num_nodes + 1):
                if not visited[v] and capacity.get((u, v), 0) > 0:
                    visited[v] = True
                    queue.append(v)
        
        # Edges from visited to not visited form the cut
        cut_edges = []
        for u, v, w in edges_list:
            # Check both directions since we added both during construction
            if (visited[u] and not visited[v]) or (visited[v] and not visited[u]):
                # Only add once
                if (u, v, w) not in cut_edges and (v, u, w) not in cut_edges:
                    cut_edges.append((u, v, w))
        
        return max_flow, cut_edges
    
    # But wait, our graph might have multiple edges between same pair of nodes.
    # We should combine them.
    edge_dict = defaultdict(int)
    for u, v, w in edges:
        if u > v:
            u, v = v, u
        edge_dict[(u, v)] += w
    
    combined_edges = []
    for (u, v), w in edge_dict.items():
        combined_edges.append((u, v, w))
    
    # Now run max-flow/min-cut
    min_cut_value, min_cut_edges = edmonds_karp(combined_edges, s, t, n)
    
    if min_cut_value > B:
        print("NO")
        return
    
    # We have a solution, now output the edges
    print("YES")
    print(len(min_cut_edges))
    for u, v, w in min_cut_edges:
        print(u, v)

if __name__ == "__main__":
    main()