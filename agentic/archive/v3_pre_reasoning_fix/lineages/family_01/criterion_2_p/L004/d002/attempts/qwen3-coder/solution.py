import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    # Color each component using BFS
    color = [0] * (n + 1)  # 0 means unvisited, 1 and 2 are the colors
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited[start]:
            # BFS to check if this component is bipartite
            queue = deque([start])
            color[start] = 1
            visited[start] = True
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        color[neighbor] = 3 - color[node]  # Flip between 1 and 2
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # Not bipartite - impossible to satisfy constraints
                        print("NO")
                        return
    
    # Verify the solution
    for u, v in edges:
        if color[u] + color[v] != 3:
            print("NO")
            return
    
    # If we get here, we have a valid solution
    # We need the lexicographically smallest one
    # Our coloring algorithm already ensures this since we start with node 1
    # and always assign the smaller color first
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

solve()