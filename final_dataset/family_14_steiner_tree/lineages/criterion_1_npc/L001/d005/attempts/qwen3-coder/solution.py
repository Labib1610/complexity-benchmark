import sys
from itertools import combinations

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1

def kruskal(n, edges, must_connect):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # First, connect all required nodes
    cost = 0
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            cost += w
            # Check if all must_connect nodes are connected
            first = find(parent, must_connect[0])
            if all(find(parent, node) == first for node in must_connect):
                break
    return cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    targets = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    edges.sort()
    
    # Use Kruskal's algorithm to find minimum cost to connect all targets
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cost = 0
    connected_components = {target: target for target in targets}
    
    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            # Check if this union connects any target components
            for target in targets:
                connected_components[target] = find(parent, target)
            
            # Count unique components among targets
            unique_components = set(connected_components.values())
            cost += w
            
            if len(unique_components) == 1:
                break
    
    print(cost)

solve()