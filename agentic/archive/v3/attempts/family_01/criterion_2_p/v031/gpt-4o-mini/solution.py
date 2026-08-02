def main():
    import sys
    from collections import deque

    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        graph[u].append(v)
        graph[v].append(u)
        idx += 2
    
    color = [-1] * (n + 1)  # -1 means uncolored
    possible = True
    
    def bfs(start):
        nonlocal possible
        queue = deque([start])
        color[start] = 0  # Start coloring with 0 (channel 1)
        
        while queue and possible:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # Not colored
                    color[neighbor] = 1 - color[node]  # Alternate color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict
                    possible = False
                    return
    
    for i in range(1, n + 1):
        if color[i] == -1:  # Not colored yet
            bfs(i)
            if not possible:
                break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        # Convert color from 0, 1 to 1, 2 for the output
        result = [c + 1 for c in color[1:]]
        print(" ".join(map(str, result)))

main()