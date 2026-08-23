import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_bits = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    for a in range(1, n + 1):
        neigh[a].sort()
        for b in neigh[a]:
            if b <= a:
                continue
            inter = adj_bits[a] & adj_bits[b]
            inter >>= b  # remove bits for nodes <= b
            if inter:
                # get index of least significant set bit
                lsb = inter & -inter
                pos = lsb.bit_length() - 1
                c = pos + b + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()