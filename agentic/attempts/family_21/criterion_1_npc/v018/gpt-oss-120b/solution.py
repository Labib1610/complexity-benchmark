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

    # sort descending for maximum kept weight
    edges.sort(reverse=True)

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

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        # if both components already have a special, cannot merge
        if has_special[ra] and has_special[rb]:
            return False
        # merge
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        has_special[ra] = has_special[ra] or has_special[rb]
        return True

    kept = set()
    kept_weight = 0
    for idx, (w, u, v) in enumerate(edges):
        if union(u, v):
            kept.add(idx)
            kept_weight += w

    removed_cost = total - kept_weight
    if removed_cost <= B:
        out = ["YES"]
        removed_edges = []
        for idx, (w, u, v) in enumerate(edges):
            if idx not in kept:
                removed_edges.append((u, v))
        out.append(str(len(removed_edges)))
        out.extend(f"{u} {v}" for u, v in removed_edges)
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()