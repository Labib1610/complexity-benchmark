import sys
from itertools import combinations

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def kruskal(n, edges, nodes):
    parent = list(range(n))
    rank = [0] * n
    cost = 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if union(parent, rank, u, v):
            cost += w
            nodes.discard(u)
            nodes.discard(v)
            if len(nodes) <= 1:
                return cost
    return cost

n, m, t = map(int, sys.stdin.readline().split())
critical = set(map(int, sys.stdin.readline().split()))
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

if t <= 1:
    print(0)
else:
    critical = [c - 1 for c in critical]
    edges = [(u - 1, v - 1, w) for u, v, w in edges]
    min_cost = float('inf')
    
    # For each subset of critical nodes, try to connect them
    for r in range(t, 0, -1):
        for subset in combinations(critical, r):
            nodes = set(subset)
            cost = kruskal(n, edges, nodes)
            if not nodes:
                min_cost = min(min_cost, cost)
                
    print(min_cost)