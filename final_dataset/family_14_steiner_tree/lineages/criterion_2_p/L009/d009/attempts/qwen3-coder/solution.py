import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    N, E, F = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    if F <= 1:
        print(0)
        return
    
    # We need to find the minimum spanning tree such that all critical nodes are connected
    # This is equivalent to finding the MST of the graph induced by the critical nodes
    # and the edges that connect them
    
    # Since the whole space has dimension N-1 and we have E=N-1 edges forming a spanning tree,
    # we can think of this as a tree where each edge corresponds to a shift vector e_u - e_v
    
    # The condition is that for any two critical coordinates x,y, e_x - e_y should be in the span
    # This means that in the graph formed by selected edges, all critical nodes must be connected
    
    # So we want the minimum cost subset of edges such that all critical nodes are connected
    # This is the Minimum Spanning Tree of the subgraph induced by critical nodes
    
    # But since we're dealing with a tree on N nodes with N-1 edges, and we want to connect F critical nodes,
    # we need to find the minimum cost to connect these F nodes in the tree
    
    # Approach:
    # Build a graph with only critical nodes and find the MST that connects all of them
    # However, since the original graph is a tree, we can do the following:
    # For each pair of critical nodes, the path between them in the tree must be included
    # But we want the minimal cost to ensure all critical nodes are connected
    
    # Better approach:
    # Use Union-Find to find the minimum cost to connect all critical nodes
    # Sort edges by weight and use Kruskal's algorithm but only to connect critical nodes
    
    edges.sort()
    
    parent = list(range(N + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[px] = py
        return True
    
    # First, let's see which critical nodes are already connected by processing edges
    # But we need to make sure all critical nodes are in the same component
    
    # Actually, since we have a tree structure (E = N-1 edges connecting N nodes),
    # and we want to connect F critical nodes, we need F-1 edges
    
    # Let's build a graph and find the MST that spans all critical nodes
    
    # We'll use a modified Kruskal's algorithm:
    # Process edges in increasing order of weight
    # For each edge, if it connects two different components and at least one component contains a critical node,
    # we add the edge
    
    # Actually, simpler:
    # We want to connect all critical nodes with minimum cost
    # This is exactly the Steiner tree problem on a tree, which can be solved optimally
    
    # Since the input graph is a tree, we can solve this efficiently:
    # 1. Root the tree at any node
    # 2. Find the subtree that contains all critical nodes
    # 3. The edges in this subtree form the minimum cost connection
    
    # Even simpler approach:
    # In a tree, to connect k nodes, we need exactly k-1 edges
    # And the minimum cost way is to take the edges on the paths between them
    # But we need to avoid double-counting
    
    # Best approach:
    # Use Union-Find with Kruskal's algorithm
    # Only process edges until all critical nodes are connected
    
    total_cost = 0
    connected_components = F
    critical_list = list(critical)
    
    # Initially, each critical node is its own component
    crit_parent = {c: c for c in critical}
    
    def find_crit(x):
        if crit_parent[x] != x:
            crit_parent[x] = find_crit(crit_parent[x])
        return crit_parent[x]
    
    def union_crit(x, y):
        nonlocal connected_components
        px, py = find_crit(x), find_crit(y)
        if px == py:
            return False
        crit_parent[px] = py
        connected_components -= 1
        return True
    
    # Create a mapping from node to whether it's critical
    is_critical = [False] * (N + 1)
    for c in critical:
        is_critical[c] = True
        
    # We need to track which components contain critical nodes
    comp_has_critical = {}
    comp_nodes = {}
    
    # Initialize each node as its own component
    for i in range(1, N + 1):
        comp_has_critical[i] = is_critical[i]
        comp_nodes[i] = [i]
        
    parent_comp = list(range(N + 1))
    
    def find_comp(x):
        if parent_comp[x] != x:
            parent_comp[x] = find_comp(parent_comp[x])
        return parent_comp[x]
    
    def union_comp(x, y, cost):
        nonlocal total_cost
        px, py = find_comp(x), find_comp(y)
        if px == py:
            return
        # Merge smaller into larger for efficiency
        if len(comp_nodes[px]) < len(comp_nodes[py]):
            px, py = py, px
            
        parent_comp[py] = px
        # Check if we're connecting two components that together have critical nodes
        if comp_has_critical[px] or comp_has_critical[py]:
            comp_has_critical[px] = comp_has_critical[px] or comp_has_critical[py]
            total_cost += cost
            
        # Move all nodes from py to px
        comp_nodes[px].extend(comp_nodes[py])
        comp_nodes[py] = []
    
    # Sort edges by weight
    edges.sort()
    
    # Run Kruskal's algorithm
    for w, u, v in edges:
        union_comp(u, v, w)
        
    print(total_cost)

threading.Thread(target=main).start()