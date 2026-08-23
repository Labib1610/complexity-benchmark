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

    color = [0] * (n + 1)

    def bfs(start):
        queue = deque([start])
        color[start] = 1
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = 3 - color[node]  # Switch between 1 and 2
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    for i in range(1, n + 1):
        if color[i] == 0:  # Not colored yet
            if not bfs(i):
                print("NO")
                return

    print("YES")
    print(" ".join(map(str, color[1:])))

if __name__ == "__main__":
    main()