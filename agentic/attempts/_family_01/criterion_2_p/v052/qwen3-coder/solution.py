import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                neighbor_color = 3 - current_color  # 1 -> 2, 2 -> 1
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = neighbor_color
                        queue.append(neighbor)
                    elif color[neighbor] != neighbor_color:
                        print("NO")
                        return
    
    # If bipartite, construct lexicographically smallest solution
    # We want nodes with no neighbors to be assigned 1 (to ensure lex smallest)
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append(1)
        else:
            result.append(color[i])
    
    print("YES")
    print(" ".join(map(str, result)))

solve()