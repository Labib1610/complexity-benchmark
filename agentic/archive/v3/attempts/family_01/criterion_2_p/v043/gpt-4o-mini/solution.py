def main():
    import sys
    from collections import defaultdict, deque
    
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    graph = defaultdict(list)
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    
    colors = [-1] * (n + 1)  # -1 means uncolored
    possible = True
    
    def bfs(start):
        nonlocal possible
        queue = deque([start])
        colors[start] = 0  # Start coloring with 0 (which will be represented as 1)
        
        while queue and possible:
            node = queue.popleft()
            current_color = colors[node]
            next_color = 1 - current_color
            
            for neighbor in graph[node]:
                if colors[neighbor] == -1:  # If not colored
                    colors[neighbor] = next_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:  # Conflict
                    possible = False
                    return
    
    for i in range(1, n + 1):
        if colors[i] == -1:
            bfs(i)
            if not possible:
                break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        # Converting 0, 1 to 1, 2 for output
        result = [color + 1 for color in colors[1:]]
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()