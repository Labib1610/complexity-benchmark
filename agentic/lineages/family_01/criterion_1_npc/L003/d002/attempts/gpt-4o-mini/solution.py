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
        color[start] = 0  # Start coloring with phase 1 (0 in 0-index)
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # Not colored
                    color[neighbor] = (color[node] + 1) % 3  # Color with the next phase
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict found
                    return False
        return True

    for i in range(1, n + 1):
        if color[i] == -1:  # Not colored
            if not bfs(i):
                print("NO")
                return

    # Prepare the output
    result = [(c + 1) for c in color[1:]]  # Convert 0-index to 1-index
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()