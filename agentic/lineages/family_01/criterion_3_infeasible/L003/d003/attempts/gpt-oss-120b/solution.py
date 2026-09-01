import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_bits = [0] * n          # bitset for each vertex
    neigh = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        # set bits
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for i in range(n):
        neigh[i].sort()

    for a in range(n):
        ba = adj_bits[a]
        for b in neigh[a]:
            if b <= a:
                continue
            common = ba & adj_bits[b]
            # delete bits <= b
            t = common >> (b + 1)
            if t:
                low = t & -t               # lowest set bit
                c = (b + 1) + (low.bit_length() - 1)
                # output in 1‑based, increasing order
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()