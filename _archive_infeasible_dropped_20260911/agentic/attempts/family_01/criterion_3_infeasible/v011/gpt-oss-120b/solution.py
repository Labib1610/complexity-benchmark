import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    neigh = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for lst in neigh:
        lst.sort()

    INF = 10 ** 9
    best = (INF, INF, INF)

    for u in range(n):
        for v in neigh[u]:
            if v <= u:
                continue
            common = adj[u] & adj[v]
            # keep only vertices with index > v
            mask = (-1) << (v + 1)
            common &= mask
            if common:
                low = common & -common
                w = low.bit_length() - 1  # 0‑based
                cand = (u + 1, v + 1, w + 1)
                if cand < best:
                    best = cand

    print(best[0], best[1], best[2])

if __name__ == "__main__":
    solve()