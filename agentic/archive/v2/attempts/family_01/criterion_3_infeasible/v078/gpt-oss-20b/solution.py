import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj_bits = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = next(it)
        v = next(it)
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        if v > u:
            neigh[u].append(v)
        else:
            neigh[v].append(u)

    for i in range(1, n + 1):
        neigh[i].sort()

    for a in range(1, n + 1):
        for b in neigh[a]:
            common = adj_bits[a] & adj_bits[b]
            mask = common >> b
            if mask:
                low = mask & -mask
                pos = low.bit_length() - 1
                c = b + pos + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    main()