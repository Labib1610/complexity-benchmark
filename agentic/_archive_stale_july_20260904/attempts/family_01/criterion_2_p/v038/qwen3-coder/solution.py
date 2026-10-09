import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    graph = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # Color the graph with BFS to check bipartiteness and get lexicographically smallest coloring
    color = [-1] * (n + 1)  # -1: unvisited, 0: color 1, 1: color 2
    
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0  # Start with color 0 (environment 1)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # Convert colors to environments (0->1, 1->2)
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()