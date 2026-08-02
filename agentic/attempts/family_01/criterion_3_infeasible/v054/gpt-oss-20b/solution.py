import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for a in range(1, n + 1):
        neigh[a].sort()

    # precompute masks for bits <= i
    mask = [(1 << (i + 1)) - 1 for i in range(n + 1)]

    for a in range(1, n + 1):
        for b in neigh[a]:
            if b <= a:
                continue
            cand = adj[a] & adj[b] & ~mask[b]
            if cand:
                # least significant set bit gives minimal c
                c_bit = cand & -cand
                c = c_bit.bit_length() - 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()