import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, all positions can be 1
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
    
    # For each edge (u,v), we need pos[u] + pos[v] = 3
    # So if pos[u] = 1, then pos[v] = 2, and vice versa
    # This is a bipartite graph coloring problem
    
    color = [-1] * n  # -1: uncolored, 0: position 1, 1: position 2
    
    # Check if the graph is bipartite
    for i in range(n):
        if color[i] == -1:
            # BFS to color the component
            queue = deque([i])
            color[i] = 0  # Start with color 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        print("NO")
                        return
    
    # Verify the solution satisfies all constraints
    for u, v in edges:
        if color[u] + color[v] != 1:  # 0+1=1, which corresponds to positions 1+2=3
            print("NO")
            return
    
    # The solution is valid. To get the lexicographically smallest,
    # we prefer color 0 (position 1) over color 1 (position 2)
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()