import sys
import heapq
from collections import defaultdict, deque

def find_mincut_edges(n, edges, source, sink):
    # Edmonds-Karp implementation for max flow
    # Returns the edges in the min-cut
    graph = defaultdict(lambda: defaultdict(int))
    edge_list = {}  # To store original edge info
    
    for u, v, w in edges:
        graph[u][v] += w
        graph[v][u] += w
        edge_list[(u, v)] = edge_list.get((u, v), 0) + w
        edge_list[(v, u)] = edge_list.get((v, u), 0) + w
    
    def bfs():
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v] and graph[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        return parent
        return None
    
    # Max flow
    while True:
        parent = bfs()
        if parent is None:
            break
            
        # Find minimum capacity along the path
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        
        # Update capacities
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    
    # Find min-cut edges
    # BFS to find reachable nodes from source
    visited = [False] * (n + 1)
    queue = deque([source])
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v] and graph[u][v] > 0:
                visited[v] = True
                queue.append(v)
    
    # Edges crossing the cut
    cut_edges = []
    for u, v, w in edges:
        # Check if edge crosses the cut
        if visited[u] and not visited[v]:
            cut_edges.append((u, v, w))
        elif visited[v] and not visited[u]:
            cut_edges.append((v, u, w))
    
    return cut_edges

def solve():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    generators = []
    for _ in range(k):
        generators.append(int(data[idx]))
        idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u, v, w))
    
    if k <= 1:
        print("YES")
        print(0)
        return
    
    # Create a super source and super sink
    # Connect super source to all generators except last
    # Connect all generators except first to super sink
    super_source = 0
    super_sink = n + 1
    
    extended_edges = edges[:]
    
    # Add edges from super_source to generators[0] with infinite capacity
    for i in range(len(generators) - 1):
        extended_edges.append((super_source, generators[i], B + 1))
    
    # Add edges from generators to super_sink with infinite capacity
    for i in range(1, len(generators)):
        extended_edges.append((generators[i], super_sink, B + 1))
    
    # Find min-cut between super_source and super_sink
    cut_edges = find_mincut_edges(n + 2, extended_edges, super_source, super_sink)
    
    # Filter out the infinite capacity edges (the ones we added)
    original_cut_edges = []
    total_cost = 0
    
    for u, v, w in cut_edges:
        if u != super_source and v != super_sink and w <= B:
            original_cut_edges.append((u, v, w))
            total_cost += w
    
    if total_cost <= B:
        print("YES")
        print(len(original_cut_edges))
        for u, v, _ in original_cut_edges:
            print(u, v)
    else:
        print("NO")

solve()