import sys
import sys
sys.setrecursionlimit(1_000_000)

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
    
    # For each edge (u,v), find a common neighbor w such that u<v<w or any order,
    # but we need sorted triple. We'll just find any triangle and then pick lexicographically smallest.
    
    # Since n <= 2000, we can do O(n^3) in worst case? No, too slow.
    # But we can do O(n^3 / 64) using bitsets.
    
    # Convert adjacency to bitsets
    bits = [0] * n
    for i in range(n):
        mask = 0
        for j in adj[i]:
            mask |= (1 << j)
        bits[i] = mask
    
    best = None
    # Try all pairs (i,j) with i<j
    for i in range(n):
        bi = bits[i]
        for j in range(i+1, n):
            if not (bi >> j) & 1:
                continue
            # common neighbors of i and j
            common = bi & bits[j]
            # clear bits <= j to avoid duplicates? Actually we need any common neighbor k != i,j
            common &= ~((1 << (j+1)) - 1)  # only consider k > j to avoid duplicate triples
            while common:
                lsb = common & -common
                k = (lsb.bit_length() - 1)
                common -= lsb
                triple = (i+1, j+1, k+1)
                if best is None or triple < best:
                    best = triple
        if best is not None:
            # Since we iterate i from small to large, the first found is lexicographically smallest
            # But we need to be careful: we might find a triple with larger i but smaller second/third?
            # Actually we iterate i increasing, and for each i, j increasing, so first found is lexicographically smallest.
            print(*best)
            return

if __name__ == "__main__":
    solve()