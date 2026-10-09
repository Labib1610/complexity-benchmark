import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [0] * n                # adjacency bitsets, 0‑based vertices

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        mask_a = adj[a]
        for b in range(a + 1, n):
            if (mask_a >> b) & 1:          # edge a‑b exists
                common = mask_a & adj[b]   # vertices adjacent to both
                # keep only vertices with index > b
                cand = common >> (b + 1)
                if cand:
                    lsb = cand & -cand                     # lowest set bit
                    rel = lsb.bit_length() - 1
                    c = b + 1 + rel
                    # output 1‑based, ordered a<b<c
                    sys.stdout.write(f"{a+1} {b+1} {c+1}")
                    return

if __name__ == "__main__":
    solve()