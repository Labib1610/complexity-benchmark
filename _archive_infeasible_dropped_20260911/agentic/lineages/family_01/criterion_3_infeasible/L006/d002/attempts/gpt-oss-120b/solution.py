import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency masks: bit i set ⇔ edge to vertex i
    masks = [0] * n
    # adjacency lists for ordered iteration
    adj = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        masks[u] |= 1 << v
        masks[v] |= 1 << u
        adj[u].append(v)
        adj[v].append(u)

    for lst in adj:
        lst.sort()

    for a in range(n):
        ma = masks[a]
        for b in adj[a]:
            if b <= a:
                continue
            # vertices adjacent to both a and b
            common = ma & masks[b]
            # discard vertices <= b
            common >>= (b + 1)
            if common:
                # lowest set bit = smallest possible c
                lowest = common & -common
                pos = lowest.bit_length() - 1
                c = b + 1 + pos
                # output 1‑based indices
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()