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

def kruskal(n, edges, must_connect):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cost = 0
    connected = set()
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    for u, v, w in edges:
        if union(parent, rank, u, v):
            cost += w
            connected.add(u)
            connected.add(v)
            # Check if all must_connect nodes are in the same component
            if must_connect.issubset(connected):
                root = find(parent, next(iter(must_connect)))
                if all(find(parent, node) == root for node in must_connect):
                    return cost
    
    return cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
    
    # Try all possible subsets of nodes that include all critical nodes
    # This is not efficient, so we use a different approach
    
    # We use Kruskal's algorithm to find the minimum spanning tree
    # that connects all critical nodes
    
    min_cost = float('inf')
    
    # Since t <= 10, we can try all possible ways to connect them
    # But a better approach is to realize this is a Steiner tree problem
    # We can solve it by trying all possible ways to connect the critical nodes
    
    # For small t, we can use dynamic programming with bitmasks
    # But for this problem, we can use the fact that we just need to connect
    # all critical nodes, so we can use Kruskal and stop when all are connected
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cost = 0
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    connected_critical = set()
    
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            cost += w
            # Check how many critical nodes are now connected
            roots = set()
            for c in critical:
                roots.add(find(parent, c))
            if len(roots) == 1:  # All critical nodes are connected
                min_cost = min(min_cost, cost)
                break
    
    print(min_cost if min_cost != float('inf') else 0)

solve()