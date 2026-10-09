import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based, each is an int bitset

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj[u] |= bit_u
        adj[v] |= bit_v

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if not (adj[a] >> (b - 1)) & 1:
                continue          # edge (a,b) missing
            common = adj[a] & adj[b]
            # keep only vertices with index >= b (i.e. number > b)
            mask = ~((1 << b) - 1)
            cand = common & mask
            if cand:
                # lowest set bit -> smallest c
                low = cand & -cand
                c = low.bit_length()   # gives index+1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()