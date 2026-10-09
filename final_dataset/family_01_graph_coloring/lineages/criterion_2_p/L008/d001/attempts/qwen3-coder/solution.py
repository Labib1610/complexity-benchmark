import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        # No constraints, assign all to shift 1 for lexicographically smallest
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build graph for constraints
    graph = defaultdict(list)
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Check if any node has odd degree - if so, impossible
    for i in range(1, n + 1):
        if degree[i] % 2 == 1:
            print("NO")
            return
    
    # Try to 2-color the graph (each component must be bipartite)
    color = [-1] * (n + 1)  # -1: unvisited, 0: color 1, 1: color 2
    
    for start in range(1, n + 1):
        if degree[start] > 0 and color[start] == -1:
            # BFS to check if component is bipartite and assign colors
            queue = deque([start])
            color[start] = 0  # Start with color 0 (shift 1)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        # Assign opposite color
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Conflict - not bipartite
                        print("NO")
                        return
    
    # If we get here, a valid assignment exists
    # For lexicographically smallest, assign:
    # color 0 -> shift 1
    # color 1 -> shift 2
    result = []
    for i in range(1, n + 1):
        if color[i] == -1:  # Isolated node (degree 0)
            result.append("1")  # Assign to shift 1 for lex smallest
        else:
            result.append(str(color[i] + 1))  # Convert 0->1, 1->2
    
    print("YES")
    print(" ".join(result))

solve()