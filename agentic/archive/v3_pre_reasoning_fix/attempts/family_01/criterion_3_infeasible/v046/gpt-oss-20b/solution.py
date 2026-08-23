import sys

def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n - 2):
        for b in range(a + 1, n - 1):
            # check if a and b are connected
            if (adj[a] >> b) & 1:
                common = adj[a] & adj[b]
                # consider only neighbors with index > b
                mask = common >> (b + 1)
                if mask:
                    lsb = mask & -mask
                    offset = lsb.bit_length() - 1
                    c = b + offset + 2  # convert to 1‑based index
                    print(a + 1, b + 1, c)
                    return

if __name__ == "__main__":
    solve()