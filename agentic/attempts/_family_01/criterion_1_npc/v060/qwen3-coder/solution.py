import sys
from collections import defaultdict, deque

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, edges

def solve(n, edges):
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: -1 means unvisited, 0, 1, 2 are colors
    color = [-1] * n
    
    # Check if graph is 3-colorable using BFS
    for start in range(n):
        if color[start] == -1:  # Unvisited component
            queue = deque([start])
            color[start] = 0  # Start with color 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                # Try to color all neighbors with a different color
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        # Assign next available color (0, 1, 2 in cycle)
                        color[neighbor] = (current_color + 1) % 3
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Conflict: adjacent nodes have same color
                        return "NO", []
    
    # Convert 0-based colors to 1-based hall numbers
    result = [str(c + 1) for c in color]
    return "YES", result

def main():
    n, edges = read_input()
    status, assignment = solve(n, edges)
    print(status)
    if status == "YES":
        print(" ".join(assignment))

if __name__ == "__main__":
    main()