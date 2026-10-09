import sys

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    m = next(it)

    adj = [0] * n
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n - 2):
        neighbors = adj[a] >> (a + 1)
        while neighbors:
            lowest = neighbors & -neighbors
            b = a + lowest.bit_length()

            common = (adj[a] & adj[b]) >> (b + 1)
            if common:
                c = b + (common & -common).bit_length()
                print(a + 1, b + 1, c + 1)
                return

            neighbors ^= lowest

main()