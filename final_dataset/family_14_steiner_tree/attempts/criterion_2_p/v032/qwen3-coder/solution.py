import sys
from collections import defaultdict, deque

def find_parent_and_size(edges, n):
    # Union-Find data structure
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if size[px] < size[py]:
            px, py = py, px
        parent[py] = px
        size[px] += size[py]
        return True
    
    # Process edges
    for u, v, w in edges:
        union(u, v)
    
    return parent, size

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
    
    critical = set()
    for _ in range(t):
        critical.add(int(data[idx]))
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
    
    # If there's 0 or 1 critical module, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Union-Find for tracking connected components
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if size[px] < size[py]:
            px, py = py, px
        parent[py] = px
        size[px] += size[py]
        return True
    
    total_cost = 0
    critical_count_in_component = [0] * (n + 1)
    
    # Initialize critical count
    for c in critical:
        critical_count_in_component[c] = 1
    
    # Kruskal's algorithm variant
    for u, v, w in edges:
        pu, pv = find(u), find(v)
        if pu != pv:
            # Union the components
            if size[pu] < size[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            size[pu] += size[pv]
            critical_count_in_component[pu] += critical_count_in_component[pv]
            
            # If this union connects two components that both have critical modules,
            # we must include this edge
            if critical_count_in_component[pu] > 0 and critical_count_in_component[pv] > 0:
                total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    main()