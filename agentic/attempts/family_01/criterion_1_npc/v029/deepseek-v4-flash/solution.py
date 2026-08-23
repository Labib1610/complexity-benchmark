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
    for nei in adj[node]:
        if colors[nei] == color:
            return False
    return True

def solve(idx):
    if idx == n:
        return True
    for c in range(1, 4):
        if is_safe(idx, c):
            colors[idx] = c
            if solve(idx + 1):
                return True
            colors[idx] = 0
    return False

if solve(0):
    print("YES")
    print(" ".join(map(str, colors)))
else:
    print("NO")