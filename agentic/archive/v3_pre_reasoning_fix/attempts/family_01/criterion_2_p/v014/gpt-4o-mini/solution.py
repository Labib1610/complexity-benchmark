def main():
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

    color = [0] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        color[start] = 1  # Start coloring with 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 2 if current_color == 1 else 1
            
            for neighbor in graph[node]:
                if color[neighbor] == 0:  # Not colored yet
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:  # Conflict found
                    return False
        return True

    for i in range(1, n + 1):
        if color[i] == 0:  # Not visited
            if not bfs(i):
                print("NO")
                return

    # Prepare the output
    print("YES")
    print(" ".join(map(str, color[1:])))

if __name__ == "__main__":
    main()