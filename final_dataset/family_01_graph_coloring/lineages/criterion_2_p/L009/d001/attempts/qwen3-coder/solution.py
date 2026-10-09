import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # For XOR to be 3, we need mode1 XOR mode2 = 3
    # Since modes are 1 or 2:
    # 1 XOR 2 = 3 (valid)
    # 1 XOR 1 = 0 (invalid)
    # 2 XOR 2 = 0 (invalid)
    # So connected nodes must have different modes
    
    # This is a bipartite graph check
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    # Check if graph is bipartite
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]  # Flip color (1->2, 2->1)
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If bipartite, construct lexicographically smallest solution
    # We want mode 1 (which is smaller) whenever possible
    result = []
    for i in range(1, n + 1):
        if color[i] == 1:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()