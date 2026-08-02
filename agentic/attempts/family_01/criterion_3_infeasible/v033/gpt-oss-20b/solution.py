import sys

def solve() -> None:
    it = iter(sys.stdin.read().strip().split())
    try:
        n = int(next(it))
    except StopIteration:
        return
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        neigh_a = adj[a]
        for b in range(a + 1, n + 1):
            if not (neigh_a >> (b - 1)) & 1:
                continue
            common = adj[a] & adj[b]
            mask = (1 << b) - 1          # bits <= b-1
            candidate = common & ~mask
            if candidate:
                low = candidate & -candidate
                c = low.bit_length() - 1 + 1  # convert to 1-index
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()