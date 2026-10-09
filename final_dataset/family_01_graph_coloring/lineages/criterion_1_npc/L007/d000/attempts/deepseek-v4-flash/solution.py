n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

colors = [-1] * n

def is_safe(node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def solve(node):
    if node == n:
        return True
    for color in range(3):
        if is_safe(node, color):
            colors[node] = color
            if solve(node + 1):
                return True
            colors[node] = -1
    return False

if solve(0):
    print("YES")
    print(" ".join(str(c + 1) for c in colors))
else:
    print("NO")