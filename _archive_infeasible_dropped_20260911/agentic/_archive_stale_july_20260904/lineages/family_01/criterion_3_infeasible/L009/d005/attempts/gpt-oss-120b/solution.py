import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bitsets, vertex i uses bit (i-1)
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj[u] |= bit_u
        adj[v] |= bit_v

    # mask_up_to[i] = bits 0..i-1 set (i.e., vertices 1..i)
    mask_up_to = [(1 << i) - 1 for i in range(n + 1)]

    out = []
    for a in range(1, n + 1):
        a_bits = adj[a]
        for b in range(a + 1, n + 1):
            # edge a-b ?
            if (a_bits >> (b - 1)) & 1:
                common = a_bits & adj[b]
                # keep only vertices > b
                common &= ~mask_up_to[b]
                if common:
                    # lowest set bit
                    low = common & -common
                    c_idx = low.bit_length() - 1      # 0‑based index
                    c = c_idx + 1
                    sys.stdout.write(f"{a} {b} {c}\n")
                    return

if __name__ == "__main__":
    solve()