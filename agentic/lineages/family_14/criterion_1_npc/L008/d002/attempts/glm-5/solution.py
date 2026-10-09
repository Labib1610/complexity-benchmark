import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    turbines = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u - 1, v - 1))
    if t <= 1:
        print(0)
        return
    edges.sort()
    parent = list(range(n))
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
        parent[rx] = ry
        return True
    total = 0
    for w, u, v in edges:
        if union(u, v):
            total += w
            roots = set(find(x) for x in turbines)
            if len(roots) == 1:
                print(total)
                return
    print(total)

solve()