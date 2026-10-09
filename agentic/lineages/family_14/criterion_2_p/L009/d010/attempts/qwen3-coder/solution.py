import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    N, E, F = map(int, sys.stdin.readline().split())
    targets = list(map(int, sys.stdin.readline().split()))
    
    # Convert to 0-indexed
    targets = [t - 1 for t in targets]
    
    edges = []
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        edges.append((w, u, v))
    
    # If F <= 1, condition is automatically satisfied
    if F <= 1:
        print(0)
        return
    
    # We need to ensure that all target nodes are connected in the final graph
    # This is equivalent to finding the MST of the subgraph induced by target nodes
    # But since we're dealing with a subset of nodes, we can model this as
    # finding the minimum cost to connect all target nodes
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(N))
    rank = [0] * N
    
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
    
    # Count how many target nodes are connected
    target_set = set(targets)
    components = len(target_set)
    
    total_cost = 0
    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            # Check if we just connected two components that contain target nodes
            # Actually, let's think differently:
            # We want to connect all target nodes together
            # So we count how many separate components of target nodes we have
            # and reduce until we have one component
            
            # Let's count number of target components
            target_parents = set()
            for t in targets:
                target_parents.add(find(t))
            
            if len(target_parents) == 1:
                break
                
    # More precise approach:
    # Use Kruskal's algorithm but stop when all targets are connected
    target_components = set(find(t) for t in targets)
    
    for w, u, v in edges:
        if len(target_components) == 1:
            break
        if find(u) != find(v):
            # Check if this union connects target components
            pu, pv = find(u), find(v)
            was_target_u = pu in target_components
            was_target_v = pv in target_components
            
            union(u, v)
            
            # Update target components
            if was_target_u:
                target_components.discard(pu)
            if was_target_v:
                target_components.discard(pv)
            if was_target_u or was_target_v:
                new_parent = find(u)  # or find(v) since they're now the same
                target_components.add(new_parent)
                
            total_cost += w
    
    print(total_cost)

threading.Thread(target=main).start()