import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, edges

def solve(n, edges):
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to color the graph with 3 colors
    # Color 0: uncolored, 1, 2, 3: colors
    colors = [0] * n
    
    def is_safe(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        for color in range(1, 4):
            if is_safe(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0
                
        return False
    
    if backtrack(0):
        return "YES\n" + " ".join(map(str, colors))
    else:
        return "NO"

def main():
    n, edges = read_input()
    result = solve(n, edges)
    print(result)

if __name__ == "__main__":
    main()