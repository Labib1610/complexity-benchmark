import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_int = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # store undirected
        adj_int[u] |= 1 << (v - 1)
        adj_int[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    # sort neighbor lists for deterministic order
    for i in range(1, n + 1):
        neigh[i].sort()

    full_mask = (1 << n) - 1

    for a in range(1, n + 1):
        for b in neigh[a]:
            if b <= a:
                continue
            # common neighbors of a and b
            common = adj_int[a] & adj_int[b]
            # keep only vertices with index > b
            mask = full_mask ^ ((1 << b) - 1)   # bits b+1 .. n
            common &= mask
            if common:
                lowbit = common & -common
                c = lowbit.bit_length()          # 1‑based index
                # c is guaranteed > b
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()