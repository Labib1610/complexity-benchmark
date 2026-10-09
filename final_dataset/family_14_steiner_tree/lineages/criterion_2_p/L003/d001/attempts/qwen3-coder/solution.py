import sys
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

def kruskal(n, edges, critical_nodes):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize Union-Find structure
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Create a mapping for critical nodes to form a complete graph
    critical_set = set(critical_nodes)
    
    # First, build a MST of the entire graph
    mst_edges = []
    for u, v, w in edges:
        if union(parent, rank, u, v):
            mst_edges.append((u, v, w))
    
    # Reset Union-Find for building Steiner tree
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Now we need to find the minimum cost to connect all critical nodes
    # We'll use the fact that in the MST, we can find the minimum cost to connect critical nodes
    
    # Build adjacency list of the MST
    mst_adj = defaultdict(list)
    for u, v, w in mst_edges:
        mst_adj[u].append((v, w))
        mst_adj[v].append((u, w))
    
    # Find which nodes are needed (critical nodes and their connectors)
    # But actually, we can just run Kruskal on a graph where edge weights are 
    # distances in the original MST between critical nodes
    
    # Better approach: create a complete graph where edge weights are 
    # shortest path distances in the MST between pairs of critical nodes
    
    # For small number of critical nodes, compute pairwise distances
    if len(critical_nodes) <= 1:
        return 0
    
    # BFS/DFS to compute distances in MST between critical nodes
    def bfs_distances(start, mst_adj, critical_set):
        distances = {}
        visited = set()
        queue = [(start, 0)]
        visited.add(start)
        
        while queue:
            node, dist = queue.pop(0)
            if node in critical_set and node != start:
                distances[node] = dist
            
            for neighbor, weight in mst_adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + weight))
        
        return distances
    
    # Create a complete graph with distances as edge weights
    distance_graph = []
    critical_indices = {node: i for i, node in enumerate(critical_nodes)}
    
    # Compute pairwise distances using BFS from each critical node in MST
    pairwise_distances = {}
    for start_node in critical_nodes:
        pairwise_distances[start_node] = bfs_distances(start_node, mst_adj, critical_set)
    
    # Create edges for the complete graph of critical nodes
    complete_edges = []
    for i in range(len(critical_nodes)):
        for j in range(i + 1, len(critical_nodes)):
            u, v = critical_nodes[i], critical_nodes[j]
            if v in pairwise_distances[u]:
                complete_edges.append((u, v, pairwise_distances[u][v]))
    
    # Run Kruskal on this complete graph to get minimum cost
    complete_edges.sort(key=lambda x: x[2])
    
    # Reset Union-Find for final MST of critical nodes
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    total_cost = 0
    edges_used = 0
    
    for u, v, w in complete_edges:
        if union(parent, rank, u, v):
            total_cost += w
            edges_used += 1
            if edges_used == len(critical_nodes) - 1:
                break
    
    return total_cost

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
n, m, t = line1[0], line1[1], line1[2]

critical_nodes = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

# Solve and print result
result = kruskal(n, edges, critical_nodes)
print(result)