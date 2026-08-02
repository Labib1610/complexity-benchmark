def is_valid_coloring(graph, colors):
    for u in range(len(colors)):
        for v in graph[u]:
            if colors[u] == colors[v]:
                return False
    return True

def backtrack(graph, n, colors, pos):
    if pos == n:
        return is_valid_coloring(graph, colors)
    
    for color in range(1, 4):
        colors[pos] = color
        if backtrack(graph, n, colors, pos + 1):
            return True
    colors[pos] = 0
    return False

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    graph = [[] for _ in range(n)]
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    
    colors = [0] * n
    if not backtrack(graph, n, colors, 0):
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, colors)))

solve()