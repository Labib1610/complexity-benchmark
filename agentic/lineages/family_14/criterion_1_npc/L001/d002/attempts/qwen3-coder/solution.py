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
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    cost = 0
    connected_components = n
    
    for u, v, w in edges:
        if union(parent, rank, u, v):
            cost += w
            connected_components -= 1
            if connected_components == 1:
                break
    
    # Check if all must_connect nodes are in the same component
    if len(must_connect) <= 1:
        return 0
        
    root = find(parent, must_connect[0])
    for node in must_connect[1:]:
        if find(parent, node) != root:
            return float('inf')  # Not all connected
            
    return cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    core_banks = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
        
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
    
    # Try all possible ways to connect the core banks
    # We'll use a greedy approach with Kruskal's algorithm
    
    # First, let's see what's the minimum cost to connect all core banks
    # We can do this by running Kruskal but only caring about connecting core banks
    
    # But actually, we need to find the minimum spanning tree that connects all core banks
    # This is a Steiner tree problem, which is NP-hard in general
    # However, since t <= 10, we can try all possible subsets of edges
    
    # Better approach: 
    # 1. Use Kruskal's algorithm to find MST of the entire graph
    # 2. Check if this connects all core banks
    # 3. If not, we need to find the minimum way to connect them
    
    # Actually, let's think differently:
    # We want the minimum cost to make all core banks in the same component
    # So we can:
    # 1. Try Kruskal's algorithm on all edges - this gives us the MST
    # 2. Check if all core banks are connected in this MST
    # 3. If yes, we're done
    # 4. If no, we need to find the minimum way to connect the components containing core banks
    
    # Let's implement a cleaner solution:
    # Run Kruskal's algorithm and see which core banks end up in the same components
    # Then find minimum cost to connect those components
    
    # Simple approach: just run Kruskal and check
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    total_cost = 0
    for u, v, w in edges_sorted:
        if union(parent, rank, u, v):
            total_cost += w
    
    # Now check if all core banks have the same root
    roots = set()
    for bank in core_banks:
        roots.add(find(parent, bank))
        
    if len(roots) == 1:
        print(total_cost)
        return
    
    # If they're not all connected, we need to find the minimum cost to connect them
    # Let's try a different approach: bitmask DP or trying small cases
    
    # Since t <= 10, we can consider all possible ways to connect the core banks
    # But that's still complex. Let's think of it as finding minimum cost to make
    # all core banks connected.
    
    # Key insight: we want to find the minimum cost forest that connects all core banks
    # This is exactly the Steiner tree problem.
    
    # For small t, we can solve it by:
    # 1. Precomputing shortest paths between all pairs
    # 2. Using dynamic programming with bitmasks
    
    # Compute all-pairs shortest paths
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
    
    # Now we have distances between all pairs
    # Create a complete graph on core banks with these distances
    # And find the minimum spanning tree of this graph
    
    if t == 1:
        print(0)
        return
    
    # For t core banks, we need t-1 edges to connect them all
    # We can model this as finding the MST of the metric closure
    # But actually, we just need the minimum cost to connect all core banks
    
    # Use Prim's algorithm on the complete graph induced by core banks
    core_dist = [[INF] * t for _ in range(t)]
    for i in range(t):
        for j in range(t):
            if i != j:
                core_dist[i][j] = dist[core_banks[i]][core_banks[j]]
    
    # Prim's algorithm
    in_tree = [False] * t
    min_edge = [INF] * t
    min_edge[0] = 0
    total_cost = 0
    
    for _ in range(t):
        # Find vertex with minimum edge weight not yet in tree
        u = -1
        for v in range(t):
            if not in_tree[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
                
        in_tree[u] = True
        total_cost += min_edge[u]
        
        # Update weights
        for v in range(t):
            if not in_tree[v]:
                min_edge[v] = min(min_edge[v], core_dist[u][v])
    
    print(total_cost)

solve()