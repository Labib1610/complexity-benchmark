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
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    # The constraint is that for each edge (u,v), tier[u] + tier[v] = 3
    # This means tier[u] != tier[v] (since tiers are 1 or 2)
    # So this is a bipartite graph check
    
    color = {}
    
    # Check if the graph is bipartite
    for start_node in graph:
        if start_node not in color:
            queue = deque([start_node])
            color[start_node] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 3 - color[node]  # Flip between 1 and 2
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If bipartite, construct the lexicographically smallest solution
    # We want nodes not in the graph to be 1 (lexicographically smallest)
    result = []
    for i in range(1, n + 1):
        if i in color:
            result.append(str(color[i]))
        else:
            result.append("1")
    
    print("YES")
    print(" ".join(result))

solve()