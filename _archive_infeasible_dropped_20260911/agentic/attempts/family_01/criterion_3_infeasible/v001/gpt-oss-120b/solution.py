import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitset of neighbors (0-indexed)
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        a_mask = adj[a]
        for b in range(a + 1, n):
            if not (a_mask >> b) & 1:   # edge a-b must exist
                continue
            common = a_mask & adj[b]
            # keep only vertices with index > b
            common &= ~((1 << (b + 1)) - 1)
            if common:
                # lowest set bit gives smallest c
                c = (common & -common).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()