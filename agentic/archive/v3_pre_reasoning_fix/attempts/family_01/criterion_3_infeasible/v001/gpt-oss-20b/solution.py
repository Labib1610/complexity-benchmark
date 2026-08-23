import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_bits = [0] * n
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        bit_u = 1 << u
        bit_v = 1 << v
        adj_bits[u] |= bit_v
        adj_bits[v] |= bit_u
        neigh[u].append(v)
        neigh[v].append(u)
    for lst in neigh:
        lst.sort()
    for a in range(n):
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj_bits[a] & adj_bits[b]
            # remove bits <= b
            mask = common >> (b + 1)
            if mask:
                low = mask & -mask
                c = b + 1 + (low.bit_length() - 1)
                # output 1-based indices
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()