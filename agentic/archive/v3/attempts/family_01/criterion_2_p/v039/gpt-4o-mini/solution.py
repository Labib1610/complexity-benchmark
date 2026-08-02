def schedule_research_facility():
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

    color = [-1] * (n + 1)  # -1 means uncolored, 0 for lab 1, 1 for lab 2

    def bfs(start):
        queue = deque([start])
        color[start] = 0  # Start coloring with lab 1
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # If not colored
                    color[neighbor] = 1 - color[node]  # Alternate color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict found
                    return False
        return True

    for researcher in range(1, n + 1):
        if color[researcher] == -1:  # Not colored yet
            if not bfs(researcher):
                print("NO")
                return

    # Prepare output
    result = [str(color[i] + 1) for i in range(1, n + 1)]
    print("YES")
    print(" ".join(result))

schedule_research_facility()