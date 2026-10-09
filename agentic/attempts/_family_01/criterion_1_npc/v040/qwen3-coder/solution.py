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
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color nodes with 3 colors using backtracking
    color = [-1] * n  # -1 means uncolored
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        for c in range(3):  # Colors 0, 1, 2
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1  # Backtrack
                
        return False
    
    # Start backtracking from node 0
    if not backtrack(0):
        return "NO"
    
    # Convert to 1-indexed colors
    result_colors = [str(c + 1) for c in color]
    return "YES\n" + " ".join(result_colors)

def main():
    n, m, edges = read_input()
    result = solve(n, m, edges)
    print(result)

if __name__ == "__main__":
    main()