import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)          # bitset, 0‑based bits for vertices 1..n
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    full_mask = (1 << n) - 1
    for a in range(1, n + 1):
        a_mask = adj[a]
        for b in range(a + 1, n + 1):
            # edge a‑b ?
            if (a_mask >> (b - 1)) & 1 == 0:
                continue
            # common neighbours of a and b
            common = a_mask & adj[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << b) - 1)   # bits with index >= b (0‑based)
            common &= mask
            if common:
                low = common & -common
                c = low.bit_length()            # 1‑based vertex number
                # c is guaranteed > b
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()