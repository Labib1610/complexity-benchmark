import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    nL = int(input[ptr]); ptr += 1
    nR = int(input[ptr]); ptr += 1
    m = int(input[ptr]); ptr += 1
    
    ops = []
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    
    for _ in range(m):
        u = int(input[ptr]); ptr += 1
        v = int(input[ptr]); ptr += 1
        ops.append((u, v))
        deg_L[u] += 1
        deg_R[v] += 1
    
    # Calculate Delta
    max_deg = 0
    for i in range(1, nL + 1):
        if deg_L[i] > max_deg: max_deg = deg_L[i]
    for i in range(1, nR + 1):
        if deg_R[i] > max_deg: max_deg = deg_R[i]
    
    Delta = max_deg
    
    # Build bipartite graph for each cycle
    # We need to find Delta matchings
    # Using edge coloring algorithm for bipartite graphs
    
    # Adjacency lists for the bipartite graph
    adj = [[] for _ in range(nL + 1)]
    edge_idx = 0
    for u, v in ops:
        adj[u].append((v, edge_idx))
        edge_idx += 1
    
    # We'll process vertices in order of decreasing degree
    order_L = list(range(1, nL + 1))
    order_L.sort(key=lambda x: -deg_L[x])
    
    # For each vertex u in L, we'll assign colors to its edges
    # Using the greedy approach with availability tracking
    
    result = [0] * m
    
    # For each u in L, track which colors are used at u
    used_at_L = [set() for _ in range(nL + 1)]
    # For each v in R, track which colors are used at v
    used_at_R = [set() for _ in range(nR + 1)]
    
    # Process edges in order of L vertices (by decreasing degree)
    for u in order_L:
        # Get all edges from u
        edges = adj[u]
        # Sort by degree of R vertex (decreasing)
        edges.sort(key=lambda x: -deg_R[x[0]])
        
        for v, idx in edges:
            # Find available color
            used_L = used_at_L[u]
            used_R = used_at_R[v]
            
            # Find smallest available color
            color = 1
            while color in used_L or color in used_R:
                color += 1
            
            result[idx] = color
            used_L.add(color)
            used_R.add(color)
    
    print("YES")
    print(" ".join(map(str, result)))

solve()