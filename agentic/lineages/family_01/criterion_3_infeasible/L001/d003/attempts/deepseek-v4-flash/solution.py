import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # For each edge (u, v), find the smallest w > v such that w is connected to both u and v
    # Since we need lexicographically smallest triple, we can iterate over a from 1 to n
    # and for each a, iterate over its neighbors b > a, and check for common neighbors c > b
    # But n is up to 2000, so O(n^3) is too slow.
    # Instead, we can use bitsets for adjacency.
    
    # Convert adjacency to bitsets
    adj_bitset = [0] * (n + 1)
    for i in range(1, n + 1):
        mask = 0
        for v in adj[i]:
            mask |= (1 << v)
        adj_bitset[i] = mask
    
    # Iterate over a
    for a in range(1, n + 1):
        # For each b > a that is adjacent to a
        for b in range(a + 1, n + 1):
            if not (adj_bitset[a] >> b) & 1:
                continue
            # Common neighbors of a and b that are > b
            common = adj_bitset[a] & adj_bitset[b]
            # Clear bits <= b
            if b + 1 <= n:
                mask = ((1 << (b + 1)) - 1)
                common &= ~mask
            if common:
                # Find smallest set bit
                c = (common & -common).bit_length() - 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()