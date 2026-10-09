import sys
import heapq
from collections import defaultdict

def read_input():
    n, m, k, B = map(int, sys.stdin.readline().split())
    licensed = set(map(int, sys.stdin.readline().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    return n, m, k, B, licensed, edges

def find_mst_with_constraints(n, edges, licensed):
    # We want to find a set of edges to remove such that 
    # the licensed nodes are in different components
    
    # This is equivalent to finding a spanning forest where
    # each licensed node is in its own tree
    
    # But we want to minimize the total weight of removed edges
    
    # Let's think differently: 
    # We want to make sure that no two licensed nodes are connected
    # So we can treat each licensed node as a "terminal"
    # And we want to separate all terminals from each other
    
    # This is similar to a multiway cut problem, but let's approach it differently
    
    # Let's use the fact that we want to disconnect all pairs of licensed nodes
    # One way is to find a minimum weight set of edges whose removal disconnects
    # all pairs of licensed nodes
    
    # But this might be complex. Let's try a greedy approach:
    # Build a MST of the whole graph, then remove the cheapest edges that 
    # connect different licensed nodes until they're disconnected
    
    # Actually, let's think of it as: we want to find a set of edges to remove
    # such that in the remaining graph, no two vertices in 'licensed' are connected
    
    # This is the minimum multiway cut problem for the set 'licensed'
    # Which is NP-hard in general, but let's see if we can solve it for this case
    
    # Alternative simpler approach:
    # Try to build a maximum spanning tree (to keep expensive edges)
    # But ensure that no edge connecting two different licensed components is kept
    
    # Let's model this as a graph contraction problem:
    # 1. Initially, each node is in its own component
    # 2. For each licensed node, mark its component as "licensed"
    # 3. Process edges in order of decreasing weight
    # 4. When processing an edge (u,v):
    #    - If u and v are in same component, skip
    #    - If both components are licensed, don't merge (this would connect licensed nodes)
    #    - Otherwise, merge the components
    
    # But we want to MINIMIZE the cost of edges we REMOVE
    # So we want to MAXIMIZE the cost of edges we KEEP
    
    # Let's sort edges by weight descending
    edges.sort(reverse=True)
    
    # Union-Find data structure
    parent = list(range(n + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    # Keep track of which components contain licensed nodes
    component_licensed = [set() for _ in range(n + 1)]
    for node in licensed:
        component_licensed[node].add(node)
    
    kept_edges = []
    
    for w, u, v in edges:
        pu, pv = find(u), find(v)
        if pu == pv:
            continue
            
        # Check if merging these components would connect two licensed components
        licensed_in_u = bool(component_licensed[pu])
        licensed_in_v = bool(component_licensed[pv])
        
        if licensed_in_u and licensed_in_v:
            # This edge connects two components that each contain licensed nodes
            # Don't include this edge (i.e., we'll remove it)
            continue
        else:
            # Safe to merge
            if union(u, v):
                kept_edges.append((w, u, v))
                # Update the licensed info for the new component
                new_p = find(u)
                component_licensed[new_p] = component_licensed[pu] | component_licensed[pv]
    
    # Edges not kept are the ones we need to remove
    kept_set = set((min(u,v), max(u,v)) for _, u, v in kept_edges)
    all_edges_set = set((min(u,v), max(u,v), w) for w, u, v in edges)
    
    removed_edges = []
    total_cost = 0
    
    for w, u, v in edges:
        key = (min(u, v), max(u, v))
        if key not in kept_set:
            removed_edges.append((u, v))
            total_cost += w
    
    return total_cost, removed_edges

def solve():
    n, m, k, B, licensed, edges = read_input()
    
    if k <= 1:
        # If there's at most one licensed company, nothing to separate
        print("YES")
        print(0)
        return
    
    # We want to find minimum cost set of edges to remove such that
    # no two nodes in 'licensed' are in the same component
    
    # This is the minimum multiway cut problem
    
    # Let's reduce this to a series of min-cut problems
    # For each pair of licensed nodes, we could separate them,
    # but that's not quite right either
    
    # Better approach: Use a greedy algorithm based on Kruskal's
    # But modified to avoid connecting licensed components
    
    # Sort edges by weight ascending (we want to remove light edges when needed)
    edges_with_index = [(w, u, v, i) for i, (w, u, v) in enumerate(edges)]
    edges_with_index.sort()
    
    # Union-find
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if size[px] < size[py]:
            px, py = py, px
        parent[py] = px
        size[px] += size[py]
        return True
    
    # Track which components contain licensed nodes
    component_has_licensed = [False] * (n + 1)
    for node in licensed:
        component_has_licensed[node] = True
    
    # We'll process edges and decide whether to keep or remove them
    # We want to keep as many high-weight edges as possible while ensuring
    # no two licensed nodes are connected
    
    # Sort edges by weight descending (keep heavy edges if safe)
    edges_desc = [(w, u, v) for w, u, v in edges]
    edges_desc.sort(reverse=True)
    
    # Reset Union-Find
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    component_licensed_count = [0] * (n + 1)
    for node in licensed:
        component_licensed_count[node] = 1
        
    kept_edges = []
    
    for w, u, v in edges_desc:
        pu, pv = find(u), find(v)
        if pu == pv:
            continue
            
        # Count licensed nodes in each component
        licensed_u = component_licensed_count[pu]
        licensed_v = component_licensed_count[pv]
        
        # If merging would put two licensed nodes in same component, skip
        if licensed_u > 0 and licensed_v > 0:
            # This edge connects two components that each have licensed nodes
            # Removing it helps separate them, so we don't add it to kept edges
            continue
        else:
            # Safe to merge
            if union(u, v):
                kept_edges.append((w, u, v))
                # Update licensed count
                new_root = find(u)
                component_licensed_count[new_root] = licensed_u + licensed_v
    
    # Calculate which edges were removed and their total cost
    kept_edge_set = set()
    for w, u, v in kept_edges:
        key = tuple(sorted([u, v]))
        kept_edge_set.add(key)
    
    all_edge_set = set()
    for w, u, v in edges:
        key = tuple(sorted([u, v]))
        all_edge_set.add((key, w))
    
    removed = []
    total_cost = 0
    for key, w in all_edge_set:
        if key not in kept_edge_set:
            u, v = key
            removed.append((u, v))
            total_cost += w
    
    if total_cost <= B:
        print("YES")
        print(len(removed))
        for u, v in removed:
            print(u, v)
    else:
        print("NO")

solve()