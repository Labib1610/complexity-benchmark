import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_mask = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj_mask[u] |= 1 << (v - 1)
        adj_mask[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    for a in range(1, n + 1):
        neigh[a].sort()

    for a in range(1, n + 1):
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj_mask[a] & adj_mask[b]
            mask = common >> b
            if mask:
                tz = (mask & -mask).bit_length() - 1
                c = b + tz + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()