import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        # set bits
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    # sort neighbour lists for deterministic order
    for lst in neigh:
        lst.sort()

    for a in range(1, n + 1):
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = ~((1 << b) - 1)
            cands = common & mask
            if cands:
                low = cands & -cands
                c = low.bit_length()          # 1‑based index
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()