import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    adj = [0] * (n + 1)
    pos = 2
    for _ in range(m):
        u, v = data[pos], data[pos + 1]
        pos += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full_mask = (1 << (n + 1)) - 2
    greater = [full_mask & (-1 << (i + 1)) for i in range(n + 1)]

    for a in range(1, n + 1):
        neighbors = adj[a] & greater[a]
        while neighbors:
            bit_b = neighbors & -neighbors
            b = bit_b.bit_length() - 1

            common = adj[a] & adj[b] & greater[b]
            if common:
                bit_c = common & -common
                c = bit_c.bit_length() - 1
                print(a, b, c)
                return

            neighbors ^= bit_b

if __name__ == "__main__":
    main()