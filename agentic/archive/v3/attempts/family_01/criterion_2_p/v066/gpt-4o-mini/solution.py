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
    
    color = [0] * (n + 1)  # 0 means uncolored, 1 and 2 will be our colors
    is_bipartite = True
    
    def bfs(start):
        nonlocal is_bipartite
        queue = deque([start])
        color[start] = 1  # Start coloring with 1
        
        while queue and is_bipartite:
            node = queue.popleft()
            current_color = color[node]
            next_color = 2 if current_color == 1 else 1
            
            for neighbor in graph[node]:
                if color[neighbor] == 0:  # If uncolored
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:  # Conflict found
                    is_bipartite = False
                    return
                
    for i in range(1, n + 1):
        if color[i] == 0:  # Not visited
            bfs(i)
            if not is_bipartite:
                break
    
    if not is_bipartite:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, color[1:])))
        
if __name__ == "__main__":
    main()