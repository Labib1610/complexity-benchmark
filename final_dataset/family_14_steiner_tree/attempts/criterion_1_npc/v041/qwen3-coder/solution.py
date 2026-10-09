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
    parent = list(range(n))
    rank = [0] * n
    result = 0
    edges.sort()
    for w, u, v in edges:
        if union(parent, rank, u, v):
            result += w
            if len(must_connect) <= 1:
                return result
    return result

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    primaries = list(map(int, sys.stdin.readline().split()))
    primaries = [x - 1 for x in primaries]  # Convert to 0-indexed
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u-1, v-1))  # Convert to 0-indexed
    
    # Create a new graph where we consider subsets of vertices
    # We use a Steiner tree approach: try all possible ways to connect the primary nodes
    # But since t <= 10, we can do this more efficiently
    
    # For small t, we can try to find the minimum spanning tree that connects all primary nodes
    # This is essentially a Steiner tree problem, but we can solve it by trying all possible connections
    
    # Since t is small (<=10), we can compute pairwise shortest paths between all nodes
    # and then find the MST of the complete graph on primary nodes with these distances
    
    # Floyd-Warshall to get all-pairs shortest paths
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for w, u, v in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Now create a complete graph on primary nodes with shortest path distances
    primary_edges = []
    for i in range(t):
        for j in range(i+1, t):
            u, v = primaries[i], primaries[j]
            primary_edges.append((dist[u][v], i, j))
    
    # Find MST of this complete graph
    parent = list(range(t))
    rank = [0] * t
    primary_edges.sort()
    result = 0
    for w, u, v in primary_edges:
        if union(parent, rank, u, v):
            result += w
    
    print(result)

solve()