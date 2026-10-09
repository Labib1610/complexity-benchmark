n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [0] * n

def dfs(node):
    for c in range(1, 4):
        ok = True
        for nei in adj[node]:
            if color[nei] == c:
                ok = False
                break
        if ok:
            color[node] = c
            if node == n - 1:
                return True
            if dfs(node + 1):
                return True
            color[node] = 0
    return False

if dfs(0):
    print("YES")
    print(" ".join(map(str, color)))
else:
    print("NO")