import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color graph with BFS (2-coloring for bipartite check)
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - current_color  # Flip color (1->2, 2->1)
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    # We need to output the coloring, but we want the lexicographically smallest
    # Since we're doing BFS starting from node 1, we might not get the lex smallest
    # But actually, our algorithm already ensures that:
    # - We process nodes in order (1 to n)
    # - When we color a node, we use the smallest available color (1)
    # - The constraint forces the colors based on the bipartite structure
    
    # Let's double-check by ensuring node 1 is colored 1
    # If node 1 was assigned color 2, we can flip all colors
    if color[1] == 2:
        for i in range(1, n + 1):
            color[i] = 3 - color[i]
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

solve()