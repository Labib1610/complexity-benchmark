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

def kruskal(n, edges, nodes):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cost = 0
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            if union(parent, rank, u, v):
                cost += w
    # Check if all required nodes are connected
    root = find(parent, next(iter(nodes)))
    for node in nodes:
        if find(parent, node) != root:
            return float('inf')
    return cost

n, m, t = map(int, sys.stdin.readline().split())
stranded = set(map(int, sys.stdin.readline().split()))
edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

if t <= 1:
    print(0)
else:
    # Try all subsets of nodes that include all stranded nodes
    min_cost = float('inf')
    # We'll use a modified approach: we want to find the minimum spanning tree
    # that connects all stranded nodes. This is essentially finding the MST
    # of the subgraph induced by the stranded nodes and potentially some
    # intermediate nodes.
    
    # Better approach: since t is small (<= 10), we can consider all possible
    # ways to connect the stranded nodes. But even better, we can use the fact
    # that the optimal solution will be a subtree of the full graph that spans
    # all the stranded nodes. This is exactly the Steiner tree problem, but
    # we can solve it by trying all possible subsets as intermediate nodes.
    
    # However, there's an easier way: since we're looking for the minimum cost
    # to connect all stranded nodes, we can run Kruskal's algorithm on the 
    # complete graph and stop when all stranded nodes are connected.
    # But that's not quite right either because we might have a cheaper way
    # going through intermediate nodes.
    
    # Let's think differently: we want the minimum spanning tree of the graph
    # such that all nodes in `stranded` are in the same component.
    # Since t <= 10, we can enumerate over all 2^(n-t) possibilities of 
    # including additional nodes, but that may still be too much.
    
    # Actually, let's reframe: we want the minimum weight subgraph that connects
    # all nodes in `stranded`. This is the Steiner Tree problem.
    # For small t, we can solve this by computing shortest paths and then 
    # finding the MST of the complete graph on the terminal nodes.
    
    # Step 1: Compute all-pairs shortest paths
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
    
    # Step 2: Create a complete graph on the stranded nodes with edge weights
    # equal to the shortest path distances
    stranded_list = list(stranded)
    k = len(stranded_list)
    mst_edges = []
    for i in range(k):
        for j in range(i + 1, k):
            u, v = stranded_list[i], stranded_list[j]
            mst_edges.append((u, v, dist[u][v]))
            
    # Step 3: Find the MST of this complete graph (this gives us the minimum
    # cost to connect all stranded nodes)
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    mst_edges.sort(key=lambda x: x[2])
    total_cost = 0
    connected_components = k
    
    for u, v, w in mst_edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total_cost += w
            connected_components -= 1
            if connected_components == 1:
                break
                
    print(total_cost)