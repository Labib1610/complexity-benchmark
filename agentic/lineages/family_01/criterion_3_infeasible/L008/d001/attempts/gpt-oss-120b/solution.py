import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full_mask = (1 << n) - 1

    for a in range(n):
        for b in range(a + 1, n):
            if ((adj[a] >> b) & 1) == 0:          # edge (a,b) missing
                continue
            common = adj[a] & adj[b]              # neighbours of both
            mask = full_mask ^ ((1 << (b + 1)) - 1)   # bits > b
            common_high = common & mask
            if common_high:
                # index of least set bit
                c = (common_high & -common_high).bit_length() - 1
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()