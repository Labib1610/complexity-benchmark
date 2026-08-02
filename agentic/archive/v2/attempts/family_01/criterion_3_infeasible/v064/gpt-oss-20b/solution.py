import sys

def solve() -> None:
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_bits = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        adj_list[u].append(v)
        adj_list[v].append(u)

    for a in range(1, n - 1):
        # neighbors of a that are greater than a
        neigh_a = [v for v in adj_list[a] if v > a]
        neigh_a.sort()
        for b in neigh_a:
            mask = adj_bits[a] & adj_bits[b]
            # keep only bits corresponding to nodes > b
            mask &= ~((1 << b) - 1)
            if mask:
                low = mask & -mask
                c = low.bit_length()  # node index (1‑based)
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()