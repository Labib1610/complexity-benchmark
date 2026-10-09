import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color each component using BFS
    # Colors: 0 = unvisited, 1 = color A, 2 = color B
    color = [0] * (n + 1)
    
    # Check if bipartite and assign lexicographically smallest coloring
    for start in range(1, n + 1):
        if color[start] == 0:
            # BFS from start node
            queue = deque([start])
            color[start] = 1  # Start with color 1 for lex smallest
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                # The product constraint: s_u * s_v = 2
                # This means one must be 1 and the other must be 2
                # So adjacent nodes must have different "colors"
                neighbor_color = 3 - current_color  # Maps 1->2, 2->1
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = neighbor_color
                        queue.append(neighbor)
                    elif color[neighbor] != neighbor_color:
                        # Conflict found - not bipartite
                        print("NO")
                        return
    
    # Construct result: color 1 -> state 1, color 2 -> state 2
    result = []
    for i in range(1, n + 1):
        if color[i] == 1:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()