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
    for nb in adj[node]:
        if color[nb] == c:
            return False
    return True

def solve(idx):
    if idx == n:
        return True
    for c in range(1, 4):
        if is_safe(idx, c):
            color[idx] = c
            if solve(idx + 1):
                return True
            color[idx] = 0
    return False

if solve(0):
    print("YES")
    print(" ".join(map(str, color)))
else:
    print("NO")