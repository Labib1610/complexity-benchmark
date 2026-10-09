import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [0] * (n + 1)          # adjacency as bitsets
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    full_mask = (1 << n) - 1     # bits 0 .. n-1 are 1

    for a in range(1, n - 1):
        bits_a = adj[a]
        for b in range(a + 1, n):
            # edge a‑b ?
            if not ((bits_a >> (b - 1)) & 1):
                continue
            common = bits_a & adj[b]
            # mask vertices > b (indices b .. n-1)
            mask = full_mask ^ ((1 << b) - 1)
            cand = common & mask
            if cand:
                low = cand & -cand          # lowest set bit
                c = low.bit_length()        # vertex number (1‑based)
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()