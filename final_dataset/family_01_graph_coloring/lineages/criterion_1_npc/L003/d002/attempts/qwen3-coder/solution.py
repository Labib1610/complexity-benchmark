import sys
from itertools import product

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    
    # For each pair of codes, check if their product is a perfect square
    forbidden = set()
    for i, j in product([1, 2, 3], repeat=2):
        if is_perfect_square(i * j):
            forbidden.add((i, j))
            forbidden.add((j, i))
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all possible colorings with backtracking
    color = [0] * n  # 0 means uncolored
    
    def is_valid(v, c):
        for neighbor in adj[v]:
            if color[neighbor] != 0 and (c, color[neighbor]) in forbidden:
                return False
        return True
    
    def backtrack(v):
        if v == n:
            return True
        
        for c in [1, 2, 3]:
            if is_valid(v, c):
                color[v] = c
                if backtrack(v + 1):
                    return True
                color[v] = 0
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

solve()