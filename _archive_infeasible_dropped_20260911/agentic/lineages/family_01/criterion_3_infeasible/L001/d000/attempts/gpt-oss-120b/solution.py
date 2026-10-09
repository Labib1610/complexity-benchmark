import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # bitsets, 1‑based indexing
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        # set bits (v-1) and (u-1)
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    full_mask = (1 << n) - 1

    for a in range(1, n + 1):
        neigh[a].sort()
        a_mask = adj[a]
        for b in neigh[a]:
            if b <= a:
                continue
            common = a_mask & adj[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << b) - 1)   # clear bits 0..b-1
            cand = common & mask
            if cand:
                lowest = cand & -cand
                c = lowest.bit_length()          # 1‑based vertex number
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()