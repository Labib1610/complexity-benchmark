import sys
from itertools import combinations

def find_min_penalty(n, m, t, priority_coords, operations):
    if t <= 1:
        return 0
    
    # Create a graph where each node is a coordinate and edges represent available transpositions
    # We want to ensure all priority coordinates are connected in the final subgraph
    # This is essentially finding the minimum spanning tree that connects all priority coordinates
    
    # Use a modified version of Kruskal's algorithm
    # Sort operations by weight
    operations.sort(key=lambda x: x[2])
    
    # Union-Find data structure for tracking connected components
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
    
    # We need to connect all priority coordinates
    priority_coords_set = set(priority_coords)
    total_penalty = 0
    
    # First, let's see which priority coordinates are already connected
    for u, v, w in operations:
        if union(u, v):
            total_penalty += w
            # Check if all priority coordinates are now connected
            roots = set(find(coord) for coord in priority_coords)
            if len(roots) == 1:  # All priority coords have same root
                break
    
    return total_penalty

def main():
    # Read input
    line = sys.stdin.readline().split()
    n, m, t = int(line[0]), int(line[1]), int(line[2])
    
    if t <= 1:
        # Skip reading operations if t <= 1
        for _ in range(m):
            sys.stdin.readline()
        print(0)
        return
    
    priority_coords = list(map(int, sys.stdin.readline().split()))
    
    operations = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        operations.append((u, v, w))
    
    # Solve using minimum spanning tree approach
    result = solve_mst(n, m, t, priority_coords, operations)
    print(result)

def solve_mst(n, m, t, priority_coords, operations):
    if t <= 1:
        return 0
    
    # Sort edges by weight
    edges = sorted(operations, key=lambda x: x[2])
    
    # Union-Find
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
    
    total_cost = 0
    connected_priority = set([priority_coords[0]])  # Start with first priority coordinate
    
    # We need to connect t-1 more priority coordinates to form a connected component
    while len(connected_priority) < t:
        best_edge = None
        best_weight = float('inf')
        
        # Find the cheapest edge that connects a new priority coordinate to existing ones
        for u, v, w in edges:
            pu_in = u in connected_priority
            pv_in = v in connected_priority
            
            # If exactly one endpoint is in our connected component
            if (pu_in and not pv_in and v in priority_coords) or \
               (pv_in and not pu_in and u in priority_coords):
                if w < best_weight:
                    best_weight = w
                    best_edge = (u, v, w)
        
        if best_edge:
            u, v, w = best_edge
            union(u, v)
            total_cost += w
            connected_priority.add(u)
            connected_priority.add(v)
        else:
            # Fallback - just use Kruskal until all priority coords connected
            break
    
    # Alternative simpler approach: just run Kruskal until all priority coords connected
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
    
    total_cost = 0
    # Get indices of priority coordinates in the priority_coords list
    priority_set = set(priority_coords)
    
    # Keep connecting until all priority coordinates have the same root
    while True:
        roots = [find(coord) for coord in priority_coords]
        if len(set(roots)) == 1:  # All have same root
            break
            
        # Find the cheapest edge that connects two different components
        edge_found = False
        new_edges = []
        for u, v, w in edges:
            if find(u) != find(v):
                if union(u, v):
                    total_cost += w
                    edge_found = True
                    break
                else:
                    new_edges.append((u, v, w))
            else:
                new_edges.append((u, v, w))
        if not edge_found:
            break
        edges = new_edges
    
    return total_cost

if __name__ == "__main__":
    main()