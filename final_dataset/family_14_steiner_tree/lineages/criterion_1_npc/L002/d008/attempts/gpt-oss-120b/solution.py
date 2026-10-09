import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    T = set(int(next(it)) for _ in range(t))
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        if u in T and v in T:
            edges.append((w, u, v))
    if t <= 1:
        print(0)
        return

    # Kruskal
    edges.sort()
    parent = {x: x for x in T}
    rank = {x: 0 for x in T}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    total = 0
    edges_used = 0
    for w, u, v in edges:
        if union(u, v):
            total += w
            edges_used += 1
            if edges_used == t - 1:
                break

    print(total)

if __name__ == "__main__":
    solve()