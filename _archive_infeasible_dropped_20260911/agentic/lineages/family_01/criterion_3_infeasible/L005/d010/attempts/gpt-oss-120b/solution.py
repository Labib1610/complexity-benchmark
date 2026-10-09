import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n               # adjacency bitsets
    neigh = [[] for _ in range(n)]   # neighbour lists (sorted later)

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    # sort neighbour lists to guarantee increasing order
    for lst in neigh:
        lst.sort()

    full_mask = (1 << n) - 1

    for a in range(n):
        for b in neigh[a]:
            if b <= a:
                continue
            # vertices adjacent to both a and b
            common = adj[a] & adj[b]
            # keep only vertices with index > b
            mask = full_mask ^ ((1 << (b + 1)) - 1)
            cand = common & mask
            if cand:
                # lowest set bit -> smallest possible c
                low_bit = cand & -cand
                c = low_bit.bit_length() - 1
                # output 1‑based, sorted
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()