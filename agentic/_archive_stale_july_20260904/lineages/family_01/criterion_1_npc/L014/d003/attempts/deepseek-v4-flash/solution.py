n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [0] * n

def is_safe(v, c):
    for u in adj[v]:
        if color[u] == c:
            return False
    return True

def solve(v):
    if v == n:
        return True
    for c in range(1, 4):
        if is_safe(v, c):
            color[v] = c
            if solve(v + 1):
                return True
            color[v] = 0
    return False

if solve(0):
    print("YES")
    print(" ".join(map(str, color)))
else:
    print("NO")