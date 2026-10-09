import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    edges = []
    masks = [0] * (n + 1)          # bitmask of neighbors, 1‑based vertices

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        edges.append((u, v))
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)

    edges.sort()                    # lexicographic order of (a,b)

    for a, b in edges:
        common = masks[a] & masks[b]          # vertices adjacent to both a and b
        # keep only vertices with index > b
        low_mask = (1 << b) - 1                # bits 0..b-1 (vertices 1..b)
        common &= ~low_mask
        if common:
            lsb = common & -common              # lowest set bit
            c = lsb.bit_length()                # vertex number (1‑based)
            print(a, b, c)
            return

if __name__ == "__main__":
    solve()