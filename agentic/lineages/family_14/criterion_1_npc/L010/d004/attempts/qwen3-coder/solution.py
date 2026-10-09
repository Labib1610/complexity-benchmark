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

def kruskal(n, edges, targets):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Try all possible ways to connect targets
    # Since t <= 10, we can use a greedy approach
    # We'll build a MST that connects all targets
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total_cost = 0
    connected_targets = set()
    
    # If there's only one target, cost is 0
    if len(targets) <= 1:
        return 0
    
    # We need to connect all targets
    # We'll use Kruskal's algorithm to find the minimum cost to connect all targets
    targets = set(targets)
    
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total_cost += w
            
            # Check if we've connected all targets
            connected_components = set()
            for target in targets:
                connected_components.add(find(parent, target))
            
            if len(connected_components) == 1:
                return total_cost
    
    return total_cost

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    line_idx = 0
    
    # Read n, m, t
    n, m, t = map(int, input_lines[line_idx].split())
    line_idx += 1
    
    # Read targets
    targets = list(map(int, input_lines[line_idx].split()))
    line_idx += 1
    
    # Read edges
    edges = []
    for _ in range(m):
        u, v, w = map(int, input_lines[line_idx].split())
        edges.append((u, v, w))
        line_idx += 1
    
    # If there's 0 or 1 target, no cost is needed
    if len(targets) <= 1:
        print(0)
        return
    
    # Use Kruskal's algorithm to find minimum spanning tree that connects all targets
    # But we only care about connecting the targets, not all nodes
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total_cost = 0
    target_components = {}  # Map each target to its component
    
    # Initialize each target in its own component
    for target in targets:
        target_components[target] = target
    
    connected_components = len(targets)
    
    for u, v, w in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)
        
        if root_u != root_v:
            union(parent, rank, u, v)
            total_cost += w
            
            # Update target components
            # Check if this union connects two different target components
            u_target_root = None
            v_target_root = None
            
            for target in targets:
                if find(parent, target) == root_u:
                    u_target_root = target
                if find(parent, target) == root_v:
                    v_target_root = target
            
            # If both u and v are connected to targets from different components, we've merged components
            if u_target_root is not None and v_target_root is not None and u_target_root != v_target_root:
                connected_components -= 1
                if connected_components == 1:
                    print(total_cost)
                    return
    
    print(total_cost)

if __name__ == "__main__":
    main()