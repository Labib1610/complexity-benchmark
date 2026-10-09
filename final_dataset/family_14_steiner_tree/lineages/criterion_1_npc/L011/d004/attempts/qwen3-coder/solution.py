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
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Try all possible ways to connect the must_connect vertices
    # Since t <= 10, we can try all spanning trees of the must_connect vertices
    # But a better approach is to compute the MST of the whole graph and 
    # then find the minimum cost to connect all must_connect vertices
    
    # Actually, let's think differently:
    # We want to find the minimum cost to connect all vertices in must_connect
    # This is the Steiner tree problem, which is NP-hard in general
    # But since t <= 10, we can use dynamic programming with bitmasks
    
    # However, there's an easier approach:
    # 1. Compute the MST of the entire graph
    # 2. In the MST, the cost to connect all vertices in must_connect 
    #    is the cost of the subtree that spans all of them
    # But this is still complex
    
    # Let's use the following approach:
    # Try all 2^(t-1) ways to connect the t vertices
    # For each way, compute the MST of that subset of edges
    # But this is also not straightforward
    
    # Best approach: Use the fact that we want the minimum cost to connect t vertices
    # This is exactly the minimum Steiner tree problem
    # For small t, we can solve it as follows:
    # 1. Compute all-pairs shortest paths
    # 2. Use dynamic programming with bitmasks on the t vertices
    
    # But let's think of an even simpler approach for this problem:
    # Since we're looking for the minimum cost to connect t vertices,
    # we can:
    # 1. Compute the complete graph on the t vertices where edge weights
    #    are the shortest path distances in the original graph
    # 2. Find the MST of this complete graph
    
    # First, compute all-pairs shortest paths
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Now we have shortest paths between all pairs
    # Create a complete graph on must_connect vertices
    t = len(must_connect)
    if t <= 1:
        return 0
    
    # Get all edges between must_connect vertices
    steiner_edges = []
    for i in range(t):
        for j in range(i + 1, t):
            u, v = must_connect[i], must_connect[j]
            steiner_edges.append((u, v, dist[u][v]))
    
    # Find MST of this complete graph
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    steiner_edges.sort(key=lambda x: x[2])
    
    total_cost = 0
    edges_used = 0
    
    for u, v, w in steiner_edges:
        if union(parent, rank, u, v):
            total_cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    return total_cost

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    line_idx = 0
    
    # Read n, m, t
    n, m, t = map(int, input_lines[line_idx].split())
    line_idx += 1
    
    # Read invariant variables
    must_connect = list(map(int, input_lines[line_idx].split()))
    line_idx += 1
    
    # Read edges
    edges = []
    for _ in range(m):
        u, v, w = map(int, input_lines[line_idx].split())
        edges.append((u, v, w))
        line_idx += 1
    
    # Solve
    result = kruskal(n, edges, must_connect)
    print(result)

if __name__ == "__main__":
    main()