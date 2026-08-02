import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n - 2):
        for b in range(a + 1, n - 1):
            if ((adj[a] >> b) & 1) == 0:
                continue
            common = adj[a] & adj[b]
            mask = common >> (b + 1)
            if mask == 0:
                continue
            lsb = mask & -mask
            offset = (lsb.bit_length() - 1)
            c = b + 1 + offset
            # convert to 1-based labels
            print(a + 1, b + 1, c + 1)
            return

if __name__ == "__main__":
    solve()