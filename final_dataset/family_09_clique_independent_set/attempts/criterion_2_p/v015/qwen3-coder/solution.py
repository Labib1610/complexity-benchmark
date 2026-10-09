import sys
from collections import defaultdict, deque

def solve():
    n, m, k = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # If no edges, we can select any k nodes
    if m == 0:
        print("YES")
        print(*range(1, k + 1))
        return
    
    # Bipartite coloring to separate into two tiers
    color = [-1] * (n + 1)
    tier1 = []
    tier2 = []
    
    # Check if graph is bipartite and find the two tiers
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                if color[node] == 0:
                    tier1.append(node)
                else:
                    tier2.append(node)
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # This shouldn't happen according to problem statement
                        print("NO")
                        return
    
    # Check if we can take k nodes
    if k <= len(tier1):
        print("YES")
        print(*tier1[:k])
    elif k <= len(tier2):
        print("YES")
        print(*tier2[:k])
    else:
        print("NO")

solve()