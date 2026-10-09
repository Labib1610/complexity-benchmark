import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    for a in range(n - 2):
        adj_a = adj[a]
        for b in range(a + 1, n - 1):
            if not (adj_a >> b) & 1:
                continue
            # candidates = neighbors of a that are > b
            candidates = adj_a & ~((1 << (b + 1)) - 1)
            # need b also connected to c
            candidates &= adj[b]
            # smallest c
            if candidates:
                c = (candidates & -c).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()