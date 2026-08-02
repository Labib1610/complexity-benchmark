import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [0] * (n + 1)           # bitset of neighbors for each vertex
    neigh = [[] for _ in range(n + 1)]  # adjacency lists

    for _ in range(m):
        u = next(it)
        v = next(it)
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj[u] |= bit_u
        adj[v] |= bit_v
        neigh[u].append(v)
        neigh[v].append(u)

    # sort adjacency lists to ensure increasing order when iterating b
    for lst in neigh:
        lst.sort()

    for a in range(1, n - 1):
        mask_a = adj[a]
        for b in neigh[a]:
            if b <= a:
                continue
            # intersection of neighbors of a and b
            mask_ab = mask_a & adj[b]
            # shift to drop vertices <= b
            shifted = mask_ab >> b
            if shifted:
                # lowest set bit in shifted
                lb = shifted & -shifted
                c = b + lb.bit_length()
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()