import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj_bits = [0] * (n + 1)          # bitset of neighbors for each node
    neighbors = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = next(it)
        v = next(it)
        if u == v:
            continue
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        neighbors[u].append(v)
        neighbors[v].append(u)

    for lst in neighbors:
        lst.sort()

    for a in range(1, n - 1):
        neigh_a = adj_bits[a]
        for b in neighbors[a]:
            if b <= a:
                continue
            inter = neigh_a & adj_bits[b]
            mask = ~((1 << b) - 1)          # zero bits for nodes <= b
            inter &= mask
            if inter:
                lsb = inter & -inter
                c = lsb.bit_length()        # node index
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()