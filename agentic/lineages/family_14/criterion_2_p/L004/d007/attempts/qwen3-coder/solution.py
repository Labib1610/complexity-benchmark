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
    
    # Sort edges by weight
    edges.sort()
    
    # We need to connect all critical nodes with minimum cost
    # This is essentially finding the minimum spanning tree that connects all critical nodes
    # We can use a modified Kruskal's algorithm
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    cost = 0
    connected_critical = 1  # We start with one critical node in the component
    first_critical = next(iter(critical))
    connected_component = {first_critical}
    
    for w, u, v in edges:
        # Check if this edge connects something new to our critical component
        u_in = u in connected_component
        v_in = v in connected_component
        
        if u_in and v_in:
            # Both already in component, skip
            continue
            
        if not u_in and not v_in:
            # Neither in component, we might add this later
            # But for now, let's see if it connects two nodes where at least one is critical
            # Actually, let's think differently
            
            # Let's use Union-Find properly
            # We want to connect all critical nodes with minimum cost
            # Run Kruskal until all critical nodes are connected
            pass
            
        # Let's restart with a cleaner approach
        pass
    
    # Cleaner approach:
    # Use Kruskal's algorithm to find MST of the subgraph that connects all critical nodes
    # But we don't need full MST, just enough to connect critical nodes
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    cost = 0
    components_with_critical = set()
    
    # Initially, each critical node is in its own component
    critical_list = list(critical)
    
    # We need to connect all critical nodes, so we need (t-1) edges
    edges_needed = t - 1
    edges_added = 0
    
    for w, u, v in edges:
        if edges_added == edges_needed:
            break
            
        pu = find(parent, u)
        pv = find(parent, v)
        
        if pu != pv:
            # Check if either component has a critical node
            # Actually, let's just do standard Kruskal but count how many critical nodes are connected
            union(parent, rank, u, v)
            cost += w
            edges_added += 1
            
            # Check if all critical nodes are now connected
            if edges_added == edges_needed:
                break
    
    # Even cleaner: we just need to connect all critical nodes
    # So we run Kruskal's algorithm until the critical nodes form one component
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    cost = 0
    critical_components = len(critical)
    
    for w, u, v in edges:
        if critical_components <= 1:
            break
            
        pu = find(parent, u)
        pv = find(parent, v)
        
        if pu != pv:
            # Check if this union connects critical nodes
            # Count how many critical nodes are in each component
            union(parent, rank, u, v)
            cost += w
            
            # We need to track how many separate critical components we have
            # This is getting complex, let's think of it as:
            # We have 't' critical nodes that need to be in the same component
            # In Union-Find terms, they should all have the same root
            # So we keep connecting until they do
            
            # Let's track the roots of critical nodes
            roots = set()
            for c in critical:
                roots.add(find(parent, c))
                
            critical_components = len(roots)
    
    print(cost)

if __name__ == "__main__":
    main()