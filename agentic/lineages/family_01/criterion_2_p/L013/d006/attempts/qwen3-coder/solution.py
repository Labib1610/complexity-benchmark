import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No dependencies, all can be tier 1 (lexicographically smallest)
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build graph
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Color array: 0 = unvisited, 1 = tier 1, 2 = tier 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS for each component
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1  # Start with tier 1 (for lex smallest)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - current_color  # Flip 1->2, 2->1
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Conflict: same tier for connected nodes
                        print("NO")
                        return
    
    # If we reach here, a valid assignment exists
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    print(" ".join(result))

solve()