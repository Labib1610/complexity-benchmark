import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    adj = [0] * n
    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        neighbors = adj[a] >> (a + 1)
        while neighbors:
            low = neighbors & -neighbors
            offset = low.bit_length() - 1
            b = a + 1 + offset

            common = (adj[a] & adj[b]) >> (b + 1)
            if common:
                c = b + 1 + (common & -common).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

            neighbors ^= low

main()