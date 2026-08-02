import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(1, n - 1):
        aa = adj[a]
        for b in range(a + 1, n):
            if not ((aa >> b) & 1):
                continue
            inter = aa & adj[b]
            mask = ~((1 << (b + 1)) - 1)
            candidates = inter & mask
            if candidates:
                low = candidates & -candidates
                c = low.bit_length() - 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()