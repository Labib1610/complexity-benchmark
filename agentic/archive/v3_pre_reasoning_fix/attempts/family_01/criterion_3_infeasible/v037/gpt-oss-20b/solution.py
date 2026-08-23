import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adjacency_mask = [0] * (n + 1)
    neighbors = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = next(it)
        v = next(it)
        adjacency_mask[u] |= 1 << v
        adjacency_mask[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

    for a in range(1, n - 1):
        neigh_a = neighbors[a]
        # sort neighbors once for each node
        neigh_a.sort()
        for b in neigh_a:
            if b <= a:
                continue
            # intersection of neighbors of a and b
            common = adjacency_mask[a] & adjacency_mask[b]
            # shift right by b to consider only c > b
            mask = common >> b
            if mask == 0:
                continue
            # least significant bit
            lsb = mask & -mask
            # k = position of this bit (0‑based)
            k = lsb.bit_length() - 1
            c = b + k
            print(a, b, c)
            return

if __name__ == "__main__":
    solve()