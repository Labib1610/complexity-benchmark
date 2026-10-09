import sys
import heapq
from collections import defaultdict

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

def kruskal(n, edges, required):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    cost = 0
    connected = len(required)
    
    for u, v, w in edges:
        if union(parent, rank, u, v):
            cost += w
            # Check if all required nodes are connected
            components = {}
            for node in required:
                root = find(parent, node)
                if root not in components:
                    components[root] = []
                components[root].append(node)
            
            if len(components) == 1 and len(list(components.values())[0]) == len(required):
                return cost
    
    return cost

def solve():
    n, m, t = map(int, input().split())
    required = list(map(int, input().split()))
    
    # If there's only one required site, no cabling needed
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    
    # Use Kruskal's algorithm to find minimum spanning tree for required nodes
    result = kruskal(n, edges, required)
    print(result)

solve()