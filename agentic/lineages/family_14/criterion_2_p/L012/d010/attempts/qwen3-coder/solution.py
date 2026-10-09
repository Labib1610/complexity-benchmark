import sys
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
    
    required = set()
    for _ in range(t):
        required.add(int(data[idx]) - 1)
        idx += 1
    
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
    
    # We need to ensure all required vertices are connected
    parent = list(range(n))
    rank = [0] * n
    total_cost = 0
    
    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            # Check if this edge connects a required node to another component
            # Actually, we just build the MST of the required nodes
            if union(parent, rank, u, v):
                total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    main()