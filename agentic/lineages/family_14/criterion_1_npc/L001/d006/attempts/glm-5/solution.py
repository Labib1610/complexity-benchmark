import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    targets = [int(next(it)) for _ in range(t)]
    if t <= 1:
        print(0)
        return
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u, v))
    edges.sort()
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
    for w, u, v in edges:
        if union(u, v):
            total += w
            if all(find(targets[0]) == find(c) for c in targets):
                print(total)
                return
    print(total)

solve()