import sys
from itertools import product

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    
    sources = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    source_set = set(sources)
    non_sources = [i for i in range(n) if i not in source_set]
    ns_count = len(non_sources)
    
    # Precompute for each non-source node, cost to assign to each source
    # Actually we can compute cut cost directly per assignment.
    
    best_cost = float('inf')
    best_assignment = None
    
    # Try all assignments of non-source nodes to k sources
    for assign in product(range(k), repeat=ns_count):
        comp = [-1] * n
        for idx, node in enumerate(non_sources):
            comp[node] = assign[idx]
        for i, s in enumerate(sources):
            comp[s] = i
        
        cost = 0
        for u, v, w in edges:
            if comp[u] != comp[v]:
                cost += w
        if cost < best_cost:
            best_cost = cost
            best_assignment = assign
    
    if best_cost > B:
        print("NO")
        return
    
    # Build the cut edges
    comp = [-1] * n
    for idx, node in enumerate(non_sources):
        comp[node] = best_assignment[idx]
    for i, s in enumerate(sources):
        comp[s] = i
    
    cut_edges = []
    for u, v, w in edges:
        if comp[u] != comp[v]:
            cut_edges.append((u, v))
    
    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(u + 1, v + 1)

if __name__ == "__main__":
    solve()