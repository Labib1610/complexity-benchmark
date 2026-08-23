def can_color(n, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * (n + 1)

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == c:
                return False
            if color[neighbor] == 0 and not dfs(neighbor, 6 - c - color[node]):
                return False
        return True

    for i in range(1, n + 1):
        if color[i] == 0:
            if not dfs(i, 1):
                return False, []
    
    return True, color[1:]

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n, m = map(int, data[0].split())
    edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

    valid, colors = can_color(n, edges)

    if not valid:
        print("NO")
    else:
        print("YES")
        # Adjust colors to be in the range 1 to 3
        for i in range(n):
            if colors[i] == 1:
                colors[i] = 1
            elif colors[i] == 2:
                colors[i] = 2
            else:
                colors[i] = 3
        print(' '.join(map(str, colors)))

if __name__ == "__main__":
    main()