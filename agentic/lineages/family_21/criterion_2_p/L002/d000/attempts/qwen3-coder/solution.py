import sys
from collections import deque, defaultdict
import heapq

def read_input():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    return input_lines

def solve():
    lines = read_input()
    first_line = list(map(int, lines[0].split()))
    n, m, h1, h2, limit = first_line
    
    edges = []
    edge_dict = defaultdict(list)
    
    for i in range(1, m+1):
        u, v, w = map(int, lines[i].split())
        edges.append((u, v, w))
        edge_dict[u].append((v, w))
        edge_dict[v].append((u, w))
    
    # Check if h1 and h2 are already disconnected
    def bfs_check(source, target):
        visited = set()
        queue = deque([source])
        visited.add(source)
        while queue:
            node = queue.popleft()
            if node == target:
                return True
            for neighbor, _ in edge_dict[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False
    
    if not bfs_check(h1, h2):
        print("YES")
        print(0)
        return
    
    # We need to find a minimum cut between h1 and h2
    # This is equivalent to finding the minimum spanning tree in the dual graph
    # But since we have edge weights, we use the max-flow min-cut theorem
    # We'll use a modified Dijkstra to find the minimum cut
    
    # Actually, we can model this as a shortest path problem in the dual
    # But the easier approach is to realize that we want to find a set of edges
    # whose removal disconnects h1 and h2, and whose total weight is minimized
    # This is the minimum cut problem.
    
    # We'll use a flow-based approach or a greedy approach.
    # Since the constraints are small, we can try all possible combinations
    # But that's exponential. Let's use a proper min-cut algorithm.
    
    # Let's implement a simple Ford-Fulkerson with DFS to find max flow = min cut
    # But we need to be careful about the output format.
    
    # Build adjacency list for flow network
    capacity = defaultdict(lambda: defaultdict(int))
    adj = defaultdict(list)
    
    for u, v, w in edges:
        # Since it's undirected, we add capacity in both directions
        capacity[u][v] += w
        capacity[v][u] += w
        adj[u].append(v)
        adj[v].append(u)
    
    def bfs_flow(source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)
        parent[source] = -1
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in visited and capacity[u][v] > 0:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
        return False
    
    def ford_fulkerson(source, sink):
        parent = defaultdict(lambda: -1)
        max_flow = 0
        
        while bfs_flow(source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, capacity[parent[s]][s])
                s = parent[s]
            
            # Update capacities
            v = sink
            while v != source:
                u = parent[v]
                capacity[u][v] -= path_flow
                capacity[v][u] += path_flow
                v = parent[v]
            
            max_flow += path_flow
        
        return max_flow
    
    # The min-cut value is equal to the max-flow
    # But we need to find which edges are in the cut
    # Let's make a copy of the original graph for cut detection
    original_capacity = defaultdict(lambda: defaultdict(int))
    original_adj = defaultdict(list)
    
    for u, v, w in edges:
        original_capacity[u][v] += w
        original_capacity[v][u] += w
        if v not in original_adj[u]:
            original_adj[u].append(v)
        if u not in original_adj[v]:
            original_adj[v].append(u)
    
    # Run max flow
    # We need to work on a copy
    capacity = defaultdict(lambda: defaultdict(int))
    adj = defaultdict(list)
    
    for u, v, w in edges:
        capacity[u][v] += w
        capacity[v][u] += w
        if v not in adj[u]:
            adj[u].append(v)
        if u not in adj[v]:
            adj[v].append(u)
    
    max_flow = ford_fulkerson(h1, h2)
    
    if max_flow > limit:
        print("NO")
        return
    
    # Now find the edges in the min-cut
    # Run BFS from h1 in the residual graph to find reachable nodes
    visited_residual = set()
    queue_residual = deque([h1])
    visited_residual.add(h1)
    
    while queue_residual:
        u = queue_residual.popleft()
        for v in adj[u]:  # adj still contains all original edges
            if v not in visited_residual and capacity[u][v] > 0:
                visited_residual.add(v)
                queue_residual.append(v)
    
    # The min-cut edges are those from visited_residual to not visited_residual
    cut_edges = []
    total_cut_weight = 0
    
    for u, v, w in edges:
        # Check if this edge goes from the source side to the sink side
        if (u in visited_residual and v not in visited_residual) or \
           (v in visited_residual and u not in visited_residual):
            cut_edges.append((u, v))
            total_cut_weight += w
    
    # Verify the total weight does not exceed the limit
    if total_cut_weight > limit:
        print("NO")
        return
    
    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(u, v)

solve()