import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency bitmask, 0-indexed bits
    masks = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, n + 1):
        adj[i].sort()

    # search lexicographically smallest triangle
    for a in range(1, n + 1):
        for b in adj[a]:
            if b <= a:
                continue
            # common neighbors of a and b
            common = masks[a] & masks[b]
            # discard vertices <= b
            common >>= b
            if common:
                # lowest set bit gives smallest c > b
                low = common & -common
                idx = low.bit_length() - 1
                c = b + 1 + idx
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()