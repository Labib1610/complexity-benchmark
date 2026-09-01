import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # bitset, 0‑based bits
    nbr = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        # store edge
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        nbr[u].append(v)
        nbr[v].append(u)

    # sort neighbour lists for deterministic order
    for i in range(1, n + 1):
        nbr[i].sort()

    for a in range(1, n + 1):
        for b in nbr[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            mask = common >> b          # keep only vertices > b
            if mask:
                low = mask & -mask       # lowest set bit
                idx = low.bit_length() - 1
                c = b + 1 + idx
                # a < b < c holds by construction
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()