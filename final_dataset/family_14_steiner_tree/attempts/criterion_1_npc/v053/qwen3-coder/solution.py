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

def kruskal(nodes, edges):
    parent = list(range(nodes + 1))
    rank = [0] * (nodes + 1)
    total_cost = 0
    edge_count = 0
    
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if union(parent, rank, u, v):
            total_cost += w
            edge_count += 1
            if edge_count == nodes - 1:
                break
                
    return total_cost

def main():
    n, m, t = map(int, sys.stdin.readline().split())
    primary = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
        
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
    
    # Create a complete graph of primary nodes with shortest path weights
    # Using Floyd-Warshall to find shortest paths between all pairs
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    # Floyd-Warshall algorithm
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Create edges between primary nodes with shortest distances
    primary_edges = []
    for i in range(len(primary)):
        for j in range(i + 1, len(primary)):
            u, v = primary[i], primary[j]
            if dist[u][v] < INF:
                primary_edges.append((u, v, dist[u][v]))
    
    # Now run Kruskal's algorithm on this complete graph of primary nodes
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    total_cost = 0
    edge_count = 0
    
    for u, v, w in sorted(primary_edges, key=lambda x: x[2]):
        if union(parent, rank, u, v):
            total_cost += w
            edge_count += 1
            if edge_count == len(primary) - 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    main()