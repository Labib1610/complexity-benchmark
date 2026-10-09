import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)               # bitset for each vertex, 1‑based
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    all_ones = (1 << n) - 1           # mask with bits 0..n-1 set

    for a in range(1, n + 1):
        a_adj = adj[a]
        for b in range(a + 1, n + 1):
            # edge (a,b) ?
            if (a_adj >> (b - 1)) & 1:
                # vertices adjacent to both a and b
                common = a_adj & adj[b]
                # keep only vertices with index > b (bits b..n-1)
                mask = all_ones ^ ((1 << b) - 1)
                cand = common & mask
                if cand:
                    low = cand & -cand            # lowest set bit
                    c = low.bit_length()          # 1‑based vertex number
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()