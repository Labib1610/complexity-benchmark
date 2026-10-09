import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitsets, 0‑based vertices
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        a_mask = adj[a]
        for b in range(a + 1, n):
            if (a_mask >> b) & 1 == 0:
                continue          # not an edge a‑b
            common = a_mask & adj[b]
            # keep only vertices > b
            mask = common >> (b + 1)
            if mask:
                # lowest set bit in mask
                low = mask & -mask
                c = (low.bit_length() - 1) + (b + 1)
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()