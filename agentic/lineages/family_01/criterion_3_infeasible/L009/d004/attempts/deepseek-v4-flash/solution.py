import sys
import sys
from collections import deque

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
    
    # For each vertex, store its adjacency as a bitmask if possible, but n up to 2000, so use bitset as integer
    # We'll use Python integers as bitsets
    adj_bitset = [0] * n
    for i in range(n):
        mask = 0
        for v in adj[i]:
            mask |= (1 << v)
        adj_bitset[i] = mask
    
    # For each edge (u,v), find a common neighbor w such that (u,v,w) forms a triangle
    # We need exactly 3 edges among the trio, so it's a triangle.
    # We'll iterate over edges and check common neighbors.
    for u, v in edges:
        common = adj_bitset[u] & adj_bitset[v]
        if common:
            # get the smallest common neighbor
            w = (common & -common).bit_length() - 1
            # output sorted
            a, b, c = sorted([u+1, v+1, w+1])
            print(a, b, c)
            return

if __name__ == "__main__":
    solve()