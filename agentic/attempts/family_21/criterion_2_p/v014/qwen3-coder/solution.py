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
    if not lines:
        return
    
    first_line = list(map(int, lines[0].split()))
    n, m, h1, h2, limit = first_line
    
    edges = []
    edge_dict = defaultdict(list)
    
    for i in range(1, m + 1):
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
    
    # We need to find a minimum cut that separates h1 and h2
    # This is equivalent to finding the minimum s-t cut in the graph
    # We can model this as a shortest path problem in the dual (using max flow = min cut)
    # But since we have weights on edges, we use Dijkstra's algorithm with modifications
    
    # Actually, this is a minimum cut problem. We can use max flow/min cut.
    # But to keep it simple, we'll use the fact that min cut = max flow and use a flow algorithm.
    # However, we can also think of it as finding a partition of nodes into two sets,
    # one containing h1 and the other containing h2, such that the sum of weights of edges
    # crossing the partition is minimized.
    
    # Let's implement a simple Ford-Fulkerson with DFS to find max flow (which equals min cut)
    
    # Build adjacency list with capacity
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
    
    min_cut_value = ford_fulkerson(h1, h2)
    
    if min_cut_value > limit:
        print("NO")
        return
    
    # Now we need to find which edges are in the min cut
    # Run BFS from h1 in the residual graph to find the S side of the cut
    visited_cut = set()
    queue_cut = deque([h1])
    visited_cut.add(h1)
    
    while queue_cut:
        node = queue_cut.popleft()
        for neighbor in adj[node]:
            if neighbor not in visited_cut and capacity[node][neighbor] > 0:
                visited_cut.add(neighbor)
                queue_cut.append(neighbor)
    
    # The min cut consists of edges from visited_cut to not visited_cut
    # Reconstruct original capacities to identify cut edges
    original_capacity = defaultdict(lambda: defaultdict(int))
    for u, v, w in edges:
        original_capacity[u][v] += w
        original_capacity[v][u] += w
    
    cut_edges = []
    total_sealant = 0
    
    for u, v, w in edges:
        # Check if this edge crosses the cut
        # An edge u-v is in the cut if:
        # (u in S and v in T) or (u in T and v in S)
        u_in_S = u in visited_cut
        v_in_S = v in visited_cut
        if u_in_S != v_in_S:  # Exactly one of them is in S
            cut_edges.append((u, v))
            total_sealant += w
    
    if total_sealant > limit:
        print("NO")
        return
        
    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(u, v)

solve()