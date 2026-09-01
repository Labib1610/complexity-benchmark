import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based, bit i‑1 corresponds to vertex i

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj[u] |= bit_u
        adj[v] |= bit_v

    for a in range(1, n + 1):
        mask_a = adj[a]
        for b in range(a + 1, n + 1):
            # edge a‑b ?
            if (mask_a >> (b - 1)) & 1 == 0:
                continue
            common = mask_a & adj[b]
            # keep only vertices > b
            common &= ~((1 << b) - 1)
            if common:
                low = common & -common          # lowest set bit
                c = low.bit_length()            # because bits are 0‑based
                # c is already the vertex number (since bit 0 -> vertex 1)
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()