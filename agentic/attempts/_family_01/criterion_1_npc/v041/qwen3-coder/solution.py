import sys
from collections import defaultdict

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    n, m = read_ints()
    
    # Build adjacency list representation of the graph
    adj = defaultdict(set)
    for _ in range(m):
        u, v = read_ints()
        adj[u].add(v)
        adj[v].add(u)
    
    # Try to 3-color the graph using backtracking
    colors = [0] * (n + 1)  # colors[i] represents the color of employee i
    
    def is_safe(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def solve(node):
        if node > n:
            return True
        
        for color in range(1, 4):  # Colors 1, 2, 3
            if is_safe(node, color):
                colors[node] = color
                if solve(node + 1):
                    return True
                colors[node] = 0  # Backtrack
        
        return False
    
    if solve(1):
        print("YES")
        print(*colors[1:])
    else:
        print("NO")

if __name__ == "__main__":
    main()