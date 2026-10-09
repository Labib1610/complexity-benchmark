n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

colors = [-1] * n

def can_color(node, color):
    for nei in adj[node]:
        if colors[nei] == color:
            return False
    return True

def solve(idx):
    if idx == n:
        return True
    for c in range(3):
        if can_color(idx, c):
            colors[idx] = c
            if solve(idx + 1):
                return True
            colors[idx] = -1
    return False

if solve(0):
    print("YES")
    print(" ".join(str(c + 1) for c in colors))
else:
    print("NO")