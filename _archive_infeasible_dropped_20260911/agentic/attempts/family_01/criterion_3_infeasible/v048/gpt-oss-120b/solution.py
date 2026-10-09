import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    bits = [0] * n          # bitset of neighbours for each vertex
    adj = [[] for _ in range(n)]  # adjacency lists (sorted)
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        bits[u] |= 1 << v
        bits[v] |= 1 << u
        adj[u].append(v)
        adj[v].append(u)

    for a in range(n):
        # ensure neighbours are sorted for lexicographic order
        adj[a].sort()
    # search lexicographically smallest triangle
    for a in range(n):
        for b in adj[a]:
            if b <= a:
                continue
            common = bits[a] & bits[b]
            # we need c > b
            common >>= b + 1
            if common:
                # lowest set bit
                low = (common & -common).bit_length() - 1
                c = b + 1 + low
                # output 1‑based indices
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()