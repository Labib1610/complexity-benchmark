import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, all relays can be assigned band 1
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    # Color array: -1 unvisited, 0 = band 1, 1 = band 2
    color = [-1] * n
    visited = [False] * n
    
    # Check if bipartite using BFS
    for start in range(n):
        if visited[start]:
            continue
            
        queue = deque([start])
        color[start] = 0
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    print("NO")
                    return
    
    # Verify the constraint for all edges
    for u, v in edges:
        if (color[u] + 1) * (color[v] + 1) != 2:  # Bands are 1-indexed (color 0->band 1, color 1->band 2)
            print("NO")
            return
    
    # Convert colors to bands (1-indexed)
    bands = [str(color[i] + 1) for i in range(n)]
    
    print("YES")
    print(" ".join(bands))

solve()