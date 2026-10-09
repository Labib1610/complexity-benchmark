import sys
import heapq
from collections import defaultdict
import itertools

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
    # Create a graph with just the required connections first
    parent = list(range(n))
    rank = [0] * n
    cost = 0
    
    # First, connect all pairs in must_connect optimally
    # We'll use Kruskal's algorithm on the complete graph formed by critical nodes
    # But we only care about connecting the critical nodes
    
    # Build a mapping for critical nodes
    critical_nodes = sorted(list(must_connect))
    node_map = {node: i for i, node in enumerate(critical_nodes)}
    critical_count = len(critical_nodes)
    
    if critical_count <= 1:
        return 0
    
    # Create edges only between critical nodes using Union-Find
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    connected_components = n
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            cost += w
            connected_components -= 1
            
    # Check if all critical nodes are connected
    roots = set(find(parent, node) for node in critical_nodes)
    if len(roots) == 1:
        return cost
    else:
        return -1  # Should not happen according to problem statement

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    critical = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
        
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1, w))  # Convert to 0-indexed
    
    # Need to find minimum cost to connect all critical nodes
    # This is a Steiner Tree problem, but since t <= 10, we can try all possible ways
    
    # Map critical nodes to 0-indexed
    critical = [x - 1 for x in critical]
    
    # For small t, we can solve this more directly
    # Build a complete graph where edge weights are shortest paths
    
    # Floyd-Warshall to get all-pairs shortest paths
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Now we have distances between all pairs
    # Extract the critical nodes subgraph
    critical_dist = []
    for i in range(len(critical)):
        for j in range(i+1, len(critical)):
            u, v = critical[i], critical[j]
            critical_dist.append((u, v, dist[u][v]))
    
    # Now find MST of this complete graph on critical nodes
    parent = list(range(n))
    rank = [0] * n
    
    def find_root(x):
        if parent[x] != x:
            parent[x] = find_root(parent[x])
        return parent[x]
    
    def union_root(x, y):
        px, py = find_root(x), find_root(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # Sort edges by weight
    critical_dist.sort(key=lambda x: x[2])
    
    total_cost = 0
    connected_count = 0
    
    for u, v, w in critical_dist:
        if find_root(u) != find_root(v):
            union_root(u, v)
            total_cost += w
            connected_count += 1
            if connected_count == len(critical) - 1:
                break
    
    print(total_cost)

solve()