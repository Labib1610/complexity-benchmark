import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bitsets
    nbr = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        # store undirected edge
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        nbr[u].append(v)
        nbr[v].append(u)

    # sort neighbour lists for deterministic order
    for i in range(n):
        nbr[i].sort()

    for a in range(n):
        for b in nbr[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = ~((1 << (b + 1)) - 1)
            common &= mask
            if common:
                lowbit = common & -common
                c = lowbit.bit_length() - 1
                # a < b < c holds
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()