import sys
from collections import defaultdict

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n

def can_assign_modes(n, edges):
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Colors: 1, 2, 3
    # For each edge, product of colors should not be a perfect square
    # Perfect squares from products of {1,2,3}: 1*1=1, 2*2=4, 3*3=9
    forbidden = {(1,1), (2,2), (3,3)}
    
    # Try all possible colorings using backtracking
    color = [0] * (n + 1)  # color[i] is the color of node i
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] != 0:  # if already colored
                if (c, color[neighbor]) in forbidden or (color[neighbor], c) in forbidden:
                    return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False
    
    if backtrack(1):
        return True, color[1:]
    else:
        return False, []

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    
    possible, coloring = can_assign_modes(n, edges)
    
    if possible:
        print("YES")
        print(" ".join(map(str, coloring)))
    else:
        print("NO")

if __name__ == "__main__":
    main()