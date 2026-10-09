import sys
import heapq
from collections import defaultdict

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

def kruskal(n, edges, must_connect):
    if len(must_connect) <= 1:
        return 0
    
    # Try all possible ways to connect the critical nodes
    # We'll use a modified Kruskal's algorithm
    min_cost = float('inf')
    
    # Since t <= 10, we can try to find the minimum spanning tree that connects all critical nodes
    # This is essentially the Steiner tree problem, but with small t we can solve it by checking
    # if all critical nodes are connected after adding edges in order of weight
    
    edges.sort(key=lambda x: x[2])
    
    # We'll use a different approach: since t is small, we can try all possible ways
    # But actually, we can just run a modified Kruskal to connect all critical components
    
    # Initially, each node is its own component
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # First, let's see which critical nodes are already connected
    critical_set = set(must_connect)
    connected_critical = []
    
    for i in range(len(must_connect)):
        connected_critical.append([must_connect[i]])
    
    cost = 0
    components = [{x} for x in must_connect]
    
    # We need to connect all critical nodes
    target_component = set(must_connect)
    
    # Create a mapping from node to its critical component index (-1 if not critical)
    node_to_component = {}
    for i, node in enumerate(must_connect):
        node_to_component[node] = i
        
    # Use Union-Find to track which critical nodes are connected
    # We'll track which "critical groups" are merged together
    critical_groups = list(range(len(must_connect)))  # Initially, each critical node is its own group
    group_size = [1] * len(must_connect)
    
    def find_critical_group(x):
        if critical_groups[x] != x:
            critical_groups[x] = find_critical_group(critical_groups[x])
        return critical_groups[x]
    
    def union_critical_groups(x, y):
        px, py = find_critical_group(x), find_critical_group(y)
        if px == py:
            return False
        if group_size[px] < group_size[py]:
            px, py = py, px
        critical_groups[py] = px
        group_size[px] += group_size[py]
        return True
    
    # Map each node to its critical index, or -1 if not critical
    node_critical_index = [-1] * (n + 1)
    for i, node in enumerate(must_connect):
        node_critical_index[node] = i
    
    # Run Kruskal's algorithm
    uf_parent = list(range(n + 1))
    uf_rank = [0] * (n + 1)
    
    total_cost = 0
    connected_groups = len(must_connect)
    
    for u, v, w in edges:
        # Find roots of u and v
        pu = find(uf_parent, u)
        pv = find(uf_parent, v)
        
        if pu != pv:
            # Get critical indices for roots if they exist
            u_critical = -1
            v_critical = -1
            
            # Find if pu or pv contains any critical node
            # For efficiency, we'll track which component each critical node is in
            # Let's rebuild the approach
            
            # Simpler approach: run Kruskal and track when all critical nodes are connected
            # Use Union-Find with tracking of critical node connectivity
            
            # Connect the components
            if uf_rank[pu] < uf_rank[pv]:
                pu, pv = pv, pu
            uf_parent[pv] = pu
            if uf_rank[pu] == uf_rank[pv]:
                uf_rank[pu] += 1
                
            # Check if this merge connects two different critical groups
            # We need to track which critical nodes are in which component
            # Let's use a different method
            
    # Let's restart with a cleaner approach
    # Use bitmasks to represent which critical nodes are connected
    # Since t <= 10, we can use dynamic programming with bitmasks
    
    # But for simplicity, let's just use the standard approach:
    # Run Kruskal's algorithm and stop when all critical nodes are connected
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Which critical nodes are in which component
    # Initially, each critical node is in its own component
    critical_component = list(range(len(must_connect)))
    for i in range(len(must_connect)):
        critical_component[i] = i
    
    def get_critical_root(idx):
        if critical_component[idx] != idx:
            critical_component[idx] = get_critical_root(critical_component[idx])
        return critical_component[idx]
    
    def merge_critical_components(idx1, idx2):
        r1 = get_critical_root(idx1)
        r2 = get_critical_root(idx2)
        if r1 != r2:
            critical_component[r2] = r1
            return True
        return False
    
    # Create mapping from node to critical index
    node_to_critical = {}
    for i, c in enumerate(must_connect):
        node_to_critical[c] = i
    
    total_cost = 0
    connected_count = 1  # We start with 1 group (any one critical node)
    
    if len(must_connect) == 1:
        return 0
    
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        pu = find(parent, u)
        pv = find(parent, v)
        
        if pu != pv:
            # Union the components
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            if rank[pu] == rank[pv]:
                rank[pu] += 1
                
            # Check if this connects two different critical groups
            cu = node_to_critical.get(u, -1)
            cv = node_to_critical.get(v, -1)
            
            # Find which critical components u and v belong to
            critical_u = -1
            critical_v = -1
            
            # Find any critical node in component of u
            def find_critical_in_component(node):
                root = find(parent, node)
                # BFS/DFS to find a critical node in this component
                visited = set()
                stack = [node]
                while stack:
                    current = stack.pop()
                    if current in node_to_critical:
                        return node_to_critical[current]
                    if current in visited:
                        continue
                    visited.add(current)
                    # Check neighbors
                    # But we don't have adjacency list...
                    # Let's precompute component representatives
                    
            # Simpler: keep track of which component each critical node is in
            comp_to_critical = {}  # component_root -> set of critical indices
            for i, c in enumerate(must_connect):
                root = find(parent, c)
                if root not in comp_to_critical:
                    comp_to_critical[root] = set()
                comp_to_critical[root].add(i)
            
            # Get roots of components being merged
            root_u = find(parent, u)
            root_v = find(parent, v)
            
            # Check if this merge connects two components that contain critical nodes
            crit_u = comp_to_critical.get(root_u, set())
            crit_v = comp_to_critical.get(root_v, set())
            
            if crit_u and crit_v and crit_u != crit_v:
                # This merge connects two groups of critical nodes
                total_cost += w
                # Merge the critical sets
                new_set = crit_u.union(crit_v)
                comp_to_critical[root_u] = new_set
                if root_v in comp_to_critical:
                    del comp_to_critical[root_v]
                
                # Check if all critical nodes are now connected
                if len(new_set) == len(must_connect):
                    return total_cost
            elif crit_u or crit_v:
                # One component has critical nodes, the other doesn't
                total_cost += w
                new_set = crit_u.union(crit_v)
                comp_to_critical[root_u] = new_set
                if root_v in comp_to_critical:
                    del comp_to_critical[root_v]
                
    return total_cost

# Read input
line = input().split()
n, m, t = int(line[0]), int(line[1]), int(line[2])

if t == 0:
    print(0)
    exit()

critical = list(map(int, input().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

print(kruskal(n, edges, critical))