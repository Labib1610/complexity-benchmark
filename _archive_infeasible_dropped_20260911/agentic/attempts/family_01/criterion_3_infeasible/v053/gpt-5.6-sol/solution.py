import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    adj = [0] * n
    p = 2
    for _ in range(m):
        u = data[p]
        v = data[p + 1]
        p += 2
        adj[u - 1] |= 1 << (v - 1)
        adj[v - 1] |= 1 << (u - 1)

    for a in range(1, n - 1):
        neighbors = adj[a - 1]
        higher = neighbors >> a

        while higher:
            lowest = higher & -higher
            b = a + lowest.bit_length()

            common = (neighbors & adj[b - 1]) >> b
            if common:
                c = b + (common & -common).bit_length()
                print(a, b, c)
                return

            higher ^= lowest

if __name__ == "__main__":
    main()