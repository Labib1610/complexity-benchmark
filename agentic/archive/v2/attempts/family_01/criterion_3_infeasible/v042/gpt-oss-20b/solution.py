import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    fullmask = (1 << n) - 1

    for a in range(1, n - 1):
        neigh_a = adj[a]
        for b in range(a + 1, n + 1):
            if neigh_a & (1 << (b - 1)):
                higher = fullmask & ~((1 << b) - 1)
                mask = neigh_a & adj[b] & higher
                if mask:
                    lsb = mask & -mask
                    c = lsb.bit_length()  # 1‑based index
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()