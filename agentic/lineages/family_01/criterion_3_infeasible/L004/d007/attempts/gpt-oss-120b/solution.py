import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n               # bitset of neighbours
    nbr = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        # set bits
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        # store for ordered iteration
        if u < v:
            nbr[u].append(v)
            nbr[v].append(u)
        else:
            nbr[v].append(u)
            nbr[u].append(v)

    # sort neighbour lists (they are already increasing because we added in order,
    # but sorting guarantees)
    for lst in nbr:
        lst.sort()

    for a in range(n):
        for b in nbr[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            common >>= (b + 1)
            if common:
                # lowest set bit
                low = common & -common
                c = (low.bit_length() - 1) + b + 1
                # output 1‑based
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()