import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [0] * (n + 1)  # 1-based
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        neigh_a = adj[a]
        for b in range(a + 1, n + 1):
            # check edge a-b
            if not (neigh_a >> (b - 1)) & 1:
                continue
            # intersection of neighbors of a and b
            mask = (neigh_a & adj[b]) >> b  # discard bits <= b-1
            if mask:
                lsb = mask & -mask
                pos = lsb.bit_length() - 1
                c = b + 1 + pos
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()