import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = set(int(next(it)) for _ in range(k))
    edges = []
    total = 0
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((w, u, v))
        total += w

    # DSU with special flag
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    has_special = [False] * (n + 1)
    for s in specials:
        has_special[s] = True

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        # check special constraint
        if has_special[rx] and has_special[ry]:
            return False
        # union by rank
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        has_special[rx] = has_special[rx] or has_special[ry]
        return True

    # Kruskal-like keep maximum weight forest respecting constraint
    edges_sorted = sorted(edges, key=lambda x: -x[0])
    kept = set()
    for idx, (w, u, v) in enumerate(edges_sorted):
        if union(u, v):
            kept.add((u, v, w))

    # Determine removed edges
    removed = []
    removed_cost = 0
    for w, u, v in edges:
        if (u, v, w) not in kept and (v, u, w) not in kept:
            removed.append((u, v))
            removed_cost += w

    if removed_cost <= B:
        out = ["YES", str(len(removed))]
        out += [f"{u} {v}" for u, v in removed]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()