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
    
    if t <= 1:
        print(0)
        return
    
    priority = set()
    for _ in range(t):
        priority.add(int(data[idx]))
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
    
    # Sort edges by weight
    edges.sort()
    
    # Initialize DSU
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total_cost = 0
    connected_components = t
    
    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            if union(parent, rank, u, v):
                # Check if either u or v is a priority center
                if u in priority or v in priority:
                    # If both u and v are now connected to priority centers
                    pu = find(parent, u)
                    pv = find(parent, v)
                    
                total_cost += w
                # Check if we've connected two components that both contain priority nodes
                # We need to track how many priority groups we have merged
                # Simpler approach: count how many priority nodes are in each component
                
                # Actually, let's think differently:
                # We want to connect all priority nodes
                # So we run Kruskal's until all priority nodes are in the same component
                # But that's not right either because they don't need to be in the same component,
                # just all pairwise connected.
                
                # Better approach: 
                # Run Kruskal's algorithm but stop when all priority nodes are connected
                # We can check if all priority nodes are in the same component
                
                # Count how many distinct components have priority nodes
                priority_components = set()
                for node in priority:
                    priority_components.add(find(parent, node))
                
                if len(priority_components) == 1:
                    break
    
    print(total_cost)

if __name__ == "__main__":
    main()