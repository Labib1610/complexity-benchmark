import sys

def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj_bits = [0] * n
    neigh = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for a in range(n):
        neigh[a].sort()
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj_bits[a] & adj_bits[b]
            mask = common >> (b + 1)  # shift so that bit 0 corresponds to node b+1
            if mask == 0:
                continue
            # index of lowest set bit in mask
            idx = (mask & -mask).bit_length() - 1
            c = b + 1 + idx
            print(a + 1, b + 1, c + 1)
            return

if __name__ == "__main__":
    solve()