import sys
from itertools import combinations
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

def kruskal(n, edges, must_connect):
    parent = list(range(n))
    rank = [0] * n
    cost = 0
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if union(parent, rank, u, v):
            cost += w
            must_connect.discard((min(u, v), max(u, v)))
            if not must_connect:
                break
    return cost if not must_connect else float('inf')

def connected_components(n, edges):
    parent = list(range(n))
    rank = [0] * n
    for u, v, _ in edges:
        union(parent, rank, u, v)
    components = defaultdict(set)
    for i in range(n):
        components[find(parent, i)].add(i)
    return list(components.values())

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    priorities = list(map(int, sys.stdin.readline().split()))
    priorities = [p - 1 for p in priorities]  # Convert to 0-indexed
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u - 1, v - 1, w))  # Convert to 0-indexed
    
    if t <= 1:
        return 0
    
    # Try all possible ways to connect the priority points
    min_cost = float('inf')
    
    # Generate all possible partitions of priority points
    # For each partition, we need to connect points within each group
    # We'll use a brute-force approach for small t
    
    # Check all subsets of edges
    for i in range(1 << m):
        selected_edges = [edges[j] for j in range(m) if (i & (1 << j))]
        
        # Find connected components
        components = connected_components(n, selected_edges)
        
        # Check if all priority points are in the same component
        priority_component = None
        valid = True
        for component in components:
            intersection = component.intersection(priorities)
            if intersection:
                if priority_component is None:
                    priority_component = component
                elif priority_component != component:
                    valid = False
                    break
        
        if valid and (priority_component is not None and len(priority_component.intersection(set(priorities))) == t):
            cost = sum(w for _, _, w in selected_edges)
            min_cost = min(min_cost, cost)
        elif valid and priority_component is None and t == 0:
            cost = sum(w for _, _, w in selected_edges)
            min_cost = min(min_cost, cost)
    
    # More efficient approach using MST with constraints
    # We need all priority points to be connected
    # This is equivalent to finding a minimum spanning tree that connects all priority points
    
    # Use a different approach: try all possible ways to connect priority points
    # and then add minimum edges to connect everything
    
    # But let's think differently. We want the minimum cost to make all priority points
    # in the same connected component.
    
    # We can use the fact that we need to connect all priority points,
    # which forms a Steiner tree problem variant. But since t is small (≤10),
    # we can try all possible ways to connect them.
    
    # Actually, let's model this properly:
    # We want to find a subset of edges such that in the resulting graph,
    # all priority vertices are in the same connected component.
    
    # This can be solved by trying all possible bipartitions of the priority vertices
    # and ensuring there's at least one edge crossing each bipartition in our solution.
    # But that's complex.
    
    # Simpler approach: since t is small, we can check all 2^m subsets for small m,
    # but for larger m, we need something better.
    
    # Let's go back to the MST idea:
    # We want to connect all priority points. So we can:
    # 1. Create a complete graph on priority points where edge weights are shortest path distances
    # 2. Find MST of this graph
    # 3. Take the corresponding edges from original graph
    
    # But even simpler for implementation here:
    # Since the constraints allow it, let's do a proper subset enumeration with pruning
    
    if m <= 20:
        # Brute force over subsets
        min_cost = float('inf')
        for mask in range(1 << m):
            selected_edges = [edges[i] for i in range(m) if mask & (1 << i)]
            # Check if all priorities are connected
            parent = list(range(n))
            rank = [0] * n
            for u, v, _ in selected_edges:
                union(parent, rank, u, v)
            
            # Check if all priority points have the same root
            roots = set(find(parent, p) for p in priorities)
            if len(roots) == 1:
                cost = sum(w for _, _, w in selected_edges)
                min_cost = min(min_cost, cost)
        
        return min_cost
    
    else:
        # For larger m, we need a more sophisticated approach
        # Use dynamic programming or Prim's/Kruskal's with modifications
        
        # Let's implement Kruskal's algorithm with early termination
        min_cost = float('inf')
        
        # Sort edges by weight
        edges.sort(key=lambda x: x[2])
        
        # Try to build MST that connects all priority nodes
        for start in range(m):
            parent = list(range(n))
            rank = [0] * n
            cost = 0
            connected_priorities = {priorities[0]}  # Start with first priority node
            
            # First, add edges from 'start' onwards until all priorities connected
            for i in range(start, m):
                u, v, w = edges[i]
                pu, pv = find(parent, u), find(parent, v)
                
                if pu != pv:
                    # Union the sets
                    if rank[pu] < rank[pv]:
                        pu, pv = pv, pu
                    parent[pv] = pu
                    if rank[pu] == rank[pv]:
                        rank[pu] += 1
                    
                    cost += w
                    
                    # Update connected priorities
                    if u in priorities or v in priorities:
                        if u in priorities:
                            connected_priorities.add(u)
                        if v in priorities:
                            connected_priorities.add(v)
                    
                    # Check if all priorities are now connected
                    all_same_component = True
                    first_root = find(parent, priorities[0])
                    for p in priorities[1:]:
                        if find(parent, p) != first_root:
                            all_same_component = False
                            break
                    
                    if all_same_component:
                        min_cost = min(min_cost, cost)
                        break
        
        return min_cost

print(solve())