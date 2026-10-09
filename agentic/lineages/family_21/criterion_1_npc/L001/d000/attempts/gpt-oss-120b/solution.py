import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = set(int(next(it)) for _ in range(k))
    edges = []
    total_cost = 0
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((w, u, v))
        total_cost += w

    # DSU with special flag
    parent = list(range(n+1))
    rank = [0]*(n+1)
    has_special = [False]*(n+1)
    for s in specials:
        has_special[s] = True

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        # if both have special, cannot merge
        if has_special[ra] and has_special[rb]:
            return False
        # union by rank
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        has_special[ra] = has_special[ra] or has_special[rb]
        return True

    # Kruskal-like: keep edges with highest weight that don't merge two specials
    edges_sorted = sorted(edges, key=lambda x: -x[0])
    kept = set()
    kept_weight = 0
    for w, u, v in edges_sorted:
        if union(u, v):
            kept.add((u, v, w))
            kept_weight += w

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