import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency bitsets, 1‑based indexing, bit i corresponds to vertex i
    mask = [0] * (n + 1)
    edges = []          # store edges for iteration
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        mask[u] |= 1 << v
        mask[v] |= 1 << u
        if u < v:
            edges.append((u, v))
        else:
            edges.append((v, u))

    # pre‑compute a mask that has bits > b set, for each b
    # higher_mask[b] = bits (b+1 .. n) = ((1 << (n+1)) - (1 << (b+1)))
    higher_mask = [0] * (n + 1)
    full = (1 << (n + 1)) - 2   # bits 1..n set
    for b in range(1, n + 1):
        higher_mask[b] = full ^ ((1 << (b + 1)) - 2)   # clear bits <= b

    # search in lexicographic order
    for a in range(1, n + 1):
        # iterate b > a where edge exists
        # we can scan all b, but using mask speeds up a bit
        neigh = mask[a]
        b = a + 1
        while b <= n:
            if (neigh >> b) & 1:
                # edge (a,b) exists
                common = mask[a] & mask[b] & higher_mask[b]
                if common:
                    # smallest c = position of lowest set bit
                    low = common & -common
                    c = low.bit_length()
                    print(a, b, c)
                    return
            b += 1

if __name__ == "__main__":
    solve()