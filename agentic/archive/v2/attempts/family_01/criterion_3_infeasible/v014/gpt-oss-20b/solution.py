import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [0] * (n + 1)
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        neigh_mask = adj[a]
        for b in range(a + 1, n + 1):
            if (neigh_mask >> (b - 1)) & 1:
                common = adj[a] & adj[b]
                mask = common >> b
                if mask:
                    lsb = mask & -mask
                    pos = lsb.bit_length() - 1
                    c = b + pos + 1
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()