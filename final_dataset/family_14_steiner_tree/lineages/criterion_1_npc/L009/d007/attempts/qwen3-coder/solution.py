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
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cost = 0
    edges.sort()
    
    for w, u, v in edges:
        if union(parent, rank, u, v):
            cost += w
            must_connect.discard(u)
            must_connect.discard(v)
            if not must_connect:
                break
    
    return cost if not must_connect else float('inf')

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    targets = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # Try all possible ways to connect the targets
    min_cost = float('inf')
    
    # We need to ensure all targets are in the same connected component
    # This is equivalent to connecting all targets together
    # We can use a spanning tree approach on the target nodes
    
    # Generate all possible connections between targets and find minimum cost
    target_set = set(targets)
    
    # Use Kruskal's algorithm variant - we want to connect all targets
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    edges.sort()
    
    cost = 0
    connected_targets = {targets[0]}
    remaining_targets = set(targets[1:])
    
    # We need to connect all targets in the same component
    while remaining_targets:
        best_edge = None
        best_cost = float('inf')
        
        # Find the cheapest edge that connects a new target to existing connected component
        for w, u, v in edges:
            if w >= best_cost:
                continue
                
            # Check if this edge connects a target in connected_targets to one in remaining_targets
            pu, pv = find(parent, u), find(parent, v)
            
            u_is_target = u in target_set
            v_is_target = v in target_set
            u_connected = u in connected_targets
            v_connected = v in connected_targets
            
            # Case 1: u connected target, v unconnected target
            if u_connected and v_is_target and v not in connected_targets:
                best_edge = (w, u, v)
                best_cost = w
            # Case 2: v connected target, u unconnected target  
            elif v_connected and u_is_target and u not in connected_targets:
                best_edge = (w, u, v)
                best_cost = w
            # Case 3: u connected target, v non-target that helps connect to unconnected target
            elif u_connected and not v_is_target and find(parent, v) != pu:
                # Check if adding this helps connect a remaining target
                for target in remaining_targets:
                    if find(parent, target) == pv:
                        best_edge = (w, u, v)
                        best_cost = w
                        break
            # Case 4: v connected target, u non-target that helps connect to unconnected target
            elif v_connected and not u_is_target and find(parent, u) != pv:
                # Check if adding this helps connect a remaining target
                for target in remaining_targets:
                    if find(parent, target) == pu:
                        best_edge = (w, u, v)
                        best_cost = w
                        break
        
        if best_edge is None:
            break
            
        w, u, v = best_edge
        cost += w
        union(parent, rank, u, v)
        
        # Update which targets are now connected
        newly_connected = set()
        for target in remaining_targets:
            if find(parent, target) == find(parent, targets[0]):
                newly_connected.add(target)
        connected_targets.update(newly_connected)
        remaining_targets -= newly_connected
    
    print(cost)

solve()