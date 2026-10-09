import sys
import sys
import sys

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
    
    # For each edge (u, v), find a common neighbor w such that (u,w) and (v,w) are edges.
    # We need lexicographically smallest triangle.
    # Since n <= 2000, we can iterate over all edges and check common neighbors.
    # To get lexicographically smallest, we can try all possible a from 0 to n-1,
    # then all b > a, then check if there is c > b such that triangle exists.
    # But we need to be efficient.
    
    # Convert adjacency sets to boolean matrix for O(1) checks
    # n <= 2000, so n^2 = 4e6, which is fine.
    # But we can also use bitsets.
    
    # Let's just iterate over all triples? n=2000 -> n^3 too big.
    # Instead, for each edge (u,v), find common neighbors and pick smallest.
    # To get lexicographically smallest triangle, we can try all a from 0 to n-1,
    # then for each b in adj[a] with b > a, find smallest c in adj[a] & adj[b] with c > b.
    # But we need to ensure we get the lexicographically smallest overall.
    
    # Since n is only 2000, we can use bitsets for intersection.
    # Represent adjacency as bitsets (integers with bits).
    
    adj_bits = [0] * n
    for i in range(n):
        mask = 0
        for v in adj[i]:
            mask |= (1 << v)
        adj_bits[i] = mask
    
    # Try all a
    for a in range(n):
        # For each b > a in adj[a]
        for b in range(a+1, n):
            if not (adj_bits[a] >> b) & 1:
                continue
            # Find smallest c > b such that c in adj[a] and c in adj[b]
            common = adj_bits[a] & adj_bits[b]
            # clear bits <= b
            common &= ~((1 << (b+1)) - 1)
            if common:
                c = (common & -common).bit_length() - 1
                print(a+1, b+1, c+1)
                return

if __name__ == "__main__":
    solve()