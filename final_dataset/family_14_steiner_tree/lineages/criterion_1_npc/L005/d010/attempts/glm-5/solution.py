import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    critical = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
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
    
    edges.sort(key=lambda e: e[2])
    
    for u, v, w in edges:
        union(u, v)
    
    root0 = find(critical[0])
    for c in critical[1:]:
        if find(c) != root0:
            print(-1)
            return
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total = 0
    for u, v, w in edges:
        if union(u, v):
            total += w
    
    print(total)

solve()