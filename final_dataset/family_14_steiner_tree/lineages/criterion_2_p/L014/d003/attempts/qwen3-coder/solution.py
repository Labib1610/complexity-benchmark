import sys
from collections import defaultdict
import heapq

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

def main():
    n, m, t = map(int, sys.stdin.readline().split())
    patent_holders = set(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # We need to connect all patent holders
    # We can use a modified Kruskal's algorithm
    # We'll keep track of which patent holders are connected
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Initially, each patent holder is in its own group
    patent_groups = {p: p for p in patent_holders}
    
    total_cost = 0
    
    for w, u, v in edges:
        # Check if u and v are already in the same component
        if find(parent, u) == find(parent, v):
            continue
            
        # Union the components
        union(parent, rank, u, v)
        
        # Update patent holder groups
        # Find which patent holders are in the components of u and v
        patents_in_u = []
        patents_in_v = []
        
        for p in patent_holders:
            if find(parent, p) == find(parent, u):
                patents_in_u.append(p)
            elif find(parent, p) == find(parent, v):
                patents_in_v.append(p)
        
        # If we connected two groups that both contain patent holders,
        # we need to pay for this edge
        if patents_in_u and patents_in_v:
            total_cost += w
            # Now all patent holders in both groups are connected
            # We can merge their groups
            root = patents_in_u[0]
            for p in patents_in_v:
                patent_groups[p] = root
        elif patents_in_u or patents_in_v:
            # Only one group has patent holders, just update the group
            pass
            
        # Check if all patent holders are in the same group
        group_roots = set(find(parent, p) for p in patent_holders)
        if len(group_roots) == 1:
            break
    
    print(total_cost)

if __name__ == "__main__":
    main()