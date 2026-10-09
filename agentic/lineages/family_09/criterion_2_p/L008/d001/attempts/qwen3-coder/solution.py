import sys
from collections import defaultdict, deque

def solve():
    n, m, k = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Check if the graph is bipartite and get the two sets
    color = {}
    set_a = []
    set_b = []
    
    # BFS for bipartite check and coloring
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited[start]:
            queue = deque([start])
            color[start] = 0
            visited[start] = True
            set_a.append(start)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        color[neighbor] = 1 - current_color
                        if color[neighbor] == 0:
                            set_a.append(neighbor)
                        else:
                            set_b.append(neighbor)
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # This should not happen according to problem statement
                        # but let's handle it anyway
                        return "NO"
    
    # Choose the larger set
    if len(set_a) >= k:
        print("YES")
        print(*set_a[:k])
    elif len(set_b) >= k:
        print("YES")
        print(*set_b[:k])
    else:
        print("NO")

solve()