import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, assign all 1s (lexicographically smallest)
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
    
    # For each edge, the sum of oxidation states must be 3 (since mean is 1.5)
    # This means one node gets 1 and the other gets 2 in each edge
    # This is equivalent to a 2-coloring problem (bipartite check)
    
    color = [-1] * n  # -1: unvisited, 0: color A, 1: color B
    
    # Check if graph is bipartite
    for start in range(n):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # Graph is bipartite, construct lexicographically smallest solution
    # Assign 1 to color 0 nodes, 2 to color 1 nodes (to get lex smallest)
    # But we want the lexicographically smallest sequence, so we need to be careful
    
    result = [0] * n
    for i in range(n):
        if color[i] == -1:
            # Isolated node, assign 1 (lexicographically smaller)
            result[i] = 1
        else:
            # color 0 -> 1, color 1 -> 2
            result[i] = 1 if color[i] == 0 else 2
    
    print("YES")
    print(" ".join(map(str, result)))

solve()