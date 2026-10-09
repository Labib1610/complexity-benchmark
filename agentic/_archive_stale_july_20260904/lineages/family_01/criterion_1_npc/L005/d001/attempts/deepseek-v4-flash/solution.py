n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

colors = [0] * n

def is_safe(node, color):
    for neighbor in adj[node]:
        if colors[neighbor] == color:
            return False
    return True

def solve(node):
    if node == n:
        return True
    for color in range(1, 4):
        if is_safe(node, color):
            colors[node] = color
            if solve(node + 1):
                return True
            colors[node] = 0
    return False

if solve(0):
    print("YES")
    print(" ".join(map(str, colors)))
else:
    print("NO")