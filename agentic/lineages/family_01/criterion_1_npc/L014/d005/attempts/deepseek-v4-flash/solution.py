n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [0] * n

def is_safe(node, c):
    for nei in adj[node]:
        if color[nei] == c:
            return False
    return True

def solve(node):
    if node == n:
        return True
    for c in range(1, 4):
        if is_safe(node, c):
            color[node] = c
            if solve(node + 1):
                return True
            color[node] = 0
    return False

if solve(0):
    print("YES")
    print(" ".join(str(c) for c in color))
else:
    print("NO")