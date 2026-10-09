import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, m, edges

def is_bipartite(graph, n):
    """Check if graph is bipartite and return coloring if so"""
    color = [-1] * n
    
    for start in range(n):
        if color[start] == -1:
            stack = [start]
            color[start] = 0
            
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        stack.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False, None
    return True, color

def solve():
    n, m, edges = read_input()
    
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all 3 colors for each component using backtracking
    colors = [0] * n  # 0 means unassigned
    
    def is_valid(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()