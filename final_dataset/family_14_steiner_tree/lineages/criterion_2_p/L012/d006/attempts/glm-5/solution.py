import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    targets = []
    for _ in range(t):
        targets.append(int(data[idx]) - 1)
        idx += 1

    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))

    if t <= 1:
        print(0)
        return

    parent = list(range(n))
    rank = [0] * n

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

    target_roots = set()
    for tgt in targets:
        target_roots.add(find(tgt))

    if len(target_roots) <= 1:
        print(0)
        return

    parent = list(range(n))
    rank = [0] * n

    for u, v, w in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            if rank[ru] < rank[rv]:
                parent[ru] = rv
            elif rank[ru] > rank[rv]:
                parent[rv] = ru
            else:
                parent[rv] = ru
                rank[ru] += 1

    target_roots = set()
    for tgt in targets:
        target_roots.add(find(tgt))

    if len(target_roots) <= 1:
        print(0)
        return

    parent = list(range(n))
    rank = [0] * n

    total_cost = 0
    components = n

    for u, v, w in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            if rank[ru] < rank[rv]:
                parent[ru] = rv
            elif rank[ru] > rank[rv]:
                parent[rv] = ru
            else:
                parent[rv] = ru
                rank[ru] += 1
            total_cost += w
            components -= 1
            if components == 1:
                break

    print(total_cost)

solve()