import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n                     # bitset for each vertex

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        a_adj = adj[a]
        for b in range(a + 1, n):
            # edge (a,b) ?
            if (a_adj >> b) & 1 == 0:
                continue
            common = a_adj & adj[b]
            # keep only vertices > b
            mask = common & ~((1 << (b + 1)) - 1)
            if mask:
                low = mask & -mask               # lowest set bit
                c = low.bit_length() - 1
                # output 1‑based, already a<b<c
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()