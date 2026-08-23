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
    
    color = [-1] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0  # Start coloring with 0 (shift 1)
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # Not colored yet
                    color[neighbor] = 1 - color[node]  # Alternate color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict found
                    return False
        return True
    
    for worker in range(1, n + 1):
        if color[worker] == -1:  # Not colored yet
            if not bfs(worker):
                print("NO")
                return
    
    result = [str(c + 1) for c in color[1:]]  # Convert 0/1 to 1/2
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()