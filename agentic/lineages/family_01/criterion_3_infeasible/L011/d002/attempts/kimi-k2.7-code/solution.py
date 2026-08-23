import sys

def solve():
    data = sys.stdin.buffer.read().split()
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

    for i in range(1, n + 1):
        neigh[i].sort()

    for a in range(1, n + 1):
        bits_a = adj_bits[a]
        for b in neigh[a]:
            if b <= a:
                continue
            mask = (bits_a & adj_bits[b]) >> b
            if mask:
                c = b + (mask & -mask).bit_length()
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()