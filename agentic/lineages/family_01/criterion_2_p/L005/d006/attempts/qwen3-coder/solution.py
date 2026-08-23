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
        u -= 1  # Convert to 0-indexed
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    # For each edge (u,v), we need mult[u] * mult[v] = 2
    # This means exactly one of them should be 2, the other 1
    # So this is a 2-coloring problem where colors represent 1 and 2
    
    # Check if the graph is bipartite
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    
    for start in range(n):
        if color[start] == -1:
            # BFS to check bipartiteness
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If bipartite, construct the solution
    # We want the lexicographically smallest assignment
    # Color 0 -> multiplier 1, Color 1 -> multiplier 2
    result = []
    for i in range(n):
        if color[i] == -1:  # Isolated vertex, assign 1
            result.append("1")
        else:
            result.append("1" if color[i] == 0 else "2")
    
    # Verify the solution
    for u, v in edges:
        mult_u = int(result[u])
        mult_v = int(result[v])
        if mult_u * mult_v != 2:
            print("NO")
            return
    
    print("YES")
    print(" ".join(result))

solve()