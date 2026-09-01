import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    masks = [0] * (n + 1)          # 1‑based
    edges = []

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        edges.append((u, v))
        # set bits (0‑based)
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)

    best = None

    for u, v in edges:            # u < v
        common = masks[u] & masks[v]
        # keep only vertices > v
        common_shifted = common >> v
        if common_shifted:
            low = common_shifted & -common_shifted
            pos = low.bit_length() - 1
            w = v + pos + 1
            cand = (u, v, w)
            if best is None or cand < best:
                best = cand

    # best is guaranteed to exist
    print(*best)

if __name__ == "__main__":
    solve()