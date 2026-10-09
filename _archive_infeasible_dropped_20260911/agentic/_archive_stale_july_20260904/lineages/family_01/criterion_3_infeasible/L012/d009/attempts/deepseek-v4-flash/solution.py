import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(1, n + 1):
        # b must be > a and adjacent to a
        bmask = adj[a] & ~((1 << (a + 1)) - 1)
        while bmask:
            low = bmask & -bmask
            b = low.bit_length() - 1
            bmask ^= low

            # c must be > b and adjacent to both a and b
            cmask = adj[a] & adj[b] & ~((1 << (b + 1)) - 1)
            if cmask:
                lowc = cmask & -cmask
                c = lowc.bit_length() - 1
                print(a, b, c)
                return

if __name__ == "__main__":
    main()