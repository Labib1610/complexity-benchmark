import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    adj_bits = [0] * (n + 1)
    adj_sorted = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj_bits[u] |= (1 << v)
        adj_bits[v] |= (1 << u)
        adj_sorted[u].append(v)
        adj_sorted[v].append(u)

    for i in range(1, n + 1):
        adj_sorted[i].sort()

    for a in range(1, n + 1):
        for b in adj_sorted[a]:
            if b <= a:
                continue
            common = adj_bits[a] & adj_bits[b]
            hi = common >> (b + 1)
            if hi:
                lsb_pos = (hi & -hi).bit_length() - 1
                c = lsb_pos + b + 1
                print(a, b, c)
                return

solve()
