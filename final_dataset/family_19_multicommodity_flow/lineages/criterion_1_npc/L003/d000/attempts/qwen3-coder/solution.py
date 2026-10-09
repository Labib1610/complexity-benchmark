import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    items = []
    for _ in range(k):
        s, t, d = map(int, sys.stdin.readline().split())
        items.append((s, t, d))
    
    edges = []
    edge_index = {}
    graph = defaultdict(list)
    for i in range(m):
        u, v, limit = map(int, sys.stdin.readline().split())
        edges.append((u, v, limit))
        edge_index[(u, v)] = i
        graph[u].append(v)
    
    return n, m, k, items, edges, edge_index, graph

def bfs_path(graph, start, end, n):
    # Find a path from start to end using BFS
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        if node == end:
            break
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)
    
    if not visited[end]:
        return None  # No path found
    
    # Reconstruct path
    path = []
    current = end
    while parent[current] != -1:
        path.append((parent[current], current))
        current = parent[current]
    path.reverse()
    return path

def solve():
    n, m, k, items, edges, edge_index, graph = read_input()
    
    # For each item type, find a flow path
    flows = [[0] * m for _ in range(k)]
    edge_usage = [0] * m  # Track total usage of each edge
    
    paths = []
    for i in range(k):
        s, t, d = items[i]
        path_edges = bfs_path(graph, s, t, n)
        if path_edges is None:
            print("NO")
            return
        paths.append(path_edges)
        
        # Check if we can send 'd' units along this path
        min_capacity = float('inf')
        for u, v in path_edges:
            idx = edge_index[(u, v)]
            remaining_capacity = edges[idx][2] - edge_usage[idx]
            min_capacity = min(min_capacity, remaining_capacity)
        
        if min_capacity < d:
            print("NO")
            return
            
        # Allocate the flow
        for u, v in path_edges:
            idx = edge_index[(u, v)]
            flows[i][idx] += d
            edge_usage[idx] += d
    
    print("YES")
    for flow in flows:
        print(' '.join(map(str, flow)))

solve()