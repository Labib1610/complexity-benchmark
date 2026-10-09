import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
    
    for a in range(1, n + 1):
        # iterate over neighbors b > a
        mask_b = adj[a] >> a  # shift to ignore bits <= a
        while mask_b:
            # get lowest set bit
            lsb = mask_b & -mask_b
            b = a + (lsb.bit_length())  # because we shifted by a
            # Actually careful: after shifting by a, bit position 0 corresponds to vertex a+1
            # Let's do it differently:
            # We'll iterate over bits directly
            break
        # Better: iterate over b in neighbors of a with b > a
        for b in range(a + 1, n + 1):
            if (adj[a] >> (b - 1)) & 1:
                common = adj[a] & adj[b]
                # find smallest c > b
                # clear bits <= b
                common &= ~((1 << b) - 1)
                if common:
                    c = (common & -common).bit_length()  # 1-indexed
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()