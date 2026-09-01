import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_int = [0] * n          # bitset of neighbors
    neigh = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj_int[u] |= 1 << v
        adj_int[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    # sort neighbor lists for deterministic order
    for lst in neigh:
        lst.sort()

    full_mask = (1 << n) - 1

    for u in range(n):
        for v in neigh[u]:
            if v <= u:
                continue
            common = adj_int[u] & adj_int[v]
            # keep only vertices with index > v
            mask = full_mask ^ ((1 << (v + 1)) - 1)
            common &= mask
            if common:
                # get smallest index c
                c = (common & -common).bit_length() - 1
                print(u + 1, v + 1, c + 1)
                return

if __name__ == "__main__":
    solve()