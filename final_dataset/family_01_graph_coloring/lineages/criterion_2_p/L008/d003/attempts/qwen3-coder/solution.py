import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        # No constraints, just assign all 1s (lexicographically smallest)
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For XOR to be 3, we need different values (since 1^2 = 3 in binary)
    # Wait, let's check: 1^2 = 3? No, 1^2 = 3 is wrong. 1^2 = 01^10 = 11 = 3
    # Actually 1^2 = 01 XOR 10 = 11 = 3. Yes, that's correct.
    # So we need adjacent nodes to have different values.
    
    # This is a bipartite graph check. If we can 2-color the graph such that
    # adjacent nodes have different colors, then we can assign 1 and 2.
    
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    
    # Check if the graph is bipartite
    for i in range(n):
        if color[i] == -1:
            # BFS to color component
            queue = deque([i])
            color[i] = 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If bipartite, construct the assignment
    # We want lexicographically smallest, so we prefer color 0 -> value 1
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()