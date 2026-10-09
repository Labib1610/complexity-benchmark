import sys
from collections import defaultdict
import heapq

def find_mst_with_target(n, edges, target_set):
    if len(target_set) <= 1:
        return 0
    
    # Create a graph where vertices are target nodes and we want to connect them
    # We'll use a modified Kruskal's algorithm or Prim's algorithm
    
    # Since we need to span the target nodes, we can think of this as finding 
    # the minimum cost to connect all target nodes in the graph formed by the vectors
    # This is essentially a Steiner tree problem, but we can solve it using Union-Find
    
    # Let's use a modified Kruskal approach:
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Union-Find data structure
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # Convert target_set to a set for faster lookup
    target_nodes = set(target_set)
    
    # Count how many target nodes are connected
    connected_targets = set()
    total_cost = 0
    
    # Run Kruskal's algorithm but only count connections between target nodes
    for u, v, w in edges:
        if union(u, v):
            # Check if this edge connects target nodes or helps connect them
            # We continue until all target nodes are in the same component
            
            # Check if both nodes are targets
            pu = find(u)
            
            # Add nodes to connected set if they become part of connected component
            targets_in_component = set()
            for node in target_nodes:
                if find(node) == pu or find(node) == find(u) or find(node) == find(v):
                    targets_in_component.add(node)
            
            total_cost += w
            
            # Check if all targets are connected
            components = set()
            for node in target_nodes:
                components.add(find(node))
            
            if len(components) == 1:
                break
    
    # Better approach: Use Prim's algorithm on the induced subgraph of target nodes
    # But let's think differently:
    # The key insight is that we want to make sure all target nodes are in the same component
    # So we run Kruskal's and stop when all target nodes are connected
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    total_cost = 0
    target_components = len(target_set)
    
    for u, v, w in edges:
        if find(u) != find(v):
            if union(u, v):
                # Check if we just connected two components that contained target nodes
                old_count = 0
                if find(u) in [find(t) for t in target_set] or u in target_set:
                    old_count += 1
                if find(v) in [find(t) for t in target_set] or v in target_set:
                    old_count += 1
                        
                total_cost += w
                
                # Check if all target nodes are now connected
                target_roots = set()
                for t in target_set:
                    target_roots.add(find(t))
                
                if len(target_roots) == 1:
                    return total_cost
    
    # Actually, let's reframe the problem:
    # We want the minimum spanning tree that connects all target nodes
    # This is a Steiner tree problem which is NP-hard in general
    # However, we can solve it optimally using the following approach:
    # Build a complete graph on target nodes where edge weights are shortest paths
    # Then find MST of this complete graph
    
    # But there's a simpler way for this specific case:
    # Since we're working in R^n with difference vectors e_u - e_v,
    # the constraint is that e_a - e_b should be in the span for all a,b in T
    # This means all {e_t | t in T} should be in the same affine subspace
    
    # The dimension of the space spanned by {e_t1, ..., e_tk} restricted to our chosen vectors
    # has codimension 1 in the full space (since we start with m=n-1 vectors of rank n-1)
    
    # Simpler approach: Use Union-Find to track when all target nodes become connected
    parent = list(range(n + 1))
    
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
    
    total_cost = 0
    target_count = {i: 0 for i in range(1, n+1)}
    for t in target_set:
        target_count[t] = 1
    
    # Count how many target nodes are in each component
    component_targets = [0] * (n + 1)
    for t in target_set:
        component_targets[t] = 1
    
    connected_target_nodes = 1  # Start with first target node
    
    for u, v, w in edges:
        pu, pv = find(u), find(v)
        if pu != pv:
            # Connect the components
            parent[pu] = pv
            # Update target count in the new component
            component_targets[pv] += component_targets[pu]
            
            # If this edge connects components with target nodes, add its cost
            if component_targets[pu] > 0 and component_targets[pv] > component_targets[pu]:
                total_cost += w
            elif component_targets[pu] > 0:
                total_cost += w
                
            # Check if all target nodes are now connected
            root = find(target_set[0])
            all_connected = True
            for t in target_set:
                if find(t) != root:
                    all_connected = False
                    break
            
            if all_connected:
                return total_cost
    
    return total_cost

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
    
    target_set = []
    for _ in range(t):
        target_set.append(int(data[idx]))
        idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # Use Union-Find based approach for the Steiner tree
    parent = list(range(n + 1))
    
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
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    total_cost = 0
    
    for u, v, w in edges:
        if union(u, v):
            total_cost += w
            # Check if all targets are connected
            roots = set(find(t) for t in target_set)
            if len(roots) == 1:
                print(total_cost)
                return
    
    print(total_cost)

if __name__ == "__main__":
    main()