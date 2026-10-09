import sys
import heapq
from collections import defaultdict

def dijkstra(graph, start, end):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    parent = {}
    heap = [(0, start)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if u == end:
            break
        if d > dist[u]:
            continue
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))
                
    return dist[end], parent

def find_path(parent, start, end):
    path = []
    current = end
    while current != start:
        prev = parent[current]
        path.append((prev, current))
        current = prev
    return path[::-1]

def solve():
    n, m, s, t, B = map(int, sys.stdin.readline().split())
    
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    # Find shortest path between s and t
    distance, parent = dijkstra(graph, s, t)
    
    if distance <= B:
        # We can't isolate them - they're too cheap to separate
        print("NO")
        return
    
    # Build residual graph for min-cut
    # We'll use the fact that min-cut = max-flow in this context
    
    # But let's think differently - we want to find minimum cut
    # Let's model this as finding minimum weight set of edges to remove
    # to disconnect s from t
    
    # Use max flow/min cut approach with capacities as weights
    from collections import deque
    
    def bfs_flow(capacity, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)
        parent[source] = -1
        
        while queue:
            u = queue.popleft()
            
            for v in capacity[u]:
                if v not in visited and capacity[u][v] > 0:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return True
        return False
    
    def ford_fulkerson(capacity, source, sink):
        parent = {}
        max_flow = 0
        
        while bfs_flow(capacity, source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, capacity[parent[s]][s])
                s = parent[s]
            
            v = sink
            while v != source:
                u = parent[v]
                capacity[u][v] -= path_flow
                if v not in capacity:
                    capacity[v] = {}
                if u not in capacity[v]:
                    capacity[v][u] = 0
                capacity[v][u] += path_flow
                v = parent[v]
            
            max_flow += path_flow
        
        return max_flow
    
    # Create capacity graph
    capacity = {}
    for u, v, w in edges:
        if u not in capacity:
            capacity[u] = {}
        if v not in capacity:
            capacity[v] = {}
        capacity[u][v] = w
        capacity[v][u] = w  # Since it's undirected
    
    # Make a copy for min-cut calculation
    import copy
    original_capacity = copy.deepcopy(capacity)
    
    # Calculate min-cut value
    min_cut_value = ford_fulkerson(copy.deepcopy(original_capacity), s, t)
    
    if min_cut_value > B:
        print("NO")
        return
    
    # Now we need to find which edges form the actual min-cut
    # Run Ford-Fulkerson again but keep track of reachable nodes from source
    
    temp_capacity = copy.deepcopy(original_capacity)
    parent = {}
    ford_fulkerson(temp_capacity, s, t)  # This modifies temp_capacity
    
    # BFS to find what nodes are reachable from source in residual graph
    visited_from_source = set()
    queue = deque([s])
    visited_from_source.add(s)
    
    while queue:
        u = queue.popleft()
        for v in temp_capacity[u]:
            if temp_capacity[u][v] > 0 and v not in visited_from_source:
                visited_from_source.add(v)
                queue.append(v)
    
    # Edges crossing from visited_from_source to unvisited form the cut
    cut_edges = []
    total_cost = 0
    
    for u, v, w in edges:
        # Check if edge crosses the cut
        u_in_source_side = u in visited_from_source
        v_in_source_side = v in visited_from_source
        
        if u_in_source_side != v_in_source_side:
            cut_edges.append((u, v))
            total_cost += w
    
    if total_cost <= B:
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(u, v)
    else:
        print("NO")

solve()