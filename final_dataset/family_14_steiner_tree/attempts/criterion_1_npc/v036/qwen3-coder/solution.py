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

def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n
    cost = 0
    for w, u, v in sorted(edges):
        if union(parent, rank, u, v):
            cost += w
    return cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    critical = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    # Convert to 0-indexed
    critical = [x - 1 for x in critical]
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u-1, v-1))
    
    min_cost = float('inf')
    
    # Try all subsets of vertices that include all critical languages
    for r in range(t, n + 1):
        for vertices in combinations(range(n), r):
            if all(c in vertices for c in critical):
                # Build subgraph induced by these vertices
                sub_edges = [(w, u, v) for (w, u, v) in edges if u in vertices and v in vertices]
                
                # Find MST of this subgraph
                vertex_map = {v: i for i, v in enumerate(vertices)}
                remapped_edges = [(w, vertex_map[u], vertex_map[v]) for (w, u, v) in sub_edges]
                
                parent = list(range(len(vertices)))
                rank = [0] * len(vertices)
                cost = 0
                connected_components = len(vertices)
                
                for w, u, v in sorted(remapped_edges):
                    if union(parent, rank, u, v):
                        cost += w
                        connected_components -= 1
                        if connected_components == 1:
                            break
                
                if connected_components == 1:
                    min_cost = min(min_cost, cost)
    
    print(min_cost)

solve()