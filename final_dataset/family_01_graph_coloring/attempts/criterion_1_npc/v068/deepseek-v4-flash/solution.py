import sys

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

colors = [0] * n  # 0 = uncolored, 1-3 for colors

def is_safe(vertex, c):
    for nb in adj[vertex]:
        if colors[nb] == c:
            return False
    return True

def solve(v):
    if v == n:
        return True
    for c in range(1, 4):
        if is_safe(v, c):
            colors[v] = c
            if solve(v + 1):
                return True
            colors[v] = 0
    return False

if solve(0):
    print("YES")
    print(" ".join(map(str, colors)))
else:
    print("NO")