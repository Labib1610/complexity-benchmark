n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

color = [-1] * n

def dfs(node):
    if node == n:
        return True
    used = set()
    for nei in adj[node]:
        if color[nei] != -1:
            used.add(color[nei])
    for c in range(1, 4):
        if c not in used:
            color[node] = c
            if dfs(node + 1):
                return True
            color[node] = -1
    return False

if dfs(0):
    print("YES")
    print(" ".join(str(c) for c in color))
else:
    print("NO")