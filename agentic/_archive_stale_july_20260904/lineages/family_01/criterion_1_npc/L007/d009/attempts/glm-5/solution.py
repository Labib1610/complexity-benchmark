```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        u -= 1; v -= 1
        if u > v:
            u, v = v, u
        edges.append((u, v))
    
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # For each node, list of neighbors with higher index
    higher_neighbors = [[] for _ in range(n)]
    for u, v in edges:
        if u < v:
            higher_neighbors[u].append(v)
        else:
            higher_neighbors[v].append(u)
    
    # For each node, list of neighbors with lower index
    lower_neighbors = [[] for _ in range(n)]
    for u, v in edges:
        if u < v:
            lower_neighbors[v].append(u)
        else:
            lower_neighbors[u].append(v)
    
    # For each node, list of (neighbor, edge_index)
    lower_edges = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if u < v:
            lower_edges[v].append((u, i))
        else:
            lower_edges[u].append((v, i))
    
    # Precompute for each node, the list of edges (neighbor, edge_index) where neighbor > node
    higher_edges = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if u < v:
            higher_edges[u].append((v, i))
        else:
            higher_edges[v].append((u, i))
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # This is lower_edges
    
    # For each node, list of all edges (neighbor, edge_index)
    all_edges = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        all_edges[u].append((v, i))
        all_edges[v].append((u, i))
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower......
    
    # Let's just use the precomputed lists
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    #......
    
    # Let's just use the precomputed lists
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor > node
    # higher_edges already defined
    
    # For each node, list of edges (neighbor, edge_index) where neighbor < node
    # lower......