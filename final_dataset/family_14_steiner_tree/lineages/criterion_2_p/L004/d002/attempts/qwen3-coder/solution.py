import sys
from collections import defaultdict, deque

def find_path(graph, start, end, n):
    visited = [False] * (n + 1)
    queue = deque([(start, [])])
    visited[start] = True
    
    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return path
            
        for neighbor, edge_idx in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, path + [edge_idx]))
    
    return None

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    flagged = list(map(int, sys.stdin.readline().split()))
    
    edges = []
    graph = defaultdict(list)
    
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v, i))
        graph[u].append((v, i))
        graph[v].append((u, i))
    
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight for Kruskal-like approach
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(n + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    # First, connect all flagged nodes with MST
    used_edges = []
    flagged_set = set(flagged)
    connected_flagged = set()
    
    # Add edges until all flagged nodes are connected
    for w, u, v, idx in edges:
        if union(u, v):
            used_edges.append((w, u, v, idx))
            # Check if we've connected all flagged nodes
            roots = set(find(node) for node in flagged)
            if len(roots) == 1:
                break
    
    total_energy = sum(w for w, _, _, _ in used_edges)
    print(total_energy)

solve()