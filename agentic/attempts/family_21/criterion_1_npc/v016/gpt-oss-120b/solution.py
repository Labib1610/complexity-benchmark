import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = set(int(next(it)) for _ in range(k))
    edges = []
    adj = {}
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u, v, w))
        adj.setdefault(u, []).append((v, w))
        adj.setdefault(v, []).append((u, w))
    cut_set = set()
    total_cost = 0
    for u, v, w in edges:
        if u in specials or v in specials:
            # edge incident to at least one special
            # we will cut it
            if (u, v) not in cut_set and (v, u) not in cut_set:
                cut_set.add((u, v))
                total_cost += w
    if total_cost <= B:
        out = ["YES", str(len(cut_set))]
        for u, v in cut_set:
            out.append(f"{u} {v}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()