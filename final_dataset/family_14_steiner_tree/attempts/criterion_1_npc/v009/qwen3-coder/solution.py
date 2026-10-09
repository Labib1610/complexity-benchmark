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

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    required = set(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # Create a mapping for required vertices to indices 0..t-1
    req_list = list(required)
    req_index = {v: i for i, v in enumerate(req_list)}
    t = len(req_list)
    
    # We use a modified Kruskal's algorithm approach
    # But we're really building a Steiner tree - which is NP-hard
    # However, since t is small (<= 10), we can try all possible combinations
    
    # Let's build the full graph and then find the MST that connects all required vertices
    # This is essentially the Steiner tree problem on a metric closure
    
    # First, compute all-pairs shortest paths between required vertices
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    # Initialize distances
    for i in range(n):
        dist[i][i] = 0
    
    # Add edges to adjacency matrix
    for w, u, v in edges:
        u -= 1  # Convert to 0-indexed
        v -= 1
        if dist[u][v] > w:
            dist[u][v] = dist[v][u] = w
    
    # Floyd-Warshall to get all-pairs shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Now create a complete graph on required vertices with shortest path distances
    req_edges = []
    for i in range(t):
        for j in range(i+1, t):
            u_idx = req_list[i] - 1
            v_idx = req_list[j] - 1
            req_edges.append((dist[u_idx][v_idx], i, j))
    
    # Sort these edges
    req_edges.sort()
    
    # Apply Kruskal's algorithm on this complete graph
    parent = list(range(t))
    rank = [0] * t
    total_cost = 0
    edges_used = 0
    
    for w, u, v in req_edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total_cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

solve()