import sys
from collections import deque, defaultdict
import heapq

def read_input():
    n, m, s, t, B = map(int, sys.stdin.readline().split())
    edges = []
    edge_dict = {}
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
        edge_dict[(u,v)] = w
        edge_dict[(v,u)] = w
    return n, m, s, t, B, edges, edge_dict

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def min_cut(edges, n, s, t):
    # Build adjacency list for residual graph
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Use Dijkstra to find shortest path as proxy for min-cut value
    # But we need actual min-cut computation
    
    # Ford-Fulkerson with BFS (Edmonds-Karp) to find min cut
    def bfs_find_path(source, sink, capacity, adj):
        parent = [-1] * (n+1)
        visited = [False] * (n+1)
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v] and capacity[(u,v)] > 0:
                    parent[v] = u
                    visited[v] = True
                    queue.append(v)
                    if v == sink:
                        return True, parent
        return False, parent
    
    # Build initial capacity dict
    capacity = defaultdict(int)
    adj = defaultdict(list)
    for u, v, w in edges:
        capacity[(u,v)] += w
        capacity[(v,u)] += w
        if v not in adj[u]:
            adj[u].append(v)
        if u not in adj[v]:
            adj[v].append(u)
            
    # Make sure adjacency lists are complete
    all_nodes = set()
    for u, v, w in edges:
        all_nodes.add(u)
        all_nodes.add(v)
        
    # Edmonds-Karp algorithm
    max_flow = 0
    while True:
        found, parent = bfs_find_path(s, t, capacity, adj)
        if not found:
            break
            
        # Find minimum capacity along the path
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, capacity[(u,v)])
            v = u
            
        # Update capacities
        v = t
        while v != s:
            u = parent[v]
            capacity[(u,v)] -= path_flow
            capacity[(v,u)] += path_flow
            v = u
            
        max_flow += path_flow
    
    # Now we need to find which edges form the min-cut
    # Run BFS from source in residual graph to find S-side of cut
    visited = [False] * (n+1)
    queue = deque([s])
    visited[s] = True
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v] and capacity[(u,v)] > 0:
                visited[v] = True
                queue.append(v)
    
    # Edges crossing the cut: from visited to unvisited
    cut_edges = []
    for u, v, w in edges:
        # Check if this edge crosses the cut
        if (visited[u] and not visited[v]) or (visited[v] and not visited[u]):
            cut_edges.append((u, v, w))
    
    return max_flow, cut_edges

def solve():
    n, m, s, t, B, edges, edge_dict = read_input()
    
    # Compute min-cut value and edges
    min_cut_value, cut_edges_list = min_cut(edges, n, s, t)
    
    if min_cut_value > B:
        print("NO")
        return
    
    # Output the solution
    print("YES")
    print(len(cut_edges_list))
    for u, v, w in cut_edges_list:
        print(u, v)

solve()