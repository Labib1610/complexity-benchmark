n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

colors = [-1] * n

def is_safe(node, c):
    for nei in adj[node]:
        if colors[nei] == c:
            return False
    return True

def solve(node):
    if node == n:
        return True
    for c in range(3):
        if is_safe(node, c):
            colors[node] = c
            if solve(node + 1):
                return True
            colors[node] = -1
    return False

if solve(0):
    print("YES")
    print(" ".join(str(c + 1) for c in colors))
else:
    print("NO")