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
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each edge, the product of power settings must be 2
    # So if one node has power 1, the other must have power 2
    # If one node has power 2, the other must have power 1
    # This is a 2-coloring problem where colors represent power settings
    # Power 1 <-> Color 0, Power 2 <-> Color 1 (or vice versa)
    
    # We need to check if the graph is bipartite
    color = [-1] * (n + 1)  # -1: unvisited, 0: first color, 1: second color
    
    # Check each connected component
    for start in range(1, n + 1):
        if color[start] == -1:
            # BFS to color this component
            queue = deque([start])
            color[start] = 0  # Start with color 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # Not bipartite - impossible to assign powers
                        print("NO")
                        return
    
    # Graph is bipartite, so a solution exists
    # We need the lexicographically smallest assignment
    # That means we want as many 1s as possible at the beginning
    # In our coloring, color 0 should correspond to power 1
    # and color 1 should correspond to power 2 to get lex smallest
    
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()