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

    colors = [0] * (n + 1)

    def can_color(node):
        queue = deque([node])
        colors[node] = 1  # Start coloring with color 1
        
        while queue:
            current = queue.popleft()
            current_color = colors[current]

            for neighbor in graph[current]:
                if colors[neighbor] == 0:  # Not colored
                    colors[neighbor] = 3 - current_color if current_color < 3 else 1  # Alternate colors
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:  # Conflict found
                    return False

        return True

    for i in range(1, n + 1):
        if colors[i] == 0:  # If not colored
            if not can_color(i):
                print("NO")
                return

    for i in range(1, n + 1):
        if colors[i] == 0:
            colors[i] = 1  # Assign default color if still 0
    
    # Now we have a valid coloring, we need the lexicographically smallest
    result = []
    for i in range(1, n + 1):
        result.append(colors[i])

    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()