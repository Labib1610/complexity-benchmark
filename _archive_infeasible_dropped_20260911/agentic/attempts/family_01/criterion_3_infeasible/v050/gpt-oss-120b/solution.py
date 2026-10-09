import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bit masks, vertex i ↔ bit i-1
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        for b in range(a + 1, n):
            # edge a‑b ?
            if ((adj[a] >> (b - 1)) & 1) == 0:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            common_shift = common >> b
            if common_shift:
                # lowest set bit → smallest possible c
                lsb = common_shift & -common_shift
                c_idx = lsb.bit_length() - 1      # 0‑based index inside shifted mask
                c = b + 1 + c_idx
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()