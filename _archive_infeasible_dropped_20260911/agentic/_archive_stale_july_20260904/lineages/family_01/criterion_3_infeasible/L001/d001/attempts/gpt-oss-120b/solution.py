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
        a_mask = adj[a]
        for b in range(a + 1, n - 1):
            # edge a-b ?
            if (a_mask >> b) & 1 == 0:
                continue
            common = a_mask & adj[b]
            # keep only vertices > b
            mask = common >> (b + 1)
            if mask:
                # lowest set bit
                low = mask & -mask
                offset = low.bit_length() - 1
                c = b + 1 + offset
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()