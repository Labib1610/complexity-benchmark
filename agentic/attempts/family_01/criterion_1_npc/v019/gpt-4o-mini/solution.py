def solve():
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
    
    color = [0] * (n + 1)  # 0 means uncolored, 1, 2, 3 are the colors
    
    def bfs(start):
        queue = deque([start])
        color[start] = 1  # Start coloring with 1
        
        while queue:
            node = queue.popleft()
            next_color = 1
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    while next_color == color[node] or any(color[neigh] == next_color for neigh in graph[neighbor]):
                        next_color += 1
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    for i in range(1, n + 1):
        if color[i] == 0:  # Not colored yet
            if not bfs(i):
                print("NO")
                return
    
    # Check for lexicographically smallest assignment
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1

    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))