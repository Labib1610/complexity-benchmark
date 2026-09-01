import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    full_mask = (1 << n) - 1     # bits 0 .. n-1 are 1

    for a in range(1, n + 1):
        a_adj = adj[a]
        for b in range(a + 1, n + 1):
            # edge (a,b) ?
            if ((a_adj >> (b - 1)) & 1) == 0:
                continue
            common = a_adj & adj[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << b) - 1)   # bits b .. n-1 are 1
            cand = common & mask
            if cand:
                low = cand & -cand               # lowest set bit
                c = low.bit_length()            # vertex number (since bit_length is index+1)
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()