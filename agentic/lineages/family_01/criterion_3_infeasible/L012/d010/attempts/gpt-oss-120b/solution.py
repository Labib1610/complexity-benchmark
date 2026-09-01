import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n                 # bitset adjacency
    nbr = [[] for _ in range(n)]  # neighbour lists

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        nbr[u].append(v)
        nbr[v].append(u)

    for lst in nbr:
        lst.sort()

    full_mask = (1 << n) - 1

    for a in range(n):
        for b in nbr[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            # keep only vertices with index > b
            mask = full_mask ^ ((1 << (b + 1)) - 1)
            common &= mask
            if common:
                # least set bit -> smallest c
                c_bit = common & -common
                c = c_bit.bit_length() - 1   # zero‑based index
                # output in 1‑based, already a<b<c
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()