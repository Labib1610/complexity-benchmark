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

    for a in range(n):
        mask_a = adj[a]
        for b in range(a + 1, n):
            if (mask_a >> b) & 1 == 0:
                continue          # edge a-b missing
            common = (mask_a & adj[b]) >> (b + 1)
            if common:
                lowbit = common & -common
                idx = lowbit.bit_length() - 1
                c = b + 1 + idx
                # output 1‑based and sorted
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()