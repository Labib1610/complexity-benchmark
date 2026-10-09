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
        a_adj = adj[a]
        for b in range(a + 1, n - 1):
            if (a_adj >> b) & 1 == 0:
                continue
            common = a_adj & adj[b]
            mask = common >> (b + 1)
            if mask:
                # lowest set bit in mask
                low = mask & -mask
                pos = low.bit_length() - 1
                c = b + 1 + pos
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()