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
    
    # Color assignment: 0 means unassigned, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]  # Switch between 1 and 2
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    print("YES")
    
    # For lexicographically smallest assignment, we need to ensure nodes are processed in order
    # We can just output the color assignment as is, since we started BFS from node 1
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append("1")  # Isolated node, assign 1
        else:
            result.append(str(color[i]))
    
    print(" ".join(result))

solve()