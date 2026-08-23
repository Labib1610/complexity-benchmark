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
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # Color assignment: 0 -> unvisited, 1 -> state 1, 2 -> state 2
    color = [0] * n
    queue = deque()
    
    # Check each component
    for start in range(n):
        if color[start] == 0:
            color[start] = 1
            queue.append(start)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - current_color  # Switches 1->2, 2->1
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # Verify solution
    for u, v in edges:
        if color[u] == color[v]:
            print("NO")
            return
    
    # Convert colors to states (1 and 2)
    result = []
    for c in color:
        if c == 1:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

solve()