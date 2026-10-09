import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bitsets, 1‑based indexing
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        # set bits (v-1) in adj[u] and (u-1) in adj[v]
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for x1 in range(1, n - 1):
        row1 = adj[x1]
        for x2 in range(x1 + 1, n):
            # edge (x1,x2) ?
            if not (row1 >> (x2 - 1)) & 1:
                continue
            inter = row1 & adj[x2]
            # keep only vertices > x2
            mask = inter >> x2
            if mask:
                # position of least significant 1‑bit
                lsb = (mask & -mask).bit_length() - 1
                x3 = x2 + 1 + lsb
                sys.stdout.write(f"{x1} {x2} {x3}")
                return

if __name__ == "__main__":
    solve()