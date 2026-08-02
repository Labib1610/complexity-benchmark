def solve():
    import sys
    from collections import deque
    
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    n, m = map(int, data[0].split())
    
    adj = [[] for _ in range(n + 1)]
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)  # 0 means uncolored, 1 and 2 are colors for shifts
    possible = True
    
    def bfs(start):
        nonlocal possible
        queue = deque([start])
        color[start] = 1  # Start with color 1
        
        while queue and possible:
            current = queue.popleft()
            for neighbor in adj[current]:
                if color[neighbor] == 0:  # Uncolored
                    color[neighbor] = 2 if color[current] == 1 else 1
                    queue.append(neighbor)
                elif color[neighbor] == color[current]:  # Conflict
                    possible = False
                    return
    
    for worker in range(1, n + 1):
        if color[worker] == 0:  # Unvisited worker
            bfs(worker)
            if not possible:
                break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, color[1:])))