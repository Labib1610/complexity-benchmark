import sys, bisect

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_bits = [0] * n
    adj_lists = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        adj_lists[u].append(v)
        adj_lists[v].append(u)

    for lst in adj_lists:
        lst.sort()

    for a in range(n):
        bits_a = adj_bits[a]
        neigh = adj_lists[a]
        idx = bisect.bisect_right(neigh, a)
        for b in neigh[idx:]:
            mask = bits_a & adj_bits[b]
            mask &= ~((1 << (b + 1)) - 1)
            if mask:
                lsb = mask & -mask
                c = lsb.bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()