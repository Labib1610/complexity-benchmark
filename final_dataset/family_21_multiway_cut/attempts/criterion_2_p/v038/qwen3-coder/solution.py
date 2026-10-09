import sys
from collections import deque, defaultdict
import heapq

def read_input():
    n, m, s, t, B = map(int, sys.stdin.readline().split())
    edges = []
    edge_dict = defaultdict(list)
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
        edge_dict[u].append((v, w, i))
        edge_dict[v].append((u, w, i))
    return n, m, s, t, B, edges, edge_dict

def dijkstra(n, source, target, edge_dict, disabled_edges=set()):
    dist = [float('inf')] * (n + 1)
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == target:
            return dist[target]
        for v, w, idx in edge_dict[u]:
            if idx in disabled_edges:
                continue
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist[target]

def find_min_cut(n, s, t, edges, B):
    # Create adjacency list for flow network
    graph = [[] for _ in range(n + 1)]
    edge_index = {}
    for i, (u, v, w) in enumerate(edges):
        graph[u].append((v, w, i))
        graph[v].append((u, w, i))
        edge_index[(u, v, i)] = i
        edge_index[(v, u, i)] = i

    # Use Ford-Fulkerson with DFS to find max flow/min cut
    def bfs_flow():
        parent = [-1] * (n + 1)
        visited = [False] * (n + 1)
        queue = deque([s])
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            for v, w, idx in graph[u]:
                if not visited[v] and w > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == t:
                        return parent
        return None

    # Create residual graph
    residual = [[0] * (n + 1) for _ in range(n + 1)]
    edge_indices = {}
    for i, (u, v, w) in enumerate(edges):
        residual[u][v] += w
        residual[v][u] += w
        if (u, v) not in edge_indices:
            edge_indices[(u, v)] = []
        if (v, u) not in edge_indices:
            edge_indices[(v, u)] = []
        edge_indices[(u, v)].append((w, i))
        edge_indices[(v, u)].append((w, i))
    
    max_flow = 0
    while True:
        parent = bfs_flow()
        if parent is None:
            break
            
        path_flow = float('inf')
        s_ptr = t
        while s_ptr != s:
            path_flow = min(path_flow, residual[parent[s_ptr]][s_ptr])
            s_ptr = parent[s_ptr]
            
        max_flow += path_flow
        
        if max_flow > B:
            return None, None
            
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u
    
    if max_flow > B:
        return None, None
        
    # Find min cut
    visited = [False] * (n + 1)
    queue = deque([s])
    visited[s] = True
    
    while queue:
        u = queue.popleft()
        for v, w, idx in graph[u]:
            if not visited[v] and residual[u][v] > 0:
                visited[v] = True
                queue.append(v)
    
    cut_edges = []
    total_cost = 0
    used_indices = set()
    
    for i, (u, v, w) in enumerate(edges):
        # Check if this edge crosses the cut
        if visited[u] and not visited[v]:
            if i not in used_indices:
                cut_edges.append((u, v))
                total_cost += w
                used_indices.add(i)
        elif visited[v] and not visited[u]:
            if i not in used_indices:
                cut_edges.append((u, v))
                total_cost += w
                used_indices.add(i)
                
    if total_cost <= B:
        return cut_edges, total_cost
    else:
        return None, None

def solve():
    n, m, s, t, B, edges, edge_dict = read_input()
    
    # Check if s and t are already disconnected
    dist = dijkstra(n, s, t, edge_dict)
    if dist == float('inf'):
        print("YES")
        print(0)
        return
    
    # Find min cut
    cut_edges, cost = find_min_cut(n, s, t, edges, B)
    
    if cut_edges is not None and cost <= B:
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(u, v)
    else:
        print("NO")

solve()