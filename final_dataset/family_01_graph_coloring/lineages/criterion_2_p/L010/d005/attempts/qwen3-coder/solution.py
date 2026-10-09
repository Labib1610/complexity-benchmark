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
    
    # Each edge must satisfy s_u^2 + s_v^2 = 5
    # Since s_u, s_v ∈ {1, 2}, we have:
    # 1^2 + 1^2 = 2  (invalid)
    # 1^2 + 2^2 = 5  (valid)
    # 2^2 + 1^2 = 5  (valid)
    # 2^2 + 2^2 = 8  (invalid)
    # So each pair must have one 1 and one 2
    
    # This is a bipartite graph problem
    # Color the graph with 2 colors such that adjacent nodes have different colors
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    # Check if the graph is bipartite
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]  # Flip color (1->2, 2->1)
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # If bipartite, construct the solution
    # Assign mode 1 to color 1 nodes, mode 2 to color 2 nodes
    result = []
    for i in range(1, n + 1):
        if color[i] == 1:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()