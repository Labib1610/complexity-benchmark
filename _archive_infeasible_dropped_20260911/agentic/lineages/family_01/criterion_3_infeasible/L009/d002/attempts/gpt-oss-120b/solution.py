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
        u = int(next(it)); v = int(next(it))
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    # sort neighbour lists for deterministic order
    for lst in neigh:
        lst.sort()

    for x in range(1, n + 1):
        bx = adj_bits[x]
        for y in neigh[x]:
            if y <= x:
                continue
            # common neighbours of x and y
            common = bx & adj_bits[y]
            # keep only vertices > y
            mask = ~((1 << (y + 1)) - 1)
            common &= mask
            if common:
                # lowest set bit -> smallest z
                low = common & -common
                z = low.bit_length() - 1   # 0‑based index
                # output sorted (x<y<z)
                sys.stdout.write(f"{x} {y} {z+1}\n")
                return

if __name__ == "__main__":
    solve()