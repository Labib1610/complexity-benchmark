import sys
from itertools import product

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    hubs = [int(next(it))-1 for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        w = int(next(it))
        edges.append((u,v,w))
    
    if k == 1:
        print("YES")
        print(0)
        return
    
    # If k > n, impossible? Actually k <= n always.
    # We'll brute force assignment of each node to one of k hubs.
    # But hubs must be in their own group.
    # So we fix hub i to group i.
    # For non-hub nodes, try all k^n assignments.
    
    non_hub = [i for i in range(n) if i not in hubs]
    hub_set = set(hubs)
    
    best_cost = B+1
    best_assignment = None
    
    # Precompute hub index for each hub
    hub_idx = {h:i for i,h in enumerate(hubs)}
    
    # For each assignment of non-hub nodes to groups 0..k-1
    for assign in product(range(k), repeat=len(non_hub)):
        group = [-1]*n
        for i,h in enumerate(hubs):
            group[h] = i
        for idx, node in enumerate(non_hub):
            group[node] = assign[idx]
        
        # Compute cut cost
        cost = 0
        cut_edges = []
        for u,v,w in edges:
            if group[u] != group[v]:
                cost += w
                cut_edges.append((u,v))
                if cost > B:
                    break
        if cost <= B and cost < best_cost:
            best_cost = cost
            best_assignment = (group, cut_edges)
    
    if best_assignment is None:
        print("NO")
    else:
        group, cut_edges = best_assignment
        print("YES")
        print(len(cut_edges))
        for u,v in cut_edges:
            print(u+1, v+1)

if __name__ == "__main__":
    solve()