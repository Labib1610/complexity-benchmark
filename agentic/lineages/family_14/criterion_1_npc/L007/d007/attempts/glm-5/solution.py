import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    key = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # We need all key politicians in the same connected component.
    # Minimum spanning forest connecting all key politicians.
    # Use Kruskal's algorithm but only merge components if at least one has a key politician.
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    has_key = [False] * (n + 1)
    for k in key:
        has_key[k] = True
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    edges.sort(key=lambda e: e[2])
    total = 0
    for u, v, w in edges:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            continue
        if has_key[ru] and has_key[rv]:
            # Both components have key politicians; merging connects them.
            total += w
            # Merge smaller into larger
            if size[ru] < size[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            size[ru] += size[rv]
            has_key[ru] = has_key[ru] or has_key[rv]
        else:
            # At most one component has key politicians; merge but don't count cost.
            if size[ru] < size[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            size[ru] += size[rv]
            has_key[ru] = has_key[ru] or has_key[rv]
    
    print(total)

solve()