import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color graph with 2 colors (Bipartite check)
    color = [-1] * n  # -1: unvisited, 0: color A, 1: color B
    visited = [False] * n
    
    for i in range(n):
        if color[i] == -1:  # Unvisited component
            queue = deque([i])
            color[i] = 0
            
            while queue:
                node = queue.popleft()
                if visited[node]:
                    continue
                visited[node] = True
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # Verify all edges satisfy constraint (product = 2)
    for u, v in edges:
        c1 = 1 if color[u] == 0 else 2
        c2 = 1 if color[v] == 0 else 2
        if c1 * c2 != 2:
            print("NO")
            return
    
    # Construct result: assign 1 to color 0, 2 to color 1 for lex smallest
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()