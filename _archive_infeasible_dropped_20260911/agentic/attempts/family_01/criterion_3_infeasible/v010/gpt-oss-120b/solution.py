import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_bits = [0] * (n + 1)          # bitset of neighbours (1‑based vertices)
    neigh = [[] for _ in range(n + 1)]  # sorted neighbour lists

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    for i in range(1, n + 1):
        neigh[i].sort()

    full_mask = (1 << n) - 1  # keep only n bits

    for a in range(1, n + 1):
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj_bits[a] & adj_bits[b]
            # keep only vertices with number > b
            mask = ~((1 << b) - 1) & full_mask
            common &= mask
            if common:
                low = common & -common          # lowest set bit
                c = low.bit_length()            # vertex number (1‑based)
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()