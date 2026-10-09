import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency bitsets, 0‑based indexing for bits
    masks = [0] * (n + 1)          # masks[vertex]

    edges = []                     # store edges with a<b
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # set bits
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)
        if u < v:
            edges.append((u, v))
        else:
            edges.append((v, u))

    # sort edges to guarantee lexicographic order of (a,b)
    edges.sort()

    for a, b in edges:
        # common neighbours of a and b
        common = masks[a] & masks[b]
        # keep only vertices > b
        common >>= b          # now bit 0 corresponds to vertex b+1
        if common == 0:
            continue
        # lowest set bit -> smallest c
        low = common & -common
        idx = low.bit_length() - 1   # position of that bit
        c = b + 1 + idx
        # output sorted triple (a<b<c already)
        sys.stdout.write(f"{a} {b} {c}")
        return

if __name__ == "__main__":
    solve()