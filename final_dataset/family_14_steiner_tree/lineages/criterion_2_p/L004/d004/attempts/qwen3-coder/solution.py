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
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    targets = list(map(int, data[idx:idx+t]))
    idx += t
    
    # Convert to 0-indexed
    targets = [x - 1 for x in targets]
    
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight
    edges.sort()
    
    # Kruskal's algorithm variant
    parent = list(range(n))
    rank = [0] * n
    cost = 0
    components = set(targets)
    
    for w, u, v in edges:
        # Check if u and v are in the target set
        in_u = find(parent, u) in components
        in_v = find(parent, v) in components
        
        if in_u and in_v:
            # Both components contain target nodes
            if find(parent, u) != find(parent, v):
                union(parent, rank, u, v)
                cost += w
                # Merge the components in our tracking set
                components.discard(find(parent, u))
                components.discard(find(parent, v))
                components.add(find(parent, u))
        elif in_u or in_v:
            # One component contains target nodes
            if union(parent, rank, u, v):
                # Merge the components in our tracking set
                new_root = find(parent, u)
                components.discard(find(parent, u))
                components.discard(find(parent, v))
                components.add(new_root)
                if in_u and in_v:
                    cost += w
                elif in_u or in_v:
                    cost += w
        else:
            # Neither component contains target nodes
            union(parent, rank, u, v)
    
    print(cost)

if __name__ == "__main__":
    main()