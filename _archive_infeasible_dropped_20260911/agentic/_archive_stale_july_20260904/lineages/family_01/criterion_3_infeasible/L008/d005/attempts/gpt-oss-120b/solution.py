import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_bits = [0] * (n + 1)          # 1‑based
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        # set bits
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    # ensure neighbor lists are sorted for deterministic order
    for lst in neigh:
        lst.sort()

    full_mask = (1 << n) - 1

    for a in range(1, n + 1):
        for b in neigh[a]:
            if b <= a:
                continue
            # common neighbours of a and b
            common = adj_bits[a] & adj_bits[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << b) - 1)   # bits b+1 .. n
            common &= mask
            if common:
                # lowest set bit gives smallest c
                low = common & -common
                c = low.bit_length()          # position (1‑based)
                # a < b < c holds by construction
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()