import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bitsets, vertices are 1‑based, bit 0 corresponds to vertex 1
    adj_bits = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    # sort neighbour lists to guarantee increasing order of b
    for lst in neigh:
        lst.sort()

    for a in range(1, n - 1):
        bits_a = adj_bits[a]
        for b in neigh[a]:
            if b <= a:
                continue
            # common neighbours of a and b
            common = bits_a & adj_bits[b]
            # keep only vertices > b
            cand = common & ~((1 << b) - 1)
            if cand:
                low = cand & -cand          # least significant 1‑bit
                c = low.bit_length()        # vertex number (1‑based)
                # a < b < c is guaranteed
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()