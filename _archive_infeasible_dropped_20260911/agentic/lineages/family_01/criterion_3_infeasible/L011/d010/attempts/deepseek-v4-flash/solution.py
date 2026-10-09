import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u] |= (1 << (v-1))
        adj[v] |= (1 << (u-1))
    
    # Look for triangle lexicographically smallest
    for a in range(1, n+1):
        # neighbors of a with index > a
        neigh_a = adj[a] & ~((1 << a) - 1)  # only b > a
        b_mask = neigh_a
        while b_mask:
            lsb = b_mask & -b_mask
            b = lsb.bit_length()  # 1-based
            # common neighbors of a and b
            common = adj[a] & adj[b]
            # only c > b
            common &= ~((1 << b) - 1)
            if common:
                c = (common & -common).bit_length()
                print(a, b, c)
                return
            b_mask ^= lsb

if __name__ == "__main__":
    solve()