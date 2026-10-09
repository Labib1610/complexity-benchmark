import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bitset
    nbr = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        # store undirected edge
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        if v > u:
            nbr[u].append(v)
        else:
            nbr[v].append(u)

    # ensure neighbour lists are sorted (they already are because we added in input order,
    # but sorting guarantees correctness)
    for lst in nbr:
        lst.sort()

    for a in range(n):
        mask_a = adj[a]
        for b in nbr[a]:          # b > a
            # common neighbours of a and b
            common = mask_a & adj[b]
            # keep only vertices > b
            shifted = common >> (b + 1)
            if shifted:
                lsb = shifted & -shifted
                # position of lsb (0‑based)
                k = lsb.bit_length() - 1
                c = b + 1 + k
                # output 1‑based
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()