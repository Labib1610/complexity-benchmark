n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

adj = [[] for _ in range(n)]
for u, v in edges:
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n

def dfs(node):
    for c in range(3):
        ok = True
        for nei in adj[node]:
            if color[nei] == c:
                ok = False
                break
        if ok:
            color[node] = c
            for nei in adj[node]:
                if color[nei] == -1:
                    if not dfs(nei):
                        ok = False
                        break
            if ok:
                return True
            color[node] = -1
    return False

possible = True
for i in range(n):
    if color[i] == -1:
        if not dfs(i):
            possible = False
            break

if not possible:
    print("NO")
else:
    print("YES")
    print(" ".join(str(c + 1) for c in color))