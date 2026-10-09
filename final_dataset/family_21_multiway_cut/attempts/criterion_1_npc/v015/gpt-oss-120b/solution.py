import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    specials = set(int(next(it)) - 1 for _ in range(k))  # zero‑based
    edges = []
    total = 0
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((w, u, v, idx))
        total += w

    # DSU with special flag
    parent = list(range(n))
    rank = [0] * n
    has_special = [i in specials for i in range(n)]

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        # cannot unite if both components already have a special
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

    # greedy maximum weight forest
    edges.sort(key=lambda x: -x[0])          # descending weight
    kept = [False] * m
    kept_weight = 0
    for w, u, v, idx in edges:
        if union(u, v):
            kept[idx] = True
            kept_weight += w

    if total - kept_weight <= B:
        # feasible
        out = []
        out.append("YES")
        # edges to cap = those not kept
        cap = [(u+1, v+1) for w, u, v, idx in edges if not kept[idx]]
        out.append(str(len(cap)))
        out.extend(f"{a} {b}" for a, b in cap)
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()