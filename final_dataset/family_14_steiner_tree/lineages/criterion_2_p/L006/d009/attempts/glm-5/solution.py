import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    T = [int(data[idx + i]) for i in range(t)]
    idx += t
    
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True
    
    edges.sort(key=lambda e: e[2])
    
    for u, v, w in edges:
        union(u, v)
    
    target_roots = set(find(x) for x in T)
    k = len(target_roots)
    
    if k == 1:
        print(0)
        return
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total = 0
    components = n
    
    for u, v, w in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            union(ru, rv)
            total += w
            components -= 1
            if components == n - (k - 1):
                break
    
    print(total)

solve()