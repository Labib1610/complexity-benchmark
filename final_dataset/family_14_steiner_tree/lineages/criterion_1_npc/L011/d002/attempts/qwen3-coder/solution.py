import sys
import heapq
from collections import defaultdict

def read_input():
    n, m, t = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    return n, m, t, critical, edges

def find_mst_with_critical_nodes(n, edges, critical):
    if len(critical) <= 1:
        return 0
    
    # Sort edges by weight
    edges.sort()
    
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
    
    # First, connect all critical nodes using MST
    total_cost = 0
    connected_critical = set()
    
    # We'll use a modified Kruskal's algorithm
    # Process edges in order of increasing weight
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
            # Check if both u and v are critical or connected to critical components
            if u in critical:
                connected_critical.add(u)
            if v in critical:
                connected_critical.add(v)
            
            # If all critical nodes are connected, we're done
            # Check if all critical nodes are in the same component
            if len(connected_critical) == len(critical):
                root = find(next(iter(critical)))
                if all(find(node) == root for node in critical):
                    break
    
    return total_cost

def solve():
    n, m, t, critical, edges = read_input()
    
    if len(critical) <= 1:
        print(0)
        return
    
    # Use Kruskal's algorithm to find MST of the subgraph induced by critical nodes
    # We need to find the minimum cost to connect all critical nodes
    
    # Union-Find for tracking components
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
    connected_count = 0
    critical_list = list(critical)
    
    # Sort edges by weight
    edges.sort()
    
    # Kruskal's algorithm
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
            # Check if this edge connects critical nodes or their components
            # Count how many critical nodes are now connected
            roots = set(find(node) for node in critical_list)
            if len(roots) == 1:  # All critical nodes in same component
                break
                
    print(total_cost)

if __name__ == "__main__":
    solve()