import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, m, edges

def solve(n, m, edges):
    # Build adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Color the graph with 3 colors using backtracking
    colors = [-1] * n  # -1 means uncolored
    
    def is_safe(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for color in [1, 2, 3]:
            if is_safe(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = -1
        
        return False
    
    if backtrack(0):
        return "YES", colors
    else:
        return "NO", []

def main():
    n, m, edges = read_input()
    result, coloring = solve(n, m, edges)
    print(result)
    if result == "YES":
        print(' '.join(map(str, coloring)))

if __name__ == "__main__":
    main()