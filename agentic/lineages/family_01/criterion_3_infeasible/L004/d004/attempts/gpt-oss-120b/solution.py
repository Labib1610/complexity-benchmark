import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u > v:
            u, v = v, u
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        edges.append((u, v))

    full_mask = (1 << n) - 1
    # sort edges to ensure lexicographic order of (u,v)
    edges.sort()
    for u, v in edges:
        # common neighbours of u and v
        common = adj[u] & adj[v]
        # zero out bits <= v
        mask = full_mask ^ ((1 << (v + 1)) - 1)
        common &= mask
        if common:
            lowbit = common & -common
            w = lowbit.bit_length() - 1
            # output sorted triple (u+1, v+1, w+1)
            print(u + 1, v + 1, w + 1)
            return

if __name__ == "__main__":
    solve()