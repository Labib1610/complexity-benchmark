import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    T = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    # If t == 1, empty set is valid (projected space has size 2)
    if t == 1:
        print(0)
        return
    
    # For t >= 2, we need all target variables to be in the same connected component.
    # We compute minimum spanning forest and check if all targets are connected.
    edges.sort(key=lambda x: x[2])
    parent = list(range(n + 1))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        parent[rx] = ry
        return True
    
    total = 0
    for u, v, w in edges:
        if union(u, v):
            total += w
    
    # Check if all targets are in the same component
    root = find(T[0])
    for x in T[1:]:
        if find(x) != root:
            print(-1)
            return
    
    print(total)

solve()