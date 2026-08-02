import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_mask = [0] * (n + 1)
    neighbors = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj_mask[u] |= bit_u
        adj_mask[v] |= bit_v
        neighbors[u].append(v)
        neighbors[v].append(u)

    for i in range(1, n + 1):
        neighbors[i].sort()

    for a in range(1, n + 1):
        for b in neighbors[a]:
            if b <= a:
                continue
            common = adj_mask[a] & adj_mask[b]
            # drop bits for nodes <= b
            sub = common >> b
            if sub:
                # lowest set bit
                lsb = sub & -sub
                pos = lsb.bit_length() - 1
                c = b + pos + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()