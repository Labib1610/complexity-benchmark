import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    targets = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    
    # First pass: connect non-target nodes to minimize cost
    non_target_edges = []
    for w, u, v in edges:
        if u not in targets and v not in targets:
            non_target_edges.append((w, u, v))
    
    for w, u, v in non_target_edges:
        union(u, v)
    
    # Second pass: Kruskal's algorithm to connect all targets
    total_cost = 0
    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            total_cost += w
            # Check if all targets are connected
            root = find(targets[0])
            all_connected = True
            for target in targets[1:]:
                if find(target) != root:
                    all_connected = False
                    break
            if all_connected:
                break
    
    print(total_cost)

if __name__ == "__main__":
    solve()