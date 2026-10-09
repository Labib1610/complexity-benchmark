import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    constraints = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        constraints.append((u-1, v-1))  # Convert to 0-indexed
    return n, m, constraints

def solve(n, m, constraints):
    # Create adjacency list for conflicts (modules that can't have the same environment)
    adj = defaultdict(set)
    for u, v in constraints:
        adj[u].add(v)
        adj[v].add(u)
    
    # Try to color the graph with 3 colors
    # This is essentially a 3-coloring problem
    colors = [0] * n  # 0 means unassigned, 1, 2, 3 are the actual colors
    
    def is_safe(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
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
                colors[node] = 0  # Backtrack
                
        return False
    
    # Start backtracking from node 0
    if backtrack(0):
        return "YES", colors
    else:
        return "NO", []

def main():
    n, m, constraints = read_input()
    result, assignment = solve(n, m, constraints)
    print(result)
    if result == "YES":
        print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()