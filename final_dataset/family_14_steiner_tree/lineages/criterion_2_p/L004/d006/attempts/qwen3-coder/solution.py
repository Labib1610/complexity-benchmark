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
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    critical = set()
    for _ in range(t):
        critical.add(int(data[idx]))
        idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # We need to find the minimum cost to connect all critical nodes
    # This is essentially finding the MST of the subgraph induced by critical nodes
    # But since we're dealing with a subset of nodes that must be connected,
    # we can use a modified Kruskal's algorithm on the entire graph but only track connections between critical nodes
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find for the entire graph
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # To track how many critical nodes are connected
    critical_parent = {}  # Maps each critical node to its representative in the Union-Find
    for c in critical:
        critical_parent[c] = c
    
    total_cost = 0
    connected_critical = len(critical)
    
    # Initially each critical node is its own component
    # We want to reduce this to 1 component
    critical_components = {c: {c} for c in critical}
    component_count = len(critical)
    
    # But actually, let's think differently:
    # We want to find the minimum cost to make all critical indices have the same value
    # In terms of graph connectivity, this means connecting all critical nodes into one component
    # So we run Kruskal's algorithm and stop when all critical nodes are connected
    
    # Reset Union-Find
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Keep track of which critical nodes are in which component
    # Map each node to its critical component representative
    crit_rep = {}
    for c in critical:
        crit_rep[c] = c
        
    components = {c: {c} for c in critical}
    
    for w, u, v in edges:
        pu = find(parent, u)
        pv = find(parent, v)
        if pu != pv:
            # Union the sets
            union(parent, rank, pu, pv)
            
            # Update critical components
            rep_u = None
            rep_v = None
            for c in critical:
                p = find(parent, c)
                if p == pu:
                    rep_u = c
                if p == pv:
                    rep_v = c
                    
            if rep_u is not None and rep_v is not None and rep_u != rep_v:
                # Merge the critical components
                # Move all elements from rep_v's component to rep_u's component
                for node in components[rep_v]:
                    crit_rep[node] = rep_u
                components[rep_u].update(components[rep_v])
                del components[rep_v]
                
                total_cost += w
                
                if len(components) == 1:
                    break
            elif rep_u is not None and rep_v is None:
                # rep_v is not a critical node, so just add v to rep_u's component if v is critical
                if v in critical:
                    crit_rep[v] = rep_u
                    components[rep_u].add(v)
            elif rep_v is not None and rep_u is None:
                # rep_u is not a critical node, so just add u to rep_v's component if u is critical
                if u in critical:
                    crit_rep[u] = rep_v
                    components[rep_v].add(u)
                    
            # Check if all critical nodes are now in one component
            if len(components) == 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    main()