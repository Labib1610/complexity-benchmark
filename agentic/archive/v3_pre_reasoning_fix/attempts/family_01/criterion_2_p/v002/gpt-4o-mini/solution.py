def solve():
    import sys
    from collections import deque
    
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    graph = [[] for _ in range(n + 1)]
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # Not colored
                    color[neighbor] = 1 - color[node]  # Alternate color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict
                    return False
        return True
    
    for i in range(1, n + 1):
        if color[i] == -1:  # Not visited
            if not bfs(i):
                print("NO")
                return
    
    # Prepare the output
    result = [str(color[i] + 1) for i in range(1, n + 1)]
    print("YES")
    print(" ".join(result))