n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

colors = [0] * n

def is_safe(node, c):
    for nb in adj[node]:
        if colors[nb] == c:
            return False
    return True

def solve(node):
    if node == n:
        return True
    for c in range(1, 4):
        if is_safe(node, c):
            colors[node] = c
            if solve(node + 1):
                return True
            colors[node] = 0
    return False

if solve(0):
    print("YES")
    print(" ".join(map(str, colors)))
else:
    print("NO")