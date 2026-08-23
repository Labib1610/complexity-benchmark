import sys
import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # For each vertex, we need to find a triangle with smallest lexicographic order.
    # Since n <= 2000, we can try all pairs (u, v) with u < v and check common neighbors.
    # But we need lexicographically smallest triangle.
    # We'll iterate over possible smallest vertex a, then second smallest b, then find smallest c.
    
    # Precompute adjacency matrix as bitsets for fast intersection
    # But n=2000, bitset of 2000 bits is fine.
    # We'll use Python integers as bitsets.
    adj_bits = [0] * n
    for i in range(n):
        mask = 0
        for j in adj[i]:
            mask |= (1 << j)
        adj_bits[i] = mask
    
    # Iterate over a
    for a in range(n - 2):
        # For each b > a
        for b in range(a + 1, n - 1):
            if not (adj_bits[a] >> b) & 1:
                continue
            # common neighbors of a and b
            common = adj_bits[a] & adj_bits[b]
            # clear bits <= b to ensure c > b
            if b + 1 < n:
                common &= ~((1 << (b + 1)) - 1)
            if common:
                # find smallest set bit
                c = (common & -common).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()