import sys
from collections import defaultdict, deque

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    
    # Check if bipartite using BFS and ensure lexicographically smallest assignment
    for i in range(n):
        if color[i] == -1:
            queue = deque()
            queue.append(i)
            color[i] = 0  # Start with color 0 (phase 1)
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 1 - current_color
                
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] == current_color:
                        print("NO")
                        return
    
    # If we reach here, it's bipartite
    result = [str(color[i] + 1) for i in range(n)]
    print("YES")
    print(" ".join(result))

solve()