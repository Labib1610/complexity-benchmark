import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Check if bipartite and find a valid assignment
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    visited = [False] * (n + 1)
    
    # For each connected component
    for start in range(1, n + 1):
        if visited[start]:
            continue
            
        queue = deque([start])
        color[start] = 1
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    color[neighbor] = 3 - color[node]  # Flip color (1->2, 2->1)
                    visited[neighbor] = True
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # Not bipartite - impossible to satisfy constraints
                    print("NO")
                    return
    
    # Verify the solution satisfies all edge constraints
    for u, v in edges:
        if color[u] + color[v] != 3:
            print("NO")
            return
    
    # Output the lexicographically smallest solution
    # Since we want lex smallest, and color 1 corresponds to staffing 1,
    # and color 2 corresponds to staffing 2, we just use the colors directly
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    print(' '.join(result))

solve()